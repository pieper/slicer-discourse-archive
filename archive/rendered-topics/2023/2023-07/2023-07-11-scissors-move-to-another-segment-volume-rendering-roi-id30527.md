# Scissors, move to another segment, volume rendering ROI

**Topic ID**: 30527
**Date**: 2023-07-11
**URL**: https://discourse.slicer.org/t/scissors-move-to-another-segment-volume-rendering-roi/30527

---

## Post #1 by @philippe (2023-07-11 18:27 UTC)

<p>Hello,</p>
<p>We are labelling structures near joints (e.g. intervertebral, mandibular, some costovertebral) to initialise grow from seeds. I have a couple of questions about a possible process.</p>
<p>It could be quicker to work in the 3D view. We use painting including spheres on the 3D view but it is limited away from the surface. We use scissors in 3D as well but the background/depth etc. seems difficult to manage in 3D (variable sizes etc).</p>
<ol>
<li>We could paint the whole region (big sphere) and then use scissors to isolate the structures. It could be done after a couple of rotate</li>
</ol>
<p>I see scissors can delete but is there any way to move what is selected to another segment (one now displayed at the time)?<br>
If it could, then the convex structure could be moved (“shaved”) to structure 1 (here: skull) and the remaining would be moved to structure 2.<br>
(image 1 below).</p>
<p>This segmentation process could be quite general.<br>
Any workaround or fast similar approaches?<br>
(besides doing the job twice : once adding and once deleting, which does not unsure the consistency)</p>
<ol start="2">
<li>Volume Rendering has a ROI to crop the area of interest (e.g. joint). It would then also be easy with a couple of rotate to label a structure using scissors (especially with a convex surface) and would have the advantage of color (image 2). But unfortunately, the ROI is not considered by the scissors (image 3).<br>
Any way to make scissors consider the ROI (=not to paint outside)? Or alternatives ?<br>
(It seems that 1 is more important)</li>
</ol>
<p>Thanks for any suggestion!<br>
Philippe</p>
<p>Image 1: scissors could be more useful if able to move to another segment not currently visible (an area could be segmented away with a couple of rotate).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/519c8cfa73f2a68d692c17a95e53eb327b9b88dd.png" data-download-href="/uploads/short-url/bDY5aGYWh4DwilSIMQZmxi4I6g5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/519c8cfa73f2a68d692c17a95e53eb327b9b88dd_2_690x237.png" alt="image" data-base62-sha1="bDY5aGYWh4DwilSIMQZmxi4I6g5" width="690" height="237" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/519c8cfa73f2a68d692c17a95e53eb327b9b88dd_2_690x237.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/519c8cfa73f2a68d692c17a95e53eb327b9b88dd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/519c8cfa73f2a68d692c17a95e53eb327b9b88dd.png 2x" data-dominant-color="C1C7C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1030×354 99.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Image 2: mandibular joint volume rendering with ROI. A scissors and a couple of rotate could label the skull and it is quite visual.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6043a895751cdec1804288510bdc134542dd0d0.png" alt="image" data-base62-sha1="sfJB8Ac9EhNR8LalmjPiZ0l8bug" width="339" height="272"><br>
Image 3: however, scissors do not consider ROI<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26b5e5669eb136439600273b3ff75aa8375b8398.png" alt="image" data-base62-sha1="5wrQYzB6K71S7IUCHop9Rhn7udy" width="298" height="300"></p>

---

## Post #2 by @muratmaga (2023-07-12 02:55 UTC)

<aside class="quote no-group" data-username="philippe" data-post="1" data-topic="30527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/f14d63/48.png" class="avatar"> philippe:</div>
<blockquote>
<p>This segmentation process could be quite general.<br>
Any workaround or fast similar approaches?<br>
(besides doing the job twice : once adding and once deleting, which does not unsure the consistency)</p>
</blockquote>
</aside>
<p>This is already doable. Create a blank segment where you want to move the cut region into. Then, in addition to fill option, make sure EEditable area option of masking choices is set to segment_XXX, in which segment_XXX is the segment where you have the original segment on which you want to use the scissors tool on.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ad2d3fda02166f49baf85091b1e5294cad3ece9.png" data-download-href="/uploads/short-url/66PKyhYcllxKbulLgmM3iS9sRlf.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ad2d3fda02166f49baf85091b1e5294cad3ece9_2_690x454.png" alt="image" data-base62-sha1="66PKyhYcllxKbulLgmM3iS9sRlf" width="690" height="454" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ad2d3fda02166f49baf85091b1e5294cad3ece9_2_690x454.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ad2d3fda02166f49baf85091b1e5294cad3ece9_2_1035x681.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ad2d3fda02166f49baf85091b1e5294cad3ece9_2_1380x908.png 2x" data-dominant-color="AEAEAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2262×1490 990 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="philippe" data-post="1" data-topic="30527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/f14d63/48.png" class="avatar"> philippe:</div>
<blockquote>
<p>Volume Rendering has a ROI to crop the area of interest (e.g. joint). It would then also be easy with a couple of rotate to label a structure using scissors (especially with a convex surface) and would have the advantage of color (image 2). But unfortunately, the ROI is not considered by the scissors (image 3).</p>
</blockquote>
</aside>
<p>This is not possible, as volume rendering is not a segmentation technique. But you can use the ROI in context of other tools, such as Local Threshold.</p>

---

## Post #3 by @philippe (2023-07-12 08:02 UTC)

<p>Hello Murat,</p>
<p>Thanks a lot. The editable area solves it completely…</p>
<p>I will initialize regions of interest (joints here) in a buffer segment and then move to the two destination segments using scissors. The mandibular joint example from above after a few rotates/scissors.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9197486aeb8d1c2f774c665bc90a4075a738fc8.jpeg" alt="image" data-base62-sha1="zxDqvKiMlZkBWwiIaGSGjT2o0Dm" width="565" height="470"></p>
<p>Regarding the volume rendering:<br>
I was not clear. Sorry. I know it is not something to be segmented but it is really useful to work in 3D with bone in CT when coupled with a threshold used as a mask and Show 3D enabled. “painting” the volume rendering (i.e. using it to position the mouse) paints the mask which appears in 3D over the volume rendering.  Illustration below (can’t find the youtube video on the ankle in which it was shown).</p>
<p>I’ll just continue to use that but to initialize the buffer segment before dispatching the two parts using Editable area. I find it considerably faster than working in the slices.</p>
<p>Thanks<br>
Philippe</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a233750ed4d37f75e2c0301058e0478a3dba311f.jpeg" alt="image" data-base62-sha1="n8TB0oSWtP9AkKbrESX2slLH807" width="450" height="448"></p>

---
