FROM python:3.8

RUN mkdir -p /usr/src/app/server/
WORKDIR /usr/src/app/server/

COPY . /usr/src/app/server/
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1
EXPOSE 8000
ENTRYPOINT ["python","manage.py","runserver","0.0.0.0:8000"]
