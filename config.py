import google.generativeai as genai
import streamlit as st

# Lấy API Key từ Secrets của Streamlit Cloud (khi đưa lên mạng) 
# Hoặc lấy trực tiếp từ hệ thống nếu chạy trên máy tính
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

# Cấu hình model sử dụng chung cho toàn hệ thống
model = genai.GenerativeModel('gemini-3.5-flash-lite')
