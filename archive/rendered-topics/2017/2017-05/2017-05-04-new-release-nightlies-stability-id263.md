# New release / Nightlies stability

**Topic ID**: 263
**Date**: 2017-05-04
**URL**: https://discourse.slicer.org/t/new-release-nightlies-stability/263

---

## Post #1 by @jondo (2017-05-04 08:17 UTC)

<p>As a Slicer newbie, I wonder: When will the next version 4.7.0 be released?</p>
<p>The <a href="https://www.slicer.org/wiki/Roadmap" rel="nofollow noopener">wiki’s roadmap</a> was not updated since 2015, and the <a href="http://na-mic.org/Mantis/roadmap_page.php" rel="nofollow noopener">bug tracker’ roadmap</a> says “Scheduled For Release 2017-01-15”. According to the <a href="https://www.slicer.org/wiki/Release_Details" rel="nofollow noopener">rhythm of the last releases</a>, November seems plausible.</p>
<p>But maybe all of this is irrelevant, because the Nightlies are stable enough for everyday use? I am fearing data loss and backwards incompatibility. What are the largest features and changes that I am missing when staying with 4.6.2? It seems there is no (preliminary) changelog in the source, and also no preliminary 4.7 version of the <a href="https://www.slicer.org/wiki/Documentation/4.6/Announcements#Slicer_4.6_Highlights" rel="nofollow noopener">4.6 highlights</a>.</p>

---

## Post #2 by @lassoan (2017-05-04 16:18 UTC)

<p>Currently a stable release is created once a year. We would like to increase the pace to once in every quarter, but for that we need to simplify our processes, which is currently we are working on.</p>
<p>Nightly versions are stable. Saved data should be always backward-compatible: you can always load a scene to a newer version of Slicer than created the scene. There may be regressions in the nightly that takes a few days to detect and fix (maybe once in every few months), but these regressions very rarely can result in data loss.</p>
<p>If the stable build is older than a few months, I would recommend to use a nightly build. If you download a nightly and have no problems with it, keep using that for a few months (until there are some fixes or improvements in the nightly builds that you need).</p>

---

## Post #3 by @jondo (2017-05-05 06:30 UTC)

<p>Thank you for your reply! I will follow your recommendation.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="263">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Saved data should be always backward-compatible: you can always load a scene to a newer version of Slicer than created the scene.</p>
</blockquote>
</aside>
<p>Ah, so I meant forward compatibility <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=12" title=":blush:" class="emoji" alt=":blush:" loading="lazy" width="20" height="20">: Whether it is possible to go back to an older version (e.g. with keeping the database) in case of problems.</p>

---

## Post #4 by @cpinter (2017-05-05 12:54 UTC)

<p>In case of problems, we’ll be happy to help you to make the latest one work for your use case <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #5 by @jondo (2017-05-05 13:22 UTC)

<p>Great!</p>
<p>So the only reason for stable releases is that the ‘highlights’ page is updated <img src="https://emoji.discourse-cdn.com/twitter/stuck_out_tongue.png?v=5" title=":stuck_out_tongue:" class="emoji" alt=":stuck_out_tongue:"> <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=5" title=":wink:" class="emoji" alt=":wink:"></p>

---
