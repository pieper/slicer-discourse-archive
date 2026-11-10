---
topic_id: 48810
title: "Transform applied to multiple volumes misbehaves when edited"
date: 2026-11-09
url: https://discourse.slicer.org/t/48810
last_bumped: 2026-11-10T04:17:14.744Z
---

# Transform applied to multiple volumes misbehaves when edited

**Topic ID**: 48810
**Date**: 2026-11-09
**URL**: https://discourse.slicer.org/t/transform-applied-to-multiple-volumes-misbehaves-when-edited/48810

---

## Post #1 by @shai-ikko (2026-11-09 15:38 UTC)

<p>When a transform is applied to more than one volume, and you then go to the Transforms module and edit it, weird things happen. When switching the presentation between the views, the transform (as applied to the volumes) changes (without changing in the module).</p>
<p>I did the following actions:</p>
<ul>
<li>
<p>Open Slicer 5.12.4</p>
</li>
<li>
<p>Open the “Sample Data” module</p>
</li>
<li>
<p>Click “MRHead” and “MRBrainTumor1”. MRBrainTumor1 is presented in the slices.</p>
</li>
<li>
<p>Go To “Data” module</p>
</li>
<li>
<p>Right click on the right side of MRHead (the transform context menu), and pick “create new transform”</p>
</li>
<li>
<p>Move to the “Transform Hierarchy” tab, and drag MRBrainTumor1 under the transform</p>
</li>
<li>
<p>Go to the “Transforms” module. Using the “Rotation” scrollbar “IS”, rotate by 45°. The MRBrainTumor1 volume is rotated as expected.</p>
</li>
<li>
<p>Go back to the “Data” module. Click the MRHead eye to make it visible. Result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69fa1975d8d34eea51b3e7bb5f335bcf99a75618.jpeg" data-download-href="/uploads/short-url/f7vY8HQlgGCMJ9FyjnOzXTorJXi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69fa1975d8d34eea51b3e7bb5f335bcf99a75618_2_690x339.jpeg" alt="image" data-base62-sha1="f7vY8HQlgGCMJ9FyjnOzXTorJXi" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69fa1975d8d34eea51b3e7bb5f335bcf99a75618_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69fa1975d8d34eea51b3e7bb5f335bcf99a75618_2_1035x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69fa1975d8d34eea51b3e7bb5f335bcf99a75618_2_1380x678.jpeg 2x" data-dominant-color="9FA0AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1545×761 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Going back to the Transforms module, it still shows the 45°:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eee8a8a58f770cc2ac76e7e291b7eefc3039a5b6.jpeg" data-download-href="/uploads/short-url/y5u6DFZDqceuzAV1Khl84tIp6WW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eee8a8a58f770cc2ac76e7e291b7eefc3039a5b6_2_690x339.jpeg" alt="image" data-base62-sha1="y5u6DFZDqceuzAV1Khl84tIp6WW" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eee8a8a58f770cc2ac76e7e291b7eefc3039a5b6_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eee8a8a58f770cc2ac76e7e291b7eefc3039a5b6_2_1035x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eee8a8a58f770cc2ac76e7e291b7eefc3039a5b6_2_1380x678.jpeg 2x" data-dominant-color="A2A3B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1545×761 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Now, clicking “Identity” to reset the transform:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d3ddd6d7fdee80bb1d9689f7c6f1ca33f25ac48.jpeg" data-download-href="/uploads/short-url/8JLFAlxg1EMvyY1JEM63xrZCkoE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d3ddd6d7fdee80bb1d9689f7c6f1ca33f25ac48_2_690x339.jpeg" alt="image" data-base62-sha1="8JLFAlxg1EMvyY1JEM63xrZCkoE" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d3ddd6d7fdee80bb1d9689f7c6f1ca33f25ac48_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d3ddd6d7fdee80bb1d9689f7c6f1ca33f25ac48_2_1035x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d3ddd6d7fdee80bb1d9689f7c6f1ca33f25ac48_2_1380x678.jpeg 2x" data-dominant-color="A2A3B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1545×761 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>And finally, “compare volumes”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff789e88a96bbd82ea72b79658b89545256606d9.jpeg" data-download-href="/uploads/short-url/As0bc5Bx6POfZBKomko2is2zr5L.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff789e88a96bbd82ea72b79658b89545256606d9_2_690x339.jpeg" alt="image" data-base62-sha1="As0bc5Bx6POfZBKomko2is2zr5L" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff789e88a96bbd82ea72b79658b89545256606d9_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff789e88a96bbd82ea72b79658b89545256606d9_2_1035x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff789e88a96bbd82ea72b79658b89545256606d9_2_1380x678.jpeg 2x" data-dominant-color="878887"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1545×761 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ul>
<p>If you now return to the “conventional” view, you get the head in 45° again.</p>
<p>This last move seems to imply that the problem is mostly in the slice views, but that does not make it “just presentation” or “cosmetic”, because the transform is edited based on this presentation – leading to wrong transformation matrices being selected.</p>

---

## Post #2 by @mikebind (2026-11-10 04:17 UTC)

<p>Thanks for the clear steps to try, that’s very helpful for troubleshooting. I tried to reproduce the issue following your steps exactly and did not see any problems in Slicer 5.10 (I haven’t upgraded yet to 5.12.4).  In your first and second screenshots, it appears that the heads are rotated 90 degrees rather than 45 degrees. Is it possible you had generated two 45 degree transforms and only reset one of them to identity? That doesn’t explain your final screenshot, but the images also don’t seem to match your description of the incorrect behavior.</p>

---
