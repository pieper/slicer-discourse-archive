---
topic_id: 32096
title: "What Is The Best Way To Smoothing Totalsegmentator Result"
date: 2023-10-08
url: https://discourse.slicer.org/t/32096
---

# What is the best way to smoothing TotalSegmentator result?

**Topic ID**: 32096
**Date**: 2023-10-08
**URL**: https://discourse.slicer.org/t/what-is-the-best-way-to-smoothing-totalsegmentator-result/32096

---

## Post #1 by @zariliusra (2023-10-08 02:02 UTC)

<p>Hi, i used TotalSegmentator to segment tibial bone, but the result is not as smooth as using seed and growth, even after configure the smoothing factor into 1. Is there some procedure to make it smoother?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fde10ed324c4b09131ae26c0de0132f4512bb4c.png" data-download-href="/uploads/short-url/boxuFmD3ryEpQbtUJscOf4QNAw4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fde10ed324c4b09131ae26c0de0132f4512bb4c_2_610x500.png" alt="image" data-base62-sha1="boxuFmD3ryEpQbtUJscOf4QNAw4" width="610" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fde10ed324c4b09131ae26c0de0132f4512bb4c_2_610x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fde10ed324c4b09131ae26c0de0132f4512bb4c_2_915x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fde10ed324c4b09131ae26c0de0132f4512bb4c.png 2x" data-dominant-color="9899CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">964×789 63.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Deep_Learning (2023-10-08 15:42 UTC)

<p>What do you want to do? Print? Visualize?</p>
<p>A) You are already looking at a smoothed version.<br>
You can turn off smoothing or increase the smoothing factor.<br>
This is only for visualization.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1e79e8464684187535e654fc727d36c66c27b9a.jpeg" data-download-href="/uploads/short-url/werFHULwgFAzSROzooQULqfiqq6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1e79e8464684187535e654fc727d36c66c27b9a_2_690x441.jpeg" alt="image" data-base62-sha1="werFHULwgFAzSROzooQULqfiqq6" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1e79e8464684187535e654fc727d36c66c27b9a_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1e79e8464684187535e654fc727d36c66c27b9a_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1e79e8464684187535e654fc727d36c66c27b9a_2_1380x882.jpeg 2x" data-dominant-color="9CA3A4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1229 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>B) You can use smoothing under segmentations (lots of options)<br>
This will smooth the mask pixel data.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc067d658eedbed7e0d21d88875ca6f0a9f5a6e9.jpeg" data-download-href="/uploads/short-url/qPlFt216cMrQGk8kUmONDFmrIHD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc067d658eedbed7e0d21d88875ca6f0a9f5a6e9_2_690x441.jpeg" alt="image" data-base62-sha1="qPlFt216cMrQGk8kUmONDFmrIHD" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc067d658eedbed7e0d21d88875ca6f0a9f5a6e9_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc067d658eedbed7e0d21d88875ca6f0a9f5a6e9_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc067d658eedbed7e0d21d88875ca6f0a9f5a6e9_2_1380x882.jpeg 2x" data-dominant-color="9EA4A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1229 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>C) You can convert to a model and then use the Surface Toolbox Module.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/047e6065332755de771f459e10779540f85192ff.jpeg" data-download-href="/uploads/short-url/DKFyW55sDgjjMjIOBixMZ27RGT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/047e6065332755de771f459e10779540f85192ff_2_690x441.jpeg" alt="image" data-base62-sha1="DKFyW55sDgjjMjIOBixMZ27RGT" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/047e6065332755de771f459e10779540f85192ff_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/047e6065332755de771f459e10779540f85192ff_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/047e6065332755de771f459e10779540f85192ff_2_1380x882.jpeg 2x" data-dominant-color="A1A6A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1229 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @rbumm (2023-10-08 22:45 UTC)

<p>There are several options in the segment editor, just experiment with what is best for your purpose.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cc47030b8af4aae828ed5ff64f7b0a7022b3f29.png" data-download-href="/uploads/short-url/8FzvWvWohqNH7zSi319DYDBsT9f.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cc47030b8af4aae828ed5ff64f7b0a7022b3f29_2_690x456.png" alt="image" data-base62-sha1="8FzvWvWohqNH7zSi319DYDBsT9f" width="690" height="456" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cc47030b8af4aae828ed5ff64f7b0a7022b3f29_2_690x456.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cc47030b8af4aae828ed5ff64f7b0a7022b3f29_2_1035x684.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cc47030b8af4aae828ed5ff64f7b0a7022b3f29.png 2x" data-dominant-color="CAC2C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1234×816 299 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
