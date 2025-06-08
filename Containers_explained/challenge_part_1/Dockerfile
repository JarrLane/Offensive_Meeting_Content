FROM python:3.10-slim

RUN pip install flask


ADD docker-site.py .

ADD templates/ ./templates/

EXPOSE 5001

CMD ["python", "docker-site.py"]
