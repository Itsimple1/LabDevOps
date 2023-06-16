FROM python
RUN pip install aiogram==2.25.1
COPY . .
CMD ["python3", "bot.py"]
