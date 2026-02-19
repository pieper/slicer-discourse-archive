---
topic_id: 25
title: "Default Settings For Discourse Users"
date: 2017-04-08
url: https://discourse.slicer.org/t/25
---

# Default settings for discourse users

**Topic ID**: 25
**Date**: 2017-04-08
**URL**: https://discourse.slicer.org/t/default-settings-for-discourse-users/25

---

## Post #1 by @lassoan (2017-04-08 14:43 UTC)

<p>(I tried to post this to the discourse config topic but new users can only post 3 messages into one topic)</p>
<p>Can we set to send responses in email by default for topics that a user posted or replied to?</p>

---

## Post #2 by @ihnorton (2017-04-09 05:00 UTC)

<p>It should be doing so already – I’ve been getting notification emails for topics I interacted with. They don’t happen immediately though, the setting <code>email time window mins</code> controls this, and is at default 10 min right now.</p>

---

## Post #3 by @lassoan (2017-04-09 09:56 UTC)

<p>Sounds good, thank you. It was not obvious for me if emails are sent or not because I was logged on the site. We should just include this piece of info in our “migration guide” for users.</p>

---

## Post #4 by @lassoan (2017-04-09 13:18 UTC)

<p>Shouldn’t we set up the default so that users get emails about all topics in Announcements?</p>

---

## Post #5 by @jcfr (2017-04-09 20:41 UTC)

<p>Is there a way to increase the number of images a user can upload ? When I tried to upload images … I could only do one at a time. May be we could increase to three images ?</p>

---

## Post #6 by @lassoan (2017-04-09 20:58 UTC)

<p>I’ve increased max image upload 1-&gt;3 and also increased max number of attachments 0-&gt;1 (in Admin / Settings / Postings). If we find that spammers take advantage of this then we can cut back the limits.</p>

---

## Post #7 by @ihnorton (2017-04-10 03:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="25" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Shouldn’t we set up the default so that users get emails about all topics in Announcements?</p>
</blockquote>
</aside>
<p>Done. The setting is <code>default categories watching</code>.</p>

---
