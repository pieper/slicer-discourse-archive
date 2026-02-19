---
topic_id: 40539
title: "Seeking Guidance Imu Based Tracking For Real Time 3D Ultraso"
date: 2024-12-06
url: https://discourse.slicer.org/t/40539
---

# Seeking Guidance: IMU-based Tracking for Real-time 3D Ultrasound Reconstruction using Plus Toolkit and Slicer

**Topic ID**: 40539
**Date**: 2024-12-06
**URL**: https://discourse.slicer.org/t/seeking-guidance-imu-based-tracking-for-real-time-3d-ultrasound-reconstruction-using-plus-toolkit-and-slicer/40539

---

## Post #1 by @MasatoshiOBA (2024-12-06 03:04 UTC)

<p>Dear Slicer and Plus Toolkit Community,</p>
<p>I am currently working on a project for real-time 3D ultrasound reconstruction. My work is largely guided by the excellent tutorials provided by the developers of 3D Slicer and the Plus Toolkit.</p>
<p><strong>Project Background:</strong></p>
<p>The unique feature of my project is the use of an IMU (Inertial Measurement Unit) to track the ultrasound probe. I understand that IMU-only tracking comes with significant challenges, such as noise and drift, compared to optical tracking systems. However, I have chosen to adopt IMU tracking due to the following reasons:</p>
<ol>
<li><strong>Cost and Size Advantages:</strong> Using an IMU reduces both the cost and the physical footprint of the tracking system.</li>
<li><strong>Upcoming High-Performance IMU:</strong> There is a new IMU, compatible with Sony’s Spresense microcontroller board, that is expected to offer high precision and low noise (<a href="https://www-kenkai-jaxa-jp.translate.goog/research/innovation/multi_imu.html?_x_tr_sl=auto&amp;_x_tr_tl=en&amp;_x_tr_hl=ja&amp;_x_tr_pto=wapp" rel="noopener nofollow ugc">details here</a>). My goal is to explore whether this new IMU can enable standalone tracking for ultrasound applications.</li>
</ol>
<p><strong>Current Challenges:</strong></p>
<p>The primary issue I am facing is that the current Plus Server does not natively support the Spresense board, and there is no existing configuration file for it. I have started developing custom code to address this. Currently:</p>
<ul>
<li>The Plus Server successfully recognizes the serial port (COM) from Spresense.</li>
<li>3D Slicer listens on port 18944.</li>
<li>However, the expected Transform nodes are not automatically created in Slicer.</li>
</ul>
<p><strong>Seeking Advice:</strong></p>
<p>At this stage, I am considering two potential approaches to move forward:</p>
<ol>
<li><strong>Custom Serial Communication via Plus Server:</strong> Develop a sketch for Spresense to output IMU data in a format suitable for Plus Server to process and relay as Transform nodes to Slicer.</li>
<li><strong>Utilize ROS2 with Slicer-ROS2 Integration:</strong> Since Spresense supports microROS, I could implement ROS2-based communication to handle Transform data exchange directly with Slicer.</li>
</ol>
<p><strong>Environment:</strong></p>
<p>I am using a Windows 10 64-bit machine for development. While I primarily work directly on Windows, I also have access to WSL2 and Docker if they could be advantageous for this project.</p>
<p>I would greatly appreciate your insights or recommendations on which approach might be more suitable, or if there are other paths I should consider.</p>
<p>Thank you in advance for your time and guidance.</p>
<p>Best regards,<br>
Masatoshi Oba</p>

---

## Post #2 by @lassoan (2024-12-07 05:47 UTC)

<p>Ultrasound image reconstruction using IMU has been studied extensively. There ultrasound probes (such as ClariUS, ExactVU) have built-in IMU for this reason.</p>
<p>Accuracy of the IMU is typically not a cause for concern, commonly available sensors are already accurate enough for determining orientation. ROS is extremely difficult to set up on Windows and would be a huge overkill if you just want to read from a serial line. Plus has several examples of hoe to read sensor data frome serial port (including IMUs).</p>
<p>The main challenge is that the rotation axis is unknown and unstable. Many solutions have been proposed for this: careful spinning (for endocavity probes, e.g., for prostate, follicle counting), pivoting (for linear probes), and mechanical constraining (stepper for transperineal prostate biopsies, and various jigs and gimbals).</p>
<p>Note that the main competition of IMU based tracking is not the expensive ($2k-$15k) optical or electromagnetic tracking; but inexpensive camera based tracking. You may get 6DOF pose with acceptable accuracy from even a single camera, but you can improve rhe results by using more cameras and/or tracking 2D barcodes.</p>

---
