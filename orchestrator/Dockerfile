FROM gradle

ENV WORKDIR=orchestrator
WORKDIR "/$WORKDIR"

RUN apt-get update
RUN apt-get install -y curl

COPY . .

CMD ["java", "-jar", "./build/libs/Orchestrator-1.0-SNAPSHOT.jar"]
