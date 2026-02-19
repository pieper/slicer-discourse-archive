---
topic_id: 31002
title: "Rfc Is There Interest In This Custom Module Guided Vein Segm"
date: 2023-08-05
url: https://discourse.slicer.org/t/31002
---

# RFC : is there interest in this custom module - Guided vein segmentation

**Topic ID**: 31002
**Date**: 2023-08-05
**URL**: https://discourse.slicer.org/t/rfc-is-there-interest-in-this-custom-module-guided-vein-segmentation/31002

---

## Post #1 by @chir.set (2023-08-05 18:59 UTC)

<p>Hi all,</p>
<p>I am contemplating merging this module, <a href="https://github.com/chir-set/Tools7/tree/master/GuidedVeinSegmentation" rel="noopener nofollow ugc">Guided vein segmentation</a>, in SlicerVMTK, so that it become easily available.</p>
<p>Beforehand, I wish to know if other users find it worthwhile as an addition to SlicerVMTK.</p>
<p>Its purpose is to segment <em>major</em> veins from CT angioscans, considering that the veins are not contrast enhanced. I find it quite efficient and useful for surgical planning in some complex aortic cases namely. Please read the notes on its homepage.</p>
<p>It does not use the VMTK libraries themselves, rather the Segment Editor effects only.</p>
<p>It’s now in my repository, moving it to SlicerVMTK is easy. I’ll do so if some users find interest in it, unless Slicer devs or VMTK devs object this proposal.</p>
<p>Thank you for any input.</p>

---

## Post #2 by @pieper (2023-08-05 19:08 UTC)

<p>That sounds useful to me.  SlicerVMTK started as a way to expose VMTK code in Slicer, but I think it’s much better to have a comprehensive set of vessel-related tools in a single extension, like SlicerRT is for RT.</p>

---

## Post #3 by @chir.set (2023-08-06 15:27 UTC)

<p>With one supportive view from a Slicer developer, I’ll proceed with the integration of this module in SlicerVMTK ASAP.</p>
<p>Thank you <a class="mention" href="/u/pieper">@pieper</a>.</p>

---

## Post #4 by @chir.set (2023-08-07 13:52 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> ,</p>
<p>Just a quick follow-up, it’s merged in <a href="https://github.com/vmtk/SlicerExtension-VMTK/pull/89" rel="noopener nofollow ugc">#89</a>.</p>
<p>Regards.</p>

---
