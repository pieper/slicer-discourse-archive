# .stl file uploaded does not appear as a "volume"

**Topic ID**: 3114
**Date**: 2018-06-07
**URL**: https://discourse.slicer.org/t/stl-file-uploaded-does-not-appear-as-a-volume/3114

---

## Post #1 by @DavideBassano (2018-06-07 14:51 UTC)

<p>Hi,</p>
<p>my .stl file is not considered a volume in the “volume” module and neither in the “landmark registration” module.<br>
Why? Is there a way to solve this problem?</p>
<p>Pictures are following to explain better my problem:</p>
<p>I uploaded a DICOM data and a .stl file:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d15896e3993861cf951431d77ab77a8e516ad2a6.jpeg" data-download-href="/uploads/short-url/tRXAMuwtW8pVgpyeGpTNiHiDThA.jpg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d15896e3993861cf951431d77ab77a8e516ad2a6_2_281x500.jpg" alt="1" data-base62-sha1="tRXAMuwtW8pVgpyeGpTNiHiDThA" width="281" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d15896e3993861cf951431d77ab77a8e516ad2a6_2_281x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d15896e3993861cf951431d77ab77a8e516ad2a6_2_421x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d15896e3993861cf951431d77ab77a8e516ad2a6_2_562x1000.jpg 2x" data-dominant-color="888591"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1295×2303 1.62 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad1e00b0350bb69aeed05d27d6a63cf2cb9ee523.jpeg" data-download-href="/uploads/short-url/oHsSJGiD2woN5FKUrD2ntYoXSmf.jpg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad1e00b0350bb69aeed05d27d6a63cf2cb9ee523_2_690x387.jpg" alt="2" data-base62-sha1="oHsSJGiD2woN5FKUrD2ntYoXSmf" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad1e00b0350bb69aeed05d27d6a63cf2cb9ee523_2_690x387.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad1e00b0350bb69aeed05d27d6a63cf2cb9ee523_2_1035x580.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad1e00b0350bb69aeed05d27d6a63cf2cb9ee523_2_1380x774.jpg 2x" data-dominant-color="848593"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">3258×1832 2.93 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
(if a select ‘volume’ instead of ‘model’ in description, it doesn’t show the volume)</p>
<p>The red volume is the dicom data and the grey one is the .stl data:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d626fd1e1b6a37e5beec54a84401dd94cf7ea335.jpeg" data-download-href="/uploads/short-url/uytI7EkPKbj6wqITbBBSYmpFcep.jpg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d626fd1e1b6a37e5beec54a84401dd94cf7ea335_2_281x500.jpg" alt="3" data-base62-sha1="uytI7EkPKbj6wqITbBBSYmpFcep" width="281" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d626fd1e1b6a37e5beec54a84401dd94cf7ea335_2_281x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d626fd1e1b6a37e5beec54a84401dd94cf7ea335_2_421x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d626fd1e1b6a37e5beec54a84401dd94cf7ea335_2_562x1000.jpg 2x" data-dominant-color="9B92AC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1832×3258 2.8 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In ‘volumes’ module, the stl volume does not appear ('‘unnamed series’ is the dicom data).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64c9344dec818e9f969d7b1944529647c6d412c0.jpeg" data-download-href="/uploads/short-url/enAPas020si7eUrkYO81AIkha7K.jpg?dl=1" title="4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64c9344dec818e9f969d7b1944529647c6d412c0_2_281x500.jpg" alt="4" data-base62-sha1="enAPas020si7eUrkYO81AIkha7K" width="281" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64c9344dec818e9f969d7b1944529647c6d412c0_2_281x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64c9344dec818e9f969d7b1944529647c6d412c0_2_421x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64c9344dec818e9f969d7b1944529647c6d412c0_2_562x1000.jpg 2x" data-dominant-color="8A8789"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">1832×3258 2.93 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks for your help,<br>
Best regards,</p>
<p>Davide</p>

---

## Post #2 by @pieper (2018-06-07 18:37 UTC)

<p>Hi Davide -</p>
<p>What you would need to do is import the STL as a</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2804936f8d7b074e333318882f4ba7cf25371fd.jpeg" data-download-href="/uploads/short-url/u2b7sjYjylJq8ez4pMgGFed1a2h.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d2804936f8d7b074e333318882f4ba7cf25371fd_2_690x97.jpg" alt="image" data-base62-sha1="u2b7sjYjylJq8ez4pMgGFed1a2h" width="690" height="97" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d2804936f8d7b074e333318882f4ba7cf25371fd_2_690x97.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d2804936f8d7b074e333318882f4ba7cf25371fd_2_1035x145.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2804936f8d7b074e333318882f4ba7cf25371fd.jpeg 2x" data-dominant-color="F0F0F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1055×149 29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Then select it in the Segmentations module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/5715cbe8c30670e5afe7ac1adba1be06b73983d6.jpeg" data-download-href="/uploads/short-url/cqoeNMSun3JYLRONcbITM7mnTIa.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5715cbe8c30670e5afe7ac1adba1be06b73983d6_2_690x472.jpg" alt="image" data-base62-sha1="cqoeNMSun3JYLRONcbITM7mnTIa" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5715cbe8c30670e5afe7ac1adba1be06b73983d6_2_690x472.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/5715cbe8c30670e5afe7ac1adba1be06b73983d6.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/5715cbe8c30670e5afe7ac1adba1be06b73983d6.jpeg 2x" data-dominant-color="DFE0E0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">721×494 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Then export to a labelmap:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef6013fc61993e078eccb16d7b63c6bbe6b8a469.jpeg" data-download-href="/uploads/short-url/y9BXCYxMcmkhReSY0CoamarwuoN.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef6013fc61993e078eccb16d7b63c6bbe6b8a469_2_690x199.jpg" alt="image" data-base62-sha1="y9BXCYxMcmkhReSY0CoamarwuoN" width="690" height="199" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef6013fc61993e078eccb16d7b63c6bbe6b8a469_2_690x199.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef6013fc61993e078eccb16d7b63c6bbe6b8a469.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef6013fc61993e078eccb16d7b63c6bbe6b8a469.jpeg 2x" data-dominant-color="E4E3E3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">798×231 50.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>From there you can use the labelmap with LandmarkRegistration.</p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @DavideBassano (2018-06-08 07:00 UTC)

<p>Hi Steve,</p>
<p>thank you for your answers, but I have a problem: I can’t import my STL as “segmentation”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0672ac77d9a839d769adad8ea3c91e37695db68.jpeg" data-download-href="/uploads/short-url/tJClB5Rd0G7HOV1JpxM0kkjIyiQ.jpg?dl=1" title="IMG_20180608_085747" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0672ac77d9a839d769adad8ea3c91e37695db68_2_690x387.jpg" alt="IMG_20180608_085747" data-base62-sha1="tJClB5Rd0G7HOV1JpxM0kkjIyiQ" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0672ac77d9a839d769adad8ea3c91e37695db68_2_690x387.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0672ac77d9a839d769adad8ea3c91e37695db68_2_1035x580.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0672ac77d9a839d769adad8ea3c91e37695db68_2_1380x774.jpg 2x" data-dominant-color="989197"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20180608_085747</span><span class="informations">3258×1832 2.37 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How is It possible?</p>
<p>Thanks,<br>
Cheers,</p>
<p>Davide</p>

---

## Post #4 by @muratmaga (2018-06-08 07:15 UTC)

<p>To convert your stl to a segmentation, you need to use the segmentation module import/export</p>
<p>Mail](<a href="https://go.microsoft.com/fwlink/?LinkId=550986" rel="nofollow noopener">https://go.microsoft.com/fwlink/?LinkId=550986</a>) for Windows 10</p>

---

## Post #5 by @Fang (2018-06-08 10:59 UTC)

<p>Hi,</p>
<p>I can export the labelmap as the suggestion from Steve’s.<br>
However, I got a problem which it does not show any image as figure below this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62159c8ecddfc97cce68ffc1c1e1b7f5e55354cb.jpeg" data-download-href="/uploads/short-url/dZH5ROxyjVbUnwwcTGIUAyv8uN5.JPG?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62159c8ecddfc97cce68ffc1c1e1b7f5e55354cb_2_636x500.JPG" alt="Capture" data-base62-sha1="dZH5ROxyjVbUnwwcTGIUAyv8uN5" width="636" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62159c8ecddfc97cce68ffc1c1e1b7f5e55354cb_2_636x500.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62159c8ecddfc97cce68ffc1c1e1b7f5e55354cb_2_954x750.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62159c8ecddfc97cce68ffc1c1e1b7f5e55354cb_2_1272x1000.JPG 2x" data-dominant-color="2C2E35"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1646×1292 71.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @Fang (2018-06-08 11:18 UTC)

<p>Hi,</p>
<p>That my faults. It already appeared.<br>
But, I still cannot use the pre-structure function.<br>
I desire to segment each part of the tooth.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad5f3d85e0e47d99de49fd616490511cf1d86b91.jpeg" data-download-href="/uploads/short-url/oJIExmBoKR0u5iXgobTCM7p49EJ.JPG?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad5f3d85e0e47d99de49fd616490511cf1d86b91_2_690x350.JPG" alt="Capture1" data-base62-sha1="oJIExmBoKR0u5iXgobTCM7p49EJ" width="690" height="350" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad5f3d85e0e47d99de49fd616490511cf1d86b91_2_690x350.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad5f3d85e0e47d99de49fd616490511cf1d86b91_2_1035x525.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad5f3d85e0e47d99de49fd616490511cf1d86b91_2_1380x700.JPG 2x" data-dominant-color="74777A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">2560×1299 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2018-06-08 14:52 UTC)

<p>It should not be necessary to use the legacy Editor module anymore. It is replaced by the Segment editor module.</p>
<p>See follow-up in this topic: <a href="https://discourse.slicer.org/t/why-i-cannot-per-structure-volume/3124">Why I cannot Per-Structure Volume</a></p>

---
