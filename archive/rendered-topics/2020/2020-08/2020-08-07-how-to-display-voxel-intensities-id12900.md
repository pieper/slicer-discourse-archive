# How to display voxel intensities

**Topic ID**: 12900
**Date**: 2020-08-07
**URL**: https://discourse.slicer.org/t/how-to-display-voxel-intensities/12900

---

## Post #1 by @Vinny (2020-08-07 20:39 UTC)

<p>Hi,</p>
<p>I have a NIFTI image of a tract that contains different voxel intensities.  In fsleyes, I am able to view the  different intensities for each voxel.  However, when I import the image into 3D Slicer, the image is displayed with a solid homogeneous colour but Slicer does recognize that there are different voxel intensities within the Data Probe tab.  I tried to change the colours in the Display-&gt;Lookup Table but with no success.  How can I get the colours of the image to reflect the different voxel intensities?</p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #2 by @lassoan (2020-08-07 21:34 UTC)

<p>By default, volumes that have single-component voxels are loaded as “scalar volumes” (voxel values are continuous), while it seems that your data is a “labelmap volume” (voxel values are discrete, each value represents one tract). While you can adjust window/level and colormap of a scalar volume so that you can distinguish each integer value, probably you want to load the volume either as a segmentation (if you want to show/hide individual label values, edit them, display in 3D, etc.) or as a labelmap volume (it can handle thousands of values without performance issues, but needs volume rendering for 3D display and cannot easily show/hide individual values).</p>
<ul>
<li>Load as a segmentation: in “Add data” dialog, choose “Segmentation” in “Description” column</li>
<li>Load as labelmap volume: in “Add data” dialog, check “Show options” and check “LabelMap” option. To avoid the need for enabling LabelMap option manually, you can rename the image file so that the filename ends with “-label” (for example, “something-label.nrrd”) and then LabelMap option will be enabled by default.</li>
</ul>
<p>You can also convert between labelmap and scalar volume in Volumes module -&gt; Volume information section -&gt; Convert to label map.</p>
<p>I would be really interested to see how these tracts look in Slicer. It would be great if you could attach a screenshot of the result.</p>

---

## Post #3 by @Vinny (2020-08-07 22:21 UTC)

<p>Hi Andras,</p>
<p>Thanks for your quick reply.  The segmentation option was taking a very long time because of the number of large number of intensity values.  However, the labelmap option appeared to work however, the output is slightly different from what I see in fsleyes.  I’ve attached screenshots for the corticospinal tract represented both in fsleyes and Slicer.  when looking at the Data Probe, the voxel intensity values are similar to what I’m seeing in fsleyes, but the tract voxel intensities are displayed differently.  Essentially, the larger the voxel intensity, the brighter the voxel should appear.  But I’m not able to display this relationship in Slicer.</p>
<p>Thanks,</p>
<p>Vinny</p>
<p>fsleyes:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aed14961764848326ef17d6ef5af7399e4ad4428.png" data-download-href="/uploads/short-url/oWvtpGrhQNdBfoRUVZyQ51ud8Pm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aed14961764848326ef17d6ef5af7399e4ad4428.png" alt="image" data-base62-sha1="oWvtpGrhQNdBfoRUVZyQ51ud8Pm" width="690" height="265" data-dominant-color="555453"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1842×708 28.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Slicer:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a53d9bd32f72bfb4f000a6a268a663e9d98d8e1.jpeg" data-download-href="/uploads/short-url/m1fb7EhXfO5MyHa8S7uyKSJEt0t.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9a53d9bd32f72bfb4f000a6a268a663e9d98d8e1_2_672x499.jpeg" alt="image" data-base62-sha1="m1fb7EhXfO5MyHa8S7uyKSJEt0t" width="672" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9a53d9bd32f72bfb4f000a6a268a663e9d98d8e1_2_672x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9a53d9bd32f72bfb4f000a6a268a663e9d98d8e1_2_1008x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a53d9bd32f72bfb4f000a6a268a663e9d98d8e1.jpeg 2x" data-dominant-color="626161"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1250×930 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-08-07 22:23 UTC)

<p>Can you upload a sample data set somewhere and post the link here?</p>

---

## Post #5 by @Vinny (2020-08-07 22:36 UTC)

<p>Here’s the link… <a href="https://github.com/vinkirk/public" rel="nofollow noopener">https://github.com/vinkirk/public</a></p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #6 by @lassoan (2020-08-07 23:13 UTC)

<p>Thank you, it was very helpful to see what kind of data you work with. Voxels of this tract volume are actually continuous, so it should be loaded with default settings (as scalar volume). You can then adjust its color mapping and display it as a foreground volume:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c37b0cfedf0006fc81ec970b3e2b3458105504f.jpeg" data-download-href="/uploads/short-url/hISwqBSHemoRwmt6Z5z2R9e7NYX.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c37b0cfedf0006fc81ec970b3e2b3458105504f_2_690x419.jpeg" alt="image" data-base62-sha1="hISwqBSHemoRwmt6Z5z2R9e7NYX" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c37b0cfedf0006fc81ec970b3e2b3458105504f_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c37b0cfedf0006fc81ec970b3e2b3458105504f_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c37b0cfedf0006fc81ec970b3e2b3458105504f_2_1380x838.jpeg 2x" data-dominant-color="BFBEC0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1370 619 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Adjust color mapping in Volumes module:</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/125de19215aa94a336bd17757533825ddb28c6de.png" data-download-href="/uploads/short-url/2CtJv0s7BsmtHwQbPcyOtnGWhe6.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/125de19215aa94a336bd17757533825ddb28c6de_2_535x500.png" alt="image" data-base62-sha1="2CtJv0s7BsmtHwQbPcyOtnGWhe6" width="535" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/125de19215aa94a336bd17757533825ddb28c6de_2_535x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/125de19215aa94a336bd17757533825ddb28c6de_2_802x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/125de19215aa94a336bd17757533825ddb28c6de_2_1070x1000.png 2x" data-dominant-color="F2EAD7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1253×1170 91.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Show tract as foreground volume:</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/0170857b25fb9921288feb90be6dfe743680fd6d.png" data-download-href="/uploads/short-url/cJyjzQCKYo13MDEXe8r8Nszclv.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/0170857b25fb9921288feb90be6dfe743680fd6d_2_690x395.png" alt="image" data-base62-sha1="cJyjzQCKYo13MDEXe8r8Nszclv" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/0170857b25fb9921288feb90be6dfe743680fd6d_2_690x395.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/0170857b25fb9921288feb90be6dfe743680fd6d_2_1035x592.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/0170857b25fb9921288feb90be6dfe743680fd6d.png 2x" data-dominant-color="ECDCBD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1337×767 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Show tract using volume rendering:</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40eefc7152280ebc798c3b4a812e7c59a580a36f.png" data-download-href="/uploads/short-url/9gqAaSwUrrWx6po8fBWoOE2bwHZ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40eefc7152280ebc798c3b4a812e7c59a580a36f_2_496x499.png" alt="image" data-base62-sha1="9gqAaSwUrrWx6po8fBWoOE2bwHZ" width="496" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40eefc7152280ebc798c3b4a812e7c59a580a36f_2_496x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40eefc7152280ebc798c3b4a812e7c59a580a36f_2_744x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40eefc7152280ebc798c3b4a812e7c59a580a36f_2_992x998.png 2x" data-dominant-color="F5F5F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1229×1238 64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To avoid the need for these 15-20 clicks to set up visualization, you could add a simple Python scripted module, which would load a tract image and set up all the visualization by a single click. You can learn about how to create such module from <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">Slicer programming tutorials</a>. We are here to help if you need any help with it. If this is a common task then we can add it to the <a href="https://github.com/PerkLab/SlicerFreeSurfer">FreeSurfer importer module</a>.</p>

---

## Post #7 by @Vinny (2020-08-07 23:31 UTC)

<p>Thank you very much Andras, this works exactly.  I agree that it would be a good idea to wrap all these steps up in script.  I’ll go through the tutorials that you provided and definitely will be in contact with your team should I need help.  Thanks again!</p>
<p>Vinny</p>

---
