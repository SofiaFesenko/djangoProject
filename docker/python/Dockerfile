FROM python:3.10.6
COPY . /project
WORKDIR /project/backend
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin gettext
RUN pip install -r requirements.txt