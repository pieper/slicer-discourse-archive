# Export images of MultiVolumeExplorer

**Topic ID**: 4805
**Date**: 2018-11-19
**URL**: https://discourse.slicer.org/t/export-images-of-multivolumeexplorer/4805

---

## Post #1 by @riep (2018-11-19 14:36 UTC)

<p>Dear, everyone,</p>
<p>I have looked at several post on this topic but I have not find something that is working for me.<br>
What I am trying to do is to reformat a stack of 10 cine slices into a slightly tilted. To be more schematic, let’s say I acquire 10 cine slices in coronal orientation and want to interpolate and reconsturct the same cine stack in transverse orientation.<br>
To do that I am using multiplevolumeimporter. It works great with our data. Then I use reformat to select a reconstruction plan that I interested in. Finaly, I can switch to mutliplevolumeexplorer to play the cine in my selected plan.</p>
<p>Now I am trying to export the selected cine plan (images) into dicom.<br>
Does anyone know how it can be done in slicer ?</p>
<p>Thanks a lot for your help,<br>
PIerre</p>

---

## Post #2 by @fedorov (2018-11-19 16:25 UTC)

<p>Sorry, export of multivolumes into DICOM is not something that multivolume-related modules can do.</p>
<p>To the best of my knowledge, there are no tools in Slicer to help with your task, if I understood it correctly.</p>
<p>Can you give us a bit more details as to what you would like to achieve? Why do you need that DICOM export - is it really critical?</p>

---

## Post #3 by @lassoan (2018-11-19 16:38 UTC)

<p>You can resample a rotated volume using Sequences extension’s “Crop volume sequence” module. To load a 4D image as Volume Sequence instead of MultiVolume, check “Advanced” checkbox in DICOM module, click “Examine” and select “… as Volume Sequence …” loadable.</p>
<p>I have a semi-functional DICOM exporter for volume sequences. If needed, I can tidy it up and make it available in Sequences extension within a few days.</p>

---

## Post #4 by @riep (2018-11-19 17:01 UTC)

<p>Thank you both for your help.<br>
@ [Andrey] To be more specific. I am working on cardiac cine images. I am interested in the strain of pulmonary vein along the cardiac cycle. Most of the time, the stack of cine images needs some adjustements (slight tilt in order to have all the time the structure of interest in-plane).<br>
Then, I would like to export this plane to a software in matlab that needs dicom as inputs.</p>
<p>@ [Andras L] I have tried to load our data as a volume but it is not working properly as the inital data are 2D<br>
I will try to work on it.</p>
<p>Thank you both<br>
Pierre</p>

---

## Post #5 by @fedorov (2018-11-19 18:12 UTC)

<aside class="quote no-group" data-username="riep" data-post="4" data-topic="4805">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/riep/48/9933_2.png" class="avatar"> riep:</div>
<blockquote>
<p>Then, I would like to export this plane to a software in matlab that needs dicom as inputs.</p>
</blockquote>
</aside>
<p>The challenge in generating DICOM datasets is how to initialize or propagate relevant attributes to have a valid object as a result. “Valid” is an elusive concept here, because there is only one validator (<a href="http://www.dclunie.com/dicom3tools/dciodvfy.html">dciodvfy</a>), basically, and not all aspects of the dataset can be validated even with that validator.</p>
<p>Considering your situation, most likely your matlab code only cares about few DICOM attributes. It will probably be a much simpler task to add an adapter or modification to your matlab code to take something other than DICOM.</p>

---

## Post #6 by @lassoan (2018-11-20 15:32 UTC)

<p>4D volume sequence export to DICOM is available as soon as <a href="https://github.com/Slicer/Slicer/pull/1045">https://github.com/Slicer/Slicer/pull/1045</a> pull request is merged (probably tomorrow).</p>
<p>I fully agree with <a class="mention" href="/u/fedorov">@fedorov</a> in that if the goal is data exchange between Slicer and MATLAB then DICOM is not a good choice. Instead, you can easily read/write 4D volumes in nrrd format in both Slicer and MATLAB. You can find nrrd reader and writer for MATLAB <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver">here</a>.</p>

---

## Post #7 by @riep (2018-11-20 16:22 UTC)

<p>Thanks a lot for your answers. I am looking foward to test the 4D export plugin.<br>
You are both right concerning matlab, however I should have precised that the software use binaries bluit from matlab code. So unfortunatly we cannot modify the code.</p>

---

## Post #8 by @lassoan (2018-11-21 00:13 UTC)

<p>Export feature will be available in tomorrow’s nightly build. You need to install Sequences extension and load the 4D volume as “Volume sequence” (not as MultiVolume).</p>

---

## Post #9 by @riep (2018-11-21 08:26 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6081077789562cbd275598b5ab9f25ee304fe23.png" data-download-href="/uploads/short-url/uxpsiqTWu6TFgxjiO7gbNF0TIr1.png?dl=1" title="Sans%20titre" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6081077789562cbd275598b5ab9f25ee304fe23_2_690x364.png" alt="Sans%20titre" data-base62-sha1="uxpsiqTWu6TFgxjiO7gbNF0TIr1" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6081077789562cbd275598b5ab9f25ee304fe23_2_690x364.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6081077789562cbd275598b5ab9f25ee304fe23_2_1035x546.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6081077789562cbd275598b5ab9f25ee304fe23_2_1380x728.png 2x" data-dominant-color="A9A7A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sans%20titre</span><span class="informations">1919×1013 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Here is what I get when I load my dataset as a volume. As the acquisition is a stack of 2D cine, there may be some discrepancies in DIOCOM tags, as compared to “real” 4D acquisitions. As is it it does not allow to detect this dataset as a cine (see picture). Or maybe I miss something …</p>
<p>Thanks a lot for you help,<br>
PIerre</p>

---

## Post #10 by @lassoan (2018-11-21 15:29 UTC)

<p>Is it just a 2D+t data set (time sequence of 2D frames)?</p>

---

## Post #11 by @riep (2018-11-21 15:42 UTC)

<p>it’s multiple 2D+t slices.</p>

---

## Post #12 by @riep (2018-11-22 08:37 UTC)

<p>I can share a dataset if it can help.</p>
<p>Pierre</p>

---

## Post #13 by @lassoan (2018-11-23 03:52 UTC)

<p>If you share the images then I can check how much work would it be to add a rule to recognize it as a volume sequence.</p>

---

## Post #14 by @riep (2018-11-23 08:01 UTC)

<p>Thanks a lot for your help.<br>
Here is a representative dataset that I want to reformat. <a href="https://www.dropbox.com/s/w3rkvcyocwbslpj/9.rar?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/w3rkvcyocwbslpj/9.rar?dl=0</a><br>
It multiple 2D cine images acquired with a conventional cine sequence from Siemens.</p>

---

## Post #15 by @riep (2018-11-23 08:02 UTC)

<p>multiplevolume load this dataset correctly, I do not know if it could help you …</p>

---
