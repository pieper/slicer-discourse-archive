# How to export the Volume Rendering into models?

**Topic ID**: 1019
**Date**: 2017-09-08
**URL**: https://discourse.slicer.org/t/how-to-export-the-volume-rendering-into-models/1019

---

## Post #1 by @doc-xie (2017-09-08 03:56 UTC)

<p>Hello,everyone!<br>
How to explore the result of Volume Rendering into models?</p>

---

## Post #2 by @deepmech (2017-09-08 04:28 UTC)

<p>:-1)In scientific visualization and computer graphics, <em>volume<br>
rendering</em> is a set of techniques used to                        display a<br>
2D projection of a 3D discretely sampled data set, typically a 3D scalar<br>
field.<br>
2)so what you will see in models is just the 3D image.<br>
3) what else you want to know you should specify and according to<br>
that other modules are available<br>
according to me but i am also new user</p>

---

## Post #3 by @doc-xie (2017-09-08 10:09 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f5464b1212a16eaa1d073291c4d099866180b0f.png" data-download-href="/uploads/short-url/krX5Aw6bktolPdT8QkdDEffnAM7.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f5464b1212a16eaa1d073291c4d099866180b0f_2_690x483.png" alt="Screenshot" data-base62-sha1="krX5Aw6bktolPdT8QkdDEffnAM7" width="690" height="483" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f5464b1212a16eaa1d073291c4d099866180b0f_2_690x483.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f5464b1212a16eaa1d073291c4d099866180b0f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f5464b1212a16eaa1d073291c4d099866180b0f.png 2x" data-dominant-color="948A8B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">874×613 307 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The result of CTA with Volume Rendering is much better than any other modules,but the 3D view can not be saved solely.<br>
What i want to know is how to save the 3D view in the proper format,so we can edit the result just like models.</p>

---

## Post #4 by @deepmech (2017-09-08 13:21 UTC)

<p>after volume rendering use segmentation&gt;export(the last option)&gt; there are<br>
some format</p>

---

## Post #5 by @lassoan (2017-09-08 13:24 UTC)

<p>Volume rendering is a visualization technique. No data is generated that could be exported to models (surface meshes). See detailed explanation in this topic:</p>
<aside class="quote quote-modified" data-post="1" data-topic="524">
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

## Post #6 by @EestiMees (2017-12-28 07:24 UTC)

<p>My understanding is that volumetric rendering is essentially a function (often specific to a tissue and/or imaging modality) which, given a 3D volume (let’s say just a CT volume with voxels with intensity values from 0 to 1), assigns color or intensity/magnitude values and opacity values to each voxel. It is therefore different data than the original 3D volume (although it could be instantly re-created by combining the original volume and the function). When I use the word function I am referring to the display preset in Slicer such as “MR-Default”.</p>
<p>I understand that volume data is inherently different from a surface mesh. However, it would still be useful to be able to export the volumetric rendering as a 3D matrix of intensity values (or color values) with associated opacity values. This would be tremendously useful for a variety of reasons which is why this topic seems to be so popular. I think that many folks are seeing some potential in the Slicer volumetric segmentation module and they want to export some of this secret sauce for use in their own applications/projects.</p>
<p>Is there any way to do this using Slicer?</p>

---

## Post #7 by @lassoan (2017-12-28 14:14 UTC)

<aside class="quote no-group" data-username="EestiMees" data-post="6" data-topic="1019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/e8c25b/48.png" class="avatar"> EestiMees:</div>
<blockquote>
<p>it would still be useful to be able to export the volumetric rendering as a 3D matrix of intensity values (or color values)</p>
</blockquote>
</aside>
<p>By burning in looked-up RGBA values into the voxel array you would remove a trivial look-up step, but you would make the data unusable for rendering, as you would lose ability to estimate surface normal from voxel gradient. You could save gradient in a separate volume but then you would end up with a more complicated rendering task overall, increased memory need (about 5x more), and complete inflexibility in how you display your data. This does not seem useful to me and that’s why this kind of data export is not implemented in Slicer (or elsewhere).</p>

---

## Post #8 by @cpinter (2018-01-03 15:48 UTC)

<p>Yes, probably exporting the volume after applying the transfer function would not be too useful.</p>
<p>But maybe we could use some information from volume rendering for simple segmentation. How about allowing the user to specify the desired “color” for thresholding? We could determine the original voxel values from that color (using the transfer function) and a tolerance factor maybe, and do a thresholding to include that interval.</p>

---

## Post #9 by @lassoan (2018-01-03 16:07 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="8" data-topic="1019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>maybe we could use some information from volume rendering for simple segmentation</p>
</blockquote>
</aside>
<p>I think live preview in slice views in Threshold effect already makes threshold setting quite easy. With multi-volume rendering (that has just been <a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/3699">merged into VTK master</a> today) we will be able to show a live preview in 3D views, too.</p>

---

## Post #10 by @lassoan (2019-03-18 13:13 UTC)

<p>4 posts were split to a new topic: <a href="/t/convert-model-to-volume-rendering/6192">Convert model to volume rendering</a></p>

---

## Post #11 by @sobiny (2020-03-26 17:54 UTC)

<p>This is an automatic translation from google:<br>
I used to worry about not being able to export STL, because I was mainly used in 3d printing. It doesn’t bother me anymore. If I just want to display a certain DICOM CT sequence, I use python + VTK to display directly, it will be very fast. If it is a general application for 3d printing, I will use python + ITK + VTK to directly export the STL file from the image. If it is for web display, in fact webgl2 now supports 3D rendering. Directly loading files in NRRD or other formats can render as beautiful as slicer.</p>
<p><a href="https://discourse.slicer.org/u/doc-xie">谢博士</a>：我曾经也一直在为不能导出STL而烦恼，因为我主要用于3d打印领域。后面也不困扰了。如果我只是要显示某个DICOM CT序列的话，我直接用python + VTK来进行显示，会非常快。如果是为了3d打印的常规应用，我会用python+ITK+VTK来直接根据影像导出STL文件。如果是为了web显示，实际上现在webgl2支持三维渲染啊，直接载入NRRD或者其他格式的文件，可以渲染得和slicer一样漂亮。</p>

---

## Post #12 by @lassoan (2020-03-26 18:06 UTC)

<p>What you write is true if you only work with CT images and you are only interested in bones.</p>

---

## Post #13 by @sobiny (2020-03-26 19:08 UTC)

<p>3d slicer is a good medical image pre-processing software, but not everyone will operate 3d slicer, so after segmenting the image, I use the “mask volume” method of the “Segment Editor” module to fill other valves Value, then export to “nrrd” format, and finally use vtk.js or three.js for web rendering, you can get a beautiful image.<br>
It’s not just CT. But I usually use CT.<br>
I give an example:<br>
This time depends on the condition of the lungs</p>
<ol>
<li>Use the 3D slicer’s “Chest Imaging Platform (CIP)” tool to match the approximate location of the lung model.</li>
<li>“margin” this Segment</li>
<li>“mask volume” method fills in other thresholds.</li>
<li>Export as nrrd.</li>
<li>According to the “CT-Air” rendering value, add the color and CT value of the infected part.</li>
<li>Render in python + vtk. Of course I can also render in webgl + vtk.js.</li>
</ol>
<p>Of course, now I have made a small plug-in for 3d slicer to complete the above steps 1-5 fully automatically. I did the above steps just to separate out the air outside the body. Otherwise, it looks like this:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/452860f9675fd74321bcc4019795cf5b32ed782a.jpeg" data-download-href="/uploads/short-url/9RNsjnc7NUPyBiyPdm6nZRw8q3E.jpeg?dl=1" title="微信图片_20200327030304" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/452860f9675fd74321bcc4019795cf5b32ed782a_2_690x394.jpeg" alt="微信图片_20200327030304" data-base62-sha1="9RNsjnc7NUPyBiyPdm6nZRw8q3E" width="690" height="394" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/452860f9675fd74321bcc4019795cf5b32ed782a_2_690x394.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/452860f9675fd74321bcc4019795cf5b32ed782a.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/452860f9675fd74321bcc4019795cf5b32ed782a.jpeg 2x" data-dominant-color="638397"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20200327030304</span><span class="informations">1026×587 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After processing and segmentation, it looks like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66bbbbd8eccc666c8020790c3289266b185f247f.jpeg" data-download-href="/uploads/short-url/eEOV1wBxRDYQfUqPxQ1h66MvCnd.jpeg?dl=1" title="微信图片_20200327030315" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66bbbbd8eccc666c8020790c3289266b185f247f_2_653x500.jpeg" alt="微信图片_20200327030315" data-base62-sha1="eEOV1wBxRDYQfUqPxQ1h66MvCnd" width="653" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66bbbbd8eccc666c8020790c3289266b185f247f_2_653x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66bbbbd8eccc666c8020790c3289266b185f247f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66bbbbd8eccc666c8020790c3289266b185f247f.jpeg 2x" data-dominant-color="1D3D70"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20200327030315</span><span class="informations">690×528 93.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60d3255b5ec5c9de2f02497dd248c656eaa13a01.png" data-download-href="/uploads/short-url/dOydljr8T8ht0YtPABYpGCWWj6N.png?dl=1" title="微信图片_20200327030324" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60d3255b5ec5c9de2f02497dd248c656eaa13a01_2_653x500.png" alt="微信图片_20200327030324" data-base62-sha1="dOydljr8T8ht0YtPABYpGCWWj6N" width="653" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60d3255b5ec5c9de2f02497dd248c656eaa13a01_2_653x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60d3255b5ec5c9de2f02497dd248c656eaa13a01.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60d3255b5ec5c9de2f02497dd248c656eaa13a01.png 2x" data-dominant-color="1E4173"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20200327030324</span><span class="informations">690×528 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So it’s not just CT and bones.<br>
Sorry, I ’m Chinese, I do n’t speak English well, I use google translation,</p>

---

## Post #14 by @lassoan (2020-03-26 19:39 UTC)

<p>I meant that there are very few things that you can easily visualize directly in native images. If you segment structures in Slicer then you can certainly use simple viewers to visualize the exported results (segmentations, masked volumes, etc.).</p>
<p>Having simple web-based viewers make sense and there are lots of them. For medical imaging, OHIF viewer is particularly good.</p>

---

## Post #15 by @sobiny (2020-03-26 19:56 UTC)

<p>yes，you are right。<br>
It seems that there is a character limit in posting, so I have to say another word</p>

---
