---
topic_id: 34973
title: "Filling Contours In A Volume"
date: 2024-03-19
url: https://discourse.slicer.org/t/34973
---

# Filling Contours In A Volume

**Topic ID**: 34973
**Date**: 2024-03-19
**URL**: https://discourse.slicer.org/t/filling-contours-in-a-volume/34973

---

## Post #1 by @yaraabdelazim (2024-03-19 12:42 UTC)

<p>Hello,</p>
<p>I am currently working on a module that segments based on Edge Detection using SimpleITK filters. The results I’m getting are satisfying, however, I’m only segmenting the contours themselves and not the whole surface delimited by those contours. I’ve tried several SimpleITK filters to be able to fill the contours but with no luck. Does anyone have any tips on how to proceed or what methods to use?</p>
<p>Here is my current segmentation:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0cd79945ecac0567aed96f63528100e1d803b4c.png" alt="image" data-base62-sha1="w4HbfaMTPAcSHPv4o8Uzw6nGCjW" width="606" height="321"></p>
<p>And here is how I would like it to look:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/384f2e7dbbdd3a86001bd70c64ed05a5ffcfe2c9.png" alt="image" data-base62-sha1="828nOGAbKMGdavaVQDzB07y93dv" width="607" height="326"></p>
<p>Here is the code that I use to create that first segmentation:</p>
<pre><code>def draw_contours(self):
    # Get the output of the Canny filter
    inputImage = sitkUtils.PullVolumeFromSlicer(self.outputVolumeNode3)
    
    caster = sitk.CastImageFilter()
    # caster.SetOutputPixelType(sitk.sitkInt8) # Pour le Fillhole Filter
    caster.SetOutputPixelType(sitk.sitkFloat64) # Pour le Threshold Filter
    inputImage = caster.Execute(inputImage)

    # Convert the image to a binary mask
    binaryFilter = sitk.BinaryThresholdImageFilter()
    binaryFilter.SetLowerThreshold(1)  # adjust this value based on your needs
    binaryFilter.SetUpperThreshold(255)  # adjust this value based on your needs
    # binaryFilter = sitk.BinaryFillholeImageFilter()
    # print(binaryFilter.GetForegroundValue())
    # binaryFilter.SetFullyConnected(False)
    print("Lower: ", binaryFilter.GetLowerThreshold())
    print("Upper: ", binaryFilter.GetUpperThreshold())

    binaryImage = binaryFilter.Execute(inputImage)
    
    # Push the binary image to a new Slicer node
    binaryVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode", "BinaryMask")
    sitkUtils.PushVolumeToSlicer(binaryImage, binaryVolumeNode)

    # Create a new segmentation node
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")

    print(type(binaryVolumeNode))
    print(type(segmentationNode))

    # Import the binary mask to the segmentation node
    slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(binaryVolumeNode, segmentationNode)

    # Now you can visualize the segmentation in 3D Slicer
    slicer.util.setSliceViewerLayers(background=self.inputVolumeNode, label=segmentationNode)

    print(binaryVolumeNode.GetImageData().GetDimensions())
</code></pre>
<p>Thank you in advance</p>

---
