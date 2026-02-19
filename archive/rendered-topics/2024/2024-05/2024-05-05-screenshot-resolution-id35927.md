---
topic_id: 35927
title: "Screenshot Resolution"
date: 2024-05-05
url: https://discourse.slicer.org/t/35927
---

# Screenshot Resolution

**Topic ID**: 35927
**Date**: 2024-05-05
**URL**: https://discourse.slicer.org/t/screenshot-resolution/35927

---

## Post #1 by @chris_nik (2024-05-05 14:20 UTC)

<p>Hello all,</p>
<p>I have noticed that when I do an “Annotation Screenshot” with Scale factor 5.0x, the resolution of the Screenshot matches the resolution of the Slice in Slicer. However, when I zoom into the Screenshot, I get progressively lower resolutioin compared to zooming on the same area in the Slice View in Slicer.</p>
<p>I figured this is normal because the Screenshot is a snapshot of the current zoom in Slicer. However, is there a way to create a Screenshot that keeps the information of the DICOM when zooming in outside of Slicer, and doesn’t lose resolution?</p>
<p>Regards</p>

---

## Post #2 by @pieper (2024-05-05 17:59 UTC)

<p>This technique could be adapted to work on the slice views too, I believe:</p>
<aside class="quote quote-modified" data-post="11" data-topic="35813">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-include-markup-annotations-in-scene-reconstruction-for-screen-capture/35813/11">How to Include Markup Annotations in Scene Reconstruction for Screen Capture</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    That’s a great idea! 
You can resize the window to any size - does not matter how large your display is (I’ve tested it on Windows, I don’t see a reason why it would not work on other operating systems or window managers). So, a code snippet to render a 3D view at arbitrarily high resolution: 
Set up a 3D view outside the main view layout: 
# Switch to a layout that has a window that is not in the main window
layoutManager = slicer.app.layoutManager()
originalLayout = layoutManager.layout
layou…
  </blockquote>
</aside>


---
