# How to generate 4D cine MRI?

**Topic ID**: 24743
**Date**: 2022-08-13
**URL**: https://discourse.slicer.org/t/how-to-generate-4d-cine-mri/24743

---

## Post #1 by @KLNU (2022-08-13 20:58 UTC)

<p>Dear Dr, Lasso,</p>
<p>Currently, I have cine MRI images (25 phases a cardiac cycle, at 2-, 3-, 4 chamber and short-axis view (9 slices from the apex to the base) [total 300 pictures]. I tried to “Reconstruct 4D volume from cine-MRI frames” in 3D slicer (V.5.03). However, I have some questions regarding the workflow. I also watched the video on youtube, however it did not answer all my questions. Please see below.</p>
<ul>
<li>Import the cine-MRI acquisition using the DICOM module: switch to DICOM module and drag-and-drop the folder that contains the DICOM files to the application window<br>
Done.</li>
<li>Load the cine-MRI data set by double-clicking on the cine-MRI series in the DICOM browser<br>
Done. There are 12 series loaded. One of them is “SAX cine_trufi_retro_invf - as a 25 frames MultiVolume by TriggerTime”.</li>
<li>Create an Annotation ROI node: click the down-arrow in the “Create and place” button on the toolbar, choose the “ROI” option at the top, then click in the middle of the region of interest in a slice view, then at a corner of a region of interest in the same slice view.<br>
This sentence is not clear. I installed Nvidiaannotation and find the “annotations” module and found the ROI. My question is which “slice views” should I work on it? 4-chamber? 2-chamber?or short-axis? and which slice? It seems that I could not pill out all slices on three windows (R, G ,Y). Only two clicks is enough? I selected 2-, 4- and a short-axis view at 3 windows and set an ROI covering the whole heart in three different views, is that right?</li>
<li>Switch to “Reconstruct 4D cine-MRI” module<br>
Done.</li>
<li>Select the loaded cine-MRI sequence as “Input sequence”<br>
When I switched to “Reconstruct 4D cine-MRI”, I was unable to find current cine MRI sequence under “input sequence”. Therefore, no “apply” showed.</li>
<li>Select the created ROI node as “Input region”<br>
It showed “R”, right?</li>
</ul>
<p>Thanks,</p>
<p>Kai</p>

---

## Post #2 by @lassoan (2022-08-13 21:41 UTC)

<aside class="quote no-group" data-username="KLNU" data-post="1" data-topic="24743">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/klnu/48/13600_2.png" class="avatar"> KLNU:</div>
<blockquote>
<p>There are 12 series loaded. One of them is “SAX cine_trufi_retro_invf - as a 25 frames MultiVolume by TriggerTime”</p>
</blockquote>
</aside>
<p>This is the issue - the sequence is loaded as a <code>MultiVolume</code>. In the menu: Edit → Application settings → DICOM → Preferred multi-volume import format → select <code>volume sequence</code>. After you restart the application, the images will be loaded as volume sequence and they will appear in the node selector.</p>

---

## Post #3 by @KLNU (2022-08-13 22:35 UTC)

<aside class="quote no-group" data-username="KLNU" data-post="1" data-topic="24743">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/klnu/48/13600_2.png" class="avatar"> KLNU:</div>
<blockquote>
<p>SAX cine_trufi_retro_invf - as a 25 frames MultiVolume by TriggerTime</p>
</blockquote>
</aside>
<p>Thanks!<br>
Now it showed “SAX cine_trufi_retro_invf - as a 25 frames MultiVolume by TriggerTime”<br>
“SAX cine_trufi_retro_invf - as a 25 frames MultiVolume by TriggerTime_1”<br>
“SAX cine_trufi_retro_invf - as a 25 frames MultiVolume by TriggerTime_2”</p>
<p>Is that normal? Do I need to just upload short-axis cine (to construct the volume) or do I need to also upload 2-, 3-, 4- chamber view? My ultimate goal is to extract radiomics features on each phase of the left ventricle.</p>
<p>Thanks!</p>
<p>Kai</p>

---

## Post #4 by @KLNU (2022-08-13 22:57 UTC)

<aside class="quote no-group" data-username="KLNU" data-post="3" data-topic="24743">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/klnu/48/13600_2.png" class="avatar"> KLNU:</div>
<blockquote>
<p>Thanks!<br>
Now it showed “SAX cine_trufi_retro_invf - as a 25 frames MultiVolume by TriggerTime”<br>
“SAX cine_trufi_retro_invf - as a 25 frames MultiVolume by TriggerTime_1”<br>
“SAX cine_trufi_retro_invf - as a 25 frames MultiVolume by TriggerTime_2”</p>
<p>Is that normal? Do I need to just upload short-axis cine (to construct the volume) or do I need to also upload 2-, 3-, 4- chamber view? My ultimate goal is to extract radiomics features on each phase of the left ventricle.</p>
<p>Thanks!</p>
<p>Kai</p>
</blockquote>
</aside>
<p>Sorry. The sequences should be:<br>
“SAX cine_trufi_retro_invf - as a 25 frames Volume Sequence by TriggerTime [0]”<br>
“SAX cine_trufi_retro_invf - as a 25 frames Volume Sequence by TriggerTime_1 [0]”<br>
…<br>
My questions are:</p>
<ol>
<li>Should I include 2-, 3-, 4- chambers images as well?</li>
<li>Where should I “Create an Annotation ROI node”? On which images?</li>
</ol>
<p>Best,</p>
<p>Kai</p>

---

## Post #5 by @KLNU (2022-08-17 02:15 UTC)

<p>Dear Dr. Lasso,</p>
<p>Finally I solved the problem in constructing 4D cine MRI. It is the problem of dicom format. The data I shared with you did not work.</p>
<p>I have another question. How can I load a sequence (such as 4-chamber view cine as separated images)? I want to get radiomics features on those 25 images one by one.</p>
<p>Thank you!</p>

---
