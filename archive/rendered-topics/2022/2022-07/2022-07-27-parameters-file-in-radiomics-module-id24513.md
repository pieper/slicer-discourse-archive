---
topic_id: 24513
title: "Parameters File In Radiomics Module"
date: 2022-07-27
url: https://discourse.slicer.org/t/24513
---

# Parameters file in Radiomics module

**Topic ID**: 24513
**Date**: 2022-07-27
**URL**: https://discourse.slicer.org/t/parameters-file-in-radiomics-module/24513

---

## Post #1 by @Joyce (2022-07-27 03:17 UTC)

<p>Operating system:Win 10<br>
Slicer version:5.0.3<br>
Expected behavior:Extract features with parameters file<br>
Actual behavior:UnicodeDecodeError</p>
<p>Hello everyone,<br>
I want to use Radiomics module to extracrt features. I want to set resegmentRange:[-1000,1000] and binCount: 64, so I wrote this Parameters file. However, I uploaded the file in the Radiomics module and clicked ‘Apply’, it showed UnicodeDecodeError.</p>
<p>The following figures showed the Parameters file and the screenshot of the Radiomics module.</p>
<p>Did I write something incorrect in the Parameters file? How could I fix it? If the Parameter file is correct, how could I solve this problem?<br>
Many thanks in advance!!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e032c6b1b3980a552a41c969867bda92b9b57cf.png" data-download-href="/uploads/short-url/mxQeQNSegNOuAhZdL10TpdwfT1d.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e032c6b1b3980a552a41c969867bda92b9b57cf_2_690x330.png" alt="image" data-base62-sha1="mxQeQNSegNOuAhZdL10TpdwfT1d" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e032c6b1b3980a552a41c969867bda92b9b57cf_2_690x330.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e032c6b1b3980a552a41c969867bda92b9b57cf_2_1035x495.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e032c6b1b3980a552a41c969867bda92b9b57cf_2_1380x660.png 2x" data-dominant-color="F3F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×920 40.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/110c3d59fe2a883a9ea882a09c15849fe0d260a7.png" data-download-href="/uploads/short-url/2qOl6fFIlBvLJyWVBcQf7oIgorZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/110c3d59fe2a883a9ea882a09c15849fe0d260a7_2_690x369.png" alt="image" data-base62-sha1="2qOl6fFIlBvLJyWVBcQf7oIgorZ" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/110c3d59fe2a883a9ea882a09c15849fe0d260a7_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/110c3d59fe2a883a9ea882a09c15849fe0d260a7_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/110c3d59fe2a883a9ea882a09c15849fe0d260a7_2_1380x738.png 2x" data-dominant-color="DFDEDE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1028 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2022-07-27 14:33 UTC)

<p>Try using only ascii in the parameters file.  It looks like these quotes aren’t compatible.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40757a3c5a2b76286a73129572e0c353eda50d7f.png" alt="image" data-base62-sha1="9cefErmxHIhAEqmoUDt8XUV9ghp" width="237" height="55"></p>

---

## Post #3 by @Joyce (2022-07-28 02:57 UTC)

<p>OMG!<br>
Thank you very much for your help!<br>
I could extract the features successfully <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=12" title=":blush:" class="emoji" alt=":blush:" loading="lazy" width="20" height="20"><br>
Thanks again. Have a nice day!</p>

---
