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

### Docker


Now that I have explained the concepts, it is time to talk about docker.

Docker is a software that you use for containerization. Docker allows you to build, deploy, run, manage, and update containers. It is open source and very widely used across many industries where its flexibility and efficiency are very beneficial.

What is a docker container? Its a running instance of a docker image that was constructed by a docker file. That may sound confusing but going back to the previous analogy will make it easier.

Lets say we have our football feild with multiple teams that are practicing, different teams might need different equipment, maybe one team needs tackle dummies, maybe another team needs cones, and most teams will probably have a unique playbook. Teams also might need the field prepared in different ways depending on the drill. If we give each team the equipment they need and prepare the field as necessary, now they can practice, and lets say the fields are closed on certain days, thats ok because as long as the team has a list of what they need and the field can provide everything on that list, they can move to another field and keep practicing without issues. 

Same with docker containers, with the use of docker file, image, and container, we can give a program everything it needs to run on any computer*.

The docker file is a list/guide/recipie/set of instructions that is used to configure a docker image. Think of it as the football team making a list of all the equipment they need as well as how the field should be set up.

The docker image is the package of all binaries, configurations, libraries, and files necessary for a container. Think of it as the actual field with all of the equipment provided and the field properly set up for practice. 

The docker container is a process that is an instance of an image that runs as an isolated process. When I say instance, I mean that it is an occurence of a program that is based off of the image. So based off the field that has been set up and equiped, the football team is like that process that uses the equipment and field. Some football teams may share the same equipment and set up requirements, so we can say those two teams are different instances/ processes that are based on the same base field setup and equipment.

To put this all together, we use docker to combine and manage each of these three things. Docker will read the docker file, use it to create the necessary image, and use this image to run containers/processes. We can say docker is the manager of the entire football field, the manager will get a list of what the football team needs, have everything set up and provided, and let the football team do their thing independently. 

Back to the computer part, docker is great for many organizations because they now have an easy and standard way to share, deploy, build, package, and run any application or service needed, this goes far beyond organizations, maybe we want to share an app we made with a friend, maybe we want to try a new appp, or maybe we want to run a ctf challenge on our computers locally. 

One important note before we continue, while docker allows for flexibility in running an app in multiple environments, it is also OS specific. If an image was configured to run with windows then it wont run on linux unless we either: create a windows VM and run the image in that vm, or make a new image that works with linux. Think about the analogy, say we have a group of kids that want to play a sport, they bring a football but they end up at a soccer field, they can either treat part of that soccer field as a football field (virtualization), go to a football field (use a different computer with the proper OS), or just play soccer instead (Use a new image with the correct operating system).










