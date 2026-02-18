# Create TIFF stack from an stl file

**Topic ID**: 26650
**Date**: 2022-12-08
**URL**: https://discourse.slicer.org/t/create-tiff-stack-from-an-stl-file/26650

---

## Post #1 by @gcoopermax (2022-12-08 14:13 UTC)

<p>Hello</p>
<p>I want to create a stack of TIFF images from an stl file and have tried the code provided in the post below however I can’t get this to work as I keep getting error “[VTK] No input data”. Can you please help with this?</p>
<aside class="quote quote-modified" data-post="7" data-topic="15949">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/a5b964/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/convert-stl-file-to-high-resolution-tiff-stack/15949/7">Convert STL file to high-resolution TIFF stack</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I only open slicer (version 4.11.20200930 ) and paste the following script into the python interactor window: 
import math
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
inputModelFile = "C:\\\Users\\\User\\\Documents\\\Slicer\\\test area.stl"
outputDir = "C:\\\Users\\\User\\\Documents\\\Slicer\\\Tiff"
outputVolumeLabelValue = 255 #contrast?? 255= white
outputVolumeSpacingMm = [0.0635, 0.0635, 0.1] #mm steps/resolution 400dpi =15.748dot/mm =0.0635 
outputVolumeMarginMm …
  </blockquote>
</aside>

<p>I couldn’t find a way to upload the stl file</p>
<pre><code class="lang-auto">
inputModelFile = r"C:\Work\Temp\Body1.stl"
outputDir = r"C:\Work\Temp\Slicer"
outputVolumeLabelValue = 255
inPlaneResolutionDpi = 200
planeThicknessMm = 1
outputVolumeMarginMm = [0, 0, 0] # mm of buffer before/after and around

import math
import numpy as np
import sys
try:
    import imageio
except ImportError:
    pip_install("imageio")

imageSpacingMm = [25.4/inPlaneResolutionDpi, 25.4/inPlaneResolutionDpi, planeThicknessMm]
inputModel = slicer.util.loadModel(inputModelFile)
bounds = np.zeros(6)
inputModel.GetBounds(bounds)
imageSize = [ int((math.ceil(bounds[axis*2+1] - bounds[axis*2] + 2 * outputVolumeMarginMm[axis]))/imageSpacingMm[axis]) for axis in range(3) ]
imageOrigin = [ bounds[axis*2] - outputVolumeMarginMm[axis] for axis in range(3) ]
sliceImageData = vtk.vtkImageData()
sliceImageData.SetDimensions(imageSize[0], imageSize[1], 1)
sliceImageData.AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 1)
sliceImageData.GetPointData().GetScalars().Fill(0)
sliceNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
sliceNode.SetOrigin(imageOrigin)
sliceNode.SetSpacing(imageSpacingMm)
sliceNode.SetAndObserveImageData(sliceImageData)
sliceNode.CreateDefaultDisplayNodes()
seg = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
seg.SetReferenceImageGeometryParameterFromVolumeNode(sliceNode)
# restrict rasterization to the reference geometry (single frame at a time)
seg.GetSegmentation().SetConversionParameter("Crop to reference image geometry", "1")
seg.GetSegmentation().SetMasterRepresentationName("Closed surface")
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(inputModel, seg)
segmentId = seg.GetSegmentation().GetNthSegmentID(0)
seg.CreateBinaryLabelmapRepresentation()

for sliceIndex in range(imageSize[2]):
    sliceNode.SetOrigin(imageOrigin[0], imageOrigin[1], imageOrigin[2] + sliceIndex * imageSpacingMm[2])
    seg.SetReferenceImageGeometryParameterFromVolumeNode(sliceNode)
    seg.GetSegmentation().CreateRepresentation('Binary labelmap', True)  # Force recreating binary labelmap representation immediately
    outputSliceImageArray = np.squeeze(slicer.util.arrayFromSegmentBinaryLabelmap(seg, segmentId))
    outputSliceImageArray[outputSliceImageArray&gt;0] = outputVolumeLabelValue
    filename = f'{outputDir}/slice_{sliceIndex:03}.tif'
    result = imageio.imwrite(filename, outputSliceImageArray)
    print(filename)
    slicer.app.processEvents()  # update console
</code></pre>

---

## Post #2 by @gcoopermax (2022-12-08 14:20 UTC)

<p>I have attached the file here.</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1ewMUciJCosxstz9XmxrUI7DD4uC-Uxw-/view?usp=share_link">
  <header class="source">

      <a href="https://drive.google.com/file/d/1ewMUciJCosxstz9XmxrUI7DD4uC-Uxw-/view?usp=share_link" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1ewMUciJCosxstz9XmxrUI7DD4uC-Uxw-/view?usp=share_link" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1ewMUciJCosxstz9XmxrUI7DD4uC-Uxw-/view?usp=share_link" target="_blank" rel="noopener nofollow ugc">Body1.stl</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2022-12-08 17:00 UTC)

<p>I’ve tried and the script works well on your data.</p>
<p>You can ignore the <code>[VTK] No input data</code> message, it is just logged when a slice view does not intersect the segmentation node and so there is nothing to show. We’ll suppress this message to not confuse users.</p>

---
