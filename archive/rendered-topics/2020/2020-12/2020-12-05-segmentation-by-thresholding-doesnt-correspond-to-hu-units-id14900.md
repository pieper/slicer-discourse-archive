# Segmentation by thresholding doesnt correspond to HU units

**Topic ID**: 14900
**Date**: 2020-12-05
**URL**: https://discourse.slicer.org/t/segmentation-by-thresholding-doesnt-correspond-to-hu-units/14900

---

## Post #1 by @Cesar_Puga (2020-12-05 16:00 UTC)

<p>Hello Everyone,</p>
<p>Im trying to segment the bones from a set of CT scans, actually i’ve done this actions both in Slicer and in Python, i have read the segmentation recipes for extracting skeletons but when i apply a threshold for the common bone HU (&gt;225 or &gt;300) values i seem to be extracting incomplete ribcages/bones along with extra artifacts (blood vessels, kidneys)</p>
<p>could this be an error of how the CT scan was taken, i researched and the parameters used for the HU unit calculation are the rescale Slope and rescale intercept<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d4c02b04e96a314b4a8f0ca7b89202dc5bd5ba1.jpeg" data-download-href="/uploads/short-url/djlfTZNxL4ajfMnvGChSQ9Oo7WV.jpeg?dl=1" title="segbones" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d4c02b04e96a314b4a8f0ca7b89202dc5bd5ba1_2_690x268.jpeg" alt="segbones" data-base62-sha1="djlfTZNxL4ajfMnvGChSQ9Oo7WV" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d4c02b04e96a314b4a8f0ca7b89202dc5bd5ba1_2_690x268.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d4c02b04e96a314b4a8f0ca7b89202dc5bd5ba1_2_1035x402.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d4c02b04e96a314b4a8f0ca7b89202dc5bd5ba1_2_1380x536.jpeg 2x" data-dominant-color="A7AEC3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segbones</span><span class="informations">1851×719 334 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> , my scans have all values of 1 and -1024 respectively, is there a workaround for mapping the HU units of my CT scans to properly encompass bone between a certain range and blood,</p>
<p>i attach images of the segmentation when applying a thrreshold of 225 HU</p>

---

## Post #2 by @lassoan (2020-12-05 16:14 UTC)

<p>Hounsfield Unit ranges cannot be used for accurate segmentation of different materials for many reasons - noise, partial volume effect, patient-specific bone density differences, etc.</p>
<p>Check out segmentation tutorials here to learn more about segmentation tools: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#tutorials">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#tutorials</a></p>

---
