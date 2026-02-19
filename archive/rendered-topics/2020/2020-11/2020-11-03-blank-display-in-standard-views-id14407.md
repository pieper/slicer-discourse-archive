---
topic_id: 14407
title: "Blank Display In Standard Views"
date: 2020-11-03
url: https://discourse.slicer.org/t/14407
---

# Blank display in standard views

**Topic ID**: 14407
**Date**: 2020-11-03
**URL**: https://discourse.slicer.org/t/blank-display-in-standard-views/14407

---

## Post #1 by @Kalman (2020-11-03 16:51 UTC)

<p>Hi All,</p>
<p>I have a question regarding the display:<br>
My computer does not show the orthogonal views with the latest nightly build versions (in the past week). I’ve tried with the sample datasets too, but I can only visualize the volume in the 3D viewer, but not in the normal views. I attach an image about it:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b34234862fb2e38df45bcb77819b989dffbe834d.jpeg" data-download-href="/uploads/short-url/pzNji0YuAyF3dNf6Pcd8Bdshehv.jpeg?dl=1" title="slicer_disp" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b34234862fb2e38df45bcb77819b989dffbe834d_2_690x362.jpeg" alt="slicer_disp" data-base62-sha1="pzNji0YuAyF3dNf6Pcd8Bdshehv" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b34234862fb2e38df45bcb77819b989dffbe834d_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b34234862fb2e38df45bcb77819b989dffbe834d_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b34234862fb2e38df45bcb77819b989dffbe834d_2_1380x724.jpeg 2x" data-dominant-color="2C2B30"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_disp</span><span class="informations">1916×1006 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What would you recommend to correct?<br>
Thanks for the help in advance!</p>
<p>Operating system: Windows 10, 64-bit<br>
Slicer version: 4.13.0 -2020-11-02 (nightly build)</p>

---

## Post #2 by @jamesobutler (2020-11-03 17:20 UTC)

<p>Welcome <a class="mention" href="/u/kalman">@Kalman</a>,</p>
<p>Yes this is a know issue with the current Slicer preview. You should use the Current Slicer stable (4.11.20200930)</p>
<p>For more details see:</p><aside class="quote" data-post="2" data-topic="14309">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slice-view-not-showing-images/14309/2">Slice view not showing images?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    It is the top open issue. See
  </blockquote>
</aside>


---

## Post #3 by @jamesobutler (2020-11-03 17:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Considering the number of reports of this on the forum, it might be best to “sticky” one of these posts to the top of the forum.</p>

---

## Post #4 by @Kalman (2020-11-03 17:29 UTC)

<p>Thank you for the quick reply <a class="mention" href="/u/jamesobutler">@jamesobutler</a>!<br>
First I’ve tried to search a topic for this issue, but as I see now, I used different terminology for searching.</p>
<p>If one looking for it, where could the latest ‘stable nightly-build version’ be downloaded? (as some newer segmentation tools can only accessed via the beta version, and I don’t have the installer file)</p>

---

## Post #5 by @jamesobutler (2020-11-03 17:42 UTC)

<p>There is a new Stable release which is Slicer 4.11.20200930 which can be downloaded from <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>.  The previous stable was Slicer 4.10.2 which was about 2 years old at the time of the new stable release and it was commonly advised to use the Slicer preview build for latest features.  Now that advice has changed as the old Slicer preview has become the stable release of Slicer 4.11.20200930 and the current Slicer preview builds are unstable at the moment with various problems.</p>
<p>If you aren’t requiring Slicer updates since 2020-09-30, that new stable should work well for whatever tools you need.</p>

---

## Post #6 by @Kalman (2020-11-03 17:47 UTC)

<p>Thank you very much!<br>
Basically, I would need the Segment Editor’s ‘Wrap solidify’ tool and the ‘seed locality’ option of the ‘Grow from seeds’ effect (which was originally added only to the beta versions).</p>

---

## Post #7 by @jamesobutler (2020-11-03 17:52 UTC)

<p>“Seed Locality” of the “Grow from seeds” effect is available in the stable Slicer-4.11.20200930<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/024f09b64a283e050e2bcf636493688dda129d59.jpeg" data-download-href="/uploads/short-url/kqia4bnBQAevA7ejVtaKRG5VBD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/024f09b64a283e050e2bcf636493688dda129d59_2_690x373.jpeg" alt="image" data-base62-sha1="kqia4bnBQAevA7ejVtaKRG5VBD" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/024f09b64a283e050e2bcf636493688dda129d59_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/024f09b64a283e050e2bcf636493688dda129d59_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/024f09b64a283e050e2bcf636493688dda129d59_2_1380x746.jpeg 2x" data-dominant-color="76767E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 291 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>“Wrap solidify” is available after installing the “SurfaceWrapSolidify” extension from the Extensions Manager.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99194add81a4eaeeb16efecf1e35d17644b11cf9.png" data-download-href="/uploads/short-url/lQneZqx7Of2z2ZUvAULPTTxSv33.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99194add81a4eaeeb16efecf1e35d17644b11cf9_2_690x376.png" alt="image" data-base62-sha1="lQneZqx7Of2z2ZUvAULPTTxSv33" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99194add81a4eaeeb16efecf1e35d17644b11cf9_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99194add81a4eaeeb16efecf1e35d17644b11cf9_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99194add81a4eaeeb16efecf1e35d17644b11cf9_2_1380x752.png 2x" data-dominant-color="F9FBFC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1922×1049 85.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @Kalman (2020-11-03 17:57 UTC)

<p>Super! Thank you so much for the help <a class="mention" href="/u/jamesobutler">@jamesobutler</a>!</p>

---

## Post #9 by @lassoan (2020-11-03 20:46 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="14407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Considering the number of reports of this on the forum, it might be best to “sticky” one of these posts to the top of the forum.</p>
</blockquote>
</aside>
<p>Good idea, it might help a bit. I’ve pinned <a href="https://discourse.slicer.org/t/no-images-shown-in-slice-viewers-in-latest-preview-release-slicer-4-13-0/13899">a topic about this issue for a week</a> (hopefully the issue will be resolved very soon).</p>

---
