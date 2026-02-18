# Colour Gradient Based on Pixel Density of Overlaid Segmentations?

**Topic ID**: 20294
**Date**: 2021-10-21
**URL**: https://discourse.slicer.org/t/colour-gradient-based-on-pixel-density-of-overlaid-segmentations/20294

---

## Post #1 by @Greg (2021-10-21 23:52 UTC)

<p>Hello,</p>
<p>I am new to 3D slicer, but I have a series of MRIs which I have overlaid and segmented. I would like to now take those segmentations and apply a filter to visualize their overlap. I have seen this done with two segmentations, but as I have ~40 I would like to use a colour scale to express the relative amount of overlap.</p>
<p>Any suggestions would be appreciated!</p>
<p>Thanks, Greg</p>

---

## Post #2 by @lassoan (2021-10-22 03:53 UTC)

<p>A simple way of dealing with this is to write a short Python script, which does the following:</p>
<ul>
<li>create an “accumulation volume” (segments from all images will be added to it) fill with all zeros, get it as a numpy array (using <code>slicer.util.arrayFromVolume()</code>)</li>
<li>load each segmentation, export the segment to a numpy array (using <code>slicer.util.arrayFromSegmentBinaryLabelmap</code>), you threshold this numpy array (set it to 1 where it has non-zero values), and add the values to the accumulation volume’s numpy array</li>
<li>update the accumulation volume node from its numpy array (using <code>slicer.util.arrayFromVolumeModified()</code>)</li>
</ul>

---

## Post #3 by @Greg (2021-10-24 21:52 UTC)

<p>Hi Andras,</p>
<p>Thank you for your response. Sorry I am still a little confused, I believe I have followed your instructions (although I am very much still learning so the mistake is probably mine), but now I just see a complete overlay of all these segmentations. Is there a way to apply a colour gradient based on the relative overlap?</p>
<p>Thanks, Greg</p>

---

## Post #4 by @lassoan (2021-10-25 11:42 UTC)

<p>Could you copy the otthon script that you created? We could tell you what to add or change to see the result as a scalar volume instead of a binary.</p>

---

## Post #5 by @Greg (2021-10-25 15:37 UTC)

<p>Hi Andras,</p>
<p>I am not terribly familiar with python (so after a few failed attempts) I used the method you mention under: <a href="https://discourse.slicer.org/t/segment-binarylabelmap-to-numpy-array/778">Segment / BinaryLabelMap to numpy array</a>.</p>
<p>Would this work for the problem?</p>

---

## Post #6 by @lassoan (2021-10-25 15:48 UTC)

<p>You need to add the numpy arrays so that if a voxel is set to 1 in multiple segmentations then that voxel value will be larger than 1 (the value should be the number of segmentations where that voxel is non-zero).</p>

---

## Post #7 by @Greg (2021-10-26 02:26 UTC)

<p>Hi Andras,</p>
<p>I think I must be making some mistake, when I try to make an accumulation volume using the code above I get thrown:</p>
<p>File “”, line 1, in <br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 1476, in arrayFromVolume<br>
vimage = volumeNode.GetImageData()<br>
AttributeError: ‘str’ object has no attribute ‘GetImageData’</p>
<p>Greg</p>

---

## Post #8 by @lassoan (2021-10-26 04:05 UTC)

<p><code>arrayFromVolumeNode</code> takes a volume node object as input (not the volume’s name). You can get the volume node object from the volume’s name by calling:</p>
<pre><code>volumeNode = slicer.util.getNode('MyVolumeName')</code></pre>

---

## Post #9 by @Greg (2021-10-26 18:08 UTC)

<p>Hi Andras,</p>
<p>When entering this code I run into the following problem:<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 1324, in getNode<br>
raise MRMLNodeNotFoundException(“could not find nodes in the scene by name or id ‘%s’” % (pattern if (isinstance(pattern, str)) else “”))<br>
slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id ‘the_scene_I_inputted.mrml’.</p>
<p>Sorry for all of these small errors</p>

---

## Post #10 by @lassoan (2021-10-26 23:29 UTC)

<p>Replace <code>MyVolumeName</code> with the actual name of your volume node. It seems that the string that the method got was <code>the_scene_I_inputted.mrml</code> which does not seem like a volume node name.</p>

---

## Post #11 by @Greg (2021-10-26 23:32 UTC)

<aside class="quote no-group" data-username="Greg" data-post="9" data-topic="20294">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/71c47a/48.png" class="avatar"> Greg:</div>
<blockquote>
<p>When entering this code I run into the following problem:<br>
Traceback (most recent call last):<br>
File “”, line 1, in<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 1324, in getNode<br>
raise MRMLNodeNotFoundException(“could not find nodes in the scene by name or id ‘%s’” % (pattern if (isinstance(pattern, str)) else “”))<br>
slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id ‘the_scene_I_inputted.mrml’.</p>
<p>Sorry for all of these small errors</p>
</blockquote>
</aside>
<p>Hi Andras, sorry I should have clarified.</p>
<p>I replaced ‘My Volume Name’ with the volume of the scene I was working with. The ‘the_scene_I_inputted.mrml’ is meant to be the placeholder for the scene that I inputted under ‘My Volume’. Sorry for the confusion.</p>

---

## Post #12 by @ungi (2021-11-14 16:53 UTC)

<p>This code should work. It produces a volume named ExportVolume, which you can use in Volume Rendering to assign colors and opacities to show the density of original segments in each location.</p>
<pre><code class="lang-auto"># Export one volume that shows the sum of segments in a segmentation of the same shape

# Update these names using your scene

segmentationNodeName = '2'
masterVolumeName = '10 ciss3d_tra_iso'
outputVolumeName = 'ExportVolume'

# Prepare nodes that will be needed

segmentationNode = slicer.mrmlScene.GetFirstNodeByName(segmentationNodeName)
segLogic = slicer.modules.segmentations.logic()
segmentation = segmentationNode.GetSegmentation()
labelmapVolume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")

# Make sure the output volume exists, and it has the same shape as the master volume for segmentation

outputVolume = slicer.mrmlScene.GetFirstNodeByName(outputVolumeName)
masterVolume = slicer.mrmlScene.GetFirstNodeByName(masterVolumeName)
if outputVolume is None:
  volumesLogic = slicer.modules.volumes.logic()
  outputVolume = volumesLogic.CloneVolume(slicer.mrmlScene, masterVolume, outputVolumeName)
  outputVolume.CreateDefaultDisplayNodes()

# Prepare output volume array and set voxel values to zero

exportArray = slicer.util.arrayFromVolume(outputVolume)
exportArray[:] = 0

# Add each segment to the output array one-by-one

for i in range(segmentation.GetNumberOfSegments()):
  segmentIds = vtk.vtkStringArray()
  segmentId = segmentation.GetNthSegmentID(i)
  segmentIds.InsertNextValue(segmentId)  
  segLogic.ExportSegmentsToLabelmapNode(segmentationNode, segmentIds, labelmapVolume, masterVolume)
  labelArray = slicer.util.arrayFromVolume(labelmapVolume)
  exportArray = exportArray + labelArray

# Update the output volume

slicer.util.updateVolumeFromArray(outputVolume, exportArray)
</code></pre>

---
