# What are containers and how to use them with CTF or in general

Containers often confuse people on how they work, what they do, and why they are used.


I will explain all three of these things, and by the end I will even have a lab for you to try out. Lets begin.


### Virtualization

In the context of computers, virtualization is a way to simulate/run an isolated system with allocated resources for that simulation. For example I can have my computer run two different operating systems at once, because I allocate parts of my resources such as storage, cpu, and ram, to be used to run this "simulation" or operating system, this operating system acts like a normal computer and independently uses its allocated resources to run. With virtualization you can do this with multiple systems and have your hardware split up into multiple simulations. This might sound weird at first but heres an analogy: Say you have one lagre grass field and there is soccer practice and football practice scheduled, What you can do is split the field in two , and the soccer team will do their own thing on one side while the football team does their thing on the other side. Same concept with virtualization. When I say simulate, I say this because the system being virtualized is controlled by an underlying software that handles setting it up (hypervisor), but the system acts just like it would if it wasn't running on top of this software. Using virtualization gives us lots of flexibility and also isolates different abstract parts of resources, like how the one big grass field is split up and treated as both a soccer and football field.


We typically use virtualization of systems for: cloud/server purposes, testing operating systems, saving money by not buying more hardware, using legacy systems, etc.


![image](https://github.com/user-attachments/assets/5eca19d8-a2b6-4f02-8c90-79d4f0f33e1d)



### Containerization


Containerization is a type of virtualization, when we say containerization we are talking about applications. Similar to how we may want to run different systems independently on one piece of hardware, we also want to run different applications independently on one operating system. To tie this back to our earlier example, we split up the field between soccer and football, but what if multiple football teams want to have their practice at the same location at the same time? Since we have such a big field, we can divide the designated football field so both teams can practice independently of each other. This means the two football teams will both have their own practice independently. Each team will practice the with equipment they need, while using the painted lines and benches on the football field that lies on one big grass feild. This is the same with containers, we package the requirements of an application with all of the software and libraries it needs, and when we run it, it uses its own files to independently run on the operating system, isolating itself from other processes. You can think of this as another type of virtualization because like virtual machines, the containers are sharing a common resource but act independently of everything else with the help of underlying software (Which we will get into next)


We typically use containers for: cloud/server purposes, development, efficiently sharing software (using containerization its easy for multiple environments to run your code without issue as long as they have the container set up properly), quickly deploying apps, etc.


![image](https://github.com/user-attachments/assets/3d969a52-9801-4c0c-b76c-0bbd2737baa5)


# Docker


Now that I have explained the concepts, it is time to talk about docker.


Docker is a software that you use for containerization. Docker allows you to build, deploy, run, manage, and update containers. It is open source and very widely used across many industries where its flexibility and efficiency are very beneficial.


What is a docker container? Its a running instance of a docker image that was constructed by a docker file. That may sound confusing but going back to the previous analogy will make it easier.


Lets say we have our football feild with multiple teams that are practicing, different teams might need different equipment, maybe one team needs tackle dummies, maybe another team needs cones, and most teams will probably have a unique playbook. Teams also might need the field prepared in different ways depending on the drill. If we give each team the equipment they need and prepare the field as necessary, now they can practice, and lets say the fields are closed on certain days, thats ok because as long as the team has a list of what they need and the field can provide everything on that list, they can move to another field and keep practicing without issues. 


Same with docker containers, with the use of docker file, image, and container, we can give a program everything it needs to run on any computer*.


## Docker File


The docker file is a list/guide/recipie/set of instructions that is used to configure a docker image. Think of it as the football team making a list of all the equipment they need as well as how the field should be set up.


## Docker image


The docker image is the package of all binaries, configurations, libraries, and files necessary for a container. Its the base template that your program will run off of. Think of it as the actual field with all of the equipment provided and the field properly set up for practice. 


## Docker container


The docker container is a process that is an instance of an image that runs as an isolated process. When I say instance, I mean that it is an occurence of a program that is based off of the image. So based off the field that has been set up and equiped, the football team is like that process that uses the equipment and field. Some football teams may share the same equipment and set up requirements, so we can say those two teams are different instances/ processes that are based on the same base field setup and equipment.


## Docker program


To put this all together, we use docker to combine and manage each of these three things. Docker will read the docker file, use it to create the necessary image, and use this image to run containers/processes. We can say docker is the manager of the entire football field, the manager will get a list of what the football team needs, have everything set up and provided, and let the football team do their thing independently. 


Back to the computer part, docker is great for many organizations because they now have an easy and standard way to share, deploy, build, package, and run any application or service needed, this goes far beyond organizations, maybe we want to share an app we made with a friend, maybe we want to try a new appp, or maybe we want to run a ctf challenge on our computers locally. 


### Important stuff to know about your OS and Docker


*One important note before we continue, while docker allows for flexibility in running an app in multiple environments, it is also OS specific. If an image was configured to run with operating system 1 (OS1) then it wont run on operating system 2 (OS2) unless we either: create a (OS1) VM and run the image in that vm, or make a new image that works with OS2. Think about the analogy, say we have a group of kids that want to play a sport, they bring a football but they end up at a soccer field, they can either treat part of that soccer field as a football field (virtualization), go to a football field (use a different computer with the proper OS), or just get a soccer ball and play soccer instead (Use a new image with the correct operating system). Operating systems use different architectures, and while some powerful tools like virtualization have been made to bridge this gap better, there are still a few limitations.


Since we are using docker desktop on windows, we dont really have to worry about this too much. The docker engine technically runs on linux, but it also runs on windows because under the hood there is a little bit of virtualization that runs linux, which docker will use. This little bit of virtualization is much different from tradtional virtualization and it is very lightweight compared to actually making a VM, and this should all happen automatically (Note). This means if you are using windows, you should be fine. If you have a windows container no worries either because you already have the architecture you need.


If you are linux you basically have everything docker needs so you are good, but if you are given a windows container you will have to create a windows VM because unlike how windows has easy lightweight virtualization options for linux, linux doesn't have that same support for windows programs appart from creating a separate VM.


Note: If you are a windows user you are probably wondering, if docker is using a vm with windows, then why not just make a linux vm and use docker there? You definitely can, but the type of virtualization being used when running docker on windows is very lightweight and more efficient, but you may prefer a linux VM, either way is fine its up to you. The great thing is that docker takes care of alot of stuff for us. 


If this is alot to understand thats ok, Docker can be confusing. Before reading on I reccomend having a solid grasp of everything I talked about up to this point, because now we are actually going to use docker and run two challenges I made. If you have any questions dm me or ping me in the discord if you are in the club. 


# Using Docker 


For this section I will split into multiple parts:
- Downloading docker
- Creating a Docker File
- Creating an image based on the Docker File
- Run a container based off of the image
- Extra notes about Docker
- 

### Downloading Docker


To start we have community or enterprise edition. Assuming you arent a big company reading this, you should download community because it is free. 


If you go to the docker website you will see a button that says "Download Docker Desktop", from there choose the operating system you use and you will get Docker with a GUI. If you are sick in the head and you don't like using GUIs, you can use your terminal too, just use the "Docker" command once installed. A good way to check if docker installed correctly is to go to your terminal and type Docker --version and if it tells you the version you're good.


### Creating Docker File


For this walkthrough, I am going to use a basic flask server as an example, here is the code: 


```
import flask
from flask import jsonify

app = flask.Flask(__name__)

@app.route("/")
def index():
    return jsonify(message = "Working docker example")

if __name__ == "__main__":
    app.run()
```

All this does is returns a json message telling me this is a working docker example, very simple.


Now I will create my Docker file.


To begin, its important to understand that Docker images consist of layers. These layers are stacked in a way that higher layers depend on the layers below. We say that the parent layer is the beginning layer that sets up a basic foundation of the image. 


When working with docker files, it will consist of commands to set up our image. These are some basic commands that are important to know:


- FROM: Specify the parent image/layer, you will build upon this
- WORKDIR: specify where docker should run necessary commands when running the image, where do you want the container to run?
- RUN: run commands necessary for the container, like installing the packages you need
- COPY: copy files from directories
- ADD: like COPY, but can also use URLs and Directories, and also handles compressed files
- ENTRYPOINT: the first command that gets run when you start a container
- CMD: give a command to run when starting a container, very similar to ENTRYPOINT but it can be over ridden, ENTRYPOINT cant
- EXPOSE: which port your container will communicate on


There are many more commands but for this lab I want you to focus on these. 


To start, lets use out FROM command, in our case we are just using a very simple python flask server so I will set this to python:3.10 for the version of python that I am running.


The next step is using the ADD command, I will put "ADD example.py .", this adds the code I showed earlier to current directory of the container. 


Next I will use the RUN command: "RUN pip install flask", this will give us the flask library which lets us run a simple web server, notice how I use pip, thats because we are going based off of python


Now I will use CMD to specify a command and its parameter which will run when the container starts, here is what that will look like: "CMD ["python", "./example.py"]", this means that when the container starts, it will run this command, this command tells python to run example.py which is located in the current directory.  


This gives us our dockerfile: 


```
FROM python:3.10

ADD example.py .

RUN pip install flask

CMD ["python", "./example.py"]
```

Lets turn this into an image.


### Creating the image


To create the image we will use the command: 
```docker build -t example-image .```


This builds a new image and the -t names it example-image. When I run this command here is what happens (Make sure you are doing this in the same directory as the docker file and code you are adding to the image.)


![image](https://github.com/user-attachments/assets/504738a5-7255-414d-99b2-0d768daba27e)


Lets open the docker app and find the image: 


![image](https://github.com/user-attachments/assets/69904030-846b-4079-b379-f9168c25203b)


We found our image, its pretty big but I probably couldve optimized it more, you can always delete images when you are done if they are taking up too much space. (Jarrett 4 hours later here, it turns out you can instead use FROM python:3.10-slim and that makes the size much less)


### Run a container from our image


Now we can run our containers, I am going to use the command line


I will run:


```docker run -d -p 8082:5000 example-image```


This runs a container with less logs and also does something called publishing a port. When you run a container, it is so isolated that the port it is running on isn't accessible to me by default. To connect to our container from the host, we can forward traffic between our two environments by giving a port for our container to interact on, and a port for us to interact with, this forwards traffic from our port 8082 to the containers port 5000. 


If you dont know what ports are in networking here is a very simplified explanation, different computers need to send different types of data to each other, how do we organize all of this data? Ports. We can give a number to different types of services and when communicating with a specific service, we communicate over that specific port, so if we visit a website we use 80 or 443, if we want to use a shell on another system we use port 23, if we want to use this shell with encryption we use port 22. In our case, we are using port 8082 to talk to our flask server. 


Another thing for those unfamiliar with networking, we are reaching this server on ip 127.0.0.1, what does this mean? This address was made to specifically refer back to our own machine, this can be useful for a variety of reasons, in our case, we are running this server on our own computer, this means that when we communicate with it, we arent using any internet, we are just talking to ourselves on different ports.


At this point I realized I made a small mistake that meant I needed to fix my python and remake the image but dont worry, its just a small change:


```app.run(host="0.0.0.0", port=5000)``` Nothing really changed from the earlier steps so we will just keep going.


With that explained lets run the command, here is what we get:


![image](https://github.com/user-attachments/assets/00472fbd-3ce2-4d98-8d6f-d5fd9a7eb5b6)


serene_saha is just a random name because i didnt specify a name for the container, lets try to visit the website.


![image](https://github.com/user-attachments/assets/c4ccdd46-2e9d-468e-bedb-29d46dbf7e95)


We got it working. 


Now if I want I can just stop or delete the container or keep it going. The Docker GUI is pretty straight forward.


That was my first time successfuly using docker, you learn alot when teaching.


### Extra notes


What I did was a basic introduction to docker, there is so much more to it, and if you all want I can go further, but for now I think this is a good place. Before moving on I want to quickly talk about other parts of docker that are worth noting.


- Docker compose
  

        Docker compose is an efficient way to deal with multiple containers and easily reproduce desired containers. It is basically a config file in YAML that is easier to read, type out, and use woth containers.


- Volumes
  

        Basically, containers sometimes need data or they generate data. We may need data from the container too, the problem is that restarting or deleting a container can cause all the data associated with that container to be lost. To fix this we use volumes, now we can access and save data that is generated by or needed by the container, even if the container is reset or deleted.


- Docker hub


        What if there is an image that has already been generated for what you need, this is where docker hub comes in. Think about it like a GitHub but for docker images. This offers countless benefits like efficiency, automation, security, access to many images, and collaboration. You can also upload your own image if you want.


- Docker security

  
        If you plan on using docker more that is great, just remember to keep security in mind. For the most part Docker very secure due to its isolation, but understanding the associated vulnerabilites of docker is important to know, especially if you want to use Docker to host servers on the internet.


There is probably more I could mention but I think I nailed the important stuff. It is time to talk about using docker for CTF, and using what you learned to try out a lab.


# Docker and CTF


Here we will talk about how docker and CTF go together, if you are Blue Team reading this or maybe you just aren't big on CTF, I reccomend you keep reading, even if you dont do CTF following along will help you understand Docker more.


In many ctf challenges, especially web, the challenge authors will provide us with the source code. This is good because we can look at the code and find a vulnerability or reverse the program. Some challenges will also provide us with docker files, this allows participants to test the challenge locally on their own computer using containers. This is beneficial for many reasons. Once the competitor finds the fake flag on their container, they can go to the real server and run the same exact exploit and get the flag. 


Docker is also Useful for those hosting a CTF. Using containers, they can deploy multiple challenges and manage them on a dedicated server that runs the containers. 


Docker is also great for general offensive stuff too, they can be used in cybersecurity labs like VMs (Be very careful) as well as quickly deploy tools. 


### Lab


Since we are talking about CTF, I made a lab for you all. I made two very simple challenges for you to host on your own computer using docker. I will provide the original challenge code and a dockerfile to configure the image, I will also give you the commands to run the container properly. When setting this all up, take the time to understand the process and how everything is working, I was almost going to make you all write the Dockerfile yourselves but that would've probably been too far. 


Usually in real CTFs the challenge code you download will include a fake flag like: "flag{test}", and you get the real flag from hacking the server. In this case I am not actually hosting these challenges so the code I give you will have the real flag, even though technically you can just look at the code and see the flag without actually solving the challenge thats the boring way of doing it. To prove to me you were able to get the flag the intended way show me a screenshot of you getting the flag running from a container.


# Conclusion


This was all a basic overview of Docker. When I first started out in cybersecurity I couldnt wrap my head around docker, same with many people starting out, so I hope this tutorial and lab i made helped. This was a cool little project and I look forward to doing more stuff. Thank you for reading my tutorial and completing my lab.



# References

https://nickjanetakis.com/blog/differences-between-a-dockerfile-docker-image-and-docker-container

https://stackoverflow.com/questions/23735149/what-is-the-difference-between-a-docker-image-and-a-container

https://jfrog.com/devops-tools/article/understanding-and-building-docker-images/

https://www.geeksforgeeks.org/what-is-dockerfile-syntax/

https://www.docker.com/blog/how-to-dockerize-your-python-applications/

https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/

https://medium.com/@leroyleowdev/the-missing-piece-why-docker-cant-run-windows-containers-on-linux-but-can-run-linux-containers-d0defc5588c1

https://askubuntu.com/questions/1163283/does-wsl2-run-linux-in-a-virtual-machine-or-alongside-the-windows-kernel

https://medium.com/@leroyleowdev/the-missing-piece-why-docker-cant-run-windows-containers-on-linux-but-can-run-linux-containers-d0defc5588c1

https://arsanatl.medium.com/understanding-python-virtual-environments-an-in-depth-guide-6ffddab02498

https://adamtheautomator.com/docker-compose-tutorial/

https://stackoverflow.com/questions/34809646/what-is-the-purpose-of-volume-in-dockerfile

https://www.geeksforgeeks.org/what-is-docker-hub/

https://www.youtube.com/watch?v=DQdB7wFEygo
