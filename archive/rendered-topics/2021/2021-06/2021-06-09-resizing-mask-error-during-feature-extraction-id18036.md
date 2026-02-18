# Resizing Mask - Error during Feature extraction

**Topic ID**: 18036
**Date**: 2021-06-09
**URL**: https://discourse.slicer.org/t/resizing-mask-error-during-feature-extraction/18036

---

## Post #1 by @tduplessis (2021-06-09 12:29 UTC)

<p>Hallo</p>
<p>I am extracting features from 2D x-rays. The segmentation model I used created png masks of 256x256 pixels.  My original x-rays are 1024x1024 pixels. So I have increased the masks with a simple python function, np.repeat(), in both dimensions and converted the array back to png images (with uint8 data type). But when I try to used these masks with the corresponding x-ray (image and mask formats and sizes are the same), I get the following error.</p>
<p>RuntimeError: Exception thrown in SimpleITK LabelStatisticsImageFilter_Execute: d:\a\1\sitk\code\common\include\sitkDualMemberFunctionFactory.hxx:214:<br>
sitk::ERROR: Pixel type: vector of 8-bit unsigned integer is not supported in 2D byclass itk::simple::LabelStatisticsImageFilter</p>
<p>How can I increase a 256x256 mask to 1024x1024 without getting this error?</p>
<p>Thanks for your help!</p>

---
