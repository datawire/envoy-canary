# Run server
FROM python:3-alpine
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]
