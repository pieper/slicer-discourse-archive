---
topic_id: 25723
title: "Volume Renderig Vis Segment Editor Different Models"
date: 2022-10-16
url: https://discourse.slicer.org/t/25723
---

# Volume renderig vis segment editor - different models

**Topic ID**: 25723
**Date**: 2022-10-16
**URL**: https://discourse.slicer.org/t/volume-renderig-vis-segment-editor-different-models/25723

---

## Post #1 by @eNable_Polska (2022-10-16 16:00 UTC)

<p>How to fix the error in ct dicom, like you see<br>
The same examination, orange - volume rendering, yellow segment editor.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36648ea2423aeeef5c3348254fc96a2724bd7f23.jpeg" data-download-href="/uploads/short-url/7Lbe1fRzbY956vQOuFGMAt52Qb9.jpeg?dl=1" title="slicer_error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36648ea2423aeeef5c3348254fc96a2724bd7f23_2_690x436.jpeg" alt="slicer_error" data-base62-sha1="7Lbe1fRzbY956vQOuFGMAt52Qb9" width="690" height="436" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36648ea2423aeeef5c3348254fc96a2724bd7f23_2_690x436.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36648ea2423aeeef5c3348254fc96a2724bd7f23_2_1035x654.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36648ea2423aeeef5c3348254fc96a2724bd7f23_2_1380x872.jpeg 2x" data-dominant-color="A98499"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_error</span><span class="informations">1774×1123 270 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>win10, slicer 5.0.3,</p>

---

## Post #2 by @pieper (2022-10-16 16:04 UTC)

<p>Please provide some more detailed information about the data files you used and what steps led to this mismatch.</p>

---

## Post #3 by @eNable_Polska (2022-10-16 16:30 UTC)

<p>Here you are anonimized data</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/146iF1KnRu4DrPaEIJ8BbcLi0sP8QI9cU/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/146iF1KnRu4DrPaEIJ8BbcLi0sP8QI9cU/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/146iF1KnRu4DrPaEIJ8BbcLi0sP8QI9cU/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/146iF1KnRu4DrPaEIJ8BbcLi0sP8QI9cU/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">Series 004 [CT - Head 1 5 H70h].zip</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I imported the data to the slicer (dicom), opened the H70h series in the volume rendering module, as a result, I see an orange model, and now I open segment editor with the same data series, I used threshold and I got the model yellow.<br>
This is not the first time I see such an error in volume rendering,  Slicer does not report any error when importing data. We use Siemens machine</p>

---

## Post #4 by @pieper (2022-10-17 15:28 UTC)

<p>Thanks for sharing the anonymized data.  The issue here is that the scan was acquired with gantry tilt, so you need to do a few steps to work with it.  First you need to be sure that Acquisition geometry regularization is enabled in the settings.  Then when you load the data, there will be a transform created.  This is applied automatically in the Slice views but it’s not accounted for in the volume rendering, so you need to go to the Transform hierarchy tab of the Data module and select “harden”.  Then the two representations will line up.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06e0a38df066dfdd10f4f55ea799fd2bf83cc195.png" data-download-href="/uploads/short-url/YQ9o20uJc8vs2zy785UMk43Hhz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06e0a38df066dfdd10f4f55ea799fd2bf83cc195_2_690x495.png" alt="image" data-base62-sha1="YQ9o20uJc8vs2zy785UMk43Hhz" width="690" height="495" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06e0a38df066dfdd10f4f55ea799fd2bf83cc195_2_690x495.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06e0a38df066dfdd10f4f55ea799fd2bf83cc195.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06e0a38df066dfdd10f4f55ea799fd2bf83cc195.png 2x" data-dominant-color="E6E6E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">824×592 68.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ec3217041e9eaa5f9c9dd798fd04a4145692ee4.png" alt="image" data-base62-sha1="beLj6pghgMF4VjQZw9jhPtM6tBa" width="489" height="396"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e91dd417c6255524ecf45647c45a5053b00218f.jpeg" data-download-href="/uploads/short-url/bd3KQ2LARnReacIb1YOiLuvbyLd.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e91dd417c6255524ecf45647c45a5053b00218f_2_446x500.jpeg" alt="image" data-base62-sha1="bd3KQ2LARnReacIb1YOiLuvbyLd" width="446" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e91dd417c6255524ecf45647c45a5053b00218f_2_446x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e91dd417c6255524ecf45647c45a5053b00218f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e91dd417c6255524ecf45647c45a5053b00218f.jpeg 2x" data-dominant-color="536067"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">506×567 70.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @eNable_Polska (2022-10-17 19:15 UTC)

<p>Thank you very much for your help, now everything works fine</p>

---
