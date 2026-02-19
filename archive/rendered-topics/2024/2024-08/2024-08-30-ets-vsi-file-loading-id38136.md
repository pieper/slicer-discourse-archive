---
topic_id: 38136
title: "Ets Vsi File Loading"
date: 2024-08-30
url: https://discourse.slicer.org/t/38136
---

# .ets .vsi File loading

**Topic ID**: 38136
**Date**: 2024-08-30
**URL**: https://discourse.slicer.org/t/ets-vsi-file-loading/38136

---

## Post #1 by @fbordignon (2024-08-30 20:12 UTC)

<p>We’ve recently came across the proprietary olympus .vsi/.ets file types used primarily at the bioinformatics field. It stores a sequence of images, much like a sequence node, but with with a pyramidal scheme, which lower resolution versions of the image are stored to facilitate the navigation. So as the user loads the file, the lowest resolution is loaded and the whole image is shown. As the user zooms in, the part been shown is updated with part of the higher resolution image.<br>
The sequence aspect is due to the format having CZT dimensions, where C is the number of channels, typically 3 (RGB), Z is the depth, representing a version of the image varying some adjustment such as the microscope focus, and T is time. Various pyramid resolutions are stored for each Z level and T.</p>
<p>For example, I have one image of CZT 3x15x1 with 64,000x40,000 pixels. Each of the 15 images are close to 7.5GiB and the whole file is 112.5GiB. Sometimes the files go up to 1TB.</p>
<p>Have anyone bumped into similar dynamic loading type of image before?<br>
Has anything similar to this been done inside 3D Slicer?<br>
Any clue on how to tackle loading and displaying this in 3D Slicer?</p>
<p><a href="https://qupath.github.io/" rel="noopener nofollow ugc">QuPath</a> implements this using the <a href="https://github.com/ome/bioformats" rel="noopener nofollow ugc">bioformats</a> library. It has the partial loading/zooming scheme described above. But it is in java and bioformats is GPLed</p>

---

## Post #2 by @pieper (2024-08-30 20:29 UTC)

<p>You might be able to adapt the <a href="https://github.com/gaoyi/SlicerBigImage">SlicerBigImage</a> extension to work with that format.  It uses OpenSlide (C / LGPL, so more Slicer friendly).</p>
<p>The older <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/IASEM">IA-SEM Module</a> also had some very nice features along the lines you describe.</p>

---
