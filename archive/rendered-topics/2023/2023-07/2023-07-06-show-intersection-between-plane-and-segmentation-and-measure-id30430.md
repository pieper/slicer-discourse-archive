# Show intersection between plane and segmentation and measure max diameter

**Topic ID**: 30430
**Date**: 2023-07-06
**URL**: https://discourse.slicer.org/t/show-intersection-between-plane-and-segmentation-and-measure-max-diameter/30430

---

## Post #1 by @Birnie (2023-07-06 11:11 UTC)

<p>Hi there!</p>
<p>For my project I’m working in 3D slicer.<br>
I have made a segmentation of a dissected aorta. This segmentation contains a segmentation of the true lumen, false lumen and the both lumina combined.<br>
In addition I have determine some anatomical planes, for example at the level of the bifurcation of the truncus pulmonalis. I have created this planes with the “Markups” module.</p>
<p>Now I want to determine the maximum diameter of the lumina at the intersection of the planes and the segmentations.<br>
I have already tried to accomplish this with the help of the centerline and cross-section analysis modules of the VMTK toolkit. However, this modules does not allow me to determine the max diameter in the specific planes I have determined.</p>
<p>Do you guys know a way to obtain the intersection of a plane (created with Markups) and a segmentation, so I can perform measurement on that cross-section?</p>
<p>With kind regards,<br>
Birnie</p>

---

## Post #2 by @lassoan (2023-07-06 16:07 UTC)

<p>Cross-section analysis module can already compute the largest inscribed sphere diameter. You can show it if you click the “show” button for “Diameter (MIS)” in “Browse cross-sections”.</p>
<p>If you want to compute the largest diameter then you can click “show” for the “Cross-sectional area” row and then analyze the created “Cross section for …” model. For example, you can get all model points like this:</p>
<pre><code class="lang-auto">coords = arrayFromModelPoints(getNode("yourmodelnodename"))
</code></pre>
<p>Can you give a bit more details about why you need computation of the maximum diameter?</p>
<p>If you think that this metric could be generally useful then you could add the computation to the module.</p>

---

## Post #3 by @chir.set (2023-07-06 18:46 UTC)

<aside class="quote no-group" data-username="Birnie" data-post="1" data-topic="30430">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/6bbea6/48.png" class="avatar"> Birnie:</div>
<blockquote>
<p>some anatomical planes</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="Birnie" data-post="1" data-topic="30430">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/6bbea6/48.png" class="avatar"> Birnie:</div>
<blockquote>
<p>in the specific planes I have determined</p>
</blockquote>
</aside>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="30430">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Cross-section analysis module can …</p>
</blockquote>
</aside>
<p>It seems that <a class="mention" href="/u/birnie">@Birnie</a> wants to cut segments with arbitrary planes, rather that cross-sectional ones that are orthogonal to a given centerline.</p>
<p>If so, he may</p>
<ul>
<li>export his segments to models</li>
<li>use ‘Place cut’ in ‘Dynamic modeler’</li>
<li>perform manual measurements on the result.</li>
</ul>
<p>A screenshot of his segments and markups planes would have been helpful.</p>

---
