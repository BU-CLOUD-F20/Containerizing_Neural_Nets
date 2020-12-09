# Deploying ChRIS on MOC
ChRIS has two important components that is essential to running it's applications. First one is the IO Handler which is Pfioh. The second one is the Process Manager which is Pman. Here is a high level overview of the ChRIS archiecture:

![](https://www.bu.edu/rhcollab/files/2017/11/image3.png)

## The Steps
The steps for deploying ChRIS on MOC can be found here: [Chris On MOC](https://github.com/FNNDSC/ChRIS_on_MOC/wiki). 

This Wiki page includes the previous work that has done to deploy ChRIS on MOC. As we came across problems and new issues, we'have taken the lead to change and add more documentation to it. Here are the main steps to deploy ChRIS on MOC:
1. [Register To Mass Open Cloud](https://github.com/FNNDSC/ChRIS_on_MOC/wiki/1.-Registering-to-Mass-Open-Cloud)
2. [Add Projects to OpenShift and OpenStack](https://github.com/FNNDSC/ChRIS_on_MOC/wiki/2.-Adding-projects-to-Openstack-and-Openshift)
3. [Install the CLI tool (OC) on your system](https://github.com/FNNDSC/ChRIS_on_MOC/wiki/3.-Install-OC-libraries-on-your-system)
4. [Create Secrets for your project](https://github.com/FNNDSC/ChRIS_on_MOC/wiki/4.-Login-and-create-secrets-in-openshift-using-CLI-commands)
5. [Deploy Pfioh on MOC](https://github.com/FNNDSC/ChRIS_on_MOC/wiki/5.-Deploying-pfioh-on-MOC)
6. [Deploy Pman on MOC](https://github.com/FNNDSC/ChRIS_on_MOC/wiki/6.-Deploying-pman-on-MOC)
7. [Test Pfioh and Pman with Provided Scripts](https://github.com/FNNDSC/ChRIS_on_MOC/wiki/7.-Running-test-scripts-on-MOC)

This Repo includes the test scripts we've written to test the plugins we've developed: [Cagriyoruk/ChRIS-E2E](https://github.com/Cagriyoruk/ChRIS-E2E)


## Demonstrating The Plugins We Built on MOC
### PL-mgz2labels
```
__  __  _____ _________  _               ____  ______ _       _____ 
|  \/  |/ ____|___  /__ \| |        /\   |  _ \|  ____| |     / ____|
| \  / | |  __   / /   ) | |       /  \  | |_) | |__  | |    | (___  
| |\/| | | |_ | / /   / /| |      / /\ \ |  _ <|  __| | |     \___ \ 
| |  | | |__| |/ /__ / /_| |____ / ____ \| |_) | |____| |____ ____) |
|_|  |_|\_____/_____|____|______/_/    \_\____/|______|______|_____/ 
------------------------------
Creating training images...
------------------------------
Loading of train data done.
Training NPY saved at: /share/outgoing/imgs_train.npy
------------------------------
Creating labeled images...
------------------------------
Loading all labels done.
Processing the whole mask...
Saving to .npy files: done.
Finished.
```
### PL-mriunet_ser
```
███╗   ███╗██████╗ ██╗██╗   ██╗███╗   ██╗███████╗████████╗     ███████╗███████╗██████╗ 
████╗ ████║██╔══██╗██║██║   ██║████╗  ██║██╔════╝╚══██╔══╝     ██╔════╝██╔════╝██╔══██╗
██╔████╔██║██████╔╝██║██║   ██║██╔██╗ ██║█████╗     ██║        ███████╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██╗██║██║   ██║██║╚██╗██║██╔══╝     ██║        ╚════██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║╚██████╔╝██║ ╚████║███████╗   ██║███████╗███████║███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═
------------------------------
Loading and preprocessing test data...
------------------------------
['734045']
TOTAL:  18
------------------------------
Creating test images...
------------------------------
Loading done.
 ---------------- preprocessed -----------------
Saving to .npy files done.
Size:  (18, 16, 256, 256, 1)
------------------------------
Test npy size:(18, 16, 256, 256, 1)
------------------------------
------------------------------
Loading saved weights...
```
### PL-img2report
```
_                  _____                           _   
(_)                / __  \                         | |  
 _ _ __ ___   __ _ `' / /'_ __ ___ _ __   ___  _ __| |_ 
| | '_ ` _ \ / _` |  / / | '__/ _ \ '_ \ / _ \| '__| __|
| | | | | | | (_| |./ /__| | |  __/ |_) | (_) | |  | |_ 
|_|_| |_| |_|\__, |\_____/_|  \___| .__/ \___/|_|   \__|
              __/ |               | |                   
             |___/                |_|                   
Version: 0.1
Convert images to numpy arrays...
1/2562/2563/2564/2565/2566/2567/2568/2569/25610/25611/25612/25613/25614/25615/25616/25617/25618/25619/25620/25621/25622/25623/25624/25625/25626/25627/25628/25629/25630/25631/25632/25633/25634/25635/25636/25637/25638/25639/25640/25641/25642/25643/25644/25645/25646/25647/25648/25649/25650/25651/25652/25653/25654/25655/25656/25657/25658/25659/25660/25661/25662/25663/25664/25665/25666/25667/25668/25669/25670/25671/25672/25673/25674/25675/25676/25677/25678/25679/25680/25681/25682/25683/25684/25685/25686/25687/25688/25689/25690/25691/25692/25693/25694/25695/25696/25697/25698/25699/256100/256101/256102/256103/256104/256105/256106/256107/256108/256109/256110/256111/256112/256113/256114/256115/256116/256117/256118/256119/256120/256121/256122/256123/256124/256125/256126/256127/256128/256129/256130/256131/256132/256133/256134/256135/256136/256137/256138/256139/256140/256141/256142/256143/256144/256145/256146/256147/256148/256149/256150/256151/256152/256153/256154/256155/256156/256157/256158/256159/256160/256161/256162/256163/256164/256165/256166/256167/256168/256169/256170/256171/256172/256173/256174/256175/256176/256177/256178/256179/256180/256181/256182/256183/256184/256185/256186/256187/256188/256189/256190/256191/256192/256193/256194/256195/256196/256197/256198/256199/256200/256201/256202/256203/256204/256205/256206/256207/256208/256209/256210/256211/256212/256213/256214/256215/256216/256217/256218/256219/256220/256221/256222/256223/256224/256225/256226/256227/256228/256229/256230/256231/256232/256233/256234/256235/256236/256237/256238/256239/256240/256241/256242/256243/256244/256245/256246/256247/256248/256249/256250/256251/256252/256Conversion finished.
(256, 256, 252)
Loading look up file from FreeSurferColorLUT.txt
Writing report as /share/outgoing/report_imgs_mask_train.html
< THE ACTUAL HTML FILE>
// I HAD TO DELETE THIS PART BECAUSE IT WAS TOO LONG FOR A MESSAGE //
Reports saved
```
