# Points of a model

**Topic ID**: 34514
**Date**: 2024-02-24
**URL**: https://discourse.slicer.org/t/points-of-a-model/34514

---

## Post #1 by @sima (2024-02-24 06:05 UTC)

<p>Hi everybody</p>
<p>I have two question about number of points and cells of a model :</p>
<p>1- In the model module in the Information section, is the <strong>number of points and cells</strong> specified for a model related to the model’s surface (as a shell) or to its volume?"</p>
<p>2- I have a model that I convert to a segment in the <strong>segment editor module</strong>. In the <strong>Hollow</strong> section of the segment editor, I turn it into a shell with a thickness of 1 millimeter. Then, I convert it back to a model. The issue is that even though the interior of the model is hollowed, the number of points and cells becomes significantly higher (the initial model has 609 points, and the one converted to a 1-millimeter thick shell has 566,840 points). Why does this happen?!!  and how can I preserve the original number of points and cells?</p>

---

## Post #2 by @RafaelPalomar (2024-02-24 09:26 UTC)

<aside class="quote no-group" data-username="sima" data-post="1" data-topic="34514">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sima/48/67638_2.png" class="avatar"> sima:</div>
<blockquote>
<p>1- In the model module in the Information section, is the <strong>number of points and cells</strong> specified for a model related to the model’s surface (as a shell) or to its volume?"</p>
</blockquote>
</aside>
<p>The most common case is that your models are surface models. The points represents the vertices of the surface and the cells represent connections forming triangles.</p>
<aside class="quote no-group" data-username="sima" data-post="1" data-topic="34514">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sima/48/67638_2.png" class="avatar"> sima:</div>
<blockquote>
<p>2- I have a model that I convert to a segment in the <strong>segment editor module</strong>. In the <strong>Hollow</strong> section of the segment editor, I turn it into a shell with a thickness of 1 millimeter. Then, I convert it back to a model. The issue is that even though the interior of the model is hollowed, the number of points and cells becomes significantly higher (the initial model has 609 points, and the one converted to a 1-millimeter thick shell has 566,840 points). Why does this happen?!! and how can I preserve the original number of points and cells?</p>
</blockquote>
</aside>
<p>There are two factors that may be involved in the increase of points here:</p>
<ol>
<li>
<p>The amount of points (vertices) generated from a segmentation is dependent on the size of the segmentation image (the larger the image, in terms of voxels, and not necessarily in volume, the larger the resulting mesh). Your original mesh may have been derived from a segmentation with less voxels (i.e., larger thickness), so when you come down to 1 mm, the conversion naturally increases.</p>
</li>
<li>
<p>If I’m understanding correctly your hollowing process, the result is going to generate a “new side” of the surface (i.e., a sphere with only outer points vs a donut with outer and inner points). This new side requires new points.</p>
</li>
</ol>
<p>If you want to reduce the number of points in the new mesh, you can use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/surfacetoolbox.html" rel="noopener nofollow ugc">Surface Toolbox</a> module, which comes with 3D Slicer and apply <strong>clean</strong> and  <strong>decimation</strong>, which will effectively simplify the mesh.</p>

---
