# Is it possible in any way to smooth the surface without "spoiling" some faces

**Topic ID**: 22071
**Date**: 2022-02-19
**URL**: https://discourse.slicer.org/t/is-it-possible-in-any-way-to-smooth-the-surface-without-spoiling-some-faces/22071

---

## Post #1 by @yoav_benhaim (2022-02-19 22:03 UTC)

<p>hello,<br>
I want to smooth my surface to receive a surface that is one face (to reduce vertices and edges) but I need that some part of the surface would be smooth but stay different faces from all the rest of the surface.</p>
<p>that is my surface after 0.5 smooth factor. in this factor, it becomes one face<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa4e20b0dc0d9dd5a38dda52d6b585e2debb776d.png" alt="image" data-base62-sha1="zIiKPTeqz1SVtgdkLljLFGhiRaJ" width="221" height="187"><br>
the red circles are the places where I want to be different faces from the whole surface</p>
<p>I try to use a lower smooth factor but it becomes too many faces, and also try to use the smoothing effect…<br>
it is very important to me to smooth the model - because I need to produce a simulation in the model and if it is composed of a lot of vertices, edges, and faces are impossible/ on the other hand I need some faces to be the input and output of the simulation.<br>
have you any idea?<br>
thank you for helping!!</p>

---

## Post #2 by @lassoan (2022-02-20 05:50 UTC)

<p>Smoothing does not reduce number of cells (triangle faces). If you want to have less cells then you can use “Decimation” module.</p>
<p>However, if you want to do finite-element analysis then you need to convert the surface mesh to a volumetric mesh. The number of cells in the volumetric mesh mainly depends on the meshing algorithm and parameters and the number of triangles in the input surface mesh should not matter much.</p>
<p>You can use SegmentMesher extension to convert a segmentation to volumetric mesh.</p>

---

## Post #3 by @yoav_benhaim (2022-02-20 13:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="22071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>SegmentMesher</p>
</blockquote>
</aside>
<p>thank you for your response!<br>
in comsol (simulation software) when I use the smooth factor it has an influence on the number of faces, edges ex’. (perhaps the software convert it to volume mesh and in this conversion Occurs)<br>
however, i understand that after that i will need also to reconvert to stl format?<br>
and another question: when trying using TetGen i receive an error</p>
<p>" self-intersection was detected. Program stopped.<br>
Hint: use -d option to detect all self-intersections.</p>
<p>Error: Command ‘tetgen.exe’ returned non-zero exit status 3."<br>
do you know what is “-d option”?</p>
<p>thank you!</p>

---

## Post #4 by @MarkusHeller (2022-02-22 17:08 UTC)

<p>Regarding your tetgen question you could have a look at the tetgen documentation:<br>
<a href="https://wias-berlin.de/software/index.jsp?id=TetGen&amp;lang=1" class="onebox" target="_blank" rel="noopener nofollow ugc">https://wias-berlin.de/software/index.jsp?id=TetGen&amp;lang=1</a></p>
<p>The option appears to do exactly what the hint suggests in that:<br>
-d	Detects self-intersections of facets of the PLC.<br>
although that appears to be the only detail offered on the matter in the documentation.</p>
<p>It might be more effective to address the problem at the source (quality of the segmentation) and you might consider e.g. editing the segmentation manually, or using morphological filters, to minimise the risk to run into such issues.</p>
<p>Most meshing tools benefit from a high-quality triangulation as input, and there are some truly excellent tools available to help with generating such triangulations such as the isotropic remeshing in OpenFlipper (<a href="https://www.graphics.rwth-aachen.de/software/openflipper/" class="inline-onebox" rel="noopener nofollow ugc">Open Flipper - Computer Graphics and Multimedia</a>) or the InstantMeshes app (<a href="https://github.com/wjakob/instant-meshes" class="inline-onebox" rel="noopener nofollow ugc">GitHub - wjakob/instant-meshes: Interactive field-aligned mesh generator</a>).</p>

---
