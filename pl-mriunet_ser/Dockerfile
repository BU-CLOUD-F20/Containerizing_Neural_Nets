# Docker file for mriunet_ser ChRIS plugin app
#
# Build with
#
#   docker build -t <name> .
#
# For example if building a local version, you could do:
#
#   docker build -t local/pl-mriunet_ser .
#
# In the case of a proxy (located at 192.168.13.14:3128), do:
#
#    docker build --build-arg http_proxy=http://192.168.13.14:3128 --build-arg UID=$UID -t local/pl-mriunet_ser .
#
# To run an interactive shell inside this container, do:
#
#   docker run -ti --entrypoint /bin/bash local/pl-mriunet_ser
#
# To pass an env var HOST_IP to container, do:
#
#   docker run -ti -e HOST_IP=$(ip route | grep -v docker | awk '{if(NF==11) print $9}') --entrypoint /bin/bash local/pl-mriunet_ser
#


FROM tensorflow/tensorflow:latest-gpu-py3
MAINTAINER fnndsc "dev@babymri.org"

ENV APPROOT="/usr/src/mriunet_ser"
COPY ["mriunet_ser", "${APPROOT}"]
COPY ["requirements.txt", "${APPROOT}"]

WORKDIR $APPROOT

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]

CMD ["mriunet_ser.py", "--help"]