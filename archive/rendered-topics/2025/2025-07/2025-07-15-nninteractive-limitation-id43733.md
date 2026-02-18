# nnInteractive limitation

**Topic ID**: 43733
**Date**: 2025-07-15
**URL**: https://discourse.slicer.org/t/nninteractive-limitation/43733

---

## Post #1 by @Sebastiets (2025-07-15 16:27 UTC)

<p>Hi, I’m currently exploring the use of nnInteractive slicer’s version and noticed that the segmentation cuts pretty steaply not finishing the segmentation of the tibia or femur for example. Maybe Andras or Steve could tell me if there’s a number of slicer or voxel limitation and if it’s possible to overpass this limitation so I can segment my full bones.</p>
<p>On a side note, for people having difficulties installing and starting the server for the extension on Windows, I found a work around until the main GitHub founds a more optimize solution, so let me know if you need my instructions on the subject.</p>
<p>Have a nice day!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4eb64cfd13c034ff3cb9ce4768752b1b27e81115.jpeg" data-download-href="/uploads/short-url/bejOQVRw6pD1qCBzmubLiLofnvf.jpeg?dl=1" title="nnInteractive limitation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4eb64cfd13c034ff3cb9ce4768752b1b27e81115_2_690x435.jpeg" alt="nnInteractive limitation" data-base62-sha1="bejOQVRw6pD1qCBzmubLiLofnvf" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4eb64cfd13c034ff3cb9ce4768752b1b27e81115_2_690x435.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4eb64cfd13c034ff3cb9ce4768752b1b27e81115_2_1035x652.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4eb64cfd13c034ff3cb9ce4768752b1b27e81115_2_1380x870.jpeg 2x" data-dominant-color="999DCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">nnInteractive limitation</span><span class="informations">2878×1816 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For exemple with image representing a whole femur. When prompt the head, it loads the orange section. If asked lower, it’s the green section and stopping at the mid point of the scrobbly section. When prompt a second point on the same segmentation, it joins the segments with this ugly and none accurate finish.</p>

---

## Post #2 by @muratmaga (2025-07-15 16:33 UTC)

<p>Like any user guided tool, NNinteractive will not give you a perfect segmentation in the first attempt. But there are no inherent limits to it (beyond your GPU size, if you are using the GPU version). You need to “guide” the segmentation by providing positive (parts belong) and negative (parts don’t belong) to the segment. You also chose to segment head as a different segment, so it kind of makes sense for it not to extend it below the other segment.</p>
<p>I suggest merging these two segments, and then adding positive scribble to that missing section, and negative scribbles to the erroneous part in the middle.</p>

---

## Post #3 by @pieper (2025-07-15 17:16 UTC)

<p>Have you looked at the image data in that region?  I suspect there’s a gap in the volume.</p>

---

## Post #4 by @Sebastiets (2025-07-15 17:40 UTC)

<p>I chose to do a first segmentation at the head to show that it stops and don’t do the full bone.</p>
<p>Green parts are to show the effect of two consecutive segmentation and the finish that it gives. The  example on the GitHub shows longer segmentation with the tool and I tried with a RTX 2080 TI, 5070 super and 5090 and same length, so no effect on the vram or GPu limitation.</p>

---

## Post #5 by @Sebastiets (2025-07-15 18:01 UTC)

<p>There’s no gap in the image. I could select any spots in the femur or tibia and it stops with a straight limit. Images will help to show I think.</p>
<p>The femur is scribble for all parts, but only the diaphyse is cutout<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc3d465fea10f6e78b01f0cdc7ebc43563213b2f.jpeg" data-download-href="/uploads/short-url/vqkk6SaoukgG9MRljuGMphqWfFl.jpeg?dl=1" title="Femur with scribble marks" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc3d465fea10f6e78b01f0cdc7ebc43563213b2f_2_690x450.jpeg" alt="Femur with scribble marks" data-base62-sha1="vqkk6SaoukgG9MRljuGMphqWfFl" width="690" height="450" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc3d465fea10f6e78b01f0cdc7ebc43563213b2f_2_690x450.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc3d465fea10f6e78b01f0cdc7ebc43563213b2f_2_1035x675.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc3d465fea10f6e78b01f0cdc7ebc43563213b2f_2_1380x900.jpeg 2x" data-dominant-color="33333C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Femur with scribble marks</span><span class="informations">2878×1878 275 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
when adding points on the epiphyses, it does segment<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b7c04b3dd1aea3d4c3c734ea681a196357bc6e7.png" data-download-href="/uploads/short-url/aLLw8MMOE5sJ3IaC96DSGacV7Yb.png?dl=1" title="full femur with 1 x scribble and 2 x point" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b7c04b3dd1aea3d4c3c734ea681a196357bc6e7_2_690x420.png" alt="full femur with 1 x scribble and 2 x point" data-base62-sha1="aLLw8MMOE5sJ3IaC96DSGacV7Yb" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b7c04b3dd1aea3d4c3c734ea681a196357bc6e7_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b7c04b3dd1aea3d4c3c734ea681a196357bc6e7_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b7c04b3dd1aea3d4c3c734ea681a196357bc6e7_2_1380x840.png 2x" data-dominant-color="9A9DD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">full femur with 1 x scribble and 2 x point</span><span class="informations">1438×876 22.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Same thing for femur<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46dfc79e5f654cd740fdcb285ebf7f1349995476.png" data-download-href="/uploads/short-url/a6YRRSTfAYDXMhIoKDJDV7WjWjc.png?dl=1" title="full tibia with 1 x scribble and 2 x point" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46dfc79e5f654cd740fdcb285ebf7f1349995476_2_690x420.png" alt="full tibia with 1 x scribble and 2 x point" data-base62-sha1="a6YRRSTfAYDXMhIoKDJDV7WjWjc" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46dfc79e5f654cd740fdcb285ebf7f1349995476_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46dfc79e5f654cd740fdcb285ebf7f1349995476_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46dfc79e5f654cd740fdcb285ebf7f1349995476_2_1380x840.png 2x" data-dominant-color="999DCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">full tibia with 1 x scribble and 2 x point</span><span class="informations">1438×876 45.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ae752a88883597a1b6d76a0d440b6efe3187b48.jpeg" data-download-href="/uploads/short-url/8p5iCh1qakhbIxoZB80A2pUyvoI.jpeg?dl=1" title="tibia with scribble marks" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3ae752a88883597a1b6d76a0d440b6efe3187b48_2_690x450.jpeg" alt="tibia with scribble marks" data-base62-sha1="8p5iCh1qakhbIxoZB80A2pUyvoI" width="690" height="450" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3ae752a88883597a1b6d76a0d440b6efe3187b48_2_690x450.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3ae752a88883597a1b6d76a0d440b6efe3187b48_2_1035x675.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3ae752a88883597a1b6d76a0d440b6efe3187b48_2_1380x900.jpeg 2x" data-dominant-color="33343D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">tibia with scribble marks</span><span class="informations">2878×1878 272 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Previous exemple was only done with axial oriented point markup, so scribbling seems to help</p>

---

## Post #6 by @muratmaga (2025-07-15 18:12 UTC)

<aside class="quote no-group" data-username="Sebastiets" data-post="5" data-topic="43733">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sebastiets/48/80354_2.png" class="avatar"> Sebastiets:</div>
<blockquote>
<p>so scribbling seems to help</p>
</blockquote>
</aside>
<p>Yes, that’s exactly how you should use it. You need to guide the segmentation. It doesn’t know what a femur (or any other structure) looks like. It just knows things like edges, boundaries, curves. And you need to help it.</p>

---

## Post #7 by @Sebastiets (2025-07-16 14:49 UTC)

<p>Yes, but still limiting to diaphyse part of the bone. Almost exactly the same slice each time. My main question was to know if there was a voxel limitation. Steve answered.</p>
<p>Thanks</p>

---

## Post #8 by @lassoan (2025-07-16 20:25 UTC)

<p>nnInteractive has an auto-zoom feature that should help with getting a complete segmentation of a structure most of the time. From the <a href="https://arxiv.org/pdf/2503.08373">nnInteractive paper</a>:</p>
<blockquote>
<p>nnInteractive dynamically expands the region of interest (ROI) based on prediction borders, iteratively zooming out by a factor of 1.5 until the object is fully captured (up to 4× zoom out)</p>
</blockquote>
<p>It is a heuristic method, so it is not guaranteed to always work perfectly, and whenever encounter oversegmentation or undersegmentation then you can just add additional hints to include less or more.</p>
<p>However, it could be possible to slightly adjust the auto-zoom method to work well for your case. Your case is a bit unusual in that the bone is very long and it is only a thin shell. At the zoom level where the complete bone would be visible in one patch, the cortical bone might become less than a single voxel thick or it may not separable from other bones. It could be a good test case for the auto-zoom method, so I would suggest to submit it to the <a href="https://github.com/MIC-DKFZ/nnInteractive">nnInteractive project issue tracker</a>.</p>

---

## Post #9 by @Sebastiets (2025-07-17 14:24 UTC)

<p>Thanks for your clear answer! I’ll submit an issue on their repository.</p>
<p>This scan is also a test scan to test my method while waiting for the official scans from the hospital, so with a better scan, might work better.</p>

---

## Post #10 by @Sebastiets (2025-07-17 15:13 UTC)

<p>Also, I noticed that from the results I get with TotalSegmentator, nnInteractive has a smoother finish as if it was applying a smoothing mask after the segmentation. I know TotalSegmentator use a binary method of including a voxel or not in the segment, but I’m not sure of the way nnInteractive gets to this smoothness from the first try.</p>
<p>Here’s the result with TotalSegmentator just to show the difference of quality.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5fbd07070b331ad8a018a5d3710c0ab70fbce05.jpeg" data-download-href="/uploads/short-url/sfrzpuq5v0XYS4RwuiLDE4FL8s5.jpeg?dl=1" title="TotalSegmentator 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5fbd07070b331ad8a018a5d3710c0ab70fbce05_2_690x431.jpeg" alt="TotalSegmentator 1" data-base62-sha1="sfrzpuq5v0XYS4RwuiLDE4FL8s5" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5fbd07070b331ad8a018a5d3710c0ab70fbce05_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5fbd07070b331ad8a018a5d3710c0ab70fbce05_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5fbd07070b331ad8a018a5d3710c0ab70fbce05_2_1380x862.jpeg 2x" data-dominant-color="9A9ED1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">TotalSegmentator 1</span><span class="informations">2904×1816 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
