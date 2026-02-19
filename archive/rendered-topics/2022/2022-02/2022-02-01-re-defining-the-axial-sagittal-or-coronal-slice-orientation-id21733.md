---
topic_id: 21733
title: "Re Defining The Axial Sagittal Or Coronal Slice Orientation"
date: 2022-02-01
url: https://discourse.slicer.org/t/21733
---

# Re-defining the axial, sagittal or coronal slice orientation using a markup-plane

**Topic ID**: 21733
**Date**: 2022-02-01
**URL**: https://discourse.slicer.org/t/re-defining-the-axial-sagittal-or-coronal-slice-orientation-using-a-markup-plane/21733

---

## Post #1 by @Benjamin_T (2022-02-01 14:19 UTC)

<p>Dear support team,</p>
<p>I am currently working on cervical segmentations and find that quite a few of these CTs are not aligned correctly (meaning neck being turned left/right/back/forth). As I am analyzing 2D-segmentations and not 3D-models, it is of interest to get these scans aligned in a similarly upright fashion.</p>
<p>Now, I already found a good video which describes the ways of realigning the 3 CT orientations via using the 3D-model and turning it into the right position (using a transform):</p><div class="youtube-onebox lazy-video-container" data-video-id="AOqeJtE04YM" data-video-title="Transforming Data to Orthogonal Planes   [3D Slicer Workflow]" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=AOqeJtE04YM" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/AOqeJtE04YM/maxresdefault.jpg" title="Transforming Data to Orthogonal Planes   [3D Slicer Workflow]" width="" height="">
  </a>
</div>

<p>This works out but I would like to be more specific about the new orientation: Is there a way of defining a self-drawn plane to become the new axial/coronal/sagittal slice orientation and save it as such for segmentation?</p>
<p>Thank you very much for looking into it!</p>
<p>Benjamin</p>

---

## Post #2 by @mikebind (2022-02-01 17:16 UTC)

<p>If you are using a very recent Slicer Preview release, there is available a few flavors of MarkupsPlane objects which are likely to be helpful for you here (some documentation is <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html">here</a>). You can define the location and orientation of the markups plane by placing control points, and depending on the type of plane definition you choose, these control points can be</p>
<ol>
<li>the plane origin and normal direction</li>
<li>the plane origin and two points which are contained on the plane and define the plane axis directions</li>
<li>any number of control points, and the plane is the best fit plane to the set of points supplied</li>
</ol>
<p>Once placed, a plane can also be manipulated interactively.</p>
<p>To get further on your problem, however, I think you will need to work with some simple linear algebra (vector cross products) and some python code.  Once you have defined one plane, you want to ensure that the other two planes are perpendicular to each other and to the original plane. And, once you have done that, you want to assign the orientations of the slice views to your chosen planes or create a transform based on your chosen planes and apply it to your image volume so that the existing slice view orientations show the planes you want.  This is all very achievable in Slicer, but there are not built-in methods to do it. Slicer is designed for users to easily be able to add functionality which is helpful for them in scripted python modules.</p>
<p>If you want to go this route, there are a lot of resources available (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">a python script repository</a> with examples of accomplishing many types of tasks, a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">developer guide</a>, and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">tutorials</a>) and this forum is a very helpful and friendly place.  You may also decide that the method you’ve found already works well enough for your purposes.</p>

---

## Post #3 by @Benjamin_T (2022-02-17 15:06 UTC)

<p>Thank you very much for your kind and helpful reply. I will contemplate getting into the fundamentals of python.</p>

---
