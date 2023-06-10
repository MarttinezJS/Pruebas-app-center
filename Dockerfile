FROM python:3.9
WORKDIR /home
COPY ./requirements.txt /home/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /home/requirements.txt
COPY ./app /home/app
COPY ./entrypoint.sh /home/entrypoint.sh
RUN ["chmod", "+x", "/home/entrypoint.sh"]
ENTRYPOINT ["/home/entrypoint.sh"]
