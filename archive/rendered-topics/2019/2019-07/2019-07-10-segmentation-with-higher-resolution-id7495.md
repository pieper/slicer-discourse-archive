---
topic_id: 7495
title: "Segmentation With Higher Resolution"
date: 2019-07-10
url: https://discourse.slicer.org/t/7495
---

# Segmentation with higher resolution

**Topic ID**: 7495
**Date**: 2019-07-10
**URL**: https://discourse.slicer.org/t/segmentation-with-higher-resolution/7495

---

## Post #1 by @David_M (2019-07-10 13:42 UTC)

<p>Hi everyone,</p>
<p>I would like to make a segmentation of the eye, with a resolution of 0.1 mm.<br>
For this purpose, I would like to start my segmentation from building spheres from python code.</p>
<p>I tried to start from this code</p>
<pre data-code-wrap="python"><code class="lang-python">import SampleData
# Load master volume
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()
# Create segmentation
segmentationNode = slicer.vtkMRMLSegmentationNode()
slicer.mrmlScene.AddNode(segmentationNode)
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
# Create segment sclera
eye = vtk.vtkSphereSource()
eye.SetCenter(30, 68, -31)
eye.SetRadius(12)
eye.Update()
segmentationNode.AddSegmentFromClosedSurfaceRepresentation(eye.GetOutput(), "1_Sclera", [1.0,1.0,0.0])
</code></pre>
<p>That works, but with a resolution of nearly 1mm.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b334c05fbcff9846a8249f70626e308e78d68681.png" data-download-href="/uploads/short-url/pzkuaQOfc0u7cRkAIdmcJWMbKWl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b334c05fbcff9846a8249f70626e308e78d68681_2_690x346.png" alt="image" data-base62-sha1="pzkuaQOfc0u7cRkAIdmcJWMbKWl" width="690" height="346" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b334c05fbcff9846a8249f70626e308e78d68681_2_690x346.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b334c05fbcff9846a8249f70626e308e78d68681.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b334c05fbcff9846a8249f70626e308e78d68681.png 2x" data-dominant-color="A9AAC5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">766×385 67.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I tried to crop the volume, increasing the resolution (scaling), with success, following <a href="https://discourse.slicer.org/t/segmentation-resolution/1394/5">this</a> instructions. However, now I don’t know how to link the sphere code to the segmentation with this higher resolution.</p>
<p>Unfortunately, I am not good at programming with python, I tried to find help with the vtk library and tutorials, without success.<br>
Thanks in advance for your help</p>

---

## Post #2 by @lassoan (2019-07-25 04:59 UTC)

<p>You did it all right, the only point that was missed that you used the input image resolution as segmentation resolution. The simplest would be to crop&amp;resample the input volume <em>before</em> running your script.</p>
<p>You could <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_new_volume" rel="nofollow noopener">create a new volume</a> with 0.1mm spacing and use that as input of <code>segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode</code> to avoid additional step of manual cropping&amp;resampling, but without cropping you would get quite large segmentation volumes (2000-3000 voxels along each axis if you have an image of the entire head) and you may run out of memory and/or segmentation may become slow.</p>

---

## Post #3 by @David_M (2019-07-25 06:50 UTC)

<p>It worked <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> thanks a lot!</p>

---
