# ThreeD view interactive mode

**Topic ID**: 8320
**Date**: 2019-09-06
**URL**: https://discourse.slicer.org/t/threed-view-interactive-mode/8320

---

## Post #1 by @JaceYang (2019-09-06 09:27 UTC)

<p>Coule we modify the code about the threeD view interaction to let we interact with threeD view like autodesk maya?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca740f4ddef1370e5309083d1d76e39c2e054a7d.png" data-download-href="/uploads/short-url/sSZ6zkQGaiVVimT6zxKkQSaKffL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca740f4ddef1370e5309083d1d76e39c2e054a7d.png" alt="image" data-base62-sha1="sSZ6zkQGaiVVimT6zxKkQSaKffL" width="690" height="313" data-dominant-color="5C5C5C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1103×501 27.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
For example,select a node in the data module then transform it in the 3D view.But currently the mouse events in the 3D view are all about camara.Why not use vtktransform to modify the node itself instead of the camera?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da0ae8dfd7d861869a5a0b6aa0c890b36d2482a5.jpeg" data-download-href="/uploads/short-url/v6TsFuUGLYcCSGiFQukG0cYgKd7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da0ae8dfd7d861869a5a0b6aa0c890b36d2482a5_2_690x330.jpeg" alt="image" data-base62-sha1="v6TsFuUGLYcCSGiFQukG0cYgKd7" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da0ae8dfd7d861869a5a0b6aa0c890b36d2482a5_2_690x330.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da0ae8dfd7d861869a5a0b6aa0c890b36d2482a5_2_1035x495.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da0ae8dfd7d861869a5a0b6aa0c890b36d2482a5_2_1380x660.jpeg 2x" data-dominant-color="BABEBD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1557×746 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @rprueckl (2019-09-06 10:44 UTC)

<p>This can be done via the ‘Transforms’ module.<br>
Create a new linear transform, apply it to your model, and enable interaction/display in the 3d viewer as shown in the screenshot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/436ff990a993a82556f5af9e67f4b3d9d0eafb0f.png" data-download-href="/uploads/short-url/9CzTwwMexTEOBgqHMJdIU0qQcwv.png?dl=1" title="trans" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/436ff990a993a82556f5af9e67f4b3d9d0eafb0f_2_490x500.png" alt="trans" data-base62-sha1="9CzTwwMexTEOBgqHMJdIU0qQcwv" width="490" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/436ff990a993a82556f5af9e67f4b3d9d0eafb0f_2_490x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/436ff990a993a82556f5af9e67f4b3d9d0eafb0f_2_735x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/436ff990a993a82556f5af9e67f4b3d9d0eafb0f.png 2x" data-dominant-color="535455"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">trans</span><span class="informations">936×954 43 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2019-09-06 14:59 UTC)

<aside class="quote no-group" data-username="JaceYang" data-post="1" data-topic="8320">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jaceyang/48/3686_2.png" class="avatar"> JaceYang:</div>
<blockquote>
<p>Why not use vtktransform to modify the node itself instead of the camera?</p>
</blockquote>
</aside>
<p>In a 3D modeling tool, such as Maya, you often translate/rotate objects using your mouse. In medical image computing you rarely do such free-hand transformations but you typically align objects automatically, based on landmarks, surfaces, or image intensities. Nevertheless, the option is available in Slicer as <a class="mention" href="/u/rprueckl">@rprueckl</a> described above.</p>

---
