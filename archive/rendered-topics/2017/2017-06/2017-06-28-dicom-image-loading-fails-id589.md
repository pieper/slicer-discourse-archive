---
topic_id: 589
title: "Dicom Image Loading Fails"
date: 2017-06-28
url: https://discourse.slicer.org/t/589
---

# DICOM image loading fails

**Topic ID**: 589
**Date**: 2017-06-28
**URL**: https://discourse.slicer.org/t/dicom-image-loading-fails/589

---

## Post #1 by @vetyasin (2017-06-28 15:27 UTC)

<p>Operating system: Windows 7 Ultimate 64 bit.</p>
<p>I can not loading DICOM files. I could uploaded to 4.7.0 slicer when I have Windows 7 Home Basic 64 bit. But it is not now. Screen images and log messages are below. I wonder is problem in the operating system? Help me please:sweat_smile:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/358c1c4d41095a149837d4c05e1e38a10a27c901.JPG" data-download-href="/uploads/short-url/7DHusYYjCrt6arSJRl8yysKCDUB.JPG?dl=1" title="slicer 4.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/358c1c4d41095a149837d4c05e1e38a10a27c901_2_690x451.JPG" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/358c1c4d41095a149837d4c05e1e38a10a27c901_2_690x451.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/358c1c4d41095a149837d4c05e1e38a10a27c901.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/358c1c4d41095a149837d4c05e1e38a10a27c901.jpeg 2x" data-dominant-color="ECEFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer 4.JPG</span><span class="informations">884×578 55.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/b4e51cb4f62d86ad3b1d1f3a82768695cca12f20.JPG" data-download-href="/uploads/short-url/pOgOxvzmkaAk8DtweABCY6Yp4R2.JPG?dl=1" title="slicer 1.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b4e51cb4f62d86ad3b1d1f3a82768695cca12f20_2_690x313.JPG" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b4e51cb4f62d86ad3b1d1f3a82768695cca12f20_2_690x313.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b4e51cb4f62d86ad3b1d1f3a82768695cca12f20_2_1035x469.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4e51cb4f62d86ad3b1d1f3a82768695cca12f20.jpeg 2x" data-dominant-color="E8E9EC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer 1.JPG</span><span class="informations">1303×592 85.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/8c75a1729acd2c9d567f9b985426cc25a14bde8a.JPG" width="661" height="407"><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/fbf3cdebec34ff26f638d977f518664236ad7350.JPG" data-download-href="/uploads/short-url/zWSc02PzmAj2ksxUS9whXlxP8NW.JPG?dl=1" title="slicer 5.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fbf3cdebec34ff26f638d977f518664236ad7350_2_690x364.JPG" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fbf3cdebec34ff26f638d977f518664236ad7350_2_690x364.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fbf3cdebec34ff26f638d977f518664236ad7350_2_1035x546.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbf3cdebec34ff26f638d977f518664236ad7350.jpeg 2x" data-dominant-color="E8E9E5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer 5.JPG</span><span class="informations">1288×681 98.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/1db088ee1c72634172cdcd255dbcddf9f7bd4382.JPG" data-download-href="/uploads/short-url/4eE4ou92yTAI8ziBEPoTIfaQwi6.JPG?dl=1" title="slicer 6.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1db088ee1c72634172cdcd255dbcddf9f7bd4382_2_690x363.JPG" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1db088ee1c72634172cdcd255dbcddf9f7bd4382_2_690x363.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1db088ee1c72634172cdcd255dbcddf9f7bd4382_2_1035x544.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1db088ee1c72634172cdcd255dbcddf9f7bd4382.jpeg 2x" data-dominant-color="E9EBED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer 6.JPG</span><span class="informations">1264×665 88.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/0501856a38269935d2905af035fc68062bad9781.JPG" data-download-href="/uploads/short-url/IhE4MvUqWetANsEfhGhj2gAu4N.JPG?dl=1" title="slicer 3.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/0501856a38269935d2905af035fc68062bad9781_2_690x240.JPG" width="690" height="240" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/0501856a38269935d2905af035fc68062bad9781_2_690x240.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/0501856a38269935d2905af035fc68062bad9781_2_1035x360.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/0501856a38269935d2905af035fc68062bad9781.jpeg 2x" data-dominant-color="DCDDE5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer 3.JPG</span><span class="informations">1234×431 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2017-06-28 15:33 UTC)

<p>You can only load volumes from folders and filenames that does not have special character in their name. Either copy the files to a different folder manually or use the DICOM Patcher module in Slicer to clean up filenames and paths.</p>

---

## Post #3 by @vetyasin (2017-06-28 15:48 UTC)

<p>Thank you for the quick reply.</p>
<p>I have tried. But it did not. The same thing is happening.</p>
<p>Best,</p>

---

## Post #4 by @lassoan (2017-06-28 15:55 UTC)

<p>Please attach the application logs of the attempt after the directory name is fixed (menu: Help / Report a bug).</p>
<p>Have you also tried to clean up your data by running DICOM Patcher?</p>

---

## Post #5 by @fedorov (2017-06-28 16:17 UTC)

<p>Also, what is the location of your DICOM database? Click this and please report:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d257066266586a53b13defa10732ff71bf71f054.png" alt="image" data-base62-sha1="u0KIzjVrulUHDcNcWa1292RKbCk" width="490" height="69"></p>

---

## Post #6 by @vetyasin (2017-06-28 17:53 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/fc0010bf67259b04ce9257637c90c0960f7a0e6b.JPG" data-download-href="/uploads/short-url/zXisGGczD1Mv0G6g7KWWvmxSo6T.JPG?dl=1" title="slicer 7.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fc0010bf67259b04ce9257637c90c0960f7a0e6b_2_690x358.JPG" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fc0010bf67259b04ce9257637c90c0960f7a0e6b_2_690x358.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fc0010bf67259b04ce9257637c90c0960f7a0e6b_2_1035x537.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc0010bf67259b04ce9257637c90c0960f7a0e6b.jpeg 2x" data-dominant-color="E4E6E7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer 7.JPG</span><span class="informations">1254×652 97.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/fc2bcb4675ef9a94877cd9b1bd2aee4af28343b6.JPG" data-download-href="/uploads/short-url/zYO9lU2ht9jwX0221b6rK34aiEK.JPG?dl=1" title="slicer 8.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fc2bcb4675ef9a94877cd9b1bd2aee4af28343b6_2_690x267.JPG" width="690" height="267" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fc2bcb4675ef9a94877cd9b1bd2aee4af28343b6_2_690x267.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fc2bcb4675ef9a94877cd9b1bd2aee4af28343b6_2_1035x400.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc2bcb4675ef9a94877cd9b1bd2aee4af28343b6.jpeg 2x" data-dominant-color="EEF0F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer 8.JPG</span><span class="informations">1200×466 71.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @vetyasin (2017-06-28 17:58 UTC)

<p>[DEBUG][Qt] 28.06.2017 20:13:00 [] (unknown:0) - Session start time …: 2017-06-28 20:13:00<br>
[DEBUG][Qt] 28.06.2017 20:13:00 [] (unknown:0) - Slicer version …: 4.7.0-2017-06-26 (revision 26137) win-amd64 - installed<br>
[DEBUG][Qt] 28.06.2017 20:13:00 [] (unknown:0) - Operating system …: Windows / Vista Professional / Service Pack 1 (Build 6001) - 64-bit<br>
[DEBUG][Qt] 28.06.2017 20:13:00 [] (unknown:0) - Memory …: 5814 MB physical, 11627 MB virtual<br>
[DEBUG][Qt] 28.06.2017 20:13:00 [] (unknown:0) - CPU …: GenuineIntel , 4 cores, 16 logical processors<br>
[DEBUG][Qt] 28.06.2017 20:13:00 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 28.06.2017 20:13:00 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 28.06.2017 20:13:00 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 28.06.2017 20:13:05 [Python] (C:\Program Files\Slicer 4.7.0-2017-06-26\lib\Slicer-4.7\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 28.06.2017 20:13:08 [Python] (C:\Program Files\Slicer 4.7.0-2017-06-26\lib\Slicer-4.7\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 28.06.2017 20:13:08 [Python] (C:\Program Files\Slicer 4.7.0-2017-06-26\lib\Slicer-4.7\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 28.06.2017 20:13:01 [] (unknown:0) - Number of registered modules: 135<br>
[DEBUG][Qt] 28.06.2017 20:13:02 [] (unknown:0) - Number of instantiated modules: 135<br>
[DEBUG][Qt] 28.06.2017 20:13:10 [] (unknown:0) - Number of loaded modules: 135<br>
[DEBUG][Qt] 28.06.2017 20:13:10 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 28.06.2017 20:14:15 [] (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Python] 28.06.2017 20:14:54 [Python] (C:/Program Files/Slicer 4.7.0-2017-06-26/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py:392) - MultiVolumeImportPlugin::examine<br>
[WARNING][Python] 28.06.2017 20:15:29 [Python] (C:\Program Files\Slicer 4.7.0-2017-06-26\bin\Python\slicer\<a href="http://util.py:812" rel="nofollow noopener">util.py:812</a>) - Warning: Plugin failed: MultiVolumeImporterPlugin</p>
<p>See python console for error message.<br>
[CRITICAL][Stream] 28.06.2017 20:15:29 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 28.06.2017 20:15:29 [] (unknown:0) -   File “C:\Program Files\Slicer 4.7.0-2017-06-26\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\<a href="http://DICOMWidgets.py" rel="nofollow noopener">DICOMWidgets.py</a>”, line 708, in getLoadablesFromFileLists<br>
[CRITICAL][Stream] 28.06.2017 20:15:29 [] (unknown:0) -     loadablesByPlugin[plugin] = plugin.examine(fileLists)<br>
[CRITICAL][Stream] 28.06.2017 20:15:29 [] (unknown:0) -   File “C:/Program Files/Slicer 4.7.0-2017-06-26/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 80, in examine<br>
[CRITICAL][Stream] 28.06.2017 20:15:29 [] (unknown:0) -     loadables += self.examineFiles(files)<br>
[CRITICAL][Stream] 28.06.2017 20:15:29 [] (unknown:0) -   File “C:/Program Files/Slicer 4.7.0-2017-06-26/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 430, in examineFiles<br>
[CRITICAL][Stream] 28.06.2017 20:15:29 [] (unknown:0) -     mvNodes = self.initMultiVolumes(subseriesLists[key])<br>
[CRITICAL][Stream] 28.06.2017 20:15:29 [] (unknown:0) -   File “C:/Program Files/Slicer 4.7.0-2017-06-26/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 726, in initMultiVolumes<br>
[CRITICAL][Stream] 28.06.2017 20:15:29 [] (unknown:0) -     mvNode.SetAttribute(‘MultiVolume.FrameFileList’, frameFileListStr)<br>
[CRITICAL][Stream] 28.06.2017 20:15:29 [] (unknown:0) - TypeError: SetAttribute argument 2: (unicode conversion error)<br>
[CRITICAL][Stream] 28.06.2017 20:15:29 [] (unknown:0) - Warning: Plugin failed: MultiVolumeImporterPlugin<br>
[CRITICAL][Stream] 28.06.2017 20:15:29 [] (unknown:0) -<br>
[CRITICAL][Stream] 28.06.2017 20:15:29 [] (unknown:0) - See python console for error message.<br>
[INFO][Stream] 28.06.2017 20:16:05 [] (unknown:0) - DICOM Plugin failed: SetAttribute argument 2: (unicode conversion error)</p>

---

## Post #8 by @vetyasin (2017-06-28 17:59 UTC)

<p>[DEBUG][Qt] 28.06.2017 20:10:28 [] (unknown:0) - Session start time …: 2017-06-28 20:10:28<br>
[DEBUG][Qt] 28.06.2017 20:10:28 [] (unknown:0) - Slicer version …: 4.7.0-2017-06-26 (revision 26137) win-amd64 - installed<br>
[DEBUG][Qt] 28.06.2017 20:10:29 [] (unknown:0) - Operating system …: Windows / Vista Professional / Service Pack 1 (Build 6001) - 64-bit<br>
[DEBUG][Qt] 28.06.2017 20:10:29 [] (unknown:0) - Memory …: 5814 MB physical, 11627 MB virtual<br>
[DEBUG][Qt] 28.06.2017 20:10:29 [] (unknown:0) - CPU …: GenuineIntel , 4 cores, 16 logical processors<br>
[DEBUG][Qt] 28.06.2017 20:10:29 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 28.06.2017 20:10:29 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 28.06.2017 20:10:29 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 28.06.2017 20:10:41 [Python] (C:\Program Files\Slicer 4.7.0-2017-06-26\lib\Slicer-4.7\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 28.06.2017 20:10:43 [Python] (C:\Program Files\Slicer 4.7.0-2017-06-26\lib\Slicer-4.7\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 28.06.2017 20:10:43 [Python] (C:\Program Files\Slicer 4.7.0-2017-06-26\lib\Slicer-4.7\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 28.06.2017 20:10:31 [] (unknown:0) - Number of registered modules: 135<br>
[DEBUG][Qt] 28.06.2017 20:10:35 [] (unknown:0) - Number of instantiated modules: 135<br>
[DEBUG][Qt] 28.06.2017 20:10:46 [] (unknown:0) - Number of loaded modules: 135<br>
[DEBUG][Qt] 28.06.2017 20:10:46 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 28.06.2017 20:10:54 [] (unknown:0) - Switch to module:  “DICOM”</p>

---

## Post #9 by @vetyasin (2017-06-28 18:02 UTC)

<p>Now I can import DICOM files, But I can not load.</p>

---

## Post #10 by @fedorov (2017-06-29 13:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Have you also tried to clean up your data by running DICOM Patcher?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/vetyasin">@vetyasin</a> this is the error: “TypeError: SetAttribute argument 2: (unicode conversion error)”</p>
<p>You need to run DICOM Patcher:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4586a04268befb6c0783d71f545bff75a01484fd.png" data-download-href="/uploads/short-url/9V3nA7srp1sKYzXbZMMn1MWe1VX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4586a04268befb6c0783d71f545bff75a01484fd_2_615x499.png" alt="image" data-base62-sha1="9V3nA7srp1sKYzXbZMMn1MWe1VX" width="615" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4586a04268befb6c0783d71f545bff75a01484fd_2_615x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4586a04268befb6c0783d71f545bff75a01484fd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4586a04268befb6c0783d71f545bff75a01484fd.png 2x" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">707×574 54.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @vetyasin (2017-06-30 08:09 UTC)

<p>Dear, Fedorov and Lasso;</p>
<p>I solved the problem as you suggested.<br>
Thank u so much for your interesting.<br>
Best,</p>

---

## Post #12 by @George_Kassis (2020-07-23 03:59 UTC)

<p><em>(translated using Google translate)</em></p>
<p>Hello excuse me, how do you run the Dicom patcher? because I can’t open .dcm files.</p>
<p>Thank you from now</p>
<details>
<summary>
Original language text</summary>
<p>Hola disculpa, como ejecutas el Dicom patcher? porque no puedo abrir los archivos .dcm.</p>
<p>DEsde ya gracias</p>
</details>

---

## Post #13 by @lassoan (2020-07-23 13:57 UTC)

<p>See documentation here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicompatcher.html">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicompatcher.html</a></p>

---
