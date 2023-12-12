# X by 2 Chat AI

Working on building an inhouse AI for. reasons. boredom?

## Docker build

To build this container, create a directory (at root) `./model_data` and add a model data set named `dataset.gguf`

Container runs on port 5005.

1. Build container `docker build -t xby2/ai .`

## Docker run

1. Run container on specified port `docker run -t --name eksy-0 -e SERVICE_PORT='5005' -p 5005:5005 xby2/ai:bananatiger`
