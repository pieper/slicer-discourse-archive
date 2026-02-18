# Shows 2D Slices on one 3D view when using dual 3D view

**Topic ID**: 21895
**Date**: 2022-02-10
**URL**: https://discourse.slicer.org/t/shows-2d-slices-on-one-3d-view-when-using-dual-3d-view/21895

---

## Post #1 by @park (2022-02-10 16:19 UTC)

<p>Hi all</p>
<p>Like figure, I would like to pop up 2D slices view on only one 3D view when using the multi 3D view</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7662e0774a0a59ba18021d13493e4ceb0aec5e9.png" data-download-href="/uploads/short-url/uJvzFGF3cEe3GsQpEyMjaQ1G1M5.png?dl=1" title="sdsd" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7662e0774a0a59ba18021d13493e4ceb0aec5e9_2_556x500.png" alt="sdsd" data-base62-sha1="uJvzFGF3cEe3GsQpEyMjaQ1G1M5" width="556" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7662e0774a0a59ba18021d13493e4ceb0aec5e9_2_556x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7662e0774a0a59ba18021d13493e4ceb0aec5e9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7662e0774a0a59ba18021d13493e4ceb0aec5e9.png 2x" data-dominant-color="5A5668"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sdsd</span><span class="informations">823×739 15.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What is the easiest way to implement this ?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2022-02-10 16:23 UTC)

<p>Follow up to this discussion:</p>
<aside class="quote quote-modified" data-post="1" data-topic="3074">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/f1d935/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/show-hide-slice-views-in-3d-view-using-python/3074/">Show/hide slice views in 3D view using Python</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi developers, 
I have a problem switching on the slice views on or off in the 3D view from Python permanently. The code I am using for i.e. switch on the red slice view is: 
current_slice_node = slicer.mrmlScene.GetNodeByID(‘vtkMRMLModelDisplayNode1’) 
current_slice_node.VisibilityOn() 
This code works well until one changes the position of the slice by i.e. scrolling in the slice view. I guess since the “eye” in the slice view is still “closed” the update will set the visibility again to 0 and…
  </blockquote>
</aside>


---
