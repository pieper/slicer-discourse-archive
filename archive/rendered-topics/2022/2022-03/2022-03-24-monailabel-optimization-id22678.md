# MONAILABEL optimization

**Topic ID**: 22678
**Date**: 2022-03-24
**URL**: https://discourse.slicer.org/t/monailabel-optimization/22678

---

## Post #1 by @Mahdis_Khodadadi (2022-03-24 20:30 UTC)

<p>Hello everyone,</p>
<p>I am working on pelvic bone segmentation in CT scans using MONAILABEL and 3D Slicer.</p>
<p>I used the “deepedit” app and trained the network using 8 perfect manually segmented mask files and got 82% accuracy. After that, when I try to segment the rest of the images using the “auto segmentation” part, I don’t get good results at all. (I’ll attach a screenshot of a sample result)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1e2329d7517bec4438af21fb90e487b4ea3797e.jpeg" data-download-href="/uploads/short-url/weg3xXgAYy5UCoAeDmuIqmL63Nk.jpeg?dl=1" title="5.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1e2329d7517bec4438af21fb90e487b4ea3797e_2_690x362.jpeg" alt="5.PNG" data-base62-sha1="weg3xXgAYy5UCoAeDmuIqmL63Nk" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1e2329d7517bec4438af21fb90e487b4ea3797e_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1e2329d7517bec4438af21fb90e487b4ea3797e_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1e2329d7517bec4438af21fb90e487b4ea3797e.jpeg 2x" data-dominant-color="9D9DA2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5.PNG</span><span class="informations">1359×713 218 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Do you have any suggestions to improve the performance?<br>
How should I modify the hyperparameters of the network to get better results?</p>
<p>(I am using MONAI weekly and the latest version of 3D Slicer)</p>
<p>I’ll appreciate your support and ideas.<br>
Thank you.</p>

---

## Post #2 by @lassoan (2022-03-25 14:52 UTC)

<p>If you expect the cancellous bone regions (less dense regions in side the bone) to be filled then it is a fairly complex segmentation problem.</p>
<p>I don’t have much experience with deep-learning based segmentation methods, but most likely you need larger training data set than just 8 images. You might need a few hundred segmentations to train a network from scratch. You may also try transfer learning - starting from a model that is already pre-trained for bone segmentation in CT images.</p>

---

## Post #3 by @Mahdis_Khodadadi (2022-03-29 11:37 UTC)

<p>Thank you for your reply.</p>
<p>You are right. I need more labeled images which I don’t have.<br>
I guess I need to try transfer learning.</p>
<p>However, I have a few ideas to improve the performance such as modifying the hyperparameters in the Slicer interface, using the other app of MONAI (‘auto segmentation’), data preprocessing, and data augmentation.<br>
Do you think they would have a great impact?</p>

---

## Post #4 by @Alex_Vergara (2022-04-11 12:59 UTC)

<p>You can try to split your images into several images for training, then rotate/mirror them to create new sets, you can actually create thousands of trining images from just those eight image sets. That will solve your image generation problem. If you try this just write your progress.</p>

---

## Post #5 by @Mahdis_Khodadadi (2022-04-11 21:32 UTC)

<p>Thank you for the suggestion.<br>
I am actually trying to apply data augmentation to my labeled images. I will surely report in case of any progress.</p>

---
