---
topic_id: 33025
title: "Maximize Views On Double Click Stopped Working"
date: 2023-11-25
url: https://discourse.slicer.org/t/33025
---

# Maximize views on double click stopped working

**Topic ID**: 33025
**Date**: 2023-11-25
**URL**: https://discourse.slicer.org/t/maximize-views-on-double-click-stopped-working/33025

---

## Post #1 by @chir.set (2023-11-25 21:49 UTC)

<p>Hi,</p>
<p>Just saw this in 5.5.0-2023-11-24 r32358 / 9b8c823 (and self-built Slicer):</p>
<p>A double click on slice views or 3D views has no effect. Usually, the view is maximized or minimized. There’s a button and a menu item to do this, just reporting.</p>
<p>Regards.</p>

---

## Post #2 by @pieper (2023-11-25 23:34 UTC)

<p>Hmm, that’s not a good regression.  I have gotten used to that feature.  I can confirm the same issue on today’s preview on my linux system.</p>
<p>I wonder if it’s related to this: <a href="https://github.com/Slicer/Slicer/pull/7311" class="inline-onebox">Improve Event Delegation in qMRMLThreeDView and qMRMLSliceView by jcfr · Pull Request #7311 · Slicer/Slicer · GitHub</a></p>

---

## Post #3 by @pieper (2023-11-26 17:09 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> I can confirm this on my local build and with a download of the current preview.</p>
<p>Can you file an issue on github?</p>

---

## Post #4 by @chir.set (2023-11-26 17:18 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="33025">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Can you file an issue on github?</p>
</blockquote>
</aside>
<p>Unfortunately, I can no longer log in my github account since they required 2FA as mandatory, which is a no-go to me for such a service. Github is no longer a welcoming place because they changed initial rules.</p>
<p>I understand that things always change with time, that’s life. Github is free to define its policies, the user is free to define his policies as well. And there’s more I can’t do because of this.</p>
<p>Regretfully, I won’t be able to file this issue.</p>

---

## Post #5 by @pieper (2023-11-26 17:24 UTC)

<p>Ah, yes, sorry, I recall now.</p>
<p>I’ll file and issue so we can get this resolved.</p>

---

## Post #6 by @lassoan (2023-11-27 06:53 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="4" data-topic="33025">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Unfortunately, I can no longer log in my github account since they required 2FA as mandatory, which is a no-go to me for such a service. Github is no longer a welcoming place because they changed initial rules.</p>
</blockquote>
</aside>
<p>This is not a github thing. 2FA had to become part of our basic cyber hygiene due to bad actors becoming increasingly sophisticated. It is no longer optional or for high-value targets only, but unfortunately it is a must for everyone.</p>
<p>The good news is that setting up 2FA in github is very simple and it does not affect daily work at all, because you only need to authenticate a device once. I was postponing adding 2FA to my github account for a while, too, because I was afraid that it would complicate my access, but it turned out to be a non-issue. Github offers many 2FA options, so you should be able to find one that you like. First time you set it up and decide about which options you prefer may take 10-20 minutes, but setup of subsequent devices should take just 10-20 seconds extra (and you only need to authenticate each device only once).</p>

---

## Post #7 by @chir.set (2023-11-27 09:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="33025">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>authenticate each device</p>
</blockquote>
</aside>
<p>I’ll give it a second look, only because I made previous contributions to extensions.</p>
<p>The problem will be in the future. Initially, there was a single password, like with many other services (mail, bank, tax department…). Then github (and others) mandated application passwords, their ‘personal access token’. Now it’s 2FA.</p>
<p>Next it will be browsers (discourse and others already do that), then such ISP would be required, such device brand, facial recognition, fingerprint of the fourth right toe, country of birth … These guys are caught in a whirlwind of paranoia, no one knows how all this will end up, my bet is nothing effective.</p>
<p>A second look, as time permits, only because I made previous contributions to extensions.</p>

---
