# In volume rendering, how to set the rendering result to not blur when rotating the camera

**Topic ID**: 39742
**Date**: 2024-10-17
**URL**: https://discourse.slicer.org/t/in-volume-rendering-how-to-set-the-rendering-result-to-not-blur-when-rotating-the-camera/39742

---

## Post #1 by @dbtruong (2024-10-17 09:39 UTC)

<p>The question is what I want to ask.<br>
How to fix results when rendering CPU usage?<br>
Thanks a lot.</p>

---

## Post #2 by @jamesobutler (2024-10-17 11:33 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html#panels-and-their-use" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html#panels-and-their-use</a></p>
<p>The above place in the documentation details Volume Rendering options associated with quality such as “Adaptive” and “Normal”.</p>

---

## Post #3 by @dbtruong (2024-10-18 02:08 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> Thank you for your answer</p>
<pre><code class="lang-auto">cpuMapper-&gt;SetSampleDistance(displayNode-&gt;GetSampleDistance());
cpuMapper-&gt;SetInteractiveSampleDistance(displayNode-&gt;GetSampleDistance());
</code></pre>
<p>I see there are two parameters as above. So what is their input value usually and what is their meaning?</p>

---

## Post #4 by @lassoan (2024-10-18 02:46 UTC)

<p>This is the sampling distance for raycasting. Higher number means coarser sampling, lower quality, higher speed. See more details in the VTK textbook and VTK documentation.</p>

---

## Post #5 by @dbtruong (2024-10-21 01:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
I have a better understanding of it. Thank you very much</p>

---
