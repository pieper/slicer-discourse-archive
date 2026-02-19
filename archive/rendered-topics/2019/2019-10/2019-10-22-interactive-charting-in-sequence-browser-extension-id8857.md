---
topic_id: 8857
title: "Interactive Charting In Sequence Browser Extension"
date: 2019-10-22
url: https://discourse.slicer.org/t/8857
---

# Interactive charting in sequence Browser extension

**Topic ID**: 8857
**Date**: 2019-10-22
**URL**: https://discourse.slicer.org/t/interactive-charting-in-sequence-browser-extension/8857

---

## Post #1 by @rbahegne (2019-10-22 09:26 UTC)

<p>Hello,</p>
<p>I’m currently using the sequence extension to record a stream and i’m wondering if i could do a plot of the signal over time, a bit like in multivolume module. There is a button “Enable interactive charting” which i think should fulfill this purpose, but i’ve now clue about how it works.</p>
<p>I read the documentation (<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences</a>) but I did not fount any hint. Anyone could give me tips ?</p>
<p>Thank you.<br>
Raphaël</p>

---

## Post #2 by @lassoan (2019-10-22 12:25 UTC)

<p>You need to collapse other sections (Browsing, Synchronized nodes), to make space for Plotting section. Then click “Enable interactive charting”. If you hover over a slice viewer then the time/intensity plot will show up.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d19ed31dc8427a3b6c39e0552632a608842e7673.png" data-download-href="/uploads/short-url/tUo4rii1BxchGDcVXqjFlz2jnBV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d19ed31dc8427a3b6c39e0552632a608842e7673_2_690x387.png" alt="image" data-base62-sha1="tUo4rii1BxchGDcVXqjFlz2jnBV" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d19ed31dc8427a3b6c39e0552632a608842e7673_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d19ed31dc8427a3b6c39e0552632a608842e7673_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d19ed31dc8427a3b6c39e0552632a608842e7673_2_1380x774.png 2x" data-dominant-color="929299"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1855×1041 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @rbahegne (2019-10-24 15:14 UTC)

<p>Thank you for your answer, it’s working but i currently experiment a strange behaviour.</p>
<p>When i am plotting something in sequence browser and then change module, if i come back to sequence browser module i can’t plot anything anymore. I need to restart slicer to plot something again.</p>
<p>Have you experienced something similar ?</p>

---

## Post #4 by @lassoan (2019-10-24 20:12 UTC)

<p>Thanks for reporting this, I was able to reproduce and fix the problem. Sequences extension that you download tomorrow or later should not have this issue.</p>

---

## Post #5 by @rbahegne (2019-10-25 09:09 UTC)

<p>Thank you, Perfect !</p>

---
