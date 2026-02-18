# Liver tumor segmentation from ultrasound 3D (GE Voluson machine)

**Topic ID**: 11272
**Date**: 2020-04-23
**URL**: https://discourse.slicer.org/t/liver-tumor-segmentation-from-ultrasound-3d-ge-voluson-machine/11272

---

## Post #1 by @emipaw (2020-04-23 18:43 UTC)

<p>Hi,</p>
<p>I am new in Slicer 3D. I want to segment a liver tumor from ultrasound 3D examine in .vol format. I tried to do it using Volume Rendering but  the 3D model doesn’tt look good. I tried to choose every preset and there was no difference. Do you have any idea what settings I should change/use to make tumor visible?</p>

---

## Post #2 by @lassoan (2020-04-23 18:55 UTC)

<p>Due to high noise and low contrast, you can rarely use volume rendering (raycasting) for visualizing ultrasound volumes. Volume rendering works well for visualizing fluid-fill cavities and vessels (this is used extensively for cardiac ultrasound) but for most everything else you need to process or segment the volume to show it in 3D.</p>
<p>For liver ablation/resection guidance using ultrasound, you can segment the liver using one of the rapid segmentation tools in Segment Editor module. I would recommend, Surface cut effect (provided by SegmentEditorExtraEffects extension).</p>
<p>Surface cut is what we use for intra-operative breast tumor segmentation on tracked ultrasound images. The advantage is that you can segment very quickly and you don’t need to use mouse&amp;keyboard but a touchscreen is enough (we just had to develop a custom module that shows just the necessary buttons and make them big so that they can be clicked easily on a tablet):</p>
<div class="lazyYT" data-youtube-id="90l0T1ADe_Y" data-youtube-title="Navigated breast conserving surgery" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque&amp;start=55"></div>

---
