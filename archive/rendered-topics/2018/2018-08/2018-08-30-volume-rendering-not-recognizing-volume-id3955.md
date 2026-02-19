---
topic_id: 3955
title: "Volume Rendering Not Recognizing Volume"
date: 2018-08-30
url: https://discourse.slicer.org/t/3955
---

# Volume Rendering not recognizing volume

**Topic ID**: 3955
**Date**: 2018-08-30
**URL**: https://discourse.slicer.org/t/volume-rendering-not-recognizing-volume/3955

---

## Post #1 by @Nicholas.jacobson (2018-08-30 19:48 UTC)

<p>Hi all,<br>
After importing a DCM file stack, I am taking the usual approach of heading to the volume rendering module. However, this time I am not getting any volumes to appear in the drop down… just rename or delete option appears. Any ideas of why this volume may not be appearing?</p>
<p>nick</p>

---

## Post #2 by @pieper (2018-08-30 20:36 UTC)

<p>The volume rendering combo box will only show scalar volumes so maybe your dicom data imported as a diffusion weighted node or similar.  You can look at the loaded node in the Data module to investigate and/or use the Advanced mode in the DICOM Browser to force using the Scalar Volume option.</p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @Nicholas.jacobson (2018-09-05 04:26 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> this helped. However, today I was given a ct multivolume of a heart. The multivolume works well to get the ‘video’ to play of the beating heart… however, I cannot seem to get a volume rendering of this file. Any advice?</p>
<p>P.S. The Bitmap Generator works well and our images are headed to the machine to print tomorrow… thank you again.</p>

---

## Post #4 by @Nicholas.jacobson (2018-09-05 05:23 UTC)

<p>Ah figured it out… you need to copy the frames to register a volume. However, cropping will not work on this volume in the volume render… any advice?</p>

---

## Post #5 by @cpinter (2018-09-05 12:40 UTC)

<aside class="quote no-group" data-username="Nicholas.jacobson" data-post="4" data-topic="3955">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/ba8739/48.png" class="avatar"> Nicholas.jacobson:</div>
<blockquote>
<p>cropping will not work</p>
</blockquote>
</aside>
<p>Can you please elaborate on this? Thanks</p>

---

## Post #6 by @Nicholas.jacobson (2018-09-05 15:00 UTC)

<p>Funny its working now… I was trying to crop using the volume rending module in the typical fashion and it was not cropping… however I opened it this morning and all it back to normal again.</p>
<p>Sorry for the confusion.</p>

---
