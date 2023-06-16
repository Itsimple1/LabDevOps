FROM python:3.10
RUN pip install aiogram==2.25.1
COPY app/bot.py app/bot.py
ENTRYPOINT ["python3", "app/bot.py"]
