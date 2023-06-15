FROM python:3.9-alpine3.8
COPY . .
CMD ["python", "./main.py"]
