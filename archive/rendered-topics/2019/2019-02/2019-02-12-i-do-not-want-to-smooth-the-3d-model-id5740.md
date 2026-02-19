---
topic_id: 5740
title: "I Do Not Want To Smooth The 3D Model"
date: 2019-02-12
url: https://discourse.slicer.org/t/5740
---

# I do not want to smooth the 3D model

**Topic ID**: 5740
**Date**: 2019-02-12
**URL**: https://discourse.slicer.org/t/i-do-not-want-to-smooth-the-3d-model/5740

---

## Post #1 by @Kazu (2019-02-12 12:12 UTC)

<p>Hello,</p>
<p>The 3D model becomes smooth by default.<br>
I want to display the change of the 3D model due to the slice thickness, so when it is a thick slice it has to be in staircase shape, but it will be displayed smoothly.<br>
When extracting it is stepwise and rough.</p>
<p>How can we set roughness by setting it?</p>
<p>Slicer version: slicer4.8.1</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bb608b08efeb05eaf4ba6abe021ec8bc7c72425.jpeg" data-download-href="/uploads/short-url/jVWncSFQgiJUjszyoJrS5kZPjZr.jpeg?dl=1" title="sphere" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bb608b08efeb05eaf4ba6abe021ec8bc7c72425_2_690x456.jpeg" alt="sphere" data-base62-sha1="jVWncSFQgiJUjszyoJrS5kZPjZr" width="690" height="456" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bb608b08efeb05eaf4ba6abe021ec8bc7c72425_2_690x456.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bb608b08efeb05eaf4ba6abe021ec8bc7c72425_2_1035x684.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bb608b08efeb05eaf4ba6abe021ec8bc7c72425_2_1380x912.jpeg 2x" data-dominant-color="3C4045"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sphere</span><span class="informations">1820×1204 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2019-02-12 19:25 UTC)

<p>Please download and install 4.10.1, a huge amount of development went into Segment Editor since 4.8.1.</p>
<p>In that new version, you can disable smoothing with this control:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/4154f6fb495d8ffa59568fde6080050bc0597fa9.png" alt="image" data-base62-sha1="9jX4rRcueNjlSDJ3UUvxuCZiDeF" width="690" height="228"></p>
<p>(Related topic: <a href="https://discourse.slicer.org/t/option-to-disable-smoothing-of-the-segment-surfaces-in-segment-editor/883/16" class="inline-onebox">Option to disable smoothing of the segment surfaces in Segment Editor - #16 by lassoan</a>)</p>

---
