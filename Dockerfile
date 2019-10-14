FROM python:3
LABEL maintainer="Ricard Lado <ricardlador@iqs.edu>"

#Clone the repo
WORKDIR /opt/
RUN git clone https://github.com/Reichyga/Aeropendulum-IOT.git
WORKDIR /opt/Aeropendulum-IOT/

#Install dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3-opencv
RUN pip install flask

#Run the web interface
ENTRYPOINT sh runWI.sh
