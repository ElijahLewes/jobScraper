FROM python:3.12-slim

# Install system dependencies for PyQt5
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    qtbase5-dev \
    qt5-qmake \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /jobScraper/
# Upgrade tools
RUN pip install --upgrade pip setuptools wheel
# Install PyQt6 and sip first to ensure wheel is used
RUN pip install --no-cache-dir PyQt6-sip==13.6.0

# Now install the rest
COPY requirementList.txt .
RUN pip install --no-cache-dir -r requirementList.txt

COPY . /jobScraper


CMD bash -c echo "Environment ready. Let's get at 'er"

