---
topic_id: 3475
title: "Model Maker External Binary Nifti Mask"
date: 2018-07-12
url: https://discourse.slicer.org/t/3475
---

# model maker- external (binary) nifti mask

**Topic ID**: 3475
**Date**: 2018-07-12
**URL**: https://discourse.slicer.org/t/model-maker-external-binary-nifti-mask/3475

---

## Post #1 by @Moran_Artzi (2018-07-12 16:35 UTC)

<p>Operating system: Win 64<br>
Slicer version: 4.8.1</p>
<p>Hi all,<br>
I’m trying to use model maker to do 3D visualization of external (binary) nifti mask<br>
On the older Slicer version i used to upload and assign such a mask as label and then a model could be easily produced<br>
How should this be done in the new version?</p>
<p>Thanks<br>
Moran</p>

---

## Post #2 by @lassoan (2018-07-12 17:09 UTC)

<p>Model maker module has not changed in the last couple of years, so you can still use it the same way as before.</p>
<p>If you wanted to edit the labelmap then you would import it to a segmentation node and there are many new possibilities around there. But if you just want to convert a labelmap to models then Model maker should work just fine.</p>

---

## Post #3 by @Moran_Artzi (2018-07-12 17:46 UTC)

<p>Thanks for your fast reply</p>
<p>I uploaded the Lesion file</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd1f77519f52d6cf9a9b65a410060b085d9b52ea.png" data-download-href="/uploads/short-url/vy8W4SOwlp3nNOn7iciBDmhE6am.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd1f77519f52d6cf9a9b65a410060b085d9b52ea.png" data-base62-sha1="vy8W4SOwlp3nNOn7iciBDmhE6am" width="562" height="108" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">740×142 4.65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But at the model maker, on the IO: Input/output parameters Tab</p>
<p>I can not see this file</p>
<p>What should I change?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/9889067ce01bb4648a60e507de846459e780097c.png" data-download-href="/uploads/short-url/lLo9mfZ3MDSgo8AJyiIuESzAy6M.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9889067ce01bb4648a60e507de846459e780097c_2_451x500.png" data-base62-sha1="lLo9mfZ3MDSgo8AJyiIuESzAy6M" width="451" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9889067ce01bb4648a60e507de846459e780097c_2_451x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9889067ce01bb4648a60e507de846459e780097c_2_676x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9889067ce01bb4648a60e507de846459e780097c_2_902x1000.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">902×997 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2018-07-12 18:01 UTC)

<p>Model maker requires labelmap volume as input. In the <em>Add data</em> dialog, check <em>Label</em> option to indicate that the file should be interpreted as labelmap. If you’ve forgot to set it when you loaded the file, you can convert scalar volume to labelmap volume in Volumes module.</p>

---

## Post #5 by @Moran_Artzi (2018-07-13 04:20 UTC)

<p>Works perfect,  Thanks a lot!</p>

---
