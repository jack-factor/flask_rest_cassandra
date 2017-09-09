FROM jackmoreno/python3_cassandra_driver

MAINTAINER Jack Moreno Barrera "jack12972@gmail.com"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./api.py" ]
