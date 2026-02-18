# Display issue with RT structs and MR volume

**Topic ID**: 546
**Date**: 2017-06-21
**URL**: https://discourse.slicer.org/t/display-issue-with-rt-structs-and-mr-volume/546

---

## Post #1 by @yannick_s (2017-06-21 13:40 UTC)

<p>Operating system: <em>Ubuntu 16.04 LTS (tried on Windows 10 with the same result)</em><br>
Slicer version: <em>4.7.0-2017-06-03 r26072</em><br>
Expected behavior: <em>RT struct with contouring done in the axial view in a radiotherapy planning software. If this contour is viewed in Slicer in the axial view, there should be a contour for each slice and the contour should be aligned with the image volume</em><br>
Actual behavior: <em>Contour is ‘tilted’ (see screenshot)</em></p>
<p>Dear all,</p>
<p>We have postoperative MR of GBM patients, with the contour of the cavity as an RT struct. The contouring was done in the radiotherapy planning software on axial slices. When loaded into Slicer, the contours are not aligned with the axial slices:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d45f90315ec97eb93357bdc80feac9b959df5ac4.png" data-download-href="/uploads/short-url/uiJXXnL7WTEzGeqk58sVC6Sb7CI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d45f90315ec97eb93357bdc80feac9b959df5ac4_2_690x299.png" alt="image" data-base62-sha1="uiJXXnL7WTEzGeqk58sVC6Sb7CI" width="690" height="299" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d45f90315ec97eb93357bdc80feac9b959df5ac4_2_690x299.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d45f90315ec97eb93357bdc80feac9b959df5ac4_2_1035x448.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d45f90315ec97eb93357bdc80feac9b959df5ac4.png 2x" data-dominant-color="638B98"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1051×456 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am not sure if that’s a problem on our side or if for some reason Slicer does not display it correctly. Due to this tilt, we have issues creating label maps from the contours. Additionally, the contouring “slices” of the RT struct are not equally spaced when viewed in the 3D window.<br>
I cannot publicly share the anonymized data here, if someone can help and try to reproduce it, I can send it e.g. by email.</p>
<p>Any help highly appreciated.</p>
<p>Best and thank you,</p>
<p>Yannick</p>

---

## Post #2 by @Sunderlandkyl (2017-06-21 14:07 UTC)

<p>Hello Yannick,</p>
<p>It looks like there is a problem with the planar contour to closed surface conversion.<br>
If you could send me an email with the data, I will see if I can figure out what the problem is.<br>
I will message you with my email.</p>
<p>Thanks!<br>
Kyle</p>

---

## Post #3 by @lassoan (2017-06-21 14:12 UTC)

<p>It seems that your MR volume axes are not aligned with patient anatomical axes. It’s not a problem, Slicer just shows slice viewers aligned with anatomical axes by default. Click “Rotate to volume plane” button in the slice view controller to align slice viewers to volume planes:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf3f0e8f408cedb7284fb9c6bff19961e44e3c25.png" alt="image" data-base62-sha1="rhQikdUsI4xSeSiEGgbNeOuGIBL" width="489" height="210"></p>
<p>In the treatment planning software, did you draw contours with variable distance between them?</p>

---

## Post #4 by @yannick_s (2017-06-21 14:47 UTC)

<p>Hi Andras and Kyle,</p>
<p>Thanks, that helped a lot already! Rotating to volume plane gets rid of the “tilt”. The contour “slices” are now aligned with the volume in the 3D  view. If I change the Segmentations display to “planar contour”, the contour “slices” seem equally spaced - great! Yes, the contours were done on all (equally spaced) axial slices.</p>
<p>What’s still strange is the label map generated from the contours:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/169763acd7a14538a83d6169f9d1a091d8b0fe74.png" data-download-href="/uploads/short-url/3dQQYT43cJ11CDqZGAJKhYcdS6g.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/169763acd7a14538a83d6169f9d1a091d8b0fe74_2_690x327.png" alt="image" data-base62-sha1="3dQQYT43cJ11CDqZGAJKhYcdS6g" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/169763acd7a14538a83d6169f9d1a091d8b0fe74_2_690x327.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/169763acd7a14538a83d6169f9d1a091d8b0fe74.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/169763acd7a14538a83d6169f9d1a091d8b0fe74.png 2x" data-dominant-color="565C57"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">949×450 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is it possible that the rotation of the volume plane is not considered when the label maps are created?</p>
<p>Best and thanks,</p>
<p>Yannick</p>

---

## Post #5 by @Sunderlandkyl (2017-06-21 16:41 UTC)

<p>The default labelmap conversion goes through the pathway: planar contours -&gt; closed surface -&gt; binary labelmap, so if there is an issue with the surface, that issue will be propagated to the labelmap.</p>
<p>For now, you can work around this issue by using the planar contour -&gt; ribbon model -&gt; binary labelmap conversion instead.</p>
<p>You can do this in the Segmentations module by long-pressing the create button and selecting advanced create (or clicking the update button if the labelmap has already been created) beside the binary labelmap representation, and selecting a different conversion path.</p>
<p>Let me know if this helps!</p>
<p>Thanks,<br>
Kyle</p>

---

## Post #6 by @pieper (2017-06-21 19:14 UTC)

<p>Kyle’s suggested fix should work - I’ve used it for other data.</p>
<p>I’ll just not <a class="mention" href="/u/yannick_s">@yannick_s</a> that with MR often an “axial” image will still be rotated with respect to patient space, for example so that the rectangular bounds of the scanned region best capture the target anatomy efficiently.  That could be why the is like this.</p>

---

## Post #7 by @yannick_s (2017-06-22 14:48 UTC)

<p>Ok, I tried both paths to create the binary label map. The closed surface and planar contour are both available when loading the segmentation, with the planar contour as master. It looks like there are multiple polygons per axial slice (sometimes overlapping), which seems to confuse the label map creation. Here’s a screenshot of a relatively “benign” example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/7460d6b714b5a7cf469f39a4c1b87ef72ed8bd06.png" data-download-href="/uploads/short-url/gBwRtOV0mUpAC4RvHOR5CXmGJHU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/7460d6b714b5a7cf469f39a4c1b87ef72ed8bd06_2_690x289.png" alt="image" data-base62-sha1="gBwRtOV0mUpAC4RvHOR5CXmGJHU" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/7460d6b714b5a7cf469f39a4c1b87ef72ed8bd06_2_690x289.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/7460d6b714b5a7cf469f39a4c1b87ef72ed8bd06_2_1035x433.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/7460d6b714b5a7cf469f39a4c1b87ef72ed8bd06.png 2x" data-dominant-color="667473"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1090×457 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<strong>Left</strong>: Segmentation as a closed surface, <strong>Right, purple label</strong>: label map created with planar contour → ribbon model → binary labelmap; <strong>right, green label</strong>: planar contour → closed surface → binary labelmap</p>
<p>Maybe I have to combine all polygons per slice first to get anything meaningful out of this.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> Is there a way to check if the “axial” image is rotated with respect to the patient space?</p>
<p>Thanks for the help!</p>

---

## Post #8 by @pieper (2017-06-22 15:09 UTC)

<p><a class="mention" href="/u/yannick_s">@yannick_s</a> yes, look in the Volumes -&gt; Information -&gt; IJKToRAS non-identity (+/-) terms.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.6/Modules/Volumes" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.6/Modules/Volumes</a></p>
<p>Also note that RT structures will often (usually?) overlap because both tumor and treatment volumes are includes.  These don’t map to a single labelmap.  I’m not sure if that’s what’s happening in your case.</p>

---

## Post #9 by @yannick_s (2017-06-23 12:54 UTC)

<p>Thanks!<br>
I checked, only the postop cavity should be in the segmentation. But apparently, the segmentation was not done with a single contour per slice, but sometimes with several polygons per slice to capture the whole cavity.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a003a7cf22d5a47fe46f8b8a6b02817fc6d26c1.png" alt="image" data-base62-sha1="jGOnAjrUjNlCoOqPMLEiaiXVcPf" width="427" height="437"><br>
For me it looks like the binary label map conversion get’s confused by multiple polygons:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75401ef3659f6d39e696caf3e977954dccb1e26e.png" alt="image" data-base62-sha1="gJff1Wjj44ZQffAImd09Wsc4kkC" width="336" height="371"></p>
<p><a class="mention" href="/u/pieper">@pieper</a><br>
I have a IJLToRAS transform looking like this.<br>
IJKtoRAS =<br>
[-0.9982,   -0.0550,    0.0218<br>
0.0495   -0.9777   -0.2042<br>
0.0325   -0.2028    0.9787]<br>
So, to align the axial image to patient space, I have to transform the volume so that it gets [-1,0,0;0,-1,0,10,0]? to avoid flipping?</p>

---

## Post #10 by @lassoan (2017-06-23 13:26 UTC)

<p>Having multiple contours in the same slice in the same structure does not seem to be valid. <a href="http://dicom.nema.org/dicom/2013/output/chtml/part03/sect_C.8.html#sect_C.8.8.6">DICOM standard Part 3 C. 8.8.6</a> does not explicitly say that intersection is prohibited, but “closed contour (polygon) containing coplanar points” indicates that a simple polygon is expected. It is explicitly stated that you cannot even make a hole in a polygon (you need to use keyhole technique instead).</p>
<p>Did you draw multiple contours in the same slice in the same structure in the treatment planning system? Or you have distinct contours in the treatment planning system but they show up at the same slice in Slicer?</p>

---

## Post #11 by @yannick_s (2017-07-05 12:34 UTC)

<p>Hi everyone,</p>
<p>Thank you all for the great help. It looks like the artifacts came from exporting from the clinical system where some “re-slicing” occurred.</p>

---

## Post #12 by @Rasha (2017-07-12 02:47 UTC)

<p>Hi All,</p>
<p>I have the same problem… After importing the RT-Structure Dicom set from TPS to 3Dslicer, I start having gabs or blanks between slides exactly as showing by yannick_sYannick image above. I tried to follow lassoan suggestions, it did work in the Sagital plan not the axial nor coronal view.</p>
<p>Any suggestions, please?</p>
<p>Thanks in advance for your help!<br>
Rasga</p>

---

## Post #13 by @Rasha (2017-07-12 02:49 UTC)

<p>I still have gabs between the slides. Can you please explain again how can I have no gabs between the slides? Please</p>

---

## Post #14 by @lassoan (2017-07-12 03:55 UTC)

<p>Please provide a screenshot of the structure set in the TPS and in 3D Slicer.</p>

---

## Post #15 by @yannick_s (2017-07-12 04:10 UTC)

<p>Hi,</p>
<p>Did you try rotating to volume plane for each view? There’s a button for this in all three (coronal, axial, sagittal) views, <a class="mention" href="/u/lassoan">@lassoan</a> pointed me to in a post above.</p>

---

## Post #16 by @Rasha (2017-07-12 14:07 UTC)

<p>Yes, I was able to rotate to volume plan only for sagital view. Doing the same way to other views do not work (axial and coronal views).</p>

---

## Post #17 by @Rasha (2017-07-12 14:14 UTC)

<p>Here is the screenshot of TPS</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/804e6035175edde2d08a4dbfea2b6b2c7f3c00af.jpg" data-download-href="/uploads/short-url/ij32cUkX2mEL6RRF8r9uSLneqvB.jpg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/804e6035175edde2d08a4dbfea2b6b2c7f3c00af_2_690x425.jpg" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/804e6035175edde2d08a4dbfea2b6b2c7f3c00af_2_690x425.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/804e6035175edde2d08a4dbfea2b6b2c7f3c00af_2_1035x637.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/804e6035175edde2d08a4dbfea2b6b2c7f3c00af_2_1380x850.jpg 2x" data-dominant-color="303231"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">2996×1848 979 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #18 by @Rasha (2017-07-12 14:16 UTC)

<p>Here is in 3D slicer. The file it too big to upload it at once.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/ec8d763ed40bff58c3e1ed4d8008ee333246a6a3.jpg" data-download-href="/uploads/short-url/xKDLlOO2PtkF3FNc8ZtfOmEuz19.jpg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ec8d763ed40bff58c3e1ed4d8008ee333246a6a3_2_616x499.jpg" width="616" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ec8d763ed40bff58c3e1ed4d8008ee333246a6a3_2_616x499.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ec8d763ed40bff58c3e1ed4d8008ee333246a6a3_2_924x748.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ec8d763ed40bff58c3e1ed4d8008ee333246a6a3_2_1232x998.jpg 2x" data-dominant-color="8791B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">2121×1721 2.19 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #19 by @lassoan (2017-07-12 15:50 UTC)

<p>Thank you. Could you share an anonymized data set using Dropbox or OneDrive so that we can investigate and fix the problem?</p>

---

## Post #20 by @Rasha (2017-07-12 15:55 UTC)

<p>I am afraid that I can not share the data in public. However, would the structure set be okay to diagnose the problem?</p>

---

## Post #21 by @lassoan (2017-07-12 16:06 UTC)

<p>Send us the structure set for now. We may be able to diagnose the issue from that.</p>
<p>If that’s not enough, then scan a phantom or use a publicly available DICOM data set (for example, download from <a href="http://www.cancerimagingarchive.net/">TCIA</a>) and perform a similar contouring in the TPS and share that data set.</p>

---

## Post #22 by @Rasha (2017-07-12 16:19 UTC)

<p>I just send it to you by email. Thanks again for your help.</p>
<p>Rasha</p>

---

## Post #23 by @lassoan (2017-07-12 19:15 UTC)

<p>I haven’t received anything by email. Please upload it to dropbox, onedrive, etc. and post the link here. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> will investigate the issue.</p>

---

## Post #24 by @Rasha (2017-07-12 19:28 UTC)

<p>Would you please provide me your email address to send it?<br>
I used  <a>"slicer@discoursemail.com</a>" in the previous email.</p>
<p>Regards,<br>
Rasha</p>

---

## Post #25 by @lassoan (2017-07-12 19:31 UTC)

<p>I don’t know what this slicer@discourse… email address is. In the meantime, <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> has received the file from you, so that is enough. He’ll investigate and report back here.</p>

---

## Post #26 by @Sunderlandkyl (2017-07-13 15:08 UTC)

<p>I managed to fix the issue by rotating the structure before triangulation so that the contour normals align with the z-axis, and then rotating back afterwards.</p>
<p>Let me know if this fixes your issue, or if you have any other problems!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e6357c3b022d0acde8e14c8245d2fec9f14acbb.png" alt="image" data-base62-sha1="bbs5bQgA1iXrQLn89zMNk45t5Cb" width="664" height="444"></p>

---

## Post #27 by @lassoan (2017-07-13 15:36 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> - Is the fix included in today’s nightly build?</p>

---

## Post #28 by @Sunderlandkyl (2017-07-13 15:39 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Yes, it should be included in the next nightly.</p>

---
