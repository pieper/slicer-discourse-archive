---
topic_id: 20348
title: "Automate Dental Splint Generation Pt 2"
date: 2021-10-26
url: https://discourse.slicer.org/t/20348
---

# Automate Dental Splint Generation Pt. 2

**Topic ID**: 20348
**Date**: 2021-10-26
**URL**: https://discourse.slicer.org/t/automate-dental-splint-generation-pt-2/20348

---

## Post #1 by @Fluvio_Lobo (2021-10-26 00:29 UTC)

<p>Hello,</p>
<p>I am following up on my previous <a href="https://discourse.slicer.org/t/automate-dental-splint-generation-using-markertomodel-module/19980">post</a> hoping to get some advise on the use of <strong>segmentation effects</strong> programmatically.</p>
<p>I am currently running a smoothing operation (gaussian), two subtractions, and an additional smoothing (median). This is the section of my code that calls the effects;</p>
<pre><code class="lang-auto"># Define master volume using the geometries within the segmentation... This is needed for the implementation of any effect!
masterVolumeNode = segNode.GetNodeReference(segNode.GetReferenceImageGeometryReferenceRole()) #----&gt; if there is a failure point, it is here!
# According to the 3D Slicer documentation, this is the most appropriate way of implementing the effects, using the widget calls
segmentEditorWidget                                         = slicer.qMRMLSegmentEditorWidget()
segmentEditorNode                                           = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorWidget.setSegmentationNode(segNode)
inputSegmentIDs                                             = vtk.vtkStringArray()
segNode.GetDisplayNode().GetVisibleSegmentIDs(inputSegmentIDs)
segmentEditorNode.SetOverwriteMode( slicer.vtkMRMLSegmentEditorNode.OverwriteNone )
# Essentially, the index for the segments is given by the order in which the segments were created or imported
# Only visible segments are read, but visibility is set to True by default, so all of the segments will be read
#
# Now we apply the effects on each segment...
# ...Firts, we run a median filter operation on the splint!
splintSegmentID = inputSegmentIDs.GetValue(0)
segmentEditorWidget.setCurrentSegmentID(splintSegmentID)
segmentEditorWidget.setActiveEffectByName("Smoothing")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("SmoothingMethod","GAUSSIAN")
effect.setParameter("KernelSizeMm",str(1.0))
effect.setParameter("ApplyToAllVisibleSegments",str(1))
effect.self().onApply()

# ...After applying the filter, we subtract both the maxilla and the mandible sequentially
maxillaSegmentID = inputSegmentIDs.GetValue(1)
mandibleSegmentID = inputSegmentIDs.GetValue(2)
segmentEditorWidget.setCurrentSegmentID(splintSegmentID)
segmentEditorWidget.setActiveEffectByName("Logical operators")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("Operation", "SUBTRACT")
effect.setParameter("ModifierSegmentID", maxillaSegmentID)
effect.self().onApply()

# ...subtract mandible
segmentEditorWidget.setCurrentSegmentID(splintSegmentID)
segmentEditorWidget.setActiveEffectByName("Logical operators")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("Operation", "SUBTRACT")
effect.setParameter("ModifierSegmentID", mandibleSegmentID)
effect.self().onApply()

# ...finally,  one additional smoothing operation
splintSegmentID = inputSegmentIDs.GetValue(0)
segmentEditorWidget.setCurrentSegmentID(splintSegmentID)
segmentEditorWidget.setActiveEffectByName("Smoothing")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("SmoothingMethod","MEDIAN")
effect.setParameter("KernelSizeMm",str(0.5))
effect.setParameter("ApplyToAllVisibleSegments",str(1))
effect.self().onApply()
</code></pre>
<p>When I run this sequence, the splint segment (green) seems to converge towards the edges of the volume at the front and the sides. If I am not mistaken, this happens when a gaussian or median filter is applied near the end of the master volume. <strong>If this is the case, how do I avoid this?</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32faf52bb9cbbf314ba8e2c03361f84e888c4103.jpeg" data-download-href="/uploads/short-url/7gZxYaGLIZzkkb0aXFjwfZzvgTp.jpeg?dl=1" title="splint_segment" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32faf52bb9cbbf314ba8e2c03361f84e888c4103_2_690x411.jpeg" alt="splint_segment" data-base62-sha1="7gZxYaGLIZzkkb0aXFjwfZzvgTp" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32faf52bb9cbbf314ba8e2c03361f84e888c4103_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32faf52bb9cbbf314ba8e2c03361f84e888c4103_2_1035x616.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32faf52bb9cbbf314ba8e2c03361f84e888c4103.jpeg 2x" data-dominant-color="151B12"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">splint_segment</span><span class="informations">1302×776 70.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-10-26 12:06 UTC)

<p>Kernel-based operations, such as Gaussian smoothing, need voxel values around each voxel’s neiguborhood to be able to compute the output. At the image boundary voxel values need to be invented (either some constant value is assumed or the image is wrapped around or mirrored a the boundary). If you don’t like the result of the automatic boundary extension then add blank voxels around your image before applying Gaussian smoothing. For example, you can use Crop volume to enlarge the image extent before you start the segmentation.</p>

---

## Post #3 by @Fluvio_Lobo (2021-10-26 12:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>What happens when my input is a surface model and not a volume? The only input to my process, not shown in the code above, is an optical scan of the teeth (STLs/OBJs) and a fiducials list. I have no “base” volume to use. Is it possible to generate  a blank volume?</p>

---

## Post #4 by @lassoan (2021-10-26 20:56 UTC)

<p>That should be no problem. You can just create an empty volume as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-a-new-volume">here</a> as use that as reference volume.</p>

---
