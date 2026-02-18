# Multivolume vs Scalar Volume

**Topic ID**: 35135
**Date**: 2024-03-27
**URL**: https://discourse.slicer.org/t/multivolume-vs-scalar-volume/35135

---

## Post #1 by @Jacqueline_Banh (2024-03-27 17:23 UTC)

<p>I’m trying to load Dicom images as multivolume but I’m only getting the option for scalar volume under reader. Why is that? How do I get multivolume?</p>

---

## Post #2 by @pieper (2024-03-27 18:35 UTC)

<p>If you go into advanced mode you might be able to select the multivolume option, but it depends on what’s in the header.  The mapping between header tags and mutlivolumes/sequences can have a lot of variants and you may need to look at the code and/or patch the files.</p>

---
