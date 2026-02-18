# Howto get imageDirections from a ROI?

**Topic ID**: 25713
**Date**: 2022-10-15
**URL**: https://discourse.slicer.org/t/howto-get-imagedirections-from-a-roi/25713

---

## Post #1 by @jumbojing (2022-10-15 01:56 UTC)

<p>I want to create a volume from a ROI:</p>
<pre><code class="lang-python">nodeName = "MyNewVolume"
imageSize = list(map(int, dim))  # the size of the ROI
voxelType=vtk.VTK_UNSIGNED_CHAR
imageOrigin = cn[0] # the origin of the ROI
imageSpacing = [1.0, 1.0, 1.0]
imageDirections = drts # the drts is directs of the ROI
fillVoxelValue = 0

# Create an empty image volume, filled with fillVoxelValue
imageData = vtk.vtkImageData()
imageData.SetDimensions(imageSize)
imageData.AllocateScalars(voxelType, 1)
imageData.GetPointData().GetScalars().Fill(fillVoxelValue)
# Create volume node
volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", nodeName)
volumeNode.SetOrigin(imageOrigin)
volumeNode.SetSpacing(imageSpacing)
volumeNode.SetIJKToRASDirections(imageDirections)
volumeNode.SetAndObserveImageData(imageData)
volumeNode.CreateDefaultDisplayNodes()
volumeNode.CreateDefaultStorageNode()
</code></pre>
<p>but I got <img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji" alt=":point_down:" loading="lazy" width="20" height="20">:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab59a7ba06a43182c19647444bc36c7920f79a8d.png" data-download-href="/uploads/short-url/orPJqQ7xmvPs8U9n3N9pT5AQuMR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab59a7ba06a43182c19647444bc36c7920f79a8d.png" alt="image" data-base62-sha1="orPJqQ7xmvPs8U9n3N9pT5AQuMR" width="454" height="500" data-dominant-color="7D91C3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">760×836 9.22 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I guess it’s because of the problem of ‘imageDirections’, so–<br>
Howto get imageDirections from a ROI?</p>

---

## Post #2 by @lassoan (2022-10-16 05:11 UTC)

<p>You can get the image axis directions from the top-left 3x3 submatrix of the <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsROINode.html#a540216cdf23db6e5766b84238e638996">ObjectToWorldMatrix</a>.</p>

---
