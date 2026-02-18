# Exporting volume (3D texture)?

**Topic ID**: 1103
**Date**: 2017-09-22
**URL**: https://discourse.slicer.org/t/exporting-volume-3d-texture/1103

---

## Post #1 by @John_D (2017-09-22 13:30 UTC)

<p>I’m totally new to Slicer and fairly new to DICOM, working on CT data. My use-case is using Slicer to export data-sets for real-time rendering and high performance.</p>
<p>I’ve already seen tutorials on using Slicer to create 3D meshes/surfaces from my CT dataset using thresholds, and I think these meshes can be saved as STL(?)</p>
<p>Another thing I’d like to do is convert the DICOM CT dataset into a raw 3D volume and export this as a 3D texture/image. I’m not sure I know the correct terminology because while I find material on volume rendering, this specific task I cannot find instructions for. Is it something I can easily do?</p>

---

## Post #2 by @lassoan (2017-09-22 13:42 UTC)

<aside class="quote no-group" data-username="John_D" data-post="1" data-topic="1103">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/f6c823/48.png" class="avatar"> John_D:</div>
<blockquote>
<p>I’ve already seen tutorials on using Slicer to create 3D meshes/surfaces from my CT dataset using thresholds, and I think these meshes can be saved as STL(?)</p>
</blockquote>
</aside>
<p>Yes. The process is described for example in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation_for_3D_printing">this tutorial</a>.</p>
<aside class="quote no-group" data-username="John_D" data-post="1" data-topic="1103">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/f6c823/48.png" class="avatar"> John_D:</div>
<blockquote>
<p>convert the DICOM CT dataset into a raw 3D volume and export this as a 3D texture/image</p>
</blockquote>
</aside>
<p>You can visualize many structures very nicely using volume rendering of the CT volume. To get nice colorful images, you need to map CT voxel values to color&amp;opacity RGBA values (and there are a couple of tricks to make the rendering faster and nicer). Volume rendering is a well-established technique, most likely you can find existing implementation on any platforms, so probably you don’t need to implement it yourself.</p>

---

## Post #3 by @John_D (2017-09-22 14:43 UTC)

<p>Thankyou.</p>
<p>I can appreciate many toolkits  automatically do volumetric rendering from<br>
a set of slices, but I would still be interested to know if there is a way<br>
I can directly export this. In other words use Slicer to load a CT<br>
dataset’s set of slices, and export effectively just a 3D array of this.<br>
For real-time, performance rendering, 3D textures may be applied to<br>
polygonal meshes so having the volumetric data in this raw form is still<br>
useful to me.</p>
<p>Since as I understand it a CT scan contains multiple sets of slices from<br>
multiple axes, how to combine these is not obvious to me… I could simply<br>
take all the slices in one axes and stack them into a volume but that would<br>
lose a substantial amount of data!</p>
<p>Apologies if this isn’t clear, the terminology I use is not necessarily the<br>
same as yours.</p>

---

## Post #4 by @cpinter (2017-09-22 15:05 UTC)

<p>Volume rendering is only a visualization technique. There is no way to “export” volume rendering, because it is created <em>directly</em> from the CT volume and a transfer function determining the colors and opacities for the density values in the CT voxels. Read more here</p><aside class="quote quote-modified" data-post="1" data-topic="524">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b19c9b/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524">Save volume rendering as STL file</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, I am a new user on 3D slicer. 
I was using the display preset feature under volume rendering, and I was wondering if there is a way to save what I was viewing as an .stl or 3D printable file. 
For example, I was viewing a sample MRI using the CT-cardiac3 preset display. 
When I tried to save that specific 3D preset displayed sample in a .stl file, the option was unavailable. 
I was only able to see .vp (volume property), .txt formats. 
Is there a way to accomplish what I desire in 3D slic…
  </blockquote>
</aside>


---
