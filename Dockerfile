FROM python:3.10-slim

WORKDIR /app

COPY best.pt .
COPY detect.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "detect.py"]
