# Automatize model remeshing using python

**Topic ID**: 43810
**Date**: 2025-07-22
**URL**: https://discourse.slicer.org/t/automatize-model-remeshing-using-python/43810

---

## Post #1 by @MrMarkus (2025-07-22 14:55 UTC)

<p>Dear all,</p>
<p>I would like to remesh a couple of model files in batch processing fashion.</p>
<p>The plan is to use “Surface Toolbox” Module, herein the “Uniform remesh” algorithm. And the<br>
number of points set to 100k.</p>
<p>By now I could only make it till here:</p>
<p>modelFile = “…model.ply”<br>
inputModel = slicer.util.loadModel(modelFile)<br>
modelDisplayNode = inputModel.GetDisplayNode()</p>
<p>the remaining main steps like:</p>
<ul>
<li>switch to the modul</li>
<li>set the parameters of the new mesh</li>
<li>perform remeshing</li>
<li>export remeshed model as *.stl</li>
</ul>
<p>are the “tricky” parts… <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=14" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
<p>Could someone please advise and give me a hint how to proceed.</p>
<p>THANKS!</p>
<p>Best,<br>
Markus</p>

---
