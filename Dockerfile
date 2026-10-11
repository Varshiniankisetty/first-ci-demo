
FROM python:3.11-slim

WORKDIR /app

COPY result_logic.py .

CMD ["python", "result_logic.py"]
