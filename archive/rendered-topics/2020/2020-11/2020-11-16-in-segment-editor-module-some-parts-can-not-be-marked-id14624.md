---
topic_id: 14624
title: "In Segment Editor Module Some Parts Can Not Be Marked"
date: 2020-11-16
url: https://discourse.slicer.org/t/14624
---

# In Segment Editor module some parts can not be marked

**Topic ID**: 14624
**Date**: 2020-11-16
**URL**: https://discourse.slicer.org/t/in-segment-editor-module-some-parts-can-not-be-marked/14624

---

## Post #1 by @Aitekk (2020-11-16 02:57 UTC)

<p>In Segment Editor module, the editable area of the volume is smaller than the whole volume, which makes some parts can not be marked</p>
<p>Operating system:Windows 10<br>
Slicer version:4.11<br>
Expected behavior:The whole volume should be editable by Paint tool.<br>
Actual behavior:The editable area of the volume is smaller than the whole volume. In fact, I’m limited to a local area when I’m tagging with the Paint tool, which prevents me from getting the desired segment (as shown in the videos and images below). that’s strange. I would appreciate for the help.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df5c3182ce005f8f018277e5a109305ffa41ef46.gif" alt="ezgif.com-crop" data-base62-sha1="vRVZXygeBhWtaqOmlrXsRIP2ctM" width="305" height="221" class="animated"> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bff3e5e18353cb7eb079f70885db497cbbd3fc03.jpeg" data-download-href="/uploads/short-url/ro5Kf3hP3oraMXjaTPv0TyfJ1wT.jpeg?dl=1" title="16054953982449" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bff3e5e18353cb7eb079f70885db497cbbd3fc03_2_345x225.jpeg" alt="16054953982449" data-base62-sha1="ro5Kf3hP3oraMXjaTPv0TyfJ1wT" width="345" height="225" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bff3e5e18353cb7eb079f70885db497cbbd3fc03_2_345x225.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bff3e5e18353cb7eb079f70885db497cbbd3fc03_2_517x337.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bff3e5e18353cb7eb079f70885db497cbbd3fc03_2_690x450.jpeg 2x" data-dominant-color="3B4045"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">16054953982449</span><span class="informations">1278×835 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-11-16 07:20 UTC)

<p>Resolution and extent of the segmentation is determined by the first selected master volume. The simplest is to choose the first master volume to be the volume that you will use later for segmentation, but you can change the extent anytime (by clicking on the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use">“Specify geometry” button in Segment Editor</a> and choose volume or ROI node).</p>

---

## Post #3 by @Aitekk (2020-11-17 02:21 UTC)

<p>I tried as you suggested, and it worked well. Thanks much for your help!</p>

---
