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
RUN cp -r /usr/lib/python3/dist-packages/* /usr/local/lib/python3.7/site-packages/
RUN pip install flask

#Run the web interface
ENTRYPOINT sh runWI.sh
