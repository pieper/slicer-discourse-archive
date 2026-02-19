---
topic_id: 19329
title: "Use Segmentation From Segment Editor As Initialization For L"
date: 2021-08-24
url: https://discourse.slicer.org/t/19329
---

# Use segmentation from Segment Editor as initialization for Level Set Segmentation

**Topic ID**: 19329
**Date**: 2021-08-24
**URL**: https://discourse.slicer.org/t/use-segmentation-from-segment-editor-as-initialization-for-level-set-segmentation/19329

---

## Post #1 by @tossin (2021-08-24 04:34 UTC)

<p>From what I can tell, the Level Set Segmentation panel from the Slicer VMTK Extension only allows initialization from scratch using colliding fronts or fast marching.  However, I’d like to be able to use Level Set Segmentation to refine a segmentation generated using the Segment Editor.  Is there some way to do this?</p>
<p>Also, I noticed that there is a leftover <code>xrange</code> in LevelSetSegmentation.py (line 583) that will raise an error and prevent the code from working properly.</p>

---

## Post #2 by @pieper (2021-08-24 13:42 UTC)

<p>A PR to fix the xrange issue would be welcome, as would any new functionality you want to add.  There is no core developer working on this extension right now, so community contributions are needed to help keep it going.</p>

---

## Post #3 by @lassoan (2021-08-25 15:08 UTC)

<p><a class="mention" href="/u/tossin">@tossin</a> thanks for reporting. I’ve fixed <code>xrange</code> (changed to <code>range</code>).</p>
<aside class="quote no-group" data-username="tossin" data-post="1" data-topic="19329">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/258eb7/48.png" class="avatar"> tossin:</div>
<blockquote>
<p>I’d like to be able to use Level Set Segmentation to refine a segmentation generated using the Segment Editor. Is there some way to do this?</p>
</blockquote>
</aside>
<p>This should be no problem. You can just add a segmentation node selector and if the user selects a segmentation node as input then you can export it to a labelmap and use it as input of the level set.</p>

---
