FROM python:3.8
WORKDIR /application
COPY . .
RUN pip3 install flask
ENTRYPOINT [ "python" ]
CMD ["app.py"]