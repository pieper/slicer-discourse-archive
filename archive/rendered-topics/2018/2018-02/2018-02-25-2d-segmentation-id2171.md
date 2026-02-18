# 2D segmentation

**Topic ID**: 2171
**Date**: 2018-02-25
**URL**: https://discourse.slicer.org/t/2d-segmentation/2171

---

## Post #1 by @jruiz (2018-02-25 18:03 UTC)

<p>Hi,</p>
<p>I’ve tried to use the Segment Editor on 2D images. I’m aware it’s designed for 3D volumes, but, anyway, sometimes we have to deal with 2D images and I’m just wondering whether it’s a suitable tool for it. It seems to work properly in 2D with several effects, but at least I haven’t managed to make it work with Level Tracing and GrowCut. Is this right?<br>
I’m running both the stable 4.8.1 version and the nightly 4.9.0 (downloaded yesterday) under Unbuntu 17.10</p>
<p>Thanks, Juan</p>

---

## Post #2 by @cpinter (2018-02-25 18:31 UTC)

<p>Hi Juan,</p>
<p>A workaround can be resampling the volume so that it contains multiple slices. You can do it in Resample Scalar Volume by entering the I and J spacing as is, and some fraction of the K.</p>
<p>I hope this helps!</p>

---

## Post #3 by @jruiz (2018-02-25 21:08 UTC)

<p>Hi Csaba,</p>
<p>yes, it works. Just in case someone else is interested, interpolation should be nearest neighbor to keep the pixel values unchanged, and I’m taking 1/10 the fraction in K since half of the volume will be zeroed, and some effects don’t work in the first slice.</p>
<p>Thanks!</p>

---
