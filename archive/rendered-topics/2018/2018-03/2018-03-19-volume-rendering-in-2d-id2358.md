# Volume Rendering in 2D

**Topic ID**: 2358
**Date**: 2018-03-19
**URL**: https://discourse.slicer.org/t/volume-rendering-in-2d/2358

---

## Post #1 by @brhoom (2018-03-19 11:59 UTC)

<ul>
<li>
<p>Is it possible to display 3D rendering in the 2D views (Axial, Coronal and Sagittal) e.g. the Maximum Intensity<br>
Projection MIP?</p>
</li>
<li>
<p>Another question, why there is no “None” Preset? after selecting a specific preset I can not go back to the default.</p>
</li>
</ul>

---

## Post #2 by @chir.set (2018-03-19 13:39 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="1" data-topic="2358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>Is it possible to display 3D rendering in the 2D views</p>
</blockquote>
</aside>
<p>Does this make sense ?</p>
<p>And there’s already a ‘Triple 3D’ layout.</p>

---

## Post #3 by @lassoan (2018-03-19 14:05 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="1" data-topic="2358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>Is it possible to display 3D rendering in the 2D views (Axial, Coronal and Sagittal) e.g. the Maximum Intensity</p>
</blockquote>
</aside>
<p>It is the other way around. Slice views can be displayed in 3D views, if you click the “eye” icon in the slice controller.</p>
<aside class="quote no-group" data-username="brhoom" data-post="1" data-topic="2358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>Another question, why there is no “None” Preset? after selecting a specific preset I can not go back to the default.</p>
</blockquote>
</aside>
<p>Instead of having a “None” preset, we’ll add a reset button to revert to default preset (<a href="https://issues.slicer.org/view.php?id=4521" class="inline-onebox">Add reset volume rendering preset to default · Issue #4521 · Slicer/Slicer · GitHub</a>). Until then as a workaround, you can select any other preset and then select the current preset again.</p>

---

## Post #4 by @brhoom (2018-03-19 14:31 UTC)

<p>thanks for the info. I already know about displaying the slices in the 3D. A reset button would be great!</p>

---
