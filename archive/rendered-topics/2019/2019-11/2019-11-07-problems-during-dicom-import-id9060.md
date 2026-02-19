---
topic_id: 9060
title: "Problems During Dicom Import"
date: 2019-11-07
url: https://discourse.slicer.org/t/9060
---

# Problems during Dicom import

**Topic ID**: 9060
**Date**: 2019-11-07
**URL**: https://discourse.slicer.org/t/problems-during-dicom-import/9060

---

## Post #1 by @JoeCrozier (2019-11-07 14:11 UTC)

<p>Slicer Version 4.11.0<br>
Windows 10</p>
<p>Hello, I’m having trouble when importing dicom files, specifically files that have been stored on google drive and downloaded.  Let me explain:</p>
<p>Normally I bring dicoms over to my workstation on a usb or similar direct transfer method.  When I import them, they work great, as expected.</p>
<p>Recently I’ve been working on a project where the images (that loaded correctly into slicer on someone else’s computer) were then uploaded into google drive (staying in their respective folders) and downloaded onto my computer, and I’m having trouble importing them.</p>
<p>Obviously this may be a google drive problem, but I’m wondering if there is anything I can do on the 3dSlicer end to fix this, here’s what happens:</p>
<p>Lets say I’m trying to import these images:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e26d32cd0bf64b1ddc30517ca6b78f862012b5f4.png" data-download-href="/uploads/short-url/wj3RCGzQJhjlOXaoIF9ANuxgPBy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e26d32cd0bf64b1ddc30517ca6b78f862012b5f4.png" alt="image" data-base62-sha1="wj3RCGzQJhjlOXaoIF9ANuxgPBy" width="690" height="348" data-dominant-color="F1F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">886×448 34.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Everything in that folder should be just one series of coronal face CT scan images.</p>
<p>3d slicer reads it as one series:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f27c61a5ad62fee6ca460908698570e24a18bb04.png" data-download-href="/uploads/short-url/yB8265DIlTkgO8Qtdh0COCya1ms.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f27c61a5ad62fee6ca460908698570e24a18bb04_2_690x227.png" alt="image" data-base62-sha1="yB8265DIlTkgO8Qtdh0COCya1ms" width="690" height="227" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f27c61a5ad62fee6ca460908698570e24a18bb04_2_690x227.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f27c61a5ad62fee6ca460908698570e24a18bb04_2_1035x340.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f27c61a5ad62fee6ca460908698570e24a18bb04_2_1380x454.png 2x" data-dominant-color="E4EBF4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1536×507 19.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But then splits it into a million “chunks”:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42668554c603208b7623db45ab8ce5affc1ebdaa.png" data-download-href="/uploads/short-url/9tpa6cwmg82D69bH5XIf7P1CRtg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42668554c603208b7623db45ab8ce5affc1ebdaa.png" alt="image" data-base62-sha1="9tpa6cwmg82D69bH5XIf7P1CRtg" width="690" height="191" data-dominant-color="EEF1F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1543×429 19.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I load one of those, it seems like it is a “few” of the total images, or something wrong like that:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8de58e1af0dca1bc27b6a908d608254b1bd0700.png" data-download-href="/uploads/short-url/uWvvDwA2O2M0fMU7MJuuwmvSGMU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8de58e1af0dca1bc27b6a908d608254b1bd0700_2_690x344.png" alt="image" data-base62-sha1="uWvvDwA2O2M0fMU7MJuuwmvSGMU" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8de58e1af0dca1bc27b6a908d608254b1bd0700_2_690x344.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8de58e1af0dca1bc27b6a908d608254b1bd0700_2_1035x516.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8de58e1af0dca1bc27b6a908d608254b1bd0700_2_1380x688.png 2x" data-dominant-color="62626B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1809×903 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any idea how to tell 3dSlicer “No, those all go together”.   Again, when imported on the original computer (before going to google drive, but in the same overall folder structure) it imports correctly.</p>

---

## Post #2 by @lassoan (2019-11-07 14:14 UTC)

<p>Could you please try with latest Slicer Preview Release? We have completely reworked DICOM infrastructure recently.</p>

---

## Post #3 by @JoeCrozier (2019-11-07 14:16 UTC)

<p>The 4.11.0 that was built on 2019-11-07?   Will do, and will report back.</p>

---

## Post #4 by @JoeCrozier (2019-11-07 14:23 UTC)

<p>Well, um… that didn’t work.  In fact, when I open slicer and see the welcome screen, the second I hit “load dicom data” it closes the programs.  Just instant crash.</p>

---

## Post #5 by @lassoan (2019-11-07 14:29 UTC)

<p>This is awesome. I’m trying to get a database that causes crash on startup (it happened to two other users). Could you zip the content of your DICOM database folder and send me in a private message (click on my name and the email icon)?</p>
<p>When you opened the new preview release of Slicer, was another Slicer instance still running?<br>
If you go to menu: Edit / Application settings / DICOM section. What folder is shown as Database location?</p>
<p>You can fix the crash by choosing a new empty folder as “Database location”.</p>

---

## Post #6 by @JoeCrozier (2019-11-07 14:31 UTC)

<p>Haha glad I can help, but not sure I’d call it “awesome” haha.</p>
<p>No other instances were running.  The folder that’s shown as the database location is:<br>
C:/Users/MyName/Documents/SlicerDicomDatabase</p>
<p>Will zip and send you database in two seconds.</p>

---

## Post #7 by @JoeCrozier (2019-11-07 14:38 UTC)

<p>Sent the zip in email.  Choosing new empty folder for database location prevented the crash, but the new dicom system didn’t fix the original problem:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01040e5f798cacadf5c150f105e6375f241dfeb9.png" data-download-href="/uploads/short-url/8ZaoIh7d53BcKvUU3JtSWZ3sZb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01040e5f798cacadf5c150f105e6375f241dfeb9_2_690x378.png" alt="image" data-base62-sha1="8ZaoIh7d53BcKvUU3JtSWZ3sZb" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01040e5f798cacadf5c150f105e6375f241dfeb9_2_690x378.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01040e5f798cacadf5c150f105e6375f241dfeb9_2_1035x567.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01040e5f798cacadf5c150f105e6375f241dfeb9_2_1380x756.png 2x" data-dominant-color="F1F5F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1795×984 48.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Still loads the one folder as a bunch of different chunks</p>

---

## Post #8 by @lassoan (2019-11-07 14:47 UTC)

<p>Can you right-click on the series, choose to view metadata, and search for “ImageOrientationPatient”? If you move the slider to browse slices, the value should remain exactly the same.</p>

---

## Post #9 by @JoeCrozier (2019-11-07 14:59 UTC)

<p>It does not.  When I move the slider, the numbers don’t change a ton, but they do “wiggle”.<br>
For example:<br>
This is 17/181:  [6] 0.9999975562, 9.125343058e-05, -0.00<strong>2207435435</strong>, 9.117864101e-05, 0.9965941906, 0.08246236295<br>
This is 18/181: [6] 0.9999975562, 9.125343058e-05, -0.00<strong>2207510173</strong>, 9.110382234e-05, 0.9965941906, 0.08246242255</p>

---

## Post #10 by @pieper (2019-11-07 15:04 UTC)

<p><a class="mention" href="/u/joecrozier">@JoeCrozier</a> is this a google drive file stream?  If so, you might need to pin the files onto your system and wait until it downloads.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dab26164889b2d2c3bec76a6384e2ddcb4a8b4d4.png" alt="image" data-base62-sha1="vcGgxV1rbToh2H5C9hL059hVGrW" width="675" height="115"></p>

---

## Post #11 by @JoeCrozier (2019-11-07 15:22 UTC)

<p>No I don’t believe it was a file stream.  I had trouble simply “downloading” from google drive (for other reasons, it took forever to zip) so eventually the way that got on my computer was through the google “Backup and Sync” app, and I believe everything was fully downloaded.</p>
<p>Again, I realize this might be a google problem that scrambled something, but is there anything we can do on the 3dSlicer end to fix it?</p>

---

## Post #12 by @lassoan (2019-11-07 16:02 UTC)

<p>OK, the difference in slice orientations explain why Slicer shows all those loadables separately. You can disable showing these (just to clean up the view a bit), in Application Settings / DICOM / Allow loading subseries by time.</p>
<p>Then, enable “Acquisition geometry regularization” and try each “DICOM reader approach”.</p>
<p>What software has created these files?</p>
<p><a class="mention" href="/u/pieper">@pieper</a> Does acquisition regularization can fix up series with not-exactly-parallel slices?</p>

---

## Post #13 by @JoeCrozier (2019-11-07 16:41 UTC)

<p>The files were originally exported out of Terarecon from our hospitals PACS server.  I’m not sure what original scanner made them or anything.  And again, when first exported out of terarecon and opened in 3dSlicer (on a different computer) they opened fine.  The problem is the student who was working on them (and had 3dslicer to view them on their computer) shared them with us(a resident and I) by uploading them to google drive.  I don’t believe they did anything to modify them prior besides dragging and dropping from their computer to google drive.  When I simply go to google drive and click “download” I run into this problem:  <a href="https://support.google.com/drive/thread/4965355?hl=en" rel="nofollow noopener">https://support.google.com/drive/thread/4965355?hl=en</a>  seems like a bunch of people have trouble downloading from there.<br>
So anyhow I then finally was able to download them using the google “Backup and Sync” app, but once they are on my computer they run into the problem we’ve discussed.</p>
<p>To clarify your most recent suggestion:<br>
Allow loading subseries by time was initially turned off when I first went into the menu, and i just clicked to turn it on.  I’ve also attempted using each of the dicom reader approaches.</p>
<p>Also acquisition geometry regularization was initially on and I’ve tried it both on and off.</p>
<p>So far it still looks weird.  Do these settings affect when I initially “import” the dicom data, or only when I load it?  In other words, should I delete the scan from my database and reimport it after changing settings?</p>

---

## Post #14 by @JoeCrozier (2019-11-07 16:43 UTC)

<p>Further details:  I’m not sure they’re still on our hospital server (or we can figure out who they were prior to randomization) and I know they’re not on the student’s computer for me to get via usb.  So I’d love to salvage these scans in whatever way I can.</p>

---

## Post #15 by @lassoan (2019-11-07 17:34 UTC)

<aside class="quote no-group" data-username="JoeCrozier" data-post="13" data-topic="9060">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c4cdca/48.png" class="avatar"> JoeCrozier:</div>
<blockquote>
<p>Do these settings affect when I initially “import” the dicom data, or only when I load it?</p>
</blockquote>
</aside>
<p>These settings only affect loading, so you don’t need to reimport, but you may need to restart Slicer for the changes to take effect.</p>

---

## Post #16 by @JoeCrozier (2019-11-07 17:34 UTC)

<p>Hmm.  Restarted it each time it prompted, and kept loading weird.</p>
<p>Any other ideas or am I out of luck?</p>

---

## Post #17 by @lassoan (2019-11-07 17:36 UTC)

<p>There are a couple of more things to try, but it is easier if we can have direct access to the data.</p>

---

## Post #18 by @JoeCrozier (2019-11-07 17:41 UTC)

<p>Just emailed you links to it.  Good luck!</p>

---

## Post #19 by @lassoan (2019-11-07 18:50 UTC)

<p>The reconstructed series contain an “overview” slice, which is an orthogonal cross-section of the reconstructed volume, showing each slice position. Since this cross-section image has the same series instance UID, appears to have valid position, orientation, etc. it is lumped together with all the image slices, therefore breaking the reconstruction.</p>
<p>The overview slice has different orientation than the other slices, which would normally be usable to weed out an outlier slice. However, in this case the 3D slices don’t have the exact same orientation either, so this mechanism could not be applied.</p>
<p>The only field that is clearly different between the overview image and 3D slices is ImageType (0008,0008). Since ImageType is expected to be the same among all slices and we have seen such overview images breaking DICOM import before, I’ve added ImageType field as a subseries grouping field, this will allow load the overview slice and 3D volume as two separate images.</p>
<p>I’ve tested it on your images and it allows correct loading of the images. This new feature will be available in Slicer Preview Release that you download tomorrow or later.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32be5ce6865da5456afd11429c34832f993de2bf.png" data-download-href="/uploads/short-url/7eTITAwUXMZWTKiTx1a2E7mnLdl.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32be5ce6865da5456afd11429c34832f993de2bf_2_690x319.png" alt="image" data-base62-sha1="7eTITAwUXMZWTKiTx1a2E7mnLdl" width="690" height="319" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32be5ce6865da5456afd11429c34832f993de2bf_2_690x319.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32be5ce6865da5456afd11429c34832f993de2bf.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32be5ce6865da5456afd11429c34832f993de2bf.png 2x" data-dominant-color="E4ECF3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">992×459 24.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve implemented a fix for the crash that occurs when an old database is attempted to be opened. It’ll be available in tomorrow’s preview release, too.</p>

---

## Post #20 by @JoeCrozier (2019-11-07 18:57 UTC)

<p>This is awesome!  Thank you!</p>

---

## Post #21 by @pieper (2019-11-07 19:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="9060">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> Does acquisition regularization can fix up series with not-exactly-parallel slices?</p>
</blockquote>
</aside>
<p>Yes, in general it will do it will do that, but only if the rotational difference led to more than 1/100th of a millimeter difference at the corners between the per-frame orientation and using the constant orientation throughout the volume.</p>

---

## Post #22 by @Juicy (2019-11-08 08:53 UTC)

<p>Hi Andras,</p>
<p>I actually had an error recently where one of these “overview” slices caused the volume to mirror about the sagittal plane. I messaged Steve peiper but I can copy you in as well. This was using 4.10.2</p>
<p>Thanks</p>

---

## Post #23 by @lassoan (2019-11-08 12:42 UTC)

<p>It would be great if you could test with today’s Preview Release if you can load your image correctly by using the loadables split by image type.</p>

---

## Post #24 by @JoeCrozier (2019-11-08 13:53 UTC)

<p>Works great!  It still splits it like so:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e0dd3e95c8ea1cfe5560e739dcb9c3f6393b2fb.png" data-download-href="/uploads/short-url/dq2vv9f0NfP1O9UsH9qgLpxptaP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e0dd3e95c8ea1cfe5560e739dcb9c3f6393b2fb.png" alt="image" data-base62-sha1="dq2vv9f0NfP1O9UsH9qgLpxptaP" width="690" height="477" data-dominant-color="EAEFF6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1330×920 36.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>but then it loads just fine like so:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c97d43563b2f6739f99fdd7cf7e985bc65acc280.jpeg" data-download-href="/uploads/short-url/sKsltsCQC2K7XaEqNhkKeXXZrlm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c97d43563b2f6739f99fdd7cf7e985bc65acc280_2_690x455.jpeg" alt="image" data-base62-sha1="sKsltsCQC2K7XaEqNhkKeXXZrlm" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c97d43563b2f6739f99fdd7cf7e985bc65acc280_2_690x455.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c97d43563b2f6739f99fdd7cf7e985bc65acc280_2_1035x682.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c97d43563b2f6739f99fdd7cf7e985bc65acc280_2_1380x910.jpeg 2x" data-dominant-color="41414D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1397×923 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also didn’t crash when I first hit to load dicom</p>

---

## Post #25 by @lassoan (2019-11-08 14:43 UTC)

<p>Happy to hear that it works well.</p>
<p>You can disable “Allow loading subseries by time” to remove all the “… - contentTime X” loadables from the list (it is not necessary for you and adds a lot of clutter to the loadable list).</p>
<p>Note that you had problems loading secondary captures (with series number 500, 501, 502, and not with primary images that typically have series number 1, 2, 3, …). So, check loading of secondary captures, too, which has series numbers in the hundreds and odd slice count (e.g, “302: spin” acquisition containing 73 slices).</p>

---

## Post #26 by @JoeCrozier (2019-11-08 14:47 UTC)

<p>Uh oh:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa53a8b0239d3f445b1fdf5a0b11896bea769628.png" data-download-href="/uploads/short-url/oiMpjYNbSgWmkpG1nVfiXv56XtS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa53a8b0239d3f445b1fdf5a0b11896bea769628_2_690x473.png" alt="image" data-base62-sha1="oiMpjYNbSgWmkpG1nVfiXv56XtS" width="690" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa53a8b0239d3f445b1fdf5a0b11896bea769628_2_690x473.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa53a8b0239d3f445b1fdf5a0b11896bea769628_2_1035x709.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa53a8b0239d3f445b1fdf5a0b11896bea769628_2_1380x946.png 2x" data-dominant-color="363642"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1386×951 83.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This was the “501” from the patient I sent you in email.</p>

---

## Post #27 by @lassoan (2019-11-08 14:50 UTC)

<p>In advanced view, choose the loadables split by image type (see my screenshot above).</p>

---

## Post #28 by @JoeCrozier (2019-11-08 14:50 UTC)

<p>Nevermind, when i select to load the “content time 2” it works fine</p>

---

## Post #29 by @lassoan (2019-11-08 14:54 UTC)

<p>Yes, you have now access to both the “overview” image and the 3D volume (as image type 1 and 2).</p>
<p>The overview image is a single-slice volume on an oblique plane. If you want to see the complete slice then it then click “Rotate to volume plane”.</p>

---

## Post #30 by @JoeCrozier (2019-11-08 14:55 UTC)

<p>Thank you so much for your help!  Images aren’t lost anymore!</p>

---

## Post #31 by @lassoan (2019-11-11 17:08 UTC)

<p>We continued the discussion in private and it came up that there is a risk that users ignore the warning that they get at loading and may proceed with loading the mixed localizer+3D volume slices, which may result in loading with incorrect geometry (mirroring). I copy posts from that private thread here below.</p>
<aside class="quote no-group" data-username="JoeCrozier">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c4cdca/48.png" class="avatar"> JoeCrozier:</div>
<blockquote>
<p>I have downloaded the nightly 4.11.0 and loaded the image set into the new DICOM module.</p>
<p>When I pressed load, an error message pops up suggesting that I examine the data in advanced mode. If I press load anyway at this point then the a normal looking volume appears except that it is mirrored.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/213c4dcd546584fdffc7886b02cb2f6c72a074df.jpeg" alt="Error%20Message%20pop%20up" data-base62-sha1="4K0XkXu3vLlidIc7IIgrnAtZzjh" width="516" height="103"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5013ba39b9a00ae7afdf81c6b67e021c3bf3a38b.jpeg" data-download-href="/uploads/short-url/bqosJEePMKpykujih0FRamdSfZF.jpeg?dl=1" title="Mirrored%20Volume"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5013ba39b9a00ae7afdf81c6b67e021c3bf3a38b_2_690x472.jpeg" alt="Mirrored%20Volume" data-base62-sha1="bqosJEePMKpykujih0FRamdSfZF" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5013ba39b9a00ae7afdf81c6b67e021c3bf3a38b_2_690x472.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5013ba39b9a00ae7afdf81c6b67e021c3bf3a38b_2_1035x708.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5013ba39b9a00ae7afdf81c6b67e021c3bf3a38b.jpeg 2x" data-dominant-color="8C8D94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Mirrored%20Volume</span><span class="informations">1251×856 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now if I close the scene, reload the image set again and open the advanced area I notice that the images have been separated by image type and image orientation patient. If I load the two image groups separately as shown in the following screenshot then two volumes appear. One volume is just the ‘orientation’ image and the other is the main volume which in this case has loaded correctly and is not mirrored.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28a1b7a926e789284851da5392f5c8a7495c4a52.jpeg" data-download-href="/uploads/short-url/5NrzLedZNajPZkhjlGSKsqnGXLA.jpeg?dl=1" title="Load%20Volume%20Separately"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28a1b7a926e789284851da5392f5c8a7495c4a52_2_677x500.jpeg" alt="Load%20Volume%20Separately" data-base62-sha1="5NrzLedZNajPZkhjlGSKsqnGXLA" width="677" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28a1b7a926e789284851da5392f5c8a7495c4a52_2_677x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28a1b7a926e789284851da5392f5c8a7495c4a52_2_1015x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28a1b7a926e789284851da5392f5c8a7495c4a52.jpeg 2x" data-dominant-color="E9EDF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Load%20Volume%20Separately</span><span class="informations">1344×992 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44462b1dc9932704821e964e3e7de93f81e17e4f.jpeg" data-download-href="/uploads/short-url/9JYNNhInp8g5wsgcESn5I9pDvBB.jpeg?dl=1" title="Non%20Mirrored"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/44462b1dc9932704821e964e3e7de93f81e17e4f_2_690x472.jpeg" alt="Non%20Mirrored" data-base62-sha1="9JYNNhInp8g5wsgcESn5I9pDvBB" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/44462b1dc9932704821e964e3e7de93f81e17e4f_2_690x472.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/44462b1dc9932704821e964e3e7de93f81e17e4f_2_1035x708.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44462b1dc9932704821e964e3e7de93f81e17e4f.jpeg 2x" data-dominant-color="84868E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Non%20Mirrored</span><span class="informations">1251×856 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57781fbd0df8e1097ca93e848b268b370622776f.jpeg" data-download-href="/uploads/short-url/ctMU4nKsj8c3yqDcUD4AoPUi7nN.jpeg?dl=1" title="Orientation%20Image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57781fbd0df8e1097ca93e848b268b370622776f_2_690x472.jpeg" alt="Orientation%20Image" data-base62-sha1="ctMU4nKsj8c3yqDcUD4AoPUi7nN" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57781fbd0df8e1097ca93e848b268b370622776f_2_690x472.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57781fbd0df8e1097ca93e848b268b370622776f_2_1035x708.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57781fbd0df8e1097ca93e848b268b370622776f.jpeg 2x" data-dominant-color="787980"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Orientation%20Image</span><span class="informations">1251×856 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would like to have sent you the offending anonymised DICOM but when I run the images through DICOM cleaner it actually does not exhibit the same behavior anymore, which is frustrating. When loading the anonymised DICOM it is still mirrored but looks obviously broken.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26de0de0e9d4a0b82b8fb8f4a3452d9a145214c1.jpeg" data-download-href="/uploads/short-url/5xPTm3ulhHUSqxGVE0RP4SRTpBf.jpeg?dl=1" title="Anon%20DICOM"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26de0de0e9d4a0b82b8fb8f4a3452d9a145214c1_2_690x472.jpeg" alt="Anon%20DICOM" data-base62-sha1="5xPTm3ulhHUSqxGVE0RP4SRTpBf" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26de0de0e9d4a0b82b8fb8f4a3452d9a145214c1_2_690x472.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26de0de0e9d4a0b82b8fb8f4a3452d9a145214c1_2_1035x708.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26de0de0e9d4a0b82b8fb8f4a3452d9a145214c1.jpeg 2x" data-dominant-color="83838A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Anon%20DICOM</span><span class="informations">1251×856 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I guess the main danger is that people seem to casually ignore warnings which they don’t understand and just see what happens. In this case one of our technicians did just that and because the volume looked pretty normal and because it is difficult to pick up mirroring about the sagittal plane a mirrored biomodel was produced.</p>
<p>Perhaps when that first window pops up then the user should be forced to look at advanced mode instead of being able to skip past it by pressing ok? Or maybe by default the images should be separated by image orientation patient and loaded as separate volumes so that if the user casually skips past the warning then at least there would be less danger of an erroneous volume appearing?</p>
<p>A colleague also informed me that he has seen this error occur before on another image set so I don’t think that it is a one off.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We could introduce a “strict mode” in application settings. It could prevent loading of data sets that have associated warning message.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="pieper">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I’m seeing more and more of these pre-MPR’d series so I think we should find some way to detect and deal with them, but I don’t know if there is a good general solution.</p>
<p>What I think is happening here is that the orientation is coming from the first index image, and then the others are essentially sorted by some arbitrary value which sometimes is the exact opposite of what you want, hence the flipping.</p>
<p>Big picture though is that these reformats are not actually useful in Slicer anyway, since they just pre-compute views that you get anyway. So people should be using the original acquisition volume (typically one of the single-digit series, like 2,3,4, not 201, 801, etc).</p>
<p>Coincidentally, I have a study here that I can use to replicate, so I’ll investigate and see if there’s a fix possible.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It seems that “localizer” is the appropriate term for the extra slice (see this post and the ImageType containing “LOCALIZER” word and David Clunie’s DICOM faq).</p>
<p>In the discourse post referenced above, the series is a 3D XA spin reconstruction by Siemens. In this post the images are 3D XA spin reconstructions by GE. So, it is common that they are both 3D spin reconstructions and localizer image is stored in the same series, but image types are different:</p>
<p>Siemens:</p>
<ul>
<li>Localizer slice: DERIVED, SECONDARY, LOCALIZER, MPR, , , PARALLEL</li>
<li>Volume slice: DERIVED, SECONDARY, AXIAL, MPR, , , PARALLEL</li>
</ul>
<p>GE:</p>
<ul>
<li>Localizer slice: DERIVED, SECONDARY, REFORMATTED</li>
<li>Volume slices: DERIVED, SECONDARY, REFORMATTED, AVERAGE</li>
</ul>
<p>DICOM does not strictly specify how to organize series. According to the DICOM standard “Each Series may be associated with exactly one Frame of Reference IE, and if so associated all Composite Instances within the Series shall be spatially or temporally related to each other”. But this very loose definition makes it hard to implement software that can robustly interpret DICOM files, so I think the practice of storing different image types with the same series instance UID should be explicitly stated as valid or invalid in the DICOM standard.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> Could you ask David Clunie’s opinion on this?</p>
<p>Also, would you mind if I copied the last few posts (without images) to the public forum topic?</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="pieper">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I agree, yes - the case I have here is the GE version, where the localizer (instance 1) is type 3 DERIVED, SECONDARY, REFORMATTED and the rest are type 4 DERIVED, SECONDARY, REFORMATTED, AVERAGE.</p>
<p>Interestingly, for the the localizer ImageOrientationPatient is 1, 0, 0, 0, 0, -1 while for the rest it is 0, 1, 0, 0, 0, -1. This makes sense since the localizer is coronal and the rest are sagittal.</p>
<p>Unfortunately we’re either going to end up with heuristics here or perhaps we need to have a more sophisticated user interface that makes it clear to the user what is going on and lets them decide.</p>
<p>For now I think the ScalarVolumePlugin should be hard-coded to detect this pattern (ignore a slice with one different image type).</p>
<p>Yes, I can ask David Clunie. We are at a meeting with him Wed-Fri this week.</p>
<p>It’s fine with me for this discussion to move to the public forum. This is something serious users should be made aware of.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>David’s opinion (and eventually the DICOM standard) is important because based on that we could decide how to handle this: if it’s considered an invalid series then we would refuse to load it and add a rule to fix it in the DICOM Patcher; if it is a valid series then we need to detect the localizer slices in scalar volume plugin and ignore them by default.</p>
<p>localizer (instance 1) is type 3 DERIVED, SECONDARY, REFORMATTED and the rest are type 4 DERIVED, SECONDARY, REFORMATTED, AVERAGE</p>
<p>Note that “3” and “4” are just the multiplicity of the values and not part of the values.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="pieper">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>If it’s invalid we should definitely flag it, but I still would want to try to load it correctly if we feel we can do it confidently. This seems to be a common pattern. My guess is that David will say this is a valid series - it’s very common to have slices with different orientations, so the question is what part of the series maps to a valid Slicer scalar volume.</p>
<p>For most Slicer purposes, these reformats should be avoided in any case. In the study I’m looking at the series 8 is .8 x .8 x 1.0 while the reformat is .8 x .8 . 2.5. which makes is visibly blurry, but only if you zoom in, so I would avoid it for any kind of analysis or planning tasks.</p>
</blockquote>
</aside>

---

## Post #32 by @lassoan (2019-11-11 17:28 UTC)

<p>Yes, it is common to have different orientations (mostly in localizer series), but different image orientations are not the problem. What does not make sense for me is allowing storage of different image types in one series.</p>
<p>I’ve just found <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.16.html#sect_C.8.16.1">section C.8.16.1 of the DICOM standard</a>, which seems to be applicable to all CT and MRI images. My interpretation is that if there are different types within a series then image type field must be set to “MIXED” and frame type contains the per-frame type information. The section also states “Image Type (0008,0008) and Frame Type (0008,9007) shall consist of four values.” which is also violated. The Siemens data set XA for image modality, so C.8.16.1 may not apply. However, the GE data set uses CT modality, so it should respect C.8.16.1.</p>
<p>Anyway, considering the creativity of how device manufacturers are (ab)using the DICOM standard, it would be important to update the standard and explicitly permit this usage (and then properly specify the expected behavior) or prohibit it.</p>

---
