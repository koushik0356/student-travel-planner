<div align="center">

# ✈️ Student AI Travel Planner

### *Your Smart Companion for Budget-Friendly Adventures*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white" alt="Gemini AI"/>
  <img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge" alt="License"/>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-demo">Demo</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-documentation">Documentation</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

**An AI-powered travel planning platform that generates personalized, budget-conscious itineraries for students. Experience intelligent trip planning with interactive maps, cost optimization, and day-by-day schedules—all powered by Google's Gemini AI.**

</div>

<br/>

## 📸 Demo

<div align="center">

### Application Interface

```
┌─────────────────────────────────────────────────────────────────┐
│  ✈️ Student AI Travel Planner                                   │
│  Smart, Budget-Friendly Itineraries in Seconds                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [Sidebar]              [Main Content Area]                     │
│  ┌──────────┐          ┌─────────────────────────────────┐     │
│  │ 📍 Goa   │          │  🗺️ Interactive Map View        │     │
│  │ 💰 5000  │          │  • Day 1: Beach Hopping         │     │
│  │ 📅 3 Days│          │  • Day 2: Culture & History     │     │
│  │ ❤️ Food  │          │  • Day 3: Adventure Activities  │     │
│  │          │          └─────────────────────────────────┘     │
│  │ [Generate]│         ┌─────────────────────────────────┐     │
│  └──────────┘          │  📅 Detailed Daily Itinerary   │     │
│                        │  ⏱️ Timed activities with costs │     │
│                        └─────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────┘
```

*Replace with actual screenshots when available*

</div>

---

## 🌟 Features

- **AI-Powered Itineraries**: Leverages Google Gemini 2.0 Flash to generate creative, personalized travel plans
- **Budget-Conscious**: Focuses on free and low-cost activities perfect for students
- **Interactive Maps**: Visualize your entire trip route with Folium-powered maps
- **Multi-Currency Support**: Plan trips in INR, USD, or EUR
- **Flexible Duration**: Create itineraries from 1 to 14 days
- **Interest-Based Planning**: Customize trips based on preferences (Adventure, History, Food, etc.)
- **Day-by-Day Breakdown**: Detailed schedules with timing, costs, and descriptions
- **Responsive UI**: Clean, modern interface built with Streamlit

---

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[Google Generative AI (Gemini)](https://ai.google.dev/)** - AI-powered itinerary generation
- **[Folium](https://python-visualization.github.io/folium/)** - Interactive map visualization
- **[streamlit-folium](https://github.com/randyzwitch/streamlit-folium)** - Folium integration for Streamlit
- **Python 3.8+** - Core programming language

---

## 📋 Prerequisites

Before running this application, ensure you have:

- Python 3.8 or higher installed
- A Google API key with Generative AI access ([Get one here](https://makersuite.google.com/app/apikey))
- pip (Python package manager)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/koushik0356/student-travel-planner.git
cd student-travel-planner
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

**Option A: Using Streamlit Secrets (Recommended)**

Create a `.streamlit` folder in the project root and add a `secrets.toml` file:

```bash
mkdir .streamlit
```

Create `.streamlit/secrets.toml`:

```toml
GOOGLE_API_KEY = "your-google-api-key-here"
```

**Option B: Environment Variables**

Set your API key as an environment variable:

```bash
# Windows (PowerShell)
$env:GOOGLE_API_KEY="your-google-api-key-here"

# Linux/Mac
export GOOGLE_API_KEY="your-google-api-key-here"
```

> ⚠️ **Security Warning**: Never commit your API key to version control. Add `.streamlit/secrets.toml` to `.gitignore`.

---

## 🎮 Usage

### Running the Application

```bash
streamlit run travel_planner.py
```

The app will open in your default browser at `http://localhost:8501`

### Using the App

1. **Enter Your Destination**: Type the city or country you want to visit
2. **Set Your Budget**: Input your maximum budget and select currency
3. **Choose Duration**: Use the slider to select trip length (1-14 days)
4. **Select Interests**: Pick activities you enjoy (Adventure, Food, History, etc.)
5. **Generate Itinerary**: Click "✨ Generate Smart Itinerary" and wait for AI magic
6. **Explore Your Plan**: View the interactive map and day-by-day breakdown

---

## 📁 Project Structure

```
IBM_Project/
│
├── travel_planner.py      # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
└── .streamlit/           # Configuration folder (create manually)
    └── secrets.toml      # API keys (DO NOT COMMIT)
```

---

## 🎨 Key Components

### AI Itinerary Generator
The `get_itinerary()` function uses Google's Gemini 2.0 Flash model to generate structured JSON itineraries with:
- Creative trip names
- Daily themes
- Activity timing and costs
- Geographic coordinates for mapping
- Detailed descriptions

### Interactive Mapping
The `plot_map()` function creates color-coded routes with:
- Markers for each activity
- Popup information cards
- Day-by-day route visualization
- Custom styling

### Session State Management
Maintains trip data across interactions without regenerating itineraries unnecessarily.

---

## 🔧 Configuration Options

### Customizing the AI Prompt
Edit the prompt in `get_itinerary()` function to adjust:
- Activity types
- Cost strictness
- Output format
- Level of detail

### Styling
Modify the CSS in the `st.markdown()` section to change:
- Color schemes
- Button styles
- Layout dimensions
- Font sizes

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: "AI Error: 429 Resource Exhausted"
- **Solution**: API rate limit reached. Add delays between requests or use a different API key.

**Issue**: Map not displaying
- **Solution**: Check that activities have valid latitude/longitude coordinates.

**Issue**: "Module not found" errors
- **Solution**: Reinstall dependencies: `pip install -r requirements.txt`

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 Future Enhancements

- [ ] Add weather forecast integration
- [ ] Export itinerary as PDF
- [ ] Multi-destination trip planning
- [ ] Social sharing features
- [ ] User authentication and saved trips
- [ ] Integration with booking platforms
- [ ] Offline map support
- [ ] Mobile app version

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**IBM Project Team**

- GitHub: [@koushik0356](https://github.com/koushik0356)
- Project Link: [https://github.com/yourusername/student-travel-planner](https://github.com/koushik0356/student-travel-planner)

---

## 🙏 Acknowledgments

- Google Generative AI for providing the Gemini API
- Streamlit for the amazing web framework
- OpenStreetMap contributors for map data
- The open-source community for various libraries

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: koushik0356@gmail.com

---

**Made with ❤️ for students who love to travel**
