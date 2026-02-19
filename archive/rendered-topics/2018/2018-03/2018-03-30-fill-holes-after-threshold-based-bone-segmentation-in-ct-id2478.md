---
topic_id: 2478
title: "Fill Holes After Threshold Based Bone Segmentation In Ct"
date: 2018-03-30
url: https://discourse.slicer.org/t/2478
---

# Fill holes after threshold-based bone segmentation in CT

**Topic ID**: 2478
**Date**: 2018-03-30
**URL**: https://discourse.slicer.org/t/fill-holes-after-threshold-based-bone-segmentation-in-ct/2478

---

## Post #1 by @alessandronavacchia (2018-03-30 18:16 UTC)

<p>Hi all,</p>
<p>I am segmenting the geometries of femur, tibia, fibula and patella from a CT scan using Threshold effect.<br>
What is the best tool to fill the holes inside the segmented cortical layer (see picture below)? I would like to export an .stl file with only the outside surface.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/7023df0ac4d20969f25f35c74d520e77c77e664c.png" alt="Picture1" data-base62-sha1="g02kusTzg0cHAvWbsCo1iWaZbaY" width="416" height="357"></p>
<p>Where the cortical layer is thin (e.g. at the epiphysis) there are some gaps in the segmentation (see picture below). Are there smart ways to fill the holes accounting for those gaps without closing them manually?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b189ce32be59e2685e9de0cd7862221fd8b3b4cb.png" data-download-href="/uploads/short-url/pkzL415Th9netmcqOtAj5V6sfCX.png?dl=1" title="Picture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b189ce32be59e2685e9de0cd7862221fd8b3b4cb_2_609x500.png" alt="Picture2" data-base62-sha1="pkzL415Th9netmcqOtAj5V6sfCX" width="609" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b189ce32be59e2685e9de0cd7862221fd8b3b4cb_2_609x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b189ce32be59e2685e9de0cd7862221fd8b3b4cb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b189ce32be59e2685e9de0cd7862221fd8b3b4cb.png 2x" data-dominant-color="201210"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture2</span><span class="informations">652×535 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks!</p>
<p>Alessandro</p>

---

## Post #2 by @lassoan (2018-03-31 01:45 UTC)

<p>If you are lucky then with “Smoothing” effect you can fill the gaps and then you can fill cavities using “Flood filling” effect (in SegmentEditorExtraEffects extension).</p>
<p>Unfortunately, often you cannot make your mesh watertight easily. In such cases, follow these instructions:</p>
<aside class="quote quote-modified" data-post="2" data-topic="960">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-edit-stl-file/960/2">Bone segmentation to create 3D-printable STL</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In the STL that you linked, large portions of the bone is missing, so I don’t think it make sense to “fix” it. Instead, I would recommend to redo the segmentation. 
I would recommend to use the latest nightly version of Slicer and perform the following steps: 

reduce image noise: use Cast Scalar Volume' module to convert input volume to Float type; use Simple Filtersmodule withGradientAnisotropicDiffusionImageFilter` on the converted volume
go to Segment Editor module, use the noise-reduced vol…
  </blockquote>
</aside>


---

## Post #3 by @alessandronavacchia (2018-04-09 20:07 UTC)

<p>Dear Andras,</p>
<p>thanks for your quick response. I was eventually able to fix the segmentation using the “Closing (fill holes)” tool in the “Smoothing” Module after some minimal manual painting. When few large holes were left inside the bone, I inverted the mask (“Logical operators” -&gt; “Invert”), removed the big islands one by one (“Islands” -&gt; “Remove selected islands”), and inverted the mask again.</p>
<p>I could not figure out how to fill the cavities with “Flood filling”…</p>
<p>Thanks for your help!</p>
<p>Alessandro</p>

---
