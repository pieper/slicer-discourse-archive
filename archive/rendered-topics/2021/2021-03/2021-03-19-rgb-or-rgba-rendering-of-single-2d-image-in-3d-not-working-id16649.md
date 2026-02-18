# RGB or RGBA rendering of single 2D image in 3D not working

**Topic ID**: 16649
**Date**: 2021-03-19
**URL**: https://discourse.slicer.org/t/rgb-or-rgba-rendering-of-single-2d-image-in-3d-not-working/16649

---

## Post #1 by @klarlund (2021-03-19 17:05 UTC)

<p>Hi!</p>
<p>For a complex registration situation, I need to position a 2D tissue image in the 3D viewer. The problem is that the picture won’t show correctly either as a slice view or as a volume rendering. Initially, after loading, the picture shows correctly in the 2D red slice viewer, however.</p>
<p>I used the nifty little code snippet by <a class="mention" href="/u/lassoan">@lassoan</a> in <a href="https://discourse.slicer.org/t/retain-image-color-in-volume-rendering/12294/10" class="inline-onebox">Retain Image Color in Volume Rendering - #10 by lassoan</a> after loading the sample picture below.</p>
<p>The problem is two-fold: the coloring changes in the 2D viewer and only a gray surface in shown in 3D. When using a different png with an existing alpha channel (picture shows up in the volume panel as a vector image of dimension 4), I don’t add the alpha, but the picture still shows up grey in 3D. (In any case, the Slice view of the red viewer in 3D serves up a red surface. But that’s not the main problem.)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fd6cbf157b929b212eafd0cd55cb2165b086583.png" alt="road runner" data-base62-sha1="6PcDJhXTVtQ1tQwsXu7fW5Gjfwv" width="175" height="288"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62accb9ecdbfb6a2bbaa5795805bf119e4b73165.png" data-download-href="/uploads/short-url/e4V0ho8xMfinxGoWmLMlPYopaIt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62accb9ecdbfb6a2bbaa5795805bf119e4b73165_2_345x162.png" alt="image" data-base62-sha1="e4V0ho8xMfinxGoWmLMlPYopaIt" width="345" height="162" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62accb9ecdbfb6a2bbaa5795805bf119e4b73165_2_345x162.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62accb9ecdbfb6a2bbaa5795805bf119e4b73165_2_517x243.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62accb9ecdbfb6a2bbaa5795805bf119e4b73165_2_690x324.png 2x" data-dominant-color="8C8CA7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1130×531 63.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Probably a stupid mistake on my part? This is in Slicer 4.13.0-2021-03-18 – same problem in 4.11 release.</p>

---

## Post #2 by @lassoan (2021-03-19 18:15 UTC)

<p>3-component RGB images appear correctly in slice views and the slices can be displayed in 3D view, too.</p>
<p>4-component RGBA images are required for color volume rendering but RGBA volumes, but slice views of such volumes cannot be displayed in 3D view - see <a href="https://github.com/Slicer/Slicer/issues/4939">this issue</a>. If you want this to be fixed then <a href="https://discourse.slicer.org/t/about-the-feature-requests-category/30">add a vote for it</a>. If an issue gets many votes (or needed for a funded project) then we can allocate developers to fix it. If you need it sooner and you are comfortable with C++ and the VTK library then then you can give it a go and fix it (we can help if you decide to try it). You can also submit a feature request for volume rendering to support RGB volumes (without the need for manually extending it to RGBA).</p>

---

## Post #3 by @klarlund (2021-03-19 20:08 UTC)

<p>Thanks, I’m unstuck now!  Your answer in <a href="https://discourse.slicer.org/t/transform-scale/8731/6" class="inline-onebox">Transform: scale - #6 by timeanddoctor</a> is useful, too for folks in a similar situation, just remember to remove the alpha channel before loading the picture (I used gimp). Then register by moving the 3D volume. The picture allows one rotation and three translational degrees of freedom. Another hack I guess would be to let a reformat widget track the picture if it’s subjected to all 6 degrees of freedom, but your suggestion will do for now!</p>
<p>Also you taught me how to vote for a github issue – that somehow had eluded me until now.</p>

---

## Post #4 by @lassoan (2021-03-26 17:37 UTC)

<aside class="quote no-group" data-username="klarlund" data-post="3" data-topic="16649">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/klarlund/48/7962_2.png" class="avatar"> klarlund:</div>
<blockquote>
<p>Another hack I guess would be to let a reformat widget track the picture if it’s subjected to all 6 degrees of freedom</p>
</blockquote>
</aside>
<p>There is a module for this already: Volume reslice driver module (in SlicerIGT extension).</p>

---
