import streamlit as st
import google.generativeai as genai
import folium
from streamlit_folium import st_folium
import json
import time

# --- CONFIGURATION ---
# SECURE WAY: Load from st.secrets (requires .streamlit/secrets.toml file)
# If running locally without secrets file, you can use os.environ or input it manually
try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
except:
    # Fallback for testing ONLY (Do not commit this to GitHub!)
    GOOGLE_API_KEY = "your-google-api-key-here"

genai.configure(api_key=GOOGLE_API_KEY)

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Student AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS (Kept same as your code)
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; color: #4F8BF9; text-align: center; font-weight: 700; }
    .sub-header { font-size: 1.2rem; color: #666; text-align: center; margin-bottom: 2rem; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #4F8BF9; color: white; font-weight: 600; }
    .cost-tag { background-color: #e6f4ea; color: #1e8e3e; padding: 4px 8px; border-radius: 12px; font-weight: bold; font-size: 0.9rem; }
</style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if 'trip_data' not in st.session_state:
    st.session_state['trip_data'] = None
if 'current_destination' not in st.session_state:
    st.session_state['current_destination'] = None

# --- SIDEBAR INPUTS ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/201/201623.png", width=80)
    st.title("Plan Your Trip")
    st.markdown("Tell us your preferences, and AI will do the rest.")
    
    with st.form("trip_form"):
        destination = st.text_input("📍 Destination", "Goa", placeholder="e.g., Paris, Kyoto")
        col1, col2 = st.columns(2)
        with col1:
            budget = st.number_input("💰 Budget", min_value=100, value=5000, step=100)
        with col2:
            currency = st.selectbox("Currency", ["INR", "USD", "EUR"])
        
        days = st.slider("📅 Duration (Days)", 1, 14, 3)
        preferences = st.multiselect(
            "❤️ Interests", 
            ["Adventure", "History", "Food", "Nightlife", "Nature", "Relaxation", "Art"],
            ["Adventure", "Food"]
        )
        
        submitted = st.form_submit_button("✨ Generate Smart Itinerary")

# --- AI GENERATION LOGIC (FIXED) ---
def get_itinerary(dest, budget, curr, days, prefs):
    prompt = f"""
    Act as an expert travel agent for students. Plan a {days}-day trip to {dest} with a strict budget of {budget} {curr}.
    The user is interested in: {', '.join(prefs)}.
    
    CRITICAL INSTRUCTIONS:
    1. Focus on free or cheap activities suitable for students.
    2. Suggest budget-friendly transport and food options explicitly.
    3. Output the response strictly as valid JSON. No markdown formatting.
    
    JSON Structure required:
    {{
      "trip_name": "A Creative and Catchy Title for the Trip",
      "summary": "A 2-sentence enthusiastic summary of the trip vibe.",
      "total_estimated_cost": "Total Cost Value (e.g., 'Is approx 4500 INR')",
      "itinerary": [
        {{
          "day": 1,
          "day_theme": "Theme for the day (e.g., Beach Hopping)",
          "activities": [
            {{ "time": "Morning (9:00 AM)", "activity": "Name of Activity", "cost": "Cost (e.g., Free or 200 INR)", "lat": 15.123, "lon": 73.456, "desc": "A compelling 2-sentence description of why a student would love this." }},
            {{ "time": "Afternoon (1:00 PM)", "activity": "Lunch Spot Name", "cost": "Approx Cost", "lat": 15.125, "lon": 73.458, "desc": "Description of food and vibe." }}
          ]
        }}
      ]
    }}
    """
    try:
        # UPDATED: Using the Experimental model which is available in your list
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        # Call API
        response = model.generate_content(prompt)
        
        # Clean response
        text = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(text)
        
    except Exception as e:
        # Print the specific error to the UI so you can see it
        st.error(f"AI Error: {e}") 
        return None

# --- MAP VISUALIZATION LOGIC ---
def plot_map(data):
    if not data or 'itinerary' not in data:
        return folium.Map(location=[20, 0], zoom_start=2)

    start_lat, start_lon = 20.0, 0.0
    # Center map on first valid coordinate
    for day in data['itinerary']:
        for act in day['activities']:
            if act.get('lat') and act.get('lon'):
                start_lat, start_lon = act['lat'], act['lon']
                break
        if start_lat != 20.0: break
            
    m = folium.Map(location=[start_lat, start_lon], zoom_start=11, tiles='cartodbpositron')
    colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FFD700']
    
    for day_idx, day in enumerate(data['itinerary']):
        day_color = colors[day_idx % len(colors)]
        group = folium.FeatureGroup(name=f"Day {day['day']}: {day.get('day_theme', '')}").add_to(m)
        
        coordinates = []
        for act in day['activities']:
            if act.get('lat') and act.get('lon'):
                coords = [act['lat'], act['lon']]
                coordinates.append(coords)
                
                popup_html = f"""
                <div style='font-family:sans-serif; min-width:200px'>
                    <h4 style='margin:0; color:{day_color}'>{act['activity']}</h4>
                    <p style='margin:5px 0; font-weight:bold'>{act['time']}</p>
                    <p style='margin:5px 0; color:green'>💰 {act['cost']}</p>
                    <p style='font-size:0.9em'>{act['desc']}</p>
                </div>
                """
                folium.Marker(
                    coords,
                    popup=folium.Popup(popup_html, max_width=300),
                    icon=folium.Icon(color='white', icon_color=day_color, icon='map-marker', prefix='fa')
                ).add_to(group)
        
        if len(coordinates) > 1:
            folium.PolyLine(coordinates, color=day_color, weight=4, opacity=0.7, dash_array='10, 10').add_to(m)
    return m

# --- MAIN APP UI ---
st.markdown('<p class="main-header">✈️ Student AI Travel Planner</p>', unsafe_allow_html=True)
st.markdown('<p class="main-header" style="font-size: 1.5rem; margin-top: -20px;">Smart, Budget-Friendly Itineraries in Seconds</p>', unsafe_allow_html=True)
st.divider()

if submitted:
    with st.spinner("🤖 AI is crafting your perfect budget trip..."):
        # Anti-spam delay to help prevent 429 errors
        time.sleep(1) 
        st.session_state['trip_data'] = get_itinerary(destination, budget, currency, days, preferences)
        st.session_state['current_destination'] = destination

if st.session_state['trip_data']:
    data = st.session_state['trip_data']
    dest_name = st.session_state['current_destination']
    
    # Note: source.unsplash.com is deprecated. Using a placeholder for now.
    # You might want to use Pexels API or simply static images later.
    st.image(f"https://source.unsplash.com/1200x400/?{dest_name},travel", use_column_width=True)
    
    st.markdown(f"# {data.get('trip_name', 'Your Trip')}")
    
    met1, met2, met3 = st.columns(3)
    met1.metric("📍 Destination", dest_name)
    met2.metric("📅 Duration", f"{days} Days")
    met3.metric("💰 Estimated Cost", data.get('total_estimated_cost', 'N/A'))
    
    st.info(f"📝 **Trip Summary:** {data.get('summary', '')}")
    
    st.subheader("🗺️ Interactive Route Map")
    try:
        map_obj = plot_map(data)
        st_folium(map_obj, width=1200, height=500)
    except Exception as e:
        st.warning(f"Could not generate map visualization. (Error: {e})")
    
    st.subheader("📅 Your Daily Plan")
    for day in data.get('itinerary', []):
        with st.expander(f"**Day {day['day']}: {day.get('day_theme', 'Explore')}**", expanded=True):
            for act in day.get('activities', []):
                time_col, content_col, cost_col = st.columns([2, 6, 2])
                with time_col:
                    st.markdown(f"**⏱️ {act['time']}**")
                with content_col:
                    st.markdown(f"### {act['activity']}")
                    st.write(act['desc'])
                with cost_col:
                    st.markdown(f'<div class="cost-tag">{act["cost"]}</div>', unsafe_allow_html=True)
else:
    st.info("👈 Configure your budget and interests in the sidebar, then click 'Generate Smart Itinerary' to begin!")
