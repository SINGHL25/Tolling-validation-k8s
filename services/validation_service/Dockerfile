
FROM python:3.11-slim
WORKDIR /app
COPY app.py /app/app.py
COPY db /app/db
RUN pip install fastapi uvicorn python-multipart
EXPOSE 80
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","80"]
