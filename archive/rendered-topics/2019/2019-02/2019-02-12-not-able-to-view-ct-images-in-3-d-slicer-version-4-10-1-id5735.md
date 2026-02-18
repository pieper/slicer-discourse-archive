# Not able to view CT images in 3 D slicer version 4.10.1

**Topic ID**: 5735
**Date**: 2019-02-12
**URL**: https://discourse.slicer.org/t/not-able-to-view-ct-images-in-3-d-slicer-version-4-10-1/5735

---

## Post #1 by @Tarun_Gangil (2019-02-12 06:11 UTC)

<p>Operating system:Windows 10 x 64- based PC; Processor	Intel® Core™ i5-2400 CPU @ 3.10GHz, 3100 Mhz, 4 Core(s), 4 Logical Processor(s); Installed Physical Memory (RAM)	8.00 GB</p>
<p>Slicer version: 4.10.1 stable releases<br>
Expected behavior: after loading the dicom images in the slicer it should be visible  as axial, sagital and coronal views in the red green and yellow frames<br>
Actual behavior: I am trying to import the DICOM CT images on the 3 D slicer it will show the message that import is successful and I will click on respective Axial, Sagital and Coronal plane and click on load. But I am not able to view the CT images in these red green and yellow frames at all. It will show the default black screen only. Even after loading the DICOM images properly.</p>
<p>Kindly let me know that this issue is occurring due to any hardware faults with my system or any changes in the software I have to do to resolve the same issue.</p>
<p>I have a laptop of similar configuration but RAM of 4.00 GB. I am able to load and view the images successfully in that using version 4.10.0 of 3 D slicer. But same I am not able to do on my PC</p>

---

## Post #2 by @pieper (2019-02-12 12:59 UTC)

<p>Hmm, hard to say.  If the same steps with the same data works on your laptop but not on your desktop PC then it does sound like a hardware issue, or maybe a driver.</p>
<p>Are you able to view the SampleData (e.g. the MRHead?).  Also you could look in the error log (in the Help-&gt;Report a bug menu).</p>

---

## Post #3 by @Tarun_Gangil (2019-02-13 04:11 UTC)

<p>No I can’t view the sample data also . I tried to load chest X ray, MR head. None of them worked.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/0/0d73b391a411b624b3b16af7379645d062c577c6.png" data-download-href="/uploads/short-url/1V05Ydny1BsG7NMxxaiIyxhHApg.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d73b391a411b624b3b16af7379645d062c577c6_2_562x316.png" alt="image.png" width="562" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d73b391a411b624b3b16af7379645d062c577c6_2_562x316.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d73b391a411b624b3b16af7379645d062c577c6_2_843x474.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d73b391a411b624b3b16af7379645d062c577c6_2_1124x632.png 2x" data-dominant-color="F0F0F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1920×1080 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>in error log I am getting this error</p>

---

## Post #4 by @Tarun_Gangil (2019-02-13 04:17 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/c/c17e8b2b38106a6d342be334642112cbaec923ce.png" data-download-href="/uploads/short-url/rBJgKUQwOWrypLefl2QjBchwbOS.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c17e8b2b38106a6d342be334642112cbaec923ce_2_562x316.png" alt="image.png" width="562" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c17e8b2b38106a6d342be334642112cbaec923ce_2_562x316.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c17e8b2b38106a6d342be334642112cbaec923ce_2_843x474.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c17e8b2b38106a6d342be334642112cbaec923ce_2_1124x632.png 2x" data-dominant-color="ECEEF4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1920×1080 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/0/0d73b391a411b624b3b16af7379645d062c577c6.png" data-download-href="/uploads/short-url/1V05Ydny1BsG7NMxxaiIyxhHApg.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d73b391a411b624b3b16af7379645d062c577c6_2_690x388.png" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d73b391a411b624b3b16af7379645d062c577c6_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d73b391a411b624b3b16af7379645d062c577c6_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d73b391a411b624b3b16af7379645d062c577c6_2_1380x776.png 2x" data-dominant-color="F0F0F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1920×1080 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @cpinter (2019-02-13 14:26 UTC)

<p>If you use a laptop with two graphics cards (an integrated and a dedicated), then it might be necessary to force Slicer to use the dedicated one.</p>
<p>Also you can try updating the graphics drivers if the above does not work.</p>

---
