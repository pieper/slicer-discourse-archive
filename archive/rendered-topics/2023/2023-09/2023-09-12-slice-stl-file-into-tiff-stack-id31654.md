# Slice STL file into TIFF stack

**Topic ID**: 31654
**Date**: 2023-09-12
**URL**: https://discourse.slicer.org/t/slice-stl-file-into-tiff-stack/31654

---

## Post #1 by @AddamE (2023-09-12 14:01 UTC)

<p>Dear Support Team,</p>
<p>I have followed the support given in <a href="https://discourse.slicer.org/t/convert-stl-file-to-high-resolution-tiff-stack/15949/8">Convert stl file to high resolution tiff stack</a>, however it appears to not be working for my model.</p>
<p>Basically I have a cylindrical part around 4 mm in diameter and 5.3 mm in length. I am trying to slice along the longitudinal axis every 0.4 mm and output this as a tiff slice. The output I am receiving are completely black slices.</p>
<p>Here is my code:</p>
<pre><code class="lang-python">inputModelFile = r"D:\PhD\Interim\Part Models\Stack_A1.stl"
outputDir = r"D:\PhD\Interim\Contour Calibration\Stack_A1"
outputVolumeLabelValue = 255
PixelWidth = 0.125 # mm
planeThicknessMm = 0.40  # mm
outputVolumeMarginMm = [0, 0, 0]

import os
import math
import numpy as np
import sys

try:
    import imageio
except ImportError:
    pip_install("imageio")

imageSpacingMm = [PixelWidth, PixelWidth, planeThicknessMm]

# Load the model
inputModel = slicer.util.loadModel(inputModelFile)
if not inputModel:
    raise ValueError(f"Failed to load the model from {inputModelFile}")

# Get bounds
bounds = np.zeros(6)
inputModel.GetBounds(bounds)

# Compute the image size and origin based on bounds and spacing
imageSize = [int(math.ceil((bounds[axis*2+1] - bounds[axis*2] + 2 * outputVolumeMarginMm[axis]) / imageSpacingMm[axis])) for axis in range(3)]
imageOrigin = [bounds[axis*2] - outputVolumeMarginMm[axis] for axis in range(3)]

# Create an empty image data slice
sliceImageData = vtk.vtkImageData()
sliceImageData.SetDimensions(imageSize[0], imageSize[1], 1)
sliceImageData.AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 1)
sliceImageData.GetPointData().GetScalars().Fill(0)

# Add the slice to the Slicer scene
sliceNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
sliceNode.SetOrigin(imageOrigin)
sliceNode.SetSpacing(imageSpacingMm)
sliceNode.SetAndObserveImageData(sliceImageData)
sliceNode.CreateDefaultDisplayNodes()

# Segment the model
seg = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
seg.SetReferenceImageGeometryParameterFromVolumeNode(sliceNode)
seg.GetSegmentation().SetSourceRepresentationName("Closed surface")
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(inputModel, seg)
segmentId = seg.GetSegmentation().GetNthSegmentID(0)
seg.CreateBinaryLabelmapRepresentation()

# Iterate over the slices to generate the images
for sliceIndex in range(imageSize[2]):
    sliceNode.SetOrigin(imageOrigin[0], imageOrigin[1], imageOrigin[2] + sliceIndex * imageSpacingMm[2])
    seg.SetReferenceImageGeometryParameterFromVolumeNode(sliceNode)
    seg.GetSegmentation().CreateRepresentation('Binary labelmap', True)
    outputSliceImageArray = np.squeeze(slicer.util.arrayFromSegmentBinaryLabelmap(seg, segmentId))
    outputSliceImageArray[outputSliceImageArray &gt; 0] = outputVolumeLabelValue
    filename = os.path.join(outputDir, f'slice_{sliceIndex:03}.tif')
    imageio.imwrite(filename, outputSliceImageArray)
    print(filename)
    slicer.app.processEvents()
</code></pre>
<p>I will try and link the file here:</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1ay9B3mx9YxXGOHK7qoUH0AxwqqaXs5bU/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1ay9B3mx9YxXGOHK7qoUH0AxwqqaXs5bU/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1ay9B3mx9YxXGOHK7qoUH0AxwqqaXs5bU/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1ay9B3mx9YxXGOHK7qoUH0AxwqqaXs5bU/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">Stack_A1.STL</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Any help is extremely appreciated!</p>
<p>Thanks,<br>
Addam</p>

---
