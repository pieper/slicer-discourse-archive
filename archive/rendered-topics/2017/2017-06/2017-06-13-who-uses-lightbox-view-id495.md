# Who uses Lightbox view?

**Topic ID**: 495
**Date**: 2017-06-13
**URL**: https://discourse.slicer.org/t/who-uses-lightbox-view/495

---

## Post #1 by @lassoan (2017-06-13 19:13 UTC)

<p>Slicer can show a lightbox view of slices (mosaic of slightly shifted views along the slice normal). The view can be activated in slice view controller by clicking on the lightbox icon and selecting number of views to show.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9c943863e45258a1fe095ccc103fe496e332633.png" alt="image" data-base62-sha1="zDI5W9FVgL5PdCiPT9y8qtGdZ8T" width="507" height="362"></p>
<p>However, it seems there are many issues with lightbox views:</p>
<ul>
<li>interaction within lightbox views is extremely difficult to implement correctly (see for example this issue <a href="https://issues.slicer.org/view.php?id=1690" class="inline-onebox">fiducial shows in wrong lightbox cell · Issue #1690 · Slicer/Slicer · GitHub</a> - which explains why markups are hidden in lightbox view mode)</li>
<li>very few features work correctly in lightbox view, for example none of these are displayed in lightbox view: model intersections, view ruler, transform display, editor, segment editor, segmentation display, transform display</li>
<li>lightbox views are very slow to operate</li>
<li>lack of metadata (ruler, orientation markers, slice position) makes images difficult to interpret</li>
</ul>
<p>Who uses lightbox view? if you use it, how well it serves your needs?</p>
<p>What do you think about replacing interactive lightbox view with generation of a high-resolution mosaic image (using screen capture of a slice view going through the volume)? It would show all content that is currently shown in slice views (markups, all annotations, slice intersections, etc).</p>
<p>The Screen Capture module already does something very similar, the only difference that it now creates separate images or video, and in this case it would generate a mosaic image. So, the implementation would not be too difficult.</p>

---

## Post #2 by @Amine (2019-12-18 21:18 UTC)

<p>screen capture module gives better control on the output but to make a mosaic view a third party program is needed, an implementation of single-file mosaic in screen capture would be nice.</p>

---

## Post #3 by @pieper (2019-12-18 23:18 UTC)

<p>The <code>CompareVolumes</code> module has a mode for generating a 3x3 lightbox with a few options.</p>

---

## Post #4 by @lassoan (2020-03-25 23:32 UTC)

<p>FYI, a new lightbox view generation feature was added that will replace dynamic lightbox views. See details here: <a href="https://discourse.slicer.org/t/new-lightbox-contact-image-mode-in-screen-capture-module/10840" class="inline-onebox">New lightbox (contact image) mode in screen capture module</a></p>

---
