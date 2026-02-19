---
topic_id: 12604
title: "2020 07 28 Hangout Early Posting For Project Week Brainstorm"
date: 2020-07-17
url: https://discourse.slicer.org/t/12604
---

# 2020.07.28 Hangout - Early Posting for Project Week Brainstorming

**Topic ID**: 12604
**Date**: 2020-07-17
**URL**: https://discourse.slicer.org/t/2020-07-28-hangout-early-posting-for-project-week-brainstorming/12604

---

## Post #1 by @Sam_Horvath (2020-07-17 19:54 UTC)

<p>Hi all:</p>
<p>This is an early announcement for the July 28th developer hangout at 10:00 AM EST until 11 AM EST.</p>
<p>We will be brainstorming ideas for what a fully virtual January project week could look like.</p>
<p>Anyone is welcome to join to ask questions at <a href="https://bit.ly/slicer-googlemeet-hosted-by-kitware" rel="nofollow noopener">https://bit.ly/slicer-googlemeet-hosted-by-kitware </a></p>
<p>Agenda:</p>
<ul>
<li>Slicer 5 progress check-in</li>
<li>Project Week Brainstorming from 10:30 on !!</li>
</ul>
<p>Feel free to post to this thread to request/suggest a topic!</p>
<p>Thanks<br>
Sam and J-Christophe</p>

---

## Post #2 by @jcfr (2020-07-27 15:09 UTC)

<p>Additional discussion topic:</p>
<ul>
<li>Concept of icon pack that could easily be swapped</li>
</ul>

---

## Post #3 by @Lee_Newberg (2020-07-28 12:36 UTC)

<p>I want small <code>all okay</code> (green check mark?), <code>warning</code>, and <code>error</code> icons for use in the Save Data Dialog box.  If there are some that are already approved for this kind of purpose, or if you have any other advice on how to get/make appropriate ones … much appreciated.</p>

---

## Post #4 by @pieper (2020-07-28 13:49 UTC)

<p>Another topic for today: does anyone have suggestions for fixing this link error?</p>
<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=1974687" class="onebox" target="_blank">http://slicer.cdash.org/viewBuildError.php?buildid=1974687</a></p>
<p>I can replicate it on my local windows release build of UKF but it’s not clear what to do about it.  UKF uses SlicerExecutionModel from the Slicer superbuild.</p>

---

## Post #5 by @jcfr (2020-07-28 18:50 UTC)

<aside class="quote no-group" data-username="Lee_Newberg" data-post="3" data-topic="12604">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lee_newberg/48/7615_2.png" class="avatar"> Lee_Newberg:</div>
<blockquote>
<p><code>warning</code> , and <code>error</code> icons for use in the Save Data Dialog box</p>
</blockquote>
</aside>
<p>See <a href="https://github.com/commontk/CTK/blob/f0bb5d7822dee7214b8458c8e2cfd4ecab756c03/Libs/Widgets/ctkErrorLogWidget.cpp#L67-L68" class="inline-onebox">CTK/Libs/Widgets/ctkErrorLogWidget.cpp at f0bb5d7822dee7214b8458c8e2cfd4ecab756c03 · commontk/CTK · GitHub</a></p>
<aside class="quote no-group" data-username="Lee_Newberg" data-post="3" data-topic="12604">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lee_newberg/48/7615_2.png" class="avatar"> Lee_Newberg:</div>
<blockquote>
<p>I want small <code>all okay</code> (green check mark?),</p>
</blockquote>
</aside>
<p>May be <code>SP_DialogOkButton</code> would work ?</p>

---
