
FROM neo4j:4.2.4
# see  https://raw.githubusercontent.com/grand-stack/grand-stack-starter/master/neo4j/Dockerfile
ENV NEO4J_AUTH=neo4j/letmein \
    APOC_VERSION=4.2.0.2 \
    GRAPHQL_VERSION=3.5.21.5

# RUN apt update ; apt install -y curl
# ENV APOC_URI https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download/${APOC_VERSION}/apoc-${APOC_VERSION}-all.jar
# RUN sh -c 'cd /var/lib/neo4j/plugins && curl -L -O "${APOC_URI}"'

# ENV GRAPHQL_URI https://github.com/neo4j-graphql/neo4j-graphql/releases/download/${GRAPHQL_VERSION}/neo4j-graphql-${GRAPHQL_VERSION}.jar
# RUN sh -c 'cd /var/lib/neo4j/plugins && curl -L -O "${GRAPHQL_URI}"'

EXPOSE 7474 7473 7687

CMD ["neo4j"]
