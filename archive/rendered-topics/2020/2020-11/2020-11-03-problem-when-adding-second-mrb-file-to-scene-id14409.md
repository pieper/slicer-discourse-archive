# Problem when adding second mrb file to scene

**Topic ID**: 14409
**Date**: 2020-11-03
**URL**: https://discourse.slicer.org/t/problem-when-adding-second-mrb-file-to-scene/14409

---

## Post #1 by @alexjamesmajor (2020-11-03 17:43 UTC)

<p>Running on Windows 10 and a recent version of Slicer (shown in picture)</p>
<p>When I add a second .mrb file (I’m aiming to compare two different scans) with File → Add Data, the scene goes blank. This doesn’t appear to be a RAM issue.</p>
<p>Any advice would be greatly appreciated!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50f4f4a3e089eb2ed9e13b9c449a02ce497fc9f3.jpeg" data-download-href="/uploads/short-url/byb0MBfkUwX2p96qWJqMWwsP0pZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/50f4f4a3e089eb2ed9e13b9c449a02ce497fc9f3_2_690x317.jpeg" alt="image" data-base62-sha1="byb0MBfkUwX2p96qWJqMWwsP0pZ" width="690" height="317" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/50f4f4a3e089eb2ed9e13b9c449a02ce497fc9f3_2_690x317.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/50f4f4a3e089eb2ed9e13b9c449a02ce497fc9f3_2_1035x475.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/50f4f4a3e089eb2ed9e13b9c449a02ce497fc9f3_2_1380x634.jpeg 2x" data-dominant-color="BABABE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1702×784 322 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd87e20ba131bf80a2bf783251982cdf21c21566.png" data-download-href="/uploads/short-url/AaPVxbgxpOvYpWsN9YxMLNdcVH8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd87e20ba131bf80a2bf783251982cdf21c21566_2_690x316.png" alt="image" data-base62-sha1="AaPVxbgxpOvYpWsN9YxMLNdcVH8" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd87e20ba131bf80a2bf783251982cdf21c21566_2_690x316.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd87e20ba131bf80a2bf783251982cdf21c21566_2_1035x474.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd87e20ba131bf80a2bf783251982cdf21c21566_2_1380x632.png 2x" data-dominant-color="A8A7AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1695×777 91.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @alexjamesmajor (2020-11-03 17:43 UTC)

<p>First image is the first mrb file, second image is after adding the second mrb file.</p>

---

## Post #3 by @alexjamesmajor (2020-11-03 17:45 UTC)

<p>Slicer version Slicer 4.11.20200930</p>

---

## Post #4 by @pieper (2020-11-03 18:46 UTC)

<p>A .mrb file has an entire scene inside, so perhaps loading one on top of another could lead to some inconsistency.  If you save the data in non-mrb form you should be able to load both volumes into a new scene.</p>

---

## Post #5 by @lassoan (2020-11-03 20:05 UTC)

<p>Probably you need to select what you want to show in slice viewers (due to <a href="https://github.com/Slicer/Slicer/issues/4570">this</a> issue). For example, you can go to Data module and show the two volume overlaid on top of each other using the visibility column:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f43bbeb01a4a23cef2e93ecc24432ab7d94bcd1c.png" data-download-href="/uploads/short-url/yQAvluZkaukekpWyEFlpK15wZNq.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f43bbeb01a4a23cef2e93ecc24432ab7d94bcd1c_2_690x404.png" alt="image" data-base62-sha1="yQAvluZkaukekpWyEFlpK15wZNq" width="690" height="404" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f43bbeb01a4a23cef2e93ecc24432ab7d94bcd1c_2_690x404.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f43bbeb01a4a23cef2e93ecc24432ab7d94bcd1c_2_1035x606.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f43bbeb01a4a23cef2e93ecc24432ab7d94bcd1c.png 2x" data-dominant-color="B9B19A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1233×723 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @alexjamesmajor (2020-11-03 23:15 UTC)

<p>Andras, this solved my issue. Thanks again! I appreciate the help.</p>
<p>Alex</p>

---
