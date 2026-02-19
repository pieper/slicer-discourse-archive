---
topic_id: 16250
title: "Release Of Slicer 4 11 20210226 In Progress Regular Builds A"
date: 2021-02-27
url: https://discourse.slicer.org/t/16250
---

# Release of Slicer 4.11.20210226 in progress: Regular builds are disabled

**Topic ID**: 16250
**Date**: 2021-02-27
**URL**: https://discourse.slicer.org/t/release-of-slicer-4-11-20210226-in-progress-regular-builds-are-disabled/16250

---

## Post #1 by @jcfr (2021-02-27 02:54 UTC)

<p>This evening, regular preview and stable builds of Slicer and associated extensions  will be disabled in favor of a new stable snapshot release.</p>
<p>To track the progress, see  <a href="https://github.com/Slicer/Slicer/issues/5489" class="inline-onebox">Release Slicer v4.11.20210226 · Issue #5489 · Slicer/Slicer · GitHub</a></p>

---

## Post #2 by @cpinter (2021-02-27 14:34 UTC)

<p>Should it be 4.13.20212026?</p>

---

## Post #3 by @jcfr (2021-02-27 15:41 UTC)

<p>Since originally, we planned to have the last 4.11.YYYYMMDD snapshot release to be with VTK 8 and have the 4.13 series to be the one with VTK9 in preparation of Slicer 5.x, I kept the minor version as 11.</p>
<p>Here is the corresponding commit history:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/381c016f55704bf6fc7bb76e85e105a12371e988.png" alt="image" data-base62-sha1="80mJSR8yNgkG0XUUd1MMop380A0" width="370" height="192"></p>

---

## Post #4 by @lassoan (2021-02-27 16:08 UTC)

<p>4.11.20212026 indicates that it is a patch release, which means no new features and no API changes. Since we both added features and changed API since 20200930, incrementing the minor version would have been appropriate. However, I don’t mind if we leave this one as 4.11, as it is just a special interim release, for hopefully a short time.</p>
<p>As we are establishing our new quarterly stable release process, we should define a versioning scheme that is informative and not too burdensome for maintainers, and apply it consistently.</p>

---

## Post #5 by @muratmaga (2021-03-01 16:55 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="1" data-topic="16250">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>This evening, regular preview and stable builds of Slicer and associated extensions will be disabled in favor of a new stable snapshot release.</p>
</blockquote>
</aside>
<p>I see Mac and Linux versions up. Any chance Windows stable will be up today? (We have a planned tech check-in for our workshop tomorrow, and if possible I would like to have users install the latest stable snapshot.)</p>

---

## Post #6 by @jcfr (2021-03-01 17:26 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="16250">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Any chance Windows stable will be up today?</p>
</blockquote>
</aside>
<p>Now I got back the sign package from our software team, I will upload it shortly</p>

---

## Post #7 by @jcfr (2021-03-01 21:11 UTC)

<p>Waiting <a href="http://download.slicer.org">download.slicer.org</a> updates itself, you can download the signed window package here:</p>
<p><a href="https://slicer.kitware.com/midas3/item/586488" class="onebox" target="_blank" rel="noopener">https://slicer.kitware.com/midas3/item/586488</a></p>

---
