# Is it possible to implement segment editor in c++

**Topic ID**: 39808
**Date**: 2024-10-23
**URL**: https://discourse.slicer.org/t/is-it-possible-to-implement-segment-editor-in-c/39808

---

## Post #1 by @bryanChau (2024-10-23 01:41 UTC)

<p>I noticed that the segment editor module is under the python. I was wondering if I could integrated segment editor module into my c++ qt app. Cuz running AI inference under python is much slower when it compared c++</p>

---

## Post #2 by @bryanChau (2024-10-23 03:10 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> it seems some effect is implemented in Python version --ref <a href="https://github.com/Slicer/Slicer/tree/main/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorEffects" class="inline-onebox" rel="noopener nofollow ugc">Slicer/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorEffects at main · Slicer/Slicer · GitHub</a>, so I guess migrating all the effects are not viable to do so. Does that make sense?</p>

---

## Post #3 by @lassoan (2024-10-23 05:33 UTC)

<aside class="quote no-group" data-username="bryanChau" data-post="1" data-topic="39808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/c2a13f/48.png" class="avatar"> bryanChau:</div>
<blockquote>
<p>Cuz running AI inference under python is much slower when it compared c++</p>
</blockquote>
</aside>
<p>There is no difference in speed of running AI inference in Python and C++, because Python just adds a very thin wrapper over underlying highly optimized compiled code with negligible overhead.</p>
<aside class="quote no-group" data-username="bryanChau" data-post="2" data-topic="39808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/c2a13f/48.png" class="avatar"> bryanChau:</div>
<blockquote>
<p>I guess migrating all the effects are not viable to do so. Does that make sense?</p>
</blockquote>
</aside>
<p>C++/Python language choice is a minor detail. It is usually very easy to translate the code between these languages.</p>
<p>The important decision for you to make is if you want to develop a C++/Qt application from scratch or build it on a well-proven application framework, such as Slicer. I would of course recommend to build on Slicer, as you can save many years of development efforts.</p>

---
