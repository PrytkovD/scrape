FROM gradle

ENV WORKDIR=orchestrator
WORKDIR "/$WORKDIR"

COPY . .

CMD ["java", "-jar", "./build/libs/Orchestrator-1.0-SNAPSHOT.jar"]
