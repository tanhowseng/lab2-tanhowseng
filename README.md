# Network Topology with Mininet

This repository is lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Execution

> TODO: 
> * Describe how to execute your program
> * Show the screenshot of using iPerf command in Mininet

### topology.py

1. Simply run the python file using the command: ./typology.py
![picture](runprogram.JPG)
![picture](runprogram2.JPG)

2. To check if the topology is correct, use the iPerf command to measure the network and produce the measurement results. Compare the results with the expected results given.
![picture](iperfcommand.JPG)

---
## Description

### Mininet API in Python

> TODO:
> * Describe the meaning of Mininet API in Python you used in detail

* Mininet is a network emulator. It creates a realistic virtual network, running real kernel, switch and application code, on a single machine (VM, cloud or native). It tuns a collection of end-hosts, switches, routers, and links on a single LInux kernel. 

### iPerf Commands

> TODO:
> * Describe the meaning of iPerf command you used in detail

* iPerf is a tool for active measurements of the maximum acheiveable bandwidth on IP networks. It supports tuning of various parameters related to timing, buffers and protocols (TCP, UDP, SCTP with IPv4 and IPV6)

### Tasks

> TODO:
> * Describe how you finish this work step-by-step in detail

1. **Environment Setup**<br />
* Step 1: <br />
I clicked the link provided to obtain the files required for the lab.<br />
* Step 2:<br />
I used Putty(instead of Pietty) to login to my linux container through ssh. <br />
* Step 3:<br />
I proceeded to clone my github files using the following command in Putty:<br />
> `$ git clone https://github.com/nctucn/lab2-<GITHUB_ID>.git Network_Topology` <br />

* Step 4:<br />
After logging in to my container, I ran Mininet for testing.<br />
> ` $ sudo service openvswitch-sitch start` <br />
 `$ sudo mn`

2. **Example of Mininet**
* Step 1: <br />
In the example, the topology depicted includes one switch and two hosts. From this I could infer that the "SingleSwitchTopo" class object written in the example.py code refers to the build of the topology, with "switch" and "host" as their attributes. The "addLink" function creates the link attributes with paramters such as bandwidth, loss and delay.
* Step 2:<br />
In the main init function, we can tell that the function "simpletest" is called. If we look closely at "simpletest" function, we could also tell that the class object "SingleSwitchTopo" is also called. From this I could infer that I should modify the function and the class object to create my own topology.
* Step 3:<br />
If there is no "net.stop" function called after building the virtual network topology, then the virtual network topology remains in mininet. Run the command "sudo mn -c" to reset the mininet virtual network.
> `$ sudo mn -c`


3. **Topology Generator**
* Step 1: <br />
Based on the example.py, I created a modified topology that matched the one depicted in the picture "topo1.png". <br />
![picture](topo1.png)
* Step 2: <br />
Remove the 'for-loops' used in example.py. Unlike the example topology, which only contains one central switch and two other hosts surrounding it, my topology is done is a straightforward manner where each switch or host is define specifically and then later linked together individually. This does away the need for 'for-loops'.<br />
![picture](multiswitchtopo.JPG)
![picture](addlink.JPG)

* Step 3: <br />
Other requirements are to dump every hosts' connections in the program, and to enter the Mininet's CLI mode in the program.<br />
![picture](requirements.JPG)

4. **Measurement**
* Step 1: <br />
Run the following iperf commands to receive the results of the network measurements. Compare the results with the given expected result.<br />
![picture](iperfmeasurement.JPG)

---
## References

Mostly the example.py and the lab2_tasks PDF file. Other than that, I also used some of these websites: 
1.	Python Classes and Objects: https://www.w3schools.com/python/python_classes.asp
2.	Vim tips and tricks: https://www.cs.swarthmore.edu/oldhelp/vim/selection.html


* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
    * [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
    * [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
    * [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
    * [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
    * [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
    * [Mininet 學習指南](https://www.sdnlab.com/11495.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributors

> TODO:
> * Please replace "YOUR_NAME" and "YOUR_GITHUB_LINK" into yours

* [YOUR_NAME](YOUR_GITHUB_LINK)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3
