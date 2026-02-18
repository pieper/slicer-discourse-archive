# Download.slicer.org and extension catalogue seems slows

**Topic ID**: 10835
**Date**: 2020-03-25
**URL**: https://discourse.slicer.org/t/download-slicer-org-and-extension-catalogue-seems-slows/10835

---

## Post #1 by @muratmaga (2020-03-25 16:38 UTC)

<p>I am not sure if it is my connection or just the server busy, but it takes a while to get a response. Once it starts downloading, speeds seems normal though…</p>

---

## Post #2 by @pieper (2020-03-25 17:00 UTC)

<p>Yes, I noticed that too.  I wonder if with the new versioning scheme the query is returning more matches or something like that.</p>

---

## Post #3 by @mhalle (2020-03-25 17:50 UTC)

<p>I’m seeing 0.5 second response to a hard reload of <a href="https://download.slicer.org" rel="nofollow noopener">https://download.slicer.org</a>, loading 130KB. There’s no dynamic query happening; the server is generating the HTML from a local sqlite db.  Midas queries happen separately on the backend and only every few hours or so.</p>
<p>If the extension catalog is also slow, then its probably something else, since <a href="http://download.slicer.org" rel="nofollow noopener">download.slicer.org</a> and the extension manager don’t use any shared front-end.</p>
<p>—Mike</p>

---

## Post #4 by @pieper (2020-03-25 18:03 UTC)

<p>Thanks Mike.</p>
<p>For me it was the extension manager taking a while to come up.</p>

---

## Post #5 by @jcfr (2020-03-25 18:11 UTC)

<p>Looking at the network performance associated with page like this one (loaded in the extension manager):</p>
<p><a href="https://slicer.kitware.com/midas3/slicerappstore?os=win&amp;arch=amd64&amp;revision=28879&amp;category=&amp;search=&amp;layout=empty" class="onebox" target="_blank" rel="noopener">https://slicer.kitware.com/midas3/slicerappstore?os=win&amp;arch=amd64&amp;revision=28879&amp;category=&amp;search=&amp;layout=empty</a></p>
<p>with cached assets (similar time after discarding the cache) is ~2s</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c0c4dd86e7d9bb4cc78440ff7589be0331a3c06.png" alt="image" data-base62-sha1="d8ihTBynKu3zMUCVZCD89Gtowaa" width="368" height="244"></p>

---

## Post #6 by @pieper (2020-03-25 18:43 UTC)

<p>Yes, that site comes up quickly for me.  I think the issue was opening the extension manager window after a fresh install.  Is anyone else seeing that?</p>

---

## Post #7 by @lassoan (2020-03-25 18:50 UTC)

<p>Slow startup of extension manager on Mac is most likely due to that the executables are not signed. You can easily self-sign the application to see if it fixes the issue. See details here: <a href="https://github.com/Slicer/Slicer/issues/4724">https://github.com/Slicer/Slicer/issues/4724</a></p>
<p>Is only the first loading is slow, or reloads are slow, too?</p>
<p>Does the <a href="http://slicer.kitware.com/midas3/slicerappstore?os=win&amp;arch=amd64&amp;revision=28879&amp;category=&amp;search=&amp;layout=layout">app store page</a> load slowly in a regular Chrome browser, too?</p>

---

## Post #8 by @pieper (2020-03-25 19:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="10835">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does the <a href="http://slicer.kitware.com/midas3/slicerappstore?os=win&amp;arch=amd64&amp;revision=28879&amp;category=&amp;search=&amp;layout=layout">app store page</a> load slowly in a regular Chrome browser, too?</p>
</blockquote>
</aside>
<p>Yes, that is very slow.  The page comes up but the wait animation “Loading extensions” is up for several minutes so far.</p>
<p>Looking at the networking tab of the chrome developer tools it says the list extensions request is pending (the form data looks right).</p>

---

## Post #9 by @lassoan (2020-03-25 19:30 UTC)

<p>Interestingly the app store link I included above loaded in a few seconds at that time (40 minutes ago), but now it has been loading for several minutes and extensions still haven’t showed up. Probably it’s just the usual unpredictability of the ancient Midas server.</p>

---

## Post #10 by @jamesobutler (2020-03-25 20:18 UTC)

<p>Yesterday morning I had poor response when trying to download the Windows Slicer Preview from I believe both the cdash uploaded package URL and the link from <a href="http://download.slicer.org" rel="nofollow noopener">download.slicer.org</a> which is something like  <a href="https://download.slicer.org/bitstream/1222761" rel="nofollow noopener">https://download.slicer.org/bitstream/1222761</a>. If these requests are both served by the Midas server then I would think that is the culprit.</p>

---

## Post #11 by @pieper (2020-03-25 20:19 UTC)

<p>Yes, it took 8.9 minutes to load in one of my tests.  Other times it’s nearly instant.</p>

---

## Post #12 by @mhalle (2020-03-25 20:38 UTC)

<p><a href="https://download.slicer.org/bitstream/1222761" rel="nofollow noopener">https://download.slicer.org/bitstream/1222761</a> is literally a redirect to Midas. <a href="http://download.slicer.org" rel="nofollow noopener">download.slicer.org</a> never handles the bits.</p>
<p>The redirect is instantaneous.</p>
<p>—Mike</p>

---

## Post #13 by @lassoan (2020-03-25 21:08 UTC)

<p><a href="http://download.slicer.org">download.slicer.org</a> page is very fast and reliable - thank you Mike! Sometimes the package download takes a few minutes instead of a few ten seconds, but that’s still fine.</p>
<p>The problem is with the extension download page (<a href="http://slicer.kitware.com/midas3/slicerappstore">http://slicer.kitware.com/midas3/slicerappstore</a>). Right now, the <a href="http://slicer.kitware.com/midas3/slicerappstore?os=win&amp;arch=amd64&amp;revision=28879&amp;category=&amp;search=&amp;layout=layout">page with specified revision</a> usually loads within seconds, <a href="http://slicer.kitware.com/midas3/slicerappstore">page without revision</a> usually loads within a minute. However, sometimes loading takes several minutes or more (or times out).</p>
<p>What might be a recent regression is that <a href="http://slicer.kitware.com/midas3/slicerappstore">http://slicer.kitware.com/midas3/slicerappstore</a> takes a really long time to load (but when we specify a revision then the page loads within seconds). <a class="mention" href="/u/jcfr">@jcfr</a> could the few very high revision numbers that showed up this week affect the latest revision detection mechanism of the page?</p>

---

## Post #14 by @jcfr (2020-03-26 17:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="10835">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>could the few very high revision numbers that showed up this week affect the latest revision detection mechanism of the page?</p>
</blockquote>
</aside>
<p>While I removed the offending packages, I will remote connect to the database and manually inspect the tables.</p>

---

## Post #15 by @jamesobutler (2020-05-03 19:20 UTC)

<p>Just wanted to report that upon trying to download the Slicer preview from the main download page today at 3:12 pm EST, that it got stuck with “Waiting for <a href="http://slicer.kitware.com" rel="nofollow noopener">slicer.kitware.com</a>…” for a long time.  I ended up reloading the webpage and trying again and actually recording the time it would take to begin serving the download.  It took 1 min 45 seconds to actually begin downloading. This was on my home internet which is stable and once it started downloading the ~200MB package it finished in like 4 seconds because of my download speeds.  Faster response to begin serving the download would be greatly appreciated.</p>

---

## Post #16 by @lassoan (2020-05-04 03:23 UTC)

<p>Thanks for reporting this. It is an open issue - see <a href="https://github.com/Slicer/Slicer/issues/4806">here</a> - I’ve added your comment to it.</p>

---
