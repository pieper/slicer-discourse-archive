# Adding colors to a volume (painting)

**Topic ID**: 4191
**Date**: 2018-09-26
**URL**: https://discourse.slicer.org/t/adding-colors-to-a-volume-painting/4191

---

## Post #1 by @Niels (2018-09-26 09:20 UTC)

<p>Hi all,</p>
<p>I have a question regarding the editing/ painting of volumes. I would like to craft a color-version of my CT scan and ideally, I would like to follow the following workflow:</p>
<ol>
<li>Load a scan (grayscale)</li>
<li>Load a colortable to translate the grayscale values to colors</li>
<li>Create a new colorvolume from scan+colortable</li>
<li>Edit the colors in the colorvolume using a paint tool.</li>
</ol>
<p>I experimented a bit with the Volume and Editor module. But I can not get it to work. I can create an empty label node, but that one is not filled with colors coming from the colortable I selected in Volumes. In the Editor module itself I am only able to select a couple of predefined colors, there is no colorpicker.</p>
<p>Does anybody have any hits or a different approach to the coloring of scans?</p>

---

## Post #2 by @timeanddoctor (2018-09-26 10:26 UTC)

<aside class="quote" data-post="5" data-topic="1789">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/using-glsl-post-process-2d-pixel-shader-with-slicer/1789/5">Using GLSL post-process (2D) pixel shader with Slicer</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Here’s the other GLSL code <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> mentioned.  It’s less coupled to the vtk rendering process so it can make it simpler to do generic algorithms.  At some point I plan to revisit this and see how it compares to the shader options recently added to VTK core and see if it’s still needed.
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2018-09-26 14:26 UTC)

<p>You can easily achieve all this using Segment Editor module. Threshold effect can be used to assign segments (colored regions) to a grayscale range. If you have many segments then you can automate segment creation by 10-20 lines of Python code - see “skin surface extraction” example in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">script repository</a>.</p>

---

## Post #4 by @Niels (2018-09-27 10:37 UTC)

<p>Sound worth a try!</p>
<p>Yesterday I thought of another approach: what about iterating the voxel array and sampling the displayNode colorMapper to get a color value. Then for each voxel I can write its colorvalue to a labelmap or some other format that can store rgb values?</p>

---

## Post #5 by @lassoan (2018-09-27 11:43 UTC)

<p>What data would you like to have at the end? What would you use it for?</p>

---

## Post #6 by @Niels (2018-09-27 12:14 UTC)

<p>In the end I would like to have a color volume that represents color, not grayscale. I would like to use it as a 3DTexture for rendering in OpenGL or Direct3D.</p>

---

## Post #7 by @lassoan (2018-09-27 12:21 UTC)

<p>For this purpose, a color lookup table is the appropriate solution. It is much more efficient in term of storage space and rendering speed and much more flexible (you can change color/opacity on-the-fly).</p>

---
