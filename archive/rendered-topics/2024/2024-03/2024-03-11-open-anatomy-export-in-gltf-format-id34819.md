# Open Anatomy Export in gltf format

**Topic ID**: 34819
**Date**: 2024-03-11
**URL**: https://discourse.slicer.org/t/open-anatomy-export-in-gltf-format/34819

---

## Post #1 by @Caterina (2024-03-11 10:43 UTC)

<p>Dear support,<br>
I used Lung CT Segmented and Analyzer extensions and I exported lung volume from segmentation and vessels from CT Analyzer in gltf format using Open Anatomy.<br>
The visualization in Slicer showed good details of lung with internal vessels.<br>
When I open the same gltf file with several online gltf viewer (<a href="https://gltf-viewer.donmccurdy.com/" rel="noopener nofollow ugc">https://gltf-viewer.donmccurdy.com/</a>, <a href="https://github.khronos.org/glTF-Sample-Viewer-Release/" class="inline-onebox" rel="noopener nofollow ugc">glTF Sample Viewer</a>), the models of lungs are correctly represented while the vessels models appeared as an unrealistic tetrahedral structure. what could be the problem?<br>
Thanks</p>

---

## Post #2 by @lassoan (2024-03-12 12:24 UTC)

<p>Could you please attach a few screenshots of the appearance in 3D Slicer and in the glTF viewers?</p>

---

## Post #3 by @Caterina (2024-03-12 12:33 UTC)

<p>Here the screenshot of the visualization using Slicer and the gltfviewer online.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df40278fce94f3085535013099e15a7f07a0bf47.jpeg" data-download-href="/uploads/short-url/vQXVqYS40rKTFiyoXfcCysB0HdB.jpeg?dl=1" title="Lung + Vessels" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df40278fce94f3085535013099e15a7f07a0bf47_2_516x500.jpeg" alt="Lung + Vessels" data-base62-sha1="vQXVqYS40rKTFiyoXfcCysB0HdB" width="516" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df40278fce94f3085535013099e15a7f07a0bf47_2_516x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df40278fce94f3085535013099e15a7f07a0bf47_2_774x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df40278fce94f3085535013099e15a7f07a0bf47_2_1032x1000.jpeg 2x" data-dominant-color="8C869B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Lung + Vessels</span><span class="informations">1394×1350 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/549b33ce731b74544289ac8d4b7e181dea8092b9.jpeg" data-download-href="/uploads/short-url/c4sCSpQUDz5n0mIpL5WEyV0HLNn.jpeg?dl=1" title="Screenshot 2024-03-12 alle 13.26.35" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/549b33ce731b74544289ac8d4b7e181dea8092b9_2_690x295.jpeg" alt="Screenshot 2024-03-12 alle 13.26.35" data-base62-sha1="c4sCSpQUDz5n0mIpL5WEyV0HLNn" width="690" height="295" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/549b33ce731b74544289ac8d4b7e181dea8092b9_2_690x295.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/549b33ce731b74544289ac8d4b7e181dea8092b9_2_1035x442.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/549b33ce731b74544289ac8d4b7e181dea8092b9_2_1380x590.jpeg 2x" data-dominant-color="343431"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-03-12 alle 13.26.35</span><span class="informations">1920×823 35.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The same situation occurs when I consider lung vessels as total segmentation results.<br>
Thanks</p>

---

## Post #4 by @Caterina (2024-03-16 17:59 UTC)

<p>Thanks to the help of <a class="mention" href="/u/lassoan">@lassoan</a>, I found out glTF only supports PBR shading (Figure in the upper side).<br>
Just other few questions:<br>
-Why if I export only the segmentation, the lung models are correctly visible and the vessels not?<br>
-So the correct procedure is to convert segmentation to models, set the PBR interpolation and then export in gltf format using Open Anatomy Export?<br>
-The vessels segmentation in Slicer (using chest ct of your database) appeared with poor dimensional resolution (vessels seems to be unreal). Can I ask you the best results concerning lung vessels segmentation and what resolution and type of source dicoms should be considered?<br>
Thank you</p>

---

## Post #5 by @lassoan (2024-03-17 00:13 UTC)

<aside class="quote no-group" data-username="Caterina" data-post="4" data-topic="34819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/439d5e/48.png" class="avatar"> Caterina:</div>
<blockquote>
<p>Why if I export only the segmentation, the lung models are correctly visible and the vessels not?</p>
</blockquote>
</aside>
<p>The gltTF file is generated the same way, regardless of the input is a segmentation or a model tree. Please compare the two files (they are just simple text files that you can open in any text editor or text comparison tool) and let us know what the differences are.</p>
<p>However, it would better if you used a 3D viewer that propertly supports transparent surface rendering (can do depth sorting, depth peeling, or similar methods).</p>
<aside class="quote no-group" data-username="Caterina" data-post="4" data-topic="34819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/439d5e/48.png" class="avatar"> Caterina:</div>
<blockquote>
<p>So the correct procedure is to convert segmentation to models, set the PBR interpolation and then export in gltf format using Open Anatomy Export?</p>
</blockquote>
</aside>
<p>What you describe works but more complex than necessary.</p>
<aside class="quote no-group" data-username="Caterina" data-post="4" data-topic="34819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/439d5e/48.png" class="avatar"> Caterina:</div>
<blockquote>
<p>The vessels segmentation in Slicer (using chest ct of your database) appeared with poor dimensional resolution (vessels seems to be unreal). Can I ask you the best results concerning lung vessels segmentation and what resolution and type of source dicoms should be considered?</p>
</blockquote>
</aside>
<p>For high-quality vessel segmentation you need high-resolution images. Typical resolution for surgical planning is 1mm. For vessel segmentation (especially for veins) you may need contrast agent.</p>
<hr>
<p>For your information, Slicer now offers fully automated lung, lobes, airways, and vessel segmentation. There are several active discussions about it see for example here:</p>
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

## Post #6 by @Caterina (2024-03-18 09:11 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
first of all thanks for support and for informations.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="34819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Please compare the two files (they are just simple text files that you can open in any text editor or text comparison tool) and let us know what the differences are.</p>
</blockquote>
</aside>
<p>I will check and share with you the differences.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="34819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What you describe works but more complex than necessary.</p>
</blockquote>
</aside>
<p>What do you mean?</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="34819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For high-quality vessel segmentation you need high-resolution images. Typical resolution for surgical planning is 1mm. For vessel segmentation (especially for veins) you may need contrast agent.</p>
<hr>
<p>For your information, Slicer now offers fully automated lung, lobes, airways, and vessel segmentation.</p>
</blockquote>
</aside>
<p>Thanks for sharing with me this extention. I compared the results of segmentation using: a) Lung segmentation extension and then vessels segmentation using Total segmentation and b) Monai extension. I used the same source origin (toracic volumetric with high resolution (slice thickness: 1 mm)). In both cases, if I zoom on vessels resolution, the result is not good (see picture in attach).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7dfdc49713eba4f454ae8368d1b37fdfa6aad9fc.jpeg" data-download-href="/uploads/short-url/hYznvdzNDapIQusXjXJPc0wYtVq.jpeg?dl=1" title="Screenshot_3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7dfdc49713eba4f454ae8368d1b37fdfa6aad9fc_2_644x500.jpeg" alt="Screenshot_3" data-base62-sha1="hYznvdzNDapIQusXjXJPc0wYtVq" width="644" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7dfdc49713eba4f454ae8368d1b37fdfa6aad9fc_2_644x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7dfdc49713eba4f454ae8368d1b37fdfa6aad9fc_2_966x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7dfdc49713eba4f454ae8368d1b37fdfa6aad9fc_2_1288x1000.jpeg 2x" data-dominant-color="7E5760"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_3</span><span class="informations">1816×1408 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>.<br>
So, in order to have good resolution on vessels segmentation, I need contrast agent dicom?<br>
Thanks</p>

---

## Post #7 by @klc (2024-03-21 17:26 UTC)

<p>Hi professor, looks like I have some problem when I am exporting the segmentation to gltf, the segmetation from slicer looks like this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6824278c7150b4a94aaff10129783b0224738df0.jpeg" data-download-href="/uploads/short-url/eRh7hTbX7dDIkTu1uTQ06dPkQ2Q.jpeg?dl=1" title="WhatsApp Image 2024-03-19 at 14.32.08_0c92a6f3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6824278c7150b4a94aaff10129783b0224738df0_2_530x499.jpeg" alt="WhatsApp Image 2024-03-19 at 14.32.08_0c92a6f3" data-base62-sha1="eRh7hTbX7dDIkTu1uTQ06dPkQ2Q" width="530" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6824278c7150b4a94aaff10129783b0224738df0_2_530x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6824278c7150b4a94aaff10129783b0224738df0_2_795x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6824278c7150b4a94aaff10129783b0224738df0.jpeg 2x" data-dominant-color="8E7C91"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2024-03-19 at 14.32.08_0c92a6f3</span><span class="informations">874×824 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, when exported to unity, the blood vessels in the gltf become like this<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc34fd69528d7e3fceaa92bb1136ed2c0599f582.jpeg" alt="WhatsApp Image 2024-03-21 at 23.39.09_2ccb8ed4" data-base62-sha1="qQXih2KA1MBbFEYc4lQ8rE8XrzQ" width="683" height="451"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9aa7dc607f8ff2ea4d675f8da7f0d6cd5135356.jpeg" alt="WhatsApp Image 2024-03-21 at 15.23.22_f7fa8218" data-base62-sha1="qutBH15LfYEHOKWgqkom38YewAe" width="534" height="453"></p>
<p>I tried using an online gltf viewer and it seems that there is a similar problem:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22543d2d445848f12a77b3f57eb43ce476171845.jpeg" data-download-href="/uploads/short-url/4TGIl4Jv36KSu4D547qcw42bWJL.jpeg?dl=1" title="WhatsApp Image 2024-03-22 at 00.14.29_7d52cf30" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22543d2d445848f12a77b3f57eb43ce476171845_2_521x500.jpeg" alt="WhatsApp Image 2024-03-22 at 00.14.29_7d52cf30" data-base62-sha1="4TGIl4Jv36KSu4D547qcw42bWJL" width="521" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22543d2d445848f12a77b3f57eb43ce476171845_2_521x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22543d2d445848f12a77b3f57eb43ce476171845.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22543d2d445848f12a77b3f57eb43ce476171845.jpeg 2x" data-dominant-color="59544F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2024-03-22 at 00.14.29_7d52cf30</span><span class="informations">755×724 83.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>May I know what can be done to solve this problem</p>
<p>Thank you</p>

---

## Post #8 by @lassoan (2024-03-21 19:05 UTC)

<p>For intricate structures like this, you need to reduce the decimation.</p>

---

## Post #9 by @klc (2024-03-22 05:31 UTC)

<p>Thank you for your prompt response. I followed this video for decimation and indeed got better results.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="d-0y7BHJ0oU" data-video-title="Reduce the File Size of Your 3D Model - &quot;Decimation&quot;  [3D Slicer Workflow]" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=d-0y7BHJ0oU" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/d-0y7BHJ0oU/maxresdefault.jpg" title="Reduce the File Size of Your 3D Model - &quot;Decimation&quot;  [3D Slicer Workflow]" width="" height="">
  </a>
</div>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4eaba74614615f672275c42d8b9f203125b2e9ad.png" data-download-href="/uploads/short-url/bdX0wqDyUtM68H1tAI7buP8SagR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4eaba74614615f672275c42d8b9f203125b2e9ad_2_462x500.png" alt="image" data-base62-sha1="bdX0wqDyUtM68H1tAI7buP8SagR" width="462" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4eaba74614615f672275c42d8b9f203125b2e9ad_2_462x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4eaba74614615f672275c42d8b9f203125b2e9ad.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4eaba74614615f672275c42d8b9f203125b2e9ad.png 2x" data-dominant-color="8C8096"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">670×724 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>May I also know that if there are little pieces of blood fragments near the blood vessel but they are not connected (see attached), apart from manually segmenting them out, is there a better way in the surface tool box extensions or other extensions to clean them up.</p>
<p>thank you very much</p>

---

## Post #10 by @lassoan (2024-03-22 12:11 UTC)

<p>Small vessels are usually not needed for surgical planning and just occlude relevant parts, so commonly users apply Islands effect / Keep largest island method on the automatic vessel extraction result to get rid of them.</p>

---

## Post #11 by @klc (2024-03-22 17:43 UTC)

<p>Thank you<br>
Sorry for asking again. I found that for some other samples, the black spots still persist after numerous decimation, I have used larger value for decimation and tried other methods in the surface toolbox (uniform remesh, decimate, smooth, compute surface normals) If i use keep largest or island, it will only get a sub part of the vessels since they are not connected. I am still not sure why this problem happened, do you have other suggestions to solve it ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c51352c3fcee396a37677996faa4cfbb1de7b1dc.jpeg" data-download-href="/uploads/short-url/s7psCDwGC9lSO5xLR46PC3ZXN6c.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c51352c3fcee396a37677996faa4cfbb1de7b1dc_2_618x499.jpeg" alt="image" data-base62-sha1="s7psCDwGC9lSO5xLR46PC3ZXN6c" width="618" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c51352c3fcee396a37677996faa4cfbb1de7b1dc_2_618x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c51352c3fcee396a37677996faa4cfbb1de7b1dc.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c51352c3fcee396a37677996faa4cfbb1de7b1dc.jpeg 2x" data-dominant-color="4F5764"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">718×580 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Moreover, may I know is it possible to write a simple python script that can eliminate small fragments that are smaller than some size (e.g. 10 mm)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca3afd42142109ea4f2bed6332693c51f6c0df91.jpeg" data-download-href="/uploads/short-url/sR0PE3num2J38nvbcKRZ8a3Cbpn.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca3afd42142109ea4f2bed6332693c51f6c0df91_2_605x500.jpeg" alt="image" data-base62-sha1="sR0PE3num2J38nvbcKRZ8a3Cbpn" width="605" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca3afd42142109ea4f2bed6332693c51f6c0df91_2_605x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca3afd42142109ea4f2bed6332693c51f6c0df91.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca3afd42142109ea4f2bed6332693c51f6c0df91.jpeg 2x" data-dominant-color="9792A2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">795×656 233 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you very much for your response.</p>

---

## Post #12 by @lassoan (2024-03-22 18:47 UTC)

<p>You can use many tools in Segment Editor to get rid of small vessels but preserve large ones. It is an independent question from glTF export and is discussed in separate topics on this forum. Please read <a href="https://discourse.slicer.org/tag/lung">recent topics related to lung</a> and if you have trouble producing good lung vessel segmentation then you can ask for more help by commenting in those topics.</p>
<aside class="quote no-group" data-username="klc" data-post="11" data-topic="34819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/klc/48/68248_2.png" class="avatar"> klc:</div>
<blockquote>
<p>have used larger value for decimation and tried other methods in the surface toolbox (uniform remesh, decimate, smooth, compute surface normals)</p>
</blockquote>
</aside>
<p>These are all unnecessary. What I meant is to simply decrease the “Reduction factor” in the OpenAnatomy Export module to a lower value to preserve more details. If you set the slider to 0 then the exported glTF file will contain the exact same details as you see in Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38e53daa82f026ff2198394a26ebb7c1a2719144.png" data-download-href="/uploads/short-url/87jSQG5MgA8Z8OVCZVW8VESuHVq.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38e53daa82f026ff2198394a26ebb7c1a2719144_2_690x432.png" alt="image" data-base62-sha1="87jSQG5MgA8Z8OVCZVW8VESuHVq" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38e53daa82f026ff2198394a26ebb7c1a2719144_2_690x432.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38e53daa82f026ff2198394a26ebb7c1a2719144_2_1035x648.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38e53daa82f026ff2198394a26ebb7c1a2719144.png 2x" data-dominant-color="3C3C3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1081×677 46.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @klc (2024-03-23 03:28 UTC)

<p>Thank you for your prompt response. I found that the exported blood vessels was not displayed correctly in gltf or obj. I have tried 0.0 decimation value. I have tried different platforms, meshlab, online viewer and unity but the result is still the same.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfe99db068ba7cb38b2fb8e85e82c06640f9c709.png" alt="image" data-base62-sha1="rnJIrggVhu4hnUA4h3REGOiQSmt" width="550" height="454"><br>
blood vessels in unity obj</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bff1fbc066f857a07edbb0d34b1e8216c8a1f606.jpeg" alt="WhatsApp Image 2024-03-22 at 18.27.22_8df728f9" data-base62-sha1="ro1DVby10KcobQtMAMWwHtd11pc" width="582" height="432"><br>
blood vessels in unity gltf</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f366e03cc1511dc99e6bd7e33da4a6a251832950.png" alt="image" data-base62-sha1="yJer1TmjzdVuhT5VWUoYTmtXxfO" width="609" height="420"><br>
blood vessels in meshlab obj</p>
<p>Steps to reproduce:<br>
Data: LIDC-IDRI-0078<br>
Slicer 5.6.1, Slicer 5.7.0 Preview release.<br>
Use MONAI Auto 3D seg, lung 2.0.1 to produce lung segmentation<br>
Export to gltf using Openanatomy export</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16a54505b4bbf71af43d91210cadb754b899ba68.png" data-download-href="/uploads/short-url/3ekAL0uFeSNWKu682FmE2oN3y9W.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16a54505b4bbf71af43d91210cadb754b899ba68_2_627x500.png" alt="image" data-base62-sha1="3ekAL0uFeSNWKu682FmE2oN3y9W" width="627" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16a54505b4bbf71af43d91210cadb754b899ba68_2_627x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16a54505b4bbf71af43d91210cadb754b899ba68.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16a54505b4bbf71af43d91210cadb754b899ba68.png 2x" data-dominant-color="93749A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">890×709 261 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This is the expected vessels in slicer</p>
<p>May I know if there is any workaround?</p>
<p>Thank you very much</p>

---

## Post #14 by @klc (2024-03-23 06:08 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0aafba82898d90d6e781c2858eff9e662c3cc88.jpeg" data-download-href="/uploads/short-url/ruq0eyTtCnviR3DYocycXDbUwdi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0aafba82898d90d6e781c2858eff9e662c3cc88_2_690x107.jpeg" alt="image" data-base62-sha1="ruq0eyTtCnviR3DYocycXDbUwdi" width="690" height="107" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0aafba82898d90d6e781c2858eff9e662c3cc88_2_690x107.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0aafba82898d90d6e781c2858eff9e662c3cc88_2_1035x160.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0aafba82898d90d6e781c2858eff9e662c3cc88_2_1380x214.jpeg 2x" data-dominant-color="FCF8F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1458×228 53.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I found that the decimation process also produced some errors in slicer but was not able to resolve them.</p>
<p>The errors prevented the GLTF file from being opened in Unity, causing compatibility issues. If I opened the gltf file on gltf viewer online, looks like the vessel can be shown clearly but there are still a lot of errors as shown on the left bottom corner.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18cac6441c0a9143a6d9222410f4cb0cd1d12b75.jpeg" data-download-href="/uploads/short-url/3xjTTLo9wzRyD2SAP7H30hIS245.jpeg?dl=1" title="WhatsApp Image 2024-03-23 at 13.33.13_353048f6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18cac6441c0a9143a6d9222410f4cb0cd1d12b75_2_690x423.jpeg" alt="WhatsApp Image 2024-03-23 at 13.33.13_353048f6" data-base62-sha1="3xjTTLo9wzRyD2SAP7H30hIS245" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18cac6441c0a9143a6d9222410f4cb0cd1d12b75_2_690x423.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18cac6441c0a9143a6d9222410f4cb0cd1d12b75_2_1035x634.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18cac6441c0a9143a6d9222410f4cb0cd1d12b75_2_1380x846.jpeg 2x" data-dominant-color="222221"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2024-03-23 at 13.33.13_353048f6</span><span class="informations">1600×982 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Fig 1: The vessels are shown correctly on gltfviewer after decimation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ea3bd168e92b3650bfd19b9b2f63cd1d4b99a61.jpeg" data-download-href="/uploads/short-url/4n38dkAVlFg1lDEL8HSWuneAPlv.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ea3bd168e92b3650bfd19b9b2f63cd1d4b99a61_2_645x500.jpeg" alt="image" data-base62-sha1="4n38dkAVlFg1lDEL8HSWuneAPlv" width="645" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ea3bd168e92b3650bfd19b9b2f63cd1d4b99a61_2_645x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ea3bd168e92b3650bfd19b9b2f63cd1d4b99a61_2_967x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ea3bd168e92b3650bfd19b9b2f63cd1d4b99a61_2_1290x1000.jpeg 2x" data-dominant-color="EDEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1782×1380 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
errors of the gltf file after decimation</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/faea78178137f08265ce4073043024bb6ee6cb40.png" data-download-href="/uploads/short-url/zNHIlQuPtgm0waGio72yoMClscM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/faea78178137f08265ce4073043024bb6ee6cb40_2_690x336.png" alt="image" data-base62-sha1="zNHIlQuPtgm0waGio72yoMClscM" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/faea78178137f08265ce4073043024bb6ee6cb40_2_690x336.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/faea78178137f08265ce4073043024bb6ee6cb40_2_1035x504.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/faea78178137f08265ce4073043024bb6ee6cb40.png 2x" data-dominant-color="2D3C4C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1075×524 36.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>On the other hand, I used the CT chest sample from slicer and created a lung segmentation using v2.0.1 MONAI 3D  Auto Seg and the blood vessels have similar problem. The attached picture didn’t undergo any decimation. The result after decimation is similar too.</p>
<p>I use both Slicer 5.6.1 and preview release version. For the 5.6.1 version, the problem persist after decimation. For the preview release version, the display results after decimation are acceptable but with errors, those errors prevent the file from being opened in Unity.</p>
<p>Please check if the openanatomy export to gltf function is working correctly</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>Thank you very much.</p>

---

## Post #15 by @Caterina (2024-04-02 08:20 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
I have similar problems of <a class="mention" href="/u/klc">@klc</a>.<br>
In addition, when I export models with several % of trasparency in gltf format using OpenAnatomy and I visualize them on Hololens 2 device, the models are always opaque.<br>
Can you please suggest me a solution?<br>
Thanks</p>

---
