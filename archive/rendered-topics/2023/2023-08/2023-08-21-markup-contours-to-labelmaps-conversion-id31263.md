# Markup contours to labelmaps conversion

**Topic ID**: 31263
**Date**: 2023-08-21
**URL**: https://discourse.slicer.org/t/markup-contours-to-labelmaps-conversion/31263

---

## Post #1 by @alireza (2023-08-21 14:44 UTC)

<p>I have questions regarding interprotability between contours and labelmaps. I’m aware of DICOM RT module and polySEG and how we can convert RTSTRUCT to labelmap to edit etc.</p>
<p>My questions are</p>
<ol>
<li>Without having an RT, is it possible to convert drawn contours in makrups module to labelmaps?</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b5fb15f555cf6b6976e8ba65f0239c744efb12d.jpeg" alt="CleanShot 2023-08-21 at 10.41.05" data-base62-sha1="d2ktbPydAuZ85j5UIBbNUOae36Z" width="530" height="417"></p>
<ol start="2">
<li>I used the markups module to draw closed curve and wanted to fill color inside of it, but doesn’t seem to have any effect. is it possible?</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f63636a6b251b8f8776e9e283fa21dd722cce84d.jpeg" data-download-href="/uploads/short-url/z85BNdvvgrajR1BhZ08tIkGGzTv.jpeg?dl=1" title="CleanShot 2023-08-21 at 10.04.41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f63636a6b251b8f8776e9e283fa21dd722cce84d_2_690x398.jpeg" alt="CleanShot 2023-08-21 at 10.04.41" data-base62-sha1="z85BNdvvgrajR1BhZ08tIkGGzTv" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f63636a6b251b8f8776e9e283fa21dd722cce84d_2_690x398.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f63636a6b251b8f8776e9e283fa21dd722cce84d_2_1035x597.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f63636a6b251b8f8776e9e283fa21dd722cce84d_2_1380x796.jpeg 2x" data-dominant-color="8B8A91"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CleanShot 2023-08-21 at 10.04.41</span><span class="informations">1901×1099 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="3">
<li>Any spline curve drawing tool in segmentEditor that can be used to draw/paint? I found the tube tool, but seems like it only paint on the outline</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a82561db3fc02ddb1b3bf5be2555abc8579dde22.jpeg" data-download-href="/uploads/short-url/nZuiYNPbDAQAlnRshXbHkAE6zya.jpeg?dl=1" title="CleanShot 2023-08-21 at 10.36.22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a82561db3fc02ddb1b3bf5be2555abc8579dde22_2_690x386.jpeg" alt="CleanShot 2023-08-21 at 10.36.22" data-base62-sha1="nZuiYNPbDAQAlnRshXbHkAE6zya" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a82561db3fc02ddb1b3bf5be2555abc8579dde22_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a82561db3fc02ddb1b3bf5be2555abc8579dde22_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a82561db3fc02ddb1b3bf5be2555abc8579dde22.jpeg 2x" data-dominant-color="ADAEAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CleanShot 2023-08-21 at 10.36.22</span><span class="informations">1294×725 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks in advance for your time and help</p>

---

## Post #2 by @pieper (2023-08-21 15:01 UTC)

<p>This would be a nice feature, but I don’t think it’s implemented now.</p>
<p>For similar problems I’ve used the Markups to Model extension.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerIGT/SlicerMarkupsToModel">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerIGT/SlicerMarkupsToModel" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/50e9d5acd90a8f1e627e7a2c6c540bcb9dbf4bcc3baf77cb3451d7aa3b79d134/SlicerIGT/SlicerMarkupsToModel" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerIGT/SlicerMarkupsToModel" target="_blank" rel="noopener">GitHub - SlicerIGT/SlicerMarkupsToModel: 3D Slicer extension to create tube...</a></h3>

  <p>3D Slicer extension to create tube or closed surface model from markup fiducials - GitHub - SlicerIGT/SlicerMarkupsToModel: 3D Slicer extension to create tube or closed surface model from markup fi...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @alireza (2023-08-21 15:05 UTC)

<p>Thanks Steve,<br>
Do you know if the fill inside the contour in markups (question <span class="hashtag-raw">#2</span>) is a bug or limitation?</p>

---

## Post #4 by @pieper (2023-08-21 17:25 UTC)

<p>The ability to fill the curve would be a nice feature.  I’m not sure what behavior to expect when the points are not co-planar.   Maybe a soap-bubble interpolated surface or filling the projection of the control points to the current plane would be good.  Or just a constraint that points can’t be moved out of the plane when the filling mode is enabled.</p>

---
