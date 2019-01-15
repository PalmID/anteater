FROM leosocy/robustpalmroi:v0.1.1

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN apk add --no-cache mariadb-connector-c-dev && \
    apk add --no-cache --virtual .build-deps \
        python3-dev \
        build-base \
        mariadb-dev && \
    pip install -i https://mirrors.aliyun.com/pypi/simple pipenv && \
    pipenv install --deploy --system && \
    apk del .build-deps