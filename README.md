## Vintage Story - Server Query

This is a small query tool used with Simple Server status query mod: https://mods.vintagestory.at/show/mod/27202
Provides a simple interface used with servers running in docker.


Tested in Linux only. no doors or windows.
Tested on X86_64 only.

Solution is built for local usage,

### Usage:

1. Edit the ```build.sh``` and update ```DOCKER_TAG``` to point to your own registry (if have any). This is needed to push your build container image to somewhere, if you want to build and run on separate machines.
2. Run ```build.sh```, which will build the docker image and uploads to a registry of your choice.
3. Run your freshly built container. Set VS_URL Env var to the VS instance (e.g. http://vintagestory.google.com:9898)


    3a. Docker compose: See  ```compose-example.yml``` for sample usage (Bonus: NFS mounting is how I use it, don't forget to update with your IP).


    3b. Docker run (update DOCKER_TAG to your tag used for building.): ```docker run -p 5000:5000 <DOCKER_TAG>```

4. Profit

Screenshot:
<img width="1316" height="463" alt="vs-query" src="https://github.com/user-attachments/assets/1f1767ed-e52d-430a-a571-5bcea62369d9" />
