---
topic_id: 40521
title: "Totalsegmentator Failed To Compute Results Status 1 Error"
date: 2024-12-05
url: https://discourse.slicer.org/t/40521
---

# TotalSegmentator: Failed to Compute Results: Status 1 Error

**Topic ID**: 40521
**Date**: 2024-12-05
**URL**: https://discourse.slicer.org/t/totalsegmentator-failed-to-compute-results-status-1-error/40521

---

## Post #1 by @rpaulus (2024-12-05 03:24 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9206e948c2370a26ee4851c962bac852b1eab601.png" data-download-href="/uploads/short-url/kPOw7dfFGBVQBbwmDRmgObDhVFD.png?dl=1" title="Slicer error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9206e948c2370a26ee4851c962bac852b1eab601_2_690x343.png" alt="Slicer error" data-base62-sha1="kPOw7dfFGBVQBbwmDRmgObDhVFD" width="690" height="343" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9206e948c2370a26ee4851c962bac852b1eab601_2_690x343.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9206e948c2370a26ee4851c962bac852b1eab601_2_1035x514.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9206e948c2370a26ee4851c962bac852b1eab601.png 2x" data-dominant-color="7E7E7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer error</span><span class="informations">1254×624 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f766a58b4bdf08b9f48f1c563e491078662782cb.jpeg" data-download-href="/uploads/short-url/ziBQZgIPyxh62M3z4ZYgLXIr45Z.jpeg?dl=1" title="2024-12-04_15-53-42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f766a58b4bdf08b9f48f1c563e491078662782cb_2_690x388.jpeg" alt="2024-12-04_15-53-42" data-base62-sha1="ziBQZgIPyxh62M3z4ZYgLXIr45Z" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f766a58b4bdf08b9f48f1c563e491078662782cb_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f766a58b4bdf08b9f48f1c563e491078662782cb_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f766a58b4bdf08b9f48f1c563e491078662782cb_2_1380x776.jpeg 2x" data-dominant-color="878891"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-12-04_15-53-42</span><span class="informations">1920×1080 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We continue to receive the Status 1 error when attempting to use Total Segmentator. I included a snip of what a user reports seeing and then I included a snip of what the error appears after a reinstallation of the application with the file path pointing to my admin account.</p>
<p>I’ve followed the tutorial guide with using the sample CTA Abdomen and ensured that we had enough CPU memory available. Continuing to receive the error message unfortunately. We are currently using version 5.2.2.</p>
<p>I checked the log and the error that stands out is,</p>
<p>“ERROR: Could not install packages due to an OSError: [WinError 5] Access is denied: ‘C:\Users\aa-RXP036\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\~umpy\.libs\libopenblas.FB5AE2TYXYH2IJRDKGDGQ3XBKLKTF43H.gfortran-win_amd64.dll’”</p>
<p>Would anyone be able to assist with troubleshooting this Status 1 Error?</p>

---

## Post #2 by @lassoan (2024-12-05 03:25 UTC)

<p>Please use the latest Slicer Stable Release or latest Slicer Preview Release.</p>

---

## Post #3 by @rpaulus (2024-12-05 14:19 UTC)

<p>Does the latest download resolve this Status 1 error? My only concern would be if we download the latest version and then attempt to run the program, we receive the same error message as previous. Thank you!</p>

---

## Post #4 by @lassoan (2024-12-05 14:30 UTC)

<p>Yes, most likely the problem will not occur with the latest versions. You do not have to uninstall the old version, so you do not risk anything by installing the current version.</p>

---

## Post #5 by @rpaulus (2024-12-05 14:35 UTC)

<p>Ok, I will download the latest and report back. Thank you!</p>

---

## Post #6 by @rpaulus (2024-12-05 21:10 UTC)

<p>I installed the newest version of 3D Slicer and am on v5.6.2. I was able to complete the CTA abdomen sample data with Total Segmentator under my admin account but I cannot complete the same function within my regular account (same account as our clinical staff). I still receive the same error message stating there was a failure installing the packages. Do you have any suggestions?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d556a7e7c07c71192a546edd714a670598fafd2.jpeg" data-download-href="/uploads/short-url/6t2uk3SdQ52SRjYha5FyldA3Vtw.jpeg?dl=1" title="2024-12-05_15-06-54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d556a7e7c07c71192a546edd714a670598fafd2_2_690x388.jpeg" alt="2024-12-05_15-06-54" data-base62-sha1="6t2uk3SdQ52SRjYha5FyldA3Vtw" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d556a7e7c07c71192a546edd714a670598fafd2_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d556a7e7c07c71192a546edd714a670598fafd2_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d556a7e7c07c71192a546edd714a670598fafd2_2_1380x776.jpeg 2x" data-dominant-color="83828A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-12-05_15-06-54</span><span class="informations">1920×1080 281 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @jamesobutler (2024-12-05 23:18 UTC)

<p>Reading the following threads has relevant information on the topic of extensions installing python packages for Slicer installed to a System rather than User location.</p>
<aside class="quote quote-modified" data-post="5" data-topic="29252">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/5-2-2-silent-installer-not-seeming-to-work-w10/29252/5">5.2.2 silent installer not seeming to work w10</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    The application is fully portable, including all data and settings. 
However, you need to install in a writable location if you want to allow your users to install extensions (as all the extensions and additional Python packages that they pull in must be all available to all users). It might be possible to remove this requirement (e.g., install additional modules and Python packages in the user’s folder), but it may not be easy to implement this and there has not been very strong demand for it (…
  </blockquote>
</aside>

<aside class="quote" data-post="3" data-topic="34805">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/installing-extension-in-users-folder-in-linux/34805/3">Installing extension in user's folder in Linux</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    It’s not set up for that.  Better to either pre-install all extensions in the read-only directory or give each user their own copy of Slicer to install extensions in.
  </blockquote>
</aside>


---

## Post #8 by @rpaulus (2024-12-06 17:51 UTC)

<p>I’m wondering if we possibly don’t have enough memory space on the workstation. We do have enough disk space as we have about 375 GB of free disk space but I’m wondering if this could possibly be the issue?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f98d1a81d1fc396214bd8ebbe773080d7ad5ca4.png" data-download-href="/uploads/short-url/6N3QXJ5mexD13SlMIwfwEvtk5Ks.png?dl=1" title="2024-12-06_11-48-06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f98d1a81d1fc396214bd8ebbe773080d7ad5ca4_2_690x388.png" alt="2024-12-06_11-48-06" data-base62-sha1="6N3QXJ5mexD13SlMIwfwEvtk5Ks" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f98d1a81d1fc396214bd8ebbe773080d7ad5ca4_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f98d1a81d1fc396214bd8ebbe773080d7ad5ca4_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f98d1a81d1fc396214bd8ebbe773080d7ad5ca4_2_1380x776.png 2x" data-dominant-color="B0B1B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-12-06_11-48-06</span><span class="informations">1920×1080 358 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
