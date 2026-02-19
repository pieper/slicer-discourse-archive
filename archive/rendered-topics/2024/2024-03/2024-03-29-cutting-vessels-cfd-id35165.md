---
topic_id: 35165
title: "Cutting Vessels Cfd"
date: 2024-03-29
url: https://discourse.slicer.org/t/35165
---

# Cutting vessels - CFD

**Topic ID**: 35165
**Date**: 2024-03-29
**URL**: https://discourse.slicer.org/t/cutting-vessels-cfd/35165

---

## Post #1 by @Killmaro (2024-03-29 14:01 UTC)

<p>Hi</p>
<p>I’m working on pulmonary vessels CFD. After extracting the centerlines of my vascular tree, I’m aiming to automatically trim vessel ends below a certain caliber, perpendicular to the centerlines. I attempted to use the “vesselness filtering” tool in the VMTK module, but it doesn’t recognize the volume of my tree (STL file directly imported into Slicer). Is there a way to achieve this ?</p>
<p>Thank you in advance for your help</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4f3ad8c9a99e4c6786bafb31912d88cb22ee44d.jpeg" data-download-href="/uploads/short-url/pOM1nsgpoUkhL7rlKONGWmMnRmt.jpeg?dl=1" title="Capture d’écran 2024-03-29 à 14.40.19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4f3ad8c9a99e4c6786bafb31912d88cb22ee44d_2_690x443.jpeg" alt="Capture d’écran 2024-03-29 à 14.40.19" data-base62-sha1="pOM1nsgpoUkhL7rlKONGWmMnRmt" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4f3ad8c9a99e4c6786bafb31912d88cb22ee44d_2_690x443.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4f3ad8c9a99e4c6786bafb31912d88cb22ee44d_2_1035x664.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4f3ad8c9a99e4c6786bafb31912d88cb22ee44d_2_1380x886.jpeg 2x" data-dominant-color="9C9CBF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-03-29 à 14.40.19</span><span class="informations">1920×1234 75.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2024-03-30 09:54 UTC)

<p>This <a href="https://github.com/dmolony3/ClipVessel" rel="noopener nofollow ugc">module</a> does just what you want.</p>
<p>The author has <a href="https://discourse.slicer.org/t/vmtk-surface-clipping-contribution/30456/14">proposed</a> to add it to SlicerVMTK extension, it’s still pending though.</p>

---

## Post #3 by @lassoan (2024-03-30 21:14 UTC)

<p>Is the ClipVessel module’s author waiting for us to do something?</p>

---

## Post #4 by @Killmaro (2024-04-21 16:38 UTC)

<p>Thanks for your answer</p>
<p>I ve tried to set it with extension wizard but when I select extension folder “clipvessel” I get the following error :</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/bin/…/lib/Slicer-5.6/qt-scripted-modules/ExtensionWizard.py”, line 284, in selectExtension<br>
xd = SlicerWizard.ExtensionDescription(sourcedir=path)<br>
File “/Applications/Slicer.app/Contents/bin/Python/SlicerWizard/ExtensionDescription.py”, line 142, in <strong>init</strong><br>
self._setProjectAttribute(“homepage”, p, required=True)<br>
File “/Applications/Slicer.app/Contents/bin/Python/SlicerWizard/ExtensionDescription.py”, line 189, in <em>setProjectAttribute<br>
v = project.getValue("EXTENSION</em>" + name.upper(), default, substitute)<br>
File “/Applications/Slicer.app/Contents/bin/Python/SlicerWizard/ExtensionProject.py”, line 282, in getValue<br>
raise KeyError(“script does not set %r” % name)<br>
KeyError: “script does not set ‘EXTENSION_HOMEPAGE’”</p>
<p>Is there anything to modify in general Slicer settings ?<br>
And in this case which path should I provide for this  EXTENSION_HOMEPAGE ?</p>
<p>Thanks again for your help</p>

---

## Post #5 by @chir.set (2024-04-21 19:49 UTC)

<aside class="quote no-group" data-username="Killmaro" data-post="4" data-topic="35165">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/killmaro/48/77864_2.png" class="avatar"> Killmaro:</div>
<blockquote>
<p>set it with extension wizard</p>
</blockquote>
</aside>
<p>The ‘Extension wizard’ is meant for creating extensions and modules based on templates.</p>
<p>You want to use the ClipVessel module. Clone it from the remote repository and drag ClipVessel.py onto Slicer. It will install it very nicely.</p>

---

## Post #6 by @Killmaro (2024-04-21 22:13 UTC)

<p>Thanks it works, I can run the module and set my cutting points.</p>
<p>However, I have 2 remaining issues:</p>
<ul>
<li>After extracting centerlines, my input 3D model disappears. How can I maintain a visual on my 3D input model to position the cutting points in the right places?</li>
<li>Similarly, after creating my centerlines cut tree, how can I obtain the corresponding output surface?</li>
</ul>
<p>Thank you in advance for the help</p>

---

## Post #7 by @DavidM (2024-04-23 15:11 UTC)

<p>I’m not sure if I fully understand the problem. Visibility of any data type in 3D Slicer can be controlled from the data module. You can turn on and off your 3D model here and similarly you can turn on/off the output surface visibility after creating your centerlines cut tree.</p>

---

## Post #8 by @Killmaro (2024-04-23 15:35 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4bad383b14587dc71b5d5f6f6432ddba3ec8a6f.jpeg" data-download-href="/uploads/short-url/pMOdw6lZr6OPtY9Hf60xQd09xCv.jpeg?dl=1" title="Capture d’écran 2024-04-23 à 17.26.05" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4bad383b14587dc71b5d5f6f6432ddba3ec8a6f_2_690x385.jpeg" alt="Capture d’écran 2024-04-23 à 17.26.05" data-base62-sha1="pMOdw6lZr6OPtY9Hf60xQd09xCv" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4bad383b14587dc71b5d5f6f6432ddba3ec8a6f_2_690x385.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4bad383b14587dc71b5d5f6f6432ddba3ec8a6f_2_1035x577.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4bad383b14587dc71b5d5f6f6432ddba3ec8a6f_2_1380x770.jpeg 2x" data-dominant-color="7A7CA8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-04-23 à 17.26.05</span><span class="informations">1920×1073 65.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Yes, I tried to display the 3D model by clicking on the small eye in the ‘data’ module interface, but only the centerlines appear.<br>
I am using pre-segmented 3D models in .STL format that are imported into slicer maybe that’s why it’s not working…</p>

---

## Post #9 by @DavidM (2024-04-23 18:53 UTC)

<p>There does not appear to be any other model loaded in your scene in the shared screenshot. Just “test” which appears to be the centerlines and the centerline endpoints.</p>

---

## Post #10 by @Killmaro (2024-04-25 10:40 UTC)

<p>Indeed, I was overwriting the input STL file during the extraction of the centerlines. I’ve corrected that, and it’s working now. The result looks good.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a6e08edf07752933a51346c587dfeae2fb8ad76.jpeg" data-download-href="/uploads/short-url/1ugwrKJuVTLyfiHurfXZgTR0Fsq.jpeg?dl=1" title="Capture d’écran 2024-04-25 à 12.36.20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a6e08edf07752933a51346c587dfeae2fb8ad76_2_580x500.jpeg" alt="Capture d’écran 2024-04-25 à 12.36.20" data-base62-sha1="1ugwrKJuVTLyfiHurfXZgTR0Fsq" width="580" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a6e08edf07752933a51346c587dfeae2fb8ad76_2_580x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a6e08edf07752933a51346c587dfeae2fb8ad76_2_870x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a6e08edf07752933a51346c587dfeae2fb8ad76_2_1160x1000.jpeg 2x" data-dominant-color="989AB7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-04-25 à 12.36.20</span><span class="informations">1920×1654 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da5cf1045872a82797f2d208032beaba5938e2d4.jpeg" data-download-href="/uploads/short-url/v9JdjtCGWN9No4s8qMcYxXAwXAg.jpeg?dl=1" title="Capture d’écran 2024-04-25 à 12.36.50" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da5cf1045872a82797f2d208032beaba5938e2d4_2_580x500.jpeg" alt="Capture d’écran 2024-04-25 à 12.36.50" data-base62-sha1="v9JdjtCGWN9No4s8qMcYxXAwXAg" width="580" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da5cf1045872a82797f2d208032beaba5938e2d4_2_580x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da5cf1045872a82797f2d208032beaba5938e2d4_2_870x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da5cf1045872a82797f2d208032beaba5938e2d4_2_1160x1000.jpeg 2x" data-dominant-color="7D72AD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-04-25 à 12.36.50</span><span class="informations">1920×1654 79.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @Killmaro (2024-04-25 10:43 UTC)

<p>However, the clip points are not behaving like beads along the centerlines; they are positioning themselves outside of the surface. Is this normal ?</p>

---

## Post #12 by @DavidM (2024-04-25 13:37 UTC)

<p>I’m glad to see it worked. Yes, the clip points do not move along the centerline. When you place them I believe 3D Slicer projects them onto the nearest visible surface. It should not matter if I remember correctly as the clip points are used to find the nearest point on the centerline. You can always hide the surface and place them on the centerline if you are having issues when they are on/outside the surface.</p>

---

## Post #13 by @Killmaro (2024-04-27 18:59 UTC)

<p>I was able to input the trimmed and extended model into my CFD software and it worked correctly. Thank you again for your help</p>

---

## Post #14 by @chir.set (2024-06-25 21:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="35165" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is the ClipVessel module’s author waiting for us to do something?</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> ,</p>
<p>I hereby draw your attention that <a class="mention" href="/u/davidm">@DavidM</a> has submitted a <a href="https://github.com/vmtk/SlicerExtension-VMTK/pulls" rel="noopener nofollow ugc">PR</a> to integrate Clip Vessel in SlicerVMTK. May be you could consider when you have some time.</p>
<p>Ragards.</p>

---

## Post #15 by @Killmaro (2024-07-23 17:36 UTC)

<p>This module needs a list of clip points as input. It’s quite simple with a limited number of vessels; however, it’s harder when there are many. Is there an easy way to create this list by auto-detection (like in the “extract centerline” module), for example, by placing one clip point 5mm above each centerline endpoint? Thank you for your help.</p>

---
