# Position of the 3D image and its cross section do not match

**Topic ID**: 39775
**Date**: 2024-10-21
**URL**: https://discourse.slicer.org/t/position-of-the-3d-image-and-its-cross-section-do-not-match/39775

---

## Post #1 by @Haru (2024-10-21 13:50 UTC)

<p>Nice to meet you.<br>
I am a student and my English is not good. Please forgive me.<br>
I have imported an X-ray CT image into 3Dslicer in DICOM file format and displayed it.<br>
I have imported 799 images sliced in the x-axis direction, 1024 images sliced in the y-axis direction, and 1024 images sliced in the z-axis direction.<br>
However, the position of the 3D image and its cross section did not match. The plane shown at the bottom of the 3D image in the attached image is the red cross section.<br>
I would like to be able to see where in the 3D image the cross-sectional view is located.<br>
I would appreciate it if you could enlighten me.</p>
<p>Operating system:windows<br>
Slicer version:5.6.2<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @pieper (2024-10-21 15:03 UTC)

<p>Can you add some screenshots to illustrate what you are seeing?</p>

---

## Post #3 by @Haru (2024-10-22 00:47 UTC)

<p>Thank you for your reply.<br>
I think I have uploaded the attached photo. I hope you can see them.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b480e8b6189d88137c0cb5c410bc34e9ac484687.png" data-download-href="/uploads/short-url/pKO87z9u8kKWz54vdHMWXLer6TR.png?dl=1" title="スクリーンショット 2024-10-21 112725" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b480e8b6189d88137c0cb5c410bc34e9ac484687_2_690x463.png" alt="スクリーンショット 2024-10-21 112725" data-base62-sha1="pKO87z9u8kKWz54vdHMWXLer6TR" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b480e8b6189d88137c0cb5c410bc34e9ac484687_2_690x463.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b480e8b6189d88137c0cb5c410bc34e9ac484687_2_1035x694.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b480e8b6189d88137c0cb5c410bc34e9ac484687.png 2x" data-dominant-color="BABAC0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2024-10-21 112725</span><span class="informations">1364×917 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2024-10-22 10:33 UTC)

<p>Is it possible that there is a deformable transformation on the volume? Look for this icon in the transform column in the row of your volume in the Data module.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6df17c13bae52bcc32e1534658f1b2282c55aac5.png" alt="DeformableTransform" data-base62-sha1="fGBqdhLs7WAaZ78wc1X9XwAUBuJ" width="21" height="21"></p>
<p>If you have this, then you can fix the display discrepancy by right-clicking and choosing the Harden transform option.</p>

---

## Post #5 by @Haru (2024-10-23 04:53 UTC)

<p>Thank you for your reply.<br>
I was able to find the icon, but what should I do next?<br>
We apologize for the inconvenience, but please let us know. Thank you very much.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a076b20198bc6678f346dd7ddb10a85d8397e9b.jpeg" data-download-href="/uploads/short-url/ayTe3LMwbLKmI8cwLBpQIAqQFej.jpeg?dl=1" title="スクリーンショット 2024-10-23 135036" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a076b20198bc6678f346dd7ddb10a85d8397e9b_2_690x468.jpeg" alt="スクリーンショット 2024-10-23 135036" data-base62-sha1="ayTe3LMwbLKmI8cwLBpQIAqQFej" width="690" height="468" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a076b20198bc6678f346dd7ddb10a85d8397e9b_2_690x468.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a076b20198bc6678f346dd7ddb10a85d8397e9b_2_1035x702.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a076b20198bc6678f346dd7ddb10a85d8397e9b.jpeg 2x" data-dominant-color="BEBDC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2024-10-23 135036</span><span class="informations">1303×885 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @cpinter (2024-10-23 10:28 UTC)

<p>I cannot interpret what is in the screenshot. Please read my comment again with attention.</p>
<p>“Look for this icon in the <strong>transform column</strong> in the row of your volume <strong>in the Data module</strong>.”</p>

---

## Post #7 by @Haru (2024-10-26 03:27 UTC)

<p>I am terribly sorry.<br>
I looked at the transform column in the data module and the Harden transform is grayed out and cannot be selected. I was only able to select create new transform and the currently selected none. So I selected create new transform and again selected the Harden transform in the same transform column, and the discrepancy between the 3D image and the slice plane seemed to be resolved.<br>
However, the image displayed on the slice plane in red does not appear to match the projected view imagined from the 3d image.<br>
I would like to rotate the slice plane 180°.<br>
I tried to rotate only the slice plane from both the transform module and the reformat module, but could not do so.<br>
What should I do?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d51a7f931ac83cb34ed3571167b64022b2b17808.jpeg" data-download-href="/uploads/short-url/upctmEcn16JzD3HDur2CZcHJkjm.jpeg?dl=1" title="スクリーンショット 2024-10-26 122425" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d51a7f931ac83cb34ed3571167b64022b2b17808_2_690x379.jpeg" alt="スクリーンショット 2024-10-26 122425" data-base62-sha1="upctmEcn16JzD3HDur2CZcHJkjm" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d51a7f931ac83cb34ed3571167b64022b2b17808_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d51a7f931ac83cb34ed3571167b64022b2b17808_2_1035x568.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d51a7f931ac83cb34ed3571167b64022b2b17808.jpeg 2x" data-dominant-color="C4C4DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2024-10-26 122425</span><span class="informations">1338×736 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bc7c00fdf87ec534712c70c097c5d04396279fc.jpeg" data-download-href="/uploads/short-url/8wQ8hQTt1UodSHPoM4zf7XQntla.jpeg?dl=1" title="スクリーンショット 2024-10-26 122316" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bc7c00fdf87ec534712c70c097c5d04396279fc_2_690x382.jpeg" alt="スクリーンショット 2024-10-26 122316" data-base62-sha1="8wQ8hQTt1UodSHPoM4zf7XQntla" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bc7c00fdf87ec534712c70c097c5d04396279fc_2_690x382.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bc7c00fdf87ec534712c70c097c5d04396279fc_2_1035x573.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bc7c00fdf87ec534712c70c097c5d04396279fc.jpeg 2x" data-dominant-color="C4C4DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2024-10-26 122316</span><span class="informations">1329×737 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @cpinter (2024-10-27 13:40 UTC)

<aside class="quote no-group" data-username="Haru" data-post="7" data-topic="39775">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ecc23a/48.png" class="avatar"> Haru:</div>
<blockquote>
<p>I looked at the transform column in the data module and the Harden transform is grayed out and cannot be selected. I was only able to select create new transform and the currently selected none. So I selected create new transform and again selected the Harden transform in the same transform column, and the discrepancy between the 3D image and the slice plane seemed to be resolved.</p>
</blockquote>
</aside>
<p>This seems odd. If there is no transform, then it should be impossible that you add a new identity transform, harden it, and the problem is fixed, as this should have no effect. Unfortunately the screenshots do not help, as you do not include the Data module, nor describe what the data contains exactly when you first load it, or in what format the data arrives.</p>
<p>Please either record a full video or send your data.</p>

---

## Post #9 by @lassoan (2024-10-27 17:05 UTC)

<p>Yes, please include a screnshot of the Data module, because we don’t know what you have in your scene. If you want to get an answer real quick then you can save your scene as .mrb file and share it with us (upload to somewhere - dropbox, onedrive, google drive, etc. - and post the link here).</p>

---

## Post #10 by @Haru (2024-10-28 08:06 UTC)

<p>Thank you for your instruction.<br>
I uploaded the data  to google drive.<br>
I hope you can see it.</p>
<p><a href="https://drive.google.com/drive/folders/1cpat7qv5KmETEsRaQEY-1Vc7Ovlnokhb?usp=drive_link" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1cpat7qv5KmETEsRaQEY-1Vc7Ovlnokhb?usp=drive_link</a><br>
<a href="https://drive.google.com/drive/folders/1Jw5aXNv5KRg5KB-Wu8DA_MVH0BsynjPr?usp=drive_link" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1Jw5aXNv5KRg5KB-Wu8DA_MVH0BsynjPr?usp=drive_link</a><br>
<a href="https://drive.google.com/drive/folders/1IO9P3Ts4vwJIBaLARpv9HRIXsQEV4nL_?usp=drive_link" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1IO9P3Ts4vwJIBaLARpv9HRIXsQEV4nL_?usp=drive_link</a></p>
<p>The data was taken with Microfocus X-ray Computed Tomography and was originally analyzed with a special software called MyVGL. I converted it to a DICOM file with that dedicated software. This picture shows the coordinate axes of the original data.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f59ff04a1e03b8b620c7fbe822516326c9bb2a9b.jpeg" data-download-href="/uploads/short-url/z2TE7P25S2v16FmmVjJKCOlb4lZ.jpeg?dl=1" title="W2-1_Dir1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f59ff04a1e03b8b620c7fbe822516326c9bb2a9b_2_690x384.jpeg" alt="W2-1_Dir1" data-base62-sha1="z2TE7P25S2v16FmmVjJKCOlb4lZ" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f59ff04a1e03b8b620c7fbe822516326c9bb2a9b_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f59ff04a1e03b8b620c7fbe822516326c9bb2a9b_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f59ff04a1e03b8b620c7fbe822516326c9bb2a9b_2_1380x768.jpeg 2x" data-dominant-color="242424"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">W2-1_Dir1</span><span class="informations">1920×1069 79.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The upper left portion shown in this picture was saved as XY. This is the coordinate axis written in the corner of the upper left part.<br>
The YZ and ZX axes were saved in the same way. Then everything was imported into 3D Slicer and worked on.</p>
<p>I apologize for the inconvenience, but if there is anything I am missing or incomplete, I would appreciate it if you could let me know.</p>

---

## Post #11 by @Haru (2024-10-28 08:08 UTC)

<p>Here is the mrb file.<br>
I am very sorry, but this is the first time I saved it, so I am not sure if I did it right.<br>
Thank you very much in advance.</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1bM11-tDQ9TmEa6dn_qC22Nr3tgjp8cpK/view?usp=drive_link">
  <header class="source">

      <a href="https://drive.google.com/file/d/1bM11-tDQ9TmEa6dn_qC22Nr3tgjp8cpK/view?usp=drive_link" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1bM11-tDQ9TmEa6dn_qC22Nr3tgjp8cpK/view?usp=drive_link" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1bM11-tDQ9TmEa6dn_qC22Nr3tgjp8cpK/view?usp=drive_link" target="_blank" rel="noopener nofollow ugc">2024-10-28-Scene.mrb</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #12 by @cpinter (2024-10-28 11:31 UTC)

<p>I think this scene was saved after the “fix” with the hardening. Just for the others to know, because that would not help in diagnosing the problem.<br>
Looking at the input data…</p>

---

## Post #13 by @cpinter (2024-10-28 11:44 UTC)

<p>I loaded the data and everything seems to work well:<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f993ff20333a1988ac11078534ee8c3021281278.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9c107e992ae0a8e1f3683b52e323af786382638.jpeg">
  </div><p></p>
<p>Is it possible that you confuse the volumes? You have three volumes, and the problem may be that you volume render one, but you show the slices of another.</p>

---

## Post #14 by @Haru (2024-10-29 10:54 UTC)

<p>Thank you so much !!!<br>
I loaded only one volume and it worked.<br>
I thought I had to load the XY axis volume, the YZ axis volume, and the ZX axis volume all to get it to show up. Why is it possible to display a 3d image with only one volume loaded? Why is it possible to create cross sections for other axes as well?<br>
Anyway, now I can proceed with my research.<br>
Thank you very much for your kind help, even though my English is poor and all the information is useless.</p>

---

## Post #15 by @cpinter (2024-10-29 11:37 UTC)

<p>I’m not familiar with such acquisitions but it’s possible that they are just different orientation acquisitions of the same thing. Each one reconstructs the whole object, but resolution may be higher along certain axes (like for XY I assume that x and y resolution is high and in z lower, and the others are a different permutation of the same thing). Just my guess.</p>

---

## Post #16 by @Haru (2024-10-29 13:38 UTC)

<p>Thank you for your reply.<br>
I am convinced. I will try to change the loading volume depending on the direction I want to observe the sliced surface. Thank you so much!</p>

---

## Post #17 by @lassoan (2024-10-29 16:30 UTC)

<aside class="quote no-group" data-username="Haru" data-post="14" data-topic="39775">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ecc23a/48.png" class="avatar"> Haru:</div>
<blockquote>
<p>I thought I had to load the XY axis volume, the YZ axis volume, and the ZX axis volume all to get it to show up.</p>
</blockquote>
</aside>
<p>Only 2D image viewers require slices in different orientations. 3D Slicer works in 3D and it can display cross-sections in any orientation (even oblique) by reslicing the volume on-the-fly.</p>

---

## Post #18 by @Haru (2024-10-31 01:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="39775">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Only 2D image viewers require slices in different orientations. 3D Slicer works in 3D and it can display cross-sections in any orientation (even oblique) by reslicing the volume on-the-fly.</p>
</blockquote>
</aside>
<p>If I can read 2D data about any axis and still construct a 3d image, does that mean that the accuracy of the slice plane remains the same?</p>

---

## Post #19 by @muratmaga (2024-10-31 03:16 UTC)

<aside class="quote no-group" data-username="Haru" data-post="18" data-topic="39775">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ecc23a/48.png" class="avatar"> Haru:</div>
<blockquote>
<p>oes that mean that the accuracy of the slice plane remains the same?</p>
</blockquote>
</aside>
<p>Yes, if your data is isotropic (same resolution for each axis).</p>

---

## Post #20 by @cpinter (2024-10-31 09:52 UTC)

<p>In your case it seems that you have three volumes of the same thing, at the same resolutions (not isotropic), but sliced differently. I don’t quite understand why. I think you can use any of them, there should be no difference. This also means that there is no sense in using more than one. I’d use the XY one given that the standard “slicing” is that you have the same spacing within the slice and lower resolution along Z, and you can see the gantry shape in the slice.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11a294bae561deda370222cf52080fba55597209.png" data-download-href="/uploads/short-url/2w0rB5T7ihuM3vpeQ9H2fQGg4Yh.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11a294bae561deda370222cf52080fba55597209.png" alt="image" data-base62-sha1="2w0rB5T7ihuM3vpeQ9H2fQGg4Yh" width="509" height="128"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">509×128 2.66 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2926ff91cfbfb0bf8640257fc66d3c62eca9864a.png" data-download-href="/uploads/short-url/5S382Xa4Wx9RRyUWl2nYVnfLklc.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2926ff91cfbfb0bf8640257fc66d3c62eca9864a.png" alt="image" data-base62-sha1="5S382Xa4Wx9RRyUWl2nYVnfLklc" width="511" height="132"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">511×132 2.68 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #21 by @Haru (2024-10-31 12:11 UTC)

<p>The imaging conditions for an X-ray CT were 779 slices. When this data was converted to a DICOM file, it was saved in each of the XY, YZ, and ZX axes, because I mistakenly thought that data for each axis was needed to restore the 3D image.<br>
At that time, I think only the files for the YZ and ZX axes were changed to 1024 pieces. I do not know why.<br>
I want to count the number of bulkheads and examine the structure of the object, which is displayed on the slice surface.<br>
I would like to use XY data. Thank you for your instruction.</p>

---

## Post #22 by @cpinter (2024-10-31 12:31 UTC)

<aside class="quote no-group" data-username="Haru" data-post="21" data-topic="39775">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ecc23a/48.png" class="avatar"> Haru:</div>
<blockquote>
<p>YZ and ZX axes were changed to 1024 pieces. I do not know why.</p>
</blockquote>
</aside>
<p>Just a different permutation of the axes. Probably those acquisitions are not necessary at all.</p>

---

## Post #23 by @Haru (2024-10-31 13:07 UTC)

<p>I learned a lot.<br>
Thank you so much!</p>

---
