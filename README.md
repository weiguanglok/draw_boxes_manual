# Draw Boxes Manual 📦

A lightweight, interactive Python utility for manually drawing and saving bounding boxes on a sequence of images. 

I developed this tool as an exploratory project during my internship. While the team ultimately utilised an existing internal workflow for data annotation, building this tool served as a valuable Proof of Concept (PoC). It allowed me to understand the mechanics of image annotation, Region of Interest (ROI) extraction, and dataset preparation for Computer Vision tasks.

## ✨ Features
* **Interactive GUI:** Uses OpenCV to provide a simple, click-and-drag interface for drawing bounding boxes.
* **Smart Sorting:** Automatically detects frame numbers in file names and sorts them chronologically (e.g., `frame1.jpg`, `frame2.jpg`).
* **Non-Destructive:** Keeps your original images intact and saves the newly boxed images in an automatically generated `boxed/` subdirectory.
* **Fast Workflow:** Built-in keyboard shortcuts to quickly confirm boxes or skip irrelevant frames.

## 🛠️ Prerequisites

You will need Python 3.x installed along with the OpenCV library.

```bash
pip install opencv-python
```

## 🚀 How to Use

    Clone this repository:
    code Bash

    git clone https://github.com/weiguanglok/draw_boxes_manual.git
    cd draw_boxes_manual
