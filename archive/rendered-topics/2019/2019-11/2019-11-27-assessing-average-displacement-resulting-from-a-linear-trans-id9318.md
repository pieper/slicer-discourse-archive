# Assessing average displacement resulting from a linear transform

**Topic ID**: 9318
**Date**: 2019-11-27
**URL**: https://discourse.slicer.org/t/assessing-average-displacement-resulting-from-a-linear-transform/9318

---

## Post #1 by @DTI (2019-11-27 22:00 UTC)

<p>Hi,</p>
<p>Is there a way in Slicer to calculate the mean DTI distortion (e.g. as mean transform needed to align DTI to T2w, like the root mean square deviation).</p>
<p>I found this:</p>
<p><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5118068/#R34" rel="nofollow noopener">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5118068/#R34</a> -&gt;</p>
<h2>From the paper:</h2>
<p>"We also calculated the root mean square (RMS) deviation for each subject, which combines the six rigid body parameters into a single estimator of mean displacement [Jenkinson, 1999; Reuter et al., 2015]:</p>
<p>RMS = sqrt{r∗r ∕ 5 + tr[(M−I)T(M − I)] + tTt},</p>
<h2>where t is the translation vector, M is (here) the 3×3 rotation matrix, I is the identity matrix, tr[] is the trace operator, and r is the approximate spherical radius of the brain (here, estimated from the data to be 65 mm). The rigid body parameters and RMS values of the navigator logs were also examined."</h2>
<p>I have a slicer transform file (.h5) for each of my subjects and wonder if there is a way to calculate the RMS (or a similar measure) from them.</p>
<p>Thanks, Lorenz</p>

---

## Post #2 by @lassoan (2019-11-27 23:49 UTC)

<p>This formula in <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5118068/">Taylor2016</a> incorrect (since it would give non-zero value for an identity matrix), don’t use this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c66a189e5f6abc8d86b64fa56828a0de4a5f1ee7.png" data-download-href="/uploads/short-url/sjfQE5ep7sRCoygo1ly3xxIl2Sj.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c66a189e5f6abc8d86b64fa56828a0de4a5f1ee7.png" alt="image" data-base62-sha1="sjfQE5ep7sRCoygo1ly3xxIl2Sj" width="690" height="139" data-dominant-color="EDD8C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">694×140 10.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The formula in <a href="https://www.ncbi.nlm.nih.gov/pubmed/25498430/">Reuter2015</a> (the paper that Taylor2016 cites) looks correct:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7df1c65efed6e4c23504f8eb03e2b8c73d951f31.png" alt="image" data-base62-sha1="hY9GpJbddrMVhmZ4jZH4ZQJSUuJ" width="474" height="138"></p>
<p>You can get the value in Slicer by copy-pasting the following code into the Python console:</p>
<pre data-code-wrap="python"><code class="lang-python">transformNode = getNode('MyLinearTransform')
r = 15

import numpy as np
import math
transformMatrix = slicer.util.arrayFromTransformMatrix(transformNode)
t = transformMatrix[0:3,3]
M = transformMatrix[0:3,0:3]
RMS = math.sqrt(r * r / 5.0 * np.trace( (M-np.eye(3)).T @ (M-np.eye(3)) ) + np.dot(t,t))
print(RMS)
</code></pre>

---

## Post #3 by @DTI (2019-11-28 06:16 UTC)

<p>Thank you very much! This is very helpful!</p>
<p>I tried copy-pasted the code and filled in the name of my transform. I get the following error. How can I fix this?</p>
<pre><code class="lang-auto">&gt;&gt;&gt; transformNode = getNode('003_transform')
&gt;&gt;&gt; r = 15
&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; import math
&gt;&gt;&gt; transformMatrix = slicer.util.arrayFromTransformMatrix(transformNode)
Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: 'module' object has no attribute 'arrayFromTransformMatrix'
</code></pre>
<p>Thanks again,<br>
Lorenz</p>

---

## Post #4 by @lassoan (2019-11-28 12:27 UTC)

<p>This script works in recent Slicer Preview Releases. If you need to use latest Slicer Stable Release (4.10.2) then you can copy the slicer.util.arrayFromTransformMatrix method from <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py">here</a>.</p>

---

## Post #5 by @DTI (2019-11-28 14:00 UTC)

<p>It used it in the newest nightly release and it worked. Thank you very much again! I appreciate it a lot. - Lorenz</p>

---

## Post #6 by @DTI (2020-03-24 19:58 UTC)

<p>Hi, one last question regarding the formula as I am writing this up: what does T stand for? Havent found a definition in those papers.  Thanks, Lorenz</p>

---

## Post #7 by @lassoan (2020-03-24 20:14 UTC)

<p><code>matrix.T</code> it means transpose of <code>matrix</code>.</p>

---

## Post #8 by @DTI (2020-04-01 13:01 UTC)

<p>Perfect. Thank you very much!</p>

---
