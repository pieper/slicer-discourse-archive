---
topic_id: 26894
title: "How To Input Ijk Coordinate And Get The Value Of The Volume"
date: 2022-12-23
url: https://discourse.slicer.org/t/26894
---

# How to input IJK coordinate and get the value of the volume as txt

**Topic ID**: 26894
**Date**: 2022-12-23
**URL**: https://discourse.slicer.org/t/how-to-input-ijk-coordinate-and-get-the-value-of-the-volume-as-txt/26894

---

## Post #1 by @WilliamLambert1205 (2022-12-23 02:58 UTC)

<p>Hi all,</p>
<p>I am trying to access to what is displayed in the Data Probe Module. I need to input IJK coordinate as array and get the value of the volume, without using the mouse at all.<br>
I looked at the example<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a61a7b503ecdc2c40076813cdbcf7f2047de6c6.png" data-download-href="/uploads/short-url/m1IKQklJjO3Z41Au1eyc8NqwYT4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a61a7b503ecdc2c40076813cdbcf7f2047de6c6.png" alt="image" data-base62-sha1="m1IKQklJjO3Z41Au1eyc8NqwYT4" width="690" height="143" data-dominant-color="EFF9DE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1443×301 5.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However, it depends on the mouse location.<br>
So, where do all the data in Data Probe come from?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/2101dc3e3810db623b56ae1797a2851eadf407e7.png" alt="image" data-base62-sha1="4HZK1diBt1tKcmi9wjzZz3Ri1SL" width="466" height="109"><br>
And what function should I use to get these ‘L’, ‘F’, ‘B’ data as array?<br>
I mean, since ‘infoWidget.layerValues[layer].text’ prints the value of the volume, ‘infoWidget = slicer.modules.DataProbeInstance.infoWidget’ must get the data array from some function. How can I use it? Or is there any driect way to input IJK coordinate as array and get the value of the volume?<br>
Thank you !</p>

---

## Post #2 by @rbumm (2022-12-23 09:47 UTC)

<p>Hello,</p>
<p>Both questions are answered in the script repository, starting from <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-value-of-a-volume-at-specific-voxel-coordinates">here</a>.</p>

---
