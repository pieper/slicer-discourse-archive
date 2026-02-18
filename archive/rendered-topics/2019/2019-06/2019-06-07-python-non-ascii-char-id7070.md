# Python non ascii char

**Topic ID**: 7070
**Date**: 2019-06-07
**URL**: https://discourse.slicer.org/t/python-non-ascii-char/7070

---

## Post #1 by @Mr.wyr (2019-06-07 14:08 UTC)

<p>how can i use chinese in python character, i add <span class="hashtag">#coding:utf-8</span> in top, but it’s not work</p>

---

## Post #2 by @lassoan (2019-06-07 16:47 UTC)

<p>Unicode support in Slicer is limited. It is supported at Python and Qt level, so it is possible to display Unicode characters to the users.</p>
<p>See these pages for details:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/slicer-internationalization/579" class="inline-onebox">Slicer Internationalization</a></li>
<li>
<a href="https://projectweek.na-mic.org/PW30_2019_GranCanaria/Projects/UltrasoundSimulatorTraining/" rel="nofollow noopener">https://projectweek.na-mic.org/PW30_2019_GranCanaria/Projects/UltrasoundSimulatorTraining/</a> (see “Background and references” section for source code of a multi-language module)</li>
</ul>

---

## Post #3 by @Mr.wyr (2019-06-08 01:34 UTC)

<p>I know Slicer internationalization,but it’s incomplete,i would like to translate SegmentEditorThresholdEffect.py，in SegmentEditorThresholdEffect.py, for example line 121, qt.QLabel(“Threshold Range:”), i would like to translate “Threshold Range” to chinese</p>

---

## Post #4 by @jcfr (2019-06-08 21:56 UTC)

<aside class="quote no-group" data-username="Mr.wyr" data-post="3" data-topic="7070">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mr.wyr/48/3347_2.png" class="avatar"> Mr.wyr:</div>
<blockquote>
<p>Slicer internationalization,but it’s incomplete</p>
</blockquote>
</aside>
<p>We have plan to work on improving the support for i18n during the upcoming <a href="https://projectweek.na-mic.org/PW31_2019_Boston/#infrastructure">project week in Boston</a>, that said if you can allocate some resources to support this work I suggest you look at the <a href="https://www.slicer.org/wiki/CommercialUse#Commercial_Partners">commercial partners</a>.</p>

---
