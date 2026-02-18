# Same volume calculated on MRI and CT?

**Topic ID**: 2129
**Date**: 2018-02-20
**URL**: https://discourse.slicer.org/t/same-volume-calculated-on-mri-and-ct/2129

---

## Post #1 by @GioMed (2018-02-20 18:13 UTC)

<p>I was wondering if you can give me an answer to a question I have in my mind.</p>
<p>If I have the same image of the same lesion on CT and on MRI and I use your program to calculate the volume, as you know, the result will be the same or similar if I define the margins with the same technique?</p>

---

## Post #2 by @lassoan (2018-02-20 18:30 UTC)

<p>If you segment the same lesion the same way on both modalities then the volume will be the same. However, it will never be exactly the same, as probably the image resolution is different, you may see the boundaries slightly differently in the two modalities, and the lesion shape and size may change between the two scans.</p>

---
