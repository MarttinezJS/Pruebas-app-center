FROM python:3.9 as Production
WORKDIR /home
COPY ./requirements.txt /home/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /home/requirements.txt
COPY ./app /home/app
COPY ./entrypoint.sh /home/entrypoint.sh
RUN ["chmod", "+x", "/home/entrypoint.sh"]
ENTRYPOINT ["/bin/sh","/home/entrypoint.sh"]

FROM python:3.9 as Tests
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /code/app
COPY ./tests.sh /code/tests.sh
RUN ["chmod", "+x", "/code/tests.sh"]
ENTRYPOINT ["/bin/sh","/code/tests.sh"]
CMD tail -f /dev/null