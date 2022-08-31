FROM python:3.8
WORKDIR /formula-streaming
COPY . .
CMD ["python", "./formula_streaming.py"]