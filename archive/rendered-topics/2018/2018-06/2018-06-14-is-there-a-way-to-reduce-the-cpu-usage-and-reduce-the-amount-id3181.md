---
topic_id: 3181
title: "Is There A Way To Reduce The Cpu Usage And Reduce The Amount"
date: 2018-06-14
url: https://discourse.slicer.org/t/3181
---

# Is there a way to reduce the CPU usage and reduce the amount of RAM used?

**Topic ID**: 3181
**Date**: 2018-06-14
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-reduce-the-cpu-usage-and-reduce-the-amount-of-ram-used/3181

---

## Post #1 by @goetzf (2018-06-14 18:36 UTC)

<p>Operating system: MacOZ 10.13.4<br>
Slicer version: 4.9.0-2018-05-30<br>
Expected behavior:<br>
Actual behavior:</p>
<p>When I first opened the stack of 547 registered serial section images, the computer was using between 5 and 6 GB RAM. I went through and segmented the whole animal to get an exterior volume . I selegted every 2nd or 4th slice, sometimes every 6th and I then operated “fill between slices”. That didn’t take too long but now of course I want to edit that fill where it wasn’t quite right. the attached image is what happened to the CPU after I did the smallest painting to extend the margin on one part. That was about 10 minutes ago and the CPU is still blown out. We are also now at 43.6GB RAM and that’s only the whole body segment. I still need to do the eyes, gut and maybe nervous system as well as the eggs.</p>
<p>My questions:<br>
How can I edit the segments that were filled between slices without it looking like I’ve doubled the thickness or not responding to the eraser?</p>
<p>How can I more efficiently use the CPU? I have 4.2 GHz Intel Core i7</p>
<p>How can I reduce the RAM usage so that I can do more segmenations?</p>
<p>How can I reduce the size of the segments? It seems like they should be quite small if they are just a shape. Is this because they are not vectors?</p>
<p>What is the best way to downsize my data when I have already started segmentation?</p>
<p>I would really appreciate the help.</p>
<p>Thank you!</p>
<p>Freya</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f7ef6b580d1bf92964cae46e5e8a3b9c472f3df.png" data-download-href="/uploads/short-url/mKXW35V6jJ40kuuiNYEVNawZrR5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f7ef6b580d1bf92964cae46e5e8a3b9c472f3df_2_298x500.png" alt="image" data-base62-sha1="mKXW35V6jJ40kuuiNYEVNawZrR5" width="298" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f7ef6b580d1bf92964cae46e5e8a3b9c472f3df_2_298x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f7ef6b580d1bf92964cae46e5e8a3b9c472f3df_2_447x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f7ef6b580d1bf92964cae46e5e8a3b9c472f3df_2_596x1000.png 2x" data-dominant-color="5A6451"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1208×2024 886 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-06-14 19:41 UTC)

<p>Most probably you’ve run out of physical memory and so disk swapping is used. In general, I would recommend to have 10x more physical RAM as the size of your data set. If that’s not feasible then you can use Crop volume module to crop and resample your volume. Obviously, also crop any regions in your volume that you don’t need.</p>
<p>For 3D processing, you can rarely benefit from having high in-plane resolution if distance between planes is large. For example, a volume of 2500x2500x500 (with spacing of 0.1x0.1x0.5) will give you approximately same quality 3D reconstructions as a volume of 500x500x500 (with spacing of 0.5x0.5x0.5). So, in Crop volume module, enable isotropic spacing and set spacing scale to a large enough number so that you end up with a volume of approximately 500x500x500 voxels (you can see in Volume information section what the cropped volume’s dimension will be).</p>
<p>Use the cropped and resampled volume as master volume for your segmentation. During segmentation, you can choose the original, full-resolution volume as background, so when you paint you may see small details, but the 3D segmentation will take up much less memory and everything will be much faster.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> is working on a new feature that will simplify setting the 3D segmentation’s resolution higher or lower than the master volume. It is expected to be ready next week. So, if you have trouble setting up the cropped, isotropic master volume node, then you may wait for this new feature (you can monitor <a href="https://issues.slicer.org/view.php?id=4308">this issue</a> to get status updates).</p>
<p>It would be also useful to know the dimensions, spacing, number of scalars, and scalar type of your data set (see in Volumes module / Volume information section), and the amount of physical RAM in your computer.</p>

---

## Post #3 by @goetzf (2018-06-14 19:51 UTC)

<p>Thank you. I will try that. I honestly haven’t wrapped my brain completely around what spacing means in this program. I’m coming from Fiji and Amira where I had serially sectioned epoxy embedded animals at 1um thick sections, photographed each section and registered them in a stack. So spacing to me means the distance between slices (1um in my case) and to have the 3D slicer “spacing” in three dimensions makes me think I’m not understanding this.</p>
<p>Here is my hardware:<br>
|Model Name:|iMac|<br>
|  Model Identifier:|iMac18,3|<br>
|  Processor Name:|Intel Core i7|<br>
|  Processor Speed:|4.2 GHz|<br>
|  Number of Processors:|1|<br>
|  Total Number of Cores:|4|<br>
|  L2 Cache (per Core):|256 KB|<br>
|  L3 Cache:|8 MB|<br>
|  Memory:|64 GB|</p>

---

## Post #4 by @goetzf (2018-06-14 19:54 UTC)

<p>Another question: would it help to just outline the different segments instead of coloring in the whole organ?</p>

---

## Post #5 by @lassoan (2018-06-14 21:08 UTC)

<aside class="quote no-group" data-username="goetzf" data-post="3" data-topic="3181">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b38774/48.png" class="avatar"> goetzf:</div>
<blockquote>
<p>I will try that. I honestly haven’t wrapped my brain completely around what spacing means in this program.</p>
</blockquote>
</aside>
<p>Spacing is distance between neighboring voxels, which is the same as size of a voxel. This is also referred to as resolution of the image.</p>
<aside class="quote no-group" data-username="goetzf" data-post="4" data-topic="3181">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b38774/48.png" class="avatar"> goetzf:</div>
<blockquote>
<p>would it help to just outline the different segments instead of coloring in the whole organ?</p>
</blockquote>
</aside>
<p>It would not make a difference.</p>
<p>It would be useful to know the dimensions, spacing, number of scalars, and scalar type of your data set (shown in Volumes module / Volume information section).</p>
<p>What would you like to do with the images in Slicer? View the shape of segmented structures? Or compute their volume or surface…?</p>

---

## Post #6 by @goetzf (2018-06-14 21:33 UTC)

<p>Thank you for that information.<br>
Here is what I ended up doing and it seems to be a bit faster, using less RAM.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e4337afdada05da5ae84ade4278be3dded9ce35.png" alt="image" data-base62-sha1="22aHf5ypSgjbZi1zZddP3z3zRid" width="670" height="463"></p>
<p>I want to make a 3D rendering of the whole animal like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fa7feb748e3e9836bdcacb1126851ed5a8ac754.jpeg" alt="image" data-base62-sha1="mMnQpHjQmThlqo0gvDeN0tZmzAg" width="412" height="471"><br>
or this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb2d968807720ba6b8e38368e694d739f26d1eae.jpeg" data-download-href="/uploads/short-url/sZoB683bwv5yc3m2E2Wx7T25VLg.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cb2d968807720ba6b8e38368e694d739f26d1eae_2_690x314.jpg" alt="image" data-base62-sha1="sZoB683bwv5yc3m2E2Wx7T25VLg" width="690" height="314" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cb2d968807720ba6b8e38368e694d739f26d1eae_2_690x314.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cb2d968807720ba6b8e38368e694d739f26d1eae_2_1035x471.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb2d968807720ba6b8e38368e694d739f26d1eae.jpeg 2x" data-dominant-color="332F27"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1079×492 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2018-06-14 21:49 UTC)

<p>You may delete the original volume to reduce memory need and potentially speed up things. You can also try further increasing spacing value and crop away all regions that you don’t need to segment.</p>
<p>You may try Volume Rendering module for visualization of the complete body. For that you may need to further increase slice spacing.</p>

---

## Post #8 by @goetzf (2018-06-14 21:58 UTC)

<p>Okay, thank you. I will try those things tomorrow. I really appreciate your quick responses.</p>

---
