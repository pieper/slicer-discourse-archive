# Undo Segment Changes in Extensions: MONAI label and nnInteractive

**Topic ID**: 45427
**Date**: 2025-12-09
**URL**: https://discourse.slicer.org/t/undo-segment-changes-in-extensions-monai-label-and-nninteractive/45427

---

## Post #1 by @Deep_Learning (2025-12-09 17:57 UTC)

<p>I am trying to understand the undo behavior when editing a segment by hand in extensions such as MONAI label or nnInteractive.</p>
<p>I am talking about using the scissors or largest island in the “segment module” in these extensions itself.</p>
<p>I feel that there is no undo, ctrl-z.</p>
<p>If I edit in the Segment Module itself, there is an undo.</p>
<p>Is that true or just me?</p>

---

## Post #2 by @cpinter (2025-12-10 12:24 UTC)

<aside class="quote no-group" data-username="Deep_Learning" data-post="1" data-topic="45427">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/deep_learning/48/15345_2.png" class="avatar"> Deep_Learning:</div>
<blockquote>
<p>I am talking about using the scissors or largest island in the “segment module” in these extensions itself.</p>
</blockquote>
</aside>
<p>The MONAI Auto3DSeg module does not offer segment editor effects, so I don’t understand what you are trying to ask. Can you give us a list of steps that you do? Which extension do you have installed (exact name please) and exactly what modules you use and in what order and what steps you do in each? Thanks!</p>

---

## Post #3 by @Deep_Learning (2025-12-10 14:13 UTC)

<p>MONAILabel and nnInteractive extensions.  Both have Segment editor as a drop down.  My experience is that I use the advanced functionality of these extensions and then trim the resulting Segemnt with the included Segment Editor (scissors or remove islands). And nothing happens with an Undo.</p>

---

## Post #4 by @dzenanz (2025-12-10 15:37 UTC)

<p>In SegmentEditor, Z is undo (Ctrl+Z also works). That shortcut does not seem to work in nnInteractive (I used it a few days ago), but clicking the undo button (bent yellow arrow) worked.</p>

---

## Post #5 by @Deep_Learning (2025-12-10 18:00 UTC)

<p>100% right…. Thanks. I’ll be doing less cloning…..</p>

---
