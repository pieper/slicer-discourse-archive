---
topic_id: 34531
title: "How To Make The Segmented Teeth Look More Accurate And Aesth"
date: 2024-02-25
url: https://discourse.slicer.org/t/34531
---

# How to make the segmented teeth look more accurate and aesthetically pleasing?

**Topic ID**: 34531
**Date**: 2024-02-25
**URL**: https://discourse.slicer.org/t/how-to-make-the-segmented-teeth-look-more-accurate-and-aesthetically-pleasing/34531

---

## Post #1 by @Jake1 (2024-02-25 16:23 UTC)

<p>Operating system: win 10<br>
Slicer version: 5.6.1<br>
I am attempting to segment teeth, but due to the connectivity of teeth between the maxilla and mandible in my CBCT image files, I am facing challenges with effectively utilizing the ‘grow from seeds’ and ‘watershed’ functions. When I attempt to use them, the following issues arise：<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cda43afbcaa199572081792d2534a092ddbfb30.png" alt="6" data-base62-sha1="8GkhcTqxp9UBZxCEw7NgnINbu7e" width="487" height="371"><br>
So, I can only resort to using the ‘fill between slices’ function, but the teeth segmented this way have irregular shapes and numerous protrusions.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9dffa7e5d9fbbb6d633987ed431c7fd64c83d89.jpeg" data-download-href="/uploads/short-url/v5ptVQw6o8F51o0eFKNTV6B2Hj3.jpeg?dl=1" title="5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9dffa7e5d9fbbb6d633987ed431c7fd64c83d89_2_642x500.jpeg" alt="5" data-base62-sha1="v5ptVQw6o8F51o0eFKNTV6B2Hj3" width="642" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9dffa7e5d9fbbb6d633987ed431c7fd64c83d89_2_642x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9dffa7e5d9fbbb6d633987ed431c7fd64c83d89_2_963x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9dffa7e5d9fbbb6d633987ed431c7fd64c83d89.jpeg 2x" data-dominant-color="69676C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5</span><span class="informations">1154×898 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
What can I do to improve this situation?<br>
I sincerely look forward to your advice！<br>
Jake</p>

---

## Post #2 by @muratmaga (2024-02-25 17:46 UTC)

<p>If you increase the number of seeds and their placement, grow from the seeds will probably work better. Also make sure you are working with an isotropic dataset (i.e., voxel spacing is equal on each dimension), and if not resample to make it isotropic before you start the segmentation.</p>
<p>Regardless, before the model conversion, if you run a smoothing filter (like median fiter), the edges will not be as jagged.</p>

---

## Post #4 by @Jake1 (2024-04-03 11:05 UTC)

<p>Thank you very much for your advice. Just finished two months of busy emergency life, I didn’t have time to study 3D slicer, I will try your suggestions.</p>

---
