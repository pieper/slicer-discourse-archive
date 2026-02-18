# Transform Translation Trouble--Step up/down 10mm

**Topic ID**: 43828
**Date**: 2025-07-23
**URL**: https://discourse.slicer.org/t/transform-translation-trouble-step-up-down-10mm/43828

---

## Post #1 by @pintoman82 (2025-07-23 20:16 UTC)

<p>Hi all,</p>
<p>I’m using 3D Slicer 5.8.1 on macOS and I’m trying to adjust the transform translation step size in the Transform module. By default, when I drag the sliders or click the spinbox arrows, they move by 10 mm increments — which is too coarse for my use case. I’d like to set it to something smaller, like 1 to 0.1 mm. I know I can manually type in values, but I have an insane amount of registrations to do and I think this would make the workflow so much easier.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2025-07-23 20:20 UTC)

<p>I would recommend to use the new interactive transformation handles instead of the spinboxes:</p>
<aside class="quote quote-modified" data-post="1" data-topic="36974">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/new-feature-interactive-transformation-adjustable-center-of-rotation/36974">New feature: Interactive transformation + adjustable center of rotation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Any nodes can now be translated, rotated, or scaled by interactive handles.  Editing operations can be constrained to specific axes and center of rotation can be freely chosen. The handles are available both in slice and 3D views. 
Transform nodes can be easily added and visualized for any node in 3D Slicer by right-clicking on the node in the Subject hierarchy visibility column and checking “Interaction”. 

  <a href="https://www.youtube.com/watch?v=ielxgJS-6SI" target="_blank" class="video-thumbnail" rel="noopener">
    [Transform Interaction Handles in 3D Slicer]
  </a>


<a name="visualization-options-1" class="anchor" href="#visualization-options-1"></a>Visualization options
Visualiza…
  </blockquote>
</aside>

<p>You can easily adjust transforms by dragging handles in slice and 3D views. You can effectively adjust the “step size” by zooming in/out in the view.</p>

---

## Post #3 by @pintoman82 (2025-07-23 22:33 UTC)

<p>Thank you! This has worked wonderfully. Much appreciated.</p>

---
