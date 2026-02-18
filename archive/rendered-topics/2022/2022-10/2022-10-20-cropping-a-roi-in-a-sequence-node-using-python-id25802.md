# Cropping a ROI in a sequence node using python

**Topic ID**: 25802
**Date**: 2022-10-20
**URL**: https://discourse.slicer.org/t/cropping-a-roi-in-a-sequence-node-using-python/25802

---

## Post #1 by @Karl-Philippe (2022-10-20 08:52 UTC)

<p>Hello,</p>
<p>I am working with large ultrasound tracking sequences (.mha files) and I need to crop the ultrasound signal from the monitor background. I have tried the “Crop volume” extension to crop the image sequence as a volume), but it doesn’t work because I need to keep the tracking information and export the sequence metafile to an .mha file. I also tried to use the “crop volume sequence” module directly but after I select the parameters and start cropping, the sequence takes a long time to process and Slicer crashes. So, how to crop a spatial ROI from a 2D image sequence (“vtkMRMLScalarVolumeNode”) using the 3D Slicer user interface or possibly using Python?</p>
<p>Thank you,</p>

---
