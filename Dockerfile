FROM python:3.9-slim
RUN pip install aiogram==2.25.1
COPY . .
CMD ["python3", "app/bot.py"]
