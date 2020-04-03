FROM python:3

WORKDIR /monitor

COPY . /monitor

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run monitor.py when the container launches
CMD ["python3", "monitor.py"]