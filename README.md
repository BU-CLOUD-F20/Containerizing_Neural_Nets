# Containerizing Neural Network Apps for Medical Compute
## Mentors:
-  Rudolph Pienaar
- Sandip Samal

## Group Members:
- Xiaoyu An
- Kenneth Krebs
- Brian Mahabir
- Cagri Yoruk
- Tingyi Zhang

## Sprint Presentations
- [Sprint 1](https://github.com/BU-CLOUD-F20/Containerizing_Neural_Nets/blob/master/DemoSlides/Sprint1.pdf)
- [Sprint 2](https://github.com/BU-CLOUD-F20/Containerizing_Neural_Nets/blob/master/DemoSlides/Sprint2.pdf)
- [Sprint 3](https://github.com/BU-CLOUD-F20/Containerizing_Neural_Nets/blob/master/DemoSlides/Sprint3%20.pdf)
- [Sprint 4](https://github.com/BU-CLOUD-F20/Containerizing_Neural_Nets/blob/master/DemoSlides/Sprint4.pdf): 
- [Sprint 5](https://github.com/BU-CLOUD-F20/Containerizing_Neural_Nets/blob/master/DemoSlides/Sprint%205.pdf)
	- [Video](https://youtu.be/wotojEguifg)

## 1. Vision and Goals Of The Project: 

Over the past few decades, there has been a tremendous amount of work done in the area of computational medical research. Researchers used image processing, machine learning and neural networks to determine certain patterns in diseases. However, we can question the practical impact of these improvements. The lack of easy access to data and computational power became the largest obstacle for the non-technical users. Our vision is to develop a ChRIS plugin that provides a text report of the MRI images using convolutional neural networks for clinical users at Boston Children's Hospital.

* Use Convolutional neural networks to segment brain MRI images.
* Create ChRIS plugin applications to run the neural network.
* Add the created apps to the ChRIS store and have them available in a ChRIS instance at Boston Children’s Hospital.


## 2. Users/Personas Of The Project:

The main target for this project is non-technical clinical end users mainly healthcare providers or researchers. However, developers are also considered for potential development and improvement.

* As a clinical user, I want to be able to easily access both data and computation results of medical images, therefore I need a user-friendly platform ChRIS whose plugins can perform medical level computation for me.


## 3.   Scope and Features Of The Project:

* Explore two neural network classifier types:
	* A network classifier that attempts to segment multiple classes concurrently and provide classification of each part of the brain. 
	* A network classifier that leverages many classifiers, each tuned to only one class pertaining to a specific anatomical feature of the brain. 
* Convert DICOM to file types compatible with the classifiers.
* Build or expand some applications that implement the explored neural networks, which can generate detailed reports of MRI images of a patient's neuroanatomy.
* Ability to run the applications on ChRIS as plugins. 
* (possible) Build classifiers for x86_64 and for IBM Power9 architectures that exist at the MOC.

## 4. Solution Concept:

### Design Implications and Discussion:

Below is a description of the system components that are building blocks of the architectural design:

ChRIS: an open source distributed data and computation platform. The frontend and backend reside within a hospital or institutional network. Data from the network can be run on plugins. 

Massachusetts Open Cloud:

* Data from ChRIS is processed and initialized for specific plugins
* Computation setting for the image processing of the desired plugins. Computational output is transferred back to the ChRIS platform.

<p align="center">
<img width="469" alt="Arch_final@2x" src="https://user-images.githubusercontent.com/56164075/101412428-98917080-38b0-11eb-8ec2-c6fe25ea5fd1.png">
</p>
Figure 1: ChRIS and MOC architecture
<br/>

![entireWorkflow@3x](https://user-images.githubusercontent.com/56164075/101412287-549e6b80-38b0-11eb-968b-9ac1e1d1d544.png)

Figure 2: Workflow Plugin Architecture
Design Implications and Discussion:

Key design decisions and motivation behind them.
* By deploying applications and computations within the cloud infrastructure, medical innovation can be driven by increasing amounts of data, computations and collaborations. 
* Computations run in containers on the Massachusetts Open Cloud that are lightweight and recreatable, this allows faster computation and results. 
* Containerizing allows workflows to be easily distributed.

## 5. Acceptance Criteria:

Minimum acceptance criteria includes a pipeline for the Chris app that can turn a host of MRI images into a text report regarding specific attributes of brain anatomy.

## 6.  Release Planning:
### Release #1 due (due Week 5):
Understanding infrastructure and plugins. Install necessary components to begin:
* Get familiar with ChRIS, web/command-line usage
* Set up develop environment (Linux, Docker)
* Research on neural networks that we need in this project
* Learn how to use the MOC

### Release #2 (due by Week 7):
* Begin conversion of DICOM images to files suitable for the classifiers
* Get familiar with ChRIS CNN plugin
* Begin work on few small classifiers
* Begin working on ChRIS connection to the cloud

### Release #3 (due by Week 9): 
* Be able to explore some existed CNN related plugins on ChRIS
* Finish a simple MRI classifiers application demo

### Release #4 (due by Week 11):
* Test and further improvement of classifiers
* Test compatibility of smaller components of project and flow

### Release #5 (due by Week 13):
* Finish ChRIS app pipeline 
