FROM python:latest

WORKDIR /demo
COPY . . 

CMD  python demo.py && tail -f /dev/null