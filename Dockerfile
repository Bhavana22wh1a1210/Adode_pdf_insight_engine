FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 👇 You can change this line to run either round1a or round1b
CMD ["python", "round1a/main.py"]
