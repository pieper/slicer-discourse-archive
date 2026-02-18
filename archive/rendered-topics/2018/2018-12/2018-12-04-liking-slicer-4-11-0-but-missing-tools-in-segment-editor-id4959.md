# Liking Slicer 4.11.0 but missing tools in segment editor

**Topic ID**: 4959
**Date**: 2018-12-04
**URL**: https://discourse.slicer.org/t/liking-slicer-4-11-0-but-missing-tools-in-segment-editor/4959

---

## Post #1 by @ermatlock (2018-12-04 19:25 UTC)

<p>Hi there,<br>
I noticed that several tools are now missing from the segment editor, namely draw tube, flood filling, mask volume, surface cut, and watershed. I was using the mask volume quite a bit and missing it. Is it hidden or am i missing something?</p>
<p>Operating system: Windows 10<br>
Slicer version: 4.9.0 nightly 2018-12-03<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @cpinter (2018-12-04 19:37 UTC)

<p>I think you forgot to install the SegmentEditorExtraEffects extension</p>

---

## Post #3 by @ermatlock (2018-12-04 20:12 UTC)

<p>I did install the extension but apparently it didn’t show till my most recent restart. Thanks.</p>

---

## Post #4 by @cpinter (2018-12-04 20:29 UTC)

<p>Yes the Extension Manager shows a restart button for this purpose, because after you install any extension Slicer needs to be restarted.</p>

---

## Post #5 by @ermatlock (2018-12-04 21:09 UTC)

<p>Yes, I was aware of that but for some reason it took several restarts to show up. In a related subject, the extensions manager sometimes does not show previously installed extensions when installing a new build. Is there any trick to refresh this? Thanks!</p>

---

## Post #6 by @cpinter (2018-12-05 14:19 UTC)

<aside class="quote no-group" data-username="ermatlock" data-post="5" data-topic="4959">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/a87d85/48.png" class="avatar"> ermatlock:</div>
<blockquote>
<p>it took several restarts to show up</p>
</blockquote>
</aside>
<p>Unfortunately since migrating to Qt5, the web-based widget of Extension Manager has issues. So now it’s better to wait 5-10 seconds after the extension installation is done, so that you can safely assume that every step is finished.</p>
<aside class="quote no-group" data-username="ermatlock" data-post="5" data-topic="4959">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/a87d85/48.png" class="avatar"> ermatlock:</div>
<blockquote>
<p>extensions manager sometimes does not show previously installed extensions</p>
</blockquote>
</aside>
<p>I’m not aware of this issue. Not sure if others in the community do, I’ll let them answer if so. In the meantime can you describe exactly what is the symptom?</p>

---

## Post #7 by @lassoan (2018-12-08 20:51 UTC)

<aside class="quote no-group" data-username="ermatlock" data-post="5" data-topic="4959">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/a87d85/48.png" class="avatar"> ermatlock:</div>
<blockquote>
<p>extensions manager sometimes does not show previously installed extensions</p>
</blockquote>
</aside>
<p>This may be the same issue: you need to wait until the “Restart” button becomes enabled (it may take tens of seconds), otherwise extension installation may be incomplete.</p>

---
