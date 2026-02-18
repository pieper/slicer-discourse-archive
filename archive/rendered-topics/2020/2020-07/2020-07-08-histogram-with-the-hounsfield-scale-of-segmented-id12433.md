# Histogram with the Hounsfield scale of segmented

**Topic ID**: 12433
**Date**: 2020-07-08
**URL**: https://discourse.slicer.org/t/histogram-with-the-hounsfield-scale-of-segmented/12433

---

## Post #1 by @cotozakot (2020-07-08 08:52 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11.0<br>
Expected behavior:<br>
Actual behavior:<br>
I have segmented. As for this manually made segmentation, I can make a histogram with the Housfield scale for each single layer. I saw an example (<a href="https://discourse.slicer.org/t/get-image-intensity-histogram-of-a-segment/11277/2" class="inline-onebox">Get image intensity histogram of a segment</a>) unfortunately I can’t use it in my case.</p>

---

## Post #2 by @lassoan (2020-07-08 13:08 UTC)

<p>If you need histogram to find good threshold value for segmentation: In recent Slicer Preview Releases, you can go to Segment Editor, create a segment, click on Threshold effect, and then click-and-drag on the image to define a region where histogram will be computed on. To view the histogram, open “Local histogram” section.</p>
<p>If you need histogram of a region under a segment then the code snippet you referenced above still works perfectly. If you have any difficulty using it then tell exactly what you do, what you expect to happen, and what happens instead.</p>

---

## Post #3 by @cotozakot (2020-07-08 13:23 UTC)

<p>I don’t know how to change the code so that the output histogram refers to the segmentation that I did manually. in the code, the segmentation is created automatically, I want to change it to my manually made segmentation.</p>
<p>śr., 8 lip 2020, 15:18 użytkownik Andras Lasso via 3D Slicer Community &lt;<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>&gt; napisał:</p>

---

## Post #4 by @lassoan (2020-07-08 13:50 UTC)

<p>To use the script on your own data: replace “Generate input data” section of the code with <code>getNode</code> calls (it gets MRML node from the scene by its name).</p>

---

## Post #5 by @cotozakot (2020-07-08 14:39 UTC)

<p>this is my code, unfortunately it doesn’t work. Could you tell me what’s wrong?</p>
<pre data-code-wrap="python"><code class="lang-python"># Generate input data
################################################

# Load master volume
import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = getVolumeNode ('6: DE DE_CarotidAngio 1.0 D30f B_80kV')()

# Create segmentation
segmentationNode=getNode('Segmentation') ()
slicer.mrmlScene.AddNode(segmentationNode)
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# Create segment
tumorSeed = vtk.vtkSphereSource()
tumorSeed.SetCenter(-6, 30, 28)
tumorSeed.SetRadius(25)
tumorSeed.Update()
segmentationNode.AddSegmentFromClosedSurfaceRepresentation(tumorSeed.GetOutput(), "Segment A", [1.0,0.0,0.0])

# Compute histogram
################################################

labelValue = 1 # label value of first segment
# Get segmentation as labelmap volume node
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, masterVolumeNode)

# Extract all voxels of the segment as numpy array
volumeArray = slicer.util.arrayFromVolume(masterVolumeNode)
labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)
segmentVoxels = volumeArray[labelArray==labelValue]

# Compute histogram
import numpy as np
histogram = np.histogram(segmentVoxels, bins=50)

# Plot histogram
################################################

slicer.util.plot(histogram, xColumnIndex = 1)
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3090c01402573aae98540a4f8311027a44ea0c51.png" alt="image" data-base62-sha1="6VD2LKAHcDLwwQerNNFGOdx0CIx" width="524" height="169"></p>

---

## Post #6 by @lassoan (2020-07-08 16:51 UTC)

<p>Replace “Generate input data” section by this:</p>
<pre><code class="lang-python">masterVolumeNode = getNode ('6: DE*')
segmentationNode = getNode('Segmentation')
</code></pre>
<p>You can choose between segments by setting <code>labelValue</code> to 1, 2, or 3.</p>

---

## Post #7 by @Alice_Durante (2024-01-30 11:24 UTC)

<p>Hello,<br>
I used the same script for my histogram and it works, but i noticed something: if i copy and paste the table of hu value and number of voxel that i get with the script, in my matlab script to calculate the mean of hu, mine mean is different form 3D slicer mean. I tried to do the same thing with excel and nothing change. The difference between matlab and excel mean with 3D slicer mean is like 6 units, but for my study they are important. Can you explain that?</p>
<p>(To calculate the mean I multiplied the single value of column A, with the single value of column B, summed the products and divided by the total number of voxels of the segment considered)</p>

---

## Post #8 by @mikebind (2024-01-30 16:29 UTC)

<p>I would guess this is due to the histogram binning.  The easiest way to find the mean is to just take the average of the list of segment voxel values (e.g. <code>np.mean(segmentVoxels)</code> ).  That will be independent of any binning or table-making, since it is literally the average of the voxel values of the segment.</p>

---
