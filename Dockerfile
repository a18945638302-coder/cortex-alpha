FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install fastapi==0.115.0 uvicorn==0.30.0 supabase==2.3.0 python-dotenv==1.0.0
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
