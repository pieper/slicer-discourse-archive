# Downstream Effects of Changing SegmentEditorWidget Source Volume

**Topic ID**: 37020
**Date**: 2024-06-25
**URL**: https://discourse.slicer.org/t/downstream-effects-of-changing-segmenteditorwidget-source-volume/37020

---

## Post #1 by @parikhmn (2024-06-25 21:13 UTC)

<p>Hello,</p>
<p>I would love some help understanding the effect changing the source volume has on the <code>SegmentEditorWidget</code>. I recently ran into an issue where, after changing the source volume with <code>setSourceVolumeNode()</code>, the Threshold effect didn’t update its default <code>MaximumThreshold</code> parameter to the maximum voxel intensity of the new volume. I know that I could identify the new maximum intensity and set it programmatically, but I wondered if there was a method by which I could make sure all default parameters similar to <code>MaximumThreshold</code> would update as soon as I changed the source volume. I’ve seen the <code>sourceVolumeNodeChanged()</code> function pop up in a couple places in the documentation, but I don’t really know how that might factor into this.</p>
<p>For context, here’s a bit of my code:</p>
<h4><a name="p-113244-initially-defining-the-segmenteditorwidget-1" class="anchor" href="#p-113244-initially-defining-the-segmenteditorwidget-1" aria-label="Heading link"></a>Initially Defining the SegmentEditorWidget</h4>
<pre><code class="lang-auto">## Define master volume node
masterVolumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")

## Create segmentation
segmentation = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentation.CreateDefaultDisplayNodes()
segmentation.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# Prepare to edit the segment
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
                                                      
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentation)
segmentEditorWidget.setSourceVolumeNode(masterVolumeNode)
</code></pre>
<p>Later, I create a new volume with the exact same features as the <code>masterVolumeNode</code> except that I’ve squared (or otherwise transformed) its voxel intensities.</p>
<h4><a name="p-113244-setting-the-new-source-volume-2" class="anchor" href="#p-113244-setting-the-new-source-volume-2" aria-label="Heading link"></a>Setting the New Source Volume</h4>
<pre><code class="lang-auto">newSourceVolume = slicer.mrmlScene.GetFirstNodeByName(newVolumeName)
segmentEditorWidget.setSourceVolumeNode(newSourceVolume)
</code></pre>
<p>Then, I check the <code>MaximumThreshold</code> parameter:</p>
<h4><a name="p-113244-checking-maximumthreshold-3" class="anchor" href="#p-113244-checking-maximumthreshold-3" aria-label="Heading link"></a>Checking MaximumThreshold</h4>
<pre><code class="lang-auto">segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.parameter("MaximumThreshold")
</code></pre>
<p>But it ends up being the old maximum intensity.</p>
<p>Any help understanding if I could add something after setting the new volume that would cause the <code>MaximumThreshold</code> parameter to update on its own would be very much appreciated.</p>
<p>Thanks!</p>

---
