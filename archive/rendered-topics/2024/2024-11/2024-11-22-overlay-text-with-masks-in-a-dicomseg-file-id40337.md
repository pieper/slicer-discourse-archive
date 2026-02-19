---
topic_id: 40337
title: "Overlay Text With Masks In A Dicomseg File"
date: 2024-11-22
url: https://discourse.slicer.org/t/40337
---

# Overlay text with masks in a dicomseg file

**Topic ID**: 40337
**Date**: 2024-11-22
**URL**: https://discourse.slicer.org/t/overlay-text-with-masks-in-a-dicomseg-file/40337

---

## Post #1 by @bywbilly (2024-11-22 20:54 UTC)

<p>Hi 3D Slicer Community,</p>
<p>I was trying to implement a dicomseg file that can contain both segmentation masks and their corresponding texts. I can compute the exact location of all the texts. For instance, I have L1 and L2 segmented, and I want L1 and L2 to appear in front of each vertebra when I open the dicomseg file in mimics.</p>
<p>I have tried the overlay plane module, but it seems that the slicer does not support it. Do you have any suggestions for that?</p>
<p>I have attached what I want below. And I like this happens for every slice.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fdcc200d0755b31e6d38efc524b606e6172fe82.jpeg" data-download-href="/uploads/short-url/kwFftYjHhxOPFABnHOB10LATTiy.jpeg?dl=1" title="3701732308816_.pic" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fdcc200d0755b31e6d38efc524b606e6172fe82_2_374x500.jpeg" alt="3701732308816_.pic" data-base62-sha1="kwFftYjHhxOPFABnHOB10LATTiy" width="374" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fdcc200d0755b31e6d38efc524b606e6172fe82_2_374x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fdcc200d0755b31e6d38efc524b606e6172fe82_2_561x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fdcc200d0755b31e6d38efc524b606e6172fe82_2_748x1000.jpeg 2x" data-dominant-color="696963"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3701732308816_.pic</span><span class="informations">1280×1707 332 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2024-11-22 21:19 UTC)

<p>A dicom seg instance will not support specifying the text display in any standard way.   I don’t know if anyone here has experience with mimics to know if there’s a kind of file you could generate to control that behavior.</p>

---

## Post #3 by @bywbilly (2024-11-22 21:28 UTC)

<p>Thanks for your prompt response. Thanks for the information that there is no standard way to embed text into the dicomseg file.</p>

---

## Post #4 by @cpinter (2024-11-23 20:11 UTC)

<p>Can you please explain your workflow so that we know why you want text burnt into your image? This should not be necessary if you use the right tools in the right workflow.</p>

---

## Post #5 by @bywbilly (2024-11-26 01:47 UTC)

<p>Hi Csbar,</p>
<p>We are developing a model for our customers and their PACS (visage) can only view dicomseg so I want to embed this text into the dicomseg. So when they open the dicomseg file, they can see the texts.</p>
<p>Thanks!</p>

---

## Post #6 by @cpinter (2024-11-27 12:06 UTC)

<aside class="quote no-group" data-username="bywbilly" data-post="5" data-topic="40337">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/7bcc69/48.png" class="avatar"> bywbilly:</div>
<blockquote>
<p>developing a model</p>
</blockquote>
</aside>
<p>I don’t understand, what kind of model are you developing?</p>
<aside class="quote no-group" data-username="bywbilly" data-post="5" data-topic="40337">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/7bcc69/48.png" class="avatar"> bywbilly:</div>
<blockquote>
<p>PACS (visage) can only view dicomseg</p>
</blockquote>
</aside>
<p>This does not seem correct. I suggest exporting DICOM SC (Secondary Capture) images, as historically that is the modality to store annotated screenshots. Any PACS must support that, it is part of DICOM for decades.</p>

---

## Post #7 by @bywbilly (2024-11-27 23:25 UTC)

<p>Thanks for your reply!</p>
<p>“The model” is an AI model for segmenting some stuff.</p>
<p>I tried secondary capture; however, if it is text, it won’t show up directly in the image like in my screenshot.</p>
<p>If it is a picture, I am unsure how it will appear in the visage, but in the 3D slicer, it won’t work. Moreover, a screenshot does not work in my case.</p>
<p>If something else comes to your mind, please share it. Thanks again for your help.</p>

---

## Post #8 by @cpinter (2024-11-28 10:52 UTC)

<aside class="quote no-group" data-username="bywbilly" data-post="7" data-topic="40337">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/7bcc69/48.png" class="avatar"> bywbilly:</div>
<blockquote>
<p>if it is text, it won’t show up directly in the image like in my screenshot.</p>
</blockquote>
</aside>
<p>SC is basically a screenshot. Whatever you put in the view will appear in the SC.</p>

---

## Post #9 by @twloehfelm (2025-09-05 21:43 UTC)

<p>I think OP is misunderstanding or conflating dicom seg and GSPS-type presentation state objects.</p>
<p>DICOM seg and GSPS are both separate dicom files that reference some source dicom file. That source file contains the source image voxel information. A DICOM seg object references a source file and defines which voxels of it correspond to specific structures of interest. So the “pixel information” of a DICOM seg object is often a pixel mask, were 0 = “not the structure of interest” and 1 = “the structure of interest”. In this scenario, there is no concept in that seg file “pixel data” to hold a label, circle, or other sort of annotation. The labels that tell you what the structure is (“L1 vertebral body”, for example) are in the dicom seg header metadata, not the pixel data.</p>
<p>Similarly GSPS is a dicom file that references a source image file. In GSPS you can define text annotations, arrows, etc, and define which source file they reference, and precisely where on the source file they are to be drawn.</p>
<p>So you can’t solve this problem only by considering the dicom seg object. But you can create GSPS or similar objects along with the seg objects. The seg will define where the structure is, the the presentation state will define what text overlays to apply and where - you can use the information from the seg object to determine this. Both are meaningless without the referent DICOM image file, but together might address the issue.</p>

---
