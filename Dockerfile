FROM python:3.7
LABEL maintainer="Ricard Lado <ricardlador@iqs.edu>"

#Copy the repo
WORKDIR /opt/Aeropendulum-IOT/
COPY . /opt/Aeropendulum-IOT/

#Install dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3-opencv
RUN cp -r /usr/lib/python3/dist-packages/* /usr/local/lib/python3.7/site-packages/
RUN pip install flask
RUN pip install pyserial

#Run the web interface
ENTRYPOINT sh runWI.sh
