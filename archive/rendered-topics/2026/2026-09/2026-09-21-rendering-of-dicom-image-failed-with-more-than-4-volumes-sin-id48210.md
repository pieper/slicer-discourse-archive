---
topic_id: 48210
title: "Rendering of DICOM image failed with more than 4 volumes since version 12"
date: 2026-09-21
url: https://discourse.slicer.org/t/48210
last_bumped: 2026-09-26T04:26:49.654Z
---

# Rendering of DICOM image failed with more than 4 volumes since version 12

**Topic ID**: 48210
**Date**: 2026-09-21
**URL**: https://discourse.slicer.org/t/rendering-of-dicom-image-failed-with-more-than-4-volumes-since-version-12/48210

---

## Post #1 by @mhouse (2026-09-21 13:58 UTC)

<p>Since version 12 (also with version 13) 3D Slicer crashes, because it cannot render an image with more than 4 volumes. At least with the version Slicer-5.11.0-2026-03-20-linux-amd64 it is working with 9 volumes, for e.g. a GE Multiphase volume.</p>
<blockquote>
<p>Slicer-5.12.4-linux-amd64$ ./Slicer<br>
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.<br>
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.</p>
<p>Switch to module:  “Welcome”<br>
Switch to module:  “DICOM”<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
Only 1 - 4 component scalars are supported by this mapper.The input data has 9 component(s).<br>
Only 1 - 4 component scalars are supported by this mapper.The input data has 9 component(s).<br>
Only 1 - 4 component scalars are supported by this mapper.The input data has 9 component(s).<br>
error: [/home/Slicer-5.12.4-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
</blockquote>

---

## Post #2 by @pieper (2026-09-21 14:07 UTC)

<p>Thanks for the report.  Are you able to share data to replicate the issue?</p>

---

## Post #3 by @mhouse (2026-09-21 14:17 UTC)

<p>Hello,</p>
<p>yes if it would help. Do you need the sequence or the log from version 11, if the log contains any information about the loading of the 9 volume sequence. So long I use the version 11, but the component display, either as RGBA or separate, is only available in further versions.</p>
<p>If you need the sequence then I need to remove the personal data. It’s my heart issue, it’s from the last Hi-Res CCTA.</p>
<p>Kindest regards</p>

---

## Post #4 by @fedorov (2026-09-21 14:31 UTC)

<p><a class="mention" href="/u/mhouse">@mhouse</a> you can check DICOM conformance of the files using the <code>dciodvfy</code> validator, which is available via this web page: <a href="https://imagingdatacommons.github.io/dicom3tools-web-distributions/">https://imagingdatacommons.github.io/dicom3tools-web-distributions/</a> and send back the output to help with debugging this issue.</p>
<p><em>If you send back the output, please look over it first to make sure no sensitive information is included!</em></p>
<p>That validation is done in the browser, and no files are uploaded anywhere. The source code is available here: <a href="https://github.com/ImagingDataCommons/dicom3tools-web-distributions">https://github.com/ImagingDataCommons/dicom3tools-web-distributions</a>.</p>

---

## Post #5 by @mhouse (2026-09-21 15:31 UTC)

<p>it will take some time, because the dataset is about 1,6Gb and consists of more than 8500 files. I have not done so much with the DICOM files in the past, I was just loading them into 3D Slicer.</p>
<p>I think after version 11 someone has limited the max. of data size. Therefore this error message. The messages before are maybe not related to this issue.</p>
<p>Only 1 - 4 component scalars are supported by this mapper.The input data has 9 component(s)</p>

---

## Post #6 by @pieper (2026-09-21 16:06 UTC)

<p><a class="mention" href="/u/mhouse">@mhouse</a> It would be great if you could share the data, but no pressure since it’s private.</p>
<p>There are several de-identification tools available. None of them are guaranteed to be 100% effective at removing all identifiers, but <a href="https://www.dclunie.com/pixelmed/software/webstart/DicomCleanerUsage.html">David Clunie’s DicomCleaner</a> is probably as good as you can find.</p>
<p>It would be good if you could confirm the behavior is the same after deidentification, since changing the tags may change how Slicer interprets the data.</p>
<p>Or if you decide not to share the data then the full logs from both versions of Slicer may be enough to help diagnose (maybe do that first if it’s easier).</p>

---

## Post #7 by @mhouse (2026-09-22 04:06 UTC)

<p>I don’t know how you want to get the logfiles, because I cannot attach them here directly. Please find the last lines of version 5.13 below.</p>
<p>I have only started the app and loaded the DICOM sequence from the DICOM database (w/o Advanced checked). After dragging the Multiphase sequence into the VR window 3D Slicer crashed with version 5.13. With version 5.11 it’s loading and displaying fine.</p>
<pre><code class="lang-auto">...

DICOMScalarVolumePlugin.py:441) - Loading with imageIOName: GDCM
[DEBUG][Python] 21.09.2026 19:33:56 [Python] (/home/m/install/Slicer-5.13.0-2026-08-05-linux-amd64/bin/../lib/Slicer-5.13/qt-scripted-modules/DICOMScalarVolumePlugin.py:563) - DICOM window/level (105.0/860.0) set to volume '315: Multiphase_7' from SOP instance 1.2.840.113619.2.416.8924333666940351969290340049978143130.1921.
[INFO][Python] 21.09.2026 19:33:57 [Python] (/home/m/install/Slicer-5.13.0-2026-08-05-linux-amd64/bin/../lib/Slicer-5.13/qt-scripted-modules/DICOMScalarVolumePlugin.py:441) - Loading with imageIOName: GDCM
[DEBUG][Python] 21.09.2026 19:34:04 [Python] (/home/m/install/Slicer-5.13.0-2026-08-05-linux-amd64/bin/../lib/Slicer-5.13/qt-scripted-modules/DICOMScalarVolumePlugin.py:563) - DICOM window/level (105.0/860.0) set to volume '315: Multiphase_8' from SOP instance 1.2.840.113619.2.416.7813687437206210351250794399055596848.2177.
[DEBUG][Qt] 21.09.2026 19:34:42 [] (unknown:0) - Switch to module:  "Data"
[ERROR][VTK] 21.09.2026 19:35:15 [vtkOpenGLGPUVolumeRayCastMapper (0x46a56d50)] (vtkGPUVolumeRayCastMapper.cxx:424) - Only 1 - 4 component scalars are supported by this mapper.The input data has 9 component(s).
</code></pre>

---

## Post #8 by @mhouse (2026-09-22 04:14 UTC)

<p>with version 5.11 it looks similar in the logfile before the crash.</p>
<pre><code class="lang-auto">...

[INFO][Python] 22.09.2026 05:22:48 [Python] (/home/m/install/Slicer-5.11.0-2025-11-19-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM
[DEBUG][Python] 22.09.2026 05:22:53 [Python] (/home/m/install/Slicer-5.11.0-2025-11-19-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:567) - DICOM window/level (105.0/860.0) set to volume '315: Multiphase_7' from SOP instance 1.2.840.113619.2.416.8924333666940351969290340049978143130.1921.
[INFO][Python] 22.09.2026 05:22:53 [Python] (/home/m/install/Slicer-5.11.0-2025-11-19-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM
[DEBUG][Python] 22.09.2026 05:22:59 [Python] (/home/m/install/Slicer-5.11.0-2025-11-19-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:567) - DICOM window/level (105.0/860.0) set to volume '315: Multiphase_8' from SOP instance 1.2.840.113619.2.416.7813687437206210351250794399055596848.2177.
[DEBUG][Qt] 22.09.2026 05:34:20 [] (unknown:0) - Switch to module:  ""
</code></pre>

---

## Post #9 by @pieper (2026-09-22 15:18 UTC)

<p>This could be due to any number of packages that changed subtly between versions (could be dcmtk, VTK, or something in Slicer itself).  If you can’t find a way to share data that we can use to reproduce we may just need to wait until someone else runs into the same issue.</p>
<p>One thing to try is advanced mode in the DICOM module and pick a different plugin (Sequence vs MultiVolume), but that’s just a guess.</p>

---

## Post #10 by @mhouse (2026-09-22 16:00 UTC)

<p>I have already tried the advanced mode. But at least with version 5.13 I cannot select another Reader than MultiVolume. In the settings I have already selected the Sequence reader in the DICOM section. The other displayed entries in the Advanced view, I have already tried which have crashed as well.</p>
<p>You could send me an email to whom I can provide an one time link, or you can provide me a link for an upload after I have removed some data.</p>
<p>btw. If I export the sequence to a file and then add this file “Sequence” is pre selected and I can drag it into the VR view and play the sequence without a crash so far.</p>
<p>Anyway this app is a great tool, because so far professional radiologists could not find any issue. But you can easily see that the RSAR has detached and destroyed the aortic root.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15d518bc2111e6755721e54c57b17790332b338d.jpeg" data-download-href="/uploads/short-url/378AdZ7fDsOIhEdrcQpK3HgbLs1.jpeg?dl=1" title="Aorta-root-RSAR-MPh-s5-ct26j-f5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15d518bc2111e6755721e54c57b17790332b338d_2_690x433.jpeg" alt="Aorta-root-RSAR-MPh-s5-ct26j-f5" data-base62-sha1="378AdZ7fDsOIhEdrcQpK3HgbLs1" width="690" height="433" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15d518bc2111e6755721e54c57b17790332b338d_2_690x433.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15d518bc2111e6755721e54c57b17790332b338d_2_1035x649.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15d518bc2111e6755721e54c57b17790332b338d_2_1380x866.jpeg 2x" data-dominant-color="694D41"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Aorta-root-RSAR-MPh-s5-ct26j-f5</span><span class="informations">1920×1206 625 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b7cd581a87762664b9a079f44b83836aeb40de5.jpeg" data-download-href="/uploads/short-url/mbvsJTnK2WadBIGYSzPwuTL1lcx.jpeg?dl=1" title="Aorta-root-RSAR-MPh-s4-ct26j-f4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b7cd581a87762664b9a079f44b83836aeb40de5_2_690x433.jpeg" alt="Aorta-root-RSAR-MPh-s4-ct26j-f4" data-base62-sha1="mbvsJTnK2WadBIGYSzPwuTL1lcx" width="690" height="433" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b7cd581a87762664b9a079f44b83836aeb40de5_2_690x433.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b7cd581a87762664b9a079f44b83836aeb40de5_2_1035x649.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b7cd581a87762664b9a079f44b83836aeb40de5_2_1380x866.jpeg 2x" data-dominant-color="664A3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Aorta-root-RSAR-MPh-s4-ct26j-f4</span><span class="informations">1920×1206 630 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @pieper (2026-09-22 17:11 UTC)

<p>My email is <a href="mailto:pieper@isomics.com">pieper@isomics.com</a></p>

---

## Post #12 by @mikebind (2026-09-22 19:35 UTC)

<aside class="quote no-group" data-username="mhouse" data-post="10" data-topic="48210">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar"> mhouse:</div>
<blockquote>
<p>Anyway this app is a great tool</p>
</blockquote>
</aside>
<p>No argument there, Slicer is great!</p>
<aside class="quote no-group" data-username="mhouse" data-post="10" data-topic="48210">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar"> mhouse:</div>
<blockquote>
<p>you can easily see that the RSAR has detached and destroyed the aortic root</p>
</blockquote>
</aside>
<p>When interpreting these images, it’s important to be aware of some of the issues that can arise from the CT image formation process.  In particular, it’s important to understand how the presence of localized high-density objects, like metal, can cause nearby shadows in CT images. Ordinarily, dark voxels in a CT image would indicate something low-density there, like air or a gap, but adjacent to metal, those dark voxels may just be an incorrect artifact of the CT image reconstruction process.  In 3D reconstructions like the volume renderings you show (which look great, by the way!), what Slicer shows is based only on the voxel values, so if those voxel values are distorted by metal artifacts, the volumetric 3D view can show features which may not be present in your actual heart.</p>
<p>I am not a doctor and am not trying to argue that the imaging demonstrates that everything is fine, and it is certainly possible for your doctors to be wrong. Part of the professional training for radiologists is to understand how various medical imaging artifacts arise, what causes them, and how to try to understand what an image indicates about the true state of the imaged tissue is, even when artifacts are present. If you are trying to understand this imaging on your own, I would recommend learning about CT artifacts in general, and specifically about how metal artifacts arise and how they appear in images. Metal artifact reduction is a difficult problem and has been an area of active research for many years. Some form of metal artifact reduction may have already been used in your imaging. Some additional knowledge may help you evaluate whether this imaging:</p>
<ul>
<li>actually does show evidence of a detached or damaged aortic root,</li>
<li>is actually consistent with a fully successful procedure,</li>
<li>or is actually inconclusive one way or another because essential areas are not clearly visualized due to metal artifacts</li>
</ul>
<p>Anyway, I hope you can sort out the technical image loading problems, and I wish you the very best.</p>
<p>Since it sounds like you likely just have this one set of images that you are interested in, a workaround which would allow you to get your data into Slicer 5.13 would be to load it into 5.11, then save the successfully loaded sequence to a .seq.nrrd file.  That sequence file should load just fine into 5.13. Note that because of the way Slicer handles sequences, where there is a sequence node in the background which has all the image frames and a proxy node in the foreground which holds just the current image frame, when you save the scene, the saved proxy node will generally have a very similar file name to the full sequence node, usually differing only by the file extension. The proxy node will have extension .nrrd, while the full sequence will have extension .seq.nrrd (and be a much larger file).  Just make sure that it’s the .seq.nrrd file that you load into 5.13.  When you load a sequence, a new proxy node is automatically created in the scene, so you don’t need to load the proxy node into 5.13.  If you try this approach and run into problems, let me know and I can try to be a little clearer; I know this description may be a bit scattered.</p>

---

## Post #13 by @mhouse (2026-09-22 23:34 UTC)

<p>Many thanks for your reply. Yes metal is always a bit tricky to handle. I have already 5 CTA (within 6 years), so I can see the progress. I was more searching the source of the strange filling of the right ventricle and the right atrium, because both structures are now bigger than the left side. It’s easy to say from the radiologists that this is coming from the problems of the left side, but always it’s good to look closer.</p>
<p>Already in the uploaded pictures you can see the jet from the aortic root into the right ventricle, which is unlikely caused by the metal artifacts or motion artifacts. This CCTA was ECG triggered with nitro application before.</p>
<p>In the echo you can see jets from all valves except the aortic valve. But die cut is above at the sinus. Also the right sinus is ruptured.</p>
<p>In another rendered picture you can see from “outside” that die ring has disrupted and you see the former loop of the fixation thread. It’s much clearer to see if you play the sequence.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2743ec1a2900870648fe6c716a5c0290400efdde.jpeg" data-download-href="/uploads/short-url/5Bm8W6GRhQF0xUukxRrof3us4ii.jpeg?dl=1" title="Aorta-root-RSAR-s2-ct26j-d3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/2743ec1a2900870648fe6c716a5c0290400efdde_2_610x499.jpeg" alt="Aorta-root-RSAR-s2-ct26j-d3" data-base62-sha1="5Bm8W6GRhQF0xUukxRrof3us4ii" width="610" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/2743ec1a2900870648fe6c716a5c0290400efdde_2_610x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/2743ec1a2900870648fe6c716a5c0290400efdde_2_915x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/2743ec1a2900870648fe6c716a5c0290400efdde_2_1220x998.jpeg 2x" data-dominant-color="52403D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Aorta-root-RSAR-s2-ct26j-d3</span><span class="informations">1816×1488 455 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/565dda12375324981bdcfade5d495f5338f9a451.jpeg" data-download-href="/uploads/short-url/ck28CHi3xULYFdOk9EWSYq7hyh3.jpeg?dl=1" title="Aorta-root-RSAR-s2-ct26j-d4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/565dda12375324981bdcfade5d495f5338f9a451_2_610x499.jpeg" alt="Aorta-root-RSAR-s2-ct26j-d4" data-base62-sha1="ck28CHi3xULYFdOk9EWSYq7hyh3" width="610" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/565dda12375324981bdcfade5d495f5338f9a451_2_610x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/565dda12375324981bdcfade5d495f5338f9a451_2_915x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/565dda12375324981bdcfade5d495f5338f9a451_2_1220x998.jpeg 2x" data-dominant-color="604C4B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Aorta-root-RSAR-s2-ct26j-d4</span><span class="informations">1816×1488 464 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @mikebind (2026-09-23 17:28 UTC)

<p>Yes, having the temporal sequence can really help our eyes see around the artifact (especially in the image slices for me; I find it harder in the volume renderings). It’s also really great that you have images from another modality (echo) to cross reference findings with.</p>
<p>I’m not familiar with this cardiac procedure or adult hearts at all (I work at a children’s hospital and have some minor familiarity with pediatric cardiac imaging, especially for congenital procedures), so I don’t want to offer any opinion on your specific case.  While I love that Slicer can enable people to explore their own medical images, I am sometimes concerned that beginners can also misinterpret those images, so that is where my cautions were coming from above.  Everyone from complete novices to experienced experts show up on this forum, so I didn’t know where you were on that spectrum.  Best wishes deepening your understanding of what is going on in your heart!</p>

---

## Post #15 by @mhouse (2026-09-25 14:51 UTC)

<p>Many thanks for your reply. I have already sent the link to Steve. First I have cut it from axial, because of the high native resolution of this plane. I have detected the crash with the Multiphase sequence during I was also using the components setting for the temporal systolic sequence in version 5.13. Because with this you can see the motion in one picture. The biggest impact to the aortic root is if the left atrium squeezes out the remaining part into the left ventricle and then the left ventricle is contracting. Unfortunately the LVEF is still above 75%.</p>
<p>Normally the ring should not break through the annulus. Of course it’s also visible in the normal slice views, what the radiologists normally use, but as written before no issues, the ring is positioned in “loco typico” …</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/860f1696bc482b495f1c126f110fbb98ed38c4ca.jpeg" data-download-href="/uploads/short-url/j7Wj3NyZ2ZVpaomlXljOCfRDFqy.jpeg?dl=1" title="Aorta-root-RSAR-Sys-ct26j-l15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/860f1696bc482b495f1c126f110fbb98ed38c4ca_2_690x488.jpeg" alt="Aorta-root-RSAR-Sys-ct26j-l15" data-base62-sha1="j7Wj3NyZ2ZVpaomlXljOCfRDFqy" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/860f1696bc482b495f1c126f110fbb98ed38c4ca_2_690x488.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/860f1696bc482b495f1c126f110fbb98ed38c4ca_2_1035x732.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/860f1696bc482b495f1c126f110fbb98ed38c4ca_2_1380x976.jpeg 2x" data-dominant-color="474644"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Aorta-root-RSAR-Sys-ct26j-l15</span><span class="informations">1920×1358 415 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cbe7ab8cee3abbedddcb397663c0a7c6db9b6e8.jpeg" data-download-href="/uploads/short-url/hNxj0iMN6Dm1bTy0CpIJuSrljT2.jpeg?dl=1" title="Aorta-root-RSAR-Sys-ct26j-l18" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7cbe7ab8cee3abbedddcb397663c0a7c6db9b6e8_2_690x488.jpeg" alt="Aorta-root-RSAR-Sys-ct26j-l18" data-base62-sha1="hNxj0iMN6Dm1bTy0CpIJuSrljT2" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7cbe7ab8cee3abbedddcb397663c0a7c6db9b6e8_2_690x488.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7cbe7ab8cee3abbedddcb397663c0a7c6db9b6e8_2_1035x732.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7cbe7ab8cee3abbedddcb397663c0a7c6db9b6e8_2_1380x976.jpeg 2x" data-dominant-color="474644"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Aorta-root-RSAR-Sys-ct26j-l18</span><span class="informations">1920×1358 417 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @lassoan (2026-09-25 17:46 UTC)

<p>4D CT loading had a regression due to a recent merging of DICOM plugins from an extension to Slicer core. A fix has been integrated. Slicer Preview Releases that you download today or later will work well.</p>
<p>I’ve also submitted an <a href="https://github.com/Slicer/Slicer/pull/9414">enhancement to CTK and Slicer that will make DICOM examine+loading about 5-10x faster</a>. With this improvement, a 4D cardiac CT with 20 time points and 512x512 slice size is loaded in 20-30 seconds instead of several minutes. It will be available in preview releases by early next week.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> if you have a chance to review these CTK and Slicer changes sooner than Monday then it could be integrated earlier.</p>

---

## Post #17 by @mhouse (2026-09-26 04:26 UTC)

<p>Many thanks, it’s loading now fine.</p>

---
