FROM python:3.9

FROM gorialis/discord.py



RUN mkdir -p /usr/src/weather/weather_app

WORKDIR /usr/src/weather/weather_app



COPY . .


CMD [ "python", "manage.py", "runserver" ]
