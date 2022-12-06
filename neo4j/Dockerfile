# The commands following all RUN instructions are run in a shell, which
# by default is /bin/sh -c on Linux or cmd /S /C on Windows.

# Initialize a new build stage and set the base image to the Docker
# Neo4j image that has the "4.4.9-community" tag.
FROM neo4j:4.4-community

# see  https://raw.githubusercontent.com/grand-stack/grand-stack-starter/master/neo4j/Dockerfile
# Set environment variables for all subsequent instructions. 
# NEO4J_AUTH stores username/password for container,
#ENV NEO4J_AUTH=neo4j/letmein \
#    APOC_VERSION=4.2.0.2 \
#    GRAPHQL_VERSION=3.5.21.5

# RUN apt update ; apt install -y curl
# ENV APOC_URI https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download/${APOC_VERSION}/apoc-${APOC_VERSION}-all.jar
# RUN sh -c 'cd /var/lib/neo4j/plugins && curl -L -O "${APOC_URI}"'

# ENV GRAPHQL_URI https://github.com/neo4j-graphql/neo4j-graphql/releases/download/${GRAPHQL_VERSION}/neo4j-graphql-${GRAPHQL_VERSION}.jar
# RUN sh -c 'cd /var/lib/neo4j/plugins && curl -L -O "${GRAPHQL_URI}"'

# Inform Docker that the container listens on the specified network
# ports at runtime. The default protocol is TCP.
EXPOSE 7474 7473 7687

# Set default executable for the container. A command shell is not
# invoked, so normal shell processing does not occur. The command is
# only executed when running the image, not during build.
CMD ["neo4j"]
