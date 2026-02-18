# Convert and export .stl file to .dcm

**Topic ID**: 13093
**Date**: 2020-08-19
**URL**: https://discourse.slicer.org/t/convert-and-export-stl-file-to-dcm/13093

---

## Post #1 by @wjd582 (2020-08-19 22:17 UTC)

<p>Hi everyone,</p>
<p>I would like to ask you to how to export the dicom file from .stl.<br>
I loaded .stl file (surface structure) and it had just outlier of the object.<br>
Is It possible to export as a dicom format?</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2020-08-19 22:23 UTC)

<p>What DICOM information object would you like to create from the segmentation: segmentation object, fake CT image, RT structure set,…?</p>

---

## Post #3 by @wjd582 (2020-08-20 02:29 UTC)

<p>Hi Andras,<br>
I want to create a fake CT image set using that .stl file. Actually, the stl file contains 3D surface object. So, I think each CT slices should have just contour of the 3d structure.<br>
Thanks in advance for any help you can give!</p>

---

## Post #4 by @lassoan (2020-08-20 02:48 UTC)

<p>What the fake CT is going to be used for radiation therapy planning? Deep learning training? Do you need to generate realistic intensities, texture, etc.?</p>

---

## Post #5 by @wjd582 (2020-08-20 02:52 UTC)

<p>I am going to use the fake CT for radiation therapy planning if possible. I just need CT image set that is contained the 3D structure. would it be possible?</p>

---

## Post #6 by @lassoan (2020-08-20 03:03 UTC)

<p>Do you want to paint in the structure (such as a device) into an existing CT image?</p>

---

## Post #7 by @wjd582 (2020-08-20 03:10 UTC)

<p>No, my stl file has a 3D surface structure just like empty can. Once the ct set is exported, I can probably create structures and assign CT numbers via treatment planning system.</p>

---

## Post #8 by @lassoan (2020-08-20 03:15 UTC)

<p>If you just the need the fake CT so that you can contour in the TPS then you can simplify the steps and just export the STL directly as an RT structure set. Install latest Slicer Preview Release, install SlicerRT extension to get the option of DICOM-RT export, load the STL file as segmentation (select “Segmentation” in Description column in Add data dialog), load the associated CT image (you cannot create valid RT structure set without referring to a CT), then use DICOM module to export the segmentation and CT.</p>

---

## Post #9 by @wjd582 (2020-08-20 03:19 UTC)

<p>Thanks a lot, I will try it and reply back. By the way, what does the associated CT mean?</p>

---

## Post #10 by @lassoan (2020-08-20 03:20 UTC)

<p>The planning CT, that contains real patient anatomy that the TPS can work on.</p>

---

## Post #11 by @wjd582 (2020-08-20 03:24 UTC)

<p>I see, but if there is no patient CT at all, is it impossible to generate CT?</p>

---

## Post #12 by @lassoan (2020-08-20 03:26 UTC)

<p>If you don’t have a CT then you can just use any CT that is taken of the body part you are interested in. If you don’t find a suitable image in Sample Data module then you can download form TCIA or similar freely accessible image databases.</p>

---

## Post #13 by @wjd582 (2020-08-20 03:28 UTC)

<p>Got it, thank you for your help!</p>

---

## Post #14 by @wjd582 (2020-08-20 16:21 UTC)

<p>I can export a file from 3D Slicer, but something are wrong. First, the type name of the file is not ‘DCM file’, it is ‘370 File’ (‘1.2.276.0.7230010.3.1.4.1525450623.10920.1597934964.370’). Second, the size of the file is 1920x1018 and count is 1. Actually, I opened the CT which has 512x512 and 127 slices.How can I adjust the size of the file that is to be exported? Third, I got some of error when I tried to open it in TPS as below.<br>
i) dicom module: image pixel: read error<br>
ii) dicom IOD: read error<br>
iii) reading the ‘secondary capture image storage’ failed.</p>
<p>What I did is as below.<br>
i) open my stl file<br>
ii) open real CT (127 slices)<br>
iii) align the 3d structure from stl file to CT image via ‘Transform’<br>
iv) create ‘NewSubject’ and ‘New child study’ and put CT, stl, and  transform into created new study<br>
v) export to dicom</p>
<p>Actually, what I want to do is,<br>
if there are some missing regions in CT, I want to make a extended CT via adding the structure from stl file.</p>
<p>Please advice me if I have to consider.<br>
Thanks in advance!</p>

---

## Post #15 by @lassoan (2020-08-20 17:46 UTC)

<aside class="quote no-group" data-username="wjd582" data-post="14" data-topic="13093">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/e36b37/48.png" class="avatar"> wjd582:</div>
<blockquote>
<p>First, the type name of the file is not ‘DCM file’, it is ‘370 File’</p>
</blockquote>
</aside>
<p>That’s all good. There is no such thing as “DICOM” file extension. “.dcm” file extension is commonly used, but it is just for users to recognize file format more easily.</p>
<aside class="quote no-group" data-username="wjd582" data-post="14" data-topic="13093">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/e36b37/48.png" class="avatar"> wjd582:</div>
<blockquote>
<p>Second, the size of the file is 1920x1018 and count is 1.</p>
</blockquote>
</aside>
<p>This looks like a scene bundle file, which contains the entire scene as a secondary capture image in a private field. This is not what you need.</p>
<p>Instead, choose “Export series” in the DICOM export dialog.</p>
<p>Also make sure you use latest Slicer Preview Release, it has many DICOM improvements and fixes.</p>

---

## Post #16 by @wjd582 (2020-08-21 01:39 UTC)

<p>Finally, I exported the dcm file from 3D Slicer and imported it to TPS. But, in TPS, only information added to the original planning CT area can be imported and other information is disappearing.</p>
<p>However, my goal is to create an extended CT by adding 3D scan file (stl file).<br>
For example, the planning CT has only chest region images, but I need to have a head region information as well. In this case, can I add the head region (just surface structure(.stl file)) and export entire information as the Dicom format (extended CT) through 3D Slicer?</p>
<p>Thanks,</p>

---

## Post #17 by @lassoan (2020-08-23 01:59 UTC)

<p>You can expand an image using Crop volume module (if the chosen ROI is larger than the input image). You may need to use interpolated mode.</p>

---

## Post #18 by @wjd582 (2020-08-24 13:27 UTC)

<p>I will try it. Many thanks!</p>

---
