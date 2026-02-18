# Clarification re RTSTRUCT display

**Topic ID**: 15973
**Date**: 2021-02-12
**URL**: https://discourse.slicer.org/t/clarification-re-rtstruct-display/15973

---

## Post #1 by @fedorov (2021-02-12 22:11 UTC)

<p>When I load RTSTRUCT, I see the following:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e38e0d52bf31e6830b44c6e8e7e31fbe8631f11.jpeg" data-download-href="/uploads/short-url/i0C1nZEkIx7slT4AgE9gKa8g9jj.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e38e0d52bf31e6830b44c6e8e7e31fbe8631f11_2_517x310.jpeg" alt="image" data-base62-sha1="i0C1nZEkIx7slT4AgE9gKa8g9jj" width="517" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e38e0d52bf31e6830b44c6e8e7e31fbe8631f11_2_517x310.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e38e0d52bf31e6830b44c6e8e7e31fbe8631f11_2_775x465.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e38e0d52bf31e6830b44c6e8e7e31fbe8631f11_2_1034x620.jpeg 2x" data-dominant-color="A5939B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1273×765 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would like to clarify:</p>
<ul>
<li>do I see the original RTSTRUCT-defined contours in the slice viewers, or those are interpolated contours?</li>
<li>is it possible to show the original RTSTRUCT-defined contours in 3d view?</li>
</ul>
<p>When I try to create the Ribbon model, I get this error:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89cdc0d8943d00a25929cff72b372a3d625d6cd9.png" alt="image" data-base62-sha1="jF4eKnZYki7BLuYzCwSqBI2yU8V" width="489" height="249"></p>
<p>I am using the latest stable release on mac.</p>

---

## Post #2 by @lassoan (2021-02-12 23:31 UTC)

<p>SlicerRT importer imports the original contours without any changes and stores it in planar contours representation. If you create closed surface representation then the original contours are still exactly preserved at slice positions but a surface is created between them by triangulation. Conversion from planar contours to ribbon representation was broken in Slicer-4.11-20200930 version but it is fixed in recent Slicer Preview Releases.</p>

---

## Post #3 by @fedorov (2021-02-15 17:46 UTC)

<p>Andras, I did not do anything myself to create a closed surface representation - it is created automatically when I load RTSTRUCT (this behavior is identical both in stable and latest releases). Because the surface representation is created and shown by default, I was not sure what is being shown in the 2d viewers, and the discretization of the 3d surface was very coarse, which made me suspicious. Thanks for the clarification.</p>

---

## Post #4 by @lassoan (2021-02-15 18:32 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="3" data-topic="15973">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Because the surface representation is created and shown by default, I was not sure what is being shown in the 2d viewers</p>
</blockquote>
</aside>
<p>You can choose which representation is shown in 2D/3D views in Segmentations module / Display / Advanced section.</p>

---

## Post #5 by @fedorov (2021-02-15 18:46 UTC)

<p>Thank you, this is very helpful! Although, if I toggle “Planar contour” for 2d view, I see points in the reformats, but not in the contour plane.</p>
<p><a href="https://www.screencast.com/t/gdPUxAeY048m" class="onebox" target="_blank" rel="noopener">https://www.screencast.com/t/gdPUxAeY048m</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33d9b9163ca591438db48c7f8fc887a2636028f9.png" data-download-href="/uploads/short-url/7oGORsEn9GvDhPitbUcxsrIkjXz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33d9b9163ca591438db48c7f8fc887a2636028f9.png" alt="image" data-base62-sha1="7oGORsEn9GvDhPitbUcxsrIkjXz" width="584" height="500" data-dominant-color="756C76"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">660×565 64.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2021-02-15 19:02 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="5" data-topic="15973">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>if I toggle “Planar contour” for 2d view, I see points in the reformats, but not in the contour plane</p>
</blockquote>
</aside>
<p>This is expected - you only see the contour in-plane if it is exactly in the slice view’s plane. This is exact match may be hard to achieve, that is why we added the ribbon representation, which is much better visible in slice views.</p>
<p>Planar contours:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/158f41841218fb97f08bbc58851fa45022aa3ab9.png" data-download-href="/uploads/short-url/34IWYHDmVqxYCRI8NiJQLKLabNf.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/158f41841218fb97f08bbc58851fa45022aa3ab9_2_690x419.png" alt="image" data-base62-sha1="34IWYHDmVqxYCRI8NiJQLKLabNf" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/158f41841218fb97f08bbc58851fa45022aa3ab9_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/158f41841218fb97f08bbc58851fa45022aa3ab9_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/158f41841218fb97f08bbc58851fa45022aa3ab9_2_1380x838.png 2x" data-dominant-color="464745"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1371 582 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Ribbon model:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e7234e0673eee583dc1a7c35a2e8b9eb73d32e5.jpeg" data-download-href="/uploads/short-url/mBG7RafDseCxKrCEKsX775GSpNj.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e7234e0673eee583dc1a7c35a2e8b9eb73d32e5_2_690x421.jpeg" alt="image" data-base62-sha1="mBG7RafDseCxKrCEKsX775GSpNj" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e7234e0673eee583dc1a7c35a2e8b9eb73d32e5_2_690x421.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e7234e0673eee583dc1a7c35a2e8b9eb73d32e5_2_1035x631.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e7234e0673eee583dc1a7c35a2e8b9eb73d32e5_2_1380x842.jpeg 2x" data-dominant-color="485A44"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2249×1373 651 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>These features are somewhat hidden, but both planar contours and ribbon model are useful mainly for diagnostic purposes (when closed surface representation does not look good then you can check the original data).</p>

---

## Post #7 by @alireza (2023-04-05 02:49 UTC)

<p>Seems like I can’t render RTSTRUCT in the 2D views as planar contour either (see video below).<br>
As Andras mentioned above it is due to the exact plane situation but shouldn’t it change the plane when holding shift and dragging on the other views? and basically just hit it? I tried zoom A LOT in the other views so that I can control the shift right click drag but still can’t, I’m wondering how much precision is needed?</p>
<p>I tried using various RTSTRUCT, I tried with the RT samples here too (<a href="https://github.com/SlicerRt/SlicerRtData/tree/master/HIT-H1-head" class="inline-onebox" rel="noopener nofollow ugc">SlicerRtData/HIT-H1-head at master · SlicerRt/SlicerRtData · GitHub</a>)</p>
<p>As you see below I have zoomed A LOT and the shift mouse drag is changing in the 1/100 of the z<br>
I understand the Ribbon is the solution, but I’m more interested in the rendering of contours for now.</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/446da2e123f05d1a260ab938d35c4cc4a55e34d9.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/446da2e123f05d1a260ab938d35c4cc4a55e34d9.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/446da2e123f05d1a260ab938d35c4cc4a55e34d9.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #8 by @lassoan (2023-04-05 04:08 UTC)

<aside class="quote no-group" data-username="alireza" data-post="7" data-topic="15973">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alireza/48/67173_2.png" class="avatar"> alireza:</div>
<blockquote>
<p>I’m wondering how much precision is needed?</p>
</blockquote>
</aside>
<p>You need the exact position match of the slice plane position (with a tolerance of something like 1e-8mm), which is practically impossible to achieve it by manual positioning. Therefore, you will not see the intersection in the contour plane, only the dots in orthogonal views.</p>
<p>The ribbon representation has an intersection with the slice plane, that’s why we added it. If you want to see the contour representation in slice views then you can export the contours to a model and apply a tube filter with a small radius.</p>
<p>Note that we consider the contour and ribbon representations to be only useful for debugging of the smooth surface generation algorithm. It allows us to see if the input contours that we get are messed up in some way (some contours are missing, duplicated, don’t match the image, etc.).</p>

---
