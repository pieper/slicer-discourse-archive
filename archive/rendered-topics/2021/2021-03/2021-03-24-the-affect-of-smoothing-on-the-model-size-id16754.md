---
topic_id: 16754
title: "The Affect Of Smoothing On The Model Size"
date: 2021-03-24
url: https://discourse.slicer.org/t/16754
---

# The affect of smoothing on the model size

**Topic ID**: 16754
**Date**: 2021-03-24
**URL**: https://discourse.slicer.org/t/the-affect-of-smoothing-on-the-model-size/16754

---

## Post #1 by @YOZ (2021-03-24 23:21 UTC)

<p>Hey guys. You’ve helped a lot so thanks.</p>
<p>I need to segment a bone but I need it to be very accurate in size. However the imaging quality isn’t great and the bone isn’t smooth at all. Should I do smoothing or will it affect the size of the bone? Is there specific smoothing tool I can use and others I can’t?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @pieper (2021-03-25 19:35 UTC)

<p>In general any of the smoothing filters will preserve the size, but if the data is low res then there’s no assurance that this is actually accurate to the bone.  Avoid Gaussian blur, since that will shrink, but I believe windowed sinc should be good.  Of course you can also just look in the Models module to see the volume before and after smoothing.</p>

---
