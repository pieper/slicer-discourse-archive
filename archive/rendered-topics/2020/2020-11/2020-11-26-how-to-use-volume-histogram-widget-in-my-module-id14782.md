---
topic_id: 14782
title: "How To Use Volume Histogram Widget In My Module"
date: 2020-11-26
url: https://discourse.slicer.org/t/14782
---

# How to use volume histogram widget in my module

**Topic ID**: 14782
**Date**: 2020-11-26
**URL**: https://discourse.slicer.org/t/how-to-use-volume-histogram-widget-in-my-module/14782

---

## Post #1 by @ond12 (2020-11-26 08:58 UTC)

<p>Hello,</p>
<p>I want to add the “Histogram” in my module <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74cb67fef0eea7af975025f31a50576d8e1927aa.png" alt="histoslicer" data-base62-sha1="gFdbjdn3KS7AkOXzbxfdt1mcmb8" width="545" height="369"></p>
<p>I find the module UI use a " ctkCollapsibleGroupBox" and inside a " ctkTransfertFunctionView" but it’s does not work in my module.</p>
<p>Can you help me, how can i add this same histogram in my own module ?</p>
<p>Thanks</p>

---

## Post #2 by @cpinter (2020-11-26 09:37 UTC)

<aside class="quote no-group" data-username="ond12" data-post="1" data-topic="14782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ond12/48/8706_2.png" class="avatar"> ond12:</div>
<blockquote>
<p>but it’s does not work in my module</p>
</blockquote>
</aside>
<p>We need more information about this part in order to help.</p>
<p>For starters, I’d suggest taking a look at how the transfer function view is used in the widget in Slicer: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Volumes/Widgets/qSlicerScalarVolumeDisplayWidget.cxx#L69-L70" class="inline-onebox">Slicer/Modules/Loadable/Volumes/Widgets/qSlicerScalarVolumeDisplayWidget.cxx at main · Slicer/Slicer · GitHub</a></p>

---
