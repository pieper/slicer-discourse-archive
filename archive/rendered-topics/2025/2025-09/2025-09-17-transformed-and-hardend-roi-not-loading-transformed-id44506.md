# transformed and hardend ROI not loading transformed

**Topic ID**: 44506
**Date**: 2025-09-17
**URL**: https://discourse.slicer.org/t/transformed-and-hardend-roi-not-loading-transformed/44506

---

## Post #1 by @Tamara (2025-09-17 14:00 UTC)

<p>Hello, I want to transform my ROI and slightly rotate it while the full image is loaded in preview mode. Then I want to just load the transformed ROI in full resolution in order to then just work on this part of the image. However, when I load in full resolution the ROI does not load the way I set it but instead just the unrotated ROI is loading. How can I change this? I hardend the ROI but this dindt help.</p>
<p>Kind regards,</p>
<p>Tamara</p>

---

## Post #2 by @pieper (2025-09-17 17:16 UTC)

<p>Are you referring to the ROI used in the ImageStacks?</p>

---

## Post #3 by @Tamara (2025-09-17 19:22 UTC)

<p>yes exactly. I have images from uCT which need to be loaded this way (.bmp images)</p>

---

## Post #4 by @muratmaga (2025-09-17 20:04 UTC)

<p>ImageStacks does not handle rotation during the import. Those should be done in two separate steps.</p>
<p>Import first, and then rotate and crop the imported volume.</p>

---
