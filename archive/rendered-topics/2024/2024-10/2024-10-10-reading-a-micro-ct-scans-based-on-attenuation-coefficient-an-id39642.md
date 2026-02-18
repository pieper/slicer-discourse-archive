# Reading a micro-Ct scans based on attenuation coefficient and knowing the attenuation coeeficient

**Topic ID**: 39642
**Date**: 2024-10-10
**URL**: https://discourse.slicer.org/t/reading-a-micro-ct-scans-based-on-attenuation-coefficient-and-knowing-the-attenuation-coeeficient/39642

---

## Post #1 by @sam5 (2024-10-10 19:22 UTC)

<p>I have a question, I have a series of micro CT scans, based on attenuation coefficient, and want to that and then transfer t to HU</p>

---

## Post #2 by @muratmaga (2024-10-10 20:04 UTC)

<p>There is nothing in Slicer that I know of that would do this. This is usually done at the image reconstruction level using the scanner vendor’s software tools (at least that’s how we do for Bruker Skyscan scanners. During the reconstruction you can choose the output to be in HU after a specific calibration).</p>

---
