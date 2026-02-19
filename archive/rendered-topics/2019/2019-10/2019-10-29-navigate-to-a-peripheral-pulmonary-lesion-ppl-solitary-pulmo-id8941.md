---
topic_id: 8941
title: "Navigate To A Peripheral Pulmonary Lesion Ppl Solitary Pulmo"
date: 2019-10-29
url: https://discourse.slicer.org/t/8941
---

# Navigate to a peripheral pulmonary lesion (PPL) / Solitary Pulmonary Nodule (SPN)

**Topic ID**: 8941
**Date**: 2019-10-29
**URL**: https://discourse.slicer.org/t/navigate-to-a-peripheral-pulmonary-lesion-ppl-solitary-pulmonary-nodule-spn/8941

---

## Post #1 by @Kedar_Hibare (2019-10-29 12:14 UTC)

<p>Hi<br>
I am new to 3D Slicer and I as an interventional pulmonologist very keen to be able to map my way (navigate) to a lesion (PPL/SPN) in the lung. I have been playing around with 3D Slicer for sometime but haven’t been able to do so. Is there any way in which we can navigate to a lesion in the lung via automatically generated paths to the lesion. This is a hot topic in interventional pulmonology with the national lung cancer screening trail showing mortality benefit. Many companies have invested hugely in this area and I wonder if 3D slicer can also do the same. Any help would be appreciated<br>
Warm Regards<br>
KrH</p>

---

## Post #2 by @lassoan (2019-10-29 16:03 UTC)

<p>I’m not sure if SlicerCIP has anything for this (I let CIP experts to comment on this) but you may be able to use SlicerVMTK extension for this. You can start from an image where airways are segmented or at processed in a way so that they show up much brighter in the image than the surroundings and then use Vascular Modeling Toolkit / Level Set Segmentation module to find a path based between two points.</p>
<p>You may also define trajectory manually, using Markups module.</p>
<p>Slicer can also do real-time position tracking (and display tool position in the image, reformat the image, etc.) using electromagnetic position trackers attached to an endoscope.</p>

---

## Post #3 by @Kedar_Hibare (2019-10-30 09:10 UTC)

<p>Dear Mr Lasso,<br>
Thank you very much for the prompt reply. I have just installed the VMTK extension that you have suggested. Over the next days I shall play around with it and report if I have made any progress in navigating via an airway to a PPL/SPN which should help me in my work.</p>
<p>It is quite interesting that you have mentioned the ability of 3D Slicer to be able to integrate with EMN! I am not sure how to make it work for now. But is there any ppt / video explaining this function to be able to integrate it in daily practice during bronchoscopy? But I am glad you mentioned it!!!</p>
<p>Meanwhile I shall also wait for other CIP experts to help me get better at what I am able to do and achieve more in this area by answering my queries.</p>
<p>Thank you again for the support and help I very much appreciate it Sir</p>
<p>Warm Regards<br>
KrH</p>

---

## Post #4 by @lassoan (2019-10-30 15:31 UTC)

<aside class="quote no-group" data-username="Kedar_Hibare" data-post="3" data-topic="8941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kedar_hibare/48/4902_2.png" class="avatar"> Kedar_Hibare:</div>
<blockquote>
<p>It is quite interesting that you have mentioned the ability of 3D Slicer to be able to integrate with EMN! I am not sure how to make it work for now.</p>
</blockquote>
</aside>
<p>Slicer can connect to commercial surgical navigation systems (Medtronic StealthStation and BrainLab) to get real-time tracking information. Or, you can get an NDI Aurora tracker Ascension tracker and install sensors on your tools.</p>
<p>See more information at <a href="http://www.slicerigt.org">www.slicerigt.org</a>.</p>

---
