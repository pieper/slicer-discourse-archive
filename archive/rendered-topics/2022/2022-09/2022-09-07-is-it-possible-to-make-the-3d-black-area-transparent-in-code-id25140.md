# Is it possible to make the 3d black area transparent in code?

**Topic ID**: 25140
**Date**: 2022-09-07
**URL**: https://discourse.slicer.org/t/is-it-possible-to-make-the-3d-black-area-transparent-in-code/25140

---

## Post #1 by @jay1987 (2022-09-07 12:14 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9582a8e3936cee0e4accb22da653d7b7b5af818.jpeg" alt="image" data-base62-sha1="sJaRK8QQ9pJINZ6rLW7Uni3slJe" width="451" height="414"></p>

---

## Post #3 by @pieper (2022-09-07 20:14 UTC)

<p>You can set the transparency threshold for the slice rendering in the Volumes module.  If that’s what you are looking for you can access the corresponding functionality with <code>vtkMRMLScalarVolumeDisplayNode::SetThreshold</code>.</p>

---

## Post #4 by @jay1987 (2022-09-08 01:39 UTC)

<p>thanks pieper .<br>
i find the code to render slice in 3d view , it looks like to convert slice volume into a texture then combine the texture into a vtkPlaneSource,render the 3d plane source use ModelDisplayNode<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6bd55473b34ce9141b8e2b103faa361a28ba1f5.png" data-download-href="/uploads/short-url/wVdsFZMzGOxByVBuQppg5TrigSx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6bd55473b34ce9141b8e2b103faa361a28ba1f5_2_690x143.png" alt="image" data-base62-sha1="wVdsFZMzGOxByVBuQppg5TrigSx" width="690" height="143" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6bd55473b34ce9141b8e2b103faa361a28ba1f5_2_690x143.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6bd55473b34ce9141b8e2b103faa361a28ba1f5_2_1035x214.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6bd55473b34ce9141b8e2b103faa361a28ba1f5.png 2x" data-dominant-color="EAEAE8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1272×265 75.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
i try to add the follow code to make the 3d rendering black area transparent,but it make no sense<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f24906da6b27d71d0311fc32494ff21d04c7adf5.png" data-download-href="/uploads/short-url/yzm0qQ7dKG7KjK3RoM9LIcJgaHj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f24906da6b27d71d0311fc32494ff21d04c7adf5_2_690x67.png" alt="image" data-base62-sha1="yzm0qQ7dKG7KjK3RoM9LIcJgaHj" width="690" height="67" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f24906da6b27d71d0311fc32494ff21d04c7adf5_2_690x67.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f24906da6b27d71d0311fc32494ff21d04c7adf5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f24906da6b27d71d0311fc32494ff21d04c7adf5.png 2x" data-dominant-color="D8D9D4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">762×74 18.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
