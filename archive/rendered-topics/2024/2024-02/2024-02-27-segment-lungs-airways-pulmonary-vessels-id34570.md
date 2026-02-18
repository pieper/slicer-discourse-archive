# Segment lungs, airways, pulmonary vessels

**Topic ID**: 34570
**Date**: 2024-02-27
**URL**: https://discourse.slicer.org/t/segment-lungs-airways-pulmonary-vessels/34570

---

## Post #1 by @Giulia_Gamberini (2024-02-27 14:22 UTC)

<p>Dear all, I am trying to segment lungs, airways and both pulmonary vein and artery. Could you please list the procedure you follow to obtain this results?<br>
Many thanks</p>

---

## Post #2 by @lassoan (2024-03-16 11:45 UTC)

<p>In short: Slicer now offers fully automated lung, lobes, airways, and vessel segmentation. There are several active discussions about it see for example here:</p>
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

## Post #3 by @Killmaro (2024-04-28 13:47 UTC)

<p>Hi All</p>
<p>I’ve tried successfully MONAI model for segmenting the arterial pulmonary tree on one of the CT models provided by Slicer. Here are the results (without filtering). Is there a way to clean this segmentation by removing all isolated pieces without using the manual scissor tool?</p>
<p>Thank you in advance for your help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e6714a8979c39eb978f7b1dd4d3dfe151bdabe1.jpeg" data-download-href="/uploads/short-url/kjKEji0Q1FRisHYKJ7NUTavednr.jpeg?dl=1" title="Capture d’écran 2024-04-28 à 15.39.45" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e6714a8979c39eb978f7b1dd4d3dfe151bdabe1_2_690x473.jpeg" alt="Capture d’écran 2024-04-28 à 15.39.45" data-base62-sha1="kjKEji0Q1FRisHYKJ7NUTavednr" width="690" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e6714a8979c39eb978f7b1dd4d3dfe151bdabe1_2_690x473.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e6714a8979c39eb978f7b1dd4d3dfe151bdabe1_2_1035x709.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e6714a8979c39eb978f7b1dd4d3dfe151bdabe1_2_1380x946.jpeg 2x" data-dominant-color="7D90C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-04-28 à 15.39.45</span><span class="informations">1920×1318 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @soothsayer (2024-11-24 21:15 UTC)

<p>I think you can use the “islands” tool. And choose “remove small islands” with a Minimum size of pixels for islands.</p>

---
