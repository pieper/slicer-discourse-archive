# Segmenting Images of Cells 

**Topic ID**: 15966
**Date**: 2021-02-12
**URL**: https://discourse.slicer.org/t/segmenting-images-of-cells/15966

---

## Post #1 by @Hello (2021-02-12 03:50 UTC)

<p>Operating system:<br>
Slicer version:4.11.200930<br>
Expected behavior: I am trying to create 3D model of a stack of images of cells and the surrounding vasculature. The cells are dyed green and the vascularture is white. I want to use threshold to only highlight the green but it won’t highlight the areas I want. Is there a better way of doing this?<br>
Please help I’m very new to this.</p>
<p>This is one of the images, they’re all very similar<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0267407cf7ce3e901a0a073aabf379cdd8b0e7f.jpeg" alt="image" data-base62-sha1="rpQ3IITWAqAnDuONQqNHy5MTVkr" width="390" height="256"></p>

---

## Post #2 by @pieper (2021-02-12 15:39 UTC)

<p>Is this one slice of a z-stack, or a frame from a time sequence?</p>

---

## Post #3 by @Hello (2021-02-12 15:57 UTC)

<p>It’s a slice from a z stack</p>

---

## Post #4 by @pieper (2021-02-12 16:01 UTC)

<p>If the z spacing is good you can try loading it and then converting to grayscale with Vector to Scalar Volume (or use ImageStacks from SlicerMorph).  Then use the Segment Editor with threshold followed by Identify Islands.  How well it works depends a lot on how distinct your cells are in 3D.  Send more detailed screenshots or sample data if you want specific advice.</p>

---
