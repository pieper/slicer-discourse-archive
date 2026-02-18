# About the scissors tool in the Segment Editor

**Topic ID**: 17803
**Date**: 2021-05-26
**URL**: https://discourse.slicer.org/t/about-the-scissors-tool-in-the-segment-editor/17803

---

## Post #1 by @slicer365 (2021-05-26 06:54 UTC)

<p>About the scissors tool in the Segment Editor, how to make the edge of the scissors be a relatively smooth line,Scissors can cut round shapes，But I want to crop any smooth arc.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14f898862e4952b5abad9ffeb61fbce860730669.jpeg" data-download-href="/uploads/short-url/2Zwa8inqhgWhAfJSu8PW3Og0I0V.jpeg?dl=1" title="无标题" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14f898862e4952b5abad9ffeb61fbce860730669_2_593x499.jpeg" alt="无标题" data-base62-sha1="2Zwa8inqhgWhAfJSu8PW3Og0I0V" width="593" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14f898862e4952b5abad9ffeb61fbce860730669_2_593x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14f898862e4952b5abad9ffeb61fbce860730669.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14f898862e4952b5abad9ffeb61fbce860730669.jpeg 2x" data-dominant-color="67856C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题</span><span class="informations">630×531 68.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-05-26 16:49 UTC)

<p>There are many tools in Slicer that allows you to do something like this.</p>
<p>For example, you can use Surface cut effect (in SegmentEditorExtraEffects extension) for defining a smooth cutting surface.</p>
<aside class="quote quote-modified" data-post="1" data-topic="699">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-segment-editor-effects-mask-volume-and-surface-cut/699">New segment editor effects: Mask volume and Surface cut</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    See short demo video of the new “Mask volume” and “Surface cut” Segment editor effects here: 

These effects were developed by Kyle Macneil (Med-i Lab, Queen’s University; SPL, Brigham and Women’s Hospital), with help from <a class="mention" href="/u/lassoan">@lassoan</a>  and <a class="mention" href="/u/fedorov">@fedorov</a> . Thank you for your contribution! 
Mask volume: Blanks out a segment or surrounding area in a volumetric image. Useful for quick removal of unwanted objects (such as CT table) or showing only a selected organ. It can also be used for creating a binary m…
  </blockquote>
</aside>

<p>You can also use <a href="https://discourse.slicer.org/t/new-module-baffle-planner-for-designing-surface-patches/16799">Baffle planner module</a> (in SlicerHeart extension) to create a cutting surface that you can import into a segmentation (by drag-and-dropping the model into the segmentation).</p>
<aside class="quote quote-modified" data-post="1" data-topic="16799">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-module-baffle-planner-for-designing-surface-patches/16799">New module: Baffle planner - for designing surface patches</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    A new module has been added in <a href="https://github.com/SlicerHeart/SlicerHeart#slicerheart-extension-for-3d-slicer">SlicerHeart extension</a> that can be generally used whenever a smooth surface patch needed that conforms to pre-existing anatomical boundary. By default a “soap-bubble” surface is created for the specified curve but the surface shape can be edited by specifying additional surface points in either slice or 3D views. 
The module can generate an infinitely thin open surface, or a closed surface with specified thickness. 
The module can also generate a flattened shape, wh…
  </blockquote>
</aside>

<p>It could be nice to have a <a href="https://github.com/Slicer/Slicer/issues/5606">combination of Draw+Scissors effect</a>. Would you be interested in implementing it? We can help you getting started.</p>

---
