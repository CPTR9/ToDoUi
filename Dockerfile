FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "gunicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]