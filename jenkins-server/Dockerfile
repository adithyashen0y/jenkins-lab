# Jenkins + the tools our pipeline needs (python, docker CLI, curl)
FROM jenkins/jenkins:lts-jdk21

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 python3-venv python3-pip curl \
    && rm -rf /var/lib/apt/lists/*

# Only the docker CLI. The real Docker engine is the VM's, reached through the socket.
COPY --from=docker:27-cli /usr/local/bin/docker /usr/local/bin/docker
COPY --from=docker:27-cli /usr/local/libexec/docker/cli-plugins/docker-buildx /usr/local/libexec/docker/cli-plugins/docker-buildx

USER jenkins
