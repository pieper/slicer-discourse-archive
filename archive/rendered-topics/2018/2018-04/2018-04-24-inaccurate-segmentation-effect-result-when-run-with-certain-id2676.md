# Inaccurate segmentation effect result when run with certain effects together

**Topic ID**: 2676
**Date**: 2018-04-24
**URL**: https://discourse.slicer.org/t/inaccurate-segmentation-effect-result-when-run-with-certain-effects-together/2676

---

## Post #1 by @EricWilson (2018-04-24 19:21 UTC)

<p>I am attempting to segment out a pelvis bone model from a volume. I have noticed that the model generated from code is not the same as the one created from the GUI using the same parameters. take a look at the image below, the same parameters and effects in the same order were used to obtain both models, but the green section only shows up when applying the effects from the GUI. the rest of the green overlaps the tan.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/716c7be2f9809595b3c06d6c92a592bb1e207aed.jpeg" data-download-href="/uploads/short-url/gbonynZhlbfQsM3r61oaPlyOWXb.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/716c7be2f9809595b3c06d6c92a592bb1e207aed_2_591x500.jpg" alt="image" data-base62-sha1="gbonynZhlbfQsM3r61oaPlyOWXb" width="591" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/716c7be2f9809595b3c06d6c92a592bb1e207aed_2_591x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/716c7be2f9809595b3c06d6c92a592bb1e207aed.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/716c7be2f9809595b3c06d6c92a592bb1e207aed.jpeg 2x" data-dominant-color="9F999F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">610×516 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>through testing, it is apparent that the combination of Threshold &gt; Smoothing (with median, opening, either or both) &gt; Islands remove small islands operations cause this issue. I am wondering if this is because the previous operations are not fully complete when the islands operation begins, and since the voxels are still being placed, some are small enough to be removed by the islands operation. However, using self.delayMs does not appear to affect it in any way so i’m not sure about that.</p>
<p>does anyone know if this is the reason, or how to prevent it?</p>
<p>some more info:<br>
i’m calling my operations like the skin surface example here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
<p>I’ve modified it to be more similar to my calls, i’m going to paste the modified code at the bottom if you want to replicate this.</p>
<p>if you follow the same operations in the gui on the sample data, it is clear that the python script has lost a fair portion of the model, it should look like this image with green being python code and tan being GUI generated:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cd95eb9399fba4ff4bcce827219d2782d0a4021.jpeg" data-download-href="/uploads/short-url/6oKIKCHoExX3OLGxDMHGuqDZU65.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2cd95eb9399fba4ff4bcce827219d2782d0a4021_2_496x500.jpg" alt="image" data-base62-sha1="6oKIKCHoExX3OLGxDMHGuqDZU65" width="496" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2cd95eb9399fba4ff4bcce827219d2782d0a4021_2_496x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cd95eb9399fba4ff4bcce827219d2782d0a4021.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cd95eb9399fba4ff4bcce827219d2782d0a4021.jpeg 2x" data-dominant-color="9597B1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">510×514 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>code:</p>
<pre><code>import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadCTChest()

# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("bone")

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

# Thresholding
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","300")
effect.setParameter("MaximumThreshold","3778")
effect.self().onApply()

# Smoothing
segmentEditorWidget.setActiveEffectByName("Smoothing")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("SmoothingMethod", "MEDIAN")
effect.setParameter("KernelSizeMm", 3)
effect.self().onApply()

# Islands
segmentEditorWidget.setActiveEffectByName("Islands")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("Minimumsize", "1000")
effect.setParameter("EditIslands", "RsEMOVE_SMALL_ISLANDS")
effect.self().onApply()

# Clean up
segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)

# Make segmentation results visible in 3D
segmentationNode.CreateClosedSurfaceRepresentation()

# Make sure surface mesh cells are consistently oriented
surfaceMesh = segmentationNode.GetClosedSurfaceRepresentation(addedSegmentID)
normals = vtk.vtkPolyDataNormals()
normals.AutoOrientNormalsOn()
normals.ConsistencyOn()
normals.SetInputData(surfaceMesh)
normals.Update()
surfaceMesh = normals.GetOutput()
</code></pre>

---

## Post #2 by @lassoan (2018-04-25 01:10 UTC)

<p>This line was incorrect (non-existing parameter name and typo in parameter value):</p>
<pre><code>effect.setParameter("EditIslands", "RsEMOVE_SMALL_ISLANDS")
</code></pre>
<p>Correct command to set operation to remove small islands:</p>
<pre><code>effect.setParameter("Operation", "REMOVE_SMALL_ISLANDS")
</code></pre>
<p>While you are working your script, it is useful to make the segment editor widget visible, so that you can verify that effect parameters are set correctly. Run this command right after creating <code>segmentEditorWidget</code>:</p>
<pre><code>segmentEditorWidget.show()
</code></pre>
<p>You don’t have to worry about operations running in parallel. <code>onApply()</code> does not return until processing is completed.</p>

---

## Post #3 by @EricWilson (2018-04-25 14:50 UTC)

<p>that was indeed the issue. I had found the correct variable name and verified it at one point, but it must have been mixed up with a storage variable name when the code was restructured. thanks</p>

---
