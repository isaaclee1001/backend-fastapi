# Start from a Python 3.9 image.
FROM python:3.11

# Create and set working directory
WORKDIR /app

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install pip dependencies
ADD requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all files to working directory
COPY . .

# Run the applications
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]