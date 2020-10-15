FROM python:3.7.1-alpine

WORKDIR /todos

COPY . /todos

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

RUN pip install -r requirements.txt

ENTRYPOINT ["python","./main.py"]
EXPOSE 9090
EXPOSE 5432