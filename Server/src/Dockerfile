# Set base image (host OS)
FROM python:3.8-alpine

# working directory
WORKDIR /src

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Copy the dependencies file to the working directory
COPY requirements.txt .

RUN pip install -r requirements.txt

# add all files to the container
COPY . /src

# By default, listen on port 5000
EXPOSE 5000/tcp

# run the command
CMD ["flask", "run"]
