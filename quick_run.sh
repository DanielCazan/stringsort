# !/bin/sh
printf "\nREMOVING previous instances of this same image build"
docker rmi csvstringsort-docker -f
printf "\nBUILDING Dockerfile.build\n"
docker build -t csvstringsort-docker -f Dockerfile.build .
printf "\nMAPPING -v /shared_target:/app/csvstringsorter"
printf "\nRUNNING python csvstringsorter.py\n"
docker run --rm -v /shared_target:/app/csvstringsorter -it csvstringsort-docker python csvstringsorter.py