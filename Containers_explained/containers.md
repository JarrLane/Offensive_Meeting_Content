# What are containers and how to use them with CTF or in general

Containers often confuse people on how they work, what they do, and why they are used.

I will explain all three of these things, and by the end I will even have a lab for you to try out. Lets begin.

### Virtualization

In the context of computers, virtualization is a way to simulate/run an isolated system with allocated resources for that simulation. For example I can have my computer run two different operating systems at once, because I allocate parts of my resources such as storage, cpu, and ram, to be used to run this "simulation" or operating system, this operating system acts like a normal computer and independently uses its allocated resources to run. With virtualization you can do this with multiple systems and have your hardware split up into multiple simulations. This might sound weird at first but heres an analogy: Say you have one lagre grass field and there is soccer practice and football practice scheduled, What you can do is split the field in two , and the soccer team will do their own thing on one side while the football team does their thing on the other side. Same concept with virtualization. When I say simulate, I say this because the system being virtualized is controlled by an underlying software that handles setting it up (hypervisor), but the system acts just like it would if it wasn't running on top of this software. Using virtualization gives us lots of flexibility and also isolates different abstract parts of resources, like how the one big grass field is split up and treated as both a soccer and football field. 

Here is a blender model showing this concept: 

### Containerization

Containerization is a type of virtualization, when we say containerization we are talking about applications. Similar to how we may want to run different systems independently on one piece of hardware, we also want to run different applications independently on one operating system. To tie this back to our earlier example, we split up the field between soccer and football, but what if multiple football teams want to have their practice at the same location at the same time? Since we have such a big field, we can divide the designated football field so both teams can practice independently of each other. This means the two football teams will both have their own practice independently. Each team will practice the with equipment they need, while using the painted lines and benches on the football field that lies on one big grass feild. This is the same with containers, we package an application with all of the software requirements it needs, and when we run it, it uses its own files to independently run on the operating system, isolating itself from other processes. 

Here is a blender model showing this concept: 
