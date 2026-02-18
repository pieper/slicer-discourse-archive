# Interpreting the results of ExtensionStats

**Topic ID**: 665
**Date**: 2017-07-11
**URL**: https://discourse.slicer.org/t/interpreting-the-results-of-extensionstats/665

---

## Post #1 by @fedorov (2017-07-11 15:50 UTC)

<p>I’ve been using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/ExtensionStats">ExtensionStats</a> module to get the number of downloads for Slicer extensions, and I have questions about intepreting the results this module returns.</p>
<p>What this extension returns is the number of downloads for each release type, where the following releases are available:</p>
<ul>
<li><code>pre-releases-nightly</code></li>
<li><code>&lt;release number&gt;</code></li>
<li><code>&lt;release number&gt;-nightly</code></li>
</ul>
<p>Where I am confused is this:</p>
<ol>
<li>
<p>What is <code>pre-release-nightly</code>?</p>
</li>
<li>
<p>Why do some extensions (DCMQI, for example) only list downloads for the <code>pre-release-nightly</code>? In the case of DCMQI, it was released in November 2016, in time for 4.6. I know I downloaded it at least once from the release! Also, QuantitativeReporting lists non-0 number of downloads for <code>4.6.2</code> and <code>4.6.2-nightly</code>, and it depends on DCMQI, so DCMQI must have been downloaded for each download of QuantitativeReporting, but DCMQI numbers for <code>4.6.2</code> and <code>4.6.2-nightly</code> are listed as 0.</p>
</li>
</ol>

---

## Post #2 by @lassoan (2017-07-11 17:08 UTC)

<p>I’ve added more detailed logging to the module and based on that it seems the aggregation of download counts is incorrect. It would be great if you could have a look, but if you don’t have time then I can check it later this week.</p>

---

## Post #3 by @fedorov (2017-07-11 17:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="665">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>it seems the aggregation of download counts is incorrect</p>
</blockquote>
</aside>
<p>Ooops. I should have thought about that possibility! I will update this post if I find anything, but I am running between meetings for most of the rest of the day.</p>

---

## Post #4 by @lassoan (2017-07-11 21:22 UTC)

<p>I had some time and cleaned up the download count aggregation. Please test.</p>

---

## Post #5 by @fedorov (2017-07-11 22:47 UTC)

<p>The updated version seems to produce results that make more sense. Thank you!</p>

---
