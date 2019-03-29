FROM python:3.8-rc-alpine
MAINTAINER Poeschl@users.noreply.github.com

ENV WORKING_DIR /home/bot/stickerblockbot
WORKDIR ${WORKING_DIR}

#Harden the container with unsetting the SUID flag
RUN for i in `find / -perm +6000 -type f`; do chmod a-s $i; done

#Add bot user
RUN addgroup -g 900 -S bot && adduser -u 900 -s /bin/sh -SDH bot bot && mkdir -p ${WORKING_DIR}

ADD requirements.txt ${WORKING_DIR}/requirements.txt
RUN apk add g++ libffi-dev openssl-dev && \
    pip install -r requirements.txt && \
    apk del g++ libffi-dev openssl-dev && rm -rf /var/cache/apk/*

COPY docker/entrypoint.sh /usr/local/bin
RUN chmod 500 /usr/local/bin/entrypoint.sh && chown bot:bot /usr/local/bin/entrypoint.sh && ln -s /usr/local/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]

ADD stickerblockbot/ ${WORKING_DIR}/
