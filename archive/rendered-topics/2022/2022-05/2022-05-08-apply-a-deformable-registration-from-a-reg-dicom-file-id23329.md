# apply a deformable registration from a REG-DICOM file

**Topic ID**: 23329
**Date**: 2022-05-08
**URL**: https://discourse.slicer.org/t/apply-a-deformable-registration-from-a-reg-dicom-file/23329

---

## Post #1 by @ssm (2022-05-08 02:05 UTC)

<p>Hi,<br>
the Transforms module is only capable of creating new volumes from a REG-DICOM import for registration done in Velocity or Eclipse but not for deformable registrations.<br>
Could you help me?</p>

---

## Post #2 by @lassoan (2022-05-08 04:27 UTC)

<p>If you install SlicerRT extension then you can load both DICOM <code>Spatial Registration Object</code> and <code>Deformable Spatial Registration Object</code> IODs. If you have any trouble loading registration objects using latest Slicer Preview Release and SlicerRT then please share a sample data set (preferably phantom data) and we can investigate.</p>

---

## Post #3 by @ssm (2022-05-09 08:45 UTC)

<p>I runned the Transforms module after installing the SlicerRT (slicer version 5.1.0.2022-05-04).<br>
The BRAINS resample Image module was unable to create deformed new volumes, too</p>
<p>How could I upload anonymized files</p>
<p>sebastià</p>

---

## Post #4 by @lassoan (2022-05-09 11:31 UTC)

<p>You can upload files anywhere (dropbox, OneDrive, Google drive, etc) and post the link here. Thank you!</p>

---

## Post #5 by @ssm (2022-05-16 06:30 UTC)

<p>I’ve just uploaded the files to dropbox in order to share them with you<br>
(they</p>
<p><a href="https://www.dropbox.com/scl/fo/wo5x2fg8g4n5vn632a3ty/h?dl=0&amp;rlkey=uv2elizkwnfhqfvw0ortkcrtt" rel="noopener nofollow ugc">https://www.dropbox.com/scl/fo/wo5x2fg8g4n5vn632a3ty/h?dl=0&amp;rlkey=uv2elizkwnfhqfvw0ortkcrtt</a></p>
<p>sebastià</p>

---

## Post #6 by @lassoan (2022-05-29 03:40 UTC)

<p>As far as I can tell, Slicer loads the deformable registration correctly. However, you don’t see any displacement because the displacement vector components are between -0.0505mm and 0.0245mm, which is about 20x smaller than a voxel. So, the displacements in this DICOM SRO deformable transformation information object (REG1.2.246.352.222.400.710025541.11064.1651650814.936.dcm) are practically all zeros. That’s why you don’t see any difference when you apply it to an image.</p>

---
