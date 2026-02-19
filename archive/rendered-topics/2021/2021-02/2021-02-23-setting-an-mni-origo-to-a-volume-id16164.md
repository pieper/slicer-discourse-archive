---
topic_id: 16164
title: "Setting An Mni Origo To A Volume"
date: 2021-02-23
url: https://discourse.slicer.org/t/16164
---

# Setting an MNI origo to a volume

**Topic ID**: 16164
**Date**: 2021-02-23
**URL**: https://discourse.slicer.org/t/setting-an-mni-origo-to-a-volume/16164

---

## Post #1 by @Kalman (2021-02-23 17:43 UTC)

<p>I would like to ask whether there is a possibility to set and/or visualize of the MNI-origo of a volume.<br>
A bit more detail about the question:</p>
<ul>
<li>
<p>I’m working with MRI images of different (mostly dog) brains. Looking at them in the MATLAB, MRIcron, or MRIcroGL shows the origo of the MNI coordinate system in a given (defined) point. You can see this on the below volume, where I set the origo to the anterior commissure:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dbf167de583a7a0a5a12841d10df7afcfd8804c.jpeg" data-download-href="/uploads/short-url/kdWJ5hQvGmptMgdWmU9k2hcXkIc.jpeg?dl=1" title="mricron" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8dbf167de583a7a0a5a12841d10df7afcfd8804c_2_418x500.jpeg" alt="mricron" data-base62-sha1="kdWJ5hQvGmptMgdWmU9k2hcXkIc" width="418" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8dbf167de583a7a0a5a12841d10df7afcfd8804c_2_418x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dbf167de583a7a0a5a12841d10df7afcfd8804c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dbf167de583a7a0a5a12841d10df7afcfd8804c.jpeg 2x" data-dominant-color="5D5D61"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mricron</span><span class="informations">454×543 42.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>When I open the same nifti file with Slicer, I can only see the image origin (according to its physical space) and its slice number (showing also in the Data Probe window), but not this specific starting point:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/491f99d3445d6489be44ab09b4bbdc79adf4511b.jpeg" data-download-href="/uploads/short-url/aqSyIjBGCH4kEyoayQqgkRbd6dR.jpeg?dl=1" title="slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/491f99d3445d6489be44ab09b4bbdc79adf4511b_2_516x371.jpeg" alt="slicer" data-base62-sha1="aqSyIjBGCH4kEyoayQqgkRbd6dR" width="516" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/491f99d3445d6489be44ab09b4bbdc79adf4511b_2_516x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/491f99d3445d6489be44ab09b4bbdc79adf4511b_2_774x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/491f99d3445d6489be44ab09b4bbdc79adf4511b_2_1032x742.jpeg 2x" data-dominant-color="323231"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer</span><span class="informations">1292×928 98 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
</ul>
<p>What is your opinion, is there a way to show that pre-defined origo in Slicer?</p>
<ul>
<li>if there is, then my next related question is whether one can be able to manually re-set this origo with the program? (like in the MATLAB’s SPM module with the ‘Reorient image(s)/Set origin to Xhairs…’ option.</li>
</ul>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2021-02-23 19:42 UTC)

<p>Would a keyboard shortcut to jump to the (0,0,0) position in all slice views would fulfill your needs?</p>

---

## Post #3 by @Kalman (2021-02-24 11:58 UTC)

<p>Dear Andras,</p>
<p>It would be a good thing to have in the first place!<br>
Besides, I’m also interested in:<br>
~ whether the MNI coordinate of a given point can be shown (e.g. in the Data Probe, or in another window)? /As sometimes we need to refer to these coordinates in the publications./<br>
~ is there an option to re-set this MNI origo if I would like to change that to another point (to correct its placement)?</p>
<p>As I work work brain normalization for dog studies, the co-registration is the major part (which can be done well with the Transforms modul), but to visualize and analyze them in this common reference space (e.g., in MATLAB) we need to set manually an MNI-origo to a volume. Currently I’m only able to do that with the SPM, but it would be nice if I could handle the entire workflow with the Slicer.</p>
<p>Thanks for your advice!<br>
Best regards, Kalman</p>

---

## Post #4 by @lassoan (2021-02-25 13:46 UTC)

<aside class="quote no-group" data-username="Kalman" data-post="3" data-topic="16164">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/59ef9b/48.png" class="avatar"> Kalman:</div>
<blockquote>
<p>It would be a good thing to have in the first place!</p>
</blockquote>
</aside>
<p>You can copy-paste this into the Python console to jump slice views to (0,0,0) position on <kbd>Ctrl</kbd>+<kbd>e</kbd>:</p>
<pre data-code-wrap="python"><code class="lang-python">shortcut = qt.QShortcut(qt.QKeySequence('Ctrl+e'), slicer.util.mainWindow())
shortcut.connect('activated()',
  lambda: slicer.modules.markups.logic().JumpSlicesToLocation(0,0,0, True))
</code></pre>
<p>If you want to make this keyboard shortcut permanent then copy-paste the code into your startup script<br>
(you can find its location in menu: Edit / Application settings / General / Application startup script).</p>
<aside class="quote no-group" data-username="Kalman" data-post="3" data-topic="16164">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/59ef9b/48.png" class="avatar"> Kalman:</div>
<blockquote>
<p>whether the MNI coordinate of a given point can be shown (e.g. in the Data Probe, or in another window)?</p>
</blockquote>
</aside>
<p>The Data probe only shows coordinate values in the world coordinate system. You can make the world coordinate system mean anything you want (e.g., MNI) by applying a transform to the volume that transforms it into that space.</p>
<p>You only need a small custom script (or if you want to be fancy then a custom module) to display coordinate values in multiple coordinate systems at the same time. For example, if you have a transform that moves your image to MNI space then you can use this code snippet to display world and MNI coordinates in the status bar as you move across the viewers:</p>
<pre data-code-wrap="python"><code class="lang-python">def onMouseMoved(observer,eventid):
  mniToWorldTransformNode = getNode('LinearTransform_3')  # replace this by the name of your actual transform
  worldToMniTransform = vtk.vtkGeneralTransform()
  mniToWorldTransformNode.GetTransformToWorld(worldToMniTransform)
  ras=[0,0,0]
  mni=[0,0,0]
  crosshairNode.GetCursorPositionRAS(ras)
  worldToMniTransform.TransformPoint(ras, mni)
  slicer.util.showStatusMessage(f"RAS={.3:ras}   MNI={mni}")

crosshairNode=slicer.util.getNode('Crosshair') 
observationId = crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, onMouseMoved)

# Run this to stop displaying values:
# crosshairNode.RemoveObserver(observationId)
</code></pre>
<aside class="quote no-group" data-username="Kalman" data-post="3" data-topic="16164">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/59ef9b/48.png" class="avatar"> Kalman:</div>
<blockquote>
<p>is there an option to re-set this MNI origo if I would like to change that to another point (to correct its placement)?</p>
</blockquote>
</aside>
<p>Yes, by applying a transform. You can create a transform in Transforms module and set the coordinates in Translation section, click “Invert”, and then apply this transform to the volume.</p>
<p>I’m not sure if it is relevant for you, but you can compute ACPC transform using ACPC transform module.</p>

---

## Post #5 by @Kalman (2021-02-26 15:45 UTC)

<p>Dear Andras,</p>
<p>Thank you very much for your help and the detailed answer, it’s the function I needed!</p>
<p>Still I found some interesting issues regarding which I would like to ask your opinion.<br>
When I first used the shortcut-code, the position of the cursor was out of the volume:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d9b3b4d7537d9deff211c2e0b97eb32eeb35725.jpeg" data-download-href="/uploads/short-url/6vs4f73bkjySRxZRvXZ3Rt6VlJP.jpeg?dl=1" title="volume_out" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2d9b3b4d7537d9deff211c2e0b97eb32eeb35725_2_690x485.jpeg" alt="volume_out" data-base62-sha1="6vs4f73bkjySRxZRvXZ3Rt6VlJP" width="690" height="485" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2d9b3b4d7537d9deff211c2e0b97eb32eeb35725_2_690x485.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2d9b3b4d7537d9deff211c2e0b97eb32eeb35725_2_1035x727.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d9b3b4d7537d9deff211c2e0b97eb32eeb35725.jpeg 2x" data-dominant-color="1E1E1D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volume_out</span><span class="informations">1305×918 72.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My colleague - who is more expert in programming - found that there is a difference in the qform/sform space, which causes this alteration. I share here the links he sent me in this topic:</p>
<ul>
<li><a href="https://github.com/MRtrix3/mrtrix3/issues/1318" class="inline-onebox" rel="noopener nofollow ugc">Inconsistent qform / sform on image write · Issue #1318 · MRtrix3/mrtrix3 · GitHub</a></li>
<li><a href="https://community.mrtrix.org/t/inconsistent-qform-sform-on-nifti-image/1663" class="inline-onebox" rel="noopener nofollow ugc">Inconsistent qform /sform on nifti image - MRtrix3 Community</a></li>
<li><a href="https://discourse.slicer.org/t/nifti-file-sform-and-slicer-image-origin-seem-to-disagree/7711" class="inline-onebox">Nifti file sform and Slicer image origin seem to disagree</a></li>
</ul>
<p>Finally he found that if he runs this code below in FSL, then afterwards the shortcut works well on the new volume:</p>
<blockquote>
<p>fslorient -copysform2qform sample_file.nii</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/287abc20b7b16a600fd78afe00aab659a424aa16.jpeg" data-download-href="/uploads/short-url/5M63xo9w2vuNawNCKr9aiXIiv5k.jpeg?dl=1" title="volume_in" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/287abc20b7b16a600fd78afe00aab659a424aa16_2_690x490.jpeg" alt="volume_in" data-base62-sha1="5M63xo9w2vuNawNCKr9aiXIiv5k" width="690" height="490" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/287abc20b7b16a600fd78afe00aab659a424aa16_2_690x490.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/287abc20b7b16a600fd78afe00aab659a424aa16_2_1035x735.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/287abc20b7b16a600fd78afe00aab659a424aa16.jpeg 2x" data-dominant-color="2E2E2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volume_in</span><span class="informations">1305×927 93.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>.<br>
<strong>A question</strong>: Is there a way that this modification (qform/sform reset) can be done in the Slicer (without having FSL and the required Linux environment)?</p>
<p>Also to share with the community - maybe some could have the same question - Adam made a little modification in the script you’ve sent (as for some reason an error message was received on its initial run), and now everything displayed correctly just as you have said:</p>
<pre><code>def onMouseMoved(observer,eventid):
  mniToWorldTransformNode = getNode('LinearTransform_3')  # replace this by the name of your actual transform
  worldToMniTransform = vtk.vtkGeneralTransform()
  mniToWorldTransformNode.GetTransformToWorld(worldToMniTransform)
  ras=[0,0,0]
  mni=[0,0,0]    
  crosshairNode.GetCursorPositionRAS(ras)
  worldToMniTransform.TransformPoint(ras, mni)
  _ras = "; ".join([str(k) for k in ras])
  _mni = "; ".join([str(k) for k in mni])
  slicer.util.showStatusMessage(f"RAS={_ras}   MNI={_mni}")

crosshairNode=slicer.util.getNode('Crosshair')
observationId = crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, onMouseMoved)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d12d372e618a2deed2b9af49f95f0b0347e6e496.jpeg" data-download-href="/uploads/short-url/tQsFf0R0l0JOgdIL4GbwvdxBL7w.jpeg?dl=1" title="MNI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d12d372e618a2deed2b9af49f95f0b0347e6e496_2_690x146.jpeg" alt="MNI" data-base62-sha1="tQsFf0R0l0JOgdIL4GbwvdxBL7w" width="690" height="146" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d12d372e618a2deed2b9af49f95f0b0347e6e496_2_690x146.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d12d372e618a2deed2b9af49f95f0b0347e6e496.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d12d372e618a2deed2b9af49f95f0b0347e6e496.jpeg 2x" data-dominant-color="363636"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MNI</span><span class="informations">747×159 34.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I will try the transformations, and if any question rises, I’ll let you know.</p>

---

## Post #6 by @lassoan (2021-02-26 17:58 UTC)

<aside class="quote no-group" data-username="Kalman" data-post="5" data-topic="16164">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/59ef9b/48.png" class="avatar"> Kalman:</div>
<blockquote>
<p>My colleague - who is more expert in programming - found that there is a difference in the qform/sform space, which causes this alteration. I share here the links he sent me in this topic:</p>
</blockquote>
</aside>
<p>NIFTI format is simply terrible. It is OK to have a simple and limited file format (such as NRRD) or complicated but very powerful format (such as DICOM). But somehow NIFTI managed to be both overcomplicated and limited at the same time with various redundancies and ambiguities. Unfortunately, this is the file format what the neuroimaging community has come up with and although many people are really unhappy with it, nobody wants to take on the work to redesign it. So, you just need to apply whatever workaround works.</p>
<aside class="quote no-group" data-username="Kalman" data-post="5" data-topic="16164">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/59ef9b/48.png" class="avatar"> Kalman:</div>
<blockquote>
<p>Is there a way that this modification (qform/sform reset) can be done in the Slicer (without having FSL and the required Linux environment)?</p>
</blockquote>
</aside>
<p>Yes, I’m sure you can fix the corrupted files by a few commands for example using <a href="https://nipy.org/nibabel/">nibabel</a>.</p>
<p>Thanks for sharing the code, I’ll add it to the script repository for future reference.</p>

---

## Post #7 by @Kalman (2021-02-27 18:12 UTC)

<p>Thanks for everything, Andras!<br>
Okay, I’ll keep that in mind, and try to shift the focus from NIFTI to NRRD in the future. It seemed first easier to handle compared to the DICOM, but now I’m also aware of its limitations.</p>
<p>I will check the nibabel, thank you for the suggestion!</p>

---
