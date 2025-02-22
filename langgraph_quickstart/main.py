import os
from dotenv import load_dotenv

load_dotenv()

from agents.chatbot_agent import run_chatbot, draw_chatbot

draw_chatbot()
run_chatbot()
