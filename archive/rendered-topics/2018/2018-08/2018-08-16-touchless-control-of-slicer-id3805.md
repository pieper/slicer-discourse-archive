# Touchless control of slicer

**Topic ID**: 3805
**Date**: 2018-08-16
**URL**: https://discourse.slicer.org/t/touchless-control-of-slicer/3805

---

## Post #1 by @JoeCrozier (2018-08-16 20:02 UTC)

<p>I was watching the hangout from 2/27 and the Dr’s use of touchless control of slicer in the OR fascinated me.  Here specifically: <a href="https://youtu.be/J-abcoEx2qg?t=42m11s" rel="nofollow noopener">https://youtu.be/J-abcoEx2qg?t=42m11s</a></p>
<p>Is there an extension to slicer that allows for that control?  Does anyone know how he connected everything?</p>

---

## Post #2 by @pieper (2018-08-17 13:19 UTC)

<p>Yes, there have been several attempts over the years - I’m not sure how practical it is.  Maybe someone can comment if they use this approach routinely.</p>
<p><a href="https://www.google.com/search?q=slicer+leap+motion" class="onebox" target="_blank">https://www.google.com/search?q=slicer+leap+motion</a></p>

---

## Post #3 by @lassoan (2018-08-17 14:06 UTC)

<p>You can also use a webcam and 2D barcodes to track hands or tools in space, which can be used to control Slicer. Various IMUs and MARG sensors can be connected, too. Hardware interface is provided by Plus toolkit (<a href="http://www.plustoolkit.org">www.plustoolkit.org</a>, <a href="http://www.slicerigt.org">www.slicerigt.org</a>). We have implemented some prototypes using these tools but we couldn’t find truly practical applications.</p>
<p>We use Slicer in the operating room running on Surface Pro tablets, placed in sterile bags (originally made for X-ray cassettes). This works quite well.</p>
<div class="lazyYT" data-youtube-id="90l0T1ADe_Y" data-youtube-title="Navigated breast conserving surgery" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>Wireless controllers (PowerPoint presentation controllers, X-box game controllers) placed in sterile plastic bag also work quite well in the operating room.</p>

---
