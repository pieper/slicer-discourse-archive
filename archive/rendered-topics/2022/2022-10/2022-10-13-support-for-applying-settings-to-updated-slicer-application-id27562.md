# Support for applying settings to updated Slicer application

**Topic ID**: 27562
**Date**: 2022-10-13
**URL**: https://discourse.slicer.org/t/support-for-applying-settings-to-updated-slicer-application/27562

---

## Post #1 by @dalv.silvermann (2022-10-13 20:10 UTC)

<p>Dear Andras Lasso,<br>
Is it possible to upgrade Slicer and stay with my current extensions and self written modules? I mean that without installing the new version and stay on my current (in the point of view of extensions and self added features) with only updating the slicer core, that includes initial modules?<br>
Where I can read about this process?</p>

---

## Post #2 by @lassoan (2022-10-19 05:49 UTC)

<aside class="quote no-group" data-username="dalv.silvermann" data-post="1" data-topic="27562">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dalv.silvermann/48/16193_2.png" class="avatar"> dalv.silvermann:</div>
<blockquote>
<p>Is it possible to upgrade Slicer and stay with my current extensions and self written modules? I mean that without installing the new version and stay on my current (in the point of view of extensions and self added features) with only updating the slicer core, that includes initial modules?<br>
Where I can read about this process?</p>
</blockquote>
</aside>
<p>We try to preserve backward API compatibility between Slicer versions, so some Python modules may work without changes on more recent Slicer versions. ABI compatibility is not preserved between Slicer versions, so you need to reinstall all extensions that contain modules implemented in C++.</p>
<p>Slicer-5.0.3 allows you to bookmark extensions and reinstall all your bookmarked extensions by a single click after you upgrade Slicer core.</p>

---
