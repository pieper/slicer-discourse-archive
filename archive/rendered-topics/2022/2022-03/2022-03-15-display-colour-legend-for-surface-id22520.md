---
topic_id: 22520
title: "Display Colour Legend For Surface"
date: 2022-03-15
url: https://discourse.slicer.org/t/22520
---

# Display Colour Legend for Surface

**Topic ID**: 22520
**Date**: 2022-03-15
**URL**: https://discourse.slicer.org/t/display-colour-legend-for-surface/22520

---

## Post #1 by @connorh (2022-03-15 14:08 UTC)

<p>Hello,</p>
<p>I’m working on an extension (in python) where I have a surface mesh with attributes that I’m colouring the mesh based on attribute value.  I would like to add a colour bar/legend programmatically with the values corresponding to my colours.<br>
Something similar to this: <a href="https://discourse.slicer.org/t/change-color-map-and-add-color-scale/10953" class="inline-onebox">Change Color map and add color scale</a><br>
Except through the colours module I can only seem to create a colour map for my foreground/background images and not for my vtkMRMLModelNode object.</p>
<p>First time posting, so I hope I’m providing sufficient detail - thanks in advance for any support!<br>
Connor</p>

---

## Post #2 by @Mik (2022-03-15 19:22 UTC)

<p>For displayed model node you can use “Models” module with “Scalars” and “Color Legend” sub-sections.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62106d20878fe3410ff53f560013b2eee07cc865.png" data-download-href="/uploads/short-url/dZvZ5gD9MoWDor53BTtdT7gG45f.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62106d20878fe3410ff53f560013b2eee07cc865_2_601x500.png" alt="image" data-base62-sha1="dZvZ5gD9MoWDor53BTtdT7gG45f" width="601" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62106d20878fe3410ff53f560013b2eee07cc865_2_601x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62106d20878fe3410ff53f560013b2eee07cc865_2_901x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62106d20878fe3410ff53f560013b2eee07cc865.png 2x" data-dominant-color="7D7E7B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1194×993 233 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Major features of “Color Legend” is described here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="21567">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/color-scalar-bar-reworked-and-upgraded-now-it-s-called-color-legend/21567">"Color Scalar Bar" reworked and upgraded, now it’s called "Color Legend"</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Starting from version <a href="https://github.com/Slicer/Slicer/pull/5828/commits/170a0e0edd448fd2c5d8e47ac6de591293fc8354" rel="noopener nofollow ugc">30530 build 2022-01-15</a> “Color Scalar Bar” section from “Colors” module was replaced with “Color Legend” section. 
The “Color Legend” section has been also added to the “Volume”, “Model” and “Markups” modules to control visibility and behavior of color legend. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6755ea30878f4e57abb5e25ea985518b838bea3e.jpeg" data-download-href="/uploads/short-url/eK9fz7FnRdhsnN7COOaH5Wc2NCm.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
New major features: 


More unified API. Each Volume, Model, Markups or any other displayable node now can have an individual color legend by means of <a href="https://apidocs.slicer.org/master/classvtkMRMLColorLegendDisplayNode.html" rel="noopener nofollow ugc">vtkMRMLColorLegendDisplayNode</a>. 


Displayed LUT is in sy…
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2022-03-16 21:12 UTC)

<p>If you want to display color legend to a model node then this should be sufficient:</p>
<pre><code class="lang-python">slicer.modules.colors.logic().AddDefaultColorLegendDisplayNode(modelNode)
</code></pre>
<p>You can find a complete example of displaying a model node with a custom colormap and a color legend in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-custom-color-map-and-display-color-legend">script repository</a>.</p>

---

## Post #4 by @connorh (2022-03-31 12:59 UTC)

<p>Thank you for the help.  Unfortunately I keep getting the error, even when following the full example you posted:</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
AttributeError: ‘vtkSlicerColorsModuleLogicPython.vtkSlicerColorLog’ object has no attribute ‘AddDefaultColorLegendDisplayNode’</p>
</blockquote>
<p>I am running the last stable release of Slicer (4.11), do I need to be running 4.13?  To make sure it wasn’t just my modelNode doing something weird, I tried <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-color-legend-for-a-volume-node" rel="noopener nofollow ugc">this</a> with a simple PET dataset and got the same error.</p>
<p>Any suggestions?</p>

---

## Post #5 by @lassoan (2022-03-31 13:00 UTC)

<p>Yes, you need to use the latest Slicer Preview Release. This feature has been added recently.</p>

---
