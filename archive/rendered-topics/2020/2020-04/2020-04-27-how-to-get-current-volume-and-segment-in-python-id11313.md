---
topic_id: 11313
title: "How To Get Current Volume And Segment In Python"
date: 2020-04-27
url: https://discourse.slicer.org/t/11313
---

# How to get current volume and segment in Python

**Topic ID**: 11313
**Date**: 2020-04-27
**URL**: https://discourse.slicer.org/t/how-to-get-current-volume-and-segment-in-python/11313

---

## Post #1 by @Shicong (2020-04-27 11:57 UTC)

<p>When going to the volumeclipmodel module, as shown in the diagram, you have to manually mouse to select the volume and segment, how to automatically get these two objects in the python code, is there a code interface? thanks!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40da7b5a9dc2ba22ebea2994250639021e19d18c.jpeg" data-download-href="/uploads/short-url/9fIEvlDZwQEuPFqkbej1X4beKMQ.jpeg?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40da7b5a9dc2ba22ebea2994250639021e19d18c_2_690x394.jpeg" alt="图片" data-base62-sha1="9fIEvlDZwQEuPFqkbej1X4beKMQ" width="690" height="394" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40da7b5a9dc2ba22ebea2994250639021e19d18c_2_690x394.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40da7b5a9dc2ba22ebea2994250639021e19d18c_2_1035x591.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40da7b5a9dc2ba22ebea2994250639021e19d18c.jpeg 2x" data-dominant-color="C6C1D4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">1298×742 227 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2020-04-27 14:29 UTC)

<p>You can get the parameter node for the VolumeClipWithModel module with this code:</p>
<pre><code class="lang-auto">volumeClipWithModelNode = slicer.mrmlScene.GetSingletonNode("VolumeClipWithModel", "vtkMRMLScriptedModuleNode")
</code></pre>
<p>And get the parameters with this code:</p>
<pre><code class="lang-auto">inputVolume = volumeClipWithModelNode.GetNodeReference("InputVolume")
clippingModel = volumeClipWithModelNode.GetNodeReference("ClippingModel")
outputVolume = volumeClipWithModelNode.GetNodeReference("OutputVolume")
</code></pre>
<p>What is your workflow?<br>
If you are doing the segmentation in the segment editor and then exporting the segment to a model to use in  volume clip with model, you can perform the masking directly within the segment editor by using the “Mask volume” effect from the “Segment Editor Extra Effects” extension.</p>

---

## Post #3 by @Shicong (2020-04-28 02:38 UTC)

<p>Thank you,I wish you a happy working life! <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=9" title=":smile:" class="emoji" alt=":smile:"></p>

---

## Post #4 by @Shicong (2020-04-28 04:17 UTC)

<p>What’s more, it’s the default not on the volumeclipwithmodel “, the display is “select a volume” and &amp; quot;select a model”, without the mouse select, I want to get the active volume object of the volumes module from the python code, and the current model object of the module. Note that I am going to get volume and model objects in the python code, can you provide the code? Thank you so much! !!!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a2fa87d951ad8d680f5ac843d580206b4c45855.png" alt="图片" data-base62-sha1="hqUmefjRtBbHhnPZuJKth63sGm9" width="640" height="341"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d46a987061d0f74dc1ad9925dd4befcc70d06c94.png" data-download-href="/uploads/short-url/uj7BpIFRTNAA4V3oM1UX2ByM3qY.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d46a987061d0f74dc1ad9925dd4befcc70d06c94_2_557x500.png" alt="图片" data-base62-sha1="uj7BpIFRTNAA4V3oM1UX2ByM3qY" width="557" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d46a987061d0f74dc1ad9925dd4befcc70d06c94_2_557x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d46a987061d0f74dc1ad9925dd4befcc70d06c94.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d46a987061d0f74dc1ad9925dd4befcc70d06c94.png 2x" data-dominant-color="F3F0EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">644×578 29.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/914416c9071e59484c7f11d88716492b12dea189.png" data-download-href="/uploads/short-url/kJ571haqciAOiV2WSG3IOTAO1C1.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/914416c9071e59484c7f11d88716492b12dea189_2_453x500.png" alt="图片" data-base62-sha1="kJ571haqciAOiV2WSG3IOTAO1C1" width="453" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/914416c9071e59484c7f11d88716492b12dea189_2_453x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/914416c9071e59484c7f11d88716492b12dea189.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/914416c9071e59484c7f11d88716492b12dea189.png 2x" data-dominant-color="F1F2F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">662×730 21.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
