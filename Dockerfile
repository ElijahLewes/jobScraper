FROM python:3
WORKDIR /jobScraper/
COPY . /jobScraper
CMD ["python3", "main.py"]

