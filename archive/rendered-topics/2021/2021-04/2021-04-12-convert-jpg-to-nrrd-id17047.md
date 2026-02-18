# Convert JPG to nrrd

**Topic ID**: 17047
**Date**: 2021-04-12
**URL**: https://discourse.slicer.org/t/convert-jpg-to-nrrd/17047

---

## Post #1 by @Tonyale1975 (2021-04-12 21:46 UTC)

<p>Dear PyRadiomics / 3DSlicer community,<br>
I imagine that the subject has already been discussed before. But, I couldn’t find the reference.<br>
I need to extract radiomic characteristics from .jpg images, is it possible?<br>
I tried to convert jpg to nrrd via 3DSlicer, and it worked. But when I call the Radiomics module, it only recognizes mask.nrrd (segmentation). Image.nrrd (volume) does not recognize.<br>
Could you please guide me on how to accomplish this task.<br>
Thank you very much.</p>

---

## Post #2 by @muratmaga (2021-04-12 22:06 UTC)

<p>If you open a JPG image and saved it as NRRD in Slicer, most likely it is saved as Vector Volume. I don’t know about pyRadiomics, but some modules work only with scalar volume. Try using Vector to Scalar module to convert your volume to scalar and see if it works.</p>

---

## Post #3 by @Tonyale1975 (2021-04-14 01:15 UTC)

<p>ok, I will try, thanks.</p>

---
