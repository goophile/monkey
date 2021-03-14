FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y vim python3 python3-pip && \
    apt-get clean

COPY pip.conf /root/.pip/
RUN python3 -m pip --no-cache-dir install Flask uwsgi graphene mongoengine

COPY ./monkey /tmp/monkey

CMD ["sh", "-c", "uwsgi --socket 0.0.0.0:5000 --protocol http --master --workers 4 --chdir /tmp --wsgi monkey:app"]
