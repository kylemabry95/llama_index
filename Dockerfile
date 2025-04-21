FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
# "--no-cache-dir" is used to avoid caching the packages in the Docker image
# This is useful for keeping the image size small and ensuring that the latest versions of the packages are installed.
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py"]