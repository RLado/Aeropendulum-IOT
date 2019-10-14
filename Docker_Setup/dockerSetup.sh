#Run me from the docker_setup folder
cd ..
VDEVS=$(python3 Docker_Setup/dstp.py)

docker build . -t aeropendulum && docker run --name Aeropendulum-IOT -p 5000:80 $VDEVS --restart=unless-stopped --security-opt seccomp="$(pwd)/docker_setup/seccomp_profile.json" smart4iv3/imrec_module &
