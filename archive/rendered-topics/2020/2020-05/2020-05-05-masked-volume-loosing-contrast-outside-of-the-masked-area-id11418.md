---
topic_id: 11418
title: "Masked Volume Loosing Contrast Outside Of The Masked Area"
date: 2020-05-05
url: https://discourse.slicer.org/t/11418
---

# Masked volume loosing contrast outside of the masked area

**Topic ID**: 11418
**Date**: 2020-05-05
**URL**: https://discourse.slicer.org/t/masked-volume-loosing-contrast-outside-of-the-masked-area/11418

---

## Post #1 by @Melodicpinpon (2020-05-05 14:54 UTC)

<p>Hi,</p>
<p>I created a segment that I use to mask my volume, filling inside with -1000, creating a new renamed volume (and affecting all segments in my case).<br>
Unfortunately the result seem to suffer a rise of the overall ‘lightning’ and loses therefore its contrast; everything gets half toned grey with weak contrasted that show that the operation has been done despite of this problem.</p>
<p>I did not achieve to find the source of the error in other posts.</p>

---

## Post #2 by @muratmaga (2020-05-05 15:36 UTC)

<p>So, I don’t think it is actually modifying the outside of the mask, at least not with the version I tried. You can test whether there is a change in intensities outside of the masked area easily by overlaying masked volume and original volume, and hovering over the dataset and check the values in the data probe tab. In my case, they are identical and only place they changed was inside the mask.</p>
<p>What’s the minimum value your original volume? I am guessing it is higher than -1000. With the mask, you are changing the range of intensities, and whatever Slicer is calculating as the ‘proper’ window/level for the new volume is not very good. You can manually adjust this either through the <code>Volumes</code> module or the using the icon below. But the values themselves are not modified.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be2eddeff1dec48877a82bc1e79d4bcc5000af63.png" alt="image" data-base62-sha1="r8r88Tz1oF2vtWQtxkHzuCL73GP" width="62" height="40"></p>

---
