

# Endsem Project : An Efficient Approach in Brain Tumor Detection using Deep Learning Techniques 

### Lycia Thomas : UR16CS151
### Aishwarya Naina : UR16CS178

## Introduction :
 This Project is based upon detecting brain tumors in the human brians on the MRI scanned T2 images, these scans are trainined on a VGG16 Convolutional Neural Network model using transfer learning techniques, further Mask R-CNN is used to segment the tumorous regions in the MRI scan. 

## Instructions :
1. Make new Conda environment using Ananconda Package manager ( assuming you have Anaconda installed )
```bash
conda create --name project-conda-env python=3.6
```

 2. Activate the conda Environment 
```bash
conda activate project-conda-env
```

3. Install the Required Dependencies :
```bash
pip install tensorflow-gpu==1.14
```
```bash
pip install keras==2.3
```

```bash
pip install plotly==latest
```

```bash
pip install tqdm
```


 4. Navigate to the `src/` directory where the source python files are located : 
```bash
cd src/
```

5. Here the `CNN-VGG16.ipnb` Notebook file is used to train the model to launch jupyter notebook in this directory:
```bash 
jupyter notebook 
```

and train the model by running each cell in the Jupyter Notebook. 


7. Note: Other files like `TRAIN/` , `TEST/`, `VAL/`,`Mask_RCNN/` are utility files that can be used additionally to get the  model weights and Mask RCNN configurations. 

