---
topic_id: 10082
title: "Loading 3Ddose Files Dicom Image In 3D Slicer"
date: 2020-02-03
url: https://discourse.slicer.org/t/10082
---

# Loading 3ddose files & DICOM image in 3D slicer

**Topic ID**: 10082
**Date**: 2020-02-03
**URL**: https://discourse.slicer.org/t/loading-3ddose-files-dicom-image-in-3d-slicer/10082

---

## Post #1 by @elham1992 (2020-02-03 14:01 UTC)

<p>Operating system:windows 10<br>
Slicer version:4.11.0<br>
Expected behavior:<br>
Actual behavior:<br>
Hi all<br>
I have installed 3D slicer 4.11.0 &amp; its extension package  but I have many problems!<br>
The phantom image is in DICOM format  &amp; 21  3ddose files resulting dosxyznrc.<br>
Can I use 3D slicer for calculating DVH?<br>
I can load my phantom and 3ddose files by choosing item “load file”.<br>
Nevertheless, I am not sure that is correct or not?<br>
I mean ,dose not loading 3ddose files need any preprocessing in 3D silcer?<br>
In  addition , for plotting DVH I have to contour organs but I could not find contour module!!<br>
where is the contour module?</p>
<p>I hope that you can help me.<br>
Thanks in advance.</p>

---

## Post #2 by @cpinter (2020-02-04 16:07 UTC)

<p>After you install the SlicerRT extension from the Extension Manager, you can load 3ddose files using drag&amp;drop or the load file menu. Also you will find the Dose Volume Histogram module in the Radiotherapy category.</p>
<p>For more infor see doc: <a href="https://www.slicer.org/w/index.php/Documentation/Nightly/Extensions/SlicerRT">https://www.slicer.org/w/index.php/Documentation/Nightly/Extensions/SlicerRT</a></p>

---

## Post #3 by @cpinter (2020-02-04 16:10 UTC)

<aside class="quote no-group" data-username="elham1992" data-post="1" data-topic="10082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/ed8c4c/48.png" class="avatar"> elham1992:</div>
<blockquote>
<p>I could not find contour module!!</p>
</blockquote>
</aside>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation</a></p>
<p>I’d also suggest trying the search option on this forum.</p>

---
