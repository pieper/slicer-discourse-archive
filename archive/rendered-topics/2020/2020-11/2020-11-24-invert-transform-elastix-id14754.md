# Invert transform (Elastix)

**Topic ID**: 14754
**Date**: 2020-11-24
**URL**: https://discourse.slicer.org/t/invert-transform-elastix/14754

---

## Post #1 by @janneke_slicer (2020-11-24 09:47 UTC)

<p>Hello,</p>
<p>I used Elastix (in Matlab) to register two images and to get the displacement field. I can import this displacement field in Slicer as a Transform. Now I have two questions:</p>
<ul>
<li>It seems that Slicer then automatically computes and imports the inverted transform. Is this true, and if so, why does it do this?</li>
<li>In the Transform module you can easily invert a transform with the ‘invert’ option. I am wondering how this works, because I understood that it can be quite challenging to invert a nonlinear displacement field, and often is an iterative process. But Slicer can do this within a few seconds, so I am wondering if someone could explain to me (the basics of) how this inverted transform is being computed.</li>
</ul>
<p>Thank you.</p>
<p>Janneke</p>
<p><em>P.S. I already read the following: <a href="https://discourse.slicer.org/t/inverting-elastix-transform/8123" class="inline-onebox">Inverting Elastix transform</a></em><br>
<em>So I undertand that the fixed image is the ‘parent’ and the moving image is the ‘child’, and that elastix computes the transform from parent (fixed) to child (moving).</em><br>
<em>Thus, the inverted transform is again from child (moving) to parent (fixed).</em></p>

---

## Post #2 by @lassoan (2020-11-24 19:39 UTC)

<aside class="quote no-group" data-username="janneke_slicer" data-post="1" data-topic="14754">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ebca7d/48.png" class="avatar"> janneke_slicer:</div>
<blockquote>
<p>It seems that Slicer then automatically computes and imports the inverted transform. Is this true, and if so, why does it do this?</p>
</blockquote>
</aside>
<p>Slicer does not invert the transform. ITK computes the inverse transform, because this is what you need for transforming images (resampling transform).</p>
<p>It may sound strange first, but for transforming objects between two coordinate systems, you need different transform, depending on what kind of data you work with. For transforming surface meshes, points, curves, etc. you need the forward (modeling) transform, while for transforming images you need the inverse (resampling) transform.</p>
<aside class="quote no-group" data-username="janneke_slicer" data-post="1" data-topic="14754">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ebca7d/48.png" class="avatar"> janneke_slicer:</div>
<blockquote>
<p>I am wondering how this works, because I understood that it can be quite challenging to invert a nonlinear displacement field, and often is an iterative process. But Slicer can do this within a few seconds, so I am wondering if someone could explain to me (the basics of) how this inverted transform is being computed.</p>
</blockquote>
</aside>
<p>Slicer needs to transform various objects, so it always needs forward and inverse transform for all transforms (including non-linear transforms, even if many of them are chained together). Therefore, we implemented transform nodes in Slicer so that they can store both “to parent” and “from parent” transforms and if only one is specified then compute the other dynamically. Dynamic inverse computation of composite non-linear transformation chains is implemented in VTK by David Gobbi -you can find more details about the used numerical methods in <a href="https://www.sciencedirect.com/science/article/abs/pii/S0895611102000915">this paper</a>.</p>
<p>If you work in an environment where VTK transforms are not available, only ITK, then the best you can do is to compute static inverse transforms over some predefined volume, which is of course very slow and very inflexible.</p>

---

## Post #3 by @janneke_slicer (2020-11-25 11:33 UTC)

<p>Hi Andras,</p>
<p>Thank you for the information! This helps me out a lot.</p>
<p>I understand that ITK computes the inverse transform (from fixed to moving) because of image resampling. But when I import this ‘inverse’ transform in Slicer, this transform seems to be automatically inverted again (to get the transform from moving to fixed). Then I can directly apply this transform to e.g. a mesh in the moving space.</p>
<p>So I was wondering why Slicer automatically inverts the transform back. When I check the transform after importing it says; “Transform to parent: Computed by inverting the transform from parent”.</p>
<p>As I understand it now Slicer automatically thus computes the inverse because it always wants “to parent” and “from parent” transforms. And as I understood from the paper it computes the inverse with an iterative process (Newton’s method). So it does this immediately during importing the transform, within a few seconds?</p>

---

## Post #4 by @lassoan (2020-11-25 14:58 UTC)

<aside class="quote no-group" data-username="janneke_slicer" data-post="3" data-topic="14754">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ebca7d/48.png" class="avatar"> janneke_slicer:</div>
<blockquote>
<p>As I understand it now Slicer automatically thus computes the inverse because it always wants “to parent” and “from parent” transforms. And as I understood from the paper it computes the inverse with an iterative process (Newton’s method). So it does this immediately during importing the transform, within a few seconds?</p>
</blockquote>
</aside>
<p>When Slicer reads a grid transform then it assumes that it is for transforming images (as most likely it was created by image registration) therefore it marks it as “from parent”.</p>
<p>Inversion is performed on-the-fly, whenever is needed, on specific data sets. For example, if you apply a non-linear transform on a volume that is displayed in a slice viewer then we don’t invert the entire volume (it would be very slow), but we set it in the image reslice filter that extracts the slice. Or, if you want to transform landmarks, it only needs to compute the inverse at those landmark locations, making computation time about 6 magnitudes faster (and a bit more accurate) than than inverting an entire field and applying that to the mesh.</p>

---
