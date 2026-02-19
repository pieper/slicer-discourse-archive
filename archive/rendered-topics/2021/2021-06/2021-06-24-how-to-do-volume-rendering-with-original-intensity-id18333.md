---
topic_id: 18333
title: "How To Do Volume Rendering With Original Intensity"
date: 2021-06-24
url: https://discourse.slicer.org/t/18333
---

# How to do volume rendering with original intensity

**Topic ID**: 18333
**Date**: 2021-06-24
**URL**: https://discourse.slicer.org/t/how-to-do-volume-rendering-with-original-intensity/18333

---

## Post #1 by @pranaysingh (2021-06-24 18:51 UTC)

<p>Hi,</p>
<p>I am trying to do volume rendering of my dicom dataset. I am able to successfully view my 3D object but its black in color. While my object, which is actually a tooth is somewhat gray and white in color, which is accurately visible in all three slicer views(coronal, axial and sagittal) with correct intensity, however the 3D rendering of same dicom data has different color which is not the original color of tooth dataset.<br>
Although I am able to visualise the tooth but I wanted it to be rendered along with original intensity values.<br>
There are lot of presets available in volume rendering module but I want it to render the object with exact intensity values of the voxels.</p>
<p>Please help me through it</p>
<p>Thanks,<br>
Pranay</p>

---

## Post #2 by @lassoan (2021-06-24 20:35 UTC)

<p>Yiu can choose the synchronize option in volume rendering module to use the lookup table of slice views as opacity and color transfer functions for volume rendering. However, this usually results in suboptimal 3D appearance. Also, in volume rendering you typically need to apply shading (brightness depending on surface normal and viewing direction), which further modifies the appearance in 3D. You can turn off shading, too, but then you’ll end up very unappealing, flat visualization, without any depth cues.</p>

---

## Post #3 by @pranaysingh (2021-06-29 05:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="18333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>to use the lookup table of slice views as opacity and color transfer functions for volume rendering.</p>
</blockquote>
</aside>
<p>Hi,<br>
Thanks for the reply, where can I find the lookup table for the slice views ?</p>

---

## Post #4 by @lassoan (2021-06-30 01:54 UTC)

<p>You can view/set color table for a volume in Volumes module.</p>

---
