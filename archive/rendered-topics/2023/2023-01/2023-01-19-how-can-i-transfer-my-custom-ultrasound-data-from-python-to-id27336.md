---
topic_id: 27336
title: "How Can I Transfer My Custom Ultrasound Data From Python To"
date: 2023-01-19
url: https://discourse.slicer.org/t/27336
---

# How can I transfer my custom ultrasound data from python to 3Dslicer through IGT

**Topic ID**: 27336
**Date**: 2023-01-19
**URL**: https://discourse.slicer.org/t/how-can-i-transfer-my-custom-ultrasound-data-from-python-to-3dslicer-through-igt/27336

---

## Post #1 by @LV52 (2023-01-19 01:53 UTC)

<p>Hi, everyone.</p>
<p>I am conducting an academic research and want to use 3DSlicer to reconstruct the ultrasound image from 2D to 3D.</p>
<p>I only have offline ultrasound images (both DICOM and .png) and 6-DOF coordinate for each ultrasound image, and I do not have the ultrasound devices and positioning equipment such as OptiTrack which is recommended in the IGT tutorial. But I found an <a href="https://github.com/lassoan/pyigtl" rel="noopener nofollow ugc">IGT Python implementation</a> from Lassoan. This Python code has two functions <strong>pyigtl.PositionMessage</strong> and <strong>pyigtl.ImageMessage</strong>, which is match with my offline ultrasound data.</p>
<p>Now, the question is how to connect the Python to 3DSlicer through IGT to realize the 3D reconstruction of ultrasonic images? I’ve seen some slicerIGT tutorials in <a href="http://slicerigt.org" rel="noopener nofollow ugc">slicerigt.org</a> and it seems like to fetch data from outside you have to use plus server and prepare a configuration file (.xml) for that.</p>
<p>I am now confused with how to write this configuration file right , any good idea?</p>
<p>In addition to preparing the correct .XML file, what other operations do I need to do to finally connect and transmit data correctly from Python to Slicer?</p>
<p>Furthermore, if I transmit the ultrasonic data correctly to the Slicer, whether the remaining steps of 3D ultrasonic reconstruction are the same as this <a href="https://www.youtube.com/watch?v=2vXeJxYFou4" rel="noopener nofollow ugc">video</a>, whitch can be implemented by calling Plus Remote, and the Volume Reconstruction module?</p>
<p>Very appreciate！</p>

---

## Post #2 by @lassoan (2023-03-01 04:47 UTC)

<p>I would recommend to create an ultrasound sequence file (igs.mha or igs.nrrd), which contains the coordinate system for each ultrasound image and the all the images. You can load these files into Slicer and use the Volume reconstructor module to paste the frames into a 3D volume.</p>
<p>The specification of the file format is available <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceFile.html">here</a>. You can find many examples <a href="https://github.com/PlusToolkit/PlusLibData/tree/master/TestImages">here</a>.</p>

---

## Post #3 by @LV52 (2023-03-01 08:54 UTC)

<p>OK，thanks! I wiil try it.<br>
I have read some documentation of SlicerIGT and OpenIGTLink before, but not getting anywhere.</p>
<p>The IGT Python implementation , I used <strong>pyigtl.ImageMessage</strong>   successfully, but <strong>pyigtl.PositionMessage</strong> failed.</p>
<p>In <strong>pyigtl.ImageMessage</strong> , I can see the moving circle image in the 3Dslicer, which has a device_name of “Image”.  But in <strong>pyigtl.PositionMessage</strong> , I see nothing in the 3Dslicer, also the  device_name of “Position” is not show.</p>
<p>The documentation of plus toolkit which I have not read yet.</p>

---

## Post #4 by @lassoan (2023-03-01 12:08 UTC)

<p>If you want to reconstruct already recorded data then it is simpler to create a .igs.nrrd file. Streaming to Slicer via openigtlink is needed if you want to reconstruct live data.</p>

---

## Post #5 by @LV52 (2023-03-02 08:13 UTC)

<p>The tutorials you gave me yesterday seems like create the .mha file through plus toolkit. The tutorials are mostly based on c++, which I am not familiar with.<br>
If I take my ultrasound images and 3D location data to create a .nrrd file, is there a way to do it in python?</p>

---
