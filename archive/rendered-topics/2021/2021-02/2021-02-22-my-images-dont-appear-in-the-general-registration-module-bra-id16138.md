# My images don't appear in the General Registration Module (BRAINS)

**Topic ID**: 16138
**Date**: 2021-02-22
**URL**: https://discourse.slicer.org/t/my-images-dont-appear-in-the-general-registration-module-brains/16138

---

## Post #1 by @kanikayad15 (2021-02-22 16:45 UTC)

<p>Title pretty much explains it all. But I am uploading two tiff files to register and was hoping to utilize the general registration module. When I go to choose fixed and moving image volumes, the options for my loaded files do not appear. I can still view the images in other modules like transform and volume but I’m confused as to why they aren’t loading into this specific module.</p>
<p>Version 4.11.20200930 r29402 / 002be18 on the Mac</p>

---

## Post #2 by @lassoan (2021-02-22 16:50 UTC)

<p>BRAINS (and most other image registration tools) work on grayscale images. You can convert your image to grayscale using “Vector to scalar volume” module. See <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#automatic-image-registration">documentation</a> for some more details.</p>

---
