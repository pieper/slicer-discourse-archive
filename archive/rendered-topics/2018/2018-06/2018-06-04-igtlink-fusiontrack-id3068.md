# IGTLink + FusionTrack

**Topic ID**: 3068
**Date**: 2018-06-04
**URL**: https://discourse.slicer.org/t/igtlink-fusiontrack/3068

---

## Post #1 by @pctlr75 (2018-06-04 14:28 UTC)

<p>Hi everybody,</p>
<p>I am new to 3D Slicer, and I have a simple question.<br>
I want to know if IGTLink modul can work with FusionTrack250 Device, from Atracsys company.<br>
I didn’t see any topic that answer this problem.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2018-06-04 14:32 UTC)

<p>Yes, Slicer can connect to Atracsys trackers via OpenIGTLink by using <a href="http://plustoolkit.org/">Plus toolkit</a>. SpryTrack models work well already. FusionTrack support is about to be completed/being tested - you can monitor progress or ask questions about it here: <a href="https://github.com/PlusToolkit/PlusLib/issues/241">https://github.com/PlusToolkit/PlusLib/issues/241</a>.</p>

---

## Post #3 by @pctlr75 (2018-06-04 14:46 UTC)

<p>Thank you very much, I’ll try your solution.</p>

---

## Post #4 by @pctlr75 (2018-06-21 12:20 UTC)

<p>Hello again Andras Lasso,</p>
<p>unfortunatly i am still stuck with this fusiontrack problem. I downloaded toolkit plus &amp; of course 3d slicer (version 4.8.1). And i cannot find fusiontrack device in the list propose by toolkit plus.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38984164abc2e0d8be8b79c952df43f7a05c6691.png" data-download-href="/uploads/short-url/84EWxdEB58t2X1N6WWgRcnX6u41.png?dl=1" title="list" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38984164abc2e0d8be8b79c952df43f7a05c6691.png" alt="list" data-base62-sha1="84EWxdEB58t2X1N6WWgRcnX6u41" width="670" height="500" data-dominant-color="E5E9ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">list</span><span class="informations">771×575 28.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also, i find out that fusion track 3d slicer link only works with the developper version of 3d slicer. Is is true ?</p>
<p>Thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @lassoan (2018-06-21 15:54 UTC)

<p>As you can see, <a href="https://github.com/PlusToolkit/PlusLib/issues/241">item #241</a> in Plus toolkit’s issue tracker is still open, which means that the work is still in progress. You can comment in that issue if you have any specific questions about fusiontrack support.</p>
<aside class="quote no-group" data-username="pctlr75" data-post="4" data-topic="3068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/3ec8ea/48.png" class="avatar"> pctlr75:</div>
<blockquote>
<p>i find out that fusion track 3d slicer link only works with the developper version of 3d slicer</p>
</blockquote>
</aside>
<p>There is no “developer” version of Slicer, just Stable and Nightly (a.k.a. Preview) versions. OpenIGTLink interface is available in both: bundled with the main installer package in Stable version, and available in a separate extension in Nightly versions.</p>

---
