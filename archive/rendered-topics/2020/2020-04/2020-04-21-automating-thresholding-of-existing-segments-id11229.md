# Automating thresholding of existing segments

**Topic ID**: 11229
**Date**: 2020-04-21
**URL**: https://discourse.slicer.org/t/automating-thresholding-of-existing-segments/11229

---

## Post #1 by @Justin (2020-04-21 11:27 UTC)

<p>Dear Andras, all,</p>
<p>Thanks again for helping me with extraction segment cross-sectional area.<br>
I was wondering if you could help me with something else.</p>
<p>As I said earlier, I’m trying to find the cross sectional area of total muscle in a single cross-sectional image on CT.</p>
<p>I can create a segment (for instance “muscle”) and manually/rougly draw or paint the area of interest.<br>
After that, I use the thresholding option to select only the area that has hounsfield units between -29 and + 150. In the “masking” menu I select “Inside muscle”, so that Slicer only “subtracts” the irrelevant area from what I manually delineated. I can then use the segment cross-section area option you provided to calculate the area.</p>
<p>I want to try to use the python scripting to do the thresholding step. I am trying to use the script over here <a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37" rel="nofollow noopener">https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37</a> as a basis but I can’t seem to edit it so that it does what I need. (It will only create new segmentations in the entire scan, but will not change the segmentation that I created)</p>
<p>Can you help me to automate this step?</p>
<p>Thanks so much in advance,<br>
Justin</p>

---

## Post #2 by @lassoan (2020-04-22 03:53 UTC)

<p>If you don’t want to create new segments but update existing ones then instead of using <code>AddEmptySegment</code>, switch to an existing segment by calling <code>setCurrentSegmentID</code> (see complete example <a href="https://gist.github.com/lassoan/2f5071c562108dac8efe277c78f2620f">here</a>).</p>

---

## Post #3 by @Justin (2020-04-28 09:37 UTC)

<p>Dear Andras,</p>
<p>Thanks for your suggestion, I have started working with your suggestion and the example that you show.<br>
Right now I have two “phases”, one creates the three segments that I will be painting by hand.</p>
<p>After painting the segment, the second one applies the thresholding to the existing segments using<br>
setCurrentSegmentID. However it wil then apply the threshold to the entire scan and not just the selected segment. When I manually perform this part i select the “Masking &gt; select editable area &gt; inside <strong>segmentname</strong>” option separately for each segment.<br>
Can you help me with the code that sets the masking settings within each segment?<br>
I’m sure the code I’m using below will contain redundant steps, but at least this way I got it to work…</p>
<p>Best, Justin</p>
<pre><code>## part 1: creating segments
# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# Create temporary segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

# Create segments by thresholding
segmentsFromHounsfieldUnits = [
    ["Pec L", -29, 150],
    ["Pec R", -29, 150],
    ["Back muscle", -29, 150] ]
for segmentName, thresholdMin, thresholdMax in segmentsFromHounsfieldUnits:
    # Create segment
    addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(segmentName)
    segmentEditorNode.SetSelectedSegmentID(addedSegmentID)

# Delete temporary segment editor
segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)

## part 2: auto thresholding the hand-painted segments
# Create temporary segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

# Create segments by thresholding
segmentsFromHounsfieldUnits = [
    ["Pec L", -29, 150],
    ["Pec R", -29, 150],
    ["Back muscle", -29, 150] ]
for segmentName, thresholdMin, thresholdMax in segmentsFromHounsfieldUnits:
    # Fill by thresholding
    segmentEditorWidget.setCurrentSegmentID(addedSegmentID)
    segmentEditorWidget.setActiveEffectByName("Threshold")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MinimumThreshold",str(thresholdMin))
    effect.setParameter("MaximumThreshold",str(thresholdMax))
    effect.self().onApply()

# Delete temporary segment editor
segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c086b5102ba5fbc53a61cb2ffed928408dae1661.png" data-download-href="/uploads/short-url/rtahz9rq91odc2cOKhvGBGz4QuZ.png?dl=1" title="editable area selection" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c086b5102ba5fbc53a61cb2ffed928408dae1661.png" alt="editable area selection" data-base62-sha1="rtahz9rq91odc2cOKhvGBGz4QuZ" width="507" height="499" data-dominant-color="F1F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">editable area selection</span><span class="informations">597×588 25.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Justin (2020-04-29 07:51 UTC)

<p>I have looked up some more information and found that I can use<br>
slicer.vtkMRMLSegmentEditorNode.PaintAllowedInsideSingleSegment</p>
<p>This segment should be defined in SetMaskSegmentID</p>
<p>So I have changed the script to this:</p>
<pre><code># Create temporary segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)
segmentEditorNode.PaintAllowedInsideSingleSegment

# Create segments by thresholding
segmentsFromHounsfieldUnits = [
    ["Pec L", -29, 150],
    ["Pec R", -29, 150],
    ["Back muscle", -29, 150] ]
for segmentName, thresholdMin, thresholdMax in segmentsFromHounsfieldUnits:
    # Fill by thresholding
    segmentEditorWidget.setCurrentSegmentID(addedSegmentID)
    segmentEditorWidget.setActiveEffectByName("Threshold")
    segmentEditorNode.SetMaskSegmentID(addedSegmentID)
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MinimumThreshold",str(thresholdMin))
    effect.setParameter("MaximumThreshold",str(thresholdMax))
    effect.self().onApply()

# Delete temporary segment editor
segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)
</code></pre>
<p>Unfortunately, this still has the same effect in that it still applies the effect on the entire scan. Do you have suggestions?</p>
<p>Justin</p>

---

## Post #5 by @lassoan (2020-04-30 01:59 UTC)

<p><code>segmentEditorNode.PaintAllowedInsideSingleSegment</code> is just a named constant. You can use this constant as an input in <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentEditorNode.html#a451836bc25febd5d1101f0c09ae6a558">SetMaskMode</a> method. If you use this mode then you also need to <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentEditorNode.html#a852187ef0aad1f680280a0c268e01452">set a mask segment ID</a>.</p>

---

## Post #6 by @Justin (2020-04-30 20:02 UTC)

<p>Thanks for your help Andras! I finally got the script working as it should.</p>
<p>Best regards, Justin</p>

---
