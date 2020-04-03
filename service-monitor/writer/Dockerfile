FROM python:3

WORKDIR /writer

COPY . /writer

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run monitor.py when the container launches
CMD ["python3", "writer.py"]