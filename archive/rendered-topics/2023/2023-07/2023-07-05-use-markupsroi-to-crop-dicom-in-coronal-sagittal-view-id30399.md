# Use MarkupsROI to crop DICOM in coronal / sagittal view

**Topic ID**: 30399
**Date**: 2023-07-05
**URL**: https://discourse.slicer.org/t/use-markupsroi-to-crop-dicom-in-coronal-sagittal-view/30399

---

## Post #1 by @dhanushkannan (2023-07-05 03:28 UTC)

<p>Hi all,<br>
I have used MarkupsROI to crop DICOM images using Python.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4551b195288808ed7950898d25072155ae753191.jpeg" data-download-href="/uploads/short-url/9TdYlCPCELoadX6SDSv7WXqAflv.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4551b195288808ed7950898d25072155ae753191_2_690x360.jpeg" alt="image" data-base62-sha1="9TdYlCPCELoadX6SDSv7WXqAflv" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4551b195288808ed7950898d25072155ae753191_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4551b195288808ed7950898d25072155ae753191_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4551b195288808ed7950898d25072155ae753191_2_1380x720.jpeg 2x" data-dominant-color="473D46"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1702×889 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the following is the code which I have used for cropping based on ROI</p>
<pre><code class="lang-auto">cropVolumeLogic = slicer.modules.cropvolume.logic()
cropVolumeParameterNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLCropVolumeParametersNode")
nodeID = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
cropVolumeParameterNode.SetInputVolumeNodeID(seriesNodeIDs[0])
cropVolumeParameterNode.SetOutputVolumeNodeID(seriesNodeIDs[0])
cropVolumeParameterNode.SetROINodeID(nodeID.GetID())
volumeNode = slicer.util.getNode(seriesNodeIDs[0])
spacing = volumeNode.GetSpacing()
radiusRAS = [(radiusIJK[0]*spacing[0])/2, (radiusIJK[1]*spacing[1])/2, (radiusIJK[2]*spacing[2])/2]
nodeID.SetRadiusXYZ(radiusRAS)
</code></pre>
<p>But the problem is, by default, the cropping or <code>SetRadiusXYZ</code> reflects only in Axial view.<br>
I need the cropping to be reflected in the points in Coronal &amp; Sagittal view.</p>
<p>Pls help me to solve this. Thanks in advance!!</p>

---
