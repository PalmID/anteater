FROM leosocy/robustpalmroi:v0.1.1

# install pipenv
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -i https://mirrors.aliyun.com/pypi/simple pipenv && \
    pipenv install --deploy --system
