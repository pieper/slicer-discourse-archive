# Model to Model Distance

**Topic ID**: 5551
**Date**: 2019-01-29
**URL**: https://discourse.slicer.org/t/model-to-model-distance/5551

---

## Post #1 by @emrobert (2019-01-29 01:44 UTC)

<p>Operating system: OS X MAC<br>
Slicer version: 4.11<br>
Expected behavior: Distance calculations between models<br>
Actual behavior: I understand that you can use model to model distance to create surface maps using the shape population viewer. However, if I want to select certain points between 2 models and get the Hausdorff distances, can you do this with just the model to model extension? I’m comparing two cranial vault volumes and I get the following output:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38f10d133026a79c9ff73e6b56fa0e9a499697d6.png" data-download-href="/uploads/short-url/87JbEfjn0xX2XIsWx2aZ1D2483s.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38f10d133026a79c9ff73e6b56fa0e9a499697d6_2_690x170.png" alt="image" data-base62-sha1="87JbEfjn0xX2XIsWx2aZ1D2483s" width="690" height="170" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38f10d133026a79c9ff73e6b56fa0e9a499697d6_2_690x170.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38f10d133026a79c9ff73e6b56fa0e9a499697d6_2_1035x255.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38f10d133026a79c9ff73e6b56fa0e9a499697d6_2_1380x340.png 2x" data-dominant-color="B2B5D1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3809×940 456 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there a way to select points on the source model and obtain values for distance between that point and the target model?<br>
Thanks!</p>

---

## Post #2 by @lassoan (2019-01-30 02:20 UTC)

<p>What is your end goal?</p>
<p>You can compute max or 95% Hausdorff distance using Segment Comparison extension (in SlicerRT).</p>
<p>If you want to get value at selected point then you can write a few-line Python script that probes the model at specific positions then copy paste this code to the Python console: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model</a></p>

---

## Post #3 by @emrobert (2019-01-30 20:14 UTC)

<p>Hello again,</p>
<p>My goal in general is:</p>
<p>Register two models together (done)</p>
<p>Make color maps comparing distances between the models (done)</p>
<p>Be able to click at a point on one model and calculate the distance between that model and the other model at any model (can’t figure out)</p>
<p>With the old 3D Mesh Metric module it was very easy. But with model to model distance and shape population viewer, I cannot figure out a way to calculate the inter-model distance just by selecting a specific part on the model. I thought that by running the two models into Model to Model distance you could get distance information, but from what I understand, Model to Model distance seems to be an intermediate step to creating a color map in Shape Population Viewer. While the color map is great, I need accurate distances between models at a number of different points.</p>
<p>Thanks in advance for your help! And I will try to RT Extension as suggested.</p>
<p>Cheers,</p>

---

## Post #4 by @lassoan (2019-01-31 00:17 UTC)

<aside class="quote no-group" data-username="emrobert" data-post="3" data-topic="5551">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/b9bd4f/48.png" class="avatar"> emrobert:</div>
<blockquote>
<p>Be able to click at a point on one model and calculate the distance between that model and the other model at any model (can’t figure out)</p>
</blockquote>
</aside>
<p>The example linked above does exactly this. In the example, you place the position by hovering over a position with the moues pointer but you can modify the behavior (see other examples in the script repository) to get the RAS position from a markup fiducial.</p>
<p>Here is the link again: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---
