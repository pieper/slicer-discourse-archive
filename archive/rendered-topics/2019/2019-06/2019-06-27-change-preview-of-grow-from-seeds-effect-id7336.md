---
topic_id: 7336
title: "Change Preview Of Grow From Seeds Effect"
date: 2019-06-27
url: https://discourse.slicer.org/t/7336
---

# Change preview of Grow from seeds effect

**Topic ID**: 7336
**Date**: 2019-06-27
**URL**: https://discourse.slicer.org/t/change-preview-of-grow-from-seeds-effect/7336

---

## Post #1 by @Fernando (2019-06-27 10:02 UTC)

<p>Hi all,</p>
<p>I would like to change the preview of the <code>Grow from seeds</code> effect of the <code>Segment Editor</code> module from the default “fill only” to “outline only”. I dived into the code a bit and I think I need access to the <a href="https://github.com/Slicer/Slicer/blob/2b25e080bce23609710ad87a82030d3fe01c4286/Modules/Loadable/Segmentations/EditorEffects/Python/AbstractScriptedSegmentEditorAutoCompleteEffect.py#L239" rel="nofollow noopener"><code>previewNode</code></a> of the effect. Where can I find the instance of <a href="https://github.com/Slicer/Slicer/blob/bf5285be34b88a2612459fadb6715f7c57a196d4/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorGrowFromSeedsEffect.py#L6" rel="nofollow noopener"><code>SegmentEditorGrowFromSeedsEffect</code></a> from Python?</p>

---

## Post #2 by @Fernando (2019-06-27 10:20 UTC)

<p>Never mind, I think I found it:</p>
<pre><code class="lang-python">e = segmentEditorWidget.activeEffect()
ps = e.parameterSetNode()
previewNode = ps.GetNodeReference("SegmentationResultPreview")
</code></pre>

---
