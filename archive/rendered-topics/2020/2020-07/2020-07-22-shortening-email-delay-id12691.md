# Shortening email delay

**Topic ID**: 12691
**Date**: 2020-07-22
**URL**: https://discourse.slicer.org/t/shortening-email-delay/12691

---

## Post #1 by @pieper (2020-07-22 14:31 UTC)

<p><a class="mention-group" href="/groups/admins">@admins</a> Would anyone have a problem if I change “email time window mins” to 0?</p>
<p>The reason is to shorten the response time for conversations for people (like me) who use mailing list mode.  I typically see posts via email, then open the web interface to reply.  But it would be nice to know the state of the conversation before opening the tab.</p>
<p>The purpose of the delay seems to be in order to give people a chance to edit posts before the email goes out if they accidentally hit send too soon.  But I don’t see this as a common enough thing to slow down the communications.</p>
<p>From what I can see zero seems to be a good setting for this.</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://d11a6trkgmumsb.cloudfront.net/optimized/3X/b/3/b33be9538df3547fcf9d1a51a4637d77392ac6f9_2_32x32.png" class="site-icon" width="16" height="16">
      <a href="https://meta.discourse.org/t/lag-of-10-minutes-between-posting-and-getting-email-notifications/34475/5" target="_blank" rel="noopener" title="02:18AM - 14 October 2015">Discourse Meta – 14 Oct 15</a>
  </header>
  <article class="onebox-body">
    <img src="https://d11a6trkgmumsb.cloudfront.net/original/3X/e/c/ecc92a52ee7353e03d5c0d1ea6521ce4541d9c25.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://meta.discourse.org/t/lag-of-10-minutes-between-posting-and-getting-email-notifications/34475/5" target="_blank" rel="noopener">Lag of 10+ minutes between posting and getting email notifications</a></h3>

<p>I will see if I can split the site setting up so we have:  email time window mins  and  email time window mins for email in   For now for predominantly “mail in” types sites I would strongly recommend reducing the default “10” there to “1”.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #2 by @fedorov (2020-07-22 22:16 UTC)

<p>I wish this was a per-user setting. One potentially unintended consequence of this is that if a thread is very active, this will result in a much higher frequency of email notifications, which (depending on user preferences) can be annoying.</p>

---

## Post #3 by @pieper (2020-07-22 22:39 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="2" data-topic="12691">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>this will result in a much higher frequency of email notifications,</p>
</blockquote>
</aside>
<p>I think it will be the same frequency of notifications, they will just come 10 minutes earlier, right?</p>

---

## Post #4 by @fedorov (2020-07-22 22:44 UTC)

<p>I mean, if I do a post, and then in the next 10 minutes I get 10 responses to that post, I would get 1 email notification with the current settings (which would include all 10 responses in the thread), and 10 with the updated settings (1 after each response)? Or maybe I don’t understand the setting correctly.</p>

---

## Post #5 by @pieper (2020-07-22 23:20 UTC)

<p>I haven’t tried it, but I believe that if you are in mailing list mode you will get one message notification per post in either case, just offset by this delay.</p>
<p>If you are in summary mode you will still get like one a day or every so many posts or something.</p>
<p>I believe they changed this setting for the vtk discourse because I seem to get the emails right away in mailing list mode.  This behaves like github, where watched issue emails appear right away.  I find the fast response more convenient.</p>

---

## Post #6 by @fedorov (2020-07-22 23:45 UTC)

<p>Ah, got it. In this case I am fine either way.</p>

---

## Post #7 by @pieper (2020-08-11 18:15 UTC)

<p>Hearing no other objections I’m going to try setting the delay to 0 minutes.  It means that sometimes emails will be sent even though someone goes back to edit their post, but I’ve seen that happen even with the current 10 minute delay.</p>

---
