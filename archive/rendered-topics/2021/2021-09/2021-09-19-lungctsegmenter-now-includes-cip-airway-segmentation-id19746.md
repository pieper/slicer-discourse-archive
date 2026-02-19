---
topic_id: 19746
title: "Lungctsegmenter Now Includes Cip Airway Segmentation"
date: 2021-09-19
url: https://discourse.slicer.org/t/19746
---

# LungCTSegmenter now includes CIP airway segmentation

**Topic ID**: 19746
**Date**: 2021-09-19
**URL**: https://discourse.slicer.org/t/lungctsegmenter-now-includes-cip-airway-segmentation/19746

---

## Post #1 by @rbumm (2021-09-19 14:31 UTC)

<p>There is a new option to perform an automatic airway segmentation along with the generation of lung masks from a lung CT. The LungCTSegmenter, part of LungCTAnalyzer V 2.45, implements a CLI call to the “Segment Lung Airways” module of the Chest Imaging Platform.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c7c80af66f23715adec053e4856c383a76b3678.png" alt="image" data-base62-sha1="8D5oqsH62eEHFa9R4qlbA1fUY88" width="596" height="452"></p>
<p>Check “Airway Segmentation (CIP)” in the segmenter and select an appropriate kernel mode.</p>
<p>The complete and simple workflow is described in this <a href="https://youtu.be/r_GnJgtudWs" rel="noopener nofollow ugc">Youtube Video</a>. This works in 3D Slicer 4.11 and 4.13.</p>

---

## Post #2 by @sandigeeup (2022-01-05 16:37 UTC)

<p>Hi there, I messaged you yesterday on youtube, regards your tutorial: <a href="https://youtu.be/9iiOBmaP8bA" class="inline-onebox" rel="noopener nofollow ugc">Airway segmentation in 3D Slicer with "Grow from Seeds" - YouTube</a>. I have tried this several times and can’t get the right result. I am a MSc med viz student and have to submit 4 assignments for Monday, but having real trouble getting this right. I wonder if you could help me. Please see my uploads Thanks in advance. Sandie C<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69beec801bbae1067b4e8446e4cbf38f0d405a4f.jpeg" alt="Anterior View" data-base62-sha1="f5tbA7sNTZZ2dvOIBZANQKj5Wrl" width="602" height="359"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e876ffb5b94245c6a10e1e0b47221aa36628bd48.jpeg" alt="Inferior view" data-base62-sha1="xatJ4K0U9U0xT0Es4YRvBusRCzu" width="602" height="359"></p>

---

## Post #3 by @rbumm (2022-01-05 19:26 UTC)

<p>Hi Sandie,</p>
<p>This looks not bad for the start. The lung masks are ok, but the airway segmentation is probably not detailed enough for surgical planning.</p>
<p>Could you provide some more information:</p>
<ul>
<li>
<p>Which Slicer version do you use (can not read exactly on the screenshot: 4.10.2?)</p>
</li>
<li>
<p>What is the main goal of your segmentation and what are you not satisfied with?</p>
</li>
<li>
<p>Did you segment the airways with the LungCTSegmenter extension or did you use the grow from seeds technique that was described in the <a href="https://youtu.be/9iiOBmaP8bA" rel="noopener nofollow ugc">other video</a>?</p>
</li>
<li>
<p>Is this dataset from a public source, safe to show on this forum and/or available for download ?</p>
</li>
</ul>

---

## Post #4 by @sandigeeup (2022-01-05 22:39 UTC)

<p>Hey, thank you for your swift response. I tried to use the grow from seeds option and followed your video. I just think I am adding too much of the paintbrush, also as you say the airway segmentation was poor. I use 4.10.2. However, since I message here I have simply used the editor segmentation tool see image attached and this has worked well, it did take me 4 goes through. I now have a few more projects to fulfil on slicer may I still ask for your advice. Warm wishes and thank you!!, Sandie<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f30645de3f98c250f5b0b6a423f76590d69f3983.jpeg" alt="Exercise 4 Lung tumour" data-base62-sha1="yFTsPqZjalbw1LkLpda9CMIGHCP" width="278" height="288"></p>

---
