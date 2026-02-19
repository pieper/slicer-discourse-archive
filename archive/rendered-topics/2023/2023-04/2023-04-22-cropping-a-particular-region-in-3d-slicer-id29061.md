---
topic_id: 29061
title: "Cropping A Particular Region In 3D Slicer"
date: 2023-04-22
url: https://discourse.slicer.org/t/29061
---

# Cropping a particular region in 3D slicer

**Topic ID**: 29061
**Date**: 2023-04-22
**URL**: https://discourse.slicer.org/t/cropping-a-particular-region-in-3d-slicer/29061

---

## Post #1 by @Roro1 (2023-04-22 20:29 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4da84ba60c2b423eddf9d94bbb042b8f268c5003.png" data-download-href="/uploads/short-url/b4ZkSbdRnAFHnzQYZrl9Ik3Gzrd.png?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4da84ba60c2b423eddf9d94bbb042b8f268c5003_2_690x263.png" alt="Capture1" data-base62-sha1="b4ZkSbdRnAFHnzQYZrl9Ik3Gzrd" width="690" height="263" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4da84ba60c2b423eddf9d94bbb042b8f268c5003_2_690x263.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4da84ba60c2b423eddf9d94bbb042b8f268c5003.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4da84ba60c2b423eddf9d94bbb042b8f268c5003.png 2x" data-dominant-color="7A7C9F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">722×276 90.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Hi everyone, in our project we have to create a 3D section of a rat bone (I’ve put the corresponding picture in the post). In this project, we also have to determine if the hole (also present in the linked picture) is reproducible between the different animals. Therefore, we would like to crop only this hole in order to apply it on other rat bones. Unfortunately, I can’t make it thanks to the segmentation part because the region that we want is a part of the backround. Does anyone have an alternative?</p>
<p>I was also wondering if it was possible to select a given zone in this hole and to see to which picture it corresponds (in order to investigate further 2D-analysis on imageJ)?</p>
<p>Many thanks for your answer(s) and have a nice week-end^^!</p>

---

## Post #2 by @tsehrhardt (2023-04-23 12:03 UTC)

<p>There are a couple of things you can do. You can crop the CT volume to the area of interest before segmentation or crop after. The image below shows how you can isolate the area of interest in the Volume Rendering module, then use the Crop Volume module to crop. The new volume will be have “cropped” appended to the name and you can save this as a separate volume. This can be helpful before segmentation if you have a large dataset.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3bc0aed9305bbacbd8ac317dea5fdfa544a4cb2.jpeg" data-download-href="/uploads/short-url/yMaU6vAEyHxcaKthcYERHWzTnR8.jpeg?dl=1" title="2023-04-23_7-43-01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3bc0aed9305bbacbd8ac317dea5fdfa544a4cb2_2_690x377.jpeg" alt="2023-04-23_7-43-01" data-base62-sha1="yMaU6vAEyHxcaKthcYERHWzTnR8" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3bc0aed9305bbacbd8ac317dea5fdfa544a4cb2_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3bc0aed9305bbacbd8ac317dea5fdfa544a4cb2_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3bc0aed9305bbacbd8ac317dea5fdfa544a4cb2_2_1380x754.jpeg 2x" data-dominant-color="9B9BAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-04-23_7-43-01</span><span class="informations">1920×1050 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Next you can use the original or cropped volume to segment the hole. Idk if your volume has soft tissue, but the first segment can be your soft tissue or background. The second segment can be the bone which by default gets subtracted from the first segment. Then you can create an empty third segment to add your “hole” to.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ed18b7368a3f7c3a49c88f0890d313ae413c3cb.jpeg" data-download-href="/uploads/short-url/275DbMWRTCJhBIZcpPtH7nEnrtN.jpeg?dl=1" title="2023-04-23_7-50-11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ed18b7368a3f7c3a49c88f0890d313ae413c3cb_2_690x377.jpeg" alt="2023-04-23_7-50-11" data-base62-sha1="275DbMWRTCJhBIZcpPtH7nEnrtN" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ed18b7368a3f7c3a49c88f0890d313ae413c3cb_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ed18b7368a3f7c3a49c88f0890d313ae413c3cb_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ed18b7368a3f7c3a49c88f0890d313ae413c3cb_2_1380x754.jpeg 2x" data-dominant-color="9A9EAD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-04-23_7-50-11</span><span class="informations">1920×1050 95.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39f90f05b5477f1d0c1ba6ff0f087034ec39b79c.jpeg" data-download-href="/uploads/short-url/8gQOW97M3a8H2n2zGApnIuOxpqk.jpeg?dl=1" title="2023-04-23_7-51-01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39f90f05b5477f1d0c1ba6ff0f087034ec39b79c_2_690x377.jpeg" alt="2023-04-23_7-51-01" data-base62-sha1="8gQOW97M3a8H2n2zGApnIuOxpqk" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39f90f05b5477f1d0c1ba6ff0f087034ec39b79c_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39f90f05b5477f1d0c1ba6ff0f087034ec39b79c_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39f90f05b5477f1d0c1ba6ff0f087034ec39b79c_2_1380x754.jpeg 2x" data-dominant-color="99979D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-04-23_7-51-01</span><span class="informations">1920×1050 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>To view correspondences between the 3D model and 2D slices, turn on the crosshairs at the top toolbar. When you hold shift and move your mouse over the 2D slices, the crosshair will move over all 3 slice views as well as on your 3D model.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b56c34c99e72fd6df12482dea1de7daca1548c34.jpeg" data-download-href="/uploads/short-url/pSWfG1H7ClWNPR2aG6eja4e6vmQ.jpeg?dl=1" title="2023-04-23_7-52-58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b56c34c99e72fd6df12482dea1de7daca1548c34_2_690x377.jpeg" alt="2023-04-23_7-52-58" data-base62-sha1="pSWfG1H7ClWNPR2aG6eja4e6vmQ" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b56c34c99e72fd6df12482dea1de7daca1548c34_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b56c34c99e72fd6df12482dea1de7daca1548c34_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b56c34c99e72fd6df12482dea1de7daca1548c34_2_1380x754.jpeg 2x" data-dominant-color="9E9FAF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-04-23_7-52-58</span><span class="informations">1920×1050 92 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hope that helps!</p>

---

## Post #3 by @Roro1 (2023-04-24 07:23 UTC)

<p>Ok thanks a lot I will try it! Have a nice day <img src="https://emoji.discourse-cdn.com/twitter/upside_down_face.png?v=12" title=":upside_down_face:" class="emoji" alt=":upside_down_face:" loading="lazy" width="20" height="20"></p>

---
