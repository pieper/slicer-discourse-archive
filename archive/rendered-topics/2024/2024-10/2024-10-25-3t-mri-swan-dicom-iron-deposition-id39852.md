---
topic_id: 39852
title: "3T Mri Swan Dicom Iron Deposition"
date: 2024-10-25
url: https://discourse.slicer.org/t/39852
---

# 3T MRI SWAN DICOM--Iron Deposition?

**Topic ID**: 39852
**Date**: 2024-10-25
**URL**: https://discourse.slicer.org/t/3t-mri-swan-dicom-iron-deposition/39852

---

## Post #1 by @EIectricalinjuryStud (2024-10-25 03:27 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.7.0<br>
Expected behavior: View Iron Deposition on DICOM 3T MRI SWAN<br>
Actual behavior: I am a new user giving a presentation on Iron deposition in the nervous system post electrical injury. I successfully uploaded the DICOM images in which the neurologist identified abnormal iron deposition for Patient’s age, but I need assistance in how to change my slicer settings to take a screen grab of the iron deposition for my presentation.</p>

---

## Post #2 by @mikebind (2024-10-25 17:54 UTC)

<p>Easiest might be to just take a screen capture using your OS (for example, Win+Shift+S on Windows).  Within Slicer, there is a screen capture button on the toolbar which looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b61a89788cd01ff9b7b0534af57cf3c866eda0e.png" data-download-href="/uploads/short-url/1CGu36HSytAVSWtkP4TnUiQUfNQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b61a89788cd01ff9b7b0534af57cf3c866eda0e.png" alt="image" data-base62-sha1="1CGu36HSytAVSWtkP4TnUiQUfNQ" width="240" height="140"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">240×140 5.63 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When you click on it, configure what you want to capture, and then click the “Save As:” button to choose where you want to save the captured image.</p>
<p>If you want to capture something more complicated, like scrolling through a series of images, a 3D rotation, or similar, the ScreenCapture module offers options for that <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/screencapture.html" rel="noopener nofollow ugc">Screen Capture — 3D Slicer documentation</a></p>

---

## Post #3 by @EIectricalinjuryStud (2024-10-25 22:33 UTC)

<p>Thank you so much. That’s precisely what I want to do.</p>
<p>I needed to be more clear in my question.</p>
<p>How do I configure slicer to view the iron deposition on a SWI DICOM image?</p>
<p>I ask because I’m neither a radiologist nor a neurologist. The report identifying extremely elevated iron was a second opinion on what was previously identified as a “normal” scan.</p>
<p>The second reading was done by a vascular neurologist who specializes in memory loss and vascular dementia–who knew how to change the configuration to view the iron an differentiate it from calcium deposition position.</p>
<p>Any assistance I can have to make that configuration would be absolutely appreciated and I will acknowledge your help in my presentation.</p>
<p>My goal is to show the “normal” scan and change the configuration to identify the iron deposition. That way my colleagues who are not trained as radiologists and neurologists can comprehend how a person with a “normal” brain scan that experiences symptoms of iron deposition, must be referred for a 3T MRI SWI–because without changing the configuration–iron deposition is invisible on the scan. Currently, most electrical injury survivors are told their symptoms are “just in your head”… and they are, just not in the way a doctor untrained in vascular neurology implies .</p>
<p>Thank you in advance for your time and assistance in my presentation. on Electrical injury’s rehabilitation needs.</p>

---

## Post #4 by @mikebind (2024-10-26 00:31 UTC)

<p>I don’t have any special expertise in SWI or other imaging of iron deposition.  Especially for a particular patient case, I would recommend consulting with the physician who did the read and produced the report. They may be able to easily provide you with screenshots highlighting what imaging features they see and how the same region looks in non-SWI imaging for the same patient.  Failing that, I would consult with another neurologist or radiologist with the relevant expertise.  You can also look for links online for examples of how iron deposition appears on SWI imaging and how that differs from how calcification appears, but  it would be much more reliable if you can talk to an expert.</p>

---

## Post #5 by @EIectricalinjuryStud (2024-10-27 16:54 UTC)

<p>I understand. This presentation will not be used to for diagnosis or treatment of the patient whose consent I have to use it. It is simply to use for educational purposes in helping others recognize the consequences of repetitive low-voltage electrical injury.</p>
<p>I will try reaching out to the neurologist again. My presentation is next month. Hopefully he will respond before my presentation. I’ve not yet heard back which is why I am attempting to pull the image he identified as showing elevated iron deposition with help from other MRI experts who have more time. Thanks!</p>

---

## Post #6 by @mikebind (2024-10-28 21:39 UTC)

<p>Some quick searching suggests that iron deposition shows up as hypointensity (low voxel values; darker areas) of certain brain regions on SWI images.  Areas of hypointensity or hyperintensity (high voxel values; lighter areas) can be made more visually conspicuous by adjusting the windowing and leveling of the grayscale voxel values.  In Slicer, you can adjust the windowing and leveling on the currently loaded image by using the Window/Level mouse mode (see  <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#mouse-modes" rel="noopener nofollow ugc">slicer.readthedocs.io/en/latest/user_guide/user_interface.html#mouse-modes</a>).  Once you have selected this mode, left-click and drag on the image to adjust the image contrast.  Dragging up makes everything darker, dragging down makes everything lighter, dragging left narrows the window of grayscale values, and dragging right widens the window of grayscale values. You may be familiar with this feature, all medical imaging software has this type of functionality.</p>
<p>In your case, if you know the affected brain region, you can navigate the slice views to that region in Slicer, and then you should be able to adjust the windowing and leveling to clearly show the affected brain region as darker than other brain regions. Then you can take a screenshot and use that for your presentation.</p>

---

## Post #7 by @EIectricalinjuryStud (2024-10-30 20:34 UTC)

<p>Stellar! Thank you so much!</p>

---
