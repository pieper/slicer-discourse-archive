---
topic_id: 7649
title: "Geometry Of Master And Merge Volumes Do Not Match When Need"
date: 2019-07-18
url: https://discourse.slicer.org/t/7649
---

# Geometry of master and merge volumes do not match when need to edit segmentation mask

**Topic ID**: 7649
**Date**: 2019-07-18
**URL**: https://discourse.slicer.org/t/geometry-of-master-and-merge-volumes-do-not-match-when-need-to-edit-segmentation-mask/7649

---

## Post #1 by @Vivian (2019-07-18 04:34 UTC)

<p>Operating system:  mac OS Mojave<br>
Slicer version: 4.8.1</p>
<p>I loaded MRI dicom files and imported its generated segmentation mask ( nii.gz ) as volume. When I switch the modules to Editor, the following warning message appears several times.<br>
“”"<br>
Warning:: Geometry of master and merge volumes do not match. Transform mismatch<br>
“”"</p>
<p>I have a few set of MRI dicom files with their respective generated segmentation mask (nii.gz). All the segmentation masks were generated in the same way using their reference dicom image. However the above warning only appear for a small portion of them when I switch to Editor module but not for the rest.</p>
<p>I understand from the other post that this problem won’t appear if I use the Segment Editor module and indeed when I switch to Segment Editor modules, the above warning message was not shown. However, after trying the Segment Editor module I notice that I cannot use it to edit my generated mask as shown over the slicer documentation :<br>
"Segment Editor does not edit labelmap volumes, as Editor does. "</p>
<p>I also tried opening dicom files and their mask with ITK-snap. None of them encounter any issue in ITK-snap and the masks overlay on the images correctly.</p>
<p>May I know how should I resolve the above warning and able to edit the imported segmentation mask?</p>
<p>Thanks for your help.</p>

---

## Post #2 by @lassoan (2019-07-18 04:36 UTC)

<p>Please use latest Stable Release (currently 4.10.2) and the Segment Editor. If you need a simple merged labelmap then you can generate in Data module by two clicks (right-click on segmentation node and click “Export visible segments to binary labelmap”).</p>

---
