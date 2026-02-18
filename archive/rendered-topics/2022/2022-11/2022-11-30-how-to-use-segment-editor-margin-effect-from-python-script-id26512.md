# How to use Segment Editor Margin Effect from Python script

**Topic ID**: 26512
**Date**: 2022-11-30
**URL**: https://discourse.slicer.org/t/how-to-use-segment-editor-margin-effect-from-python-script/26512

---

## Post #1 by @Caetox (2022-11-30 15:50 UTC)

<p>I am trying to grow segments with the margin effect. I have a segmentation with 5 segments, all segments are supposed to grow by 1mm (with overlap).<br>
This is how I use it in my script:</p>
<pre><code class="lang-auto">        segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
        segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
        segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
        slicer.mrmlScene.AddNode(segmentEditorNode)
        segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)

        segmentEditorWidget.setSegmentationNode(segmentationNode)
        segmentEditorWidget.setMasterVolumeNode(volumeNode)
        segmentEditorWidget.setActiveEffectByName("Margin")
        effect = segmentEditorWidget.activeEffect()
        effect.setParameter("MarginSizeMm", 1.0)
        effect.setParameter("ApplyToAllVisibleSegments", 1)
        segmentEditorNode.SetOverwriteMode(2)
        segmentEditorNode.SetMaskMode(0)
        effect.self().onApply()
</code></pre>
<p>When i run this, the effect is applied only to the first segment in my segmentation, and it is applied 5 times to this segment. Instead I want the effect to be applied once to each segment. It works perfectly if I do this manually in the Segment Editor.<br>
How can I solve this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ef5487e433e4ec8a423475a7b4cd8eac9ea767d.jpeg" data-download-href="/uploads/short-url/4pRQ8oZALiXtZgqcQLvaT6O96TX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ef5487e433e4ec8a423475a7b4cd8eac9ea767d.jpeg" alt="image" data-base62-sha1="4pRQ8oZALiXtZgqcQLvaT6O96TX" width="690" height="491" data-dominant-color="78717D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">754×537 59.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-12-01 02:59 UTC)

<p>Good catch, the issue was due to the effect iterated through effects in the Segment Editor module’s widget and not in your custom widget. I’ve <a href="https://github.com/Slicer/Slicer/commit/b803ad48595c71a6e8768f920dab9f86c18be893">fixed</a> this now, so the Slicer Preview Release that you download tomorrow or later should work well.</p>

---
