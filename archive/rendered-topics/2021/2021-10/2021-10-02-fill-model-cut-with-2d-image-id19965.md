# Fill model cut with 2D image

**Topic ID**: 19965
**Date**: 2021-10-02
**URL**: https://discourse.slicer.org/t/fill-model-cut-with-2d-image/19965

---

## Post #1 by @slicer365 (2021-10-02 07:51 UTC)

<p>Dear experts</p>
<p>Just like the first picture, how to achieve this effect in slicer,</p>
<p>the cross-section of the model is displayed as a 2D image，not the pitcture 2</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/759a03c079db90978adf70f8809657030cc7e2b7.jpeg" alt="image" data-base62-sha1="gMlQ0OfVzJw5JN2FUH8SyIANFm7" width="333" height="244"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba43f7eec494286f1d208f8039793292670da498.png" alt="image" data-base62-sha1="qzMqJYxXHb8ACSx4nNm50GW3zGo" width="304" height="274"></p>

---

## Post #2 by @lassoan (2021-10-02 14:42 UTC)

<p>You can achieve this by:</p>
<ul>
<li>in Segment Editor, create a bone segment, use it to mask the volume, and also export it to a model</li>
<li>show the masked volume with enabling thresholding in Volumes module</li>
<li>optional: use Surface toolbox Decimate tool with 0.95 reduction (or 0.90 for higher quality) to make reslicing of the model faster</li>
<li>hide the segmentation, show the decimated model, enable red slice clipping in Models module</li>
</ul>
<p>Threshold:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/174c7c5d004ec7643f26ee9dafd36b894f0cef78.jpeg" data-download-href="/uploads/short-url/3k6QOCtpHRVBDbV6ygZzBRgEZDO.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/174c7c5d004ec7643f26ee9dafd36b894f0cef78_2_690x419.jpeg" alt="image" data-base62-sha1="3k6QOCtpHRVBDbV6ygZzBRgEZDO" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/174c7c5d004ec7643f26ee9dafd36b894f0cef78_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/174c7c5d004ec7643f26ee9dafd36b894f0cef78_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/174c7c5d004ec7643f26ee9dafd36b894f0cef78_2_1380x838.jpeg 2x" data-dominant-color="3C3C41"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1166 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Clipping:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1eb312870ee60b211a35fe3459c142f347dcee0.jpeg" data-download-href="/uploads/short-url/rFu2ZYXczNY80iWU2fWtQd9WkAU.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1eb312870ee60b211a35fe3459c142f347dcee0_2_690x418.jpeg" alt="image" data-base62-sha1="rFu2ZYXczNY80iWU2fWtQd9WkAU" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1eb312870ee60b211a35fe3459c142f347dcee0_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1eb312870ee60b211a35fe3459c142f347dcee0_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1eb312870ee60b211a35fe3459c142f347dcee0_2_1380x836.jpeg 2x" data-dominant-color="393937"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1164 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Result:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a31686b31b55b70c91d7bc5de772a27d5e1342a9.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a31686b31b55b70c91d7bc5de772a27d5e1342a9.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a31686b31b55b70c91d7bc5de772a27d5e1342a9.mp4</a>
    </source></video>
  </div><p></p>

---
