---
topic_id: 6505
title: "Slicerelastix Not Compatible With Nightly"
date: 2019-04-15
url: https://discourse.slicer.org/t/6505
---

# SlicerElastix not compatible with nightly

**Topic ID**: 6505
**Date**: 2019-04-15
**URL**: https://discourse.slicer.org/t/slicerelastix-not-compatible-with-nightly/6505

---

## Post #1 by @Alex_Vergara (2019-04-15 15:35 UTC)

<p>When installing SlicerElastix it says</p>
<p>File “/Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py”, line 330<br>
print e<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(e)?</p>

---

## Post #2 by @lassoan (2019-04-15 15:43 UTC)

<p>Thanks for reporting this. Slicer core has been upgraded to Python3 but most extensions have not been made Python3 compatible yet.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> are you going to submit a pull request for SlicerElastix? In general, do you plan to send pull requests for most extensions?</p>

---

## Post #3 by @Alex_Vergara (2019-04-15 15:46 UTC)

<p>I am very happy for the python3 upgrade <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"> Now the bundled python can release the GIL and numpy runs in multiprocessing using several cores.</p>

---

## Post #4 by @jcfr (2019-04-15 23:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="6505">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>are you going to submit a pull request for SlicerElastix?</p>
</blockquote>
</aside>
<p>SlicerElastix has been updated to support Python3.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="6505">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>In general, do you plan to send pull requests for most extensions?</p>
</blockquote>
</aside>
<p>This will happen on “as needed” basis.</p>

---

## Post #5 by @lassoan (2019-04-16 01:03 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="6505">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>SlicerElastix has been updated to support Python3.</p>
</blockquote>
</aside>
<p>Great, thank you!</p>
<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="6505">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>This will happen on “as needed” basis.</p>
</blockquote>
</aside>
<p>Do you mean we can ask for your help whenever we want to upgrade an extension to be compatible with Python3?</p>

---
