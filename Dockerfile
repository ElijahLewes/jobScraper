FROM python:3

# Install system dependencies for PyQt5
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    qtbase5-dev \
    qt5-qmake \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /jobScraper/
COPY requirementList.txt .
RUN pip install r requirementList.txt 

COPY . /jobScraper


CMD bash -c echo "Environment ready. Let's get at 'er"

