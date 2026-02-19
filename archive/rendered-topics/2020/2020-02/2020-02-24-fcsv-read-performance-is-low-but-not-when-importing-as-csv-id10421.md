---
topic_id: 10421
title: "Fcsv Read Performance Is Low But Not When Importing As Csv"
date: 2020-02-24
url: https://discourse.slicer.org/t/10421
---

# Fcsv read performance is low (but not when importing as csv)

**Topic ID**: 10421
**Date**: 2020-02-24
**URL**: https://discourse.slicer.org/t/fcsv-read-performance-is-low-but-not-when-importing-as-csv/10421

---

## Post #1 by @muratmaga (2020-02-24 22:52 UTC)

<p>I have a fcsv file with 1000 points in it. If I load this into Slicer it takes about couple minutes to import. If I rename it to as csv, strip the first two rows, and load it (as a table), its instantaneous.</p>
<p>I assume the difference is in the creation of the mrml node(s) for fiducials?</p>

---

## Post #2 by @pieper (2020-02-24 23:15 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="10421">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I assume the difference is in the creation of the mrml node(s) for fiducials?</p>
</blockquote>
</aside>
<p>Yes, that is probably it.  We probably just need to put the scene into batch mode when reading the fcsv.  Can you post the example files so we can easily replicate?</p>

---

## Post #3 by @muratmaga (2020-02-25 00:30 UTC)

<p>Sure. here they are:<br>
csv: <a href="https://app.box.com/s/qn8lczlzm81penm0qpgzm9opdp98d7na" rel="nofollow noopener">https://app.box.com/s/qn8lczlzm81penm0qpgzm9opdp98d7na</a><br>
fcsv: <a href="https://app.box.com/s/x2x6f1m3bxg7mmtpr6te8vfqudpaub90" rel="nofollow noopener">https://app.box.com/s/x2x6f1m3bxg7mmtpr6te8vfqudpaub90</a></p>
<p>also it would be good to move text size and glyph size settings into fcsv file as well (there is already visibility setting, but as far as I can tell it doesn’t honored when fcsv is read into the scene).</p>

---

## Post #4 by @pieper (2020-02-28 20:42 UTC)

<p>I was able to reproduce the slow fiducial loading with a Slicer preview from a few weeks ago, but with the current Preview version the fcsv file loads instantly.  I suspect the overhaul <a class="mention" href="/u/lassoan">@lassoan</a> did to change to LPS coordinates also fixed this slowdown.  Let us know how it works for you <a class="mention" href="/u/muratmaga">@muratmaga</a>.</p>

---

## Post #5 by @muratmaga (2020-02-28 21:31 UTC)

<p>Yep, it is working fast for me too with the latest update. I thought you did something <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---
