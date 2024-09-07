FROM python:3.10

WORKDIR /APP.

COPY . .

RUN pip install -r requirement.txt

EXPOSE 5000 




CMD [ "python" , "test2.py"]
