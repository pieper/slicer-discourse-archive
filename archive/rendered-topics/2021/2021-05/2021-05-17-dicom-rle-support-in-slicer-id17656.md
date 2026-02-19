---
topic_id: 17656
title: "Dicom Rle Support In Slicer"
date: 2021-05-17
url: https://discourse.slicer.org/t/17656
---

# DICOM RLE Support in Slicer

**Topic ID**: 17656
**Date**: 2021-05-17
**URL**: https://discourse.slicer.org/t/dicom-rle-support-in-slicer/17656

---

## Post #1 by @Federico (2021-05-17 17:23 UTC)

<p>Hi everyone,<br>
I was wondering if Slicer is able to convert the pixel data of a binary label map to <a href="http://dicom.nema.org/medical/dicom/2019a/output/chtml/part05/sect_8.2.2.html" rel="noopener nofollow ugc">DICOM Run-Length-Encoding</a> (RLE). Does anyone know if this is possible and how?</p>
<p>Thanks for your help! much appreciated!</p>

---

## Post #2 by @lassoan (2021-05-17 17:37 UTC)

<p>Yes, you can do this in Slicer. After you installed “Quantative Reporting” extension, you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database">export segmentation node to DICOM Segmentation Object</a>.</p>

---

## Post #3 by @Federico (2021-05-17 17:48 UTC)

<p>Thanks for the answer!</p>
<p>I had looked into that module but I couldn’t find any trace of RLE. I will have a closer look but is there perhaps an example of c++/python code that I could look at?</p>

---

## Post #4 by @lassoan (2021-05-17 17:52 UTC)

<aside class="quote no-group" data-username="Federico" data-post="3" data-topic="17656">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/federico/48/10963_2.png" class="avatar"> Federico:</div>
<blockquote>
<p>I had looked into that module but I couldn’t find any trace of RLE.</p>
</blockquote>
</aside>
<p>It is implemented at one level lower, in DCMTK.</p>
<p>It seems that the default segmentation encoding is bit packing and not RLE (see <a href="https://github.com/QIICR/dcmqi/blob/ac7d0fea3a4458a2e14bae0bac886813051b6ad4/apps/seg/itkimage2segimage.cxx#L121">here</a>). <a class="mention" href="/u/fedorov">@fedorov</a>, do you remember why you did not end up exposing the RLE option on the itkimage2segimage interface?</p>
<p>Bit packing allows random access to any part of the segmentation without decompressing the entire volume and for very complex segmentations its compression ratio may be similar or better than RLE. Why would you prefer using RLE over bit packing?</p>

---

## Post #5 by @fedorov (2021-05-17 18:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="17656">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>do you remember why you did not end up exposing the RLE option on the itkimage2segimage interface?</p>
</blockquote>
</aside>
<p>We added and tested reading of RLE-compressed segmentations, and did some experiments with writing, but I don’t recall if the result was documented. I think the main concern is that introducing compression will further complicate interoperability. Note that RLE would be applied <strong>after</strong> bit packing (for binary segmentations). Bit packing alone can be challenging for interoperability, and I am not convinced we should make it even more challenging.</p>
<p>No one asked about this before - it could be added as an option, but I would want to know how bit packing + RLE is supported in the existing tools before adding it.</p>

---

## Post #6 by @twloehfelm (2021-05-17 23:25 UTC)

<p>I have to convert bitmasks to RLE for a particular framework (detectron2) that uses on COCO data format. I use a python library called pycocotools to convert bitmask =&gt; RLE like so:</p>
<pre><code class="lang-auto">from pycocotools import mask
import numpy as np

# Example bitmask array. Replace with your actual bitmask.
bitmask = np.array([
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
])

rle_mask = mask.encode(np.asarray(bitmask, order="F", dtype=np.uint8))
</code></pre>
<p>For more context <a href="https://colab.research.google.com/github/twloehfelm/SAR2020/blob/master/04%20-%20Segmentation.ipynb" rel="noopener nofollow ugc">this colab notebook</a> shows how it is used in the training of a liver segmentation algorithm.</p>

---

## Post #7 by @lassoan (2021-05-18 01:42 UTC)

<p>I don’t think that COCO’s RLE compression is related to DICOM. There are many RLE implementations and RLE codecs specified in the DICOM standard are completely different from what COCO uses.</p>
<p>A possible data flow would be:</p>
<ul>
<li>Load each image from DICOM into 3D Slicer, segment it, and save both the image and segmentation in NRRD file format. In addition to this, you may also export the segmentations in DICOM segmentation objects for archival (DICOM segmentation object is more future-proof, because it stores referenced object UIDs, standard terminologies, etc. in standard fields).</li>
<li>To generate training data, you would convert the NRRD files to COCO json files with a small Python script.</li>
</ul>

---

## Post #8 by @Federico (2021-05-18 07:33 UTC)

<p>I guess pydicom would be able to do the RLE too, right?</p>

---

## Post #9 by @lassoan (2021-05-18 19:29 UTC)

<p>pydicom would do the same kind of RLE as DCMTK. I would not recommend to use RLE compression in your DICOM segmentation objects because it would lead to incompatibility with many software packages and would not help in any way with getting segmentations to COCO format (you would need to decompress the DICOM RLE, unpack the bits, and use COCO’s trivial RLE encoding).</p>

---
