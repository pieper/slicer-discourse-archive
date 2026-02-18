# Bug: zoom in linked slices gets out of sync when using right-click+drag (again)

**Topic ID**: 22996
**Date**: 2022-04-18
**URL**: https://discourse.slicer.org/t/bug-zoom-in-linked-slices-gets-out-of-sync-when-using-right-click-drag-again/22996

---

## Post #1 by @DIV (2022-04-18 07:13 UTC)

<p>I linked the slice views and when I <strong>right-click+drag</strong> to change the field of view (zoom), only the field of view of the slice where my mouse is is changed.</p>
<p>When I use <strong>ctrl+scroll</strong> all the linked slice views are synchronised and change together.</p>
<p>This unexpected behaviour happened in both</p>
<ul>
<li>version 4.13.0 revision 30748 built 2022-03-31</li>
<li>version 4.13.0 revision 30784 built 2022-04-16</li>
</ul>
<p>I assume that this is a bug, based on similar past reports:</p>
<ul>
<li>
<a href="https://discourse.slicer.org/t/zoom-in-linked-slices-gets-out-of-sync-when-using-ctl-scroll/9994" class="inline-onebox">Zoom in linked slices gets out of sync when using ctl+scroll</a> (Jan. 2020)</li>
<li>
<a href="https://discourse.slicer.org/t/zoom-in-linked-slices-gets-out-of-sync-when-using-right-click-drag/21678" class="inline-onebox">Zoom in linked slices gets out of sync when using right-click+drag</a> (Jan. 2022)</li>
</ul>
<p>In previous versions using either <strong>right-click+drag</strong> or <strong>ctrl+scroll</strong> was equivalent:  both methods changed the field of view of all linked slices.<br>
Indeed, the second linked post, above, indicates that a bug with the same symptoms was fixed in version 4.13.0; revision 30570; built 2022-01-29, so maybe this is a regression?</p>
<p>—DIV</p>
<p>P.S.  I didn’t notice any indication in the online <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-views" rel="noopener nofollow ugc">User Guide for the user interface</a> that the behaviour is supposed to be different.</p>

---

## Post #2 by @rbumm (2022-04-18 10:35 UTC)

<p>In 4.13.0-2022-04-12 r30779 / ed4845f I link the slice views and</p>
<ul>
<li>zoom in a single, selected slice by using right-click+drag</li>
<li>zoom in all slices simultaneously by using ctrl + mouse wheel</li>
</ul>

---

## Post #3 by @cpinter (2022-04-18 11:17 UTC)

<p>It looks like a bug to me. Can you please add it as an issue <a href="https://github.com/Slicer/Slicer/issues">here</a> for milestone 5.0.1? Thanks!</p>

---

## Post #4 by @DIV (2022-04-19 10:36 UTC)

<p>Hello, Csaba.<br>
I’ve submitted the <a href="https://github.com/Slicer/Slicer/issues/6318" rel="noopener nofollow ugc">bug report</a>, but couldn’t see how to <a href="https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/associating-milestones-with-issues-and-pull-requests" rel="noopener nofollow ugc">associate that issue with the specified milestone</a>.  Maybe that needs to be done by an administrator?<br>
—DIV</p>

---

## Post #5 by @cpinter (2022-04-19 15:26 UTC)

<p>Thank you!</p>
<aside class="quote no-group" data-username="DIV" data-post="4" data-topic="22996">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>Maybe that needs to be done by an administrator?</p>
</blockquote>
</aside>
<p>Probably needs at least triage rights. I added the milestone.</p>

---

## Post #6 by @DIV (2022-04-21 01:20 UTC)

<p>Thanks.<br>
Andras has <a href="https://github.com/Slicer/Slicer/issues/6318#issuecomment-1103283676" rel="noopener nofollow ugc">reportedly fixed</a> this now.</p>

---
