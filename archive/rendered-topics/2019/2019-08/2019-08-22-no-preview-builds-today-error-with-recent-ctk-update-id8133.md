# No preview builds today: error with recent CTK update

**Topic ID**: 8133
**Date**: 2019-08-22
**URL**: https://discourse.slicer.org/t/no-preview-builds-today-error-with-recent-ctk-update/8133

---

## Post #1 by @Sam_Horvath (2019-08-22 14:31 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=1675447" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/viewBuildError.php?buildid=1675447</a></p>
<p>looking into it</p>

---

## Post #2 by @jcfr (2019-08-22 14:38 UTC)

<p>Ooops. It turns out that my local build also failed.</p>
<p>If you haven’t done so, I can also have a look after lunch when I am back in the office.</p>

---

## Post #3 by @jcfr (2019-08-22 14:43 UTC)

<p>I think this should be fixed by <a href="https://github.com/commontk/CTK/pull/879" rel="nofollow noopener">https://github.com/commontk/CTK/pull/879</a></p>

---

## Post #4 by @pieper (2019-08-22 15:03 UTC)

<p>FYI I added this patch to my mac build and it seems to be working (previously broken build in progress to confirm).</p>
<p>Update: build completed!</p>

---

## Post #5 by @lassoan (2019-08-22 15:23 UTC)

<p>Thank you! Since there have not been any Windows build for almost a week, it would be great if you could trigger a rebuild on the dashboard now.</p>

---

## Post #6 by @Sam_Horvath (2019-08-22 15:57 UTC)

<p>Great!  <a class="mention" href="/u/jcfr">@jcfr</a> could you merge the ctk patch, and I will take care of doing the slicer fix and restarting the factories.</p>

---

## Post #7 by @jcfr (2019-08-22 16:57 UTC)

<aside class="quote no-group" data-username="Sam_Horvath" data-post="6" data-topic="8133">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>ould you merge the ctk patch</p>
</blockquote>
</aside>
<p>Will do so at 2pm following my upcoming meeting</p>

---

## Post #8 by @jcfr (2019-08-22 19:54 UTC)

<p>Fix integrated in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28457" rel="nofollow noopener">r28457</a></p>

---
