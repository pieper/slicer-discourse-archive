---
topic_id: 25321
title: "Volume Rendering Disappears After Placing A Markups Roi"
date: 2022-09-19
url: https://discourse.slicer.org/t/25321
---

# Volume rendering disappears after placing a markups ROI

**Topic ID**: 25321
**Date**: 2022-09-19
**URL**: https://discourse.slicer.org/t/volume-rendering-disappears-after-placing-a-markups-roi/25321

---

## Post #1 by @CharlesChen (2022-09-19 02:54 UTC)

<p>Version: Slicer 5.0.3<br>
System: Ubuntu 64-bit</p>
<p>Hi there,<br>
I’m trying to <strong>create a markups ROI, place it into the 3d view and turn on the cropping</strong>.<br>
Here is the code snippet I execute in the python console:</p>
<pre><code class="lang-auto"># Get the Volume node of "MRHead".
volumeNode = slicer.util.getNode("MRHead")

# Get the display node of volume rendering.
vrLogic = slicer.modules.volumerendering.logic()
displayNode = vrLogic.GetFirstVolumeRenderingDisplayNode(volumeNode)

#Create a markups ROI node.
roiNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
roiNodeID = roiNode.GetID()
displayNode.SetAndObserveROINodeID(roiNodeID)

# Fit markups ROI to volume and enable the cropping.
vrLogic.FitROIToVolume(displayNode)
displayNode.SetCroppingEnabled(True)
</code></pre>
<p>However, as shown below, after I executed the above code, the volume rendering in the ROI box disappeared unexpectedly.<br>
To be precise, after the</p>
<blockquote>
<p>vrLogic.FitROIToVolume(displayNode)</p>
</blockquote>
<p>is executed, the volume rendering disappears.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f185c91079acb8fe5f6a62a863a4d465295ca349.png" data-download-href="/uploads/short-url/ysBHFixwVm8xJq7dJWDLYrTjO6l.png?dl=1" title="ROI 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f185c91079acb8fe5f6a62a863a4d465295ca349_2_690x342.png" alt="ROI 1" data-base62-sha1="ysBHFixwVm8xJq7dJWDLYrTjO6l" width="690" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f185c91079acb8fe5f6a62a863a4d465295ca349_2_690x342.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f185c91079acb8fe5f6a62a863a4d465295ca349_2_1035x513.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f185c91079acb8fe5f6a62a863a4d465295ca349_2_1380x684.png 2x" data-dominant-color="CCCEE5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ROI 1</span><span class="informations">1413×702 88.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, I also executed the same code snippet on Windows and Mac, the volume rendering didn’t disappear, and everything was ok.</p>
<p>Why does this happen? Is my code correct? What exactly should I do to fix/avoid this on the Ubuntu/Linux version of Slicer?</p>
<p>Any help would be appreciated!</p>

---

## Post #2 by @lassoan (2022-09-19 05:05 UTC)

<p>I cannot reproduce this on a linux computer, so most likely the problem is not due to using linux but due to some Slicer or system configuration or driver issue.</p>
<p>Can you reproduce the behavior if you use the application GUI?<br>
Does it occur with all volume rendering settings (CPU, GPU, multi-volume), depth peeling enabled/disabled (in view settings)?<br>
Does the volume rendering reappears if you rotate around the view, hide the ROI, …?<br>
Try to remove your Slicer.ini file (to reset all settings to default) and see if it makes any difference.</p>

---

## Post #3 by @CharlesChen (2022-09-19 06:45 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a><br>
Thank you so much for your reply!<br>
Just to make sure, after you executed my code on your Linux computer, the volume rendering didn’t disappear and is still there, right?  In fact, the above code was executed on my VMware ubuntu system. Could this be the reason why volume rendering disappeared?</p>
<p><strong>Note:</strong><br>
The premise of executing my code and reproducing is selecting ‘MRHead’ in the ‘Sample Data’ module and enabling volume rendering of ‘MRHead’ in the ‘volume rendering’ module.</p>
<p><strong>Here are the results of what I just tried on VMware ubuntu I’m using:</strong><br>
CPU rendering and enabled depth peeling: appears<br>
CPU rendering and disabled depth peeling: appears</p>
<p>GPU rendering and enabled depth peeling: disappears<br>
GPU rendering and disabled depth peeling: reappears</p>
<p>multi-volume rendering and enabled depth peeling: disappears<br>
multi-volume rendering and disabled depth peeling: reappears</p>
<p>Rotate around the view: volume rendering doesn’t reappear.<br>
Hide the ROI: reappear.</p>
<p>All of the above situations are also the same as when using the application GUI (Create a markups ROI in the ‘Markups’ module and drag it to the 3d view.)</p>
<p>However, on Windows or Mac computers(not VMware), volume rendering does not disappear after ROI placement, whether depth peeling is enabled or not and no matter what type of rendering is used.</p>
<p>Because my expectation/goal is to create a new markups ROI in 3d view and enable cropping with GPU volume rendering and depth peeling turned on. Therefore, can this issue be fixed in the Linux version of Slicer?</p>
<p>By the way, how can I find Slicer.ini in ubuntu? I searched for it in the file manager, but there are no results found:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89db6dc426a5f2cd8d90321387661c13b39bf15c.png" data-download-href="/uploads/short-url/jFxxjT92s7b0nViokz8ShsphhX6.png?dl=1" title="no result" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89db6dc426a5f2cd8d90321387661c13b39bf15c_2_498x375.png" alt="no result" data-base62-sha1="jFxxjT92s7b0nViokz8ShsphhX6" width="498" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89db6dc426a5f2cd8d90321387661c13b39bf15c_2_498x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89db6dc426a5f2cd8d90321387661c13b39bf15c_2_747x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89db6dc426a5f2cd8d90321387661c13b39bf15c.png 2x" data-dominant-color="DCCAD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">no result</span><span class="informations">876×658 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you very much!</p>

---

## Post #4 by @lassoan (2022-09-19 07:34 UTC)

<p>It seems to be a problem with the graphics driver (or how it is used) when initializing the Z buffer. Enabling/disabling depth peeling resets the Z buffer.</p>
<p>Does this happen with Slicer-5.0.3? As a workaround, you can disable/enable depth peeling in your script.</p>
<aside class="quote no-group" data-username="CharlesChen" data-post="3" data-topic="25321">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/charleschen/48/8444_2.png" class="avatar"> CharlesChen:</div>
<blockquote>
<p>By the way, how can I find Slicer.ini in ubuntu? I searched for it in the file manager, but there are no results found:</p>
</blockquote>
</aside>
<p>See <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location" class="inline-onebox">Application settings — 3D Slicer documentation</a></p>

---

## Post #5 by @CharlesChen (2022-09-19 18:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="25321">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does this happen with Slicer-5.0.3?</p>
</blockquote>
</aside>
<p>Yes. The same issue also happens with version 5.0.2 and version 4.11.20210226.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="25321">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It seems to be a problem with the graphics driver (or how it is used) when initializing the Z buffer.</p>
</blockquote>
</aside>
<p>Therefore, Is there any possibility to fundamentally solve this problem?</p>
<p>Thank you so much!</p>

---

## Post #6 by @lassoan (2022-09-19 19:00 UTC)

<aside class="quote no-group quote-modified" data-username="CharlesChen" data-post="5" data-topic="25321">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/charleschen/48/8444_2.png" class="avatar"> CharlesChen:</div>
<blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="25321">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It seems to be a problem with the graphics driver (or how it is used) when initializing the Z buffer.</p>
</blockquote>
</aside>
<p>Therefore, Is there any possibility to fundamentally solve this problem?</p>
</blockquote>
</aside>
<p>In general, we cannot fix problems that we cannot reproduce. An easy workaround is to enable and disable depth peeling in your script to reset the Z buffer state; or maybe use CPU volume rendering (if that is OK for your use case).</p>
<p>Most likely the issue is in VTK. However, VTK developers - similarly to us - can only work on problems that they can reproduce on their systems.</p>

---
