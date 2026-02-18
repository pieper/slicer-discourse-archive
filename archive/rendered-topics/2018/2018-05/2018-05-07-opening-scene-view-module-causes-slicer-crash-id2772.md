# Opening Scene View module causes Slicer Crash

**Topic ID**: 2772
**Date**: 2018-05-07
**URL**: https://discourse.slicer.org/t/opening-scene-view-module-causes-slicer-crash/2772

---

## Post #1 by @Sam_Horvath (2018-05-07 22:21 UTC)

<p>Operating System - Windows 10<br>
Slicer version- 5/04/2018 nightly</p>
<p>Opening the Scene Views module (with or without data loaded) causes Slicer to crash.</p>

---

## Post #2 by @pieper (2018-05-08 00:00 UTC)

<p>Thanks for the report - this is actually already a known issue but it hasn’t been looked into yet:</p>
<p><a href="https://issues.slicer.org/view.php?id=4508" class="onebox" target="_blank">https://issues.slicer.org/view.php?id=4508</a></p>
<p>As an aside <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> do you use SceneViews in your work?  They have proven to be a problematic feature and we have been thinking they may need to be re-implemented (or removed?) at some point.</p>

---

## Post #3 by @Sam_Horvath (2018-05-08 02:36 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>, I do not currently use them.  I was looking into the module mainly because I hadn’t ever done anything with it.  I’m working on a surgical planning project where we need to generate a step by step instruction list based on actions performed in the Slicer-based planner.  We will be using screenshots as the main way to capture changes from one state to the next, but I was wondering if anything in Scene Views would be useful.</p>

---

## Post #4 by @pieper (2018-05-08 12:04 UTC)

<p>Thanks for the feedback – yes, SceneViews could potentially be useful in those scenarios.  You could play with it in 4.8.1 to see if it seems workable (there are several corner cases that have led to headaches over the years and I’m not sure they were all resolved).</p>
<p>A workaround could be to save separate scene (.mrb) at each step and have the user close the scene and open a new one to get to a particular step.</p>

---

## Post #5 by @lassoan (2018-08-24 17:58 UTC)

<p>Scene views module has been recently fixed in Slicer-4.9.</p>

---
