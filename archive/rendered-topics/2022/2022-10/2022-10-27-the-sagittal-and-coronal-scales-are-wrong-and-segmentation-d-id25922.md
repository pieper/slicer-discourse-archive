---
topic_id: 25922
title: "The Sagittal And Coronal Scales Are Wrong And Segmentation D"
date: 2022-10-27
url: https://discourse.slicer.org/t/25922
---

# The sagittal and coronal scales are wrong and segmentation does not work

**Topic ID**: 25922
**Date**: 2022-10-27
**URL**: https://discourse.slicer.org/t/the-sagittal-and-coronal-scales-are-wrong-and-segmentation-does-not-work/25922

---

## Post #1 by @Eiichi (2022-10-27 02:38 UTC)

<p>Hi, I’m Eiichi, a Japanese plastic surgeon and researcher.<br>
I am studying the evaluation of the healing process of cranial bone defects in rats.<br>
For this purpose, the cranial crowns of rats are collected and imaged with μCT.</p>
<p>I am trying to perform 3D segmentation using a slicer, but the scale of sagittal/coronal is not correct and it does not work well.</p>
<p>Is this a problem that can be solved by manipulating the slicer? Or should I use software other than slicer?</p>
<p>Apologies that this is an out of place question.<br>
Thanks.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7217cfe93781a4d8b32649e66c21061d1e586ff.jpeg" data-download-href="/uploads/short-url/wYG2ITRkCltsIcUcftEtN7IYaBx.jpeg?dl=1" title="スクリーンショット 2022-10-27 080924" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7217cfe93781a4d8b32649e66c21061d1e586ff_2_690x453.jpeg" alt="スクリーンショット 2022-10-27 080924" data-base62-sha1="wYG2ITRkCltsIcUcftEtN7IYaBx" width="690" height="453" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7217cfe93781a4d8b32649e66c21061d1e586ff_2_690x453.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7217cfe93781a4d8b32649e66c21061d1e586ff_2_1035x679.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7217cfe93781a4d8b32649e66c21061d1e586ff.jpeg 2x" data-dominant-color="5B5C74"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2022-10-27 080924</span><span class="informations">1353×889 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-10-27 02:50 UTC)

<p>What you experienced is quite common with μCT images, as these scanners often create invalid DICOM files or export data in non-standard formats.</p>
<p>If you provide us more information about your scanner, the used file format, and preferably also provide a sample data set (upload to dropbox/onedrive/google drive and post the link here) then we may give some tips about how to fix your data.</p>

---

## Post #3 by @Eiichi (2022-10-27 03:25 UTC)

<p>Thanks a lot.<br>
My scanner is named <code>inspeXio</code> ,file format is CB,I just started using it, so there are many things I don’t understand, sorry about it.</p>
<p>And I will upload my storage data for your inspection.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/scl/fo/8tgom8qh7b43z4hmhsvdw/h?dl=0&amp;rlkey=vximiqcifuo1rm2ve9e2tcovw">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/scl/fo/8tgom8qh7b43z4hmhsvdw/h?dl=0&amp;rlkey=vximiqcifuo1rm2ve9e2tcovw" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/scl/fo/8tgom8qh7b43z4hmhsvdw/h?dl=0&amp;rlkey=vximiqcifuo1rm2ve9e2tcovw" target="_blank" rel="noopener nofollow ugc">3Dslicer</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2022-10-27 05:08 UTC)

<p>It seems that ITK (the library that Slicer uses for reading/writing images) recognizes this file format but it cannot determine the distance between slices. However, often micro-CT scans are acquired with isotropic spacing, and it seems to be the case here, too. So, you can fix the loaded image by manually setting in Volumes module the slice spacing (spacing along the third image axis) from 1.0 to the same value as the spacing along the first two image axes:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbeee19fab663a78d0a15cb8398a635ec3156609.jpeg" data-download-href="/uploads/short-url/qOx5rQFYvGZ3amAE5pd4AttiIMp.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbeee19fab663a78d0a15cb8398a635ec3156609_2_690x419.jpeg" alt="image" data-base62-sha1="qOx5rQFYvGZ3amAE5pd4AttiIMp" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbeee19fab663a78d0a15cb8398a635ec3156609_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbeee19fab663a78d0a15cb8398a635ec3156609_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbeee19fab663a78d0a15cb8398a635ec3156609_2_1380x838.jpeg 2x" data-dominant-color="39383A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1166 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="Eiichi" data-post="3" data-topic="25922">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eiichi/48/16583_2.png" class="avatar"> Eiichi:</div>
<blockquote>
<p><code>inspeXio</code> ,file format is CB</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> does this file format look familiar to you?</p>

---

## Post #5 by @Eiichi (2022-10-27 06:32 UTC)

<p>thanks a lot!<br>
I got it.</p>

---

## Post #6 by @muratmaga (2022-10-28 15:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="25922">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> does this file format look familiar to you?</p>
</blockquote>
</aside>
<p>No, never heard of it.</p>

---
