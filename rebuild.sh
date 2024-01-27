docker rm -f sum
docker build . --tag summarization
docker run -itd --name sum --network=host summarization:latest
docker logs -f sum