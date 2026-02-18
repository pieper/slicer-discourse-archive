# Trouble showing DICOM-pictures with different B-values in 3D-Slicer

**Topic ID**: 4317
**Date**: 2018-10-08
**URL**: https://discourse.slicer.org/t/trouble-showing-dicom-pictures-with-different-b-values-in-3d-slicer/4317

---

## Post #1 by @persst (2018-10-08 11:18 UTC)

<p>Hi!</p>
<p>I have a set of DICOM-files with diffusion weighted images, which I intend to use to access cerebral ischemia. The DICOM-files have both B0, B500 and B1000 sequences in the same stack. When I load the file in 3D-Slicer, only the B0-images are visible, but I am interested in the B1000-sequence.</p>
<p>How do I show the B1000-sequence in 3D-Slicer?</p>

---

## Post #2 by @fedorov (2018-10-08 14:37 UTC)

<p>You can use MultiVolumeExplorer module to select the b-value to be shown, if your dataset is loaded as a multivolume.</p>

---

## Post #3 by @Mihail_Isakov (2018-10-09 05:05 UTC)

<p>I have such series from Siemems Avanto, e.g. 320 x 320 x 25 x 4 as single series, where 4th dimension is B-value of 0, 500, 1000, 1500. Somehow i also failed to load it into Slicer, there are errors and no volume appeared in Volume Rendering module, tried different checkboxes. Alternatively you can load the series in<br>
<a href="http://www.aliza-dicom-viewer.com/" rel="noopener nofollow ugc">Aliza DICOM Viewer</a><br>
It loads it as 4 volumes very easy (open folder in DICOM browser, e,g, drag-and-drop <em>folder</em>), then save a volume as e.g. MHA file and load it in Slicer.<br>
If somebody wants investigate, i can upload, i’ve got from 1st hand and anonymized</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e53920028583544c09a654b37b28e71c8fee2cea.jpeg" data-download-href="/uploads/short-url/wHNJihGXe4l5kcBDTuFp05qA6XE.jpeg?dl=1" title="Screenshot2018-10-09%2006-47-41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e53920028583544c09a654b37b28e71c8fee2cea_2_690x388.jpeg" alt="Screenshot2018-10-09%2006-47-41" data-base62-sha1="wHNJihGXe4l5kcBDTuFp05qA6XE" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e53920028583544c09a654b37b28e71c8fee2cea_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e53920028583544c09a654b37b28e71c8fee2cea_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e53920028583544c09a654b37b28e71c8fee2cea_2_1380x776.jpeg 2x" data-dominant-color="909298"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot2018-10-09%2006-47-41</span><span class="informations">1920×1080 328 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/827d0a6e045858c1e90cde42240832444b7ba616.jpeg" data-download-href="/uploads/short-url/iClY7zglL5lbV876D1ek99GR9MW.jpeg?dl=1" title="Screenshot2018-10-09%2006-48-07" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/827d0a6e045858c1e90cde42240832444b7ba616_2_690x388.jpeg" alt="Screenshot2018-10-09%2006-48-07" data-base62-sha1="iClY7zglL5lbV876D1ek99GR9MW" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/827d0a6e045858c1e90cde42240832444b7ba616_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/827d0a6e045858c1e90cde42240832444b7ba616_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/827d0a6e045858c1e90cde42240832444b7ba616_2_1380x776.jpeg 2x" data-dominant-color="55524F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot2018-10-09%2006-48-07</span><span class="informations">1920×1080 419 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2018-10-09 05:37 UTC)

<p>MultiVolume requires all volumes to have exact same geometry, maybe this is not true for your data set. If you enable in Application settings / DICOM / Allow loading subseries by time then you may be able to load each volume in the DICOM browser’s advanced section.</p>
<p>Please upload the anonymized data set somewhere and post the link. We can then tell what options need to be set exactly or why the data set cannot be loaded.</p>

---

## Post #5 by @Mihail_Isakov (2018-10-09 06:19 UTC)

<p><a href="https://drive.google.com/file/d/1Xm6P51artAGleefRXLAwGc25g2gVicE3/view?usp=sharing" rel="nofollow noopener">Data set</a></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Here is the data set, not sure it is similar with data set in question, just if you like to experiment, i don’t need support with it just now.</p>
<p>Regards</p>

---

## Post #6 by @fedorov (2018-10-09 13:41 UTC)

<p>Thanks for sharing the dataset! Everything works for me as expected.</p>
<p>Your dataset is being parsed with different parsing strategies, and the one that initializes b-values is not the one that is loaded by default. You can see all parsed multivolume loadables by enabling “Advanced” checkbox in “DICOM Browser”. If you do that, you can select the multivolume parsed by b-values:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/055a09a9a5982b633e862b0f096bb5b2f7d6f0bc.png" data-download-href="/uploads/short-url/Lli7IE2PXUAycgDuywW2xuefjm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/055a09a9a5982b633e862b0f096bb5b2f7d6f0bc_2_690x201.png" alt="image" data-base62-sha1="Lli7IE2PXUAycgDuywW2xuefjm" width="690" height="201" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/055a09a9a5982b633e862b0f096bb5b2f7d6f0bc_2_690x201.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/055a09a9a5982b633e862b0f096bb5b2f7d6f0bc.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/055a09a9a5982b633e862b0f096bb5b2f7d6f0bc.png 2x" data-dominant-color="F0F0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">990×289 28.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Next you can use “MultiVolume Explorer” module to scroll through the volumes corresponding to the individual b-values:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9985823778cbfb9132efad691fbbfb12fe9e6d37.png" data-download-href="/uploads/short-url/lU75PbBc6BiwToRWo4Xf9P9UwHt.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9985823778cbfb9132efad691fbbfb12fe9e6d37_2_690x440.png" alt="image" data-base62-sha1="lU75PbBc6BiwToRWo4Xf9P9UwHt" width="690" height="440" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9985823778cbfb9132efad691fbbfb12fe9e6d37_2_690x440.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9985823778cbfb9132efad691fbbfb12fe9e6d37_2_1035x660.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9985823778cbfb9132efad691fbbfb12fe9e6d37_2_1380x880.png 2x" data-dominant-color="ABAAAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1455×928 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Mihail_Isakov (2018-10-09 19:11 UTC)

<p>Thank you, Prof. Fedorov, screenshot is very useful.<br>
Regards</p>

---

## Post #8 by @Joejoe (2018-10-14 06:22 UTC)

<p>Thanks! very helpful.</p>
<p>I wonder if it is possible to put different b value image on the four screen together? So when I load the Simens trace diffusion images, I can segment the lesion with reference to different b value images.</p>

---

## Post #9 by @fedorov (2018-10-15 15:56 UTC)

<p>There is a “Copy frame” button in MultiVolumeExplorer that you can use to copy individual frames into separate scalar volume nodes.</p>

---
