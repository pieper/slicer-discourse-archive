---
topic_id: 27525
title: "Matlabbridge Empty Volume By Default Instead Of No Volume"
date: 2023-01-29
url: https://discourse.slicer.org/t/27525
---

# MatlabBridge - empty volume by default instead of no volume

**Topic ID**: 27525
**Date**: 2023-01-29
**URL**: https://discourse.slicer.org/t/matlabbridge-empty-volume-by-default-instead-of-no-volume/27525

---

## Post #1 by @georg (2023-01-29 09:04 UTC)

<p>Dear 3D-Slicer community,</p>
<p>I am developing an extension using MatlabBridge which involves loading 3D and 4D images into 3D-Slicer. I adapted the automatically generated Matlab function to do so, but unfortunately it <strong>only</strong> works when I select “Create new volume” in the dropdown IO &gt; “Create new volume” (see Figure 2). I have multiple volumes that need to be displayed by 3D-Slicer and I don’t want the user to click through each volume and select “Create new volume”. When I leave the setting at “None” (default, see Figure 1), the code returns the following error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a1e193b8c5284bf48dd2a96204f811c1a797af6.png" data-download-href="/uploads/short-url/jHQnmpWO2rLFWcKm2Gd3LCK4wSy.png?dl=1" title="Bildschirmfoto vom 2023-01-28 23-28-42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a1e193b8c5284bf48dd2a96204f811c1a797af6_2_690x100.png" alt="Bildschirmfoto vom 2023-01-28 23-28-42" data-base62-sha1="jHQnmpWO2rLFWcKm2Gd3LCK4wSy" width="690" height="100" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a1e193b8c5284bf48dd2a96204f811c1a797af6_2_690x100.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a1e193b8c5284bf48dd2a96204f811c1a797af6_2_1035x150.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a1e193b8c5284bf48dd2a96204f811c1a797af6.png 2x" data-dominant-color="FEF9F9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto vom 2023-01-28 23-28-42</span><span class="informations">1320×192 33.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there a way to create an empty volume by default? Maybe by modifying the xml-file or the Matlab function? When using “Create new volume”, the struct “inputParams.outputvolume” contains a path to a nrrd-file and a params-file which are afterwards created by the function “cli_imagewrite”. I tried to set similar paths (before calling “cli_imagewrite”) when using the setting “None” for “Output volume”. But this does not work either.</p>
<p>Many thanks in advance for your help.</p>
<p>Figure 1 - not working setting:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8911c30506d0bb52166e6729fd4b58311277ae53.png" data-download-href="/uploads/short-url/jyzt0H61AVH74WrPq813AGP35g7.png?dl=1" title="Bildschirmfoto vom 2023-01-28 23-01-08" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8911c30506d0bb52166e6729fd4b58311277ae53_2_357x500.png" alt="Bildschirmfoto vom 2023-01-28 23-01-08" data-base62-sha1="jyzt0H61AVH74WrPq813AGP35g7" width="357" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8911c30506d0bb52166e6729fd4b58311277ae53_2_357x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8911c30506d0bb52166e6729fd4b58311277ae53.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8911c30506d0bb52166e6729fd4b58311277ae53.png 2x" data-dominant-color="EDEDED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto vom 2023-01-28 23-01-08</span><span class="informations">508×711 30.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Figure 2 - working setting:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c90bdcd27e137605169c8d827c3e9cf6035c9883.png" data-download-href="/uploads/short-url/sGxnZLn0OQxgJiF6GtZuuq7gmVJ.png?dl=1" title="Bildschirmfoto vom 2023-01-28 23-01-01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c90bdcd27e137605169c8d827c3e9cf6035c9883_2_357x500.png" alt="Bildschirmfoto vom 2023-01-28 23-01-01" data-base62-sha1="sGxnZLn0OQxgJiF6GtZuuq7gmVJ" width="357" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c90bdcd27e137605169c8d827c3e9cf6035c9883_2_357x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c90bdcd27e137605169c8d827c3e9cf6035c9883.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c90bdcd27e137605169c8d827c3e9cf6035c9883.png 2x" data-dominant-color="ECEDED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto vom 2023-01-28 23-01-01</span><span class="informations">508×711 31.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Code:</p>
<pre><code class="lang-auto">function outputParams=test2(inputParams)
outputParams.min=0; % just to prevent no outputParams given error
outputParams.max=0;

load("/home/user/my_mask.mat") % loads the matrix "mask"
img.pixelData=int8(mask);

inputParams.outputvolume.
cli_imagewrite(inputParams.outputvolume, img);
</code></pre>

---

## Post #2 by @lassoan (2023-01-29 09:10 UTC)

<p>By selecting a volume, the user indicates that he is interested in computing that output. Currently, we don’t have an option to automatically create a required output node if the user has not created one. Would you mind creating a feature request in the <a href="https://issues.slicer.org">Slicer issue tracker</a> to keep track of the ideaI?</p>

---

## Post #3 by @georg (2023-01-29 16:37 UTC)

<p>Done: <a href="https://github.com/Slicer/Slicer/issues/6804" class="inline-onebox" rel="noopener nofollow ugc">MatlabBridge - option to set output node as default instead of "None" · Issue #6804 · Slicer/Slicer · GitHub</a></p>

---
