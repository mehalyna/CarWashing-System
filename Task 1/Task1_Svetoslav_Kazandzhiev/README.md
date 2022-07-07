READ me

#Building image
svetoslav@svet:~/docker_python$ sudo docker build -t python_game .

#Check if the image has been created
svetoslav@svet:~/docker_python$ docker images

REPOSITORY       TAG       IMAGE ID       CREATED         SIZE
python_game      latest    941144af7d2b   9 minutes ago   143MB

#Run the script
svetoslav@svet:~/docker_python$ docker run python_game

#Output
svetoslav@svet:~/docker_python$ docker run python_game
INFO:my_first_docker_app:It works, go to the next iteration.
INFO:my_first_docker_app:It works, go to the next iteration.
