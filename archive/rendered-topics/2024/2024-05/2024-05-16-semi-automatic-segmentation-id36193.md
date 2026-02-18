# Semi Automatic Segmentation 

**Topic ID**: 36193
**Date**: 2024-05-16
**URL**: https://discourse.slicer.org/t/semi-automatic-segmentation/36193

---

## Post #1 by @slicer1biology (2024-05-16 05:25 UTC)

<p>Hello,<br>
I am very new on 3D Slicer but before strating everything I had a little question.<br>
Does 3D Slicer allow (semi) automatic segmentation on MRI ?<br>
If yes, do you have pdf or videos that could help me with that ?</p>
<p>Thnak you very much!!</p>

---

## Post #2 by @LeidyMoraV (2024-05-16 14:22 UTC)

<p>I think it’s possible, you should check out this <a href="https://discourse.slicer.org/t/ai-assisted-segmentation-extension/9536/63">AI-assisted segmentation extension - Announcements - 3D Slicer Community</a></p>

---

## Post #3 by @lassoan (2024-05-16 14:28 UTC)

<p>NVIDIA AIAA was one of the first AI segmentation tools in Slicer. The field is evolving extremely quickly and so there are now better fully automatic MRI segmentation tools in Slicer. See for example this:</p>
<aside class="quote quote-modified" data-post="1" data-topic="35680">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/new-extension-monai-auto3dseg-raise-the-bar-in-ai-medical-image-segmentation/35680">New extension: MONAI Auto3DSeg - raise the bar in AI medical image segmentation</a> <a class="badge-category__wrapper " href="/c/announcements/7"><span data-category-id="7" style="--category-badge-color: #ED207B; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="Low-traffic category for 3D Slicer, extension, and community news and announcements."><span class="badge-category__name">Announcements</span></span></a>
    </div>
  </div>
  <blockquote>
    <a name="new-extension-monai-auto3dseg-raise-the-bar-in-ai-medical-image-segmentation-1" class="anchor" href="#new-extension-monai-auto3dseg-raise-the-bar-in-ai-medical-image-segmentation-1"></a>New extension: MONAI Auto3DSeg - raise the bar in AI medical image segmentation
MONAI Auto3DSeg extension is a collaboration between MONAI and 3D Slicer developer teams (led by Andres Diaz Pinto - NVIDIA and Andras Lasso - PerkLab) to improve on the state-of-the-art in fully automatic 3D medical image segmentation and make the results widely accessible. 
The extension comes with dozens of pre-trained segmentation models for specific clinical use cases, which are designed to be fast and run anywh…
  </blockquote>
</aside>

<p>But there are several others and more are coming in the next few weeks.</p>
<p>What structures you want to segment?</p>

---
