# 👀 Brain Tumor Classification & Segmentation Project 

An end-to-end deep learning pipeline for **Brain Tumor Detection and Segmentation**, combining **ResNet-50** for classification and **U-Net** for segmentation, specifically fine-tuned for medical imaging diagnostics, and deployed through a **Flask API** for real-time inference.

---

## 📊 Project Overview

* **Classification:** Categorizing MRI scans into *Glioma*, *Meningioma*, *Pituitary*, or *No Tumor* using a fine-tuned **ResNet-50**.
* **Segmentation:** Pixel-wise tumor boundary detection using a custom **U-Net** architecture.
* **Deployment:** End-to-end integration with a **Flask Web API** for easy clinical use.

---

## 📁 Dataset Details

### Classification Dataset

* **Source:** Brain MRI Images for Brain Tumor Detection (Kaggle)
* **Classes:** Glioma, Meningioma, Pituitary, No Tumor
* **Split:** 80% Training, 20% Testing

### Segmentation Dataset

* **Source:** LGG MRI Segmentation Dataset
* **Labels:** Binary Pixel Masks for Tumor Regions
* **Split:** 80% Training, 20% Testing

---

## 🛠️ Models Overview

### 👁️ ResNet-50 (Classification)

* Transfer Learning using **ResNet-50** pre-trained on ImageNet.
* Fine-tuned on the MRI classification dataset.
* Techniques Used: **EarlyStopping**, **ReduceLROnPlateau**, **ModelCheckpoint** for stable training.
* **Validation Accuracy:** \~98%, focusing on maintaining a balance between **Sensitivity** (True Positive Rate) and **Specificity** (True Negative Rate).

---

### 🤖 U-Net (Segmentation)

* Custom **U-Net** architecture designed for precise tumor boundary segmentation.
* Handled complex cases with faint tumor edges and imbalanced data.
* Used **Dice Loss** to focus on spatial overlap.
* **Dice Coefficient (DSC):** \~0.98 on Validation Set.

---

## 🛍️ Deployment with Flask API

* Built a lightweight **Flask API** that wraps the classification and segmentation models.
* Real-time image upload and inference.
* Designed for easy integration with hospital PACS systems.
* Scalable for future cloud deployment.

---

## 📊 Model Performance Summary

| Model     | Metric                 | Result |
| --------- | ---------------------- | ------ |
| ResNet-50 | Validation Accuracy    | \~98%  |
| U-Net     | Dice Coefficient (DSC) | \~0.98 |

---

##

## 💡 Key Highlights

* 🔄 Combined **ResNet-50** for Classification & **U-Net** for Segmentation.
* 🔢 Prioritized **DSC**, **Sensitivity**, **Specificity** over raw accuracy numbers.
* 🔹 Applied **EarlyStopping** and **Dynamic Learning Rate Scheduling**.
* 📶 Delivered a **Flask API** for seamless clinical integration.

---

---

## 🔗 Useful Links

* 🔗 **Kaggle Notebook (Classification):************************c************************[ation):](https://www.kaggle.com/code/nourzayed/brain-tumor-classification-resnet)**[ ](https://www.kaggle.com/code/nourzayed/brain-tumor-classification-resnet)[https://www.kaggle.com/code/nourzayed/brain-tumor-classification-re](https://www.kaggle.com/code/nourzayed/brain-tumor-classification-resnet)🔗 \*\*Kaggle Notebook (Segmentation):\*\*t[ation): ](https://www.kaggle.com/code/nourzayed/brain-tumor-segmentation-unet)[https://www.kaggle.com/code/nourzayed/brain-tumor-segmentation-unet](https://www.kaggle.com/code/nourzayed/brain-tumor-segmentation-unet)

---

## 📢 Hashtags

\#AIinHealthcare #BrainTumorDetection #MedicalImaging #DeepLearning #ResNet50 #UNet #FlaskAPI #AIProjects #HealthcareInnovation #MedicalAI #RadiologyAI #PythonAI #MedicalSegmentation #AIDeployment #AIHealthcareSolutions
