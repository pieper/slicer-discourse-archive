---
topic_id: 45416
title: "How To Cut A Model Using A Grid Surface Markup"
date: 2025-12-09
url: https://discourse.slicer.org/t/45416
---

# How to cut a Model using a Grid Surface markup?

**Topic ID**: 45416
**Date**: 2025-12-09
**URL**: https://discourse.slicer.org/t/how-to-cut-a-model-using-a-grid-surface-markup/45416

---

## Post #1 by @GroadoSwaggins (2025-12-09 09:34 UTC)

<p>tldr: I would like to cut a Model in “half” using a non-flat planar surface I created with Markup &gt; Geometric Surface Grid. Is it possible? Further explanation below.</p>
<p>I have a CT scan asymmetrical brain Volume that I have made a Model out of. I am trying to cut it into two hemispheres to measure the actual volume.</p>
<p>Because of the asymmetry a straight vertical cut is unsatisfactory, and it seems the best way to follow the longitudinal fissure is with homologous points on the Geometric Surface Grid (I need repeatability, and it will be further implemented by some Python guru’s and use of a named template).</p>
<p>I would like to cut the resultant Model with a GSG, <em>OR</em> failing that, cut the Volume with a GSG, and make two Models with that, that I can measure the actual volumes with.<br>
Is it possible?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/328c36c7f72ae9e7c34afca5d9630d068063c9ca.jpeg" data-download-href="/uploads/short-url/7dahoEHPx2dvA9h4kvJYkcS2Hq2.jpeg?dl=1" title="splitexample" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/328c36c7f72ae9e7c34afca5d9630d068063c9ca_2_690x291.jpeg" alt="splitexample" data-base62-sha1="7dahoEHPx2dvA9h4kvJYkcS2Hq2" width="690" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/328c36c7f72ae9e7c34afca5d9630d068063c9ca_2_690x291.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/328c36c7f72ae9e7c34afca5d9630d068063c9ca_2_1035x436.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/328c36c7f72ae9e7c34afca5d9630d068063c9ca_2_1380x582.jpeg 2x" data-dominant-color="828DAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">splitexample</span><span class="informations">1493×631 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2025-12-09 09:53 UTC)

<p>I think this is possible even without scripting. Once established, a simple module can be created easily based on the workflow, especially with the current capabilities of agents.</p>
<ol>
<li>
<p>The grid surface needs a surface model node so that we have the surface patch in a data structure that can be used more easily later</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/4257487dca85a357c2e6de117b3cf86de03d2c35.png" data-download-href="/uploads/short-url/9sSw0XfWJZXVyDDxvYogaQsXsZn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/4257487dca85a357c2e6de117b3cf86de03d2c35.png" alt="image" data-base62-sha1="9sSw0XfWJZXVyDDxvYogaQsXsZn" width="625" height="180"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">625×180 7.46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>The model node containing the patch needs to be extruded so that it becomes a closed surface containing the half you need to keep. I haven’t used it yet, but it seems that the Extrude tool in Dynamic Modeler can do it</p>
</li>
<li>
<p>Get the intersection of the two models using Combine Models module in the Sandbox extension. Not sure how robust it is, but this would be my first option</p>
</li>
</ol>
<p>Let us know how it goes.</p>

---

## Post #3 by @GroadoSwaggins (2025-12-11 09:43 UTC)

<p>I can’t get that to work.<br>
I made model “plane” and extruded it away from a plane as you can see in screenshot.</p>
<p>Then I tried the various operations (in Combine Model) including Intersections for brain model and the extruded model, but it just thinks for 5 minutes or so and then makes the intersection model, but that model is always empty.</p>
<p>I am at a loss. Is there an easier way that I can use a model or the grid markup as a border for a segmentation instead?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93e55e0e792f877ba75246a87b422a596c0db180.jpeg" data-download-href="/uploads/short-url/l6lBxMnzVEU4q1sxGdXupu8xihy.jpeg?dl=1" title="extrude" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93e55e0e792f877ba75246a87b422a596c0db180_2_690x459.jpeg" alt="extrude" data-base62-sha1="l6lBxMnzVEU4q1sxGdXupu8xihy" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93e55e0e792f877ba75246a87b422a596c0db180_2_690x459.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93e55e0e792f877ba75246a87b422a596c0db180_2_1035x688.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93e55e0e792f877ba75246a87b422a596c0db180.jpeg 2x" data-dominant-color="948FB6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">extrude</span><span class="informations">1375×916 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2025-12-11 10:36 UTC)

<p>If surface mesh operations are not reliable (if you look up I mentioned that I was not sure how robust it was, because this is a very hard problem, but some tools were added by <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> which I haven’t used yet), then you could use Segment Editor. Convert both the brain model and the extruded model to segmentation, and create the intersection in Segment Editor using the Logical operators effect. Actually I’d be surprised if your brain model was not a segmentation before you made it a model.</p>

---

## Post #5 by @mau_igna_06 (2025-12-11 18:40 UTC)

<p>By the way, looking at your first picture (on the left side):</p>
<ul>
<li>That brain model has a lot of holes which makes the CombineModels algorithm work harder and increasing the possibility it will fail. I suggest you save both models, the <em>brain</em> and the <em>grid</em> as <code>.vtk</code> files and open an issue for the maintainer of the algorithm → <a href="https://github.com/zippy84/vtkbool/issues/new" rel="noopener nofollow ugc">here</a></li>
</ul>
<p>I would try to measure the volume on the labelmap domain as <a class="mention" href="/u/cpinter">@cpinter</a> suggested as it straight-forward, you may need to check if your hardware is big enough to reach a measurement quality that makes the computed volume error trivial.<br>
You may also need to upsample your image/segmentation to achieve smaller voxels that increase the measurement quality at expense of larger computing-time/hardware</p>

---

## Post #6 by @GroadoSwaggins (2025-12-12 01:01 UTC)

<p>Yes, the holes were a contrast issue I screwed up early when playing with the volumes. I just didn’t go back and fix it as this was mainly experimenting with a technique and I wasn’t concerned, though maybe should have been.</p>
<p>cPinter’s 2nd suggestion worked after converting models back into segmentations, putting them in a single Segmentation folder and using the logical operator Intersect properly.</p>

---
