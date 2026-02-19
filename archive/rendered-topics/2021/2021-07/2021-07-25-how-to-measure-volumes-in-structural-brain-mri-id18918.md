---
topic_id: 18918
title: "How To Measure Volumes In Structural Brain Mri"
date: 2021-07-25
url: https://discourse.slicer.org/t/18918
---

# How to measure volumes in structural brain MRI?

**Topic ID**: 18918
**Date**: 2021-07-25
**URL**: https://discourse.slicer.org/t/how-to-measure-volumes-in-structural-brain-mri/18918

---

## Post #1 by @aalaa12341 (2021-07-25 14:52 UTC)

<p>How to measure volumes in structural brain MRI? can you tell me step by step how can i measure brain volume in slicer 4.11 from structural mri</p>

---

## Post #2 by @Fluvio_Lobo (2021-07-25 15:25 UTC)

<p><a class="mention" href="/u/aalaa12341">@aalaa12341</a>,</p>
<p>A quick an easy way to do this is to:</p>
<ol>
<li>
<p>Segment the tissue or structure of the brain that you are interested in using the <strong>Segment Editor</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21268ddcba8e1e9d980555c9725e945ff3716e73.jpeg" data-download-href="/uploads/short-url/4JgmdIQ2vOC4T1Frco9QrrAmoO7.jpeg?dl=1" title="segment.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21268ddcba8e1e9d980555c9725e945ff3716e73_2_345x186.jpeg" alt="segment.PNG" data-base62-sha1="4JgmdIQ2vOC4T1Frco9QrrAmoO7" width="345" height="186" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21268ddcba8e1e9d980555c9725e945ff3716e73_2_345x186.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21268ddcba8e1e9d980555c9725e945ff3716e73_2_517x279.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21268ddcba8e1e9d980555c9725e945ff3716e73_2_690x372.jpeg 2x" data-dominant-color="38393A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segment.PNG</span><span class="informations">1920×1040 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Here I created a small segment of part of the ventricular system.<br>
For MRI, I usually use the <strong>threshold</strong> tool to create a <em>mask</em> and the <strong>brush</strong> tool to segment the masked region.</p>
</li>
<li>
<p>Calculate a volume of the tissue or structure by using the <strong>Segment Statistics</strong> module<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4acaf77e6047ec200a37e87c38b1923e692b385.jpeg" data-download-href="/uploads/short-url/s3RyMz1b0KRAh1kXQz8pnsymAfz.jpeg?dl=1" title="volumebrain.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4acaf77e6047ec200a37e87c38b1923e692b385_2_345x186.jpeg" alt="volumebrain.PNG" data-base62-sha1="s3RyMz1b0KRAh1kXQz8pnsymAfz" width="345" height="186" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4acaf77e6047ec200a37e87c38b1923e692b385_2_345x186.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4acaf77e6047ec200a37e87c38b1923e692b385_2_517x279.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4acaf77e6047ec200a37e87c38b1923e692b385_2_690x372.jpeg 2x" data-dominant-color="3C3B3B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volumebrain.PNG</span><span class="informations">1920×1040 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Look are the settings I used on the right, this module is simple, but make sure you are using the volume that corresponds to the segmentation volume, if you have multiple.</p>
</li>
</ol>
<p>Also, I used the MRHead sample dataset available with 3D Slicer for practice!</p>

---
