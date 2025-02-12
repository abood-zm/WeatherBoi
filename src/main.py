import getpass
import requests
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain.vectorstores import pinecone
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
import pinecone

load_dotenv('config/.env')


@tool
def getWeather(self, city: str):
    weather_api = os.getenv("OPENWEATHER_API_KEY")
    if not self.weather_api:
        print("API key is missing!")
        return
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}"
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data: {response.status_code}")
        return None


class ConversationState():
    def __init__(self):
        
    
    def setState(self):
        return
    
class WeatherBot():
    def __init__(self):
        self.memory = MemorySaver()
        self.model = init_chat_model("llama3-8b-8192", model_provider='groq')
        self.tools = [getWeather]
        self.agent = create_react_agent(self.model, self.tools)


    def agent_executor(self):
        prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content="You are a friendly weather forecaster that informs user about weather using the tools that you have."),
            HumanMessage(content="What is the weather in Glasgow?"),
            MessagesPlaceholder(variable_name="transcipts"),
        ])

        response = self.agent.invoke(prompt)
        return response["messages"]
    
    def recognize_intent(self, user_input):
        return
    
    def fill_slots(self, user_input):
        return
    

    
    def run(self):
        city = "London"
        weather_json = self.getWeather(city)
        if weather_json:
            print(weather_json)
        else:
            print("No weather data available.")

bot = WeatherBot()
bot.run()