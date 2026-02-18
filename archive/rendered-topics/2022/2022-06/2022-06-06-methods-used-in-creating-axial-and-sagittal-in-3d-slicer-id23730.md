# Methods used in creating axial and sagittal in 3d Slicer

**Topic ID**: 23730
**Date**: 2022-06-06
**URL**: https://discourse.slicer.org/t/methods-used-in-creating-axial-and-sagittal-in-3d-slicer/23730

---

## Post #1 by @Gabriela_Zurliana (2022-06-06 12:30 UTC)

<p>Hello! pardon for any mistakes I made here, this is my first time posting a question in this forum.</p>
<p>I am currently trying to create a segmentation of the spine from a self-gathered data using ultrasound and is trying to create my own program and algorithm to do so, but i am stuck on creating the sagital and coronal view. Though i noticed in 3d slicer, it is automatically possible to create the views from the png images of ultrasound as seen here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2be498786ffdcbb52cdea7455fb8c16479ea2236.png" data-download-href="/uploads/short-url/6giii2S4Bbm5Or970YDuSaCOi3A.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2be498786ffdcbb52cdea7455fb8c16479ea2236_2_690x388.png" alt="image" data-base62-sha1="6giii2S4Bbm5Or970YDuSaCOi3A" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2be498786ffdcbb52cdea7455fb8c16479ea2236_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2be498786ffdcbb52cdea7455fb8c16479ea2236_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2be498786ffdcbb52cdea7455fb8c16479ea2236_2_1380x776.png 2x" data-dominant-color="616278"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 376 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>i was wondering, if possible, what is the method used by 3d slicer to achieve this? i am using python for my coding algorithm.<br>
Thank you in advance!</p>

---

## Post #2 by @pieper (2022-06-06 16:32 UTC)

<p>Slicer uses <a href="https://vtk.org/doc/nightly/html/classvtkImageReslice.html"><code>vtkImageReslice</code></a> for this.  It’s available in python.</p>

---

## Post #3 by @mau_igna_06 (2022-06-06 20:29 UTC)

<p>Why don’t you check out this link:</p><div class="youtube-onebox lazy-video-container" data-video-id="2vXeJxYFou4" data-video-title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=2vXeJxYFou4" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/2vXeJxYFou4/maxresdefault.jpg" title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" width="" height="">
  </a>
</div>


---
