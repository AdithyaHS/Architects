FROM holbertonschool/ubuntu-1404-python3
MAINTAINER Deepak Hanumanthaiah "dhanuman@iu.edu"
COPY . /index
WORKDIR /index
RUN pip3 install -r requirements.txt
CMD ["python3", "index.py"]
