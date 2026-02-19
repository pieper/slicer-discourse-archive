---
topic_id: 10234
title: "Centerline Options And Best Way To Measure Arterial Vessels"
date: 2020-02-13
url: https://discourse.slicer.org/t/10234
---

# Centerline options and best way to measure arterial vessels?

**Topic ID**: 10234
**Date**: 2020-02-13
**URL**: https://discourse.slicer.org/t/centerline-options-and-best-way-to-measure-arterial-vessels/10234

---

## Post #1 by @Romeo_Guevara (2020-02-13 03:09 UTC)

<p>Good evening, how can I make the axial cut, when shown in the “3D only” follow the center line I made? that in order to measure the diameter of the vessels as well as possible.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/1149914c2403cc7c18665a8d0747e05cb484225f.jpeg" alt="slicer centerline" data-base62-sha1="2sVJyvUhOhAksY7Kl6fL6hPBb5l" width="661" height="357"></p>

---

## Post #2 by @lassoan (2020-02-13 16:20 UTC)

<p>We have developed a module that does this in SlicerHeart project, but we’ll make it public only when the associated paper is published. Until then, there are two modules that you can use to achieve this:</p>
<ol>
<li>Create curved planar reformat volume and measure on that volume</li>
</ol>
<aside class="quote quote-modified" data-post="7" data-topic="9456">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-implement-cpr-curved-plannar-reconstruction-from-centerline/9456/7">How to implement CPR (curved planar reconstruction) from centerline?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi Andras, 
Sometimes people end up having to scan coiled snakes, or fish that are in little jars. Depending on what they need to do with it, they may have to ‘straighten’ the specimen. Is there a way this CPR can be generalized for such use cases? 
[image] 
[image]
  </blockquote>
</aside>

<ol start="2">
<li>Reslice the original volume along a curve using Endoscopy module</li>
</ol>
<div class="youtube-onebox lazy-video-container" data-video-id="thExIlffL0I" data-video-title="Curved multi-planar reconstruction (MPR) view in 3D Slicer" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=thExIlffL0I" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/thExIlffL0I/maxresdefault.jpg" title="Curved multi-planar reconstruction (MPR) view in 3D Slicer" width="" height="">
  </a>
</div>


---

## Post #3 by @Romeo_Guevara (2020-02-14 14:01 UTC)

<p>Good morning, I managed to make the centerline with the module “volume reslice driver” with the previous version, however in this new version “2020-02-11” the module “Endoscopy” does not recognize the pattern when using the "open curve markup "which is indispensable to see if the centerline is correct. Thanks for your help.</p>

---

## Post #4 by @lassoan (2020-02-16 15:00 UTC)

<p>I’ve updated the Endoscopy module to also take markups curve as input (in Slicer Preview Release, available from tomorrow) to take. Endoscopy still creates an approximating curve, which slightly differs from the interpolating curve of markups curve, but as long as the points are equally spaced and curvatures are not too extreme then they should be close enough.</p>
<p>We’ll release a curve explorer module later that can use markups curves without approximation. Maybe we’ll merge it with the curve planar reformatting module.</p>

---

## Post #5 by @Romeo_Guevara (2020-02-17 14:09 UTC)

<p>Good morning, Andrass, when I try to download the version 2020-02-17, I download the 2020-02-12, how can I download the newest version? Cheers</p>

---

## Post #6 by @manjula (2020-02-17 14:42 UTC)

<p>I had the same problem today !</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="10308" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"><a href="https://discourse.slicer.org/t/linux-preview-release-download-points-to-old-built-fyi/10308/2">Linux Preview Release Download Points to old built - FYI</a></div>
<blockquote>
<p>The date in the file name is not actually the date it was built, but corresponds to the date when the most recent commit was merged. Therefore there hasn’t been any updates merged to Slicer since 2020-02-12.</p>
</blockquote>
</aside>

---

## Post #7 by @lassoan (2020-02-17 15:32 UTC)

<p>Date in the Slicer package reflects the date when Slicer core is last changed. If there are no changes in the core then the package date will remain the same.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7392f340511afc3eb1b7c776a0975d08b5326ea.png" data-download-href="/uploads/short-url/q8RTqPFFzz4rWtI3QRTyPXdI4Fs.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7392f340511afc3eb1b7c776a0975d08b5326ea_2_690x381.png" alt="image" data-base62-sha1="q8RTqPFFzz4rWtI3QRTyPXdI4Fs" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7392f340511afc3eb1b7c776a0975d08b5326ea_2_690x381.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7392f340511afc3eb1b7c776a0975d08b5326ea_2_1035x571.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7392f340511afc3eb1b7c776a0975d08b5326ea_2_1380x762.png 2x" data-dominant-color="E1E2E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1680×928 96.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Changed extensions are still updated (you need to update or uninstall/reinstall in Extension Manager to get latest version if there was any change).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/979b02130b08aa4fd040b36d2e64717bd7f2df71.png" data-download-href="/uploads/short-url/lDacu3oshlhVHCT5NG0oVvc7elX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/979b02130b08aa4fd040b36d2e64717bd7f2df71_2_690x226.png" alt="image" data-base62-sha1="lDacu3oshlhVHCT5NG0oVvc7elX" width="690" height="226" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/979b02130b08aa4fd040b36d2e64717bd7f2df71_2_690x226.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/979b02130b08aa4fd040b36d2e64717bd7f2df71_2_1035x339.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/979b02130b08aa4fd040b36d2e64717bd7f2df71.png 2x" data-dominant-color="E7E9F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1347×442 52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Romeo_Guevara (2020-02-19 13:30 UTC)

<p>Good night Andras, the “open curve markup” is not yet recognized by the “endoscopy” module in version 2020-02-17. Thank you for your help, where would I send you a personal email? regards.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30fcdd80e5db99c4db531a15b62c9a6d10aaf402.png" data-download-href="/uploads/short-url/6ZmG9rIHioFgu5BOpgA67yOcf6i.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30fcdd80e5db99c4db531a15b62c9a6d10aaf402_2_690x388.png" alt="image" data-base62-sha1="6ZmG9rIHioFgu5BOpgA67yOcf6i" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30fcdd80e5db99c4db531a15b62c9a6d10aaf402_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30fcdd80e5db99c4db531a15b62c9a6d10aaf402_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30fcdd80e5db99c4db531a15b62c9a6d10aaf402_2_1380x776.png 2x" data-dominant-color="7B7B81"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @lassoan (2020-02-19 16:49 UTC)

<p>I’ve merged this today (in rev28775). It should be avaiable in tomorrow’s Slicer Preview Release (or you can replace Endoscopy.py file in your Slicer installation by <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/Endoscopy/Endoscopy.py">this latest version</a>).</p>

---
