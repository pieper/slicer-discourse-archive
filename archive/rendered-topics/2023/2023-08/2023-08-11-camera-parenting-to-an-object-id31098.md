# Camera parenting to an object

**Topic ID**: 31098
**Date**: 2023-08-11
**URL**: https://discourse.slicer.org/t/camera-parenting-to-an-object/31098

---

## Post #1 by @B4D (2023-08-11 06:11 UTC)

<p>A video is attached in what I want to achieve.  We have the ability to create objects in Blender and port them into 3D slicer.<br>
I need to be able to parent or link my camera in Slicer to the object plane, so that when it translates I will get to see the segment in the yellow slice.<br>
Is this a possibility?</p>
<div class="youtube-onebox lazy-video-container" data-video-id="ZPuSLjIQkXE" data-video-title="3d slicer to link camera" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=ZPuSLjIQkXE" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/ZPuSLjIQkXE/maxresdefault.jpg" title="3d slicer to link camera" width="" height="">
  </a>
</div>


---

## Post #2 by @lassoan (2023-08-11 22:12 UTC)

<p>Yes, there are many ways to do this. There are modules for moving the camera around, such as Viewpoint module in SlicerIGT extension, but it is probably simpler to just add an observer to the plane node and and whenever it is modified then update the camera node accordingly.</p>

---

## Post #3 by @B4D (2023-08-12 11:46 UTC)

<p>Is this something you could help us with or perhaps you know someone.?<br>
Regards Michael.</p>

---
