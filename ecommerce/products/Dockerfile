# product_service/Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y build-essential libssl-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 8001

CMD [ "python", "run.py" ]