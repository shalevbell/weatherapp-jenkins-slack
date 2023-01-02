FROM python:3.8-slim
RUN mkdir /app
WORKDIR /app
RUN pip3 install requests datetime flask gunicorn
ADD . /app
EXPOSE 9090
ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "wsgi:weather_app"]
