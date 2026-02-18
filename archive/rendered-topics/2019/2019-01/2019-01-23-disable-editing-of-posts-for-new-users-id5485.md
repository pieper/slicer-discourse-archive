# Disable editing of posts for new users

**Topic ID**: 5485
**Date**: 2019-01-23
**URL**: https://discourse.slicer.org/t/disable-editing-of-posts-for-new-users/5485

---

## Post #1 by @lassoan (2019-01-23 16:08 UTC)

<p>It has become a common pattern that spam bots post some seemingly valid message that they edit to add malicious links a few days later (when people who monitor all new posts don’t read them anymore).</p>
<p>See for example these topics (spam posts are marked deleted and will disappear at some point):</p>
<ul>
<li><a href="https://discourse.slicer.org/t/initial-presentation/100/38" class="inline-onebox">Initial presentation</a></li>
<li><a href="https://discourse.slicer.org/t/migrating-github-issue-to-discourse/3738/8" class="inline-onebox">Migrating GitHub issue to discourse</a></li>
</ul>
<p>There are two options to discourage these spam bots:</p>
<ul>
<li>Option A: Change <a href="https://discourse.slicer.org/admin/site_settings/category/all_results?filter=min%20trust%20to%20edit%20post">minimum trust level for post editing</a> from “0: new user” to “1: basic user” (see <a>settings</a>). Since <a href="https://blog.discourse.org/2018/06/understanding-discourse-trust-levels/" rel="nofollow noopener">trust level 1 can be earned by just browsing the site</a>, it might not be very effective if spam bots are programmed to spend some time on the site.</li>
<li>Option B: Reduce <a href="https://discourse.slicer.org/admin/site_settings/category/all_results?filter=post%20edit%20time">time limit for editing a post</a> form the default 60 days to something like 1 hour (or maybe even 15 minutes). We would probably spot malicious links added soon after a new post is created. Spammers currently wait a few days.</li>
</ul>
<p>Option B would be probably more effective, but it would impact all users. However, it may not be that bad to limit post editing to quick modifications right after posting anyway. So, I slightly prefer option B.</p>
<p>What do you think <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/ihnorton">@ihnorton</a> <a class="mention" href="/u/fedorov">@fedorov</a></p>

---

## Post #2 by @pieper (2019-01-23 17:37 UTC)

<p>Yes, I prefer option B.  If people make a big mistake like posting possible PHI or something and don’t realize right away then they should be able to contact an admin to get the post edited.</p>

---

## Post #3 by @fedorov (2019-01-23 18:05 UTC)

<p>Amazing. I am glad you caught this Andras.</p>
<p>Why don’t we implement both A and B?</p>

---

## Post #4 by @lassoan (2019-01-23 18:18 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="3" data-topic="5485">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Why don’t we implement both A and B?</p>
</blockquote>
</aside>
<p>It is better do the minimum necessary restrictions to not frustrate users. We can first try if applying one of the restrictions is enough.</p>

---

## Post #5 by @jamesobutler (2019-01-23 18:20 UTC)

<p>OptionB sounds like a good option Andras.</p>
<p>I was suspicious of those comments in the topics that you marked as examples above. I specifically checked the specific user a day later to see if they modified the posts with links and sure enough they did. I then marked as spam at that time.</p>

---

## Post #6 by @lassoan (2019-01-23 18:23 UTC)

<p>Thanks for all the feedbacks. I’ve set post editing time limit to 60 minutes. Hopefully it is long enough for legitim users and short enough for spammers.</p>

---

## Post #7 by @fedorov (2019-01-23 18:31 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="5485">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It is better do the minimum necessary restrictions to not frustrate users. We can first try if applying one of the restrictions is enough.</p>
</blockquote>
</aside>
<p>Makes sense. I thought most will meet A anyway, but I can understand your concern. No objections!</p>

---
