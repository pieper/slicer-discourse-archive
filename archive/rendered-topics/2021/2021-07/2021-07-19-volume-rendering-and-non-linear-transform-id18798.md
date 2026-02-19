---
topic_id: 18798
title: "Volume Rendering And Non Linear Transform"
date: 2021-07-19
url: https://discourse.slicer.org/t/18798
---

# Volume rendering and non-linear transform

**Topic ID**: 18798
**Date**: 2021-07-19
**URL**: https://discourse.slicer.org/t/volume-rendering-and-non-linear-transform/18798

---

## Post #1 by @riep (2021-07-19 13:03 UTC)

<p>Hi everyone,</p>
<p>We have some interests to make volume rendering of volume bound to a non-linear transform. We know that, for now, Slicer does not handle this case.<br>
Do you know if this feature has been asked in the past? Is there a will to make slicer compatible ? It is in VTK  that the job must be done ?</p>
<p>Thank you for your clarifications,<br>
Pierre</p>

---

## Post #2 by @lassoan (2021-07-19 13:43 UTC)

<p>You need to harden the non-linear transform on the volume if you want to display it using volume rendering. This is not a VTK limitation, we just have not yet implemented automatic resampling in the volume rendering displayable manager. It would be great if you could work on it. It would be very similar to what is implemented in the model displayable manager.</p>

---

## Post #3 by @riep (2021-07-19 15:42 UTC)

<p>Yes, you are right. However, we would like to avoid harden the transform.<br>
Thanks for the hints!<br>
Pierre</p>

---
