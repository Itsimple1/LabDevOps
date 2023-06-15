FROM python:3-alpine
COPY main.py main.py
CMD sh -c 'python main.py'
