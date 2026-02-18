# Newbie: Overlaying .nii file with Dicom

**Topic ID**: 15854
**Date**: 2021-02-05
**URL**: https://discourse.slicer.org/t/newbie-overlaying-nii-file-with-dicom/15854

---

## Post #1 by @jberanoteh (2021-02-05 01:19 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20200930</p>
<p>I have a DICOM file containing 1 CT scan cross-section slice and an .nii / .nii.gz file containing the tagged muscle volume of the specific DICOM file. I would like to overlay the 2 files to see the tagged muscles.</p>
<p>I drag and drop both files in 3D slicer and I get a pop-up that asks me the “description” (volume, segmentation, transform) for each file and gives different import option depending on what I choose.</p>
<p>I import DICOM file as “volume” and the .nii file as “segmentation”. I arrange them in hierarchy so that dicom file is the parent and the .nii file is the child.</p>
<p>I do not see the tag from the .nii/.nii.gz file when I overlay them in the red view. Please advise.</p>

---

## Post #2 by @lassoan (2021-02-05 03:33 UTC)

<p>You have chosen the descriptions correctly (CT → “Volume”, binary labelmap overlay → “Segmentation”). If they are in the same physical position then they appear overlaid - you don’t need to do anything else.</p>
<p>To verify that the two volumes are in the same position, load the files, but this time load both as “Volume”, then go to Volumes module and take a screenshot of the contents of “Volume Information” section for each volume and post them here.</p>

---

## Post #3 by @jberanoteh (2021-02-05 17:25 UTC)

<p>Thank you, Andras.</p>
<p>I already see the difference - but I do not really know why. Any insights?</p>
<p>Here’s the volume for the DICOM:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d79a94519f543dd1c8971d7e88caea9a15af027.png" alt="image" data-base62-sha1="fCsHxkPZ6Eip6XKbLcf9Rvs1MZ9" width="534" height="257"></p>
<p>Volume for the .nii.gz file:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f8af5c5f4c0ff955b29261b076b1d619f1440a8.png" alt="image" data-base62-sha1="blFrk3XUBR3G8U4RNAAJrhwJGyc" width="538" height="260"></p>

---

## Post #4 by @lassoan (2021-02-05 17:53 UTC)

<p>The software that created the segmentation file did not copy the origin, spacing, and axis direction of the input volume. Most likely this segmentation was created in Python and stored as a numpy array (hence the inverted image dimensions KJI instead of IJK) and written to file without setting the image geometry (IJK to physical space mapping) in the nifti file writer. Report the problem to the developer of the segmentation software.</p>
<p>As a workaround, you could create a labelmap volume in the correct physical space and just copy over the voxel data from the imported labelmap volume.</p>

---

## Post #5 by @jberanoteh (2021-02-05 17:56 UTC)

<p>You are correct, Andras. The file was created in Python and stored as numpy.<br>
I will report this issue to the developer.</p>
<p>Thank you for your help. Very much appreciated!</p>

---
