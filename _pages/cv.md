---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}
Education
======
* Ph.D. in Electrical and Computer Engineering, University of Illinois Chicago (Expected Dec. 2025)
* M.S. in Electrical Engineering (Power System), Shanghai University of Electric Power, 2018
* B.S. in Electrical Engineering (Automation), Shanghai University of Electric Power, 2015

Work Experience
======
* Quanta Technology LLC – Intern, Distribution Team (May 2023 – Aug. 2023)
  * Conducted power distribution analysis and renewable integration studies
  * Supported DER/IBR protection and IEEE 2800 compliance projects
  * Supervisor: Andrija Sadikovic  

* Graduate Research Assistant, University of Illinois Chicago (Sep. 2019 – Present)
  * Research in AI-driven environmental hazard prediction and renewable integration
  * Developed deep learning frameworks for wildfire spread prediction, vegetation monitoring, and adversarial robustness
  * Supervisor: Prof. Ahmet Enis Cetin, Prof. Lina He

* Teaching Assistant, University of Illinois Chicago (2019 – Present)
  * Assisted in courses on power systems, signal processing, and image processing
  * Mentored students in lab projects and assignments

Research & Project Experience
======
* **Wildfire Spread Prediction (2019 – Now)**  
  Developed Hadamard Transform UNet (HT-UNet) for next-day wildfire prediction using multi-modal satellite data, improving F1-score and reducing parameters compared to CNN baselines.

* **Vegetation and Power Line Monitoring (2016 – Now)**  
  Designed UAV/camera-based vegetation monitoring using PowerLine-YOLO (OBB detection), stereovision 3D reconstruction, and NDVI proxies from satellite imagery to reduce outage risks.

* **Infrared Air Leak Detection (2024 – Now)**  
  Proposed Sobel-enhanced YOLO achieving 52% AP50 improvement over baseline detectors, enabling lightweight, mobile-friendly diagnostics for energy efficiency.

* **AI Robustness & Safety (2024 – Now)**  
  Developed multi-resolution training and Gaussian-prefiltered CNNs (ResNet, MobileNet, VGG) improving adversarial robustness for autonomous vehicle traffic sign recognition.

* **Renewable Energy Integration (2021 – 2022)**  
  Built DER/IBR overcurrent protection algorithms, grid-forming inverter models in Simulink/OPAL-RT, and contributed to offshore wind integration projects with Ørsted/Eversource.

Skills
======
* Deep Learning & Computer Vision: YOLO, ResNet, MobileNet, UNet, EfficientNet, Diffusion Models  
* Geospatial/Remote Sensing: Sentinel-2, Landsat, VIIRS, NDVI/NBR indices, ArcGIS, GDAL  
* Programming & Tools: Python, PyTorch, TensorFlow, MATLAB, OpenCV, LaTeX, Git, Visual Studio  
* Power Systems & Simulation: Simulink, OPAL-RT, AutoCAD, LTspice  

Publications
======
<ul>{% for post in site.publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

Talks
======
<ul>{% for post in site.talks reversed %}
  {% include archive-single-talk-cv.html %}
{% endfor %}</ul>

Teaching
======
<ul>{% for post in site.teaching reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

Service and Leadership
======
* Reviewer: IEEE Transactions on Power Delivery, Signal, Image and Video Processing  
* Member: IEEE Student Member, IEEE Women in Engineering  
* Mentor: Undergraduate research projects in ECE  

Awards & Additional Information
======
* Runner-up, 2024 NASA Wildfire Climate Tech Challenge  
* UIC ECE Department Award (2019)  
* SUEP First-Class Scholarships & President’s Scholarship (2015–2018)  
* Languages: English (proficient), Mandarin (native)  