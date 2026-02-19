---
topic_id: 37009
title: "Weird Results With Dental Segmentator"
date: 2024-06-25
url: https://discourse.slicer.org/t/37009
---

# Weird results with dental segmentator

**Topic ID**: 37009
**Date**: 2024-06-25
**URL**: https://discourse.slicer.org/t/weird-results-with-dental-segmentator/37009

---

## Post #1 by @mohammed_alshakhas (2024-06-25 17:08 UTC)

<p><a class="mention" href="/u/thibault_pelletier">@Thibault_Pelletier</a><br>
weird results with dental segmentator<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a30bb840895185676509943f3d03b4fb914227f.jpeg" data-download-href="/uploads/short-url/3JGP1YNfB8kZA98Cgfio2YflE6z.jpeg?dl=1" title="Screenshot 2024-06-25 191912" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a30bb840895185676509943f3d03b4fb914227f_2_690x370.jpeg" alt="Screenshot 2024-06-25 191912" data-base62-sha1="3JGP1YNfB8kZA98Cgfio2YflE6z" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a30bb840895185676509943f3d03b4fb914227f_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a30bb840895185676509943f3d03b4fb914227f_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a30bb840895185676509943f3d03b4fb914227f_2_1380x740.jpeg 2x" data-dominant-color="A2A29C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-06-25 191912</span><span class="informations">1920×1032 96.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
, i had it outside ct and looks awkward</p>

---

## Post #2 by @Thibault_Pelletier (2024-06-26 05:44 UTC)

<p>Hi <a class="mention" href="/u/mohammed_alshakhas">@mohammed_alshakhas</a>,</p>
<p>Thanks for reaching out.</p>
<p>The segmentation you are displaying may not correspond to the CT currently displayed in the 2D views.</p>
<p>For instance, when loading the CBCT dental surgery sample data, two CTs are loaded at the same time : Post and Pre dental surgeries.</p>
<p>You can change what is displayed from the data module using the eye icon next to the data or the 2D view from the drop down menu :</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a44a883a5a791c1feb3b3bbe3485968e51eea6f9.png" alt="image" data-base62-sha1="nrnZlKedikgUzjLLxRJ32V4Z3E5" width="555" height="291"></p>

---

## Post #3 by @mohammed_alshakhas (2024-06-26 17:03 UTC)

<p>i actually only loaded one volume . i did many autosegmentations .<br>
i tried to run it twice for the same voume . now i just had the same issues with different patient with different volume . im betting its a volume realated but not sure .<br>
thanks</p>

---

## Post #4 by @mohammed_alshakhas (2024-07-09 16:01 UTC)

<p>same issue with new volume</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ef9ebacc4659e0cfa3c87b408be9ca14ac06eff.jpeg" data-download-href="/uploads/short-url/6HzpNmuwdgA1F5gC0VshJklzwcv.jpeg?dl=1" title="Screenshot 2024-07-09 190038" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ef9ebacc4659e0cfa3c87b408be9ca14ac06eff_2_690x487.jpeg" alt="Screenshot 2024-07-09 190038" data-base62-sha1="6HzpNmuwdgA1F5gC0VshJklzwcv" width="690" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ef9ebacc4659e0cfa3c87b408be9ca14ac06eff_2_690x487.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ef9ebacc4659e0cfa3c87b408be9ca14ac06eff_2_1035x730.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ef9ebacc4659e0cfa3c87b408be9ca14ac06eff_2_1380x974.jpeg 2x" data-dominant-color="727590"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-07-09 190038</span><span class="informations">1920×1357 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @pieper (2024-07-09 17:46 UTC)

<p>Probably the segmentation is not being put in the same transform.</p>

---

## Post #6 by @mohammed_alshakhas (2024-07-09 18:10 UTC)

<p>there is no transform , and if you noticed it looks compressed and distorted. i did very low quality scans before and was perfect . so im wondering whats the cause for this</p>

---
