# display incorrectly when two volume rendering  by3D slicer 4.10.0

**Topic ID**: 4669
**Date**: 2018-11-07
**URL**: https://discourse.slicer.org/t/display-incorrectly-when-two-volume-rendering-by3d-slicer-4-10-0/4669

---

## Post #1 by @morewd (2018-11-07 12:29 UTC)

<p>Problem report for Slicer 4.10.0 win-amd64: [please describe expected and actual behavior]<br>
Problem report for Slicer 4.10.0 win-amd64: [please describe expected and actual behavior]<br>
the 3d slicer 4.10.0 can render two volumes at same time. It is really important function for me. But when I use this function, I find the display is not correctly.My setting is following：<br>
1，OS：windows 10 professional X64 with latest update;<br>
2, 3D slicer version:4.10.0 released and 4.11.0 nightly.<br>
3, data: CTchest.<br>
4, input two CTchest volumes . first volume use preset"CT-lung" and the second  use “CT-AAA”.And then let these two volumes display in one windows.<br>
5,problem:  the lung should be around by rips.But when rotate the sense ,the lung is always on foreground . The rips can not be displayed correctly. the snapshot is attached:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/057c7ca84343cb6807b537d2b78b103138544b73.jpeg" data-download-href="/uploads/short-url/Mx6a4XsZeA484ubRgvCN2XxBpF.jpeg?dl=1" title="twovolumes%20render" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/057c7ca84343cb6807b537d2b78b103138544b73_2_690x377.jpeg" alt="twovolumes%20render" data-base62-sha1="Mx6a4XsZeA484ubRgvCN2XxBpF" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/057c7ca84343cb6807b537d2b78b103138544b73_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/057c7ca84343cb6807b537d2b78b103138544b73_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/057c7ca84343cb6807b537d2b78b103138544b73_2_1380x754.jpeg 2x" data-dominant-color="A2A8C5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">twovolumes%20render</span><span class="informations">1920×1050 316 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2018-11-07 12:56 UTC)

<p>For multiple visible volumes you need to use the new rendering mode:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea36c89d4fa9dafa518276b1a7609944fb83509a.png" alt="image" data-base62-sha1="xpX6idNdnv9AxfvSzI0wPYuuC7w" width="483" height="60"></p>
<p>Should be:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e90f5c4130bd4f4bbbb5289c0d3cab1cb7be2623.jpeg" alt="image" data-base62-sha1="xfK9VfAkxD2ucrdoHKUlUDHCDXt" width="315" height="81"></p>

---

## Post #3 by @lassoan (2018-11-07 22:09 UTC)

<p>Multi-volume renderer currently does not support shading, so the images will not look surface-like. Until this feature is implemented, you can segment all additional structures using Segment editor module and show them in 3D. Some structures, such as bones and devices should be easy to segment (using threshold effect, optionally followed by some smoothing, cutting, etc.), while others might be more difficult.</p>

---

## Post #4 by @morewd (2018-11-08 03:20 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a><br>
thanks to response. Now dispaly  is correct  when rendering change to VTK Multi-Volume(experimental).And  it is pretty work for me.Thanks for all developers! But the rendering quality is different between "VTK multi-volume(experimental) " and “VTK-GPU ray casting”. I think “VTK-GPU ray casting” is better .</p>
<p>rendering by VTK multi-volume(experimental) :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e920202a51887b23619d0d5d060f753be5aaf401.jpeg" data-download-href="/uploads/short-url/xgk4VzrLcQfp5JS0D9qcrAD2hgZ.jpeg?dl=1" title="VTK%20multi-volume%EF%BC%88experimental%EF%BC%89" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e920202a51887b23619d0d5d060f753be5aaf401_2_690x377.jpeg" alt="VTK%20multi-volume%EF%BC%88experimental%EF%BC%89" data-base62-sha1="xgk4VzrLcQfp5JS0D9qcrAD2hgZ" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e920202a51887b23619d0d5d060f753be5aaf401_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e920202a51887b23619d0d5d060f753be5aaf401_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e920202a51887b23619d0d5d060f753be5aaf401_2_1380x754.jpeg 2x" data-dominant-color="B6BCCB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">VTK%20multi-volume%EF%BC%88experimental%EF%BC%89</span><span class="informations">1920×1050 361 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>rendering by VTK-GPU ray casting:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc09b1adbee8d72e7911cff946e420ab806eaec1.jpeg" data-download-href="/uploads/short-url/t70aKwB16GbIgR3VBQPFOfbwDhT.jpeg?dl=1" title="VTK%20GPUray%20Casting" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc09b1adbee8d72e7911cff946e420ab806eaec1_2_690x377.jpeg" alt="VTK%20GPUray%20Casting" data-base62-sha1="t70aKwB16GbIgR3VBQPFOfbwDhT" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc09b1adbee8d72e7911cff946e420ab806eaec1_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc09b1adbee8d72e7911cff946e420ab806eaec1_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc09b1adbee8d72e7911cff946e420ab806eaec1_2_1380x754.jpeg 2x" data-dominant-color="A9AEBA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">VTK%20GPUray%20Casting</span><span class="informations">1920×1050 338 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
