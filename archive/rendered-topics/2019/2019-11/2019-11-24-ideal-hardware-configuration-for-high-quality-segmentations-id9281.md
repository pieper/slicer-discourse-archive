# Ideal hardware configuration for high quality segmentations

**Topic ID**: 9281
**Date**: 2019-11-24
**URL**: https://discourse.slicer.org/t/ideal-hardware-configuration-for-high-quality-segmentations/9281

---

## Post #1 by @apparrilla (2019-11-24 09:02 UTC)

<p>We are working with CT scan source images to segment bone. High resolution segments are needed. Each source Cropped Volume is around 1400x600x300 px. Grow from seeds is our actual approach.</p>
<p>Actual configuration:</p>
<ul>
<li>Operating system: Win10</li>
<li>Slicer version: 4.11.0-2019-11-15 r28624</li>
<li>Graphic card: Nvidia GTX 1060 6G</li>
<li>RAM: 48Gb DDR3 1333</li>
<li>2x Xeon E5 2670</li>
<li>SATA 3 SSD 240Gb</li>
</ul>
<p>Each segmentation made with Grow from seeds takes around 10 min. Any paint tast to improve/fix segments takes around a minute so autoupdate is not very usable. Other edit segment tools are affected. Margin Tool - Grow is a full night task, for example.</p>
<p>Checking system monitor, we saw some interesting items:</p>
<ul>
<li>Just one core is 100%, the others are most 0%</li>
<li>RAM is almost full</li>
<li>Main thread is almost blocked.</li>
</ul>
<p>Questions:</p>
<ul>
<li>How can we improve/change hardware for ideal configuration?</li>
<li>Have CUDA drivers any role in this task? Which is best Nvidia Driver?</li>
<li>Any application setting change could improve computation times?</li>
</ul>
<p>Thanks on advance!</p>

---

## Post #2 by @lassoan (2019-11-24 19:32 UTC)

<p>RAM almost full is probably the main issue. Could you please try how the performance changes if you slightly crop/downscale the image before segmentation using Crop volume module?</p>
<p>Grow from seeds builds a graph representation of the image, which currently requires about 80 bytes per voxel, that’s why the memory usage jumps up so much. We could probably reduce it by about 50% without significant change in the algorithm. If indeed memory usage is the main culprit then this could help a lot.</p>
<p>What kernel size do you use for the margin tool?</p>

---

## Post #3 by @apparrilla (2019-11-24 20:24 UTC)

<p>I’m going to make some tries with different amounts of RAM and I send you the benchmark…<br>
I use about 3-5mm of margin.</p>

---

## Post #4 by @apparrilla (2019-11-24 21:43 UTC)

<p>Kernel size in margin tool is from 50x50x20 to 100x100x40 aprox…</p>

---

## Post #5 by @lassoan (2019-11-24 21:43 UTC)

<p>What is the main size in voxels? (it should be displayed in the effect, or you can compute by dividing margin size in mm by the size of one voxel)</p>

---

## Post #6 by @apparrilla (2019-11-24 21:52 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6958ffa749dfe7deca5bdae92f55a140606be35a.png" data-download-href="/uploads/short-url/f1WOpCGRm0XSGWDFp795KtIZhN0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6958ffa749dfe7deca5bdae92f55a140606be35a.png" alt="image" data-base62-sha1="f1WOpCGRm0XSGWDFp795KtIZhN0" width="690" height="277" data-dominant-color="F5F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">729×293 5.54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2019-11-24 21:55 UTC)

<p>If you use such a huge kernel for margin then it means that you lose all the small details in the image. You might get equivalent results by downsampling the input by a factor of 5 along each axis (reducing memory need by a factor of 100x). Try Crop volume module with setting spacing scale to 5.0 to create a downsampled image and segment that.</p>

---

## Post #8 by @apparrilla (2019-11-24 22:19 UTC)

<p>Ok. I will do a new segmentation from a less resolution source volumen, aply margin and send the segmented item to the high resolution segmentation… It´s a bit tricky but i think it should work. Is there other way to make a low resolution growth from a segment?</p>
<p>On the other hand, recovering initial question about Grow from seeds. How can I tried this “non significant change in the algorithm”? <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=9" title=":grin:" class="emoji" alt=":grin:"></p>
<p>Thanks.</p>

---

## Post #9 by @lassoan (2019-11-24 23:03 UTC)

<p>Is margin effect a final step in your workflow? If it is then it means there there will be no fine details in your segmentation results, so you may just as well do the complete segmentation workflow on a lower-resolution volume.</p>
<p>What kind of data you work with? What do you need to segment? Why do you need the huge margin?</p>
<aside class="quote no-group" data-username="apparrilla" data-post="8" data-topic="9281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>recovering initial question about Grow from seeds. How can I tried this “non significant change in the algorithm”?</p>
</blockquote>
</aside>
<p>We could change indices to use 32-bit indexes instead of the current 64-bit indexes and 64-bit pointers. That could reduce memory usage by about about a factor of 2x. However, if you can increase spacing scale by 2.0 (and still get appropriate results) then memory usage would drop by a factor of 8x (and scale of 5.0 would result in 125x less memory used).</p>

---

## Post #10 by @apparrilla (2019-11-24 23:18 UTC)

<p>Margin Effect:<br>
I need a high resolution source volumen because I want high accuracy bone segmentations. I need to grow some segments to make logical operations and combine them with the others. This is the reason not to downsample segmentation.</p>
<p>Grow from Seeds:<br>
Reason is the same. If I drop/copy a low resolution segment to the high resolution segmentation, surface is not smooth (stepped surface)</p>
<p>Thanks for your patience and support.</p>

---

## Post #11 by @lassoan (2019-11-24 23:23 UTC)

<p>Can you post a few screenshots so that we can have an idea about the kind of images you work with? Is the spacing of the image isotropic? Have you tried <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">WrapSolidify</a> effect to fix discontinuities?</p>

---

## Post #12 by @apparrilla (2019-11-24 23:57 UTC)

<p>This is inicial high resolution segment (after grow from seeds)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/4167814067fe766c16ec475327dae9505e0f8fc0.jpeg" data-download-href="/uploads/short-url/9kANdih550KKPKOALj0X2QIWDjq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4167814067fe766c16ec475327dae9505e0f8fc0_2_318x250.jpeg" alt="image" data-base62-sha1="9kANdih550KKPKOALj0X2QIWDjq" width="318" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4167814067fe766c16ec475327dae9505e0f8fc0_2_318x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4167814067fe766c16ec475327dae9505e0f8fc0_2_477x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4167814067fe766c16ec475327dae9505e0f8fc0_2_636x500.jpeg 2x" data-dominant-color="A5A0B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">781×613 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I make a new low resolution segmentation and copy segment to it. I apply gaussian smooting and margin grow 6mm. “Show 3d Surface Smoothing” is ON because “you send what you see”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74bbda15df381658c0e87904c65bb58f01a4db2e.jpeg" data-download-href="/uploads/short-url/gEFR9RhNdYZlJoix4qAKEcRgOxo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/74bbda15df381658c0e87904c65bb58f01a4db2e_2_318x250.jpeg" alt="image" data-base62-sha1="gEFR9RhNdYZlJoix4qAKEcRgOxo" width="318" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/74bbda15df381658c0e87904c65bb58f01a4db2e_2_318x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/74bbda15df381658c0e87904c65bb58f01a4db2e_2_477x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/74bbda15df381658c0e87904c65bb58f01a4db2e_2_636x500.jpeg 2x" data-dominant-color="8994AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">875×687 56 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Copy back it to the high resolucion segmentation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29d5c85be02475d6203a39ed7e915cac6f3a7509.jpeg" data-download-href="/uploads/short-url/5Y5BpSMYOGxitT8BNKXMBzsub4R.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29d5c85be02475d6203a39ed7e915cac6f3a7509_2_315x250.jpeg" alt="image" data-base62-sha1="5Y5BpSMYOGxitT8BNKXMBzsub4R" width="315" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29d5c85be02475d6203a39ed7e915cac6f3a7509_2_315x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29d5c85be02475d6203a39ed7e915cac6f3a7509_2_472x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29d5c85be02475d6203a39ed7e915cac6f3a7509_2_630x500.jpeg 2x" data-dominant-color="8794AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">822×651 65.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When you make any change in this segment, for example, cutting it:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00ffd80f59a85ff41a6749030b9a2259b2d29ca8.png" data-download-href="/uploads/short-url/8Q8SuwoPxW5xVVOFCaRpQtYetW.png?dl=1" title="4_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00ffd80f59a85ff41a6749030b9a2259b2d29ca8_2_317x250.png" alt="4_2" data-base62-sha1="8Q8SuwoPxW5xVVOFCaRpQtYetW" width="317" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00ffd80f59a85ff41a6749030b9a2259b2d29ca8_2_317x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00ffd80f59a85ff41a6749030b9a2259b2d29ca8_2_475x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00ffd80f59a85ff41a6749030b9a2259b2d29ca8_2_634x500.png 2x" data-dominant-color="8A95AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4_2</span><span class="informations">893×703 91.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
“Show 3d Surface Smoothing” is ON in the high resolution segmentation too.<br>
I don´t know why is so good looking at begining but it decrease quality when you make any change on it.</p>

---

## Post #13 by @lassoan (2019-11-25 00:59 UTC)

<aside class="quote no-group" data-username="apparrilla" data-post="12" data-topic="9281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>I don´t know why is so good looking at begining but it decrease quality when you make any change on it.</p>
</blockquote>
</aside>
<p>When you copy a high-resolution segment to a low-resolution segmentation then the segment is not converted immediately, only when needed (e.g., when the segment is edited). If the segmentation’s resolution is isotropic (spacing is the same along all axes) then surface smoothing can remove step artifacts without losing details.</p>

---

## Post #14 by @apparrilla (2019-11-25 06:29 UTC)

<p>Both source volumes are made in isotropic way from begining.<br>
Low resolution segmentation is making good job with sended segment as you see in images. The real problem is from low to high resolution segmentation.<br>
I have tried to export smoothed low resolution segment as stl and import it again to high resolution segmentation and quality is as perfect as expected (but i have to turn 180º model with a transform). Tricky workflow but effective.</p>
<p>Thanks.</p>

---

## Post #15 by @lassoan (2019-11-25 13:56 UTC)

<aside class="quote no-group" data-username="apparrilla" data-post="14" data-topic="9281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>I have tried to export smoothed low resolution segment as stl and import it again to high resolution segmentation and quality is as perfect as expected (but i have to turn 180º model with a transform)</p>
</blockquote>
</aside>
<p>Why do you need to export and reimport to file?<br>
If you export in RAS coordinate system then there is no need for LPS-&gt;RAS conversion after import (180deg rotation).</p>

---

## Post #16 by @Chris_Rorden (2019-11-25 21:15 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> your comments regarding cropping and downsampling for the current robust solution are all spot on. If anyone wants to devote the engineering time for a faster solution, you might want to explore the <a href="http://cs.brown.edu/people/pfelzens/dt/" rel="nofollow noopener">Felzenszwalb and Huttenlocher</a> method for computing Euclidean Distance Transforms. This is elegantly described by <a href="https://prideout.net/blog/distance_fields/" rel="nofollow noopener">Philip Rideout</a> who provides elegant <a href="https://prideout.net/snowy/" rel="nofollow noopener">Python code</a>. This method is far faster than computing erosion, providing a separable filter for each of dimension. For each dimension, you can compute the rows in parallel, leveraging multiple CPUs.</p>
<p>I provide a sample project <a href="https://github.com/neurolabusc/DistanceFields" rel="nofollow noopener">Thick3D</a> that demonstrates parallel acceleration and can work with NIfTI and NRRD input. Since the code handles parallel threading, anisotropic images and other situations, it is not as elegant as Rideout’s code for porting into Slicer3D, but it fully demonstrates the potential for solving these problems with tremendous speed and with very little RAM.</p>
<p>Its not a one-to-one replacement for the current algorithm - it is really designed for binary images. However, it might provide a real-time method for some situations.</p>

---

## Post #17 by @dzenanz (2019-11-25 21:29 UTC)

<p><a href="https://github.com/KitwareMedical/HASI/blob/fe38e0f08682fd3ba2fd9ec816118b844321fdb8/segmentBonesInMicroCT.cxx#L102-L155" rel="nofollow noopener">This code</a> is ready to be stolen. As <code>Maurer</code>, <code>Not</code> and <code>Threshold</code> filters are parallelized, this should scale with number of CPU cores, which is not the case with regular morphology. Not to mention that the size of radius mostly doesn’t matter for computation time.</p>

---

## Post #18 by @apparrilla (2019-11-25 23:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="9281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Why do you need to export and reimport to file?</p>
</blockquote>
</aside>
<p>Sending segment LOW–&gt;HIGH segmentation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00ffd80f59a85ff41a6749030b9a2259b2d29ca8.png" data-download-href="/uploads/short-url/8Q8SuwoPxW5xVVOFCaRpQtYetW.png?dl=1" title="4_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00ffd80f59a85ff41a6749030b9a2259b2d29ca8_2_317x250.png" alt="4_2" data-base62-sha1="8Q8SuwoPxW5xVVOFCaRpQtYetW" width="317" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00ffd80f59a85ff41a6749030b9a2259b2d29ca8_2_317x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00ffd80f59a85ff41a6749030b9a2259b2d29ca8_2_475x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00ffd80f59a85ff41a6749030b9a2259b2d29ca8_2_634x500.png 2x" data-dominant-color="8A95AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4_2</span><span class="informations">893×703 91.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Export LOW–&gt;STL + Import STL–&gt;HIGH:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee781e2f45d9e477b56900e20f3df3b4bb2aa828.png" data-download-href="/uploads/short-url/y1AZlfDzg4S2Q27zd6ab3qkSeGQ.png?dl=1" title="8" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee781e2f45d9e477b56900e20f3df3b4bb2aa828_2_335x250.png" alt="8" data-base62-sha1="y1AZlfDzg4S2Q27zd6ab3qkSeGQ" width="335" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee781e2f45d9e477b56900e20f3df3b4bb2aa828_2_335x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee781e2f45d9e477b56900e20f3df3b4bb2aa828_2_502x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee781e2f45d9e477b56900e20f3df3b4bb2aa828_2_670x500.png 2x" data-dominant-color="8491A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">8</span><span class="informations">943×703 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="9281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you export in RAS coordinate system then there is no need for LPS-&gt;RAS conversion after import (180deg rotation).</p>
</blockquote>
</aside>
<p>Right, it was a LPS STL, much easier in RAS format…</p>
<p>Thanks.</p>

---

## Post #19 by @lassoan (2019-11-26 18:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="9281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We could change indices to use 32-bit indexes instead of the current 64-bit indexes and 64-bit pointers. That could reduce memory usage by about about a factor of 2x.</p>
</blockquote>
</aside>
<p>I’ve updated Grow from seeds effect with these changes and did some performance optimizations. Now peak memory usage is about half than before and the effect is about 20% faster.</p>
<aside class="quote no-group" data-username="Chris_Rorden" data-post="16" data-topic="9281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>If anyone wants to devote the engineering time for a faster solution, you might want to explore the <a href="http://cs.brown.edu/people/pfelzens/dt/">Felzenszwalb and Huttenlocher </a> method for computing Euclidean Distance Transforms.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> <a class="mention" href="/u/dzenanz">@dzenanz</a> Thanks for the suggestions. We haven’t thought about using distance transforms for margin and hollow effect, but of course it makes complete sense.</p>
<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> do you know if Felzenswalb&amp;Huttenlocher or Rideout methods have any advantage over ITK’s distance map filters? Felzenswalb&amp;Huttenlocher writes this about Maurer’s method (one of the methods implemented in ITK):</p>
<blockquote>
<p>There are a number of other algorithms for computing the EDT of a binary image in linear-time (e. g., [18, 7, 17]); however these methods are quite involved and are not widely used in practice. In contrast, our algorithm is relatively simple, easy to implement, and very fast in practice.</p>
</blockquote>
<p>This is not just vague but even misleading, since for example ITK’s signed Maurer distance is used very widely. Considering obvious bias of the authors and absence of qualitative or quantitative comparison to established methods, I don’t feel much motivation to spend time with evaluating their method, but if <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> or others have first-hand experience then it would be great to learn about it.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> Could you look into using distance map images instead of vtkImageDilateErode3D in Segment editor? Not urgent, just when you can get to it. Simple distance map computation + thresholding (as shown in <a class="mention" href="/u/dzenanz">@dzenanz</a> example) should work. Since we don’t rely much on SimpleITK in Slicer core modules, it would be probably better not to add a dependency now, but instead add a new “vtkITKImageMargin” filter, which would offer erosion, dilation, and hollowing by wrapping the ITK filters. If morphological filter performance is better for small kernels then we might keep both methods and use morphological operators for small kernel sizes and switch to distance map for large kernels.</p>

---

## Post #20 by @Chris_Rorden (2019-11-27 17:32 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I suspect the Maurer method performs similarly to F&amp;H. Several groups seem to have independently discovered separable ways to compute distance fields.  If you are interested in the different methods, the history of their discovery, as well as clever optimizations, I strongly recommend <a href="https://github.com/seung-lab/euclidean-distance-transform-3d" rel="nofollow noopener">William Silversmith’s Github project</a>. That page also notes a trick for accelerating the estimate for the first dimension using a simple forward and back sweep. Finally, Silversmith also describes how these algorithms can be modified to handle anisotropic images. This is important, as anisotropic images are typically not handled by erosion methods or these separable filters.</p>
<p>So while there are variations on these methods, and a few tricks to accelerate any implementation, I think all are much faster and have lower memory requirements than traditional methods. If the Maurer method is already available in a robust, parallelized form, I think that would be sufficient.</p>

---

## Post #21 by @apparrilla (2019-11-28 21:17 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I have tried  Linux nightly build and I suspect it isn´t updated. Doesn´t it or I´m doing something wrong?<br>
Thanks.</p>

---

## Post #22 by @lassoan (2019-11-28 22:03 UTC)

<p>Linux build should be up-to-date tomorrow (there was a build error).</p>

---

## Post #23 by @Sunderlandkyl (2019-12-03 18:53 UTC)

<p>I’ve added a WIP pull request that adds the vtkITK margin filter, and adapts the margin and hollow editor effects.</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/1274" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/1274" target="_blank" rel="nofollow noopener">ENH: Add vtkITK filter for computing label margins</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>Sunderlandkyl:vtkitk_margin</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2019-12-03" data-time="18:47:48" data-timezone="UTC">06:47PM - 03 Dec 19 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/Sunderlandkyl" target="_blank" rel="nofollow noopener">
          <img alt="Sunderlandkyl" src="https://avatars3.githubusercontent.com/u/9222709?v=4" class="onebox-avatar-inline" width="20" height="20">
          Sunderlandkyl
        </a>
      </div>

      <div class="lines" title="1 commits changed 5 files with 300 additions and 101 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/1274/files" target="_blank" rel="nofollow noopener">
          <span class="added">+300</span>
          <span class="removed">-101</span>
        </a>
      </div>
    </div>

  </div>
</div>
  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
