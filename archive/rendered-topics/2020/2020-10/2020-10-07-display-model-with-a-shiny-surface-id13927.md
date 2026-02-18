# Display model with a "shiny" surface

**Topic ID**: 13927
**Date**: 2020-10-07
**URL**: https://discourse.slicer.org/t/display-model-with-a-shiny-surface/13927

---

## Post #1 by @aldoSanchez (2020-10-07 18:46 UTC)

<p>hello<br>
Today I try to modify the brightness(Shiny material properties) of the modules<br>
but I found only one XML file<br>
and I don’t know how to access this code.</p>
<p><a href="https://github.com/Slicer/Slicer/search?q=shiny" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/search?q=shiny</a></p>
<p>I just want to change the Preview<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d0970289e8f9d8a1baaab3ab817643ff13180a6.png" data-download-href="/uploads/short-url/hQ7U6nk9m2NFjjE3YGvaZLjJLQG.png?dl=1" title="shyni" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d0970289e8f9d8a1baaab3ab817643ff13180a6_2_690x348.png" alt="shyni" data-base62-sha1="hQ7U6nk9m2NFjjE3YGvaZLjJLQG" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d0970289e8f9d8a1baaab3ab817643ff13180a6_2_690x348.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d0970289e8f9d8a1baaab3ab817643ff13180a6_2_1035x522.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d0970289e8f9d8a1baaab3ab817643ff13180a6.png 2x" data-dominant-color="A8A4A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">shyni</span><span class="informations">1366×689 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-10-07 19:48 UTC)

<p>Display properties are stored in the <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html">display node</a>. For example, you can use <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html#a17b863f325bdb1c32edf488f932b9897">SetAmbient</a>, <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html#ab75da4d3244c0c8705bb88629095a562">SetDiffuse</a>, <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html#ab69c2a106a20855acce900fb65030862">SetSpecular</a>, and <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html#abe4ea8419ecb3de20963fa37719688b3">SetPower</a> methods.</p>

---

## Post #3 by @aldoSanchez (2020-10-07 20:13 UTC)

<p>wow that works perfectly thanks<br>
I leave the code here:</p>
<pre><code class="lang-python">vtkRCC=getNode('Right-Cerebral-Cortex')

vtkRCC.GetDisplayNode().SetAmbient(.1)
vtkRCC.GetDisplayNode().SetDiffuse(.6)
vtkRCC.GetDisplayNode().SetSpecular(.5)
vtkRCC.GetDisplayNode().SetPower(40)
</code></pre>

---

## Post #4 by @aldoSanchez (2020-10-08 16:43 UTC)

<p>hello today i found a bug<br>
what i do is the following instruction<br>
vtkRCC.GetDisplayNode().ClippingOn()<br>
vtkRCC.GetDisplayNode().ClippingOff()<br>
and automatically changes the visible sides of<br>
Right-Cerebral-Cortex to all.<br>
but when I want to do it with the left side it doesn’t work<br>
I just want to use this instruction visible side all.</p>

---

## Post #5 by @lassoan (2020-10-08 16:50 UTC)

<p>This is not a bug but a feature. If you clip a model then you need to show both frontface and backface of the model.</p>

---

## Post #6 by @aldoSanchez (2020-10-08 17:15 UTC)

<p>but it just aply to right side the left side is not changging</p>

---

## Post #7 by @lassoan (2020-10-08 17:17 UTC)

<p>If you want to show both sides of a model then you can call <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html#ae171c148f2a8fce408d2008fbd4645d8"><code>BackfaceCullingOff()</code></a> method.</p>

---

## Post #8 by @aldoSanchez (2020-10-08 17:19 UTC)

<p>thank you that explains everything</p>

---
