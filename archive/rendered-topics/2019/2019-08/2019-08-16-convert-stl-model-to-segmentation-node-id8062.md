# Convert STL model to segmentation node

**Topic ID**: 8062
**Date**: 2019-08-16
**URL**: https://discourse.slicer.org/t/convert-stl-model-to-segmentation-node/8062

---

## Post #1 by @Andrew_Kanawati (2019-08-16 16:10 UTC)

<p>I am having trouble creating a segmentation node from an STL of a 3d scan. The imported transform looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bed4a8ac13ee850a879e75c1d171942d17f6070.jpeg" data-download-href="/uploads/short-url/foLtXYRW6vqJCH7O5ArsTSLoH2o.jpeg?dl=1" title="04%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bed4a8ac13ee850a879e75c1d171942d17f6070_2_690x396.jpeg" alt="04%20PM" data-base62-sha1="foLtXYRW6vqJCH7O5ArsTSLoH2o" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bed4a8ac13ee850a879e75c1d171942d17f6070_2_690x396.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bed4a8ac13ee850a879e75c1d171942d17f6070_2_1035x594.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bed4a8ac13ee850a879e75c1d171942d17f6070_2_1380x792.jpeg 2x" data-dominant-color="6F6E82"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">04%20PM</span><span class="informations">1641×944 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The segmentation has characteristics that are not present on the STL:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf25a42c883d23ac8828a7e0db2cbda788b259ca.jpeg" data-download-href="/uploads/short-url/rgXQgpr6dIN25X10FKREqj6iQVY.jpeg?dl=1" title="08%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf25a42c883d23ac8828a7e0db2cbda788b259ca_2_690x388.jpeg" alt="08%20PM" data-base62-sha1="rgXQgpr6dIN25X10FKREqj6iQVY" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf25a42c883d23ac8828a7e0db2cbda788b259ca_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf25a42c883d23ac8828a7e0db2cbda788b259ca_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf25a42c883d23ac8828a7e0db2cbda788b259ca_2_1380x776.jpeg 2x" data-dominant-color="737183"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">08%20PM</span><span class="informations">1656×933 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Help would be much appreciated.</p>

---

## Post #2 by @cpinter (2019-08-16 16:28 UTC)

<p>It seems that the master representation when you choose the ‘Convert model to segmentation node’ stays binary labelmap, and the artifacts are probably the result of these two conversions (from stl to labelmap and then back to surface for 3D visualization).</p>
<p>I should probably fix this. <a class="mention" href="/u/lassoan">@lassoan</a> this seems a trivial issue, not sure if there was a decision to keep it labelmap.</p>
<p>In the meantime you can</p>
<ul>
<li>Go to Segmentations module</li>
<li>Create new segmentation node</li>
<li>Change master to Closed surface</li>
<li>In Import/Export section import the model node to the segmentation node</li>
</ul>

---

## Post #3 by @Andrew_Kanawati (2019-08-16 16:35 UTC)

<p>This has worked! thank you</p>

---
