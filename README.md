# Containerizing_Neural_Nets
Containerizing Neural Network Apps for Medical Compute

Project Logistics:
Mentors: Rudolph Pienaar email: rudolph.pienaar@childrens.harvard.edu;  Sandip Samal email: sandip.samal@childrens.harvard.edu
Will the project be open source: yes
 
Preferred Past Experience:
Python: Required
Docker: Valuable
Neural Network Python Libraries: Valuable

Project Overview:
Background: One might argue that the potential impact of computation in medicine and medical care is still in its infancy. While computational based medical research has been a very active field over the past two decades -- witness image processing, machine intelligence and neural networks, protein modeling, genomics -- the practical impact of all this computational power is not fully realized.

Many possible reasons exist for the relatively low clinical impact of advanced computing, but for the purposes of this cloud course we might consider the lack of easy access for non-technical users to both data and compute to be the largest obstacle.

In this project, you will develop and expand some important medical compute applications and help to make them deliverable to clinical users at Boston Children's Hospital. The applications are neuro magnetic resonance image segmenters, i.e. apps that take a brain MRI and classify each voxel as one of multiple classes. This is a classic convolutional Neural Network (cNN) type problem and though you won't necessarily be building the cNNs from scratch (we have some already under development) you will help to deploy them to the MOC and use the ChRIS platform (also developed at BCH with support from Red Hat and others). 

ChRIS has a web-based GUI and an infrastructure that allows non technical users to easily run these kind of apps on the MOC. You will help bring these apps to clinical end users using ChRIS.
 
Project Specifics: In this project you will:

* Explore two neural network classifier types -- one that attempts to segment multiple classes concurrently and another solution type that leverages many classifiers, each tuned though to only one class. You will help run these on the MOC

* Create ChRIS plugin apps of these classifiers and continue work that already exists

* Add these to the ChRIS store and ultimately have them available in a ChRIS instance that exists at BCH

* If there is time, to build classifiers for *both* x86_64 (i.e. conventional consumer computer architecture) as well as IBM Power9 architectures that exist at the MOC.

ChRIS project
https://chrisproject.org 
Background video on ChRIS and the MOC
https://redhat.com/chris 




Some Technologies you will learn/use:
System design
ChRIS plugin development
Full stack problem solving
