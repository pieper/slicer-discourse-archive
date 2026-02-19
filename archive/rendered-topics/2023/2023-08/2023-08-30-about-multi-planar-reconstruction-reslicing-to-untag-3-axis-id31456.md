---
topic_id: 31456
title: "About Multi Planar Reconstruction Reslicing To Untag 3 Axis"
date: 2023-08-30
url: https://discourse.slicer.org/t/31456
---

# About multi-planar reconstruction reslicing to untag 3 axis

**Topic ID**: 31456
**Date**: 2023-08-30
**URL**: https://discourse.slicer.org/t/about-multi-planar-reconstruction-reslicing-to-untag-3-axis/31456

---

## Post #1 by @Pinyu_Huang (2023-08-30 22:03 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99253fdfdca61cadf5405fe70c1bfdb4b06abc22.jpeg" data-download-href="/uploads/short-url/lQMRiD0ay5TzkXf6X8IDz6jW1do.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99253fdfdca61cadf5405fe70c1bfdb4b06abc22_2_592x499.jpeg" alt="image" data-base62-sha1="lQMRiD0ay5TzkXf6X8IDz6jW1do" width="592" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99253fdfdca61cadf5405fe70c1bfdb4b06abc22_2_592x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99253fdfdca61cadf5405fe70c1bfdb4b06abc22_2_888x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99253fdfdca61cadf5405fe70c1bfdb4b06abc22.jpeg 2x" data-dominant-color="55545F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1028×868 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dae8837bd38e19951db758f48b2c3640397355b2.png" alt="image" data-base62-sha1="veyfibp7XAa7DqRJ5l9riHMhRMC" width="251" height="201"><br>
Hi there, multi-planar reconstruction view is activated with that click, but each axis are tagged as orthogonal, how can I canceled the binding with only move one axis each time?<br>
Thanks a lot.</p>

---

## Post #2 by @mikebind (2023-08-30 23:47 UTC)

<p>I’m not sure I understand your question, but I think you are asking how to control the orientation of the slicing axis for each individual slice viewer independently.  The controls for that are described here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view" class="inline-onebox" rel="noopener nofollow ugc">User Interface — 3D Slicer documentation</a>.  Use the “Reformat” button to allow you to use controls shown in the 3D view to orient the slicing plane for a slice view independently of all others.</p>
<p>Depending on what you are trying to accomplish, you might also find the keyboard shortcut Ctrl-Alt- on a slice view to rotate the intersecting slicing planes useful, although this approach rotates the other two planes together, so does not allow fully independent reorientation. This is described here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-views" class="inline-onebox" rel="noopener nofollow ugc">User Interface — 3D Slicer documentation</a></p>

---

## Post #3 by @Pinyu_Huang (2023-09-01 02:03 UTC)

<p>Thanks for reply! I apologize for the confusing presentation. In multi-planar reconstruction, if I just move one axis(like the yellow one) in axial plane, the green one will move too, for maintaining orthogonalty. But how can I just move the yellow axis without the green one moving? Thanks a lot!</p>

---

## Post #4 by @yulaomao (2023-09-01 06:04 UTC)

<p>like this？<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/584ed9bd5d698038d46b2f4f8f979c5f51355c0d.jpeg" data-download-href="/uploads/short-url/cBcX8QyQQcZMPIYmzxBYo9h5exf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/584ed9bd5d698038d46b2f4f8f979c5f51355c0d_2_690x356.jpeg" alt="image" data-base62-sha1="cBcX8QyQQcZMPIYmzxBYo9h5exf" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/584ed9bd5d698038d46b2f4f8f979c5f51355c0d_2_690x356.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/584ed9bd5d698038d46b2f4f8f979c5f51355c0d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/584ed9bd5d698038d46b2f4f8f979c5f51355c0d.jpeg 2x" data-dominant-color="262626"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">874×452 40.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @yulaomao (2023-09-01 06:09 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63f51e9754d3b9aab23e06a9130d49e8e5b6ef8c.jpeg" data-download-href="/uploads/short-url/eggr0JiIhqcJhGhWXKQ76Ya2Vre.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63f51e9754d3b9aab23e06a9130d49e8e5b6ef8c_2_690x312.jpeg" alt="image" data-base62-sha1="eggr0JiIhqcJhGhWXKQ76Ya2Vre" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63f51e9754d3b9aab23e06a9130d49e8e5b6ef8c_2_690x312.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63f51e9754d3b9aab23e06a9130d49e8e5b6ef8c_2_1035x468.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63f51e9754d3b9aab23e06a9130d49e8e5b6ef8c.jpeg 2x" data-dominant-color="6C6C7C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1213×549 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Pinyu_Huang (2023-09-04 01:30 UTC)

<p>Thanks a lot! Yes. Can I move the axis in the plane rather than move it in 3D view?</p>

---

## Post #7 by @yulaomao (2023-09-04 03:55 UTC)

<p>I’m sorry, I don’t know how to achieve it through simple settings, but modifying the source code should be able to implement this functionality.</p>

---

## Post #8 by @mikebind (2023-09-05 22:10 UTC)

<p>You can set a slice normal and orientation using python through the <code>SetSliceToRASByNTP()</code> method of vtkMRMLSliceNode objects. I don’t believe there is a way to achieve reorienting a single slice in base 3D Slicer using only GUI elements and without using a 3D view.</p>

---
