---
topic_id: 11060
title: "Is There A Color Bar Or Color Legend Available"
date: 2020-04-09
url: https://discourse.slicer.org/t/11060
---

# Is there a color bar or color legend available?

**Topic ID**: 11060
**Date**: 2020-04-09
**URL**: https://discourse.slicer.org/t/is-there-a-color-bar-or-color-legend-available/11060

---

## Post #1 by @ButuiHu (2020-04-09 17:42 UTC)

<p>I have calculated model to model distance with Model to Model Distance extension, and I want a color bar or color legend. I check <a href="https://discourse.slicer.org/t/where-to-turn-on-and-off-color-scale-bar/8347">this post</a>, but failed to find one.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/132585050add23e241aa3e5f447241dca46f656d.png" data-download-href="/uploads/short-url/2JnslY9llHGDZ6UviuPn1Dyk9Vr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/132585050add23e241aa3e5f447241dca46f656d_2_690x437.png" alt="image" data-base62-sha1="2JnslY9llHGDZ6UviuPn1Dyk9Vr" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/132585050add23e241aa3e5f447241dca46f656d_2_690x437.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/132585050add23e241aa3e5f447241dca46f656d_2_1035x655.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/132585050add23e241aa3e5f447241dca46f656d_2_1380x874.png 2x" data-dominant-color="F0F6F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2286×1448 486 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I would like something like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1359c36544cc81a2c3f53f27d3eb364ca95e2b95.jpeg" data-download-href="/uploads/short-url/2Lbo6IzvNdQT6VlFLi7XptLutgx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1359c36544cc81a2c3f53f27d3eb364ca95e2b95_2_425x499.jpeg" alt="image" data-base62-sha1="2Lbo6IzvNdQT6VlFLi7XptLutgx" width="425" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1359c36544cc81a2c3f53f27d3eb364ca95e2b95_2_425x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1359c36544cc81a2c3f53f27d3eb364ca95e2b95_2_637x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1359c36544cc81a2c3f53f27d3eb364ca95e2b95.jpeg 2x" data-dominant-color="EAE5E5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">788×926 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I have to calculate model to model distance with 3DMetricMesh, save the result to vtk file, and import it to paraview to get this rendering. It would be great if I could do all this in Slicer.</p>
<p>Another question, is there any method to capture the 3D view with only the 3D cube? I don’t want the extra white border with Slicer’s capture screenshot.</p>

---

## Post #2 by @jamesobutler (2020-04-09 18:18 UTC)

<aside class="quote no-group" data-username="ButuiHu" data-post="1" data-topic="11060">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/butuihu/48/2386_2.png" class="avatar"> ButuiHu:</div>
<blockquote>
<p>I check <a href="https://discourse.slicer.org/t/where-to-turn-on-and-off-color-scale-bar/8347">this post</a>, but failed to find one.</p>
</blockquote>
</aside>
<p>Did you actually switch to the “DataProbe” module as that post describes? This is different from the Data Probe button that is usually at the bottom of the left side module panel area. In the image shown above you were still in the “Models” module.</p>

---

## Post #3 by @lassoan (2020-04-09 18:48 UTC)

<p>See also this post:</p>
<aside class="quote quote-modified" data-post="2" data-topic="10953">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/change-color-map-and-add-color-scale/10953/2">Change Color map and add color scale</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can do this all in Slicer. 
Edit color table: Go to colors module, choose a color node that you would like to modify, click “Copy” button to create an editable copy (the default color nodes are read-only). If you choose a “color table” type of node (this is the most common) then you get hundreds of predefined colors and you can modify each by double-clicking the color swatch in the color column, which can be tedious if you want to make large changes. It may be more convenient to modify “Cont…
  </blockquote>
</aside>


---
