import os
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
import requests
from llama_agents import (
    AgentService,
    HumanService,
    AgentOrchestrator,
    CallableMessageConsumer,
    ControlPlaneServer,
    ServerLauncher,
    SimpleMessageQueue,
    QueueMessage,
)

from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

def get_coordinates(city: str) -> tuple:
    """Fetches coordinates (latitude, longitude) for a given city using geopy and Nominatim."""
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    else:
        raise ValueError(f"Could not fetch coordinates for {city}.")

def get_weather_info(city: str) -> str:
    """Fetches weather information for a given city from OpenWeatherMap API."""
    try:
        lat, lon = get_coordinates(city)
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"The current weather in {city} is {weather_description} with a temperature of {temperature}°C."
        else:
            return f"Could not fetch weather information for {city}."
    except ValueError as e:
        return str(e)

def get_news_headlines() -> str:
    """Returns the latest news headlines."""
    return "Today's headlines: Market hits record high, new tech innovations emerge, and global peace talks continue."

# Create tools from the functions
weather_tool = FunctionTool.from_defaults(fn=get_weather_info)
news_tool = FunctionTool.from_defaults(fn=get_news_headlines)

# Create workers and agents
worker1 = FunctionCallingAgentWorker.from_tools([weather_tool], llm=OpenAI())
worker2 = FunctionCallingAgentWorker.from_tools([news_tool], llm=OpenAI())
agent1 = worker1.as_agent()
agent2 = worker2.as_agent()

# Create our multi-agent framework components
message_queue = SimpleMessageQueue()
queue_client = message_queue.client

control_plane = ControlPlaneServer(
    message_queue=queue_client,
    orchestrator=AgentOrchestrator(llm=OpenAI()),
)
agent_server_1 = AgentService(
    agent=agent1,
    message_queue=queue_client,
    description="Provides weather information of any city.",
    service_name="weather_info_agent",
    host="127.0.0.1",
    port=8002,
)
agent_server_2 = AgentService(
    agent=agent2,
    message_queue=queue_client,
    description="Provides news headlines.",
    service_name="news_info_agent",
    host="127.0.0.1",
    port=8003,
)
human_service = HumanService(
    message_queue=queue_client,
    description="Answers general queries.",
    host="127.0.0.1",
    port=8004,
)

# Additional human consumer
def handle_result(message: QueueMessage) -> None:
    print("Got result:", message.data)

human_consumer = CallableMessageConsumer(handler=handle_result, message_type="human")

# Launch the servers
launcher = ServerLauncher(
    [agent_server_1, agent_server_2, human_service],
    control_plane,
    message_queue,
    additional_consumers=[human_consumer],
)

launcher.launch_servers()
