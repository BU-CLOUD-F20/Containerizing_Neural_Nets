# Deploying ChRIS on MOC
ChRIS has two important components that is essential to running it's applications. First one is the IO Handler which is Pfioh. The second one is the Process Manager which is Pman. Here is a high level overview of the ChRIS archiecture:

![](https://www.bu.edu/rhcollab/files/2017/11/image3.png)

## The Steps
The steps for deploying ChRIS on MOC can be found here: https://github.com/FNNDSC/ChRIS_on_MOC/wiki. 

This Wiki page includes the previous work that has done to deploy ChRIS on MOC. As we came across problems and new issues, we'have taken the lead to change and add more documentation to it. Here are the main steps to deploy ChRIS on MOC:
1. Register To Mass Open Cloud
2. Add Projects to OpenShift and OpenStack
3. Install the CLI tool (OC) on your system
4. Create Secrets for your project
5. Deploy Pfioh on MOC
6. Deploy Pman on MOC
7. Test Pfioh and Pman with Provided Scripts. 

This Repo includes the test scripts we've written to test the plugins we've developed: [Cagriyoruk/ChRIS-E2E](https://github.com/Cagriyoruk/ChRIS-E2E)


## Demonstrating The Plugins We Built on MOC
