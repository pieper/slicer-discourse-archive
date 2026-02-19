---
topic_id: 9663
title: "Whole Brain Segmentation Registration"
date: 2019-12-30
url: https://discourse.slicer.org/t/9663
---

# Whole brain segmentation registration 

**Topic ID**: 9663
**Date**: 2019-12-30
**URL**: https://discourse.slicer.org/t/whole-brain-segmentation-registration/9663

---

## Post #1 by @DanTran (2019-12-30 15:04 UTC)

<p>Hi, my project consists of fully segmenting non-human brains ex-vivo in order to compute difference in the volume of brain tissue between pre and postoperative conditions. My questions are:</p>
<ul>
<li>what format should I use to save my segmentation in order to perform rigid and affine registration?</li>
<li>how do I determine the amount of image deformation postregistration?<br>
I am currently using Elastix, but am open to anything else. Thank you.</li>
</ul>
<p>Best,</p>
<p>Dan</p>

---

## Post #2 by @lassoan (2019-12-30 15:30 UTC)

<aside class="quote no-group" data-username="DanTran" data-post="1" data-topic="9663">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c6cbf5/48.png" class="avatar"> DanTran:</div>
<blockquote>
<p>what format should I use to save my segmentation in order to perform rigid and affine registration?</p>
</blockquote>
</aside>
<p>In general, I would recommend NRRD (.nrrd) file format for this. For brain imaging, you may find Nifti (.nii) format useful, too, because it is very commonly used in neuroimaging.</p>
<aside class="quote no-group" data-username="DanTran" data-post="1" data-topic="9663">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c6cbf5/48.png" class="avatar"> DanTran:</div>
<blockquote>
<p>how do I determine the amount of image deformation postregistration?</p>
</blockquote>
</aside>
<p>You can assess the resulting transform using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms">Transforms module</a>.</p>
<p>          <a href="https://www.slicer.org/w/img_auth.php/b/b0/GlyphArrow2d.png" target="_blank" rel="noopener" class="onebox">
            <img src="https://www.slicer.org/w/img_auth.php/b/b0/GlyphArrow2d.png" width="378" height="323">
          </a>
</p>
<p>There are many visualization options, you can see displacement vector value at current mouse pointer position in “Information” section. You can compute average displacement in regions defined by segments (created in Segment Editor) by computing Segment Statistics on displacement magnitude image (created in Transforms module / Convert, Magnitude only =&gt; checked, Apply).</p>

---

## Post #3 by @DanTran (2019-12-30 15:04 UTC)

<p>Hi,</p>
<p>I work on bovine brains and am trying to fully segment pre and postoperative MRIs, then register them to compute the difference in brain tissue between the two sets of MRIs. I have put plastic fiducials to help with registration but am facing a few difficulties.</p>
<ul>
<li>Because of the amount of brain deformation during image acquisition, I have trouble doing a rigid registration before applying affine registration. Is there a way to designate whole structures as fiducials on 3D slicer before registration?</li>
<li>What format should I save my segmentations in to do registration of segmentations? I am trying to register 2 whole brain segmentations.</li>
</ul>
<p>Thank you.</p>
<p>Dan</p>

---

## Post #4 by @lassoan (2019-12-31 03:50 UTC)

<aside class="quote no-group" data-username="DanTran" data-post="3" data-topic="9663">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c6cbf5/48.png" class="avatar"> DanTran:</div>
<blockquote>
<p>Because of the amount of brain deformation during image acquisition, I have trouble doing a rigid registration before applying affine registration.</p>
</blockquote>
</aside>
<p>If you use intensity-based image registration then you don’t need a very accurate initial alignment. It is enough to identify a few basic anatomical landmarks in the brain or skull.</p>
<aside class="quote no-group" data-username="DanTran" data-post="3" data-topic="9663">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c6cbf5/48.png" class="avatar"> DanTran:</div>
<blockquote>
<p>Is there a way to designate whole structures as fiducials on 3D slicer before registration?</p>
</blockquote>
</aside>
<p>You can register entire segmented structures using Segment Registration extension.</p>

---
