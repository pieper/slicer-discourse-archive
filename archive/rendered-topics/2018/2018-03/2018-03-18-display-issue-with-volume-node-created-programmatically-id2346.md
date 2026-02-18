# Display Issue with Volume Node Created Programmatically

**Topic ID**: 2346
**Date**: 2018-03-18
**URL**: https://discourse.slicer.org/t/display-issue-with-volume-node-created-programmatically/2346

---

## Post #1 by @zjx1805 (2018-03-18 01:53 UTC)

<p>I am doing vesselness analysis on some dataset that requires performing all the tasks from the python interpreter. The steps so far are:</p>
<ol>
<li>Splitting the 3D data volume into smaller 3D blocks (In the attached python code I used MRHead sample data as an example)</li>
<li>For each of the smaller block I perform some analysis (for the sake of simplicity, I just copied the data in the attached python code)</li>
</ol>
<p>So the resulting volume node (called ‘VesselnessFiltered’) should have exactly the same data array as the sample MRHead node. Indeed I checked numpy.array_equal(array(‘MR*’), array(‘VesselnessFiltered’))<br>
and the return value is True. However, when I load the resulting ‘VesseslnessFiltered’ node into the volume rendering module, I see nothing. So I went to check the volume in the Volume module and I see that the scalar range is 0 to 0 and the histogram also gives nothing. So I assume that it might be because I didn’t properly create a volume node (but I followed <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_new_volume" rel="nofollow noopener">this</a> when creating an empty volume so I am really confused now). Also a side question is whether there is an efficient way to split a larger 3D array into smaller ones programmatically and in a custom way in 3D slicer. The attached py file merely copied the array data from a volume node to another volume node but it took around 40 seconds to run. Any help is much appreciated!</p>
<pre><code>%%%%%%% The Python Code %%%%%%%%
from __future__ import division
import numpy as np
import math
import SampleData

def createEmptyVolume(imageSize, imageSpacing, nodeName):
	# imageSize=[512, 512, 512]
	# imageSpacing=[1.0, 1.0, 1.0]
	voxelType=vtk.VTK_SHORT
	# Create an empty image volume
	imageData=vtk.vtkImageData()
	imageData.SetDimensions(imageSize)
	imageData.AllocateScalars(voxelType, 1)
	thresholder=vtk.vtkImageThreshold()
	thresholder.SetInputData(imageData)
	thresholder.SetInValue(0)
	thresholder.SetOutValue(0)
	# Create volume node
	volumeNode=slicer.vtkMRMLScalarVolumeNode()
	volumeNode.SetSpacing(imageSpacing)
	volumeNode.SetImageDataConnection(thresholder.GetOutputPort())
	volumeNode.SetName(nodeName)
	# Add volume to scene
	slicer.mrmlScene.AddNode(volumeNode)
	displayNode=slicer.vtkMRMLScalarVolumeDisplayNode()
	slicer.mrmlScene.AddNode(displayNode)
	colorNode = slicer.util.getNode('Grey')
	displayNode.SetAndObserveColorNodeID(colorNode.GetID())
	volumeNode.SetAndObserveDisplayNodeID(displayNode.GetID())
	volumeNode.CreateDefaultStorageNode()

def performVesselness(inputNode, cutSpacing, outputNode=None):
	inputImageData = array(inputNode.GetName())
	xDim, yDim, zDim = inputNode.GetImageData().GetDimensions()
	xCutSpacing, yCutSpacing, zCutSpacing = cutSpacing
	xSpacing, ySpacing, zSpacing = inputNode.GetSpacing()
	createEmptyVolume([xDim, yDim, zDim], [xSpacing, ySpacing, zSpacing], 'VesselnessFiltered')
	xNumOfSlices = int(math.ceil(xDim / xCutSpacing))
	yNumOfSlices = int(math.ceil(yDim / yCutSpacing))
	zNumOfSlices = int(math.ceil(zDim / zCutSpacing))
	for ii in range(xNumOfSlices):
		if ii != xNumOfSlices - 1:
			xLocs = range(ii * xCutSpacing , (ii + 1) * xCutSpacing)
		else:
			xLocs = range(ii * xCutSpacing , xDim)

		for jj in range(yNumOfSlices):
			if jj != yNumOfSlices - 1:
				yLocs = range(jj * yCutSpacing , (jj + 1) * yCutSpacing)
			else:
				yLocs = range(jj * yCutSpacing , yDim)

			for kk in range(zNumOfSlices):
				if kk != zNumOfSlices - 1:
					zLocs = range(kk * zCutSpacing , (kk + 1) * zCutSpacing)
				else:
					zLocs = range(kk * zCutSpacing , zDim)

				createEmptyVolume([len(xLocs), len(yLocs), len(zLocs)], [xSpacing, ySpacing, zSpacing], 'tempV')
				array('tempV')[:] = inputImageData[np.ix_(zLocs, yLocs, xLocs)]
				array('VesselnessFiltered')[np.ix_(zLocs, yLocs, xLocs)] = array('tempV')[:]
				slicer.mrmlScene.RemoveNode(getNode('tempV'))

SampleData.SampleDataLogic().downloadMRHead()
performVesselness(getNode('MR*'), [20,20,20])
print np.array_equal(array('MR*'), array('VesselnessFiltered'))</code></pre>

---

## Post #2 by @lassoan (2018-03-18 04:23 UTC)

<p>Creating a node is an expensive operation. You create 1183 volume nodes (and associated display and storage nodes) just to copy some voxels into them and delete them. This increases execution time from about 1 sec to 30sec.</p>
<p>Probably the issue was how you copied/moved value ranges between numpy arrays. As memory of image arrays managed by VTK, if you apply complex range operations, the safest is to make a copy of the numpy array and update the volume with the processed array. Only use <code>getNode</code> and <code>array</code> in testing code, not in actual production code, as looking up nodes by name is not reliable (multiple nodes may have the same name). After cleaning up and simplifying the code a bit, you can get this version that works correctly:</p>
<pre><code>from __future__ import division
import numpy as np
import math
import SampleData

def createEmptyVolume(imageSize, imageSpacing, nodeName):
  voxelType=vtk.VTK_SHORT
  # Create an empty image volume
  imageData=vtk.vtkImageData()
  imageData.SetDimensions(imageSize)
  imageData.AllocateScalars(voxelType, 1)
  thresholder=vtk.vtkImageThreshold()
  thresholder.SetInputData(imageData)
  thresholder.SetInValue(0)
  thresholder.SetOutValue(0)
  thresholder.Update()
  # Create volume node
  volumeNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", nodeName)
  volumeNode.SetSpacing(imageSpacing)
  volumeNode.SetAndObserveImageData(thresholder.GetOutput())
  volumeNode.CreateDefaultDisplayNodes()
  volumeNode.CreateDefaultStorageNode()
  return volumeNode

def performVesselness(inputNode, cutSpacing, createTempVolumes):
  inputImageArray = slicer.util.arrayFromVolume(inputNode)
  dim = inputNode.GetImageData().GetDimensions()
  spacing = inputNode.GetSpacing()
  numOfSlices = [0,0,0]
  for i in range(3):
    numOfSlices[i] = int(math.ceil(dim[i] / cutSpacing[i]))
  print(numOfSlices)
  outputNode = createEmptyVolume(dim, spacing, 'VesselnessFiltered')
  outputImageArray = slicer.util.arrayFromVolume(outputNode).copy()
  for ii in range(numOfSlices[0]):
    xMin = ii * cutSpacing[0]
    xMax = min((ii + 1) * cutSpacing[0], dim[0])
    for jj in range(numOfSlices[1]):
      yMin = jj * cutSpacing[1]
      yMax = min((jj + 1) * cutSpacing[1], dim[1])
      for kk in range(numOfSlices[2]):
        zMin = kk * cutSpacing[2]
        zMax = min((kk + 1) * cutSpacing[2], dim[2])
        tileDim = [xMax-xMin, yMax-yMin, zMax-zMin]
        if createTempVolumes:
          tempVolume = createEmptyVolume(tileDim, spacing, 'tempV')
          tempVolumeArray = slicer.util.arrayFromVolume(tempVolume)
          tempVolumeArray[:] = inputImageArray[zMin:zMax, yMin:yMax, xMin:xMax]
          outputImageArray[zMin:zMax, yMin:yMax, xMin:xMax] = tempVolumeArray
          slicer.mrmlScene.RemoveNode(tempVolume)
        else:
          outputImageArray[zMin:zMax, yMin:yMax, xMin:xMax] = inputImageArray[zMin:zMax, yMin:yMax, xMin:xMax]
  slicer.util.updateVolumeFromArray(outputNode, outputImageArray)
  # Copy origin, spacing, axis directions
  ijkToRAS = vtk.vtkMatrix4x4()
  inputNode.GetIJKToRASMatrix(ijkToRAS)
  outputNode.SetIJKToRASMatrix(ijkToRAS)
  return outputNode

inputVolume = SampleData.SampleDataLogic().downloadMRHead()
outputVolume = performVesselness(inputVolume, [20,20,20], True)  # slow
outputVolume = performVesselness(inputVolume, [20,20,20], False)  # fast
print np.array_equal(array('MR*'), array('VesselnessFiltered'))</code></pre>

---

## Post #3 by @zjx1805 (2018-03-18 07:25 UTC)

<p>Thank you Iassoan! Your code solves my problem perfectly. The reason why I created those dummy nodes is that in my real code I would provide these nodes to an internal function (‘computeVesselnessVolume’) of the Slicer-VMTK plugin, which takes volume node instead of data array as input argument. So in this case I guess I have to use expensive node creation procedure (please let me know if there is another way around). Still, I am a little bit curious why via my version of the code the new volume cannot be displayed as the underlying data array is exactly the same (as indicated by the output of numpy.array_equal). Is there something else in the volume node whose value I didn’t set properly that caused the display to fail? Thanks!</p>

---

## Post #4 by @lassoan (2018-03-18 11:26 UTC)

<p>If you modify voxels using numpy, then when you finished with the changes you need no notify VTK about the changes by calling:</p>
<pre><code>v=getNode('VesselnessFiltered')
v.GetImageData().GetPointData().GetScalars().Modified()
v.Modified()
</code></pre>
<p>To see the same volume, you need to set the same window/level in the display node and copy image origin, spacing, and directions from the original volume.</p>
<p>Speed: you definitely should not create 1183 temporary volume nodes and run VMTK filtering 1183 times. Why would you split the image into so many small pieces and run VMTK on these small pieces instead of the whole volume?</p>

---

## Post #5 by @zjx1805 (2018-03-18 16:29 UTC)

<p>Thank you for your reply! I only copied the data array previously and perhaps that is why the slicer could not display it. As for the speed, performing vmtk filtering on the whole volume would have a tradeoff between losing fine details of the vessel (using stricter filtering parameters) and including non-vessel voxels (using less strict parameters). So I was trying to split the whole volume into smaller ones, apply filtering with strict parameters on each of them, exclude those subvolumes that merely have any vessels and refilter the remaining subvolumes that do have vessels with less strict parameters so that the fine details could be revealed. And yes you are right, my true dataset has a dimension of 640x880x880 and I definitely have to find a better way to do this instead of creating an enormous amount of subvolumes…</p>

---

## Post #6 by @lassoan (2018-03-18 17:15 UTC)

<p>Volume subdivision may indeed decrease the computation time but you have to keep the number of subvolumes small (up to a few ten or so).</p>
<p>You may be able to reduce number of voxels by a factor of 10-100x by cropping to a single rectangular region of interest, using Crop volume module.</p>

---

## Post #7 by @zjx1805 (2018-03-18 19:50 UTC)

<p>Thank you for your advice. This might be a little bit deviated from this post, but am I right in that cropping the volume using crop volume module is not as efficient as directly taking blocks from the numpy array, at least on the programmatic level? Because it is hard to use the mouse to drag the same ROI every time, or even if there is a way to programmatically drag the same ROI every time, then isn’t it the same as directly taking blocks from the numpy array?</p>

---

## Post #8 by @lassoan (2018-03-18 21:10 UTC)

<aside class="quote no-group" data-username="zjx1805" data-post="7" data-topic="2346">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/f08c70/48.png" class="avatar"> zjx1805:</div>
<blockquote>
<p>am I right in that cropping the volume using crop volume module is not as efficient as directly taking blocks from the numpy array</p>
</blockquote>
</aside>
<p>If you just crop without resampling then Crop volume module will not be much slower. What I propose is just to use a single, clinician-defined region of interest. In that case a slight speed difference is negligible. Depending on the shape and size of the vessel of interest, voxel count may be reduced by 10-100x, so you may not need more sophisticated subdivision.</p>

---

## Post #9 by @zjx1805 (2018-03-18 23:14 UTC)

<p>Thank you for all of the help and time! I have selected your previous post as the solution so that others can see it easily.</p>

---

## Post #10 by @Saima (2020-12-14 05:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="2346">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>out the changes by calling:</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
I need the following results after creating new scalar volume. The input array to update the volume is from fuzzy classification.<br>
when I write using nrrd like below I get the required results.<br>
nrrd.write(dir_path+“/brain_ventricle_membership.nrrd”, brain_ventricle_membership, header)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/929ef19bd6da3935f0340b91a6731290b26a68a1.jpeg" data-download-href="/uploads/short-url/kV4fghPcizkqRtMKYBFHsJ28RoZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/929ef19bd6da3935f0340b91a6731290b26a68a1.jpeg" alt="image" data-base62-sha1="kV4fghPcizkqRtMKYBFHsJ28RoZ" width="474" height="500" data-dominant-color="3A3A3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">493×520 44.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>but within a newly created volume I do not get desired results as above.</p>
<p>instead I am getting</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b720993bf61137b87b427cf353d950293fff8fa.png" data-download-href="/uploads/short-url/hC33hjmUvnerXKaszuyZz32nNRo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b720993bf61137b87b427cf353d950293fff8fa.png" alt="image" data-base62-sha1="hC33hjmUvnerXKaszuyZz32nNRo" width="512" height="499" data-dominant-color="959595"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">595×580 652 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The section of code I am using is below:<br>
brain_ventricle_membership = np.zeros(brainImg.shape)<br>
brain_ventricle_membership[brainMask &gt; 0] = u[0]</p>
<p>dim = inputVolume.GetImageData().GetDimensions()<br>
spacing = inputVolume.GetSpacing()<br>
outputNode = self.createEmptyVolume(dim, spacing, ‘newVolume’)<br>
slicer.util.updateVolumeFromArray(outputNode, brain_ventricle_membership)<br>
ijkToRAS = vtk.vtkMatrix4x4()<br>
inputVolume.GetIJKToRASMatrix(ijkToRAS)<br>
outputNode.SetIJKToRASMatrix(ijkToRAS)</p>

---

## Post #11 by @lassoan (2020-12-14 06:20 UTC)

<p>What is this line supposed to do?</p>
<pre><code>brain_ventricle_membership[brainMask &gt; 0] = u[0]
</code></pre>
<p>As far as I can tell, you set all the voxels in the mask to a constant value, which is exactly what you show in the result image. Maybe you meant this:</p>
<pre><code>brain_ventricle_membership[brainMask &lt;= 0] = 0
</code></pre>
<p>You may also need to set appropriate window/level in the display node of the volume so that you can see the gray levels.</p>

---

## Post #12 by @Saima (2020-12-14 06:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="2346">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>0]</code></p>
</blockquote>
</aside>
<p>the line</p>
<pre><code class="lang-auto">brain_ventricle_membership[brainMask &gt; 0] = u[0]
</code></pre>
<p>is assigning some values calculated by fuzzy classification to region where the brain ventricles exists. brainMask is nrrd image with binary values, white where the whole brain exists and black with no brain region its like a mask. How can I assign scalar values to the same region. u[0] contains the membership values from fuzzy classification.</p>
<p>how to set appropriate window levels?</p>

---

## Post #13 by @lassoan (2020-12-14 06:38 UTC)

<p>If you set brain_ventricle_membership the same way for both the first and second example then it should be OK.</p>
<aside class="quote no-group" data-username="Saima" data-post="12" data-topic="2346">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>how to set appropriate window levels?</p>
</blockquote>
</aside>
<p>See example here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_window.2Flevel_.28brightness.2Fcontrast.29_or_colormap_of_a_volume" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---
