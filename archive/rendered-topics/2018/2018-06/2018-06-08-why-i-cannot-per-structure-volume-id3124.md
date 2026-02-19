---
topic_id: 3124
title: "Why I Cannot Per Structure Volume"
date: 2018-06-08
url: https://discourse.slicer.org/t/3124
---

# Why I cannot Per-Structure Volume

**Topic ID**: 3124
**Date**: 2018-06-08
**URL**: https://discourse.slicer.org/t/why-i-cannot-per-structure-volume/3124

---

## Post #1 by @Fang (2018-06-08 11:53 UTC)

<p>Operating system: Windows10<br>
Slicer version: 4.9.0</p>
<p>Since I have an ‘STL’ file. I use segmentation module in order to get the labelmap.<br>
And using that labelmap as an input data.</p>
<p>However, I cannot use the Per-Structure Volume to separate each part of the tooth.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad5f3d85e0e47d99de49fd616490511cf1d86b91.jpeg" data-download-href="/uploads/short-url/oJIExmBoKR0u5iXgobTCM7p49EJ.JPG?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad5f3d85e0e47d99de49fd616490511cf1d86b91_2_690x350.JPG" alt="Capture1" data-base62-sha1="oJIExmBoKR0u5iXgobTCM7p49EJ" width="690" height="350" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad5f3d85e0e47d99de49fd616490511cf1d86b91_2_690x350.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad5f3d85e0e47d99de49fd616490511cf1d86b91_2_1035x525.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad5f3d85e0e47d99de49fd616490511cf1d86b91_2_1380x700.JPG 2x" data-dominant-color="74777A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">2560×1299 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I would like to ask that how can I use the Per-Structure in this situation?<br>
Does 3DSlicer support for the tooth anatomy?</p>
<p>Thanks for your help,<br>
Best regards,</p>

---

## Post #2 by @cpinter (2018-06-08 12:33 UTC)

<p>Hi Fang,</p>
<p>Please try the newer Segment Editor module. It has more advanced “per-structure” handling, as inherently it stores the segmentations as per-structure labelmaps (segments). You can find tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">here</a>.</p>
<p>Although I’m not sure I understand your question. An STL file can only contain one structure. How do you have multiple structures? Also if you use the segmentation module as you say, then how come you edit the labelmap and not the segmentation?</p>

---

## Post #3 by @Fang (2018-06-08 12:59 UTC)

<p>Hi Csaba,</p>
<p>Thank you for your helping.<br>
I got a problem as <a href="https://discourse.slicer.org/t/stl-file-uploaded-does-not-appear-as-a-volume/3114/2">this link</a></p>
<p>As you said, the STL file contains one structure so I follow the suggestion and then I got the labelmap.<br>
My aim is to segment the tooth from the STL. But I don’t sure for the process how can I do that.</p>

---

## Post #4 by @cpinter (2018-06-08 13:16 UTC)

<p>Hi Fang,</p>
<p>An STL file contains one surface mesh, which represents one segmentation. You don’t need to (and cannot) segment it. If you want to segment the different parts of the tooth, then you need to have the CT, in DICOM, or one of the research formats such as nrrd. As opposed to the STL, those contain a 3D image with different intensities in the voxels. Those are the images we have to segment.</p>

---

## Post #5 by @cpinter (2018-06-08 14:13 UTC)

<p>I created a simple slide explaining the typical data formats encountered when segmentation is involved:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/4014597a8298a92002e6e13cfacd320fe51ce4eb.png" data-download-href="/uploads/short-url/98S9IBNaDX3aZRlXAmAnkVuvllV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/4014597a8298a92002e6e13cfacd320fe51ce4eb_2_690x368.png" alt="image" data-base62-sha1="98S9IBNaDX3aZRlXAmAnkVuvllV" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/4014597a8298a92002e6e13cfacd320fe51ce4eb_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/4014597a8298a92002e6e13cfacd320fe51ce4eb_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/4014597a8298a92002e6e13cfacd320fe51ce4eb_2_1380x736.png 2x" data-dominant-color="CFDFD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1751×934 367 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I also uploaded the <a href="https://www.slicer.org/wiki/File:SlicerDataFormats.pptx">pptx</a> and here is the png’s <a href="https://www.slicer.org/wiki/File:SlicerDataFormats.png">wiki location</a>. <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> where do you think I should put this on the wiki?</p>

---

## Post #6 by @lassoan (2018-06-08 14:20 UTC)

<p>Looks good! You could upload it here: <a href="http://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html">http://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html</a></p>

---

## Post #7 by @lassoan (2018-06-08 14:43 UTC)

<aside class="quote no-group" data-username="Fang" data-post="3" data-topic="3124">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/96bed5/48.png" class="avatar"> Fang:</div>
<blockquote>
<p>My aim is to segment the tooth from the STL</p>
</blockquote>
</aside>
<p>If you mean that you would like to split the segment into multiple parts then you may follow this segmentation recipe for cutting segments into multiple pieces: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/" class="inline-onebox">Overview | 3D Slicer segmentation recipes</a></p>

---

## Post #8 by @cpinter (2018-06-08 14:59 UTC)

<p>You will still need the original anatomical image though, otherwise you cannot know where to cut.</p>

---

## Post #9 by @cpinter (2018-06-08 15:04 UTC)

<p>I created a short page about Data Loadng and Saving in the documentation, including this diagram too:<br>
<a href="http://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html" class="onebox" target="_blank">http://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html</a></p>

---

## Post #10 by @Fang (2018-06-09 16:31 UTC)

<p>Thank you for your suggestion.<br>
I already follow your link and I feel wondering.</p>
<p>Could it be possible to make the image(blue arrow) to be transparent?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4e974849e0d4e5165802bc61a297203e19de6fb.jpeg" data-download-href="/uploads/short-url/pOq7rotPNpscHcEtTH4qD1F6ZgD.JPG?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4e974849e0d4e5165802bc61a297203e19de6fb_2_550x500.JPG" alt="Capture2" data-base62-sha1="pOq7rotPNpscHcEtTH4qD1F6ZgD" width="550" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4e974849e0d4e5165802bc61a297203e19de6fb_2_550x500.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4e974849e0d4e5165802bc61a297203e19de6fb_2_825x750.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4e974849e0d4e5165802bc61a297203e19de6fb_2_1100x1000.JPG 2x" data-dominant-color="303639"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">1401×1272 84.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @Fang (2018-06-09 16:36 UTC)

<p>Thank you for helping me.</p>
<p>What do you mean for the original anatomical image?<br>
Actually, I don’t know where to cut and also which area represents the original anatomical image.</p>

---

## Post #12 by @lassoan (2018-06-09 17:15 UTC)

<p>You can adjust display settings, such as transparency, in the Segmentations module / Display section. You can make transparent all segments or just specific ones.</p>

---

## Post #13 by @cpinter (2018-06-11 13:45 UTC)

<p>Original anatomical image = The CT based on which the STL model was made. You cannot just “draw” a tooth model from nothing, you need the CT. Please see the diagram above.</p>

---

## Post #14 by @Fang (2018-06-13 14:26 UTC)

<p>Thank you for your all suggestion.<br>
It can help me a lot :))</p>

---
