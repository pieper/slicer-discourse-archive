---
topic_id: 41472
title: "Skull Stripping Brain Extraction For Canine Brains With Hdbr"
date: 2025-02-03
url: https://discourse.slicer.org/t/41472
---

# Skull stripping/ Brain Extraction for canine brains with HDBrainExtraction a/o SwissSkullStripper

**Topic ID**: 41472
**Date**: 2025-02-03
**URL**: https://discourse.slicer.org/t/skull-stripping-brain-extraction-for-canine-brains-with-hdbrainextraction-a-o-swissskullstripper/41472

---

## Post #1 by @ma_apan (2025-02-03 21:04 UTC)

<p>I have to extract canine brains from around 60 patients in T1w 3D MRI-images. I tried both options</p>
<ul>
<li>SwissSkullstripper doesn’t extract all brain, but only a small part of the brain (image 1)</li>
<li>HD Brain Extraction Tool works better, but doesn’t extract all brain as well (image 2)</li>
</ul>
<p>I tried the HD Brain Extraction Tool with a atlas volume and atlas mask, which I manually segmented beforehand.</p>
<p>image 1: green is the atlas mask segmentation, blue is the brain extraction by Swiss SkullStripping<br>
image 2: white is brain extraction by HD Brain Extraction</p>
<p>I am thankful for any tipps on how to extract the brain properly or any additional settings that may help. Thanks in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/392d1cbeff3e1d423a1bc85b507162542ecbd675.jpeg" data-download-href="/uploads/short-url/89NRQjUGfpf9zkhix3gscE3gaHP.jpeg?dl=1" title="Bildschirmfoto 2025-02-03 um 12.19.54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/392d1cbeff3e1d423a1bc85b507162542ecbd675_2_690x416.jpeg" alt="Bildschirmfoto 2025-02-03 um 12.19.54" data-base62-sha1="89NRQjUGfpf9zkhix3gscE3gaHP" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/392d1cbeff3e1d423a1bc85b507162542ecbd675_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/392d1cbeff3e1d423a1bc85b507162542ecbd675_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/392d1cbeff3e1d423a1bc85b507162542ecbd675_2_1380x832.jpeg 2x" data-dominant-color="9C9CA2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2025-02-03 um 12.19.54</span><span class="informations">1524×919 251 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74427c7ea303688c2ccdd0754137c5867795735e.jpeg" data-download-href="/uploads/short-url/gAtPDomS6WpwBh9KDmH7YnQwJUW.jpeg?dl=1" title="image1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74427c7ea303688c2ccdd0754137c5867795735e_2_690x425.jpeg" alt="image1" data-base62-sha1="gAtPDomS6WpwBh9KDmH7YnQwJUW" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74427c7ea303688c2ccdd0754137c5867795735e_2_690x425.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74427c7ea303688c2ccdd0754137c5867795735e_2_1035x637.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74427c7ea303688c2ccdd0754137c5867795735e_2_1380x850.jpeg 2x" data-dominant-color="979EA4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image1</span><span class="informations">1515×935 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
