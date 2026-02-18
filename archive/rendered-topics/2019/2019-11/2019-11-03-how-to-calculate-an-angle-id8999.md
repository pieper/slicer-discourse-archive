# How to calculate an angle?

**Topic ID**: 8999
**Date**: 2019-11-03
**URL**: https://discourse.slicer.org/t/how-to-calculate-an-angle/8999

---

## Post #1 by @Romeo_Guevara (2019-11-03 01:58 UTC)

<p>i need to now, how to calculate an angle in the last version of slicer, thanls</p>

---

## Post #2 by @lassoan (2019-11-03 05:02 UTC)

<p>In Slicer Preview Release that you download on November 4, 2019 (or later), you can add angle measurements by selecting angle markups on the toolbar and clicking in the viewers. You can see the angle values in 3D views and in Markups module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d1acd2b968abfdc962ac5f1886460501ca04eb1.jpeg" data-download-href="/uploads/short-url/b06bB3i5PMfimv65JmvHxSTGykN.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d1acd2b968abfdc962ac5f1886460501ca04eb1_2_584x500.jpeg" alt="image" data-base62-sha1="b06bB3i5PMfimv65JmvHxSTGykN" width="584" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d1acd2b968abfdc962ac5f1886460501ca04eb1_2_584x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d1acd2b968abfdc962ac5f1886460501ca04eb1_2_876x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d1acd2b968abfdc962ac5f1886460501ca04eb1_2_1168x1000.jpeg 2x" data-dominant-color="B5B5B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1193×1020 287 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Romeo_Guevara (2019-11-03 10:44 UTC)

<p>Thank you very much, another question, do you know how to calculate the position of the angiograph, to calculate the angulation I need to get a better image?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b53f371e3766a7fdcbeacb9da81c4531b1ba2080.jpeg" data-download-href="/uploads/short-url/pRnRl3Gcbc9tohwAZ8Kpho7E8a4.jpeg?dl=1" title="Screenshot_20191103_054346_com.android.chrome.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b53f371e3766a7fdcbeacb9da81c4531b1ba2080_2_240x500.jpeg" alt="Screenshot_20191103_054346_com.android.chrome.jpg" data-base62-sha1="pRnRl3Gcbc9tohwAZ8Kpho7E8a4" width="240" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b53f371e3766a7fdcbeacb9da81c4531b1ba2080_2_240x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b53f371e3766a7fdcbeacb9da81c4531b1ba2080_2_360x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b53f371e3766a7fdcbeacb9da81c4531b1ba2080_2_480x1000.jpeg 2x" data-dominant-color="EEEFF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20191103_054346_com.android.chrome.jpg</span><span class="informations">1080×2244 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2019-11-03 18:32 UTC)

<p>Can your angio system do 3D reconstruction or do you have a 3D angio CT image? If yes, then you can determine optimal viewing angles from that.</p>
<p>If you only have access to 2D imaging then it is up to you to find the optimal viewing angle.</p>

---

## Post #5 by @Romeo_Guevara (2019-11-05 02:16 UTC)

<p>I cannot load DICOM images, the program closes automatically, how do I solve this problem? Thank you.</p>

---

## Post #6 by @lassoan (2019-11-05 03:04 UTC)

<p>Maybe you run into <a href="https://discourse.slicer.org/t/cancellous-bone-fill-for-3d-printing/8952/13">this</a> issue. Download the <em>current</em> Slicer Preview version, open Application Settings in Edit menu. In DICOM section, change “Database location” to a new empty folder.</p>

---

## Post #7 by @Romeo_Guevara (2019-11-05 12:16 UTC)

<p>Excellent, it worked…</p>

---

## Post #8 by @lassoan (2019-11-05 12:30 UTC)

<p>What Slicer version did you use before? Were you prompted to update your database when you first opened it with Slicer Preview Release?</p>
<p>By any chance, could you share with me the content of the previous dicom database folder so that we can investigate why opening it crashed the application? (you can send me private message by clicking on my name and then on the mail icon)</p>

---

## Post #9 by @Romeo_Guevara (2019-11-05 19:30 UTC)

<ul>
<li>
<p>What Slicer version did you use before?  The Stable release for windows  4.10.2</p>
</li>
<li>
<p>Were you prompted to update your database when you first opened it with Slicer Preview Release?  No</p>
</li>
<li>
<p>By any chance, could you share with me the content of the previous dicom database folder so that we can investigate why opening it crashed the application? I deleted the previous       version and the folders.   But if you need another kind of information I will gladly send it to you</p>
</li>
</ul>

---

## Post #11 by @lassoan (2019-11-06 12:10 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-define-vessel-centerline/9042">How to define vessel centerline</a></p>

---

## Post #12 by @Romeo_Guevara (2019-11-07 00:18 UTC)

<p>Is there a way to create a centerline like the one in the image?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19f7a15c1d996429c63f96384dad3315003cf293.jpeg" data-download-href="/uploads/short-url/3HItTNse0F1pzAiku8O8Np2lpDB.jpeg?dl=1" title="2019-11-06 (1).jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19f7a15c1d996429c63f96384dad3315003cf293_2_690x388.jpeg" alt="2019-11-06 (1).jpg" data-base62-sha1="3HItTNse0F1pzAiku8O8Np2lpDB" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19f7a15c1d996429c63f96384dad3315003cf293_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19f7a15c1d996429c63f96384dad3315003cf293_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19f7a15c1d996429c63f96384dad3315003cf293_2_1380x776.jpeg 2x" data-dominant-color="7B7B7C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2019-11-06 (1).jpg</span><span class="informations">1920×1080 676 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @Romeo_Guevara (2019-11-18 00:08 UTC)

<p>Good night, currently, does 3D Slicer have any international approval for medical use? regards</p>

---

## Post #14 by @rkikinis (2019-11-18 00:41 UTC)

<p>No, as far as I know. But nothing prevents a user from seeking such an approval. The license has no give back requirement.</p>

---

## Post #15 by @rkikinis (2019-11-18 00:44 UTC)

<p>You can have Slicer display the Slice intersections. Shift plus mouse movement will allow you to navigate slices.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cff0cb9a949b8bcd5e56ac585f37a8781230e490.png" data-download-href="/uploads/short-url/tFwJKQkuTYfneNsxGSqRqzGB4qs.png?dl=1" title="Screen Shot 2019-11-17 at 7.43.15 PM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cff0cb9a949b8bcd5e56ac585f37a8781230e490_2_362x499.png" alt="Screen Shot 2019-11-17 at 7.43.15 PM.png" data-base62-sha1="tFwJKQkuTYfneNsxGSqRqzGB4qs" width="362" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cff0cb9a949b8bcd5e56ac585f37a8781230e490_2_362x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cff0cb9a949b8bcd5e56ac585f37a8781230e490.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cff0cb9a949b8bcd5e56ac585f37a8781230e490.png 2x" data-dominant-color="D2D2D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2019-11-17 at 7.43.15 PM.png</span><span class="informations">504×696 69.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @lassoan (2019-11-18 04:25 UTC)

<blockquote>
<p>does 3D Slicer have any international approval for medical use?</p>
</blockquote>
<p>Slicer has been used clinically in many projects in many countries, as described in thousands of papers that cite Slicer (see a selection <a href="http://www.spl.harvard.edu/publications/gallery">here</a>). For each use case, it is your responsibility to ensure that Slicer fits for the purpose and obtain the necessary approvals. See more information in these related discussions:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/clinical-use-of-slicer-extensions/1630" class="inline-onebox">Clinical use of Slicer extensions?</a></li>
<li><a href="https://discourse.slicer.org/t/multiple-module-panels/2569/3" class="inline-onebox">Multiple module panels - #3 by lassoan</a></li>
<li><a href="https://discourse.slicer.org/t/2d-3d-fill-tool/2682/16" class="inline-onebox">2D/3D fill tool - #16 by lassoan</a></li>
</ul>
<aside class="quote no-group" data-username="Romeo_Guevara" data-post="12" data-topic="8999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/romeo_guevara/48/3539_2.png" class="avatar"> Romeo_Guevara:</div>
<blockquote>
<p>Is there a way to create a centerline like the one in the image?</p>
</blockquote>
</aside>
<p>Yes, and there are several options. Your question has been already forked out to this topic, let’s continue the discussion there: <a href="https://discourse.slicer.org/t/how-to-define-vessel-centerline/9042" class="inline-onebox">How to define vessel centerline</a></p>

---
