---
topic_id: 16360
title: "How To Prioritize Feature Requests"
date: 2021-03-04
url: https://discourse.slicer.org/t/16360
---

# How to prioritize feature requests?

**Topic ID**: 16360
**Date**: 2021-03-04
**URL**: https://discourse.slicer.org/t/how-to-prioritize-feature-requests/16360

---

## Post #1 by @lassoan (2021-03-04 14:31 UTC)

<p>We get a number of feature requests and it is not obvious how to prioritize them.</p>
<p>Discourse has an excellent <a href="https://www.discourse.org/plugins/topic-voting.html">topic voting</a> feature that is developed exactly for this. The nice thing is that it limits the number of votes, so it forces people to think about their priorities. Unfortunately, it requires the <a href="https://www.discourse.org/pricing">business hosting plan</a>, which costs $300/month instead of $100.</p>
<p>It is possible to sort issues by reactions (e.g., likes) on github, so it would also be an option to advertise this to users: <a href="https://github.com/Slicer/Slicer/issues?q=is%3Aopen+is%3Aissue+label%3Atype%3Aenhancement+sort%3Areactions-%2B1-desc">feature requests sorted by number of likes</a>.</p>
<p>The advantage is that people would know exactly what they vote on (instead of voting on a discussion topic that may mention many ideas) and it is free, but the number of votes (likes) is not limited, it is harder to discover this, and users need to create a github account.</p>
<p>What do you think? Should we start advertising to users to add likes to the github issue tracker or should we consider upgrading to business (or see if we can ask discourse for the voting feature be enabled for us)?</p>

---

## Post #2 by @pieper (2021-03-04 14:45 UTC)

<p>If we could stay within discourse I think this would be preferable.  Now that we are paying customers (even at a discount) maybe they would enable it?  But I guess they would prefer for us to upgrade our plan, since that is their business model after all.  I don’t think this specific feature would justify a big additional expense.</p>
<p>Speaking for myself, I prioritize based on projects that pay for me to deliver working systems, so while I like hearing from users I probably wouldn’t change my behavior much.</p>
<p>In the ideal world we would have a dedicated funding model to support development of new features based on community feedback.  We used to have that in NA-MIC, but we don’t currently have support like that, so for sustainability I’d focus on free resources like github, at least for now.</p>

---

## Post #3 by @lassoan (2021-03-04 14:53 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="16360">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I don’t think this specific feature would justify a big additional expense.</p>
</blockquote>
</aside>
<p>I agree.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Could you ask discourse about this? We should probably also ask about the page views limit, that we exceed by about 50%. We are really stretching it, as we get a discount and asking for extras, but if we ask politely then hopefully they will not be upset.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="16360">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>In the ideal world we would have a dedicated funding model to support development of new features based on community feedback. We used to have that in NA-MIC, but we don’t currently have support like that, so for sustainability I’d focus on free resources like github, at least for now.</p>
</blockquote>
</aside>
<p>It could be interesting to try to get CZI funding for this. I’ll write a separate email about this.</p>

---

## Post #4 by @pieper (2021-03-04 14:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="16360">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It could be interesting to try to get CZI funding for this. I’ll write a separate email about this.</p>
</blockquote>
</aside>
<p>Yes, I was thinking about this too, but since it’s just one year at a time we’d need to think about how a renewing service like discourse should handled for the long term.</p>

---

## Post #5 by @lassoan (2021-03-25 15:09 UTC)

<p>In response to comment from <a class="mention" href="/u/muratmaga">@muratmaga</a> on <a href="https://github.com/Slicer/Slicer/issues/5505#issuecomment-806856628">a github issue</a>:</p>
<p>The current method of adding “thumbs-up” on the github issue is not ideal, but there is no better option right now:</p>
<ul>
<li>Discourse: “business” plan (the minimum plan that contains voting plugin) costs $300. Currently, we pay something like $50 per month.</li>
<li>Github: Many people requested github to implement voting but for some reason they think that this is not a good idea (see <a href="https://github.com/isaacs/github/issues/9#issuecomment-150331398" class="inline-onebox">Add explicit `+1` feature for issues that isn't a comment · Issue #9 · isaacs/github · GitHub</a>). What Gtihub finally added is the ability to sort issues by emojis, which is of course not ideal, but should work well if there is a clear user need (even if there is some noise and missed votes due to incorrect voting).</li>
<li>Other servies: dedicated user feedback collection services (uservoice, canny, etc.) cost hundreds of dollars per month and would make our infrastructure more fragmented (more things to sign up for and monitor for both users and developers).</li>
</ul>

---

## Post #6 by @muratmaga (2021-03-25 16:17 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="16360">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The current method of adding “thumbs-up” on the github issue is not ideal, but there is no better option right now:</p>
</blockquote>
</aside>
<p>In addition to be able to vote, GH requires you to be logged in. I assume that’s to avoid bots and stuff but may not be convenient for everyone.</p>
<p>I think all of these goes back to how to support and grow this infrastructure and be able to keep paying for it from an open source project. Can there be a ‘subscription’ process for individual extensions to pay an annual fee that help running the extension manager (a free service), the forum to report their issues (another free service). i think for grant supported projects an annual ‘service’ fee couple thousand wouldn’t be too bad…</p>
<p>Another option is to establish a Slicer foundation and try to do some fundraising to pay these costs. I am not entirely sure what the legal relationships between Slicer the brand, the community and kitware so maybe not possible…</p>

---

## Post #7 by @lassoan (2021-03-25 20:16 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="16360">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>In addition to be able to vote, GH requires you to be logged in. I assume that’s to avoid bots and stuff but may not be convenient for everyone.</p>
</blockquote>
</aside>
<p>Logging in cannot be avoided, because you don’t want to make it very easy for one person to vote many times on the same issue. It is a good filter, too: if someone does not take the effort to sign up then that request can be safely ignored.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="16360">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I think all of these goes back to how to support and grow this infrastructure and be able to keep paying for it from an open source project.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="16360">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>establish a Slicer foundation and try to do some fundraising to pay these costs</p>
</blockquote>
</aside>
<p>It is a hard question. There are organizations that can act as financial hosts and have infrastructure for collecting donations (such as NumFocus or <a href="https://opencollective.com/opensource">OpenCollective</a>), so it would not be necessary to create a new legal entity.</p>
<p>However, crowdfunding works better for projects that have a very wide user base (e.g., all web developers) and that have no other chance of getting funding. Since medical image computing community is relatively small, and many groups have research grant funding that can be partially redirected to fund some Slicer features; focusing on getting funding via research grants is probably a better approach overall.</p>
<p>There is of course lots of room for improvement. For example, it would be great to have a mechanism that would allow pooling funding and developers to ensure continuous funding and continuous developer availability.</p>

---
