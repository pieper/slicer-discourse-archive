---
topic_id: 3198
title: "Where To File Report Bugs Discourse Or Mantis"
date: 2018-06-15
url: https://discourse.slicer.org/t/3198
---

# Where to file/report bugs: Discourse or mantis?

**Topic ID**: 3198
**Date**: 2018-06-15
**URL**: https://discourse.slicer.org/t/where-to-file-report-bugs-discourse-or-mantis/3198

---

## Post #1 by @muratmaga (2018-06-15 17:07 UTC)

<p>Hi<br>
I reported an issue with VR module couple days ago with one of the nightlies on Mantis (<a href="https://issues.slicer.org/view.php?id=4572" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4572</a>) .<br>
But I have been seeing people are also reporting issues on the forum as well. What is the preferred way of reporting them?</p>

---

## Post #2 by @cpinter (2018-06-15 17:24 UTC)

<p>Valid question. I think what you did was the proper procedure, reporting bugs should happen on Mantis, and discourse is for questions. Many times when people ask something that is a bug, we need a Mantis issue.</p>
<p>I understand your concern though, because discourse is much more active. This is partly because I think not a lot of people follow all the activity on Mantis (such as myself), and the auto-assignment system is not very up-to-date. For example in this case a volume rendering (that said please let’s not use the term VR for that, because most people think it’s about virtual reality), the bug was assigned to J2, but he’s very unlikely to work on that, and it should be me who investigates. I’ll look into your issue.</p>

---

## Post #3 by @lassoan (2018-06-15 17:26 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Is it possible to set up Mantis to notify me about all incoming issues?</p>

---

## Post #4 by @cpinter (2018-06-15 17:29 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Now while we’re at it: there’s an issue I fixed for you a few days ago, and in this case we’re waiting for your response <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"> If you missed the notification, then it’s a good illustration about this problem…</p>

---

## Post #5 by @muratmaga (2018-06-15 17:32 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a><br>
I did get the notification. But I think it will be good to link mantis and discourse somehow.</p>
<p>Anyways, this is actually a new issue I encountered with normal volume rendering, while testing your update. I provided a sample dataset. FOr me it reproduces all the time. Same dataset functions perfectly fine with the stable version.</p>

---

## Post #6 by @cpinter (2018-06-15 17:36 UTC)

<p>I downloaded the dataset and will check it out. If it’s an easy fix I’ll do it today, but if not, I cannot promise anything because we’ll have the project week very soon. I’ll keep you posted… in the Mantis issue.</p>

---

## Post #7 by @muratmaga (2018-06-15 17:38 UTC)

<p>No rush on my end. I just want to make you aware, and also provide you a high-resolution dataset for testing purposes. Sometimes those are overlooked as they are not common in medical datasets.</p>

---

## Post #8 by @jcfr (2018-06-15 17:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="3198" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Is it possible to set up Mantis to notify me about all incoming issues?</p>
</blockquote>
</aside>
<p>There are two things to consider</p>
<h3><a name="p-12611-email-notification-1" class="anchor" href="#p-12611-email-notification-1" aria-label="Heading link"></a>Email notification</h3>
<p>Could you check your account settings:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dab2b134067389bd3be3aa4c2af04f8e373bca1.png" data-download-href="/uploads/short-url/kdg34PEvb7CcBCEbt833AO9wZAB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dab2b134067389bd3be3aa4c2af04f8e373bca1_2_690x463.png" alt="image" data-base62-sha1="kdg34PEvb7CcBCEbt833AO9wZAB" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dab2b134067389bd3be3aa4c2af04f8e373bca1_2_690x463.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dab2b134067389bd3be3aa4c2af04f8e373bca1_2_1035x694.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dab2b134067389bd3be3aa4c2af04f8e373bca1.png 2x" data-dominant-color="E6ECEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1091×733 57.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-12611-auto-assign-of-issues-2" class="anchor" href="#p-12611-auto-assign-of-issues-2" aria-label="Heading link"></a>Auto-assign of issues</h3>
<p>Currently some of the categories are auto-assigned. See below.</p>
<p>I think it is time to revisit this. Generally, I suggest we review each new issue, and then decide if we assign it or set the backlog target.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce013dbd5a13f25cf7f9bef0604bf9e8f5eceaf7.png" data-download-href="/uploads/short-url/top17BFoxAat4r12gMYzIucIJFR.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce013dbd5a13f25cf7f9bef0604bf9e8f5eceaf7_2_690x357.png" alt="image" data-base62-sha1="top17BFoxAat4r12gMYzIucIJFR" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce013dbd5a13f25cf7f9bef0604bf9e8f5eceaf7_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce013dbd5a13f25cf7f9bef0604bf9e8f5eceaf7_2_1035x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce013dbd5a13f25cf7f9bef0604bf9e8f5eceaf7_2_1380x714.png 2x" data-dominant-color="E9ECEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1778×922 78.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2018-06-15 18:23 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="8" data-topic="3198">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Could you check your account settings</p>
</blockquote>
</aside>
<p>I have exactly the same settings as you, still, I don’t get notification about all new issues. I only get notifications if a bug changes that is assigned to me (or when I set a bug to be monitored, maybe also after I add a comment to an issue).</p>

---

## Post #10 by @cpinter (2018-06-15 18:27 UTC)

<p>Same for me. I have all those checkboxes checked, still only get updates about issues assigned to me or monitored.</p>

---

## Post #11 by @lassoan (2018-06-15 19:04 UTC)

<p>Removing default_notify_flags might solve this issue - see here: <a href="https://www.mantisbt.org/forums/viewtopic.php?f=3&amp;t=6352">https://www.mantisbt.org/forums/viewtopic.php?f=3&amp;t=6352</a>.</p>

---

## Post #12 by @jcfr (2018-06-15 19:17 UTC)

<p>I just updated the configuration was described below:</p>
<ul>
<li>Always notify user with “manager” access level (see below) for details</li>
<li>Added <a class="mention" href="/u/cpinter">@cpinter</a> to the manager level (<a class="mention" href="/u/lassoan">@lassoan</a> was already associated with that access level)</li>
</ul>
<h3><a name="p-12624-after-1" class="anchor" href="#p-12624-after-1" aria-label="Heading link"></a>After</h3>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/428677c444412371200d4b8a66b9e18865078ea2.png" data-download-href="/uploads/short-url/9uvBLfftX3Gyxpe8eKu63wVRmvw.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/428677c444412371200d4b8a66b9e18865078ea2_2_690x289.png" alt="image" data-base62-sha1="9uvBLfftX3Gyxpe8eKu63wVRmvw" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/428677c444412371200d4b8a66b9e18865078ea2_2_690x289.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/428677c444412371200d4b8a66b9e18865078ea2_2_1035x433.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/428677c444412371200d4b8a66b9e18865078ea2_2_1380x578.png 2x" data-dominant-color="EEF2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1681×706 56.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-12624-before-2" class="anchor" href="#p-12624-before-2" aria-label="Heading link"></a>Before</h3>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01feb9310379a70b7fa30676495017fa8087542d.png" data-download-href="/uploads/short-url/hEdD5FkssmjLuH7uy9mPRT0aXH.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01feb9310379a70b7fa30676495017fa8087542d_2_690x301.png" alt="image" data-base62-sha1="hEdD5FkssmjLuH7uy9mPRT0aXH" width="690" height="301" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01feb9310379a70b7fa30676495017fa8087542d_2_690x301.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01feb9310379a70b7fa30676495017fa8087542d_2_1035x451.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01feb9310379a70b7fa30676495017fa8087542d_2_1380x602.png 2x" data-dominant-color="EEF2F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1687×738 59.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @jcfr (2018-06-15 19:19 UTC)

<p>I also made sure that manager could tweak these settings:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b3c9fcb95b84d48b499800d8ba042feee6f4237.png" alt="image" data-base62-sha1="3SWMgmUTfeYuKt1eDTx6iIoOOaj" width="399" height="50"></p>

---

## Post #14 by @lassoan (2018-06-16 14:32 UTC)

<p>Thank you <a class="mention" href="/u/jcfr">@jcfr</a>. I’ll let you know if I’m start getting notifications about new issues.</p>

---

## Post #15 by @cpinter (2018-07-25 18:35 UTC)

<p>I still haven’t received any email about any issue that I aws not monitoring. <a class="mention" href="/u/lassoan">@lassoan</a> have you?</p>

---

## Post #16 by @lassoan (2018-07-25 18:58 UTC)

<p>I get notifications when an issue is assigned to me or later when its state changes. However, I cannot get notifications about any new issues (before I interact with them).</p>

---
