# Extract features using segment generated labelmap

**Topic ID**: 19188
**Date**: 2021-08-13
**URL**: https://discourse.slicer.org/t/extract-features-using-segment-generated-labelmap/19188

---

## Post #1 by @hotsen (2021-08-13 21:35 UTC)

<p>Hi all,</p>
<p>In Slicer, I have segment done on CT images, but registration for CT and MRI is not good (these two are too far away). So I manually transform MRI to align with CT and harden the transform. Then, generate labelmap from the segment, and try to extract features using Radiomics, transformed MRI as input image, labelmap as input region. Not sure this is possible/a proper way in Radiomics, I can get some numbers e.g. min, max, mean… using “Label statistics”, but Radiomics keeps giving me errors:</p>
<p>ValueError: Bounding box of ROI is larger than image space:<br>
ROI bounds (x, y, z image coordinate space) ((146.8418475884187, 83.86141228352409, 7.687500085149379), (227.50923956172693, 159.2217389954305, 22.27083297696697))<br>
Image Size (352, 352, 22)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/384343fe138a92b83a3c1eef78d56248fc9ea502.png" alt="Capture" data-base62-sha1="81IQXClpt7Zrh01Sv0safFDgKbg" width="621" height="360"></p>
<p>I think it might because some small part of segment is out of boundary of MRI (the red circle part)? Any suggestion to make this work without change the segmentation?</p>
<p>Thank you!</p>
<p>Hotsen</p>

---

## Post #3 by @pieper (2021-08-16 17:24 UTC)

<p>You should resample the labelmap to be in the space of the MR.  I believe pyradiomics can do this for you with a flag, but you can also do it in Slicer using, for example, Resample Image (BRAINS).</p>

---

## Post #4 by @hotsen (2021-08-17 19:38 UTC)

<p>Thank you for reply. Could you please specify how to do resample? I have applied resamplePixelSpacing: 2,2,2 in the radiomics settings, is this the resample you refer to? How will resample change the labelmap position to MR? Thank you.</p>

---

## Post #5 by @pieper (2021-08-17 20:02 UTC)

<p>In Slicer’s Resample Image (BRAINS) module you would select the MR as the reference volume and the labelmap as the volume to “warp” even though you aren’t warping it and pick Nearest Neighbor as the method with probably unsigned short as the data type.</p>

---
