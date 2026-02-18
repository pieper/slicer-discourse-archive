# Trim background in slicer

**Topic ID**: 1119
**Date**: 2017-09-26
**URL**: https://discourse.slicer.org/t/trim-background-in-slicer/1119

---

## Post #1 by @muratmaga (2017-09-26 03:27 UTC)

<p>Hi<br>
convert3d (c3d) tool has this nice feature called trim, which finds the smallest rectangular region of non-background voxels. I use quite a lot with masked images. In Slicer, Crop Volume gives a similar functionality, but in a more manual/visual kind of way. Given c3d is based on ITK, I thought maybe Slicer has a similar option too, but couldn’t find it in Simple Filters. Is this feature available?</p>

---

## Post #2 by @lassoan (2017-09-26 04:13 UTC)

<p>It is really easy to do this, but I guess it hasn’t come up as a feature request, as it is quite rare that images contain large irrelevant background regions that could be removed by simple thresholding. What kind of images do you have?</p>
<p>Anyway, it’s really simple to do, just copy-paste this into the Python console (image is cropped to region with voxel intensity &gt; 0):</p>
<pre><code>volumeNode = getNode('MRHead')
import vtkSegmentationCorePython as seg
img = slicer.modules.segmentations.logic().CreateOrientedImageDataFromVolumeNode(volumeNode)
img.UnRegister(None)
extent=[0,0,0,0,0,0]
seg.vtkOrientedImageDataResample.CalculateEffectiveExtent(img, extent)
croppedImg = seg.vtkOrientedImageData()
seg.vtkOrientedImageDataResample.CopyImage(img, croppedImg, extent) 
slicer.modules.segmentations.logic().CopyOrientedImageDataToVolumeNode(croppedImg, volumeNode)
</code></pre>
<p>If you need to set a custom threshold value for cropping then download Slicer nightly build on Wednesday or later and use this code:</p>
<pre><code>volumeNode = getNode('MRHead')
threshold = 20
import vtkSegmentationCorePython as seg
img = slicer.modules.segmentations.logic().CreateOrientedImageDataFromVolumeNode(volumeNode)
img.UnRegister(None)
extent=[0,0,0,0,0,0]
seg.vtkOrientedImageDataResample.CalculateEffectiveExtent(img, extent, threshold)
croppedImg = seg.vtkOrientedImageData()
seg.vtkOrientedImageDataResample.CopyImage(img, croppedImg, extent) 
slicer.modules.segmentations.logic().CopyOrientedImageDataToVolumeNode(croppedImg, volumeNode)</code></pre>

---

## Post #3 by @muratmaga (2017-09-26 18:37 UTC)

<p>Hi Andras,</p>
<p>It worked great, thank you! Once trimmed, may I ask how to pad images as well? Perhaps, add a buffer of few voxels on each side.</p>
<p>I use this on head microCT of mice. I segment all non-cranial elements (there would be limbs, shoulder blade, mandible etc) and usually left with a volume with 50% (if not more) background voxels.</p>

---

## Post #4 by @lassoan (2017-09-26 18:43 UTC)

<p>To pad images, adjust the extent after calling <code>CalculateEffectiveExtent</code>:</p>
<pre><code>volumeNode = getNode('MRHead')
threshold = 20
margin=5
import vtkSegmentationCorePython as seg
img = slicer.modules.segmentations.logic().CreateOrientedImageDataFromVolumeNode(volumeNode)
img.UnRegister(None)
extent=[0,0,0,0,0,0]
seg.vtkOrientedImageDataResample.CalculateEffectiveExtent(img, extent, threshold)
extent=[extent[0]-margin,extent[1]+margin,extent[2]-margin,extent[3]+margin,extent[4]-margin,extent[5]+margin]
croppedImg = seg.vtkOrientedImageData()
seg.vtkOrientedImageDataResample.CopyImage(img, croppedImg, extent) 
slicer.modules.segmentations.logic().CopyOrientedImageDataToVolumeNode(croppedImg, volumeNode)</code></pre>

---

## Post #5 by @lassoan (2023-03-21 02:50 UTC)

<p>This feature is available in “Split volume” effect (provided by SegmentEditorExtraEffects extension).</p>

---

## Post #6 by @lassoan (2023-03-21 02:50 UTC)



---
