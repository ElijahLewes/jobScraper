FROM python:3
WORKDIR /jobScraper/
COPY . .
CMD ["python3", "main.py"]

