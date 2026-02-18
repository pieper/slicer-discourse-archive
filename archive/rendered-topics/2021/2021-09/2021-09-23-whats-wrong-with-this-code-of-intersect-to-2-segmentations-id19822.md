# What's wrong with this code of 'INTERSECT' to 2 segmentations?

**Topic ID**: 19822
**Date**: 2021-09-23
**URL**: https://discourse.slicer.org/t/whats-wrong-with-this-code-of-intersect-to-2-segmentations/19822

---

## Post #1 by @jumbojing (2021-09-23 10:15 UTC)

<p>我想做2个Segmentation的交集…遇到了问题…大神帮帮我</p>
<blockquote>
<p>I want to use python to do the intersection of 2 Segmentations…I have a problem…Help me please</p>
</blockquote>
<pre><code class="lang-auto">seg = slicer.util.getNode("segment")

# Cyl = Logic.p2pCyl(P0,P1,radius=1)
modNode = getNode("Cylinder")
cylSegnode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
cylSegnode.SetName("segCly")
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(
  modNode, cylSegnode
)


# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
# To show segment editor widget (useful for debugging):
# segmentEditorWidget.show()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(cylSegnode)
# segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteNone)
segmentEditorNode.SetMaskMode(slicer.vtkMRMLSegmentEditorNode.PaintAllowedEverywhere)


segmentEditorWidget.setCurrentSegmentID(cylSegnode.GetID())
segmentEditorWidget.setActiveEffectByName("Logical operators")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("Operation", "INTERSECT")
35 &gt;&gt;&gt; effect.setParameter("ModifierSegmentID", seg.GetID())
effect.self().onApply()
</code></pre>
<pre><code class="lang-auto">Line 35:    

File /Applications/Slice98.app/Contents/lib/Slicer-4.13/qt-scripted-modules/SegmentEditorEffects/SegmentEditorLogicalEffect.py, in onApply:
Line 244:   vtkSegmentationCore.vtkOrientedImageDataResample.OPERATION_MINIMUM, selectedSegmentLabelmap.GetExtent())

AttributeError: 'NoneType' object has no attribute 'GetExtent'
</code></pre>
<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #2 by @mikebind (2021-09-23 17:13 UTC)

<p>There might be multiple problems here, but one I see is that in the above code, the two segments you are trying to intersect are not in the same segmentation. You get <code>seg</code> using <code>getNode()</code>, which must not be how you really do it because you cannot get segmentation segments using getNode because they are not MRML nodes. After that, you create a new segmentation node for the cylinder model and make a segment from the model node. Thus the new segmentation node only has the cylinder segment, not any other segments.  Later, you try to use the <code>seg</code> segment, which is not in the <code>cylSegNode</code> segmentation, as a modifier, which will not work, because there is not segment with that ID in the <code>cylSegNode</code>.</p>
<p>I also suspect that you need to set the geometry (grid spacing and orientation) of the cylSeg segmentation somehow before it can be used in a logical intersection (setting a master volume is a typical way to do this).  When you create the a segment from a model, the closed surface representation of that model is definitely created in the segmentation, but you might need to explicitly create the binary labelmap representation (you can see what representations are present by looking at the segmentation in the Segmentations module). Looking at your error message, the ‘selectedSegmentLabelmap’ for your cylinder segment might be ‘None’ because it has not been created yet.</p>

---
