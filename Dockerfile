# Dockerfile
FROM python:3.9-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "flask_app.py"]