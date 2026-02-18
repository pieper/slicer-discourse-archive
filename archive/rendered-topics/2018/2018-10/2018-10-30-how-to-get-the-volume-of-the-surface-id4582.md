# How to get the volume of the surface

**Topic ID**: 4582
**Date**: 2018-10-30
**URL**: https://discourse.slicer.org/t/how-to-get-the-volume-of-the-surface/4582

---

## Post #1 by @Gary (2018-10-30 06:11 UTC)

<p>Hi everyone,</p>
<p>First of all, I need to appreciate the help from everyone. Your suggestions do really help me on the project that I am working on.</p>
<p>The question now is that I got the 3D of the graph(Picture 2). However, I just noticed that I need to get the surface of the border, which means to <strong>use the line between the black and white region to form a volume of the surface</strong>(Picture 1). I got the 3D volume of the black region right now, and cannot find the way to <strong>remove the black region and keep the inside border surface</strong>. Just like an empty box.<br>
After removing the outside surface, the inside parts should be like Picture 3.<br>
Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86a746d203928ad5f6a68daa0c91fee903818b7b.png" data-download-href="/uploads/short-url/jdcmUIl4tRsR6pL4icuIfiS2Bl1.png?dl=1" title="NEWCapture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86a746d203928ad5f6a68daa0c91fee903818b7b_2_690x427.png" alt="NEWCapture" data-base62-sha1="jdcmUIl4tRsR6pL4icuIfiS2Bl1" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86a746d203928ad5f6a68daa0c91fee903818b7b_2_690x427.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86a746d203928ad5f6a68daa0c91fee903818b7b_2_1035x640.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86a746d203928ad5f6a68daa0c91fee903818b7b.png 2x" data-dominant-color="63636F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">NEWCapture</span><span class="informations">1376×853 65.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Gary (2018-10-30 06:17 UTC)

<p>In other words, How could I only mark the border (The line that between black and white region) to form a volume of the surface?</p>

---

## Post #3 by @pieper (2018-10-31 20:05 UTC)

<p>Hi <a class="mention" href="/u/gary">@Gary</a> -</p>
<p>Sorry if this is a language issue, but can you clarify what you mean by the “volume of the surface”  do you mean the surface area (mm^2)? or the volume of the surface vessels (mm^3)?   And when you say the “line between black and white region” does that mean only the outer surface of the heart or also the white part that is inside the heart?  Your figure 3 looks like vessels on the outer surface - is that what you are trying to segment?</p>
<p>-Steve</p>

---

## Post #4 by @Gary (2018-11-05 03:51 UTC)

<p>Hi pieper,</p>
<p>Sorry about confusing language, what I mean is to form a 3D model only by using the green part as the attached picture. The green part is the boundary which split the white and black region in my graph.</p>
<p>Thank you!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15a9e079e7f5a880ac856f3dcb60e0144c6881d0.png" alt="boundary" data-base62-sha1="35DZ9CtrnshxdhFfvpKsUyiIT1S" width="581" height="396"></p>

---

## Post #5 by @Gary (2018-11-05 03:53 UTC)

<p>By the way, I used the threshold to mark the part that I want, but after I click “apply”, it just disappear. Could you tell me how to solve the problem?</p>
<p>Thank you!</p>

---

## Post #6 by @Gary (2018-11-05 06:09 UTC)

<p>I think I got the result by using hollow.</p>

---

## Post #7 by @Gary (2018-11-05 06:38 UTC)

<p>Hi pieper, my current problem is how to remove the most outside surface. I found a very useful function in Segmentation Editor, which is Islands. However, there is no option to remove the largest island. But there is an option called “remove selected island”, how could I selected the outside surface?</p>
<p>Thank you.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3938fe097c3dc28b3d1ce25fb7eeef91e3109a1.png" alt="Islands" data-base62-sha1="pCBChdmUFj0ETx41NVKpbhNohwJ" width="578" height="265"></p>

---

## Post #8 by @Gary (2018-11-05 06:39 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b49b51eddae80f4b7998aec10db398d4ae819f9.png" data-download-href="/uploads/short-url/8su5tCGvI22s3l4pBdHTPjHxGZ3.png?dl=1" title="newsurface2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b49b51eddae80f4b7998aec10db398d4ae819f9_2_690x493.png" alt="newsurface2" data-base62-sha1="8su5tCGvI22s3l4pBdHTPjHxGZ3" width="690" height="493" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b49b51eddae80f4b7998aec10db398d4ae819f9_2_690x493.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b49b51eddae80f4b7998aec10db398d4ae819f9_2_1035x739.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b49b51eddae80f4b7998aec10db398d4ae819f9.png 2x" data-dominant-color="575E5A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">newsurface2</span><span class="informations">1163×831 264 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @pieper (2018-11-05 13:18 UTC)

<aside class="quote no-group" data-username="Gary" data-post="7" data-topic="4582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/839c29/48.png" class="avatar"> Gary:</div>
<blockquote>
<p>But there is an option called “remove selected island”, how could I selected the outside surface?</p>
</blockquote>
</aside>
<p>This means that you can click on one of the segments in the slice views and any voxels ‘connected’ to that voxel are removed.</p>

---

## Post #10 by @Gary (2018-11-09 23:00 UTC)

<p>Thank you pieper,<br>
By the way, When I use the “hollow”, will the shell thickness affect my export .stl file? In other words, will the stl file contain the data of the thickness?</p>
<p>Thank you</p>

---

## Post #11 by @lassoan (2018-11-10 04:59 UTC)

<aside class="quote no-group" data-username="Gary" data-post="10" data-topic="4582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/839c29/48.png" class="avatar"> Gary:</div>
<blockquote>
<p>When I use the “hollow”, will the shell thickness affect my export .stl file?</p>
</blockquote>
</aside>
<p>Yes. Your model will have double-walled. Distance between the two walls is the shell thickness.</p>

---

## Post #12 by @Gary (2018-11-12 02:50 UTC)

<p>Thank you for your reply.<br>
Is there anyway that we could mark the boundary part by using a very thin “line”, rather than using “shell thickness”, because the smallest value 0.5mm is still too large for my data.</p>

---

## Post #13 by @lassoan (2018-11-12 03:14 UTC)

<p>The smallest achievable shell thickness is determined by the segmentation node’s internal labelmap resolution. You can make the resolution finer by clicking the box icon next to the “Master volume” selector, choose the image volume, and increase the oversampling factor. Note that 2x oversampling enables 2x thinner walls, but increases memory usage and computation time of most operations by a factor of 8x.</p>
<aside class="quote no-group" data-username="Gary" data-post="12" data-topic="4582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/839c29/48.png" class="avatar"> Gary:</div>
<blockquote>
<p>Is there anyway that we could mark the boundary part by using a very thin “line”,</p>
</blockquote>
</aside>
<p>If you don’t do anything, the surface mesh representation is already an infinitely thin shell, so you might be able to use the mesh as is, without applying hollowing. What would you like to achieve?</p>

---

## Post #14 by @Gary (2018-11-12 03:32 UTC)

<p>By using the threshold, it seems like I could only mark the black or white region of the picture. If I do not use hollow and form a 3D model. Will the inside of the 3D model be empty, just like the top right of the first picture? Or we could directly mark the boundary by using the threshold?<br>
Sorry about disturbing.</p>
<p>My final result is to form a 3D model only with marked boundary(which is much tiny than the green part on the first picture). And then I only need a single-walled surface and remove the outside surface and then see all the blood vessels like the second picture.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ae28d5f7bdaffd7c76b1b8a5b88342e0141e414.png" alt="3d" data-base62-sha1="1yi9Xu7S5osJTQlIxeLKKZeDq4I" width="690" height="493"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7d45fcb492629cb4fabc1a1e00c21829d92444f.png" alt="result" data-base62-sha1="x4RiVx10g5CwUa4iAzVd4jvPjY3" width="690" height="373"></p>

---

## Post #15 by @lassoan (2018-11-12 04:10 UTC)

<p>Is extraction of the coronary vessels? For what purpose? Visualization only? How the image was obtained?</p>
<p>Was contrast agent used for the imaging? If not, then I don’t think you have a chance to separate vessels from other tissues.</p>

---

## Post #16 by @Gary (2018-11-12 04:18 UTC)

<p>I would like to get the extraction of the coronary vessels, for visualization only, it will be better if I could export the data without the outside surface.</p>
<p>Thank you</p>

---
