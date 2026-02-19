---
topic_id: 8808
title: "Manual Segmentation In A Projection Different From The Mri S"
date: 2019-10-17
url: https://discourse.slicer.org/t/8808
---

# Manual segmentation in a projection different from the MRI scan one

**Topic ID**: 8808
**Date**: 2019-10-17
**URL**: https://discourse.slicer.org/t/manual-segmentation-in-a-projection-different-from-the-mri-scan-one/8808

---

## Post #1 by @gabriella (2019-10-17 03:11 UTC)

<p>Hi,<br>
I am currently using MrView-Mrtrix to analyze MRI-DTI data from a very small animal model.<br>
I am having problems in doing the manual segmentation of the ROIs because in MrView it’s not possible to re-orient the MRI scan into a projection of the brain which is symmetrical for doing the actual segmentation.<br>
I can re-orient the MRI view into a symmetrical projection but then when I click on the image to trace the ROIs and do the segmentation, the view goes back to the asymmetrical view of the brain in which the sample was scanned.<br>
As it’s very hard for our brain samples to be placed in the proper orientation for scanning, I need a software that allows me to do the manual segmentation on a re-oriented projection different from the one obtained during the MRI-DTI scan.<br>
Is it possible to do this with your software?<br>
Would the 3D slicer allow it?<br>
Thanks a lot<br>
Gabriella</p>

---

## Post #2 by @lassoan (2019-10-17 04:41 UTC)

<p>In Slicer’s Segment Editor module you can segment in arbitrarily oriented slice views.</p>
<p>You may also choose to apply a transform to the volume that aligns it to standard orientation (e.g., by using ACPC transform module) and then resample it.</p>

---

## Post #3 by @gabriella (2019-10-17 06:31 UTC)

<p>Hi,<br>
thank you so much for your reply.<br>
So can I open a .nii file created in Mrtrix (with the function mrconvert) with Slicer?<br>
I have tried to open this file with other imaging softwares (MIPAV) but it won’t allow me even though the NIFTI format is supported…<br>
Or should i create a .nii file from all the dicom images just for 3dSlicer?<br>
I am currently reading the documentation, but there isn’t much information on the formats supported and how to pass from one to the other…<br>
Thanks a lot!<br>
Gabriella</p>

---

## Post #4 by @lassoan (2019-10-17 11:29 UTC)

<p>Slicer can read most file formats that are used in medical image computing - DICOM, nifti, nrrd, mha, vtk, etc. See complete list here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/SupportedDataFormat" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/SupportedDataFormat</a></p>

---

## Post #5 by @gabriella (2019-10-23 05:26 UTC)

<p>Hi and thank you so much again for your reply and help.<br>
I managed to open my MRI scan file (.nii) in Slicer and I used the Module “Transform” to rotate the MRI view so that I can have a symmetrical view of all the structures.<br>
To do this - within the “Apply Transform” field - I moved the MRI .nii file from the “Transformable” column on the left into the “Transformed” column on the right .<br>
Then I changed the values in the Module menu “Edit” &gt; “Rotation”. I had to change values for all three axes of rotation to produce a symmetrical view: LR, PA, IS. I then clicked on “Apply” in the “Convert” drop menu section.</p>
<p>Is this the option you suggested in your previous reply? Can I now save the .nii file transformed in this way? Or these are just viewing options?</p>
<p>I have tried to save the .nii file which I thought was now transformed (rotated) but when I try to open it with MRView for example it does not shpw any change.<br>
I also tried to save it in a different way: in the “Convert” menu I put the .nii file as “Reference volume” and in “Output displacement field” I selected "create a new transform as “new name” and then I saved it as a .nii file. However, when I open this file in MRview for example it does not even show the brain scan…it’s a weird file. So what am I missing? What is the proper way of doing it?<br>
I have been going through several of your tutorial videos, including creating labels for manual segmentation but I have found no information on this rotation process yet.<br>
I have watched your tuttorial on transformations (<a href="https://www.screencast.com/t/Z6dQVjK3m" rel="nofollow noopener">https://www.screencast.com/t/Z6dQVjK3m</a>), but I have not quite understood how then you produce a new .nii file with the same MRI scan in a new orientation.</p>
<p>You suggested previously to use the ACPC transform module, but I cannot find this ACPC transform among the optios. Is there any documentation I can read about this?<br>
Resampling means that the software creates a new .nii file as a new “MRI scan” with the transformation applied to it, is that right? How do I resample it in Slicer?</p>
<p>Could you guide me through this process a bit more? Or is there any other tutorial that I could follow?</p>
<p>Thank you a lot for any help you could provide! I would really appreciate some further guidelines or link to more in-depth documentation.<br>
Thanks a lot!<br>
Gabriella</p>

---
