FROM buildpack-deps:jammy-curl

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends vim htop net-tools

CMD ["tail", "-f", "/dev/null"]
