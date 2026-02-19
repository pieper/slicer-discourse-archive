---
topic_id: 7493
title: "How To Do Ray Tracing In 3D Images Such As Ct Images"
date: 2019-07-10
url: https://discourse.slicer.org/t/7493
---

# How to do Ray Tracing in 3D images, such as CT images?

**Topic ID**: 7493
**Date**: 2019-07-10
**URL**: https://discourse.slicer.org/t/how-to-do-ray-tracing-in-3d-images-such-as-ct-images/7493

---

## Post #1 by @shahrokh (2019-07-10 12:21 UTC)

<p>Hi Dear 3DSlicer developers</p>
<p>I want to calculate the length of any ray that propagates from a point source and passes through the CT voxels. In other words, I want to calculate the length of each ray along its path through the voxels. So for each ray I want to calculate two parameters:</p>
<ol>
<li>
<p>The index number of the ray that the ray passes through.</p>
</li>
<li>
<p>The distance traveled within the voxel.</p>
</li>
</ol>
<p>For a better explanation and understanding, please look at the following figure.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4404cc943954148487bf5165e162d86ec032846e.png" data-download-href="/uploads/short-url/9HIKvmi4DeNaSN9f145GSSp61u6.png?dl=1" title="Picture3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4404cc943954148487bf5165e162d86ec032846e_2_579x500.png" alt="Picture3" data-base62-sha1="9HIKvmi4DeNaSN9f145GSSp61u6" width="579" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4404cc943954148487bf5165e162d86ec032846e_2_579x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4404cc943954148487bf5165e162d86ec032846e_2_868x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4404cc943954148487bf5165e162d86ec032846e_2_1158x1000.png 2x" data-dominant-color="9098AC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture3</span><span class="informations">1207×1041 76.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In the above figure, it is assumed that the rays emanated from of a point source are equal to the number of pixels in the imaging system. These rays are lines drawn from the point source to the center of pixel. So if the image matrix is 1024x1024, then there will be 1048576 rays. The figure below is a demonstration of this concept in the sagital slice (2D).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da438233f6224fd5ad4bfd79dc4453e6610c3bb4.png" data-download-href="/uploads/short-url/v8QIXclN3bkl33CXkycSuzBDF7C.png?dl=1" title="Picture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/da438233f6224fd5ad4bfd79dc4453e6610c3bb4_2_672x500.png" alt="Picture2" data-base62-sha1="v8QIXclN3bkl33CXkycSuzBDF7C" width="672" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/da438233f6224fd5ad4bfd79dc4453e6610c3bb4_2_672x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/da438233f6224fd5ad4bfd79dc4453e6610c3bb4_2_1008x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/da438233f6224fd5ad4bfd79dc4453e6610c3bb4_2_1344x1000.png 2x" data-dominant-color="9CB1D0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture2</span><span class="informations">1349×1003 60.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In this particular ray, how can I determine it passes which voxels? What distance has it traveled from each of these voxels? The figure below is the same concept in three dimensions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b3904d6fb51fd95abbc08fb2653795669e2e3d9.png" data-download-href="/uploads/short-url/6amH0t8pA7mGooF109cHE8nFEaB.png?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b3904d6fb51fd95abbc08fb2653795669e2e3d9_2_411x500.png" alt="Picture1" data-base62-sha1="6amH0t8pA7mGooF109cHE8nFEaB" width="411" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b3904d6fb51fd95abbc08fb2653795669e2e3d9_2_411x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b3904d6fb51fd95abbc08fb2653795669e2e3d9_2_616x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b3904d6fb51fd95abbc08fb2653795669e2e3d9.png 2x" data-dominant-color="6584AA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">818×993 56.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What is your proposed solution to perform these calculations?<br>
Does VTK have a library to do it?<br>
Please guide me.<br>
Shahrokh</p>

---

## Post #2 by @shahrokh (2019-07-10 13:43 UTC)

<p>Excuse me, I must correct the above message:</p>
<p>… for each ray I want to calculate two parameters:</p>
<ol>
<li>The index number of the <strong>voxel</strong> that the ray passes through.</li>
<li>The distance traveled within the voxel.<br>
…</li>
</ol>

---

## Post #3 by @gcsharp (2019-07-10 14:28 UTC)

<p>Honestly you should just do this in plastimatch.  Use plastimatch drr with the --raytrace-details option.  It will create a large file with exactly what you want.</p>

---

## Post #4 by @mta152 (2019-07-12 21:33 UTC)

<p>I think this problem has been solved.</p>
<p>Take a look at this journal paper: Siddon, Robert L. “Fast calculation of the exact radiological path for a three‐dimensional CT array.”  <em>Medical physics</em>  12.2 (1985): 252-255.<br>
and its implementation at : <a href="https://code.google.com/archive/p/drrsuite/downloads" rel="nofollow noopener">https://code.google.com/archive/p/drrsuite/downloads</a></p>
<p>There are also two VTK functions that may help:<br>
vtkFixedPointVolumeRayCastMapper<br>
vtkGPUVolumeRayCastMapper</p>
<p>If they do not work for you, you can check some journal papers on Digitally Reconstructed Radiograph (DRR). I saw that they were trying to solve the same problem as yours.</p>
<p>Hope this help.<br>
Manh</p>

---

## Post #5 by @shahrokh (2024-08-04 12:02 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="7493">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>Hi Dear 3DSlicer developers</p>
</blockquote>
</aside>
<p>Hi Dear 3DSlicer and Plastimatch developers,<br>
I apologize for bringing up my question again after 5 years.<br>
Let’s assume that the file stack.mha has the following specifications:</p>
<pre><code class="lang-auto">$ plastimatch header stack.mha
Type = short
Planes = 1
Origin = -249.5117 -459.5117 -921.4000
Size = 512 512 72
Spacing = 0.9766 0.9766 3.0000
Direction = 1.0000 0.0000 0.0000 0.0000 1.0000 0.0000 0.0000 0.0000 1.0000
$
</code></pre>
<p>Now, I have calculated DRR image and the related ray tracing information using the following command.</p>
<pre><code class="lang-auto">$ plastimatch drr --nrm "0 -1 0" --vup "0 0 1" --sid 940 --sad 535 -r "512 512" -z "899.588785047 899.588785047" -c "256 256" -o "-0.4787000 -210.4787 -816.4000" --raytrace-details -I stack.mha -i uniform -O DRRSample -t pfm
I/O time: 0.000524 sec
Total time: 59.2702 secs
$ ll -h
...
-rw-rw-r-- 1 sn sn 1.1M Aug  4 13:33  DRRSample0000.pfm
-rw-rw-r-- 1 sn sn  913 Aug  4 13:33  DRRSample0000.txt
-rw-rw-r-- 1 sn sn 2.6G Aug  4 13:33  -I0000.txt
-rw-rw-r-- 1 sn sn  17M Jul  6 11:48  stack.mha
$ vi -I0000.txt
...
</code></pre>
<p>The ray tracing information has been saved in the file <code>-I0000.txt</code>. The contents of this file are extensive, as follows:</p>
<pre><code class="lang-auto">51,0,0,0,0,0.732422,0,0
51,1,0,0,0,0.732422,0,0
51,2,0,0,0,0.732422,0,0
51,3,0,0,0,0.732422,0,0
51,4,0,0,0,0.732422,0,0
51,5,0,0,0,0.732422,0,0
51,6,0,0,0,0.732422,0,0
51,7,0,0,0,0.732422,0,0
51,8,0,0,0,0.732422,0,0
51,9,0,0,0,0.732422,0,0
...
455,503,1,0,0,0.732422,0,0
455,504,0,0,0,0.732422,0,0
455,504,1,0,0,0.732422,0,0
455,505,0,0,0,0.732422,0,0
455,505,1,0,0,0.732422,0,0
455,506,0,0,0,0.732422,0,0
455,506,1,0,0,0.732422,0,0
455,507,0,0,0,0.732422,0,0
455,507,1,0,0,0.732422,0,0
455,508,0,0,0,0.732422,0,0
455,508,1,0,0,0.732422,0,0
455,509,0,0,0,0.732422,0,0
455,509,1,0,0,0.732422,0,0
455,510,0,0,0,0.732422,0,0
455,510,1,0,0,0.732422,0,0
455,511,0,0,0,0.732422,0,0
455,511,1,0,0,0.732422,0,0
$
</code></pre>
<p>Please explain the eight parameters of each row for me.</p>
<p>I imagine the first parameter corresponds to the Ray ID. If my understanding is correct, why does it start from number 51 and end at 455? Similarly, what are the other parameters?</p>
<p>My ultimate goal is to use this ray tracing information to track each ray passing through a 3D CT matrix. I intend to determine the Hounsfield number of each voxel (from the ray tracing data), then calculate the angle of incidence of the ray with that voxel. Subsequently, based on the Hounsfield number, I will adjust the scattering kernel computed from Monte Carlo simulation according to the calculated angle, and apply it to the voxel position.</p>
<p>Another objective is to utilize this information to identify edge voxels of the RTPlan radiation field.</p>
<p>Please guide me on these matters.<br>
Your sincerely.<br>
Shahrokh</p>

---
