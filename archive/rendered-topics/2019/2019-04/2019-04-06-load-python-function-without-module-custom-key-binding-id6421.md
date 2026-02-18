# Load python function without module; custom key binding

**Topic ID**: 6421
**Date**: 2019-04-06
**URL**: https://discourse.slicer.org/t/load-python-function-without-module-custom-key-binding/6421

---

## Post #1 by @chir.set (2019-04-06 17:26 UTC)

<p>I have found the <a href="https://discourse.slicer.org/t/synchronize-display-scale-across-slice-viewers/4547/5">toggleZoomSync()</a> user function quite useful. It works very well in the Python interactor.</p>
<p>I wish to load it on start without creating a GUI module/extension. And also, create a keyboard shorcut (Meta+Z on Linux) for quick access. I don’t wish any GUI widget to use that function.</p>
<p>I should be able to create a module with the Extension Wizard if it can’t be avoided. I could find no documentation to create a custom key binding however.</p>
<p>Can you please advise ?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2019-04-06 17:29 UTC)

<p>This example should answer all your questions:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_keyboard_shortcuts" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_keyboard_shortcuts</a></p>

---

## Post #3 by @chir.set (2019-04-06 18:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="6421">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This example should answer all your questions:</p>
</blockquote>
</aside>
<p>Yes, both questions are resolved.</p>
<p>Thank you very much.</p>

---
