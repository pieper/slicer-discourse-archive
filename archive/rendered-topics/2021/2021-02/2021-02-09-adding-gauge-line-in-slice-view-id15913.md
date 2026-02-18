# Adding gauge line in Slice view

**Topic ID**: 15913
**Date**: 2021-02-09
**URL**: https://discourse.slicer.org/t/adding-gauge-line-in-slice-view/15913

---

## Post #1 by @forfullstack (2021-02-09 10:18 UTC)

<p>I would like to implement gauge line around the slice intersection lines like screenshot. Then I will add some UI to control thickness of gauge.<br>
I think to add functions of drawing gauge line in the module what draws intersection lines. Else I should add node data structure for this gauge.<br>
What would be the best way to go?<br>
Should I take care of Python or VTK or QT parts or all those?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8ffc14cc79e40b1fadb30066e5d26853bf2c8e29.jpeg" alt="image" data-base62-sha1="kxKmjgy8ydlKQVxJhRWsOoAZlgt" width="539" height="284"><br>
Thanks</p>

---

## Post #2 by @lassoan (2021-02-09 13:56 UTC)

<p>The proper thing implementation is to add this to the slice intersection widget, in C++. You can then cleanly and easily implement both drawing of the lines and interaction with them.</p>

---

## Post #4 by @lassoan (2021-02-10 12:58 UTC)

<p>Keep us updated about your progress because we plan to add and maintain this feature in Slicer core and both you and core developers save a lot of time if we can work together. The key is to choose a design that is compatible with widget/displayable manager design of Slicer, which is somewhat different from VTK widgets (especially the event handling, distribution of responsibilities between widget and representation, and direct integration with MRML).</p>

---

## Post #5 by @forfullstack (2021-02-16 16:10 UTC)

<p>I have some progress now with this gauge. I was trying to implement as simple as possible.<br>
Really I have found SliceIntersectionDisplayPipeline is drawing intersection lines and added gauge pipelines to the every “main” pipelines as child. So whenever pipelines are updated it calculates gauge pipelines.<br>
Only problem is how to draw dashed line. Pipeline uses property of vtkProperty2D and there was obsoleted StipplePattern. Instead of, I tried to get effect using thickness and opacity.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbeeed5dd58e257a4375f910625a9bcb50cfa9ba.png" data-download-href="/uploads/short-url/t64PbY3KLrzvYpQf11AyS3TOGRY.png?dl=1" title="gauge" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbeeed5dd58e257a4375f910625a9bcb50cfa9ba_2_540x500.png" alt="gauge" data-base62-sha1="t64PbY3KLrzvYpQf11AyS3TOGRY" width="540" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbeeed5dd58e257a4375f910625a9bcb50cfa9ba_2_540x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbeeed5dd58e257a4375f910625a9bcb50cfa9ba.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbeeed5dd58e257a4375f910625a9bcb50cfa9ba.png 2x" data-dominant-color="858485"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">gauge</span><span class="informations">751×695 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ll be appreciated if anyone give me an idea about drawing of dashed line.</p>

---

## Post #6 by @lassoan (2021-02-16 16:41 UTC)

<p>This looks very promising! If you send a link to your branch then I can have a quick look.</p>
<aside class="quote no-group" data-username="forfullstack" data-post="5" data-topic="15913">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/forfullstack/48/9751_2.png" class="avatar"> forfullstack:</div>
<blockquote>
<p>I’ll be appreciated if anyone give me an idea about drawing of dashed line.</p>
</blockquote>
</aside>
<p>It is more complicated to create dashed lines with the OpenGL2 backend, but it should be possible. See this example:</p>
<p><a href="https://kitware.github.io/vtk-examples/site/Python/Rendering/StippledLine/" class="onebox" target="_blank" rel="noopener">https://kitware.github.io/vtk-examples/site/Python/Rendering/StippledLine/</a></p>

---

## Post #7 by @forfullstack (2021-02-18 00:14 UTC)

<p>I was working in the main branch and let me try to create my branch and commit later.<br>
Meanwhile I can send you patch if you are comfortable.<br>
In other hand, I’m not sure if the approach of this link is working to create dashed lines.<br>
SliceIntersectionDisplayPipeline is using vtkActor2D, vtkPolyDataMapper2D and vtkProperty2D. Really vtkActor2D does not support texture but vtkActor does. But if I try to use vtkActor, it doesn’t support vtkPolyDataMapper2D and vtkProperty2D so I can’t access SetLineWidth.<br>
Csaba already submitted this issue before.</p><aside class="quote" data-post="5" data-topic="1254">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/dashed-lines-for-isodose-curves/1254/5">Dashed lines for isodose curves</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Here is an example that uses texture: 
<a href="https://lorensen.github.io/VTKExamples/site/Cxx/Rendering/StippledLine/" class="onebox" target="_blank" rel="noopener nofollow ugc">https://lorensen.github.io/VTKExamples/site/Cxx/Rendering/StippledLine/</a>
  </blockquote>
</aside>


---

## Post #8 by @lassoan (2021-02-18 12:44 UTC)

<p>VTK plotting supports dashed lines and it paints in 2D. Maybe you can have a look at how that is implemented. Or check what would it take to use the same technique in 2D as it is used in the 3D actor/mapper. If you identified a few potential implementation options then ask on the VTK forum what they would recommend.</p>

---

## Post #9 by @Mik (2023-01-08 09:14 UTC)

<p>What is the status of dash line support in display managers? It would be great to have such feature for multiple isodose lines in SlicerRT and for my internal project as well. For exampe vtkLine in vtkChartXY supports dash line. May be i can help with some implementation?</p>

---

## Post #10 by @lassoan (2023-01-08 20:14 UTC)

<p>You can check out VTK examples and techniques described in <a href="https://gitlab.kitware.com/vtk/vtk/-/issues/15799">this issue</a>.</p>
<p>Note that result of model/slice intersection is a set of random tiny line pieces that you need to concatenate into a long polyline to be able to draw it with dashed style. You can use vtkStripper to merge connected line segments into polylines. You may need to adjust the maximum number of segments.</p>

---

## Post #11 by @Mik (2023-01-22 10:51 UTC)

<p>If i understood correctly such approach is only working in 3D. I was able to implement <a href="https://gitlab.kitware.com/vtk/vtk/-/issues/15799" rel="noopener nofollow ugc">the issue</a> in C++ and it`s working, The main task is how to make it work in 2D without adding another display manager.</p>

---

## Post #12 by @lassoan (2023-01-22 13:49 UTC)

<p>You may modify the model displayable manager (2D or 3D) in Slicer core and if it works then submit a pull request.</p>

---
