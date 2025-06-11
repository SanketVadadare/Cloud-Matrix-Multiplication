FROM python:3.9-slim
WORKDIR /app
RUN pip install numpy
COPY matrix_multiply.py .
CMD ["python", "matrix_multiply.py"]