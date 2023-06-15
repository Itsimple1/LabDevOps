FROM python:3

COPY . .

#Компилим
RUN pip install pyinstaller && pyinstaller --onefile main.py

# Выполняемая команда при запуске
CMD [ "./main" ]
