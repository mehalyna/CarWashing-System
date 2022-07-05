#Creating container
sudo docker run --name psqltest -e POSTGRES_PASSWORD=secret -e POSTGRES_USER=dev -e POSTGRES_DB=dev -d postgres:14

Digest: sha256:4ba3b78788bb284687376b9c1e0565b245375ddee0fe14cef25e315b6bd88b1a
Status: Downloaded newer image for postgres:14
d2a0bb6302ef967e58ab39a87d6c556c33cf3dbb5dcab0c6c9ae6e9f556dc512

#Active containers
svetoslav@svet:$ docker ps

CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS         PORTS      NAMES
d2a0bb6302ef   postgres:14   "docker-entrypoint.s…"   7 seconds ago   Up 5 seconds   5432/tcp   psqltest

svetoslav@svet:~$ sudo docker ps -a
CONTAINER ID   IMAGE         COMMAND                  CREATED       STATUS                   PORTS      NAMES
d2a0bb6302ef   postgres:14   "docker-entrypoint.s…"   2 hours ago   Up 2 hours               5432/tcp   psqltest
55d26028247e   postgres      "docker-entrypoint.s…"   3 hours ago   Created                             some-postgres


#Checking IP
docker inspect -f '{{.NetworkSettings.IPAddress}}' psqltest
172.17.0.2

docker exec -it psqltest psql --user dev
psql (14.4 (Debian 14.4-1.pgdg110+1))
