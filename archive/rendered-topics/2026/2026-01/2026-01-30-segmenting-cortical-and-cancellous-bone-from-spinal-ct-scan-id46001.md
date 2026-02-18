# Segmenting cortical and cancellous bone from spinal ct scan

**Topic ID**: 46001
**Date**: 2026-01-30
**URL**: https://discourse.slicer.org/t/segmenting-cortical-and-cancellous-bone-from-spinal-ct-scan/46001

---

## Post #1 by @Jamielynn_Lu (2026-01-30 13:21 UTC)

<p>Hello I am trying to find the best way to differentiate between cancellous and cortical bone in my vertebrae for a FEA. I am having a hard time thresholding to create the different bone textures as my scan isn’t the best quality. Is there another way for me to accomplish this. Should I just segment the whole vertebrae then shrink it using margin and subtract from the original body.</p>

---

## Post #2 by @pieper (2026-01-30 13:42 UTC)

<p>Yes, if you can’t see it well in the image then just shrinking by a realistic amount is probably okay.  FEA simulations are already very approximate so this may not introduce much additional error.</p>

---

## Post #4 by @Jamielynn_Lu (2026-01-30 22:52 UTC)

<p>Thanks so much. Do you have any recommendations for segmenting the IVD? I ended up painting the space inbetween the vertebrae and subtracting the vertebrae from the segment. I’m having issues again, with seperating the NP and AF with this method. Is it enough to cutout the center area of the disc and choosing that to be my NP? Do I need to find a more substantial way to accomplish this.</p>

---

## Post #5 by @pieper (2026-01-31 12:21 UTC)

<p>It’s hard to say - if you don’t see the disc well in your images then you need to create something that seems realistic to you.  However at this point you might be better off just scaling or otherwise adapting a generic joint to the dimensions of the imaged subject.  It’s not clear to me what would be most accurate given the many assumptions involved in any such analysis.</p>

---
