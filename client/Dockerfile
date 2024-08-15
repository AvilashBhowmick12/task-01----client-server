# Use a lightweight web server
FROM python:3.9-slim

WORKDIR /app

# Copy the application files
COPY app.py .
COPY templates/ ./templates/

# Install Flask
RUN pip install Flask

# Expose the port
EXPOSE 80

# Command to run the application
CMD ["python", "app.py"]