# How to limit "Grow from seeds" to a particular region?

**Topic ID**: 22516
**Date**: 2022-03-15
**URL**: https://discourse.slicer.org/t/how-to-limit-grow-from-seeds-to-a-particular-region/22516

---

## Post #1 by @mdear (2022-03-15 13:26 UTC)

<p>Hello,</p>
<p>I’m having a lot of trouble with my trachea / tracheostomy tube stoma segmentation.  I want to segment the air inside the tube/stoma but the grow from seeds is spilling out into all the air outside the body and creating havoc.</p>
<p>How can I limit the grow from seeds to a particular region ?</p>
<p>Thanks, experts.  I’m learning more about slicer and getting better every day.  With my current knowledge I’ve been able to segment my medically fragile son’s complex airway and produce a way to custom shape a tracheostomy tube.  <a href="https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/62747652541663514507087434811839774222596193624949302758567741995891971588097/" rel="noopener nofollow ugc">https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/62747652541663514507087434811839774222596193624949302758567741995891971588097/</a></p>

---

## Post #2 by @mikebind (2022-03-15 17:54 UTC)

<p>There are a few possible approaches.  One is to place seeds for an “externalAir” segment in the air just outside the interface you want and seeds for your “internalAir” segment (or whatever you want to call the segment you want) just inside the interface you want.  Since the air voxels are pretty uniform, the interface between these two segments will basically just be defined by proximity to seeds, so if you place the seeds symmetrically across the boundary you want, it will probably work pretty well.</p>
<p>Another approach would be to create a segment containing the body and internal air, perhaps through thresholding followed by closing holes.  Then, you can limit Grow from seeds using “Masking” settings to limit the “Editable area” to “Inside bodyPlusAir”.</p>

---

## Post #3 by @lassoan (2022-03-16 21:59 UTC)

<p>Both are excellent suggestions.</p>
<p>“Grow from seeds” travels in homogeneous regions, such as air very quickly, which can make it difficult to stop its propagation with just placing seeds. That’s why the <code>Seed locality</code> parameter was added, which makes it preferable to grow regions near seeds. Even by slightly increasing the value of this parameter from the default 0 to a small value like 1 or a larger value like 5 should make it easier to limit leaks by placing a seed in the outside air.</p>
<p>For the second idea, you can get a solid “inside body” segment using <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify#surface-wrap-solidify">Wrap Solidify effect</a> (provided by SurfaceWrapSolidify extension).</p>

---
