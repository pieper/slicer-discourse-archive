# Margin effect altering multiple segments at once

**Topic ID**: 45554
**Date**: 2025-12-19
**URL**: https://discourse.slicer.org/t/margin-effect-altering-multiple-segments-at-once/45554

---

## Post #1 by @parmidajafarian (2025-12-19 12:48 UTC)

<p>Hi everyone,</p>
<p>I’m running into a problem while trying to use the margin effect in the segment editor. My goal is to create a shrunken copy of a Brain segment for CSF segmentation without altering the original Brain segment.</p>
<p>For some reason, the moment <code>effect.self().onApply()</code> is executed, the original Brain segment is altered in a way I don’t expect. Instead of leaving the original segment untouched, it appears to contain only the voxels that were removed from the shrunken segment.</p>
<p>Here’s the relevant code snippet:</p>
<pre><code class="lang-auto"># Create Brain Shrunk Segment as a copy of original Brain
existingIds = set(segmentation.GetSegmentIDs())
segmentation.CopySegmentFromSegmentation(segmentation, segmentId)
newIds = set(segmentation.GetSegmentIDs())
shrunkSegmentId = list(newIds - existingIds)[0]  # The new segment ID
shrunkSegment = segmentation.GetSegment(shrunkSegmentId)
shrunkSegment.SetName(shrunkSegmentName)

# Set up Segment Editor to subtract shrunk Brain from CSF shell
slicer.app.processEvents()
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segNode)

# Shrink Brain Segment
segmentEditorWidget.setActiveEffectByName("Margin")
effect = segmentEditorWidget.activeEffect()
segmentEditorNode.SetSelectedSegmentID(shrunkSegmentId)
effect.setParameter("ApplyToAllVisibleSegments", 0)
effect.setParameter("MarginSizeMm", marginMm)  # Amount to shrink
effect.self().onApply()
</code></pre>
<p>Theoretically, CopySegmentFromSegmentation should create a deep copy, and I don’t experience the same issue later on when applying the logical operators effect on another copy of the Brain Segment. I’ve also verified that the selected segment ID is correctly set before calling the effect.</p>
<p>Any guidance on how to ensure that only the selected segment is affected would be greatly appreciated. Thanks in advance.</p>

---

## Post #2 by @muratmaga (2025-12-19 22:52 UTC)

<aside class="quote no-group" data-username="parmidajafarian" data-post="1" data-topic="45554">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/parmidajafarian/48/81663_2.png" class="avatar"> parmidajafarian:</div>
<blockquote>
<pre><code class="lang-auto">segmentEditorWidget.setActiveEffectByName("Margin")
effect = segmentEditorWidget.activeEffect()
segmentEditorNode.SetSelectedSegmentID(shrunkSegmentId)
effect.setParameter("ApplyToAllVisibleSegments", 0)
effect.setParameter("MarginSizeMm", marginMm)  # Amount to shrink
effect.self().onApply()
</code></pre>
</blockquote>
</aside>
<p>I haven’t done this through scripting, but normally on the Editor,  if you want only modify the existing segment, and you have more than one segment, you need to set the Masking correctly. For example you can set the Modify other segments to “Overwrite visible” and set the visibility of all other segments to hidden.</p>

---

## Post #3 by @mikebind (2025-12-19 23:06 UTC)

<p>Yes, this is your masking settings interfering.  It must be set to Overwrite All or Overwrite Visible, so when the shrunken version is written, it deletes those voxels from the original brain segment, leaving only the original voxels which are not present in the shrunken version.  Below is a code snippet which uses the margin effect and handles masking settings. It isn’t stand-alone, but you can see how masking settings are applied…</p>
<pre><code class="lang-auto">    def grow_segment(
        self,
        segmentID,
        segmentationNode,
        growMarginMm,
        overwriteOtherSegments=False,
        useIntensityMask=False,
    ):
        """Uses Margin segment editor effect to grow given segment by given amount in mm. By default
        this growth does not overwrite any other segments or use the intensity mask settings, but these
        can be overridden by flags.
        """
        segmentEditorWidget, segmentEditorNode, segmentationNode = setup_segment_editor(
            segmentationNode, None
        )
        segmentEditorNode.SetSelectedSegmentID(segmentID)
        segmentEditorWidget.setActiveEffectByName("Margin")
        effect = segmentEditorWidget.activeEffect()
        effect.setParameter(
            "MarginSizeMm", growMarginMm
        )  # negative values would shrink
        # Handle masking
        if overwriteOtherSegments:
            segmentEditorNode.OverwriteMode(segmentEditorNode.OverwriteAll)
            # OverwriteVisible is also an option
        else:
            segmentEditorNode.SetOverwriteMode(
                segmentEditorNode.OverwriteNone
            )  # allow overlap
        segmentEditorNode.SetMasterVolumeIntensityMask(useIntensityMask)
        # segmentEditorNode.setMasterVolumeIntensityMaskRange(minVal, maxVal) # if needed, this is how to set
        # Apply margin growth
        effect.self().onApply()
        # Clean up
        slicer.mrmlScene.RemoveNode(segmentEditorNode)
        return  # no need to return anything, segment is just modified...
```
</code></pre>

---

## Post #4 by @parmidajafarian (2025-12-20 05:58 UTC)

<p>Thank you both so much for the help - that did the trick! Really appreciate it.</p>

---
