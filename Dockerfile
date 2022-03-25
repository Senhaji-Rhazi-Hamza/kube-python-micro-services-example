FROM python:3.8

# Install Unix packages
RUN apt-get update && \
    apt-get -qq -y install curl && \
    apt-get -y install libglib2.0-0 libsm6 libxext6 libxrender-dev

# Python requirements
RUN mkdir /appp
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy code
ADD . /appp/
RUN chmod -R 0644 /app
WORKDIR /appp/
ENV PYTHONPATH=${PYTHONPATH}:.

EXPOSE 8000

ENTRYPOINT ["python", "app/cli/run.py"]