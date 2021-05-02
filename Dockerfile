FROM python:3.9.2

RUN apt-get update -y

RUN apt install -y wget

RUN apt install -y --no-install-recommends \
    libatlas-base-dev \
    gfortran \
    nginx \
    supervisor \
    build-essential \
    uwsgi-plugin-python \
    uwsgi \
    uwsgi-src \
    uuid-dev \
    libcap-dev \
    libpcre3-dev \
    python-virtualenv \
    uwsgi-plugin-python3

RUN ln -s /usr/bin/uwsgi /usr/local/bin/uwsgi

RUN chmod +x /usr/local/bin/uwsgi

WORKDIR /app

RUN useradd --no-create-home nginx

ENV FLASK_ENV=production

ENV PYTHON=python3.9

RUN uwsgi --build-plugin "/usr/src/uwsgi/plugins/python python39"

RUN mv python39_plugin.so /usr/lib/uwsgi/plugins/python39_plugin.so

RUN chmod +x /usr/lib/uwsgi/plugins/python39_plugin.so

COPY . .

RUN pip install -r requirements.txt

RUN rm -r /root/.cache

RUN rm /etc/nginx/sites-enabled/default

RUN mv nginx/conf.d/flask-api-nginx.conf /etc/nginx/conf.d/

RUN mv nginx/uwsgi.ini /etc/uwsgi/

RUN mv nginx/supervisord.conf /etc/

RUN mv nginx/conf.d/nginx.conf /etc/nginx/

EXPOSE 8000

ENTRYPOINT ["/usr/bin/supervisord"]
