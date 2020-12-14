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
	
- [Final Presentation](https://youtu.be/Q44JWbjaJCE)

## 1. Vision and Goals Of The Project: 

Over the past few decades, there has been a tremendous amount of work done in the area of computational medical research. Researchers used image processing, machine learning and neural networks to determine certain patterns in diseases. However, we can question the practical impact of these improvements. The lack of easy access to data and computational power became the largest obstacle for the non-technical users. Our vision is to develop a ChRIS plugin that provides a text report of the MRI images using convolutional neural networks for clinical users at Boston Children's Hospital.

* Use Convolutional neural networks to segment brain MRI, and generate brain volume text report from segmented brain images.
* Create ChRIS plugins for this pipeline.
* Add the created apps to the ChRIS store and have them available in a ChRIS instance at Boston Children’s Hospital.


## 2. Users/Personas Of The Project:

The main target for this project is non-technical clinical end users mainly healthcare providers or researchers. However, developers are also considered for potential development and improvement.

* As a clinical user, I want to analysis volume from brain MRI images. But I don't have enough computating resources and technical background, so I need a pipeline of ChRIS plugins that do the analysis for me in a user-friendly way.


## 3.   Scope and Features Of The Project:

* Explore two types of neural network classifier of brain MRI:
	* A network classifier that attempts to segment multiple classes concurrently and provide classification of each part of the brain. 
	* A network classifier that leverages many classifiers, each tuned to only one class pertaining to a specific anatomical feature of the brain. 
* Convert DICOM to file types compatible with the classifiers.
* Convert brain MRI to seperate labels
* Convert segmented brain images to volume text report
* Ability to run the applications on ChRIS as plugins. 
* (possible) Build classifiers for x86_64 and for IBM Power9 architectures that exist at the MOC.

## 4. Solution Concept:

### Design Implications and Discussion:

Below is a description of the system components that are building blocks of the architectural design:

ChRIS: an open source distributed data and computation platform. The frontend and backend reside within a hospital or institutional network. Data from the network can be run on plugins. 

Massachusetts Open Cloud:

* Data from ChRIS is processed and initialized for specific plugins
* Computation setting for the image processing of the desired plugins. Computational output is transferred back to the ChRIS platform.

ChRIS and MOC architecture
---

**Figure 1: ChRIS, MOC, and our workflow**
<p align="center">
<img width="469" alt="Arch_final@2x" src="https://user-images.githubusercontent.com/56164075/101412428-98917080-38b0-11eb-8ec2-c6fe25ea5fd1.png">
</p>


Workflow Plugin Architecture
---

**Figure 2: Training Pipeline**
<p align="center">
<img width="618" alt="training_black@2x" src="https://user-images.githubusercontent.com/56164075/101413428-44878b80-38b2-11eb-8a2d-f7d071b2dcfa.png">
</p>
<br/>

**Figure 3: Inference Pipeline**
<p align="center">
<img width="743" alt="inference_Black@2x" src="https://user-images.githubusercontent.com/56164075/101413426-42253180-38b2-11eb-9e13-61ec62e3f085.png">
</p>

Design Implications and Discussion:

Key design decisions and motivation behind them.
* By deploying applications and computations within the cloud infrastructure, medical innovation can be driven by increasing amounts of data, computations and collaborations. 
* Computations run in containers on the Massachusetts Open Cloud that are lightweight and recreatable, this allows faster computation and results. 
* Containerizing allows workflows to be easily distributed.

## 5. Acceptance Criteria:

Minimum acceptance criteria includes a pipeline for the Chris app that can turn a host of MRI images into a text report regarding specific attributes of brain anatomy.

## 6. Deliverables:
### Plugins:
- [pl-mgz2labels](https://github.com/FNNDSC/pl-mgz2labels) (convert mgz files to images of seperated labels of the brain)
- [pl-mriunet_ser](https://github.com/BU-CLOUD-F20/Containerizing_Neural_Nets/tree/master/pl-mriunet_ser) (3D-Unet for training and inference)
- [pl-img2report](https://github.com/FNNDSC/pl-img2report) (convert segmented images to volume text report)
- [pl-heatmap](https://github.com/BU-CLOUD-F20/Containerizing_Neural_Nets/tree/master/pl-heatmap) (for comparison between ground truth and segmented images)

### Weights:
- [3D-Unet-500.h5](https://drive.google.com/file/d/1Yg4n5IiH_4m6VmC0oQbPh7ql5kaR01oG/view?usp=sharing) (the model for the whole brain)
- [label-11157.h5](https://drive.google.com/file/d/1u8P_fMxTkMfwN6A96zv8ydcOD-XCm09G/view?usp=sharing) (a sample model trained for label 11157 of a brain)

### MOC:
- [ChRIS on MOC](https://github.com/BU-CLOUD-F20/Containerizing_Neural_Nets/tree/MOC)

## 7. Release planning:
### Sprint 1:
Understanding infrastructure and plugins. Install necessary components to begin:
* Get familiar with ChRIS, web/command-line usage
* Set up develop environment (Linux, Docker)
* Research on neural networks that we need in this project
* Learn how to use the MOC

### Sprint 2:
* Tested existed ChRIS plugins for training and inference on brain MRI
* A design blueprint of our pipeline
* Begin working on MOC deplyment

### Sprint 3: 
* Finished the pipeline of the first type of classifier (one classifier for the whole brain)
* Using models on RGB brain inference (just an experiment)
* Deploy Pman and Pfioh using test scripts

### Sprint 4:
* Built a plugin that converts brain MRI to seperated labels (each for a specific region of this brain)
* Made the current 3D-Unet plugin able to train and infer brain images in serial
* Finished the training pipeline of the second type of classifier (one classifer for a specific region of brain)

### Sprint 5:
* Built a plugin that can generate volume text report from segmented brain images
* Finished the inference pipeline for two types of classifier
* Able to run plugins on ChRIS UI
* Able to test plugins on MOC containers

## 8. Usage:
There are ```in``` folders in our plugins, which are the example input files. Follow the ```readme``` in our plugins or check the ```command.txt``` in our plugins' folder, and run.

- Also you can try this [example mgz dataset](https://github.com/FNNDSC/mgz_converter_dataset)
