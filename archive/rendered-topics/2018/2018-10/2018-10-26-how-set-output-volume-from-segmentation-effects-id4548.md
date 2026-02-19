---
topic_id: 4548
title: "How Set Output Volume From Segmentation Effects"
date: 2018-10-26
url: https://discourse.slicer.org/t/4548
---

# How set output volume from segmentation effects

**Topic ID**: 4548
**Date**: 2018-10-26
**URL**: https://discourse.slicer.org/t/how-set-output-volume-from-segmentation-effects/4548

---

## Post #1 by @kayarre (2018-10-26 18:55 UTC)

<p>I am trying to specify the output of the “Mask Volume” effect<br>
how can I specify the input and output volumes ?<br>
assuming I don’t want to use the master as input and I don’t know how to set the output?</p>
<p>e.g.</p>
<pre><code class="lang-auto">segmentEditorWidget.setActiveEffectByName('Mask volume')
maskEffect = segmentEditorWidget.activeEffect()
maskEffect.setParameter('FillValue', -1)
maskEffect.setParameter('Operation', 'FILL_OUTSIDE')
</code></pre>

---

## Post #2 by @jamesobutler (2018-10-26 19:15 UTC)

<p>A good method for figuring out how to set code for items in the widget that you are using(SegmentEditorWidget in this case) is calling .children(), .findChildren(…) if you know the object type, or the more specific .findChild(…) if you know object type and object name.</p>
<p>From the slicer python interactive you can always do something like SegmentEditorWidget.[tab] to see what members are available to use.</p>

---

## Post #3 by @lassoan (2018-10-26 21:41 UTC)

<p>Have a look at the source code of this effect: <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorMaskVolume/SegmentEditorMaskVolumeLib/SegmentEditorEffect.py">https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorMaskVolume/SegmentEditorMaskVolumeLib/SegmentEditorEffect.py</a></p>
<p>It should be possible to set the input and output volume by modifying the segment editor node, but unfortunately this effect is not storing this information in MRML. This is a mistake, and this kind of mistakes are the reason why this effect is not yet integrated into Slicer core but still in this extension.</p>
<p>However, you can easily perform the Masking operation by calling <code>maskVolumeWithSegment</code> method of the effect.</p>

---

## Post #4 by @kayarre (2018-10-29 17:36 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> I have looked at those attributes but didn’t find a helpful clue. I see now how to use the .children()</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>  i looked through the source but can do some more investigation. how do I access maskVolumeWithSegment?</p>
<p>What would it take for the effect to be slicer core ready?</p>

---

## Post #5 by @lassoan (2018-10-29 19:04 UTC)

<aside class="quote no-group" data-username="kayarre" data-post="4" data-topic="4548">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>how do I access maskVolumeWithSegment</p>
</blockquote>
</aside>
<p>qMRMLSegmentEditorWidget::effectByName method should work.</p>
<aside class="quote no-group" data-username="kayarre" data-post="4" data-topic="4548">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>What would it take for the effect to be slicer core ready?</p>
</blockquote>
</aside>
<p>See <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/issues/10" class="inline-onebox">Move Mask Volume effect to Slicer core · Issue #10 · lassoan/SlicerSegmentEditorExtraEffects · GitHub</a></p>

---

## Post #6 by @kayarre (2018-10-29 19:18 UTC)

<p>Basically it’s easier to just replicate the method maskVolumeWithSegment without the use of the widget as its pretty simply using vtkImageToImageStencil.</p>

---

## Post #7 by @lassoan (2018-10-29 19:24 UTC)

<p>Yes, maskVolumeWithSegment method is all you need, so you can copy-paste as is into your script. The only disadvantage of cloning the code is that if there are any fixes or improvements then you don’t get those automatically, but since the amount of code is very small, most likely this won’t be an issue.</p>

---
