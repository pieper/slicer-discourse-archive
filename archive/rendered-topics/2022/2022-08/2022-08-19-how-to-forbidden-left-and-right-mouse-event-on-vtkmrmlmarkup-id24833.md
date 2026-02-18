# How to forbidden left and right mouse event on vtkMRMLMarkupsLineNode

**Topic ID**: 24833
**Date**: 2022-08-19
**URL**: https://discourse.slicer.org/t/how-to-forbidden-left-and-right-mouse-event-on-vtkmrmlmarkupslinenode/24833

---

## Post #1 by @jay1987 (2022-08-19 13:27 UTC)

<p>i made a line node like the picture<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8264fe08e98637c8d6a54adf4cf7978b3976b79b.png" alt="image" data-base62-sha1="iBwrFfbdSdNwllSMtXIeJp0rX9V" width="347" height="287"><br>
and i want the line node to not react on mouse left and mouse right event<br>
how to do it in the C++ or python Code?</p>

---

## Post #2 by @Sunderlandkyl (2022-08-19 15:26 UTC)

<p>You can lock the markups node to prevent interaction.</p>
<h4><a name="p-82242-from-the-markups-module-1" class="anchor" href="#p-82242-from-the-markups-module-1" aria-label="Heading link"></a>From the Markups module:</h4>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03538f036ec032e49be2c58b72b5bfb1e30f6363.png" alt="image" data-base62-sha1="tqsgNZYOpWW3J4QWXjha2ZZT7J" width="245" height="66"></p>
<h4><a name="p-82242-from-pythonc-2" class="anchor" href="#p-82242-from-pythonc-2" aria-label="Heading link"></a>From Python/C++:</h4>
<pre data-code-wrap="python"><code class="lang-python">getNode("MarkupsLine").SetLocked(True)
</code></pre>

---

## Post #3 by @jay1987 (2022-08-20 02:37 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="2" data-topic="24833">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p><code>SetLocked(True)</code></p>
</blockquote>
</aside>
<p>thank you ,it’s very useful for me</p>

---
