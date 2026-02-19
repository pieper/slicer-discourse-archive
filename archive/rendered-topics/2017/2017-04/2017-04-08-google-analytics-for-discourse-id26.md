---
topic_id: 26
title: "Google Analytics For Discourse"
date: 2017-04-08
url: https://discourse.slicer.org/t/26
---

# Google analytics for discourse

**Topic ID**: 26
**Date**: 2017-04-08
**URL**: https://discourse.slicer.org/t/google-analytics-for-discourse/26

---

## Post #1 by @lassoan (2017-04-08 18:48 UTC)

<p>Should we set up Google analytics? It would be great to know how many readers the forum has and from where.</p>
<p>I’ve found some settings here:<br>
<a href="https://discourse.slicer.org/admin/site_settings/category/basic" class="onebox" target="_blank">https://discourse.slicer.org/admin/site_settings/category/basic</a></p>

---

## Post #2 by @pieper (2017-04-08 20:17 UTC)

<p>The dashboard already looks pretty helpful.  Google analytics would add some extra features I’m sure.</p>

---

## Post #3 by @ihnorton (2017-04-09 05:20 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/thumbsup.png?v=5" title=":thumbsup:" class="emoji" alt=":thumbsup:"> it might make sense to put under a general <a href="http://slicer.org">slicer.org</a> analytics account (if one already exists) so that we can have a sense of whether people find the forum, broader bounce rate, etc.</p>

---

## Post #4 by @pieper (2017-04-09 15:31 UTC)

<p>Good point <a class="mention" href="/u/ihnorton">@ihnorton</a>, I know we discussed google analytics at some point in the na-mic era but I don’t know if was ever implemented.  I posted a question on the equality-tech support discourse site to see if it’s set up on the new slicer wiki instance.   From a look at the <a href="http://slicer.org">slicer.org</a> pages I think that it is not currently set up anywhere.</p>

---

## Post #5 by @ihnorton (2017-04-10 14:56 UTC)

<p>Mike pointed out that GA has had issues in the past for users in China. Per recent articles it is supposed to work fine now, but something to be aware of.</p>
<p>I didn’t see any analytics running on <a href="http://slicer.org">slicer.org</a>, so I set up a new account and added people as owners/admins. After creating the analytics account, simple had to set the tracking code in the setting <code>ga universal tracking code</code> (per <a href="https://meta.discourse.org/t/google-analytics-setting-configuration/46466">here</a>).</p>
<p>Once I disabled uBlock on <a href="http://discourse.slicer.org">discourse.slicer.org</a>, my session showed in the analytics realtime dashboard immediately.</p>
<p>Note: if you use uBlock or adBlock etc., <a href="http://google.com/analytics">google.com/analytics</a> also needs to be white-listed in order for the admin page to load. (no small irony there <img src="https://emoji.discourse-cdn.com/twitter/pensive.png?v=9" title=":pensive:" class="emoji" alt=":pensive:">)</p>
<p>There’s also a newer thing called Google Tag Manager, which is harder to block, but I didn’t set that up (yet, at least).</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://d11a6trkgmumsb.cloudfront.net/optimized/3X/b/3/b33be9538df3547fcf9d1a51a4637d77392ac6f9_2_32x32.png" class="site-icon" width="32" height="32">
      <a href="https://meta.discourse.org/t/setup-google-tag-manager-for-analytics/47335" target="_blank" title="09:34PM - 14 July 2016">Discourse Meta – 14 Jul 16</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:640/500;"><img src="https://d11a6trkgmumsb.cloudfront.net/optimized/3X/0/6/06b09784b2dc263c550c985f159c4bd41574156a_2_1024x799.png" class="thumbnail" width="640" height="500"></div>

<h3><a href="https://meta.discourse.org/t/setup-google-tag-manager-for-analytics/47335" target="_blank">Setup Google Tag Manager for Analytics</a></h3>

<p>Support for Google Tag Manager was added today! This howto will show you how to use Google Universal Analytics through Google Tag Manager. After you’re done, the Google Tag Manager API will be running on your Discourse site, so you could in theory...</p>

  <p><span class="label1">Reading time: 9 mins 🕑</span>
    <span class="label2">Likes: 92 ❤</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @pieper (2017-04-13 17:27 UTC)

<p>Here’s what I heard back from Greg about analytics on the wiki.  I think it’s a great idea to implement this on both discourse and wiki using whatever system people prefer.  GA would be the default option in my mind unless someone know differently or wants to do the research.</p>
<blockquote>
<p>Hi Steve,</p>
</blockquote>
<blockquote>
<p>It’s not setup yet. I just need to know your GA code.</p>
</blockquote>
<blockquote>
<p>I recommend the approach described at <a href="https://www.mediawiki.org/wiki/User:Dantman/Analytics_integration" class="inline-onebox">User:Dantman/Analytics integration - MediaWiki</a> The short version is that I would add your GA code to the <a href="http://slicer.org">slicer.org</a> wiki configuration file (LocalSettings.php).</p>
</blockquote>
<blockquote>
<p>There are some other interesting analytics options like Piwik or Open Web Analytics if you’re curious.</p>
</blockquote>

---

## Post #7 by @lassoan (2017-04-13 17:43 UTC)

<p>A few weeks ago I’ve spent a couple of hours with checking what web analytics services are available. For me it seems that GA is by far the most sophisticated system and it gives a lot for free (much more than most paid service).<br>
It can also be used to track mobile apps and desktop applications usage (it has an API just for this purpose, which doesn’t require javascript).</p>

---

## Post #8 by @ihnorton (2017-04-13 18:25 UTC)

<p>In case someone wants to look at this, there’s a GA account called “Slicer Analytics”, and it is active for this subdomain (we’ve had ~80 uniques). I added <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> as managers for the account when I set it up, and we can add anyone else if needed.</p>
<p>I think you can just go to <a href="https://analytics.google.com">https://analytics.google.com</a> and log in, it should show up in the list of accounts.</p>

---

## Post #9 by @lassoan (2017-04-13 18:40 UTC)

<p>Thank you for setting up GA, it’s awesome. With this we’ll be able to get to know user base much better!</p>

---

## Post #10 by @pieper (2017-04-13 18:42 UTC)

<p>Yes, the analytics is working well - interesting to see what cities show up in the top ten so far : D</p>
<p><a class="mention" href="/u/ihnorton">@ihnorton</a> do you know the GA code to send to Greg?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/127dfabbca4ea9a7e417137c260b8d4bc4e37688.png" alt="image" data-base62-sha1="2DAvfWvdxHL5xf3KwkremycDUg0" width="671" height="379"></p>

---

## Post #11 by @ihnorton (2017-04-13 19:18 UTC)

<p><code>UA-97117718-1</code>, at least for <a href="http://discourse.slicer.org">discourse.slicer.org</a>. I’m not sure if we should use that, or set up a different one for the top level – when I looked in to this very briefly, it seemed like there were some extra configuration steps required to make a subdomain and top-level work correctly in the stats.</p>
<p>We could also add Greg to the analytics account if he’s going to be setting it up.</p>

---

## Post #12 by @pieper (2017-04-18 14:41 UTC)

<p>I passed this over to Greg.</p>

---

## Post #13 by @pieper (2017-04-20 16:05 UTC)

<p>We now have analytics that includes the forum and the rest of <a href="http://slicer.org">slicer.org</a> (at least static and wiki content).  Over 4,000 page views yesterday.  Lots of other stuff to explore for anyone interested.</p>

---

## Post #14 by @ihnorton (2017-04-20 16:26 UTC)

<p>Well that explains the huge spike! It isn’t obvious to me how to disaggregate the discourse traffic, but I guess we have a decent idea of that from the dashboard.</p>

---

## Post #15 by @pieper (2017-04-20 19:04 UTC)

<p>I don’t see an obvious way to filter the pageviews between <a href="http://slicer.org">slicer.org</a> and <a href="http://discourse.slicer.org">discourse.slicer.org</a>. Maybe that’s not a problem since the discourse dashboard can give us metrics about the forum and the google analytics can be about our web presence as a whole.</p>

---
