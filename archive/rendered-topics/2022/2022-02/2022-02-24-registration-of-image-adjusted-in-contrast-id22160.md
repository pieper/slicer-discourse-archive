---
topic_id: 22160
title: "Registration Of Image Adjusted In Contrast"
date: 2022-02-24
url: https://discourse.slicer.org/t/22160
---

# Registration of image adjusted in contrast

**Topic ID**: 22160
**Date**: 2022-02-24
**URL**: https://discourse.slicer.org/t/registration-of-image-adjusted-in-contrast/22160

---

## Post #1 by @Engineer90 (2022-02-24 15:39 UTC)

<p>Good morning,<br>
I have to perform an image registration, and I would like to do it after changing the contrast, using “adjust window level …” of the two images i’m using.<br>
However, if I perform registration of the processed images, the intensity information is actually taken from the original images.<br>
Is there a way to force the registration algorithm touse the info of the new processed image?</p>

---

## Post #2 by @mau_igna_06 (2022-02-25 10:20 UTC)

<p>I’m quite sure there must be a way to do that with itk filters. Try to explore the simpleFilters extension</p>

---
