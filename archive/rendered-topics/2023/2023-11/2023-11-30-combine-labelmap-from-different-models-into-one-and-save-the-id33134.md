---
topic_id: 33134
title: "Combine Labelmap From Different Models Into One And Save The"
date: 2023-11-30
url: https://discourse.slicer.org/t/33134
---

# Combine labelmap from different models into one and save the data

**Topic ID**: 33134
**Date**: 2023-11-30
**URL**: https://discourse.slicer.org/t/combine-labelmap-from-different-models-into-one-and-save-the-data/33134

---

## Post #1 by @LLL (2023-11-30 04:47 UTC)

<p>Hi,</p>
<p>I have several surface models (in .stl format) and would like to create one single labelmap which contains all individual models. Here’s is a screenshot for the model.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e1a709f8871f4710439ff127a05ec5f2c4884d5.jpeg" data-download-href="/uploads/short-url/dqtwPttGhD7DJ8GngYhuOL7jCjH.jpeg?dl=1" title="Combine lablemap from diffeernt stl models into One" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e1a709f8871f4710439ff127a05ec5f2c4884d5_2_690x373.jpeg" alt="Combine lablemap from diffeernt stl models into One" data-base62-sha1="dqtwPttGhD7DJ8GngYhuOL7jCjH" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e1a709f8871f4710439ff127a05ec5f2c4884d5_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e1a709f8871f4710439ff127a05ec5f2c4884d5_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e1a709f8871f4710439ff127a05ec5f2c4884d5_2_1380x746.jpeg 2x" data-dominant-color="7A797B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Combine lablemap from diffeernt stl models into One</span><span class="informations">1920×1040 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Currently I can only export the labelmap individually as .nrrd file. However, it lost the relative coordination information between the models. I also tried to merge the models but:</p>
<ol>
<li>only two models can be merged at a time;</li>
<li>once merged, colour (label) assigned to corresponding model get lost.<br>
Before Merging:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf1f98dba0af8c3105612857cb7c775690f60a2a.png" data-download-href="/uploads/short-url/tyix2juYG9sCY04Nf7EIyVfdsAq.png?dl=1" title="Before merging" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf1f98dba0af8c3105612857cb7c775690f60a2a_2_690x388.png" alt="Before merging" data-base62-sha1="tyix2juYG9sCY04Nf7EIyVfdsAq" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf1f98dba0af8c3105612857cb7c775690f60a2a_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf1f98dba0af8c3105612857cb7c775690f60a2a_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf1f98dba0af8c3105612857cb7c775690f60a2a_2_1380x776.png 2x" data-dominant-color="747377"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Before merging</span><span class="informations">2560×1440 496 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
After Merging:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcf1c3edf0cc1e92acc2c7145b9438485febc775.png" data-download-href="/uploads/short-url/qXtK99vvmY94R1fxb1nzDSlpmtf.png?dl=1" title="After merging" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcf1c3edf0cc1e92acc2c7145b9438485febc775_2_690x375.png" alt="After merging" data-base62-sha1="qXtK99vvmY94R1fxb1nzDSlpmtf" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcf1c3edf0cc1e92acc2c7145b9438485febc775_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcf1c3edf0cc1e92acc2c7145b9438485febc775_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcf1c3edf0cc1e92acc2c7145b9438485febc775_2_1380x750.png 2x" data-dominant-color="787879"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">After merging</span><span class="informations">2560×1392 449 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p>May I ask how I can combine all the label maps into one and export it into some format that can be loaded into Matlab?</p>
<p>Many Thanks!</p>

---
