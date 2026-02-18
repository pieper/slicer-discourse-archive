# Isodose module not showing colorwash

**Topic ID**: 23756
**Date**: 2022-06-07
**URL**: https://discourse.slicer.org/t/isodose-module-not-showing-colorwash/23756

---

## Post #1 by @TomNB (2022-06-07 19:55 UTC)

<p>The dose is calculated using the orthovoltage engine, fig 1. I wonder if it is not compatible with isodose module because when I switch to Isodose module the colorwash disappears, fig 2. However when I calculate the isodose, I get the lines fig 3. I would like to have the colorwash and the lines.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b1b2a80494dfa8a8814e7e70e6ec4ed961b6687.jpeg" data-download-href="/uploads/short-url/3RN5RLlktYxpM8oF8pSUMofvBRB.jpeg?dl=1" title="fig 1.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b1b2a80494dfa8a8814e7e70e6ec4ed961b6687_2_690x399.jpeg" alt="fig 1.PNG" data-base62-sha1="3RN5RLlktYxpM8oF8pSUMofvBRB" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b1b2a80494dfa8a8814e7e70e6ec4ed961b6687_2_690x399.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b1b2a80494dfa8a8814e7e70e6ec4ed961b6687_2_1035x598.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b1b2a80494dfa8a8814e7e70e6ec4ed961b6687_2_1380x798.jpeg 2x" data-dominant-color="909395"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fig 1.PNG</span><span class="informations">1916×1109 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06439ae2c7089e6825e635efadb64904f833543a.jpeg" data-download-href="/uploads/short-url/TpHTeeKE2mRxF8nFleUH5HBbia.jpeg?dl=1" title="fig 2.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06439ae2c7089e6825e635efadb64904f833543a_2_690x398.jpeg" alt="fig 2.PNG" data-base62-sha1="TpHTeeKE2mRxF8nFleUH5HBbia" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06439ae2c7089e6825e635efadb64904f833543a_2_690x398.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06439ae2c7089e6825e635efadb64904f833543a_2_1035x597.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06439ae2c7089e6825e635efadb64904f833543a_2_1380x796.jpeg 2x" data-dominant-color="848383"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fig 2.PNG</span><span class="informations">1918×1108 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad8e8768dc5c3df7bd9ed699c903f43fd491228d.jpeg" data-download-href="/uploads/short-url/oLlY5Ln9fLZ3fO2KTvKKKC7ttQV.jpeg?dl=1" title="fig 3.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad8e8768dc5c3df7bd9ed699c903f43fd491228d_2_690x402.jpeg" alt="fig 3.PNG" data-base62-sha1="oLlY5Ln9fLZ3fO2KTvKKKC7ttQV" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad8e8768dc5c3df7bd9ed699c903f43fd491228d_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad8e8768dc5c3df7bd9ed699c903f43fd491228d_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad8e8768dc5c3df7bd9ed699c903f43fd491228d_2_1380x804.jpeg 2x" data-dominant-color="9E9DA5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fig 3.PNG</span><span class="informations">1898×1108 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2022-06-07 20:58 UTC)

<p>When the isodose module is opened, it adjusts the colors of the dose volume to match the isodose levels. Probably this is causing your volume to be invisible. It should adjust the colors again when you click “Generate isodose”, but that doesn’t seem to be the case.</p>
<p>Could you email me your scene so I can take a look at it?</p>
<p>You should be able to change the window/level back to normal in the Volumes module, or by clicking on this button and dragging in one of the 2D views:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/546fcfe7e24fd214ce26afbc681a9be1be7537a6.png" alt="image" data-base62-sha1="c2XFa3kqXklCRyNsCgcrnplUZsW" width="53" height="42"></p>

---

## Post #3 by @TomNB (2022-06-08 23:21 UTC)

<p>I tried adjusting the window/level but still that did not solve the problem. See my email with scene attached</p>

---

## Post #4 by @Sunderlandkyl (2022-06-09 19:20 UTC)

<p>It looks like the image threshold is being modified.</p>
<p>You can change it back in the Volumes module by changing threshold from “Manual” to “Off”, or by lowering the minimum threshold.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2aab062230021c639200e49ac1ad06fe01807c43.png" alt="image" data-base62-sha1="65stc90fneNq7aJK61zbYrsEvtx" width="491" height="87"></p>

---

## Post #5 by @TomNB (2022-06-10 22:31 UTC)

<p>Thank you Kyle, changing threshold from ‘Manual’ to ‘Off’ solved the problem. For some reason whenever you go to Isodose even when the set up was ‘Off’ it changes to ‘Manual’.</p>

---
