---
topic_id: 4739
title: "Saved Transformed Registration For Calculating Model To Mode"
date: 2018-11-13
url: https://discourse.slicer.org/t/4739
---

# Saved Transformed Registration for Calculating Model To Model Distance

**Topic ID**: 4739
**Date**: 2018-11-13
**URL**: https://discourse.slicer.org/t/saved-transformed-registration-for-calculating-model-to-model-distance/4739

---

## Post #1 by @Olivia_Yeuhsin_Chou (2018-11-13 04:47 UTC)

<p>Operating system: windows<br>
Slicer version: 4.8.1</p>
<p>Hello,</p>
<p>I have a question regarding how I can save registration (done under transform module) to a file form that could be used for calculating model to model distance.</p>
<p>The registration was automatically saved as “.h5” by the software, and when I tried calculating “model to model distance” with the “.h5” registration, the calculation just ran forever and did not come up with an result.</p>
<ul>
<li>Olivia</li>
</ul>

---

## Post #2 by @lassoan (2018-11-15 20:34 UTC)

<p>Try latest version of Slicer.</p>
<p>Can you share an example scene (saved as .mrb file) where you can reproduce the issue? Tell us the exact steps that you do after you load the scene.</p>

---

## Post #3 by @Olivia_Yeuhsin_Chou (2018-11-15 23:08 UTC)

<p>Here is the scene. This is after I’ve registered the 2nd time point surface model(in vtk format) onto the 1st time point surface model. I wanted to save the models in their registered positions, so that I can later generate model to model distance color map off it. But on the save options, there was not an option for saving the registered models as vtk or gipl format.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c765cf40a8755aaf10efbe63a0ec75678018a9a.jpeg" data-download-href="/uploads/short-url/k2Ar8g3T3cHi2B9Ty5ANxJuMaNk.jpeg?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c765cf40a8755aaf10efbe63a0ec75678018a9a_2_690x412.jpeg" alt="Picture1" data-base62-sha1="k2Ar8g3T3cHi2B9Ty5ANxJuMaNk" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c765cf40a8755aaf10efbe63a0ec75678018a9a_2_690x412.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c765cf40a8755aaf10efbe63a0ec75678018a9a_2_1035x618.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c765cf40a8755aaf10efbe63a0ec75678018a9a_2_1380x824.jpeg 2x" data-dominant-color="B8A7C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">1876×1121 585 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2018-11-16 04:34 UTC)

<p>If you want to persistently modify model point positions then <em>harden</em> the transform on the model. You can do it in <em>Transforms</em> module (select the transformed node in Apply transform / Transformed section and click harden button) or in <em>Data</em> module’s <em>Transform hierarchy</em> tab (right-click on transformed node and click <em>Harden transform</em>).</p>

---

## Post #5 by @Olivia_Yeuhsin_Chou (2018-11-29 22:33 UTC)

<p>So I was able to save the transform following your advice!! Thanks a lot!!</p>
<p>However, I’ve ran into another problem. That is, after creating a color map file with the transformed models in “model to model distance module”, I moved on to the “ShapePolulationView” (as instructed in DCBIA tutorial video <span class="hashtag">#5A</span> 3D), and nothing happened when I clicked apply . I was waiting for an independent window to pop up like in the tutorial, but nothing happened. Any ideas on how to get the colormap module window to show?</p>
<p>Here is how the scene look like:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5a2d969998497c06775b2f13a6c10cb9a3d61c3.jpeg" data-download-href="/uploads/short-url/nDhGvkHHiJYnHv0pEoLfBLTn7Fx.jpeg?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5a2d969998497c06775b2f13a6c10cb9a3d61c3_2_690x430.jpeg" alt="Picture1" data-base62-sha1="nDhGvkHHiJYnHv0pEoLfBLTn7Fx" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5a2d969998497c06775b2f13a6c10cb9a3d61c3_2_690x430.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5a2d969998497c06775b2f13a6c10cb9a3d61c3_2_1035x645.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5a2d969998497c06775b2f13a6c10cb9a3d61c3_2_1380x860.jpeg 2x" data-dominant-color="B4BDC9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">1850×1154 439 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks in advance for any suggestions!!</p>

---

## Post #6 by @lassoan (2018-11-30 00:23 UTC)

<p>ShapePopulationViewer only works in latest nightly version of Slicer. <a class="mention" href="/u/jcfr">@jcfr</a> can you confirm?</p>
<p>Most features of ShapePopulationViewer are also available directly in Slicer. What would you like to do?</p>

---

## Post #7 by @Olivia_Yeuhsin_Chou (2018-11-30 00:35 UTC)

<p>I would like to get my registered models to show quantitative changes in colormaps</p>

---

## Post #8 by @lassoan (2018-11-30 13:51 UTC)

<p>You can go to Models module and enable coloring by distance in <em>Scalars</em> section: check <em>Visible</em> checkbox, choose <em>Active scalar</em>, and you may further customize display by selecting colormap, displayed range, thresholding, etc.</p>

---
