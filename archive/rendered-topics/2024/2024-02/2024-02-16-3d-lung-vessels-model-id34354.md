---
topic_id: 34354
title: "3D Lung Vessels Model"
date: 2024-02-16
url: https://discourse.slicer.org/t/34354
---

# 3d lung vessels model

**Topic ID**: 34354
**Date**: 2024-02-16
**URL**: https://discourse.slicer.org/t/3d-lung-vessels-model/34354

---

## Post #1 by @Vikram (2024-02-16 03:51 UTC)

<p>I want to create 3d lung vessels tree model any one can help me please</p>

---

## Post #2 by @Matteboo (2024-02-19 10:18 UTC)

<p>If you want to segment the lung vessel of a CT, the latest version of total segmentator offer a lung vessel segmentation task.<br>
However, as far as I’m aware, it does not check for connectivity of the tree so you might have to clean the results a little bit<br>
If you just want one example of lung vessel tree, I suggest doing the above on some of the sample data</p>

---

## Post #3 by @Vikram (2024-02-21 00:34 UTC)

<p>can you please send me the link to the latest version of total segmentation.<br>
because i need lung vessels tree model for 3d printing ,</p>

---

## Post #4 by @Matteboo (2024-02-21 10:51 UTC)

<p>It’s an extension, It’s available from the extension manager</p>

---

## Post #5 by @lassoan (2024-03-16 11:50 UTC)

<p>Slicer now offers fully automated lung, lobes, airways, and vessel segmentation. There are several active discussions about it see for example here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="34869">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/klc/48/68248_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/using-monai-label-to-fine-tune-the-vessel-segmentation/34869">Using MONAI label to fine tune the vessel segmentation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, I have acheived robust and satisfactory segmentation result when using lungCTsegmenter before. 
[image] 
However, if i use other samples(LIDC-IDRI dataset), most of the results have lung/vessel leaks. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/929651905bdbb6a62bac9a2c572fb8ca1061f3ae.jpeg" data-download-href="/uploads/short-url/kULLxEGek4kQni89dZCupTiHZHE.jpeg?dl=1" title="WhatsApp Image 2024-03-13 at 23.28.56_0857f222" rel="noopener nofollow ugc">[WhatsApp Image 2024-03-13 at 23.28.56_0857f222]</a> 
<a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7730cea4c95a27e8e88240af9589a38d0342c4de.jpeg" data-download-href="/uploads/short-url/h0po3cTIUBXUf5aeRMqnGMtmEFM.jpeg?dl=1" title="WhatsApp Image 2024-03-13 at 23.29.21_1eecf52d" rel="noopener nofollow ugc">[WhatsApp Image 2024-03-13 at 23.29.21_1eecf52d]</a> 
Should I use MONAI label to finetune the vessel segmentation part, or this is not a good use case? Since I watch this demo: 
  <a href="https://www.youtube.com/watch?v=wtiEe_jiUzg&amp;t=5531s" target="_blank" rel="noopener">
    [MONAI Label Workshop - Project Week 37]
  </a>


(1:35:27) and t…
  </blockquote>
</aside>


---
