# Blurb for Slicer Download page

**Topic ID**: 16040
**Date**: 2021-02-17
**URL**: https://discourse.slicer.org/t/blurb-for-slicer-download-page/16040

---

## Post #1 by @muratmaga (2021-02-17 18:54 UTC)

<p>Often new users of Slicer are confused about what version of Slicer to use, and also how the stable and preview versions differ from each other.</p>
<p>It also doesn’t help that the current preview has red “unstable” text next to it.</p>
<p>I suggest something like this to be added below the installer table:</p>
<p><strong>Which version of 3D Slicer to install?</strong><br>
<strong>Stable:</strong> Is more rigorously tested but will not contain the latest features and functionality added to the Slicer. All extensions are available.<br>
<strong>Preview:</strong> is bleeding edge and is changed daily. Some days preview versions may not be fully functional or extensions may be incomplete. If you encounter a unstable preview version or it is missing the extensions you are looking for, you will have to install another preview version in the next day or so.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #2 by @pieper (2021-02-17 19:23 UTC)

<p>Yes, that would be good wording.  Maybe also on the Preview we could add "If you encounter a unstable preview version or it is missing the extensions you are looking for <em>check the Support section of the forum for recent status reports, or</em> another preview version in the next day or so <em>to see if the issue is resolved.</em></p>
<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="16040">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>It also doesn’t help that the current preview has red “unstable” text next to it.</p>
</blockquote>
</aside>
<p>Yes, this is out of date and should be removed - it was added when vtk9 was enabled but not working for a number of key features.</p>

---

## Post #3 by @Sam_Horvath (2021-02-17 19:32 UTC)

<p>I can take that down, but we are about to attempt vtk9 again so…  maybe we keep it there until that goes through.  I’m fine either way</p>

---

## Post #4 by @muratmaga (2021-02-17 19:49 UTC)

<aside class="quote no-group" data-username="Sam_Horvath" data-post="3" data-topic="16040">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>I can take that down, but we are about to attempt vtk9 again so…</p>
</blockquote>
</aside>
<p>With or without VTK9 attempt, I wouldn’t suggest it taking it down -at least not without replacing a more descriptive and helpful text. At least right now it suggests there might be issues… But I think something more detailed would be better.</p>

---

## Post #5 by @lassoan (2021-02-17 19:52 UTC)

<p>I think if we can keep creating a new stable release every 3 months then most users could just use the latest stable. Only those users would need the preview who wants to try work-in-progress features.</p>
<p>We are getting closer to this target - the new stable release will probably come out within days, which means we needed about 4-5 months.</p>
<p>Instead of the strong “Unstable” message, we could write “Recommended” next to the stable release. (although after VTK9 integration we expect to run into issues).</p>

---

## Post #6 by @muratmaga (2021-02-17 19:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="16040">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Instead of the strong “Unstable” message, we could write “Recommended” next to the stable release. (although after VTK9 integration we expect to run into issues).</p>
</blockquote>
</aside>
<p>That’s fine too, but extensions are a big part of 3D Slicer ecosystem, and the fundamental difference between stable and preview versions are not described with these single words. Issue is not just stability.</p>

---
