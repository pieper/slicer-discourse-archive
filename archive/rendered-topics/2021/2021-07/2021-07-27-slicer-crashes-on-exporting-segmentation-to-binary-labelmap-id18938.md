---
topic_id: 18938
title: "Slicer Crashes On Exporting Segmentation To Binary Labelmap"
date: 2021-07-27
url: https://discourse.slicer.org/t/18938
---

# Slicer crashes on exporting segmentation to binary labelmap volume

**Topic ID**: 18938
**Date**: 2021-07-27
**URL**: https://discourse.slicer.org/t/slicer-crashes-on-exporting-segmentation-to-binary-labelmap-volume/18938

---

## Post #1 by @Panda (2021-07-27 06:13 UTC)

<p>Hello, attached is a screenshot of the report- I have tried countless things - however not sure why 3d slicer is crashing when I try to export a segmentation to a label map volume.</p>
<p>I was closely following this example by <a class="mention" href="/u/lassoan">@lassoan</a> - <a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37" rel="noopener nofollow ugc">https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37</a></p>
<p>This is the function I am using - <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#:~:text=static%20bool%20ExportVisibleSegmentsToLabelmapNode,extentComputationMode%20%3D%20vtkSegmentation%3A%3AEXTENT_UNION_OF_EFFECTIVE_SEGMENTS" rel="noopener nofollow ugc">ExportVisibleSegmentstoLabelMapNode(…)</a></p>
<p>If any other info or detail is needed, could do that gladly. Any insight please would be super nice, Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/586fb2c25922a765e1cc1581de52aadbb6053faa.png" data-download-href="/uploads/short-url/cClkrY24GZSvNgPlNdv4Ztw6Xua.png?dl=1" title="Screenshot 2021-07-27 at 8.04.11 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/586fb2c25922a765e1cc1581de52aadbb6053faa_2_690x453.png" alt="Screenshot 2021-07-27 at 8.04.11 AM" data-base62-sha1="cClkrY24GZSvNgPlNdv4Ztw6Xua" width="690" height="453" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/586fb2c25922a765e1cc1581de52aadbb6053faa_2_690x453.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/586fb2c25922a765e1cc1581de52aadbb6053faa_2_1035x679.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/586fb2c25922a765e1cc1581de52aadbb6053faa_2_1380x906.png 2x" data-dominant-color="2C2C2B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-07-27 at 8.04.11 AM</span><span class="informations">1940×1276 358 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-07-27 17:10 UTC)

<p>ExportVisibleSegmentsToLabelmapNode tries to retrieve the list of visible segments from the display node of your segmentation node, but your segmentation does not have a display node. You can create one by calling <code>segmentationNode.CreateDefaultDisplayNodes()</code> or export all segments by using <code>ExportAllSegmentsToLabelmapNode</code> method. I’ll update the code to display a helpful error message instead of crashing.</p>

---

## Post #3 by @Panda (2021-07-28 08:15 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thank you very very much for pointing this out!!! I got it to work after incorporating your feedback. Had spent tons of time trying to fix it, just glad it worked out with this update, otherwise would have done it manually which would have been quite a pain for a lot of CT scans.</p>
<p>I had no idea about this, displayNode function - I believe based on your explanation as to what this function does - fetching the display nodes etc - I now also understand the error that was popping up in the crash report, in the meantime, I was going through this, trying to investigate what could have caused it <img src="https://emoji.discourse-cdn.com/twitter/stuck_out_tongue.png?v=10" title=":stuck_out_tongue:" class="emoji" alt=":stuck_out_tongue:"></p>
<p><a href="https://developer.apple.com/documentation/xcode/investigating-memory-access-crashes" rel="noopener nofollow ugc">memory_crash_mac</a></p>
<p>Once I am done, I will share the whole python 3d slicer code with the hope that it could help someone in the future.</p>
<p>Appreciate the help! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"> <img src="https://emoji.discourse-cdn.com/twitter/grinning_face_with_smiling_eyes.png?v=10" title=":grinning_face_with_smiling_eyes:" class="emoji" alt=":grinning_face_with_smiling_eyes:"></p>

---
