# How to remove some segment editor effects

**Topic ID**: 16162
**Date**: 2021-02-23
**URL**: https://discourse.slicer.org/t/how-to-remove-some-segment-editor-effects/16162

---

## Post #1 by @akshay_pillai (2021-02-23 16:54 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.11.202.00930</p>
<p>I am trying to create a new module from the segment editor module and need to remove some of the editor effects that I won’t be needing. Is there any way to do this. I want to keep some of the effects and remove the rest.For example, remove Draw tube, Engrave, Islands, Level tracing, split volume,flood filling, but keep the rest. Please let me know if anyone has done this and how? Any help is appreciated. Thanks.</p>

---

## Post #2 by @Sunderlandkyl (2021-02-23 17:00 UTC)

<p>You can use <a href="https://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html#ac28caab505058e98b850f73044c82ee8" rel="noopener nofollow ugc">setEffectNameOrder</a> to set the order that you would like the effects to appear and disable <a href="https://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html#a7950066736b1a5aa30b32ddc67fb9e56" rel="noopener nofollow ugc">unorderedEffectsVisible</a> to hide the ones that weren’t specified.</p>

---

## Post #3 by @akshay_pillai (2021-02-23 17:04 UTC)

<p>Hey, thanks a lot. If its no trouble, Can you give me an example of how the code would be for any one effect to be listed.</p>

---

## Post #4 by @Sunderlandkyl (2021-02-23 17:09 UTC)

<p>Sure, here’s an example of creating a segment editor widget with only the paint and threshold effects:</p>
<pre><code class="lang-auto">segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setEffectNameOrder(["Paint", "Threshold"])
segmentEditorWidget.unorderedEffectsVisible = False
segmentEditorWidget.show()

</code></pre>

---

## Post #5 by @akshay_pillai (2021-02-23 17:43 UTC)

<p>Thanks! That helped.</p>

---

## Post #6 by @danielgreenwood (2021-05-31 18:46 UTC)

<p>Good question and perfect answers to solve this problem. <a href="https://removalsofberkshire.com/" rel="noopener nofollow ugc"><img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=9" title=":slightly_smiling_face:" class="emoji only-emoji" alt=":slightly_smiling_face:"></a> I appreciate that, thanks!</p>

---
