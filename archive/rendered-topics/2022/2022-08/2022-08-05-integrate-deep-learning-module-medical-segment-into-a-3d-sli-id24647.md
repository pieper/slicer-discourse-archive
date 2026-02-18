# Integrate deep learning module medical segment into a 3D slicer

**Topic ID**: 24647
**Date**: 2022-08-05
**URL**: https://discourse.slicer.org/t/integrate-deep-learning-module-medical-segment-into-a-3d-slicer/24647

---

## Post #1 by @Thu_n_Chu_th (2022-08-05 03:44 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I’m looking to integrate deep learning deep learning into a 3D slicer.<br>
I found a similar post about brain segmentation (<a href="https://github.com/fepegar/SlicerParcellation#readme" class="inline-onebox" rel="noopener nofollow ugc">GitHub - fepegar/SlicerParcellation: 3D Slicer modules for brain segmentation using deep learning.</a>). but t install according to the instructions, the 3D slicer gives an error.<br>
Hope everybody help please.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3db813efc667b4e5876c2330a2791f416744da59.png" alt="image" data-base62-sha1="8NZvFftirk31txCHBLmLVvdcjUJ" width="669" height="448"></p>

---

## Post #2 by @pieper (2022-08-05 14:09 UTC)

<p>There should be messages in the python console telling why it didn’t load.  It would be great if you could debug the module and contribute fixes.  <a class="mention" href="/u/fernando">@Fernando</a> may have additional suggestions.</p>

---

## Post #3 by @Thu_n_Chu_th (2022-08-05 15:25 UTC)

<p>I look forward to everyone’s help to solve this problem.<br>
I followed the instructions on the github code link. But I don’t know if I’ve done enough.</p>
<ul>
<li>I have downloaded torchIO and pytorch on 3D slicer extension.</li>
<li>I have downloaded and unzipped the github code.<br>
I then linked the code to the 3D slicer via Edit/application setting/modules/ Additional modules path. and I passed the entire link code in there.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a49e9b4b035a612876d555007eb96bf8814d6757.png" data-download-href="/uploads/short-url/nui7kzBXQmU5wK7BxzzdtGGPHJZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a49e9b4b035a612876d555007eb96bf8814d6757.png" alt="image" data-base62-sha1="nui7kzBXQmU5wK7BxzzdtGGPHJZ" width="690" height="324" data-dominant-color="F5F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1097×516 28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a49e9b4b035a612876d555007eb96bf8814d6757.png" data-download-href="/uploads/short-url/nui7kzBXQmU5wK7BxzzdtGGPHJZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a49e9b4b035a612876d555007eb96bf8814d6757.png" alt="image" data-base62-sha1="nui7kzBXQmU5wK7BxzzdtGGPHJZ" width="690" height="324" data-dominant-color="F5F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1097×516 28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
<p>When I click on BrainParcellation, there is no message and nothing happens.</p>

---

## Post #4 by @Thu_n_Chu_th (2022-08-05 15:28 UTC)

<p>when I read the author’s code I see that the UNet network downloads are all open source and library. So I don’t know if doing it on my computer will need to fix or change this code.<br>
Thank you.</p>

---

## Post #5 by @Fernando (2022-09-19 20:27 UTC)

<p>Thanks for the ping, Steve.</p>
<p>Hi, <a class="mention" href="/u/thu_n_chu_th">@Thu_n_Chu_th</a>. Could you please share which version of Slicer you’re using and whether you see any messages in the Python console, as <a class="mention" href="/u/pieper">@pieper</a> suggested?</p>

---
