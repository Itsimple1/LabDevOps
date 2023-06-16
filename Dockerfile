FROM python
RUN pip install aiogram==2.25.1
COPY app/bot.py bot.py
CMD ["python", "bot.py"]
