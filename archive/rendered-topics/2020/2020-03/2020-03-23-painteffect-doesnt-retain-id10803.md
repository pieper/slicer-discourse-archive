# PaintEffect doesn't retain

**Topic ID**: 10803
**Date**: 2020-03-23
**URL**: https://discourse.slicer.org/t/painteffect-doesnt-retain/10803

---

## Post #1 by @orchid (2020-03-23 19:20 UTC)

<p>Hello,<br>
I am a newbie for 3D Slicer. I have 4.10.0 version.<br>
I use ‘Threshold effect’ to get the majority of my model and then try to use ‘PaintEffect’ to pick up the ones I missed. I have checked ‘sphere’ and ‘threshold paint’ option, select a diameter and started tracing/painting. I see the trace but when I release the mouse or pen, the trace are gone. I am not sure what I missed. Please advise.</p>
<p>Thank you.</p>

---

## Post #2 by @muratmaga (2020-03-23 19:22 UTC)

<p>4.10.0 is fairly old. Try with a newer preview builds and if you have to use 4.10 stream, then try downloading the latest stable 4.10.2</p>

---

## Post #3 by @lassoan (2020-03-23 20:22 UTC)

<p>Most probably you have restricted the “Editable intensity range” (by clicking “Use for masking” in Threshold effect). Uncheck “Editable intensity range” in Masking section at the bottom to enable painting everywhere.</p>

---

## Post #4 by @orchid (2020-03-23 21:12 UTC)

<p>Thank you, <a class="mention" href="/u/muratmaga">@muratmaga</a>. I just downloaded the latest version.</p>

---

## Post #5 by @orchid (2020-03-23 21:14 UTC)

<p>Thank you so much, Andras!<br>
I tried your suggestion and I was able to paint nown <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>

---
