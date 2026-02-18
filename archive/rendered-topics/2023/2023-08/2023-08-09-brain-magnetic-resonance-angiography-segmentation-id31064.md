# Brain magnetic resonance angiography segmentation

**Topic ID**: 31064
**Date**: 2023-08-09
**URL**: https://discourse.slicer.org/t/brain-magnetic-resonance-angiography-segmentation/31064

---

## Post #1 by @Gonzalo_Rojas_Costa (2023-08-09 13:35 UTC)

<p>Any slicer extension to segment arteries from a brain magnetic resonance angiography image?</p>
<p>Gonzalo Rojas Costa</p>

---

## Post #2 by @pieper (2023-08-10 14:28 UTC)

<p>Typically MRA scans highlight the vessels enough that thresholding works well.  Of course they can be very noisy so people tend to use MIP or other volume rendering.</p>
<p>Depending on your use case this module could be helpful:</p>
<aside class="quote quote-modified" data-post="1" data-topic="31002">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/rfc-is-there-interest-in-this-custom-module-guided-vein-segmentation/31002">RFC : is there interest in this custom module - Guided vein segmentation</a> <a class="badge-category__wrapper " href="/c/community/vmtk/28"><span data-category-id="28" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent" title="This is the new home of the VMTK community (moved from VMTK Google Groups)"><span class="badge-category__name">VMTK</span></span></a>
  </div>
  <blockquote>
    Hi all, 
I am contemplating merging this module, <a href="https://github.com/chir-set/Tools7/tree/master/GuidedVeinSegmentation" rel="noopener nofollow ugc">Guided vein segmentation</a>, in SlicerVMTK, so that it become easily available. 
Beforehand, I wish to know if other users find it worthwhile as an addition to SlicerVMTK. 
Its purpose is to segment major veins from CT angioscans, considering that the veins are not contrast enhanced. I find it quite efficient and useful for surgical planning in some complex aortic cases namely. Please read the notes on its homepage. 
It does not use the VMTK librarie…
  </blockquote>
</aside>


---
