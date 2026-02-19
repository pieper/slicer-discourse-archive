---
topic_id: 17998
title: "Extract The Coronary And Aorta"
date: 2021-06-07
url: https://discourse.slicer.org/t/17998
---

# Extract the coronary and aorta

**Topic ID**: 17998
**Date**: 2021-06-07
**URL**: https://discourse.slicer.org/t/extract-the-coronary-and-aorta/17998

---

## Post #1 by @smm9886 (2021-06-07 16:46 UTC)

<p>Operating system: Windows 64 bit<br>
Slicer version: 4.11.20210226 r29738 / 7a593c8<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi all,</p>
<p>I could get to know about the Slicer about 2 weeks ago. So far I could read several of the Slicer documentation files as well as watching several tutorial videos. However, I could not yet understand how to use this software in an organized manner.<br>
Specifically, I have a set of thorax and heart DICOM files. I need to extract the coronary artery and aorta from the whole domain and save it into the STL format. Anyone can please suggest to me some solutions how I can use (efficiently, not like to use the scissor to cut parts to get to the coronary) the Slicer to get this goal, I will appreciate it. I can provide more details if necessary.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2021-06-08 03:50 UTC)

<p>If you have contrasted CTs then aorta segmentation should be trivial (even simple thresholding will give you good results). However, coronary artery segmentation is challenging, because the vessels are thin, so you need to acquire and work with a high-resolution image, and since their voxel intensities are very similar to surrounding regions you need to use sophisticated segmentation methods (simple thresholding or region growing is not sufficient).</p>
<p>One option is to use Grow from seeds method, similarly as you would do it for whole heart segmentation, but you would place separate seeds into the major coronary vessels:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="BJoIexIvtGo" data-video-title="Whole heart segmentation from cardiac CT in 10 minutes" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=BJoIexIvtGo" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/BJoIexIvtGo/maxresdefault.jpg" title="Whole heart segmentation from cardiac CT in 10 minutes" width="" height="">
  </a>
</div>

<p>Since you need to work with a high-resolution volume and you may need to place several seeds along each vessel to ensure that the complete vasculature is segmented, this can be a time-consuming process (probably about 30 minutes per segmentation, after you got familiar with all the tools; with a strong computer). The advantage of segmenting the vessels is that then you can automatically extract centerlines and compute vessel diameters (using Extract Centerline module in SlicerVMTK extension).</p>
<p>An alternative approach is to place curve markup points manually along the vessel centerline. You can do this either in slice views (shifting and rotating slice views) or in a volume rendered view. You can place points very quickly in volume rendering but first you need to do an approximate segmentation of the heart to remove ribs, spine, etc. so that they don’t occlude the view. This can be done in a few minutes using Surface cut and Mask volume effects.</p>
<p>What is your end goal? Making training phantoms? Printing models for demonstration? How many cases do you need to segment? Are there any specific time constraints or accuracy requirements?</p>

---

## Post #3 by @smm9886 (2021-06-09 08:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="17998">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>with a strong computer</p>
</blockquote>
</aside>
<p>I much appreciate your prompt and helpful reply message to my question.</p>
<p>1- How can I know about the image resolution of my DICOM file? I, an engineering Ph.D. student, received these DICOM data files from a physician. In Slicer it says, Modality: CT, Size: 512 x 512, Count: 545, and Spacing 0.34mm x 0.34mm x 0.30mm.</p>
<p>2- I can better understand now that you mentioned: “ <em>…with a strong computer…</em> ”. There are some moments in my working with 3D Slicer, that my computer (RAM 6GB, Processor Intel(R) Xeon(R) CPU 2.53GHz) freezes and absolutely stops from working till I press the restart button.</p>
<p>3- I have 2 sets of thorax and abdomen DICOM files, one is with the normal coronaries, and the other is with abnormal coronaries. I need to extract the Aortic sinuses of Valsalva, ascending aorta, and coronaries from these 2 files. Next, I need to export them to the STL files. Then, I should pass these STL files to a bio-manufacturer so they can make the silicone phantoms for us (I think they use 3D printing technology). Then we want to connect those phantoms to a pulsatile pump and study the flow patterns within these models. This is important for us that the final phantom models resemble accurately nature.</p>
<p>I need to pass these STL data files to the company as soon as possible so they can start the manufacturing process and thus we can start our experimental studies which are part of my Ph.D. research thesis.</p>
<p>I hope I could clarify better the situation. I can provide more details if necessary. I look forward to hearing back from you.</p>
<p>Best wishes,</p>
<p>Mahmoud</p>

---

## Post #4 by @lassoan (2021-06-09 20:47 UTC)

<p>With 6GB of physical RAM I’m surprised that you can load a volume of 512x512x545 voxels at all. I would recommend minimum of 16GB RAM, an Intel Core i7 CPU, and a computer not more than 3 years old.</p>
<p>Since you will only create a few models, it should be no problem to invest a lot of time in the segmentation process. As you also want high accuracy, it is probably better to not use curves (which would only give you vessel centerline curves and not diameters), but simply set an editable threshold range and then paint the vessels in 3D or slice views. I’ve uploaded a short video tutorial here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="aeOFl19fh_c" data-video-title="Coronary vessel segmentation on cardiac CT images" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=aeOFl19fh_c" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/aeOFl19fh_c/maxresdefault.jpg" title="Coronary vessel segmentation on cardiac CT images" width="" height="">
  </a>
</div>


---

## Post #5 by @smm9886 (2021-06-10 05:55 UTC)

<p>I understand your points. That video should help a lot. I will try to follow the steps soon (tomorrow with my pc in the university) to see how it works. Thank you, for your prompt help and assistance.</p>

---
