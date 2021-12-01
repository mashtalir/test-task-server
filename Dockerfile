FROM node:16

RUN apt-get update || : && apt-get install -y \
    python3 \
    python3-pip


RUN mkdir -p /usr/src/app/client/
WORKDIR /usr/src/app/client/

COPY test-task-client /usr/src/app/client/

RUN npm install

EXPOSE 3000


RUN mkdir -p /usr/src/app/server/
WORKDIR /usr/src/app/server/

COPY test-task-server/task /usr/src/app/server/
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1
EXPOSE 8000

WORKDIR /usr/src/app/
COPY runner.sh /usr/src/app/

RUN ["chmod", "+x", "runner.sh"]
ENTRYPOINT ["./runner.sh"]

