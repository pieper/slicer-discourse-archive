---
topic_id: 31888
title: "How To Substract Two Stl Files"
date: 2023-09-25
url: https://discourse.slicer.org/t/31888
---

# How to substract two STL files?

**Topic ID**: 31888
**Date**: 2023-09-25
**URL**: https://discourse.slicer.org/t/how-to-substract-two-stl-files/31888

---

## Post #1 by @Inka_Saraswati (2023-09-25 14:49 UTC)

<p>I have 2 STLs, one is a model of bone with defect, the other one is an intact one. I want to get a 3D model of the defect (the difference between the two files). I know how to substract with  Logical Operators in Segment Editor, but I believe it only works if I did a segmentation from volume data (such as CT) in the Slicer itself. I want to be able to import 2 STLs and substract them. How to do it in Slicer?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2023-09-25 15:06 UTC)

<p>You can load the two STLs as segmentation and use the logical operators as you describe.  But depending on where they came from they probably won’t line up correctly.  So you need to first register them either manually or with a <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#model-registration">model registration</a> tool.  This can be challenging when parts are missing from one of the bones, but you should be able to get a good approximation.</p>

---

## Post #3 by @Inka_Saraswati (2023-09-26 02:04 UTC)

<p>I’ve done registration with SlicerIGT (still not perfect but I just want to try the features for now). I’ve  tried 2 things that didn’t really work.</p>
<ol>
<li>
<p>This one I’ve imported the two STLS as models, and all of the Segment Editor is greyed out. My models did not appear in the Segmentation list.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfda10350f99d0062107d9fe544ae5b09ea9b2b9.png" data-download-href="/uploads/short-url/vWhFOnxbIGLH0AbZEH0LPgVYcLT.png?dl=1" title="import as model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfda10350f99d0062107d9fe544ae5b09ea9b2b9_2_690x406.png" alt="import as model" data-base62-sha1="vWhFOnxbIGLH0AbZEH0LPgVYcLT" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfda10350f99d0062107d9fe544ae5b09ea9b2b9_2_690x406.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfda10350f99d0062107d9fe544ae5b09ea9b2b9_2_1035x609.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfda10350f99d0062107d9fe544ae5b09ea9b2b9_2_1380x812.png 2x" data-dominant-color="939397"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">import as model</span><span class="informations">2880×1698 297 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>I’ve also tried importing the two STLs as segmentation. My data did appear in the Segmentation list in the Segment Editor, but I can only choose one or the other. And all the buttons on the left are also greyed out, including Logical Operators.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5fcd1a456c973be923af26114dacfdf43a28521.png" data-download-href="/uploads/short-url/ux1mwfZG3P9klExUZccC67LHsit.png?dl=1" title="import as segmentation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5fcd1a456c973be923af26114dacfdf43a28521_2_690x405.png" alt="import as segmentation" data-base62-sha1="ux1mwfZG3P9klExUZccC67LHsit" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5fcd1a456c973be923af26114dacfdf43a28521_2_690x405.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5fcd1a456c973be923af26114dacfdf43a28521_2_1035x607.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5fcd1a456c973be923af26114dacfdf43a28521_2_1380x810.png 2x" data-dominant-color="929397"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">import as segmentation</span><span class="informations">2880×1692 333 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>What should I do so I can substract them?</p>

---

## Post #4 by @pieper (2023-09-27 23:41 UTC)

<p>You probably need to import one of the CT scans too so the segment editor has a reference volume, then you can edit.  Use the Segmentations module to copy a segment from one segmentation to the other.</p>

---

## Post #5 by @lassoan (2023-09-28 02:02 UTC)

<p>Loading the original CT as <a class="mention" href="/u/pieper">@pieper</a> suggested is the best, as it allows you to verify that all segmentation operations are sufficiently accurate. Alternatively, you can create a default blank volume as described in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#editing-a-segmentation-imported-from-model-surface-mesh-file">documentation</a>.</p>
<p>Your segmented surfaces look very noisy. You could consider smoothing it before doing any other operation. Also, volumetry is not appropriate for compatison when you work with very thin structures as we can see in your image. Instead, you can measure surface-to-surface distance (using ModelToModelDistance extension) or you can fill in cavities and work with solid objects (using <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify#surface-wrap-solidify">SurfaceWrapSolidify extension</a>).</p>

---
