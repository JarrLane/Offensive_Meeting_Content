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

*One important note before we continue, while docker allows for flexibility in running an app in multiple environments, it is also OS specific. If an image was configured to run with operating system 1 (OS1) then it wont run on operating system 2 (OS2) unless we either: create a (OS1) VM and run the image in that vm, or make a new image that works with OS2. Think about the analogy, say we have a group of kids that want to play a sport, they bring a football but they end up at a soccer field, they can either treat part of that soccer field as a football field (virtualization), go to a football field (use a different computer with the proper OS), or just get a soccer ball and play soccer instead (Use a new image with the correct operating system). Operating systems use different architectures, and while some powerful tools like virtualization have been made to bridge this gap better, there are still a few limitations.

Since we are using docker desktop on windows, we dont really have to worry about this too much. The docker engine technically runs on linux, but it also runs on windows because under the hood there is a little bit of virtualization that runs linux, which docker will use. This little bit of virtualization is much different from tradtional virtualization and it is very lightweight compared to actually making a VM, and this should all happen automatically (Note). This means if you are using windows, you should be fine. If you have a windows VM no worries either because you already have the architecture you need.

If you are linux you basically have everything docker needs so you are good, but if you are given a windows container you will have to create a windows VM because unlike how windows has easy lightweight virtualization options for linux, linux doesn't have that same support for windows programs appart from creating a separate VM.

Note: If you are a windows user you are probably wondering, if docker is using a vm with windows, then why not just make a linux vm and use docker there? You definitely can, but the type of virtualization being used when running docker on windows is very lightweight and more efficient, but you may prefer a linux VM, either way is fine its up to you. The great thing is that docker takes care of alot of stuff for us. 

If this is alot to understand thats ok, Docker can be confusing. Before reading on I reccomend having a solid grasp of everything I talked about up to this point, because now we are actually going to use docker and run two challenges I made. If you have any questions dm me or ping me in the discord if you are in the club. 

# Using Docker 

For this section I will split into multiple parts:
- Downloading docker
- Creating a Docker File
- Creating an image based on the Docker File
- Run a container based off of the image

### Downloading Docker

To start we have community or enterprise edition. Assuming you arent a big company reading this, you should download community because it is free. 

If you go to the docker website you will see a button that says "Download Docker Desktop", from there choose the operating system you use and you will get Docker with a GUI. If you are sick in the head and you don't like using GUIs, you can use your terminal too, just use the "Docker" command once installed. A good way to check if docker installed correctly is to go to your terminal and type Docker --version and if it tells you the version you're good.

### Creating Docker File

For this walkthrough, I am going to use a basic flask server as an example, here is the code: 

'''
import flask
from flask import jsonify

app = flask.Flask(__name__)

@app.route("/")
def index():
    return jsonify(message = "Working docker example")

if __name__ == "__main__":
    app.run()
'''
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

We found our image, its pretty big but I probably couldve optimized it more, you can always delete images when you are done if they are taking up too much space.

### Run a container from our image

Now we can run our containers, I am going to use the command line

I will run:

```docker run -d -p 127.0.0.1:8082:5000 example-image```

This runs a container with less logs and also does something called publishing a port. When you run a container, it is so isolated that the port it is running on isn't accessible to me by default. To connect to our container from the host, we can forward traffic between our two environments by giving a port for our container to interact on, and a port for us to interact with, this forwards traffic from our port 8082 to the containers port 5000. 

If you dont know what ports are in networking here is a very simplified explanation, different computers need to send different types of data to each other, how do we organize all of this data? Ports. We can give a number to different types of services and when communicating with a specific service, we communicate over that specific port, so if we visit a website we use 80 or 443, if we want to use a shell on another system we use port 23, if we want to use this shell with encryption we use port 22. In our case, we are using port 8082 to talk to our flask server. 

Another thing for those unfamiliar with networking, we are running this server on ip 127.0.0.1, what does this mean? This address was made to specifically refer back to our own machine, this can be useful for a variety of reasons, in our case, we are running this server on our own computer, this means that when we communicate with it, we arent using any internet, we are just talking to ourselves on different ports.

With that explained lets run the command, here is what we get:





