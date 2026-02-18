# How to do cross section with free angle?

**Topic ID**: 10016
**Date**: 2020-01-30
**URL**: https://discourse.slicer.org/t/how-to-do-cross-section-with-free-angle/10016

---

## Post #1 by @Illusion (2020-01-30 03:57 UTC)

<p>Slicer version: 4.10.2</p>
<p>How to use the slicer to do free-angle cross-section, not only the three anatomy planes?<br>
How could I get the cross-section like the several cross-sections in blue planes?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b79351190c09b24183806417c95514bb44ba0b01.png" alt="Untitled" data-base62-sha1="qbZ078hiwWXbB7VzoqW61GXvt7z" width="432" height="412"><br>
Thank you very much!</p>

---

## Post #2 by @lassoan (2020-01-30 04:02 UTC)

<p>There are many options, for example:</p>
<ul>
<li>Option A: Reformat module can be used to adjust angles of slice views using sliders</li>
<li>Option B: Show reslice widget in slice view and then adjust reslice plane in 3D views:</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11220132d775341d8b38aecc844a09d50c6097bd.png" data-download-href="/uploads/short-url/2ryYfbCyfCPOlZBKvRNUya5m6UR.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11220132d775341d8b38aecc844a09d50c6097bd_2_690x317.png" alt="image" data-base62-sha1="2ryYfbCyfCPOlZBKvRNUya5m6UR" width="690" height="317" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11220132d775341d8b38aecc844a09d50c6097bd_2_690x317.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11220132d775341d8b38aecc844a09d50c6097bd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11220132d775341d8b38aecc844a09d50c6097bd.png 2x" data-dominant-color="F2E9E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">833×383 26.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Option C: Use recent Slicer preview release, show slice intersections, and use Ctrl+Alt+Left-click-and-drag to rotate intersecting slice views around the slice intersection point.</li>
</ul>

---

## Post #3 by @Illusion (2020-01-30 04:18 UTC)

<p>Hi Andras,</p>
<p>Thank you very much for your help!</p>
<p>Could you please teach me which python package and API should I use to write python codes for getting multiple cross-sections automatically as desired?</p>

---

## Post #4 by @lassoan (2020-01-30 04:31 UTC)

<p>I’m not sure what you mean. Would you like to show a number of slice views in a 3D view, rotated by different angles? What is the clinical application? Would you like to compute Cobb angle? Reslice the image along the spinal chord curve? …?</p>

---

## Post #5 by @Illusion (2020-01-30 04:36 UTC)

<p>I would like to write codes in python, to get cross-sections just like the figure in my first post above.<br>
I.e., for each vertebra, I would like to get four cross-sections.</p>
<p>Assume I assign an array of starting points for each vertebra along with four rotation angles, how can I write python codes to get cross-sections and save the images?</p>

---

## Post #6 by @lassoan (2020-01-30 04:44 UTC)

<p>You can switch to a layout that has at least as many slice views as you need (e.g., “Four over four” built-in layout, or a custom layout that you specify), set the slice view positions/orientations by modifying the matrix returned by <code>sliceNode.GetSliceToRAS()</code>, and show the slice views in 3D. You can then switch to any layout, the slices will remain visible in 3D view.</p>
<p>There are lots of related examples in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">Slicer script repository</a>.</p>

---

## Post #7 by @Illusion (2020-03-09 23:05 UTC)

<p>Hi Iassoan,</p>
<p>I am able to manually control the reformat widget now. However, not accurate.</p>
<p>Could you please let me know what is the python function to program the position and angle of anatomy plane reformat widget?</p>
<p>Thank you very much!</p>

---

## Post #8 by @lassoan (2020-03-09 23:42 UTC)

<p>As I wrote above, there are many examples of slice manipulations in the script repository, see for example, <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_slice_orientation">this</a>.</p>

---

## Post #9 by @Illusion (2020-03-11 03:02 UTC)

<p>Hi Iassoan,</p>
<p>I found a existing module “Reformat”, which can do exactly what I want.<br>
However, I was not able to find the source file in the Slicer installation folder.</p>
<p>I did a lot of search locally on the disk, and still cannot find the module find, even though I can run the module. <img src="https://emoji.discourse-cdn.com/twitter/innocent.png?v=9" title=":innocent:" class="emoji" alt=":innocent:"><br>
It seems that the file of the link below is not in the installation folder. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Reformat/qSlicerReformatModule.h" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Reformat/qSlicerReformatModule.h</a></p>
<p>Could you please let me know where to find the souce file of module Reformat such that I can debug the module?</p>
<p>Thank you very much!</p>

---

## Post #10 by @lassoan (2020-03-11 12:08 UTC)

<p>You can find all the source files in the same folder. It is a C++ module, which is compiled into a dynamically loadable library. The source files are not used at runtime and so they are not included in the install package.</p>

---

## Post #11 by @Illusion (2020-03-11 19:17 UTC)

<p>Thank you for your help, Iassoan!<br>
I figured out how to do it. <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>
<p>One last question, any link that demonstrated how to debug the C++ codes with Slicer API?</p>

---

## Post #12 by @lassoan (2020-03-12 22:34 UTC)

<p>This topic should help. If you still have questions then let us know.</p>
<aside class="quote" data-post="1" data-topic="9882">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbahegne/48/4837_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/debugging-step-by-step/9882">Debugging step by step</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hello, 
I created a C++ extension, which works quite fine but i never managed to make to debugger work. 
I tried with several IDE QtCreator, Kdevelop, Clion, I correctly set the CMAKE_BUILD_TYPE Flag to debug (for my extension and for 3D Slicer), and each time i can’t get breakpoints working. It seems that debug symbols are not generated. 
Am I missing something ?
  </blockquote>
</aside>


---

## Post #13 by @Alice (2020-10-08 02:34 UTC)

<p>Hi,I also encountered the same problem, I also need to extract a certain angle of section.  Can you tell me how  you solved it?</p>

---

## Post #14 by @lassoan (2020-10-08 05:04 UTC)

<p>Do these options work for you?</p><aside class="quote quote-modified" data-post="2" data-topic="10016">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-do-cross-section-with-free-angle/10016/2">How to do cross section with free angle?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    There are many options, for example: 

Option A: Reformat module can be used to adjust angles of slice views using sliders
Option B: Show reslice widget in slice view and then adjust reslice plane in 3D views:

[image] 

Option C: Use recent Slicer preview release, show slice intersections, and use Ctrl+Alt+Left-click-and-drag to rotate intersecting slice views around the slice intersection point.
  </blockquote>
</aside>

<p>Since then we also added free slice rotation option by Ctrl/Cmd+Alt+Left-click-and-drag in slice views (around the slice intersection point, so you need to enable display of slice intersection in the toolbar, in the crosshair button’s drop-down menu).</p>
<p>You may also find “Valve view” module useful (provided by SlicerHeart extension), which allows rotating two orthogonal slice views around the plane normal of a third slice view.</p>
<p>If you want to reslice along a curve then you can use “Cross-section analysis” module (provided by SlicerVMTK extension).</p>
<p>You can find several examples for setting slice orientation from a Python script. If they don’t do what you want then let us know what you would like to achieve.</p>

---

## Post #15 by @Alice (2020-11-04 02:37 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9675d1b70106bfd2d20f7ff9f90a32cf9bed3c8.png" data-download-href="/uploads/short-url/v1f48KGnfRbUUvEvSwUsrMR8Y4g.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9675d1b70106bfd2d20f7ff9f90a32cf9bed3c8_2_690x495.png" alt="image" data-base62-sha1="v1f48KGnfRbUUvEvSwUsrMR8Y4g" width="690" height="495" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9675d1b70106bfd2d20f7ff9f90a32cf9bed3c8_2_690x495.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9675d1b70106bfd2d20f7ff9f90a32cf9bed3c8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9675d1b70106bfd2d20f7ff9f90a32cf9bed3c8.png 2x" data-dominant-color="9C9DCC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">693×498 72.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This is my image.The module "Extract Centerline " just only shows the mean diameter , and the module “Airway Inspector” just calculates one airway,but I want to calculate several pairs of inner radius and outer radius along the centerline.</p>

---

## Post #16 by @lassoan (2020-11-04 02:42 UTC)

<p>The radius does not change much within a segment, so the mean value characterizes a branch quite well. But if you need more details then you can get the radius for each curve point from the output model node (stored in point data array).</p>
<p>What do you mean by inner and outer radius?</p>

---

## Post #17 by @Alice (2020-11-04 02:49 UTC)

<p>Is that? I will try it.<br>
Inner and outer diameter are the output of the module “Airway Inspector” , represent the airway’s inner diameter and outer diameter which contains the thickness of the airway wall.</p>

---

## Post #18 by @Alice (2020-11-04 03:00 UTC)

<p>What do you mean by “the output model node (stored in point data array)”? I just find the ID and coordinates of every point in each curve.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37bd8b76083f0008bdefdea64561fdb77e111101.png" data-download-href="/uploads/short-url/7X6meJlSOdR3MT7HQS5JcfIiuYN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37bd8b76083f0008bdefdea64561fdb77e111101.png" alt="image" data-base62-sha1="7X6meJlSOdR3MT7HQS5JcfIiuYN" width="668" height="500" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">677×506 9.65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #19 by @Team_Python (2024-02-27 15:48 UTC)

<h3><a name="p-107539-how-to-create-cross-sectional-view-dentistry-1" class="anchor" href="#p-107539-how-to-create-cross-sectional-view-dentistry-1" aria-label="Heading link"></a>How to create cross sectional view (dentistry)?</h3>
<p>Hello Sir  I have heard about you that you work with DICOM. I have a question. I have been stuck on this task for several months, but I am not understanding how to proceed. I work in dentistry, and I want to use the Python programming language to extract individual teeth from DICOM images, similar to what is shown in this gif. But sir, I am very distressed. I have tried creating sagittal, coronal, axial, and panoramic X-ray images, but I am unable to achieve this. I am not able to understand it. Please guide me. I am waiting for your response. Thank you.</p>

---
