# Base image
FROM python:3.10

# Working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install flask gunicorn

# Expose port
EXPOSE 5000

# Run app
CMD ["python" , "app.py"]