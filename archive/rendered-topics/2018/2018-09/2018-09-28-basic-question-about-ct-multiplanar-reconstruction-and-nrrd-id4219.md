---
topic_id: 4219
title: "Basic Question About Ct Multiplanar Reconstruction And Nrrd"
date: 2018-09-28
url: https://discourse.slicer.org/t/4219
---

# Basic question about CT MultiPlanar Reconstruction and NRRD files

**Topic ID**: 4219
**Date**: 2018-09-28
**URL**: https://discourse.slicer.org/t/basic-question-about-ct-multiplanar-reconstruction-and-nrrd-files/4219

---

## Post #1 by @jdx-john (2018-09-28 13:40 UTC)

<p>When Slicer imports a raw CT DICOM dataset, my recollection is this is a set of 2D image ‘stacks’ taken on 3 orthogonal axes - correct? And Slicer uses MPR to convert this into a volumetric dataset so you can slice it any way and do volume rendering.</p>
<p>Is this volumetric data literally just a 3D array of voxel data, and is that what is saved in NRRD or are the original slices retained?</p>
<p>In the consumer GPU world, 3D textures are widely supported now for polygon rendering so I’m wondering how trivial it would be to export/convert a CT scan into such a format that could be applied in regular OpenGL or DirectX? Like if I wanted to employ a brain scan in a video game, etc</p>

---

## Post #2 by @lassoan (2018-09-28 14:12 UTC)

<aside class="quote no-group" data-username="jdx-john" data-post="1" data-topic="4219">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a6a055/48.png" class="avatar"> jdx-john:</div>
<blockquote>
<p>Is this volumetric data literally just a 3D array of voxel data, and is that what is saved in NRRD or are the original slices retained?</p>
</blockquote>
</aside>
<p>Original slices are not retained, it is just a 3D array.</p>
<p>This 3D array is downloaded into the GPU as a texture and used for volume rendering.</p>
<p>For slice views, reslicing is done on the CPU because there are several and sharing of textures between renderers was not implemented in VTK (maybe it is now) and we would need to implement slice viewer layer compositing in GPU (fading between foreground, background, label volume). These are all doable, it just has not been the highest priority.</p>

---

## Post #3 by @jdx-john (2018-09-28 14:24 UTC)

<p>Thanks Andras <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
