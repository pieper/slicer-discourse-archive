# Volume Miscalculation

**Topic ID**: 13274
**Date**: 2020-09-01
**URL**: https://discourse.slicer.org/t/volume-miscalculation/13274

---

## Post #1 by @Angel (2020-09-01 07:47 UTC)

<p>Hello,</p>
<p>I have been using the Segment Statistics Module to try and compute the volumes of segmentations. However, the values do not seem to be correct. For example, the volume of the right ventricle is shown to be greater than the volume of the left ventricle. Also the volume is much lower than what we found to be the stroke volume.</p>
<p>Is there any reason that my readings are coming out this way?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-09-01 13:33 UTC)

<p>Volume computation is extensively tested and should be correct.</p>
<p>After you finished defining your seeds, you need to click Apply in “Grow from seeds” effect. Without that, you just measure volume of your seeds.</p>
<p>If this does not help then send the segmentation that you have problem with (or st least a few screenshots).</p>

---

## Post #3 by @Angel (2020-09-01 18:35 UTC)

<p>Hi,</p>
<p>Thank you for your response. I had used the Grow from Seeds Effect. We found the volume of blood pumped by the left ventricle per beat to be  9.7 ± 2.1 mm3 with some previous research…yet the left ventricle does not seem to have near that much volume itself.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6cfc1e5b004b12f0efda355d5931ea7c8b2e6956.png" alt="image" data-base62-sha1="fy7J9Q8tTZNGwLBBkEZmiTWr07Y" width="645" height="260"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/171274e7ea241bf06eeac474a6ed4b1f09be2c02.png" alt="image" data-base62-sha1="3i6wyfJCIW0E3ZvjirGsgnLuZ3Q" width="476" height="131"></p>

---

## Post #4 by @muratmaga (2020-09-01 18:50 UTC)

<p>Is this human data? Those values are too small. Can you confirm the spacing of your original dataset is correct?</p>

---

## Post #5 by @lassoan (2020-09-01 19:02 UTC)

<p>These seem to be just the seeds that you used for region growing. Have you tried going to Segment Editor module and click Apply in Grow from seeds effect?</p>
<p>But <a class="mention" href="/u/muratmaga">@muratmaga</a> is right, too. Non-clinical scanners often save their data with incorrect spacing that you need to fix manually. What is the spacing value displayed in Volumes module / Volume information section?</p>

---

## Post #6 by @Angel (2020-09-01 20:08 UTC)

<p>Hi,</p>
<p>Thank you for your response. This is not human data. We are using images of chicken embryo hearts. As for spacing I’m going by the information that the person I work under has provided me with.</p>

---

## Post #7 by @Angel (2020-09-01 20:12 UTC)

<p>Hi,</p>
<p>I did use the grow from seeds effect in the segment editor module. Here is the volume information:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/994fa87c87aa5b31d1241492e2f05d5be0013798.png" alt="image" data-base62-sha1="lSfICPkKLH4wLO9P5h3hK2Y9sRq" width="593" height="305"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96f7cdb34fb7219c88f4a74964a635bd6aaa2504.png" alt="image" data-base62-sha1="lxwxiOZOqY4LZPuAY0wzjnirele" width="594" height="355"></p>
<p>Thanks</p>

---

## Post #8 by @lassoan (2020-09-01 20:12 UTC)

<p>2633 voxels are about 50x50 voxels, which would be too few for a highly detailed surface that you show in the screenshot. So, it is a bit more likely that you compute volume for not the right segmentation node.</p>
<p>Can you share an example segmentation (upload somewhere and post the link here) so that we can have a look?</p>

---

## Post #9 by @Angel (2020-09-01 21:43 UTC)

<p>How do I upload the segmentation in order to share here?</p>

---

## Post #10 by @lassoan (2020-09-01 22:14 UTC)

<p>You can upload the file to Dropbox, OneDrive, Google Drive, etc. and post the link here.</p>

---

## Post #11 by @Angel (2020-09-01 23:27 UTC)

<p><a href="https://drive.google.com/file/d/15vlxpXtIvLiOe9_UWYHjOHLpQDRYqa5q/view?usp=sharing" rel="nofollow noopener">https://drive.google.com/file/d/15vlxpXtIvLiOe9_UWYHjOHLpQDRYqa5q/view?usp=sharing</a></p>
<p>I think one must download after clicking this link. Let me know if this link works.</p>

---

## Post #12 by @lassoan (2020-09-01 23:53 UTC)

<p>You have only uploaded the .mrml file, which is an index to the actual data files. Please save the scene as a single-file bundle (.mrb file) by clicking the package icon in the save data window:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9323762a1db15e80da4b2a4a3b4b4aed2f1fdebd.png" data-download-href="/uploads/short-url/kZEablf5Xd1KpSn1ssFW1zBsrx3.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9323762a1db15e80da4b2a4a3b4b4aed2f1fdebd_2_690x388.png" alt="image" data-base62-sha1="kZEablf5Xd1KpSn1ssFW1zBsrx3" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9323762a1db15e80da4b2a4a3b4b4aed2f1fdebd_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9323762a1db15e80da4b2a4a3b4b4aed2f1fdebd_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9323762a1db15e80da4b2a4a3b4b4aed2f1fdebd.png 2x" data-dominant-color="F9F9F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1262×710 39.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @Angel (2020-09-02 02:03 UTC)

<p>Thanks, I hope I uploaded it correctly this time.</p>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1_VM7zm5lfet6J7tEtFKVfTUovMwzFLsj/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1_VM7zm5lfet6J7tEtFKVfTUovMwzFLsj/view?usp=sharing" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1_VM7zm5lfet6J7tEtFKVfTUovMwzFLsj/view?usp=sharing" target="_blank" rel="nofollow noopener">2020-06-23-Scene.mrb</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #14 by @muratmaga (2020-09-02 05:09 UTC)

<p><a class="mention" href="/u/angel">@Angel</a> as <a class="mention" href="/u/lassoan">@lassoan</a> indicated previously, you didn’t finalize the ‘grow from the seed’. You need to first initialize using the seeds and review the expected segmentation with those seeds. If you are satisfied with that you then need to hit apply. Here is a result from your share scene where I simply hit initialize followed by apply. I think these numbers make much more sense:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91b5804156e520fe86d3ab3b48db6b3ad8f85b92.png" data-download-href="/uploads/short-url/kN0623adWj7R2743z0zXpznVYQ2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91b5804156e520fe86d3ab3b48db6b3ad8f85b92_2_690x346.png" alt="image" data-base62-sha1="kN0623adWj7R2743z0zXpznVYQ2" width="690" height="346" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91b5804156e520fe86d3ab3b48db6b3ad8f85b92_2_690x346.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91b5804156e520fe86d3ab3b48db6b3ad8f85b92_2_1035x519.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91b5804156e520fe86d3ab3b48db6b3ad8f85b92_2_1380x692.png 2x" data-dominant-color="3D3B3E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3840×1926 1.29 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @Angel (2020-09-02 07:45 UTC)

<p>Hi,</p>
<p>Thank you so much for taking a look! These numbers are definitely closer to my predictions. Is there any reason as to why the left ventricle is still less in volume as compared to the right ventricle?</p>
<p>Thanks!</p>

---

## Post #16 by @muratmaga (2020-09-02 14:51 UTC)

<p>I think your segmentation can use a bit more work and you probably want to add some more detail, before actually looking at the numbers.</p>

---

## Post #17 by @lassoan (2020-09-02 15:15 UTC)

<p>Yes, it looks like the segmentation does not cover the entire ventricle (it looks like up to about 5% of the volume may be missed in the segmentation). You can adjust the “Editable intensity range” so that includes a bit more of the dark regions (set the lower threshold value a bit lower) and use Margin effect to grow it a bit into these regions.</p>

---

## Post #19 by @Angel (2020-09-03 01:23 UTC)

<p>Thank you so much for your patience! I have one last question: why does the volume information change after I save to files?</p>
<p>Unsaved:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ece69f54ced354c2b0b75a46e9e835e99e86344a.png" alt="image" data-base62-sha1="xNIMVJzDaWPEKzjEMUGm63JbvKi" width="595" height="207"></p>
<p>Saved:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fb12c5cfe97aa30707953668df8f08a6ad19ea0.png" alt="image" data-base62-sha1="2eOKKIo6dGJbUCSuBFL27D0RF3a" width="594" height="212"></p>

---

## Post #20 by @lassoan (2020-09-03 01:29 UTC)

<p>Volume spacing should not change when you save the scene and reload it. What file format are you saving into?</p>

---

## Post #21 by @Angel (2020-09-03 01:46 UTC)

<p>I tried saving it as both .mrml file and .mrb file and it changed both times.</p>

---

## Post #22 by @lassoan (2020-09-03 02:24 UTC)

<p>In the scene file that you have uploaded, the volume spacing was [0.016, 0.016, 1.0]. I have changed it to [0.016, 0.016, 0.016] in Volumes module then saved it as both .mrml and mrb. In both cases, the spacing was saved in the <em>504_16-perfect-TOF.VOX256.nrrd</em> image file correctly (as [0.016, 0.016, 0.016]) and after loading the scene or the image file, the spacing was correct again ([0.016, 0.016, 0.016]).</p>
<p>Is it possible that you may have chosen a different filename when you saved the image? Or maybe you have not saved it after changing the spacing? If you can reproduce the incorrect behavior (not saving modified spacing into the nrrd file) then let us know.</p>
<p>Note that volume spacing is not saved in the .mrml file but in the image (.nrrd) file, and only if you choose to save the image file (saving should be offered by default after you change spacing and open the save data window).</p>

---

## Post #23 by @Angel (2020-09-03 05:43 UTC)

<p>Hi,</p>
<p>The filename was not changed. I had cropped the image after changing spacing since the voxel size is 16 microns, and the image became very small. Then, I performed the segmentation, and saved the scene after I finished. As a result, the .nrrd image file is saving the cropped version of the image and using its volume information. Is the segmentation going to be saved in the .nnrd image file as well?</p>
<p>Thanks</p>

---

## Post #24 by @muratmaga (2020-09-03 06:17 UTC)

<p>Your previous thread indicated data came as a JPG sequence. Since JPG doesn’t contain the image spacing, you need to manually enter 0.016 to all three fields right after the import and then save the NRRD file. My suspicion is you never actually saved the imported volume in NRRD file and scene file (MRML) just points out to the JPG stack and you are loosing the spacing information every time you open the MRML file (it essentially re-imports everything). That would be my guess as why your spacing changes after reload (since image spacing information is contained in NRRD file, not in the MRML).</p>
<p>As for image getting small after you are entering the correct spacing, you can use the ‘center field of view’ button to fix that.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/1967f155f272022787eef465a84cc478f19c2f98.png" alt="image" data-base62-sha1="3CKDfhfBVA0XAjCsNOk68FnVkYU" width="397" height="106"></p>

---

## Post #25 by @Angel (2020-09-04 22:13 UTC)

<p>That is probably why I have been losing the image information. Also thanks for letting me know about the centering function.</p>
<p>I appreciate the help from both of you. Thank you so much for being so patient. Looking forward to working more with Slicer.</p>

---

## Post #26 by @muratmaga (2020-09-05 03:26 UTC)

<p>No problem. If your data routinely comes in the form of image sequence (jpg or other formats). I highly encourage you to install SlicerMorph extension and use the <a href="https://github.com/SlicerMorph/S_2020/blob/master/Day_1/ImageStacks/ImageStacks.md" rel="nofollow noopener">ImageStacks</a> module for importing that. You can specify spacing at the time of import (not after), and you do not have to do the vector to scaling conversion to use the segment editor or the volume rendering.</p>

---

## Post #27 by @Angel (2020-09-08 04:37 UTC)

<p>Just installed the extension. Thanks for letting me know about it!</p>

---
