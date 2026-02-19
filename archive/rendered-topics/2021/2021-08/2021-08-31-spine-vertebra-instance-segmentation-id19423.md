---
topic_id: 19423
title: "Spine Vertebra Instance Segmentation"
date: 2021-08-31
url: https://discourse.slicer.org/t/19423
---

# Spine Vertebra Instance Segmentation

**Topic ID**: 19423
**Date**: 2021-08-31
**URL**: https://discourse.slicer.org/t/spine-vertebra-instance-segmentation/19423

---

## Post #1 by @oguzcanbekar (2021-08-31 04:49 UTC)

<p>Hello everyone, I’m a graduate student and working on medical images. Nowadays I am trying to segment my CT Spine data as instance segmentation. I tried to use 3D Slicer for this purpose, but I encountered many problems. For example, the software froze many times and I could not save my results. I also tried different extensions but could not find the best and fastest path. I want your help and opinion… I need to finish the segmentation as soon as possible. I’m going to post a photo of what my final goal was when I finished. I hope you can suggest me a quick way to follow this. Thank you very much in advance.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c6c5ac7baa8984432186085dd44541ee08e8de5.jpeg" data-download-href="/uploads/short-url/k2eZF1Mf1XaQMlokELRQU0dzGLz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c6c5ac7baa8984432186085dd44541ee08e8de5_2_690x373.jpeg" alt="image" data-base62-sha1="k2eZF1Mf1XaQMlokELRQU0dzGLz" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c6c5ac7baa8984432186085dd44541ee08e8de5_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c6c5ac7baa8984432186085dd44541ee08e8de5_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c6c5ac7baa8984432186085dd44541ee08e8de5_2_1380x746.jpeg 2x" data-dominant-color="8B8A91"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1039 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-08-31 18:33 UTC)

<p>You are using a very old Slicer version. Upgrade to at least the latest stable version. It might not solve application freezing, because that is most likely due to that you are running out of memory. You may need downsample your input image (but then you may lose some small details), increase virtual memory setting in your operating system (but then the software may slow down when your memory usage increases), or add more RAM to your computer (but it costs money and if you computer is old then it might not be feasible, and you may be better off buying a new computer).</p>
<p>Once you took care of the memory usage issue, you can segment the spine very quickly. You can either use classic methods, such as “Grow from seeds” effect with intensity masking followed by hole filling; or deep learning based methods, for example in MONAILabel. See more information in this post:</p>
<aside class="quote quote-modified" data-post="4" data-topic="19143">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/mask-volume-query/19143/4">Vertebra segmentation for volume masking</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    What visualization mode is that you could not set up in Slicer? 

You can save the whole image as well. 

Yes, of course. You can have unlimited number of volumes, segmentations, segments in the scene and you can export all of them to files. 

Slicer has many tools for spine segmentation. 
For example, using classic tools, you can quickly segment the entire spinal column (each vertebra in a separate segment) using Grow from seeds effect, and filling internal holes using <a href="https://gist.github.com/lassoan/0f45db8bae792ea19ccad36ceefbf52d">this code snippet</a>. 
Ther…
  </blockquote>
</aside>


---

## Post #3 by @oguzcanbekar (2021-09-08 01:55 UTC)

<blockquote>
<p>You are using a very old Slicer version. Upgrade to at least the latest stable version. It might not solve application freezing, because that is most likely due to that you are running out of memory.</p>
</blockquote>
<p>Yes I know this stituation but unfortunately when I am trying to segment my data by GrowFromSeeds method the 4.11 version doesn`t work stably. Because of that I was trying to use old version.</p>
<blockquote>
<p>You may need downsample your input image (but then you may lose some small details), increase virtual memory setting in your operating system (but then the software may slow down when your memory usage increases), or add more RAM to your computer (but it costs money and if you computer is old then it might not be feasible, and you may be better off buying a new computer).</p>
</blockquote>
<p>Yes you are right thanks for suggestion probably I need more powerful stuff.</p>
<blockquote>
<p>Once you took care of the memory usage issue, you can segment the spine very quickly. You can either use classic methods, such as “Grow from seeds” effect with intensity masking followed by hole filling; or deep learning based methods, for example in MONAILabel. See more information in this post:</p>
</blockquote>
<p>After your suggestion I became more close to GrowFromSeeds method but unfourtanetly it still requires at least 1 hour for each patient and also when I look forward to MONAILabel as far as I understand they just allow segment data by just foreground and background but as you see I have to segment my spine data vertebra by vertebra. At that point if you don`t mind I would like to ask after segment just all vertebras and background segmentation is there any way to label them manually? I hope I could explain myself clearly. Thank you very much in advance…</p>

---

## Post #4 by @muratmaga (2021-09-08 02:02 UTC)

<aside class="quote no-group" data-username="oguzcanbekar" data-post="3" data-topic="19423">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/oguzcanbekar/48/12174_2.png" class="avatar"> oguzcanbekar:</div>
<blockquote>
<p>Yes I know this stituation but unfortunately when I am trying to segment my data by GrowFromSeeds method the 4.11 version doesn`t work stably. Because of that I was trying to use old version.</p>
</blockquote>
</aside>
<p>That is not correct, since there are many people who are using the grow from the seed in the current stable successfully. Please download and retry with the latest stable.</p>
<aside class="quote no-group" data-username="oguzcanbekar" data-post="3" data-topic="19423">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/oguzcanbekar/48/12174_2.png" class="avatar"> oguzcanbekar:</div>
<blockquote>
<p>After your suggestion I became more close to GrowFromSeeds method but unfourtanetly it still requires at least 1 hour for each patient</p>
</blockquote>
</aside>
<p>Again, this is far too long. We use grow from the seeds on small animal microCT scans that is almost an order of magnitude larger in volume size compared to medical scans, and it takes minutes. Again, try with the latest stable and if these issues persist, you might be trying to use  a computer that just simply doesn’t have enough resources (RAM and CPU cores).</p>
<p>If the issue persists with the latest stable, downsample and try again. If things work out faster, than lack of RAM on your computer is the culprit for slow computation.</p>

---

## Post #5 by @lassoan (2021-09-08 02:26 UTC)

<p><a class="mention" href="/u/oguzcanbekar">@oguzcanbekar</a> We made spine segmentation using masked grow from seeds magnitudes faster in the latest Slicer Preview Release (there was a bug in Slicer-4.11 that slowed down updates in this specific use case).</p>

---
