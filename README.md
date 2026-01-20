# ✈️ Student AI Travel Planner

An intelligent, budget-friendly travel planning application built with Streamlit and powered by Google's Gemini AI. This app helps students plan their trips by generating personalized itineraries that fit their budget and interests.

## 🌟 Features

- **AI-Powered Itinerary Generation**: Uses Google's Gemini 2.0 Flash model to create personalized travel plans
- **Budget-Conscious Planning**: Focuses on free or low-cost activities suitable for students
- **Interactive Map Visualization**: Displays your entire trip route with color-coded daily plans using Folium
- **Customizable Preferences**: Choose from various interests like Adventure, History, Food, Nightlife, Nature, Relaxation, and Art
- **Multi-Currency Support**: Plan your budget in INR, USD, or EUR
- **Day-by-Day Breakdown**: Get detailed daily schedules with activity times, locations, and cost estimates
- **Visual Timeline**: Each activity includes time slots, descriptions, and estimated costs

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Google API Key for Gemini AI
- Internet connection

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/koushik0356/student-travel-planner.git
   cd student-travel-planner
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Google API Key**
   
   Create a `.streamlit` directory in the project root and add a `secrets.toml` file:
   ```bash
   mkdir .streamlit
   touch .streamlit/secrets.toml
   ```
   
   Add your Google API key to `.streamlit/secrets.toml`:
   ```toml
   GOOGLE_API_KEY = "your-google-api-key-here"
   ```
   
   To get a Google API key:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Enable the Generative Language API

### Running the Application

```bash
streamlit run travel_planner.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📖 Usage

1. **Configure Your Trip** (in the sidebar):
   - Enter your destination (e.g., "Paris", "Tokyo", "Goa")
   - Set your budget and select currency
   - Choose trip duration (1-14 days)
   - Select your interests from the available options

2. **Generate Itinerary**:
   - Click the "✨ Generate Smart Itinerary" button
   - Wait for the AI to generate your personalized plan

3. **Explore Your Trip**:
   - View the interactive map with all your activities plotted
   - Browse day-by-day activities with times and costs
   - Read detailed descriptions for each location

## 🛠️ Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Interactive web application framework
- **AI Model**: [Google Gemini 2.0 Flash](https://ai.google.dev/) - Advanced generative AI
- **Mapping**: [Folium](https://python-visualization.github.io/folium/) - Interactive maps
- **Languages**: Python 3.x

## 📦 Dependencies

- `streamlit` - Web application framework
- `google-generativeai` - Google's Gemini AI SDK
- `folium` - Python mapping library
- `streamlit-folium` - Streamlit component for Folium maps

## 🔒 Security Notes

**Important**: Never commit your API keys to version control!

- Always use the `.streamlit/secrets.toml` file for API keys
- Add `.streamlit/` to your `.gitignore` file
- The fallback API key in the code is for demonstration only and should be removed in production

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Koushik**
- GitHub: [@koushik0356](https://github.com/koushik0356)

## 🙏 Acknowledgments

- Google Gemini AI for powering the intelligent itinerary generation
- Streamlit for the amazing web framework
- The open-source community for the excellent libraries used in this project

## 📞 Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

---

Made with ❤️ for students who love to travel on a budget!