---
topic_id: 23645
title: "Export Scene As Dicom"
date: 2022-05-30
url: https://discourse.slicer.org/t/23645
---

# Export scene as dicom

**Topic ID**: 23645
**Date**: 2022-05-30
**URL**: https://discourse.slicer.org/t/export-scene-as-dicom/23645

---

## Post #1 by @Pheasant (2022-05-30 15:34 UTC)

<p>Hi,</p>
<p>I am a bit new at using the Dicom export function and currently it gives the error:</p>
<p>Traceback (most recent call last):<br>
File “”, line 2, in <br>
TypeError: <strong>init</strong>() missing 1 required positional argument: ‘referenceFile’</p>
<p>When I try to export the scene into Dicom. I am aware that in this case it can only be opened with slicer but that is the point. I checked from the code of the export function that it should take the first file from the dicom database as the reference or you can specify a reference file but I do not see such option as the export scene freezes all options to begin with.</p>
<p>How do I solve this?</p>

---

## Post #2 by @pieper (2022-05-30 19:06 UTC)

<p>Thanks for reporting.  Yes, it looks like <a href="https://github.com/Slicer/Slicer/commit/b89b3c8a4b2a209ba3654377ee3050da62a14877">this refactoring</a> led to an argument mismatch between the dialog code and the python class.  You could try going back to an earlier version of Slicer and it might work.  <a class="mention" href="/u/lassoan">@lassoan</a> or <a class="mention" href="/u/cpinter">@cpinter</a> have you tried this feature lately?</p>
<p><a class="mention" href="/u/pheasant">@Pheasant</a> you can call the exporter from Python with the needed argument - as you say it just needs to be a file from the study you want to export into.</p>

---

## Post #3 by @lassoan (2022-05-30 20:42 UTC)

<p>We refactored the scene bundle export to use the export plugin infrastructure (using the first file in the DICOM database as a basis of the bundle just seemed very arbitrary). However, we forgot to remove the option from the top (and nobody reported it that it was broken until now).</p>
<p>You can choose <code>Slicer data bundle</code> export type to export a scene in a DICOM file:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2b39e26af6a08b88169a3af78e23500d05f728b.png" data-download-href="/uploads/short-url/u3X657YHxUsLB1t83zouFKo226v.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2b39e26af6a08b88169a3af78e23500d05f728b_2_648x500.png" alt="image" data-base62-sha1="u3X657YHxUsLB1t83zouFKo226v" width="648" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2b39e26af6a08b88169a3af78e23500d05f728b_2_648x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2b39e26af6a08b88169a3af78e23500d05f728b_2_972x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2b39e26af6a08b88169a3af78e23500d05f728b_2_1296x1000.png 2x" data-dominant-color="3F4142"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1423×1097 53.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The item that you right-click on will be used as a basis for the DICOM file, so if you don’t have anything loaded from DICOM then you first need to export something (e.g., a volume node) to DICOM and then load it into the scene. It is definitely not nice or convenient, there was just not a lot of interest in this feature to make it polished and easily usable for many workflows.</p>
<p><a class="mention" href="/u/pheasant">@Pheasant</a> can you tell a bit about your workflow? How do you plan to use these scene bundle DICOM files?</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/cpinter">@cpinter</a> what do you think about removing the <code>Export entire scene</code> option from the top of the DICOM export dialog and just use export type selector instead?</p>

---

## Post #4 by @pieper (2022-05-30 20:57 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>Yes, I think coming up with something cleaner makes sense.  Since the scene may not include anything loaded via dicom, it could be nice to be able to pick an instance to use as the source of metadata for the export, so that the exported scene gets associated with the desired study.</p>
<p>I’d also be curious to hear from <a class="mention" href="/u/pheasant">@Pheasant</a> how you might use this and how it works in actual practice.</p>

---

## Post #5 by @Pheasant (2022-05-31 05:14 UTC)

<p>Hi, thank you for the excellent response.</p>
<p>The main purpose of the DICOM export is storage. The place where we store data accepts only DICOM-format. The point would be to be able to store old works in a way that doesn’t require them to be saved locally. The workflow is something that is repeated regularly and the main use for Slicer is jumping from one mark up point to other to see specific parts of the brain. The scene has multiple markups in it.</p>
<p>I tried the save data bundle option but got a different error from it (I removed the paths and replaced them with * for this post):</p>
<p>Saving Image…</p>
<p>Saving scene into MRB…</p>
<p>Making dicom reference file…</p>
<p>Using reference file reference_file.dcm</p>
<p>Failed to export using plugin DICOMSlicerDataBundlePluginClass</p>
<p>Traceback (most recent call last):</p>
<p>File “”, line 3, in </p>
<p>File “*/DICOMSlicerDataBundlePlugin.py”, line 226, in export</p>
<pre><code>exporter.export()
</code></pre>
<p>File “*\DICOMExportScene.py”, line 58, in export</p>
<pre><code>success = self.createDICOMFileForScene()
</code></pre>
<p>File “*\DICOMExportScene.py”, line 119, in createDICOMFileForScene</p>
<pre><code>dump = str(dumpByteArray.data(), encoding='utf-8')
</code></pre>
<p>UnicodeDecodeError: ‘utf-8’ codec can’t decode byte 0xc4 in position 3173: invalid continuation byte</p>
<p>Should I try a different encoder? If so what would work in your opinion?</p>

---

## Post #6 by @cpinter (2022-05-31 08:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="23645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>removing the <code>Export entire scene</code> option from the top of the DICOM export dialog and just use export type selector instead?</p>
</blockquote>
</aside>
<p>Agreed, this seems like an oversight. And one option fewer to handle for the user and for us.</p>
<aside class="quote no-group" data-username="Pheasant" data-post="5" data-topic="23645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pheasant/48/15560_2.png" class="avatar"> Pheasant:</div>
<blockquote>
<p>I tried the save data bundle option but got a different error from it</p>
</blockquote>
</aside>
<p>I just tried the data bundle export using 5.0.2 on Windows and it worked for me. What Slicer version and OS do you use?</p>

---

## Post #7 by @Pheasant (2022-06-01 05:20 UTC)

<p>I use 5.0.2 on Windows 10.</p>
<p>I did some tests on it and I didn’t get an error from selecting export scalar volume for the reference Dicom file. Then I loaded the exported file and used that as the reference for the Export as data bundle and it seems to work like that.  I guess exporting it as scalar volume made the dicom file readable for it?</p>
<p>I think the reason might be that there are some characters (for example ä or ö) in the original Dicom file, I tried removing the ones that I noticed but it didn’t help though.</p>
<p>I am curious however about the reason for that exporting the scalar volume works well but not the data bundle one.</p>

---

## Post #8 by @pieper (2022-06-01 13:42 UTC)

<p><a class="mention" href="/u/pheasant">@Pheasant</a> If it’s possible for you to create an mrb (no patient data) that fails to export to dicom for you then it could be tested on different machines for debugging.</p>

---

## Post #9 by @Pheasant (2022-06-03 05:38 UTC)

<p>That should be possible (I have some files from my own MRI so there shouldn’t be a problem).</p>
<p>I am a bit busy currently and I would like to anonymize them a bit so I can send them around tuesday. Where should I send it?</p>

---

## Post #10 by @pieper (2022-06-03 12:44 UTC)

<p>As long as you are comfortable, sharing your own MRI is fine.  You can put them in a service like dropbox, google drive, etc.  Share a link by direct message if you’d rather not make them public.</p>

---

## Post #11 by @Pheasant (2022-11-22 09:20 UTC)

<p>Hi,</p>
<p>In the newest version when I try to import the scene to dicom. It only imports a screenshot of the dicom-module as seen on the linked picture i.e. that is the imported Dicom file.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba605ddeacc865d6462492b6a8fe7c38cf86e762.jpeg" data-download-href="/uploads/short-url/qALgZSgb9gC3o3qo6vizZHBxJt0.jpeg?dl=1" title="f54fd38d65004551199e3f27746d9b87" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba605ddeacc865d6462492b6a8fe7c38cf86e762_2_690x369.jpeg" alt="f54fd38d65004551199e3f27746d9b87" data-base62-sha1="qALgZSgb9gC3o3qo6vizZHBxJt0" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba605ddeacc865d6462492b6a8fe7c38cf86e762_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba605ddeacc865d6462492b6a8fe7c38cf86e762_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba605ddeacc865d6462492b6a8fe7c38cf86e762_2_1380x738.jpeg 2x" data-dominant-color="252525"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">f54fd38d65004551199e3f27746d9b87</span><span class="informations">1920×1027 55.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @lassoan (2022-11-25 06:24 UTC)

<p>You can un-toggle the “Show DICOM database” button to see the viewers instead of the DICOM database.</p>

---

## Post #13 by @Pheasant (2022-11-25 08:25 UTC)

<p>Thanks for the answer but the point would be to save the entire package as a dicom file i.e. so that the dicom file could be loaded and contain all the volumes and mark up points</p>

---

## Post #14 by @lassoan (2022-11-25 18:41 UTC)

<p>This works well in the very latest Slicer Preview Releases.</p>

---

## Post #15 by @Pheasant (2022-12-13 06:18 UTC)

<p>Hi, I can’t seem to be able to get it to work in the lates preview release. So could you give me some instructions on how it works. It seems that the dicom module doesn’t even show any of the volumes loaded in.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed913828471dc7c47e882e5a6cf1adc37b5f6ad8.png" data-download-href="/uploads/short-url/xTCi4IyOXScTYkEsjjtsQAIBm9W.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed913828471dc7c47e882e5a6cf1adc37b5f6ad8_2_290x499.png" alt="image" data-base62-sha1="xTCi4IyOXScTYkEsjjtsQAIBm9W" width="290" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed913828471dc7c47e882e5a6cf1adc37b5f6ad8_2_290x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed913828471dc7c47e882e5a6cf1adc37b5f6ad8_2_435x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed913828471dc7c47e882e5a6cf1adc37b5f6ad8.png 2x" data-dominant-color="202020"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">494×849 4.48 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #16 by @pieper (2022-12-13 13:11 UTC)

<p>I can confirm that exporting the scene to dicom and reloading works for me in the 5.2.1 release on Mac.</p>
<p>Steps are to right click in the Data module and pick Export to DICOM. In the dialog pick the data you want and select scene export and click the Export button.  Data is then in database and can be reloaded.</p>

---

## Post #17 by @Pheasant (2022-12-13 16:00 UTC)

<p>Hi, Thank you I got it to work now.</p>
<p>However I noticed that I had to load the exported dicom series as a patient into the dicom database.</p>
<p>If I only dragged the created dicom file from the folders it ended up with the same problem as mentioned before as in it was just a screen shot. Even though the filesize would indicate it would be correct.</p>
<p>But it does work if you drag the main folder into slicer. But it would be great to know why just using the dicom file gives such a strange result.</p>

---

## Post #18 by @pieper (2022-12-13 19:01 UTC)

<p>Oh, I see what you are doing.  Right, if you drag and drop the exported dicom Slicer will try to read it as a single frame secondary capture, because that’s what it technically “is”.  The “data bundle” concept puts a zip file of the data from your scene into a private tag of the dicom header.  We do this so that you can use conventional PACS or other dicom infrastructure to exchange data with other Slicer users.</p>
<p>This private tag is detected when you load the data in Slicer through the dicom module and the scene is unpacked and loaded.  So if you want to drag-and-drop the file, you need to enter the DICOM module first so the file gets added to the database.</p>

---

## Post #19 by @Pheasant (2022-12-19 11:51 UTC)

<p>Thank you for the explanation. That makes sense then.</p>

---
