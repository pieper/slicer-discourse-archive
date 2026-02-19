---
topic_id: 15949
title: "Convert Stl File To High Resolution Tiff Stack"
date: 2021-02-11
url: https://discourse.slicer.org/t/15949
---

# Convert STL file to high-resolution TIFF stack

**Topic ID**: 15949
**Date**: 2021-02-11
**URL**: https://discourse.slicer.org/t/convert-stl-file-to-high-resolution-tiff-stack/15949

---

## Post #1 by @FLRonan (2021-02-11 02:42 UTC)

<p>Hello,<br>
I am running a python script to slice an .stl file into a tif stack as per previous forum posts and the script repo.<br>
I have been having issues with certain stl files causing slicer to crash.<br>
Slicer will exit/crash when the script attempts to import the model to a segmentation node.</p>
<p>There are no exit/crash/error warnings and the log file contains nothing after the import line from the script.<br>
The stl i am attempting to slice is just a 200 x 200 x 200 mm cube that has been created in autodesk inventor and converted to an stl, It has got a file size of just 3 kb.</p>
<p>Is there a limit to the model size or complexity of the stl file that slicer can handle?<br>
I have allocated 100Gb of virtual memory as well as having 32Gb of physical memory.<br>
I don’t understand why it is failing, any help would be much appreciated!</p>
<p>Thank you!</p>
<p>The script i am using is as follows:</p>
<blockquote>
<p>import math<br>
import numpy as np<br>
import sys<br>
np.set_printoptions(threshold=sys.maxsize)<br>
inputModelFile = “C:\Users\User\Documents\Slicer\test area.stl”<br>
outputDir = “C:\Users\User\Documents\Slicer\Tiff”<br>
outputVolumeLabelValue = 255<br>
outputVolumeSpacingMm = [0.0635, 0.0635, 0.1] <span class="hashtag-raw">#mm</span> steps/resolution 400dpi =15.748dot/mm =0.0635<br>
outputVolumeMarginMm = [0, 0, 0] <span class="hashtag-raw">#mm</span> of buffer before/after and around</p>
</blockquote>
<h1><a name="p-54456-read-model-1" class="anchor" href="#p-54456-read-model-1" aria-label="Heading link"></a>Read model</h1>
<blockquote>
<p>inputModel = slicer.util.loadModel(inputModelFile)</p>
</blockquote>
<h1><a name="p-54456-determine-output-volume-geometry-and-create-a-corresponding-reference-volume-2" class="anchor" href="#p-54456-determine-output-volume-geometry-and-create-a-corresponding-reference-volume-2" aria-label="Heading link"></a>Determine output volume geometry and create a corresponding reference volume</h1>
<blockquote>
<p>bounds = np.zeros(6)<br>
inputModel.GetBounds(bounds)<br>
imageData = vtk.vtkImageData()<br>
imageSize= [4724,4724,400]<br>
imageOrigin = [ bounds[axis*2]-outputVolumeMarginMm[axis] for axis in range(3) ]<br>
imageData.SetDimensions(imageSize)<br>
imageData.AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 1)<br>
imageData.GetPointData().GetScalars().Fill(0)<br>
referenceVolumeNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLScalarVolumeNode”)<br>
referenceVolumeNode.SetOrigin(imageOrigin)<br>
referenceVolumeNode.SetSpacing(outputVolumeSpacingMm)<br>
referenceVolumeNode.SetAndObserveImageData(imageData)<br>
referenceVolumeNode.CreateDefaultDisplayNodes()</p>
</blockquote>
<h1><a name="p-54456-convert-model-to-labelmap-3d-scalar-volume-node-3" class="anchor" href="#p-54456-convert-model-to-labelmap-3d-scalar-volume-node-3" aria-label="Heading link"></a>Convert model to labelmap ( 3d scalar volume node.)</h1>
<blockquote>
<p>seg = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLSegmentationNode’)<br>
seg.SetReferenceImageGeometryParameterFromVolumeNode(referenceVolumeNode)<br>
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(inputModel, seg)<br>
seg.CreateBinaryLabelmapRepresentation()<br>
outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLLabelMapVolumeNode’)<br>
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg, outputLabelmapVolumeNode, referenceVolumeNode)<br>
outputLabelmapVolumeArray = (slicer.util.arrayFromVolume(outputLabelmapVolumeNode) * outputVolumeLabelValue).astype(‘uint8’) <span class="hashtag-raw">#voxel</span> array as numpy array (‘uint8’)<br>
final=np.invert(outputLabelmapVolumeArray)<br>
finaltest = np.where(final &gt; 100, 0, 1)</p>
</blockquote>
<h1><a name="p-54456-write-labelmap-volume-to-series-of-tiff-files-4" class="anchor" href="#p-54456-write-labelmap-volume-to-series-of-tiff-files-4" aria-label="Heading link"></a>Write labelmap volume to series of TIFF files</h1>
<blockquote>
<p>pip_install(“imageio”)<br>
import imageio<br>
for i in range(len(outputLabelmapVolumeArray)):<br>
imageio.imwrite(f’{outputDir}/image_Page{i:03}_Clr1.tif’, final[i])</p>
</blockquote>
<p>It crashes at the line:<br>
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(inputModel, seg)</p>

---

## Post #2 by @lassoan (2021-02-11 02:57 UTC)

<p>200 x 200 x 200 mm cube at 0.0635x0.0635x0.1 mm/pixel resolution is 40GB. If you want to make sure that you don’t run into memory allocation error then allocate 10x more memory space than the size of your data set is, which in this case is about 400GB.</p>
<p>I would recommend to start small. See if everything works if you work with smaller volumes (larger voxel size) and check everything works well and what your peak memory usage is. Then you can gradually reduce the voxel size to find a good tradeoff between accuracy and memory usage (and computation times).</p>
<p>Can you tell a bit more about your application? What kind of data are you working with and what is your overall goal?</p>

---

## Post #3 by @FLRonan (2021-02-11 03:56 UTC)

<p>Thank you for your response!</p>
<p>This is for a 3d printing application.<br>
I am currently developing a binder jetting printer with a native resolution of 400 dpi.</p>
<p>The tif files that can be interpreted by the printing software i am using need to be in a 1-bit color depth. This is because there is no form of color or intensity modulation per pixel, it is just a binary on or off per pixel. Currently i am converting them to 1-bit after slicing has finished but if that could be included in the process it may significantly decrease the size of the data set?</p>
<p>Could compression or dynamic voxel sizing be possible? Otherwise I can try to reduce resolution by reducing voxel size and then converting back to 400 dpi through interpolation or similar after slicing has completed.</p>

---

## Post #4 by @lassoan (2021-02-11 04:13 UTC)

<p>In this case, you could generate one (or few or a few dozens of slices) at a time. Set the image size to something like [4724, 4724, 10] generate rasterize the model, save it to file, then shift the origin, and repeat.</p>

---

## Post #5 by @FLRonan (2021-02-11 21:19 UTC)

<p>I have attempted this approach but even at [4724, 4724, 1], the application still crashes/quits without any warning, logging or error messages</p>

---

## Post #6 by @lassoan (2021-02-11 21:21 UTC)

<p>Can you describe the exact steps that you did (each click, any scripts that you run)?</p>

---

## Post #7 by @FLRonan (2021-02-11 21:29 UTC)

<p>I only open slicer (version 4.11.20200930 ) and paste the following script into the python interactor window:</p>
<pre><code class="lang-auto">import math
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
inputModelFile = "C:\\\Users\\\User\\\Documents\\\Slicer\\\test area.stl"
outputDir = "C:\\\Users\\\User\\\Documents\\\Slicer\\\Tiff"
outputVolumeLabelValue = 255 #contrast?? 255= white
outputVolumeSpacingMm = [0.0635, 0.0635, 0.1] #mm steps/resolution 400dpi =15.748dot/mm =0.0635 
outputVolumeMarginMm = [0, 0, 0] #mm of buffer before/after and around
inputModel = slicer.util.loadModel(inputModelFile)
bounds = np.zeros(6)
inputModel.GetBounds(bounds)
imageData = vtk.vtkImageData()
imageSize= [4724,4724,1]   
imageOrigin = [ bounds[axis*2]-outputVolumeMarginMm[axis] for axis in range(3) ]
imageData.SetDimensions(imageSize)
imageData.AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 1)
imageData.GetPointData().GetScalars().Fill(0)
referenceVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
referenceVolumeNode.SetOrigin(imageOrigin)
referenceVolumeNode.SetSpacing(outputVolumeSpacingMm)
referenceVolumeNode.SetAndObserveImageData(imageData)
referenceVolumeNode.CreateDefaultDisplayNodes()
seg = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
seg.SetReferenceImageGeometryParameterFromVolumeNode(referenceVolumeNode) 
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(inputModel, seg)
seg.CreateBinaryLabelmapRepresentation()
outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg, outputLabelmapVolumeNode, referenceVolumeNode)
outputLabelmapVolumeArray = (slicer.util.arrayFromVolume(outputLabelmapVolumeNode) * outputVolumeLabelValue).astype('uint8') #voxel array as numpy array ('uint8') 
final=np.invert(outputLabelmapVolumeArray)
finaltest = np.where(final &gt; 100, 0, 1)
pip_install("imageio")
import imageio
for i in range(len(outputLabelmapVolumeArray)):
    imageio.imwrite(f'{outputDir}/image_Page{i:03}_Clr1.tif', final[i])
</code></pre>

---

## Post #8 by @lassoan (2021-02-12 01:27 UTC)

<p>By default, when you import a module, the image extents are increased to include the entire model, essentially undoing the limit that you set on the reference geometry. You can disable this by changing a conversion parameter.</p>
<p>After some cleanup and simplification of the code, here is a complete working version:</p>
<pre data-code-wrap="python"><code class="lang-python">inputModelFile = r"c:\Users\andra\OneDrive\SpinePhantom2Model.stl"
outputDir = r"c:\tmp\20210211-model-rasterization"
outputVolumeLabelValue = 255
inPlaneResolutionDpi = 400
planeThicknessMm = 0.1
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
seg.GetSegmentation().SetSourceRepresentationName("Closed surface")
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(inputModel, seg)
segmentId = seg.GetSegmentation().GetNthSegmentID(0)
seg.CreateBinaryLabelmapRepresentation()

for sliceIndex in range(imageSize[2]):
    sliceNode.SetOrigin(imageOrigin[0], imageOrigin[1], imageOrigin[2] + sliceIndex * imageSpacingMm[2])
    seg.SetReferenceImageGeometryParameterFromVolumeNode(sliceNode)
    seg.GetSegmentation().CreateRepresentation('Binary labelmap', True)  # Force recreating binary labelmap representation immediately
    outputSliceImageArray = np.squeeze(slicer.util.arrayFromSegmentBinaryLabelmap(seg, segmentId)).astype('uint8')
    outputSliceImageArray[outputSliceImageArray&gt;0] = outputVolumeLabelValue
    filename = f'{outputDir}/slice_{sliceIndex:03}.tif'
    result = imageio.imwrite(filename, outputSliceImageArray)
    print(filename)
    slicer.app.processEvents()  # update console
</code></pre>
<p>It takes a while to generate thousands of slices if conversion is done for one slice at a time. Probably you can make it faster if you convert 10-20 frames at a time instead.</p>

---

## Post #9 by @Lars (2022-06-13 10:50 UTC)

<p>Hello Andras,</p>
<p>could you explain a little bit further, what you mean by “converting 10-20 frames a at a time instead”? I have a similar problem as Ronan. For me the slicer crashes at the first slice of the stl model. Even when reducing the resolution tremendously , the slicer still crashes. My stl is 1.4MB.</p>

---

## Post #10 by @lassoan (2022-06-13 12:52 UTC)

<p>What were the <code>imageSize</code> vector values in your case?</p>
<p>Start with lower resolution first to make image generation very fast and with little memory requirement. You can then experiment with what the highest resolution is that your computer can practically handle.</p>

---

## Post #11 by @Lars (2022-06-14 10:49 UTC)

<p>The image size vector is [3523,3804,40].</p>
<p>I tried the resolution of (x,y) = 1,1 and even in this case, the slicer crashes.<br>
I’m using 3D slicer 4.11.20210226.</p>

---

## Post #12 by @muratmaga (2022-06-14 17:48 UTC)

<p>Use crop volume module with x2 scale, create a new low-resolution volume and retry with that.  If it crashes try with x4 scale.</p>

---

## Post #13 by @lassoan (2022-06-15 03:10 UTC)

<p>If you used the code snippet above, then you can lower the output resolution by setting a smaller value in <code>inPlaneResolutionDpi = 400</code> (for example, start with 100). You can then gradually increase it to see what your computer can handle.</p>

---
