FROM python:3.9-slim

# Working Directory
WORKDIR / APP

# Copy source code to working directory
COPY requirements.txt /app/

# Install packages from requirements.txt#

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

CMD python app.py
