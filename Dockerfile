FROM python:3.10 as Production
WORKDIR /home
COPY ./requirements.txt /home/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /home/requirements.txt
COPY ./app /home/app
COPY ./entrypoint.sh /home/entrypoint.sh
RUN ["chmod", "+x", "/home/entrypoint.sh"]
ENTRYPOINT ["/bin/sh","/home/entrypoint.sh"]