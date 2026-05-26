---
topic_id: 46780
title: "New extension pull request awaiting approval"
date: 2026-04-18
url: https://discourse.slicer.org/t/46780
last_bumped: 2026-04-22T16:58:12.266Z
---

# New extension pull request awaiting approval

**Topic ID**: 46780
**Date**: 2026-04-18
**URL**: https://discourse.slicer.org/t/new-extension-pull-request-awaiting-approval/46780

---

## Post #1 by @MaxHoges (2026-04-18 09:14 UTC)

<p>I recently got my BoneMat extension to a useful state and decided to try adding it to the extensions index. My first pull request to the ExtensionsIndex didn’t pass the extension validation test (which was initiated by a maintainer), so I fixed the issue and resubmitted it. I was waiting on a maintainer to approve the other 2 workflows that need to happen for about a week, in which time I’d made other significant changes, so I closed that pull request and opened a new one ( <a href="https://github.com/Slicer/ExtensionsIndex/pull/2336" class="inline-onebox" rel="noopener nofollow ugc">Add BoneMat extension by MaxHoges · Pull Request #2336 · Slicer/ExtensionsIndex · GitHub</a> ).</p>
<p>I’ve been waiting for a couple days for this maintainer approval, and was happy to wait for longer as I thought the Slicer maintainers were rightfully busy. However, a new extension’s pull request was submitted today and got approval fairly quickly, which is why I’ve come to the forum.</p>
<p>Is there anything I need to do on my end after the AI-analysis was successful for those other workflows to run? My other thought is that my extension’s need for approval was somehow missed after the first round of approved workflows failed, and the resubmission just didn’t raise any flags. Any guidance here would be appreciated.</p>

---

## Post #2 by @pieper (2026-04-19 19:05 UTC)

<p>Thanks for raising this and for your patience.  We’re not ignoring anyone on purpose, it’s more that reviewing and approving extensions is a bit of a chore that’s not directly funded by any actively funded project so there can be a backlog.</p>
<p>We are a bit cautious because accepting extensions probably implies to some people that we “vouch” for the code in some way, but of course we can’t know exactly what all the code is doing and we don’t perform any kind of developer vetting the way something like the Apple or Microsoft stores would do.</p>
<p>We plan to discuss this on Tuesday’s developer call.  There’s a thread here with some ideas about how we might be able to make the process easier for everyone.</p>
<aside class="quote" data-post="3" data-topic="46731">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/2026-04-14-weekly-meeting/46731/3">2026.04.14 Weekly Meeting</a> <a class="badge-category__wrapper " href="/c/community/hangout/20"><span data-category-id="20" style="--category-badge-color: #12A89D; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #F7941D;" data-parent-category-id="12" data-drop-close="true" class="badge-category --style-square --has-parent" title="This category is used to announce hangouts and organize associated notes."><span class="badge-category__name">Weekly meetings</span></span></a>
    </div>
  </div>
  <blockquote>
    Here’s something we can discuss at the next meeting: <a href="https://github.com/Slicer/ExtensionsIndex/issues/2341" class="inline-onebox">Add a feature to make it easy to install extension PRs · Issue #2341 · Slicer/ExtensionsIndex · GitHub</a> 
BTW, maybe we should have a “next meeting” thread dedicated to posting agenda items for upcoming developer calls.  Currently we post back to the meeting announcement, but sometimes, like this, I want to make a note in advance.
  </blockquote>
</aside>


---

## Post #3 by @MaxHoges (2026-04-20 05:36 UTC)

<p>I appreciate the response Steve, it’s completely understandable. Thank you for re-running the checks on my extension after this.</p>
<p>Now that the extension is passing all the checks, are there any other barriers to merging it? Could I do it myself, or is that left to the maintainers? I couldn’t find anything in the documentation/forum of what the protocol is at this point, but I think from previous merge commits which were made only by maintainers I’m not supposed to do it myself?</p>

---

## Post #4 by @pieper (2026-04-21 17:53 UTC)

<p>We talked about this at today’s dev meeting.  We are going to publish a set of review criteria so that all reviewers follow more or less the same process and so extension developers and users know what to expect.</p>
<p>One very good suggestion was for extension developers to drop in at a weekly meeting to demo their extension - this is likely the best way to get timely feedback and action.</p>
<p>For BoneMat in particular, I merged the PR today so it should show up for testing in tomorrows builds.</p>
<p>Also note that as Slicer maintainers, we are actively looking for lighter weight ways for users and extension developers to work with each other without use being the bottleneck.</p>

---

## Post #5 by @muratmaga (2026-04-22 16:58 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="46780">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>was for extension developers to drop in at a weekly meeting to demo their extension - this is likely the best way to get timely feedback and action.</p>
</blockquote>
</aside>
<p>While I agree this is probably good thing to do, I would discourage this being a mandatory expectation (ie., your review goes to the bottom of the pool, if you don’t attend). I have been in Slicer community for over a decada, and I was able to attend maybe a handful developer meetings due the time difference.</p>

---
