---
topic_id: 37641
title: "Totalsegmentator Issues"
date: 2024-07-31
url: https://discourse.slicer.org/t/37641
---

# TotalSegmentator Issues

**Topic ID**: 37641
**Date**: 2024-07-31
**URL**: https://discourse.slicer.org/t/totalsegmentator-issues/37641

---

## Post #1 by @arflores (2024-07-31 17:45 UTC)

<p>Hello,</p>
<p>I am new to TotalSegmentator. I am trying to use it to autosegment vertebral bodies on CTs.</p>
<p>I am using an iMac with Radeon Pro 5500 XT 8GB GDDR6 memory (not sure if this is compatible/usable?). I am using Slicer 5.6.2 and the most recent stable TotalSegmentator (as of today). For input, I select the CT I’ve uploaded. I choose vertebra body as task. I’ve tried both “fast” and full resolution options and get the same error (below). Of note, it indicates “no GPU detected” so I think it is using CPU only. I also tried the <a href="http://totalsegmentator.com" rel="noopener nofollow ugc">totalsegmentator.com</a> and this gave Internal server error. Anyway, the error I get in Slicer:</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 3255, in tryWithErrorDisplay<br>
yield<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 298, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 971, in process<br>
self.processVolume(inputFile, inputVolume,<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 1045, in processVolume<br>
self.logProcessOutput(proc)<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 817, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/7q/zlc8w0qx549dl50655_1s_7m0000gn/T/Slicer-alexflores/__SlicerTemp__2024-07-31_09+30+29.195/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/7q/zlc8w0qx549dl50655_1s_7m0000gn/T/Slicer-alexflores/__SlicerTemp__2024-07-31_09+30+29.195/segmentation’, ‘–task’, ‘vertebrae_body’]’ returned non-zero exit status 1.</p>
<p>Any help on this?</p>
<p>Thanks<br>
Alex</p>

---

## Post #2 by @Matteboo (2024-08-01 12:24 UTC)

<p>Thank you for this very precise error report.</p>
<p>Have you tried to run total segmentator on the sample CT that are already available in slicer ?<br>
Also, how much free space do you have on your disk? Sometimes, on my computer, if<br>
i have little space left (&gt;10Go) it causes issues</p>

---

## Post #3 by @diazandr3s (2024-08-05 10:07 UTC)

<p>Hi <a class="mention" href="/u/arflores">@arflores</a>,</p>
<p>Have you considered using Auto3DSeg on Slicer?</p>
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

<p>Just downloaded the latest Slicer and then install Auto3DSeg using Extension Manager. We made several models available (full res and quick) incuding Spine segmentation.</p>
<p>Hope this helps,</p>

---
