---
topic_id: 11662
title: "Question On Using Mask Volume"
date: 2020-05-22
url: https://discourse.slicer.org/t/11662
---

# Question on using Mask volume

**Topic ID**: 11662
**Date**: 2020-05-22
**URL**: https://discourse.slicer.org/t/question-on-using-mask-volume/11662

---

## Post #1 by @Deepa (2020-05-22 02:56 UTC)

<p>Continuing the discussion from <a href="https://discourse.slicer.org/t/extracting-a-subnetwork-from-3d-volume/11570/4">Extracting a subnetwork from 3D volume</a>:</p>
<p>To retain only green and exclude red from a volume like below<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3154fdfcd338545332d2d16034bb60d9d1d2c6db.png" alt="Untitled" data-base62-sha1="72puqU5Lc9mB0QWfmdqiBGkkKiD" width="265" height="196"></p>
<p>I’m using the Mask volume option.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41914e19c4e44aee03c2ecb31de8e57fbbc15fdb.png" data-download-href="/uploads/short-url/9m2lItfI7pgtpVpLWVkESrkIhzt.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41914e19c4e44aee03c2ecb31de8e57fbbc15fdb_2_299x500.png" alt="Untitled" data-base62-sha1="9m2lItfI7pgtpVpLWVkESrkIhzt" width="299" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41914e19c4e44aee03c2ecb31de8e57fbbc15fdb_2_299x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41914e19c4e44aee03c2ecb31de8e57fbbc15fdb_2_448x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41914e19c4e44aee03c2ecb31de8e57fbbc15fdb.png 2x" data-dominant-color="F2F3F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">571×953 33.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve selected the segment (e.g. segment_3, see below) &gt; Mask Volume and used the default<br>
options provided to create a new volume.</p>
<p>However, I couldn’t see only green in new volume( renamed: 10umvolume)  after I click <code>Apply</code>.</p>
<p>I’m not sure if I should be changing the default options (e.g. Editable area) to display only green in the new volume that will be created after using <code>Mask Volume</code>.</p>
<p>Any suggestions?</p>

---

## Post #2 by @muratmaga (2020-05-22 03:15 UTC)

<p>MaskVOlume just creates a new volume with the masked region only. It doesn’t turn off what’s being displayed on the 3D rendering window, nor automatically switch to masked volume. You will need to do that.</p>
<p>Turn off the visibility of existing segments/segmentations, go to volume rendering, find the masked volume recently created, and hit the eye icon next to it.</p>

---
