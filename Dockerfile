FROM python:3.7

WORKDIR /app

# only copy requirements.txt first to leverage Docker cache
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python","run.py"]

# EXPOSE 3000