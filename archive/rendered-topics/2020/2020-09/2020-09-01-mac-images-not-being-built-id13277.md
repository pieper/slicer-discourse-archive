---
topic_id: 13277
title: "Mac Images Not Being Built"
date: 2020-09-01
url: https://discourse.slicer.org/t/13277
---

# Mac images not being built

**Topic ID**: 13277
**Date**: 2020-09-01
**URL**: https://discourse.slicer.org/t/mac-images-not-being-built/13277

---

## Post #1 by @Alex_Vergara (2020-09-01 08:25 UTC)

<p>I have noticed that in the last three days the mac extension images are not being built</p>
<p>see:  <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2020-08-31&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Opendose" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2020-08-31&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Opendose</a></p>

---

## Post #2 by @jamesobutler (2020-09-01 19:38 UTC)

<p>On 8/31/2020 and 8/30/2020 the macOS build had a large number of core tests fail (237 and 177 respectively).  This is probably why macOS extensions were not built.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> or <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> Do you know if a certain number of failing core tests causes extensions to not be built? Or just some specific failed tests results in extensions not being built?</p>

---

## Post #3 by @Sam_Horvath (2020-09-02 02:56 UTC)

<p>So, if there are that many failing tests, it usually means that the test is failing to terminate correctly, and the tests are going to the 15 minute time-out.  This delays the entire build process, so the extension step is not reached.</p>
<p>JC and I are working on some solutions to this issue (severely shortening test timeouts, re-ordering the dashboard process, etc)</p>

---

## Post #4 by @Alex_Vergara (2020-09-02 07:18 UTC)

<p>Yesterday it was all fine</p>
<p><a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2020-09-01&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Opendose" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2020-09-01&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Opendose</a></p>

---

## Post #5 by @jamesobutler (2020-09-02 13:40 UTC)

<p>Yes, a lot were hitting that 15 minute timeout.</p>
<p>It was due to a missing library likely causing Slicer not to fully start</p>
<pre><code class="lang-auto">dyld: Library not loaded: /Volumes/D/P/S-0-build/CTK-build/CTK-build/bin/libCTKQtTesting.0.1.dylib
  Referenced from: /Volumes/D/P/S-0-build/Slicer-build/bin/Slicer.app/Contents/MacOS/./Slicer
  Reason: image not found
error: [/Volumes/D/P/S-0-build/Slicer-build/bin/Slicer.app/Contents/MacOS/./Slicer] exit abnormally - Report the problem.
</code></pre>
<p>This happened after there was a CTK update in Slicer. That update was on the 29th and then the corresponding builds on the night of the 29th (30th dashboard build date) and night of the 30th (31st dashboard build date) had the above issue. Once there was another commit to Slicer (a general Slicer update) on the 31st, then the corresponding build on the night of the 31st (Sept 1st dashboard build date) was successful.</p>
<p>Maybe something is wrong with processing a CTK update</p>

---
