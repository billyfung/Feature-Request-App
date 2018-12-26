FROM python:3.6-alpine

COPY . /app
WORKDIR /app
RUN pipenv install --dev
ENTRYPOINT ["python"]
CMD ["app.py"]
