# WeatherBoi

This coursework involves developing a **task-oriented dialogue system** that allows users to request weather forecasts for a given location and date. The system will utilize **Natural Language Understanding (NLU)** to extract intents and entities, and it must integrate with the **OpenWeatherMap API** to fetch real-time weather data.

## Assignment Structure

The coursework is divided into two parts:

### Part A: Core Implementation

- Develop a weather chatbot based on provided sample dialogues.
- Implement **NLU components** to detect user intents and extract relevant entities (e.g., city, date).
- Integrate the chatbot with the **OpenWeatherMap API** for real-time weather retrieval.
- Evaluate the system's **NLU performance** using a set of unseen test dialogues.

### Part B: Extended Agent Design

- Design an enhanced version of the chatbot with **advanced features**, such as:
  - **Multi-modal UI** (e.g., cards, lists, or visual elements).
  - **Persona-based responses** for a more engaging interaction.
  - **Socialbot capabilities** (e.g., extended conversations about the weather).
  - **Additional API integrations** (e.g., travel advice or local events).
- Choose to either **implement the extended version** or **conduct a user evaluation**.

## Implementation Details

The system can be built using **LangChain**, leveraging:

- **LLM-based NLU** for intent recognition and slot filling.
- **Memory components** to maintain conversation history.
- **API tools** for real-time weather queries.
- **Evaluation techniques** to analyze chatbot performance.
