---
topic_id: 24786
title: "Slicer Deepseg Issue"
date: 2022-08-16
url: https://discourse.slicer.org/t/24786
---

# Slicer-DeepSeg issue

**Topic ID**: 24786
**Date**: 2022-08-16
**URL**: https://discourse.slicer.org/t/slicer-deepseg-issue/24786

---

## Post #1 by @platanus (2022-08-16 13:47 UTC)

<p>Hello, All members in 3D-Slicer</p>
<p>Maybe… Have you ever used the Slicer-DeepSeg extension?</p>
<p>I’m reproducting extraction of brain tumor using Slicer-DeepSeg extension based on 3D-Slicer.</p>
<p>I’m running DeepSeg extension using MICCAI_BraTS2020_TrainingData in 3D-Slicer refering to Slicer-DeepSeg github.</p>
<p>I ran the Slicer-DeepSeg extension in 3D-Slicer as following.</p>
<ol>
<li>
<p>Creation of Slicer-DeepSeg Extension/DeepSeg module<br>
1)I run ‘Extension Wizard’ module-&gt;2)Select ‘Select Extension’ button-&gt;3)Select ‘Slicer-DeepSeg’ folder-&gt; 4)Select whether ‘DeepSeg module’ loads or not</p>
</li>
<li>
<p>I downloaded dataset<br>
-MICCAI_BraTS2020_TrainingData</p>
</li>
<li>
<p>I run DeepSeg module using MICCAI_BraTS2020_TrainingData in 3D-Slicer<br>
(1) After pressing ‘Add Data’ button in ‘Welcome to Slicer’ module, I imported ‘BraTS20_Training_001’ folder in MICCAI_BraTS2020_TrainingData.<br>
(2) And then I selected ‘DeepSeg’ module in ‘modules finder’ option.<br>
(3) In Inputs item, I selected ‘BraTs20_Training_001_flair_1’ in ‘FLAIR Volume’ option.<br>
(4) In Outputs item, I selected one volume (MRI) dicom file in ‘Tumor Volume’<br>
(5) I set the different options in ‘Advanced Segmentation Parameters’ item as following.:</p>
<ul>
<li>Image Modalities : FLAIR</li>
<li>Corrped Image Shape :(192, 224, 160)</li>
<li>Tumor Type : Whole Tumor</li>
<li>3D Background Colour : Black</li>
</ul>
</li>
</ol>
<p>After completing setting using DeepSeg module in 3D-Slicer, I pressed ‘Apply’ button.</p>
<p>But It occurs the error that is “Failed to compute results: Incomplete or corrupted file detected. The sha256 file hash does not match the provided value of 941eb4b2c7da98310a95176e7adabe8f84d2e3df.<br>
Traceback (most recent call last):<br>
File “C:/Users/TRL 3D/Extension_dev/Slicer-DeepSeg/DeepSeg/DeepSeg.py”, line 603, in onApplyButton modelPath = get_file(pretrainedURL.split(”/“)[-1], pretrainedURL, File “C:\Users\TRL 3D\AppData\Local\NA-MIC\Slicer 5.1.0-2022-07-01\lib\Python\Lib\site-packages\keras\utils\data_utils.py”, line 298, in get_file<br>
raise ValueError(ValueError: Incomplete or corrupted file detected. The sha256 file hash does not match the provided value of 941eb4b2c7da98310a95176e7adabe8f84d2e3df.”.</p>
<p>Please, refer to attached image associated with error massage.<br>
<a href="https://user-images.githubusercontent.com/41041429/184850207-d1413721-fae4-47c9-ac00-888cb6541edb.png" rel="noopener nofollow ugc"><img src="https://user-images.githubusercontent.com/41041429/184850207-d1413721-fae4-47c9-ac00-888cb6541edb.png" alt="sha256_error" width="690" height="411"></a></p>
<p>Please, let me know in detail how to solve this problem.</p>
<p>Thank you for reading my writing.</p>

---

## Post #2 by @pieper (2022-08-17 21:04 UTC)

<p>I guess you refer to code from <a href="https://github.com/razeineldin/DeepSeg">this repository</a>.  Best to file an issue there.</p>

---
