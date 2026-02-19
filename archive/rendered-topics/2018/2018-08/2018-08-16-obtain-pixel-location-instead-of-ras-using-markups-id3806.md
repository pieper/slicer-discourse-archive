---
topic_id: 3806
title: "Obtain Pixel Location Instead Of Ras Using Markups"
date: 2018-08-16
url: https://discourse.slicer.org/t/3806
---

# Obtain pixel location instead of RAS using Markups

**Topic ID**: 3806
**Date**: 2018-08-16
**URL**: https://discourse.slicer.org/t/obtain-pixel-location-instead-of-ras-using-markups/3806

---

## Post #1 by @lgroves (2018-08-16 20:47 UTC)

<p>I would like to be able to use the Markups module to obtain a 2D pixel location, instead of the RAS coordinates on a transformed image.<br>
For example I would like to obtain the coordinates of Image_Probe not RAS in the following image:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fbdc7fb9ddd48aff106cfba1eb2cba7d2d0cbbd.png" data-download-href="/uploads/short-url/bnqk7huwJ2nFlvWVIgNeAK2epTn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fbdc7fb9ddd48aff106cfba1eb2cba7d2d0cbbd.png" alt="image" data-base62-sha1="bnqk7huwJ2nFlvWVIgNeAK2epTn" width="690" height="135" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">854×168 3.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>.</p>
<p>Any help is appreciated. Thanks.</p>

---

## Post #2 by @Andinet_Enquobahrie (2018-08-16 23:39 UTC)

<p>As shown in</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_DataProbe_text" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_DataProbe_text</a></p>
<p>you can do something like</p>
<pre><code class="lang-python">infoWidget = slicer.modules.DataProbeInstance.infoWidget
infoWidget.layerIJKs['B'].text
</code></pre>

---

## Post #3 by @lassoan (2018-08-17 06:47 UTC)

<p>I’ve added an example to the script repository that shows how to get voxel coordinate from RAS coordinate of a markup fiducial point: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates</a></p>

---
