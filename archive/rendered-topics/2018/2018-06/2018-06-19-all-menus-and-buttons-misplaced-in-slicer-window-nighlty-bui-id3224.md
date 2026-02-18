# All menus and buttons misplaced in Slicer window (nighlty build version)

**Topic ID**: 3224
**Date**: 2018-06-19
**URL**: https://discourse.slicer.org/t/all-menus-and-buttons-misplaced-in-slicer-window-nighlty-build-version/3224

---

## Post #1 by @mag (2018-06-19 12:33 UTC)

<p>Hello,</p>
<p>I am having issues on Windows 10 with the latest nighlty build Slicer. The window of Slicer does not display correctly (see screenshot). The menu bar is missing and the tool bar is displaying in its place. Other menu/buttons below are also misplaced.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04585c2d1b82c9394f484bc40090b3d75ed4d583.png" data-download-href="/uploads/short-url/CrdFo2XlGWhCbNKSns8Z6zsCl5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/04585c2d1b82c9394f484bc40090b3d75ed4d583_2_690x388.png" alt="image" data-base62-sha1="CrdFo2XlGWhCbNKSns8Z6zsCl5" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/04585c2d1b82c9394f484bc40090b3d75ed4d583_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/04585c2d1b82c9394f484bc40090b3d75ed4d583_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/04585c2d1b82c9394f484bc40090b3d75ed4d583_2_1380x776.png 2x" data-dominant-color="6A6A71"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 264 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Note that if I click on the tools nothing happens but if I click on the void space just below one of them, then the tool is selected (e.g. here with module selector), so it seems to be just a visualization problem.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a85a71b9b2531f8a98c39c5c968b3401ace95574.png" data-download-href="/uploads/short-url/o1jZr7h7suNY1PmLKnSd6oDXdzK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a85a71b9b2531f8a98c39c5c968b3401ace95574_2_690x388.png" alt="image" data-base62-sha1="o1jZr7h7suNY1PmLKnSd6oDXdzK" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a85a71b9b2531f8a98c39c5c968b3401ace95574_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a85a71b9b2531f8a98c39c5c968b3401ace95574_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a85a71b9b2531f8a98c39c5c968b3401ace95574_2_1380x776.png 2x" data-dominant-color="696970"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Until last Friday I was working with the stable release which I installed last November and it has no display issues. Not sure if this is my laptop being weird or a Slicer problem. Any help will be very much appreciated.</p>
<p>Thanks,</p>
<p>Marta</p>

---

## Post #2 by @lassoan (2018-06-19 12:58 UTC)

<p>There is an Intel display driver bug that causes this problem for all Qt5-based applications. Need to update the display driver to latest version or change NVidia settings to use the discrete GPU for Slicer (which may be a good idea anyway).</p>
<p>See details in this post:</p>
<aside class="quote" data-post="2" data-topic="2613">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/missing-menu-items-from-slicer-application-main-window/2613/2">Missing menu items from Slicer Application Main Window</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    This is a known issue with all Qt5 applications on some laptops that have both Intel and NVidia graphics card. One solution is to set your NVidia application settings to use NVidia for 3D Slicer (SlicerApp-real.exe). 
<a href="https://communities.intel.com/thread/116003">Intel has acknowledged that this is an issue in their graphics card driver</a> that was introduced in x.x.x.4627 and they fixed the problem in driver version: x.x.x.4729.
  </blockquote>
</aside>


---

## Post #3 by @mag (2018-06-19 14:22 UTC)

<blockquote>
<p>Need to update the display driver to latest version</p>
</blockquote>
<p>That worked, thank you!</p>
<blockquote>
<p>or change NVidia settings to use the discrete GPU for Slicer (which may be a good idea anyway).</p>
</blockquote>
<p>I am afraid I am quite ignorant about GPUs. I just left all settings on “Let the 3D application decide” and never worried to much about what Slicer was using since it didn’t give me problems. What is it exactly that I should select on the NVIDIA control panel to make sure SlicerApp-real is using the discrete GPU?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b639872f876562cdbd67a46e1aa5f46f2d9ed0f.png" data-download-href="/uploads/short-url/d2sPAXj7RScQ61z9SPqtsRH1PvV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b639872f876562cdbd67a46e1aa5f46f2d9ed0f_2_690x388.png" alt="image" data-base62-sha1="d2sPAXj7RScQ61z9SPqtsRH1PvV" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b639872f876562cdbd67a46e1aa5f46f2d9ed0f_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b639872f876562cdbd67a46e1aa5f46f2d9ed0f_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b639872f876562cdbd67a46e1aa5f46f2d9ed0f_2_1380x776.png 2x" data-dominant-color="C9CFD5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 488 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2018-06-19 14:38 UTC)

<aside class="quote no-group" data-username="mag" data-post="3" data-topic="3224">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/58f4c7/48.png" class="avatar"> mag:</div>
<blockquote>
<p>I just left all settings on “Let the 3D application decide”</p>
</blockquote>
</aside>
<p>Applications cannot select if they want to run on the on-board / discrete GPU. If you want an application to use the discrete GPU then you must set it in the NVidia control panel explicitly. You’ll see a huge speed improvement in volume rendering and visible performance improvement in display of very large models.</p>

---

## Post #5 by @jcfr (2018-08-03 20:48 UTC)

<p>This is now tracked in issue <a href="https://issues.slicer.org/view.php?id=4594">https://issues.slicer.org/view.php?id=4594</a></p>

---
