---
topic_id: 36882
title: "Generating configuration files in the Autscoper preprocessing module"
date: 2024-06-18
url: https://discourse.slicer.org/t/36882
last_bumped: 2026-04-20T17:09:07.372Z
---

# Generating configuration files in the Autscoper preprocessing module

**Topic ID**: 36882
**Date**: 2024-06-18
**URL**: https://discourse.slicer.org/t/generating-configuration-files-in-the-autscoper-preprocessing-module/36882

---

## Post #1 by @Amy_Morton (2024-06-18 16:06 UTC)

<p><a class="mention" href="/u/jeffrey_k_spear">@Jeffrey_K_Spear</a></p>
<p>Could you add some details about your data, which you’re trying to prep for use in Autoscoper?</p>

---

## Post #2 by @Jeffrey_K_Spear (2024-06-18 21:56 UTC)

<p>Details of my files:</p>
<p><strong>Radiographs:</strong><br>
Files were originally .avi video files that I converted to .jpg files in FIJI in order to read them into XMA Lab without lag. Originally I had exported them as .jpg files and then converted them to .tiff, but after we spoke I tried exporting the undistorted files directly as .tiffs. I then created a test dataset of only two radiograph images that I edited to be 1260x1260 squares (in Gimp). After editing the Mayacam files to be 1260x1260, I loaded our jury-rigged .cfg file but the images still don’t show up. So I suspect you’re right that important ‘hidden’ data got lost along the way somewhere. I will keep experimenting and let you know if I find anything. The next thing I plan to try is to read the .avi files directly into XMALab and then export undistorted .tiffs from there.</p>
<p><strong>CT data:</strong><br>
CT data was originally a .tiff stack that I read into Slicer.</p>
<p><strong>Segmentations/Volumes:</strong><br>
I segmented the bones directly in Slicer. I created the partial volumes using the Autoscoper pre-processing module. As we saw today, the volume files seem to load just fine when using the jury-rigged .cfg file.</p>
<p><strong>Calibration files:</strong><br>
My calibration files are Mayacam 2.0 files as .txt files exported from XMALab.</p>

---

## Post #3 by @HHH (2026-04-18 13:42 UTC)

<p>Hello!</p>
<p>I am a new user of SlicerAutoscoperM, currently learning to use this powerful tool for biomechanics research. First of all, thank you very much for developing and maintaining such an excellent open-source project, which has provided great convenience for our research work.</p>
<p>I have encountered a problem and hope to get your guidance: I have built a high-precision 3D bone model in Amira software and successfully exported it as an STL format file. Now I need to convert this STL bone model into TIFF format volume data for subsequent registration and analysis in SlicerAutoscoperM.</p>
<p>I have tried the following steps but failed:</p>
<ol>
<li>
<p>Imported the STL model into 3D Slicer</p>
</li>
<li>
<p>Tried to use the “Volumes” module for conversion, but did not find an option to directly convert a surface model to volume data</p>
</li>
<li>
<p>Searched the official documentation and forums of SlicerAutoscoperM, but did not find a specific tutorial for converting Amira STL to TIFF</p>
</li>
</ol>
<p>Could you please answer the following questions:</p>
<ol>
<li>
<p>Is there a dedicated module or tool in SlicerAutoscoperM or 3D Slicer that can convert STL surface models to TIFF format volume data?</p>
</li>
<li>
<p>If yes, could you briefly explain the specific operation steps?</p>
</li>
<li>
<p>During the conversion process, what parameter settings (such as voxel size, resolution, etc.) need special attention to ensure that the quality of the converted volume data is suitable for subsequent registration analysis?</p>
</li>
</ol>

---

## Post #4 by @John_Holtgrewe (2026-04-20 17:09 UTC)

<p>There is not a dedicated tool to convert STL surface models to TIFF format. The pre-processing module only accepts volume nodes that contain CT data. If you have the CT scans, you can load those in and then load in your STL models as segmentations.</p>

---
