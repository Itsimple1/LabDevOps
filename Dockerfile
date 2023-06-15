FROM python:3-alpine
COPY main.py main.py
COPY im.py im.py
CMD ["python3", "im.py"]
