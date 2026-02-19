---
topic_id: 13364
title: "3D Image Generation From A Volumetric Mesh"
date: 2020-09-07
url: https://discourse.slicer.org/t/13364
---

# 3D Image generation from a volumetric mesh

**Topic ID**: 13364
**Date**: 2020-09-07
**URL**: https://discourse.slicer.org/t/3d-image-generation-from-a-volumetric-mesh/13364

---

## Post #1 by @suranga (2020-09-07 07:00 UTC)

<p>I have created a volumetric mesh (FEM) using gmsh and exported it as a .vtk file (i.e. unstructuredGrid).  This FE model consists of a box with an ellipsoid where ellipsoid is located inside of the box. (Scalar range is 1 to 2)</p>
<p>I loaded it as a model in 3D slicer and then used Probe volume with model module to generate a 3D image (i.e. .mhd file). But, unfortunately, I am not able to select the Input Volume in the Probe volume with model (it only consists two values namely rename current node and delete current node) as you can see in the screenshot below.</p>
<p>Did I forget any steps here ? How can I generate a 3D image volume and save it as a .mhd file or .nrrd file format ? Thanks in advance for your time and consideration.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebf8c4187ca90aa23e7a52dbeeb1049f11de577e.png" data-download-href="/uploads/short-url/xFvbqfPbrCkF3lmWCM9oGTkkwnI.png?dl=1" title="slicer_output" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebf8c4187ca90aa23e7a52dbeeb1049f11de577e_2_690x310.png" alt="slicer_output" data-base62-sha1="xFvbqfPbrCkF3lmWCM9oGTkkwnI" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebf8c4187ca90aa23e7a52dbeeb1049f11de577e_2_690x310.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebf8c4187ca90aa23e7a52dbeeb1049f11de577e_2_1035x465.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebf8c4187ca90aa23e7a52dbeeb1049f11de577e_2_1380x620.png 2x" data-dominant-color="63636C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_output</span><span class="informations">1894×852 47.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @steffen-o (2020-09-08 07:48 UTC)

<p>As I understand your post…I think the easiest way to achive your goal is to create an empty  volume per python code :<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_new_volume" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_new_volume</a></p>
<p>and then you can import your model as a segmentation.</p>

---

## Post #3 by @lassoan (2020-09-08 18:27 UTC)

<aside class="quote no-group" data-username="steffen-o" data-post="2" data-topic="13364">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/steffen-o/48/2660_2.png" class="avatar"> steffen-o:</div>
<blockquote>
<p>you can import your model as a segmentation</p>
</blockquote>
</aside>
<p>Segment import was only allowed for surface meshes, but now I enabled it for volumetric meshes, too. If you download Slicer Preview Release tomorrow or later then you can convert volumetric mesh to segmentation then export segmentation to binary labelmap (using right-clicking menu in Data module).</p>

---
