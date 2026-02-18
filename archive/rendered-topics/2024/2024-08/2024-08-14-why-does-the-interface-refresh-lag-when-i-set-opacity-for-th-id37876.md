# Why does the interface refresh lag when I set opacity for the display node

**Topic ID**: 37876
**Date**: 2024-08-14
**URL**: https://discourse.slicer.org/t/why-does-the-interface-refresh-lag-when-i-set-opacity-for-the-display-node/37876

---

## Post #1 by @fl_wang (2024-08-14 07:53 UTC)

<p>femurClipedDisplayNode-&gt;SetOpacity(0.6);<br>
tibiaClipedDisplayNode-&gt;SetOpacity(0.6);</p>

---

## Post #2 by @rfenioux (2024-08-19 09:17 UTC)

<p>you can try <code>slicer.app.processEvents()</code> to process pending GUI events</p>

---
