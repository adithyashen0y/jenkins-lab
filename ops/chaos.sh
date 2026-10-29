#!/usr/bin/env bash
# Incident simulator for the Jenkins lab.
# Try NOT to read below this line before doing the drill -- the point is to debug blind.
# Usage: ./ops/chaos.sh 1|2|3
set -e

case "$1" in
  1)
    docker stop hello-app >/dev/null
    ;;
  2)
    img=$(docker inspect hello-app --format '{{.Config.Image}}')
    docker rm -f hello-app >/dev/null
    docker run -d --name hello-app --network lab-net -p 8081:5000 "$img" >/dev/null
    ;;
  3)
    docker exec jenkins sh -c 'mkdir -p /var/jenkins_home/init.groovy.d && echo "jenkins.model.Jenkins.get().setNumExecutors(0); jenkins.model.Jenkins.get().save()" > /var/jenkins_home/init.groovy.d/zz.groovy'
    docker restart jenkins >/dev/null
    echo "waiting for Jenkins to come back..."
    until curl -s -o /dev/null http://localhost:8080/login; do sleep 3; done
    sleep 10
    docker exec jenkins rm -f /var/jenkins_home/init.groovy.d/zz.groovy
    ;;
  *)
    echo "usage: $0 1|2|3"
    exit 1
    ;;
esac

echo "Incident $1 started. Something is wrong now. Go find it."
