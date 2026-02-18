# Creating a sicer module: Overlap RGB arrays

**Topic ID**: 6182
**Date**: 2019-03-18
**URL**: https://discourse.slicer.org/t/creating-a-sicer-module-overlap-rgb-arrays/6182

---

## Post #1 by @laura.gelcano (2019-03-18 04:15 UTC)

<p>Operating system:Windows<br>
Slicer version: 4.8.1</p>
<p>Hi all,<br>
I am creating a module using python.</p>
<p>First, I have an image as inputVolume, which I have converted into an array to know some information such as dimensions:</p>
<p>nodeInput = self.inputSelector.currentNode ()<br>
volume = slicer.util.arrayFromVolume(nodeInput)<br>
numGrids = len(volume)</p>
<p>Second, I created an RGB array, initialized as:</p>
<p>image = np.zeros ([256,256,4], dtype =np.uint8);<br>
GridsImage = [image] * numGrids;</p>
<p>As a result, I have 3 numpy RGB arrays: GridImage [0], GridImage [1] and GridImage [2]. Each array is completed by reading from a .txt file.</p>
<p>Now I want to overlap, the RGB arrays in the input image as the output volume. Any help or sugggestion?</p>
<p>How can I overlap a numpy RGB array into a input volume?</p>
<p>Thanks you in advance</p>

---

## Post #2 by @lassoan (2019-03-18 04:57 UTC)

<p>In slice views, you can overlay two scalar volumes by choosing one of them as foreground and the other as background volume. From Python, you can use <code>slicer.util.setSliceViewerLayers()</code> method to choose volumes and opacity of the overlaid volume.</p>
<p>To create a RGB color volume from a numpy array, use <code>slicer.util.updateVolumeFromArray</code> like this:</p>
<pre><code>volumeNodeRGB = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLVectorVolumeNode")
import numpy as np
voxels = np.random.rand(20,30,40,3)
slicer.util.updateVolumeFromArray(volumeNodeRGB, voxels)
slicer.util.setSliceViewerLayers(background=volumeNodeRGB, fit=True)</code></pre>

---

## Post #3 by @laura.gelcano (2019-03-19 20:42 UTC)

<p>Thanks for answering.</p>
<p>I’m trying other alternatives, since I have problems overlaying both volumes in the correct position.</p>
<p>Also, fit = True argument is not defined in my program version.</p>
<p>I’m trying to create a color image of the arrayRGB and overlay it with the input volume.</p>
<p>I have tried with this:</p>
<p>voxelsRGB = np.zeros ([256, 256, 1, 4], dtype = np.uint8)<br>
nodeOutput = self.outputSelector.currentNode ()<br>
sitkImageOutput = sitk.GetImageFromArray (voxelsRGB)<br>
volumeNode = sitkUtils.PushVolumeToSlicer (sitkImageOutput, None)<br>
slicer.util.setSliceViewerLayers (background = volumeNode)<br>
sitkUtils.PushVolumeToSlicer (sitkImageOutput, outputVolumeNode)<br>
nodeOutput.SetOrigin (nodeInput.GetOrigin ())<br>
nodeOutput.SetSpacing (nodeInput.GetSpacing ())<br>
slicer.util.updateVolumeFromArray (nodeOutput, voxelsRGB)</p>
<p>However, I can’t import stikUtils library.</p>
<p>What I actually want to do is to read a set of coordinates from a text file and paint the corresponding pixel in red, blue or green. The color of the pixel is read from another text file.<br>
Is there any other way to color a specific pixel?</p>
<p>Any help is appreciated</p>

---

## Post #4 by @lassoan (2019-03-19 21:09 UTC)

<aside class="quote no-group" data-username="laura.gelcano" data-post="3" data-topic="6182">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/c77e96/48.png" class="avatar"> laura.gelcano:</div>
<blockquote>
<p>Also, fit = True argument is not defined in my program version.</p>
</blockquote>
</aside>
<p>Please use latest stable version (4.10.1).</p>
<aside class="quote no-group" data-username="laura.gelcano" data-post="3" data-topic="6182">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/c77e96/48.png" class="avatar"> laura.gelcano:</div>
<blockquote>
<p>sitkUtils.PushVolumeToSlicer</p>
</blockquote>
</aside>
<p>This is deprecated. Please use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer.util">slicer.util</a> helper functions instead.</p>
<aside class="quote no-group" data-username="laura.gelcano" data-post="3" data-topic="6182">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/c77e96/48.png" class="avatar"> laura.gelcano:</div>
<blockquote>
<p>What I actually want to do is to read a set of coordinates from a text file and paint the corresponding pixel in red, blue or green.</p>
</blockquote>
</aside>
<p>This sounds terribly inefficient. How many points do you have? Do you really want to color single voxels like this or actually you would like to place a colored markers at each of the listed positions?</p>

---
