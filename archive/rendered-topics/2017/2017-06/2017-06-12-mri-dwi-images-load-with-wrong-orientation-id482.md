# MRI DWI images load with wrong orientation

**Topic ID**: 482
**Date**: 2017-06-12
**URL**: https://discourse.slicer.org/t/mri-dwi-images-load-with-wrong-orientation/482

---

## Post #1 by @Andrea_Barucci (2017-06-12 14:20 UTC)

<p>Hi,<br>
i want to say thank you for your amazing work with Slicer.<br>
Thank you very much for all your efforts helping researcher around the world with your software.</p>
<p>I have a question for you because i have not been able to find a solution in your forum/tutorials/etc.<br>
I have to analyse a dataset of many patients in order to extract some radiomics features.<br>
Any patient has many images stored in one directory in my computer.<br>
In this directory you can find T2 images, DWI images, etc.<br>
I can load all images with your import but something go wrong when i look at the images.<br>
For T2 images the orientation seems good for almost all the slices less initial and final,<br>
this can be argued because initial an final slides are always cut.</p>
<p>For DWI images this problem becomes worst, images becoming completely cut.<br>
A rectangular planar image becomes just a trapezoid comprising just a little part of the original image.<br>
However if i look at this images with another dicom visualisation all the images appear perfect.</p>
<p>All these problems can be due to the orientation of the acquisition?<br>
I know that in the case of DWI the acquisition volume is not oriented as one of the principal axes XYZ,<br>
but probably has a generic orientation decided by the clinician.</p>
<p>What do you think about this?</p>
<p>Please help me</p>
<p>Thank you very much</p>
<p>Andrea</p>

---

## Post #2 by @lassoan (2017-06-12 14:47 UTC)

<p>Slice viewers in Slicer are by default oriented in anatomical planes. If your volumes are acquired in different plane orientation then click the “Rotate to volume planes” button in the slice viewer controller widget to show them in their acquisition planes.</p>

---
