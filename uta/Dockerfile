FROM postgres
COPY ./init-uta.sh /docker-entrypoint-initdb.d/
ENV UTA_VERSION=uta_20210129.pgd.gz
RUN chmod a+x /docker-entrypoint-initdb.d/init-uta.sh
RUN apt-get update ; apt-get install -y curl
RUN curl -O http://dl.biocommons.org/uta/$UTA_VERSION
EXPOSE 5432
