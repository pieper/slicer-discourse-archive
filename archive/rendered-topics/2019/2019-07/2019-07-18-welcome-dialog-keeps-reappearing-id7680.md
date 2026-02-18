# Welcome dialog keeps reappearing

**Topic ID**: 7680
**Date**: 2019-07-18
**URL**: https://discourse.slicer.org/t/welcome-dialog-keeps-reappearing/7680

---

## Post #1 by @chir.set (2019-07-18 19:10 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="8" data-topic="7656">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"><a href="https://discourse.slicer.org/t/problem-in-slicer/7656/8">Problem in slicer</a></div>
<blockquote>
<p>If you check the don’t show again checkbox and start Slicer then the dialog should not appear. Can you confirm this?</p>
</blockquote>
</aside>
<p>A brief intrusion in this thread.</p>
<p>The ‘Don’t show again and always OK’ checkbox does not work on Slicer at start and on exit, if no old configuration directory exists. At least on Linux.<br>
You may test after</p>
<blockquote>
<p>mv $HOME/.config/NA-MIC $HOME/.config/NA-MIC.bak</p>
</blockquote>

---

## Post #2 by @chir.set (2019-07-18 19:23 UTC)

<aside class="quote no-group quote-modified" data-username="chir.set" data-post="10" data-topic="7656">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"><a href="https://discourse.slicer.org/t/problem-in-slicer/7656/10">Problem in slicer</a></div>
<blockquote>
<p>does not work on Slicer at start and on exit</p>
</blockquote>
</aside>
<p>I mean, the dialog is shown everytime Slicer starts and exits, even if the checkbox is ticked. But it does not crash.</p>

---

## Post #3 by @lassoan (2019-07-19 04:37 UTC)

<p>Could you check If the <code>Slicer.ini</code> configuration file already exists, does the “don’t show again” setting properly saved in it?</p>
<p>By default the <code>Slicer.ini</code> file should contain <code>DontShowDisclaimerMessage=-1</code> and if you click don’t show checkbox and OK then it should change to <code>DontShowDisclaimerMessage=1024</code>.</p>

---

## Post #4 by @chir.set (2019-07-19 06:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="7680">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>the <code>Slicer.ini</code> file should contain <code>DontShowDisclaimerMessage</code></p>
</blockquote>
</aside>
<p>DontShowDisclaimerMessage is <em>always</em> missing in Slicer.ini, when this file is created in an empty configuration directory.</p>

---
