# [Slicer] Wrong threshold when opening NifTi file

**Topic ID**: 198
**Date**: 2017-04-26
**URL**: https://discourse.slicer.org/t/slicer-wrong-threshold-when-opening-nifti-file/198

---

## Post #1 by @Guido_Buezas (2017-04-26 18:56 UTC)

<p>Hi everyone</p>
<p>I made a NifTi file from a stack of Tiff slices (8-bit gray scale) in ImageJ. After i save the .nii file, i check it in ImageJ and it’s OK.</p>
<p>When i load .nii file into Slicer, the threshold levels are wrong, with a narrower interval than the original files, so a big number of gray pixels cant be seen. This problem is only with Slicer, with ImageJ i can see it as the original Tiff files. Is it normal? What should i do?</p>
<p>Best regards</p>
<p>Guido</p>

---

## Post #2 by @lassoan (2017-04-26 19:32 UTC)

<p>Left-click and drag up/down, left/right in image slice viewers to adjust the default brightness/contrast.</p>
<p>If you work with volumetric images then use a file format that can store image slice spacing. For example, you can use NIFTI (ImageJ: File / Save as / Analyze 7.5).</p>

---

## Post #3 by @Guido_Buezas (2017-04-28 14:44 UTC)

<p>Well, that was a silly question. Anyway, i tried directly with threshold effect and (as i remember) the lower limit was at the lowest level possible. So, i thougth it can’t be lowered anymore. Additionally, i tried actions with the mouse but is evident that i didn’t use left-click + drag.</p>
<p>Thank you very much!!</p>

---
