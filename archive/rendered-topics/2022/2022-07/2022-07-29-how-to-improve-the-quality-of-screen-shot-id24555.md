# How to improve the quality of screen shot

**Topic ID**: 24555
**Date**: 2022-07-29
**URL**: https://discourse.slicer.org/t/how-to-improve-the-quality-of-screen-shot/24555

---

## Post #1 by @1023185654 (2022-07-29 03:26 UTC)

<p>hello,everyone.  I want the screenshot of the 3D window to be sharper, I saw the previous issue that scale factor can be adjusted，is there a Python code for that now ? Now, i used off screen render to set a   high resolution widget then use screen shot but its too slow,Is there any better way for that?</p>

---

## Post #2 by @pieper (2022-07-29 15:25 UTC)

<p>The last time I looked the scale factor option was not working for capturing tiled rendering for the volume renderer.  Offscreen rendering is probably the best bet for now.</p>

---
