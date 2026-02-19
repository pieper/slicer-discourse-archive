---
topic_id: 18585
title: "Measuring Error Between Desired And Current Trajectories"
date: 2021-07-08
url: https://discourse.slicer.org/t/18585
---

# Measuring Error between desired and current trajectories

**Topic ID**: 18585
**Date**: 2021-07-08
**URL**: https://discourse.slicer.org/t/measuring-error-between-desired-and-current-trajectories/18585

---

## Post #1 by @Ahmet_Yildiz (2021-07-08 16:42 UTC)

<p>I am working on designing and following pre-defined and in real-time trajectories in brain interventions in Slicer.<br>
I am wondering whether there is a module/way to calculate in real-time the error between desired and current trajectory for a pre-inserted cannula so the surgeon can re-align the current trajectory to meet desired one before insertion, i made a rough image from 3D Slicer,</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/985117ee22fc094b5bd7e720ad17b323d52a7b7c.jpeg" alt="image" data-base62-sha1="lJsjGoVW9eTqsTOSRhsQsFBgKkY" width="630" height="370"></p>
<p>Thank you so much,</p>

---

## Post #2 by @ungi (2021-07-09 01:45 UTC)

<p>I don’t think there is a specific module for this. I would measure the distance between the planned and actual entry points and target (tip) points of the cannula. You can also calculate the angle between the two lines. While there may be no module that does exactly this, you could export the line end-points as tables and do the calculations in Excel, or if you are familiar with Python, you could quickly implement a script or a module that does these calculations inside Slicer.</p>

---

## Post #3 by @Ahmet_Yildiz (2021-07-10 15:33 UTC)

<p>Thank you so much Dr. Ungi for your amazingly straightforward reply,<br>
I found a previously written code on Slicer documentation page;<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-angle-between-two-markup-lines" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-angle-between-two-markup-lines</a></p>
<p>I worked on the code to further fit my needs that is to decompose the measured angle the its x, y and z components,<br>
My summary of what i did is that in order to get the x, y, and z angles between two vectors, i took the dot product of the projections of the two vectors onto the orthogonal plane of the axis i want. That is, if i wanted the z-angle between the two vectors, create xy-plane vectors of the originals. To do this, a vector that ignores the z-component of the vectors is made.</p>
<p>I went through linear algebra and the code got missy little bit, i shared a section of it for illustration.</p>
<p>Is there a function/library for example similar to “vtk.vtkMath.AngleBetweenVectors” that can decompose the measured angle into x, y and z?</p>
<p>Thank you so much for your time!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9cafeac2a710a1ac42e965d5d38103fc906910e7.png" data-download-href="/uploads/short-url/mm7nVnpDaG5yY1eOhWmJ0cwRSzZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cafeac2a710a1ac42e965d5d38103fc906910e7_2_690x304.png" alt="image" data-base62-sha1="mm7nVnpDaG5yY1eOhWmJ0cwRSzZ" width="690" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cafeac2a710a1ac42e965d5d38103fc906910e7_2_690x304.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cafeac2a710a1ac42e965d5d38103fc906910e7_2_1035x456.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cafeac2a710a1ac42e965d5d38103fc906910e7_2_1380x608.png 2x" data-dominant-color="434442"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1553×685 50.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @ungi (2021-07-10 16:39 UTC)

<p>You could probably simplify the code. To normalize a vector (in numpy format), you can just divide it by its norm: v = v / np.linalg.norm(v)<br>
Since X, Y, and Z axes in your case are (1,0,0), (0,1,0), (0,0,1), you could simplify the projection of a vector v to the YZ plane by doing this: v[0] = 0.0<br>
So the angle in the “sagittal” plane between two vectors (v and w) would be:<br>
v[0] = 0.0<br>
w[0] = 0.0<br>
vtk.vtkMath.AngleBetweenVectors(v, w)</p>
<p>For the record, I don’t alway like to use the AngleBetweenVectors, because the result doesn’t give me a sense of direction. E.g. I cannot tell if w is in flexion or extension relative to v, if we are talking in anatomical terms. If you calculate the angle using cross product, and you have a reference direction vector d, then you can compute the dot product of the cross product: np.dot(np.cross(v,w),d) and the sign of the result will tell you if w is clockwise or counter-clockwise relative to v if you look at them from that particular direction d. You can safely ignore this paragraph if you are only interested in the absolute value of the angle.</p>

---
