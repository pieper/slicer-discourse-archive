---
topic_id: 21236
title: "Different Semi Automatic Segmentation Method On Pet Image"
date: 2021-12-27
url: https://discourse.slicer.org/t/21236
---

# Different semi-automatic segmentation method on PET image

**Topic ID**: 21236
**Date**: 2021-12-27
**URL**: https://discourse.slicer.org/t/different-semi-automatic-segmentation-method-on-pet-image/21236

---

## Post #1 by @MPhilip (2021-12-27 12:35 UTC)

<p>Operating system: Windows 11 home<br>
Slicer version: Slicer 4.13.0-2021-12-15<br>
Hi,<br>
I have a few questions relating to applying different segmentation method on a PET image.</p>
<ol>
<li>I have applied a few segmentation methods on my PET image and would like to extract features from all those segments together into a table. Please have a look at the different segments. I had to export the segments to labelmap to extract features. I was manually selecting each segment and calculating the features which takes time.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eafed7e0329d17ec43e1af5e013b6a3def61c0e4.png" data-download-href="/uploads/short-url/xwRJ5AOxSGT9G9QcH4UC9KNw5WQ.png?dl=1" title="different seg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eafed7e0329d17ec43e1af5e013b6a3def61c0e4_2_690x358.png" alt="different seg" data-base62-sha1="xwRJ5AOxSGT9G9QcH4UC9KNw5WQ" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eafed7e0329d17ec43e1af5e013b6a3def61c0e4_2_690x358.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eafed7e0329d17ec43e1af5e013b6a3def61c0e4_2_1035x537.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eafed7e0329d17ec43e1af5e013b6a3def61c0e4_2_1380x716.png 2x" data-dominant-color="D2D2D4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">different seg</span><span class="informations">1913×993 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>Also while calculating segments using <strong>segment statistics</strong> module, I could see different options like labelmap statistics, scalar volume statistics, closed surface statistics and PET volume statistics. I am confused about which one to select because, in the <strong>'input</strong> ’ &gt; <strong>segmentation</strong> option, I can only see ‘closed surface’ segments and not labelmap.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/040ea5402fcf6a2369a707027aa010fe97f353eb.png" data-download-href="/uploads/short-url/zThQ5nfz0fwkVvUuGuqqofkEXN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/040ea5402fcf6a2369a707027aa010fe97f353eb.png" alt="image" data-base62-sha1="zThQ5nfz0fwkVvUuGuqqofkEXN" width="690" height="318" data-dominant-color="F7F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">755×348 6.58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="3">
<li>Is it possible to integrate results of segment statistics with output of radiomics module into a single table as I have 100 patients on which I have to repeat the same procedure and a single table for each patient would be easy to handle (calculated for all segments)</li>
<li>Is it possible to see the tumours outlined using different segmentation method on the PET image so the differences in tumour outline by different methods can be easily seen?</li>
<li>I would also like to know the default resampled voxel size value Log kernel size and bin width available under the ‘Radiomics’ module. I could see that 3D slicer calculates the features even if I don’t enter a resampled voxel size value.<br>
Thanks in advance</li>
</ol>

---
