FROM python:3-alpine
WORKDIR /app
COPY calculator/calc.py .
ENTRYPOINT ["python3", "calc.py"]