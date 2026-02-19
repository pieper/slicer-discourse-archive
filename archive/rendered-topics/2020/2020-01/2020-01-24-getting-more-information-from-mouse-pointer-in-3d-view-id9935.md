---
topic_id: 9935
title: "Getting More Information From Mouse Pointer In 3D View"
date: 2020-01-24
url: https://discourse.slicer.org/t/9935
---

# Getting more information from mouse pointer in 3D view

**Topic ID**: 9935
**Date**: 2020-01-24
**URL**: https://discourse.slicer.org/t/getting-more-information-from-mouse-pointer-in-3d-view/9935

---

## Post #1 by @Niels (2020-01-24 10:11 UTC)

<p>Hello slicer developers,</p>
<p>For my module I need the user to mouse click in the 3D view and see if it hits the 3D model. I found this example:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model</a></p>
<p>and this user that did something similar:</p>
<aside class="quote" data-post="1" data-topic="7753">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/select-cells-of-a-3d-model/7753">Select cells of a 3D model</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    how to create a mouse event inside the 3d slicer view. Need to pick cells from a mesh object from within the 3d slice view of the slicer. 
Need help
  </blockquote>
</aside>

<p>Is there also a way to read a mouse button event in the 3D view?<br>
Is there another way to get the 2D or 3D mouse coordinates from the 3D view?</p>

---

## Post #2 by @Niels (2020-01-24 11:47 UTC)

<p>I think this might solve part of my problem:</p><aside class="quote" data-post="9" data-topic="2726">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segment-editor-and-rotate-tumble-orbit-function-in-3d-view/2726/9">Segment Editor and rotate/tumble/orbit function in 3D view</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’ve made painting/erasing in 3D view optional. It should be available in nightly builds that you download tomorrow or later. I’ve also added “smudge” option to Paint effect: auto-select segment at click position, which should help in minimizing switching between segments when adjusting boundaries between them. I’ve also added option to erase all segments (not just the selected segment) using Erase effect.
  </blockquote>
</aside>

<p>This seems to hit the model in the 3D view and identify the slice coordinates? if so i need to capture the mouse click-events en calculate the RAS coords.</p>

---

## Post #3 by @lassoan (2020-01-24 15:36 UTC)

<p>You can either use <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model">crosshair node</a> or a markups node (in Slicer Preview Releases, when markups is in place mode, you can <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer">get the 3D coordinates</a> of the mouse cursor from the markups node).</p>

---

## Post #4 by @Niels (2020-01-24 16:12 UTC)

<p>Hi Andras,<br>
Yes using a markup node seems to work as well. For me it would work best if it is placed when a key is pressed or moushe click recorded in the 3D view. So i can remove it when the key or mouse button is released. Is there a way to record that in the 3D view?</p>

---

## Post #5 by @lassoan (2020-01-24 16:34 UTC)

<p>When you click with the mouse then the markup is placed, which changes the state of that markup point. You can observe state changes similarly to position changes. If you don’t need to keep displaying the markup then you can delete it right after the point is placed.</p>

---
