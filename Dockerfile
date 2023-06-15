FROM python:3.9
RUN adduser --system --no-create-home nonroot
WORKDIR /home
COPY ./requirements.txt /home/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /home/requirements.txt
USER nonroot
COPY ./app /home/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]