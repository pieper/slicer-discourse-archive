---
topic_id: 37200
title: "Optimal C Arm Angulation Along A Plane From Ct"
date: 2024-07-04
url: https://discourse.slicer.org/t/37200
---

# Optimal C-arm angulation along a plane from CT

**Topic ID**: 37200
**Date**: 2024-07-04
**URL**: https://discourse.slicer.org/t/optimal-c-arm-angulation-along-a-plane-from-ct/37200

---

## Post #1 by @Miguel_Nobre_Menezes (2024-07-04 18:50 UTC)

<p>Hi there. I’m an Interventional Cardiologist looking to use 3D Slicer for planning interventions based on CT. Current state of the art software (3mensio) enables C-arm rotation angles along a plane, thereby displaying a sinusoidal wave of LAO/RAO CAU/CRA. Is there any way of doing this on 3D Slicer? I read this post from a couple of years ago (<a href="https://discourse.slicer.org/t/get-c-arm-angles-from-3d-view-orientation/24435" class="inline-onebox">Get C-arm angles from 3D view orientation</a>) where lassoan (Andras Lasso) said they were working on this. I’m reasonably comfortable with python, in case this is reasonably easy to implement. One<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/625523d1a62647c8ccb6ee1a6e16b198e2b79f43.png" alt="image" data-base62-sha1="e1TcCorBNwKIimBNBSaa0a5fEoX" width="290" height="346"></p>

---

## Post #2 by @lassoan (2024-07-04 21:03 UTC)

<p>Yes, we have a really nice cathlab simulator for Slicer that includes configurable C-arm models, realistic 3D rendering (for patient collision and field of view evaluation), DRR generation, segmentation based opacitication simulation, etc.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f0bee4a992effbc1b11c48185d99683f2681d65.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/660a48cd9269a9391f7b513aa8f36f5e7594b3b2.jpeg">
  </div><p></p>
<p>We’ll release this publicly as soon as the associated paper gets accepted for publication, which will probably take a few months.</p>
<p>It should not be hard to add computation of optimal fluoro angles from markup planes or lines, but we have not worked on that. It would be great if you could work it out in the next few months and then when the cathlab simulator gets released we can help with integrating that into the module. You can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-line">this code snippet</a> to compute how the C-arm can be rotated around a line or you can use any of the formulations described in the papers dicussing optimal C-arm angulations.</p>

---

## Post #3 by @Miguel_Nobre_Menezes (2024-07-04 21:47 UTC)

<p>Thanks for the swift reply. I really do hope to see that in action soon. I’d argue that for intervention, we absolutely need to understand the planes of desired target structures and display them accordingly. I’d love to create a simple module geared for TAVI and left atrial appendage occlusion in particular, because I believe existing comercial options are extremely expensive considering what they do.</p>

---

## Post #4 by @Miguel_Nobre_Menezes (2024-07-06 12:07 UTC)

<p>Thanks for the swift reply. I really do hope to see that in action soon. I’d argue that for intervention, we absolutely need to understand the planes of desired target structures and display them accordingly.</p>
<p>In the mean time, I tried your code snippet and it works - thanks! But the problem is, it “collides” with another snippet I was using to get the angles of a fluoro, which I found on another post by yourself:</p>
<pre><code class="lang-auto">threeDViewIndex = 0  # change this to show angles in a different 3D view

def positionerAngleFromViewNormal(viewNormal):
    # According to https://www5.informatik.uni-erlangen.de/Forschung/Publikationen/2014/Koch14-OVA.pdf
    nx = -viewNormal[0]  # L
    ny = -viewNormal[1]  # P
    nz =  viewNormal[2]  # S
    import math
    if abs(ny) &gt; 1e-6:
        primaryAngleDeg = math.atan(-nx/ny) * 180.0 / math.pi
    elif nx &gt;= 0:
        primaryAngleDeg = 90.0
    else:
        primaryAngleDeg = -90.0
    secondaryAngleDeg = math.asin(nz) * 180.0 / math.pi
    return [primaryAngleDeg, secondaryAngleDeg]

def formatPositionerAngle(positionerAngles):
    primaryAngleDeg, secondaryAngleDeg = positionerAngles
    text =  f'{"RAO" if primaryAngleDeg &lt; 0 else "LAO"} {abs(primaryAngleDeg):.1f}\n'
    text += f'{"CRA" if secondaryAngleDeg &lt; 0 else "CAU"} {abs(secondaryAngleDeg):.1f}'
    return text

def cameraUpdated(cameraNode, view):
    viewNormal = cameraNode.GetCamera().GetDirectionOfProjection()
    positionerAngleText = formatPositionerAngle(positionerAngleFromViewNormal(viewNormal))
    view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperRight, positionerAngleText)
    view.cornerAnnotation().GetTextProperty().SetColor(1,1,0)  # yellow
    view.scheduleRender()

layoutManager = slicer.app.layoutManager()
view = layoutManager.threeDWidget(threeDViewIndex).threeDView()
threeDViewNode = view.mrmlViewNode()
cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(threeDViewNode)
cameraObservation = cameraNode.AddObserver(vtk.vtkCommand.ModifiedEvent, lambda caller, event, view=view: cameraUpdated(caller, view))

cameraUpdated(cameraNode, view)

# Execute the next line to stop updating the positioner angles in the view corner
# cameraNode.RemoveObserver(cameraObservation)
</code></pre>
<p>I understand one method is actually rotating the volume while the other is using the camera view. My question now would be, which would be the better option? Adapting both for rotating the volume or the camera?</p>

---

## Post #5 by @lassoan (2024-07-08 13:47 UTC)

<p>I would recommend to rotate the C-arm (=camera) and keep the image stationary.</p>

---

## Post #6 by @Miguel_Nobre_Menezes (2024-07-15 18:12 UTC)

<p>Thanks for the tip and the great work you guys do with 3D slicer. So I did end up building a module that I’m quite happy with.</p>
<p>It automatically calculates the ideal projection of a given plane. I geared it to the aortic valve but can be applied to any structure. It displays the projection curve which can be click as well. I also added custom measurements.</p>
<p>This short clip shows it in action, with its almost every feature.</p>
<p>I still need to review the code because it’s still quite messy, especially because I’m just an enthusiast Interventional Cardiologist, not a developer.</p>
<p>What’s now missing is a module for studying the vasculature access. I tried several modules but none seemed quite right. I’ll think about working on that as well.</p>
<p>Link: <a href="https://drive.google.com/file/d/1WlN7XExhRCvTYhapD8tRF8O7qRqjTpBK/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1WlN7XExhRCvTYhapD8tRF8O7qRqjTpBK/view?usp=sharing</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd8d38a9df9a1447e31b9eaabd2988599b437667.jpeg" data-download-href="/uploads/short-url/vBW5lJvTql7R0ZOlfyB0Me7dLXp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd8d38a9df9a1447e31b9eaabd2988599b437667_2_690x366.jpeg" alt="image" data-base62-sha1="vBW5lJvTql7R0ZOlfyB0Me7dLXp" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd8d38a9df9a1447e31b9eaabd2988599b437667_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd8d38a9df9a1447e31b9eaabd2988599b437667_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd8d38a9df9a1447e31b9eaabd2988599b437667_2_1380x732.jpeg 2x" data-dominant-color="898682"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1020 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2024-07-15 19:53 UTC)

<p>Amazing progress! The clickable plane projection curve is especially a nice touch (and could be useful when you work with multiple lines you want to rotate around).</p>
<p>I would recommend to tune the projection computation to auto-rotate the view (spin the image around the camera normal) to make patient superior direction approximately be the up direction in the view (see implementation <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-slice-position-and-orientation-from-a-normal-vector-and-position">here</a>) as it is done in fluoro systems.</p>
<p>Also note that the annotations don’t need to be done manually anymore. For example, “Cardiac TS2” model of MONAIAuto3DSeg extension can segment all the relevant cardiac structures and from that you can get your landmark points fully automatically. Maybe computation of the commissure points would not be completely trivial, but should be doable, too.</p>
<p>If you think this module could be useful for others, too, then it could make sense to add it to an extension so that it is easily accessible.</p>

---

## Post #8 by @Miguel_Nobre_Menezes (2024-07-16 15:30 UTC)

<p>Thanks! With regards to your observations:</p>
<ul>
<li>I did the current angulation projection on purpose - I did have one at first like you suggested, but the way the module works is precisely replicating what we use in clinical practice for TAVI (<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f107e411c63fc378c4553276bb846b1e3d158b5f.jpeg" data-download-href="/uploads/short-url/yofYxQ6RrDvI1tSqq6COugnh5oj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f107e411c63fc378c4553276bb846b1e3d158b5f_2_623x499.jpeg" alt="image" data-base62-sha1="yofYxQ6RrDvI1tSqq6COugnh5oj" width="623" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f107e411c63fc378c4553276bb846b1e3d158b5f_2_623x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f107e411c63fc378c4553276bb846b1e3d158b5f_2_934x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f107e411c63fc378c4553276bb846b1e3d158b5f.jpeg 2x" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1080×866 87.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
).  See link here (<a href="https://www.sciencedirect.com/science/article/pii/S1936879814009236" rel="noopener nofollow ugc">https://www.sciencedirect.com/science/article/pii/S1936879814009236</a>)That’s why the logic behind my implementation is getting all the angulations corresponding to all vectors perpendicular to the aortic plane</li>
<li>Automatically getting the hinge points would be a “Holy Grail” as it would fundamentally render the process fully automatic. I’m not aware of any software that does this, but all that it would take I suppose would be getting a lot of cases where we’ve had such measurements done. I have already thought of finding a way of exporting our current measurements in official leading software to 3D slicer to form a training base. If I find I way, a collaborative approach with other institutions could follow for validating it</li>
<li>I have experimented with the MONAI and Total Segmentator. They’re very impressive, but even on a MacBook M3 Max with 64 Gb of RAM (what I’m running) seems pretty slow, as it takes a couple of minutes running the inference. Don’t know if that’s to be expected or not.</li>
<li>I’ll be testing my module locally with fellow Structural Heart Operators to see how they feel about it and correct/find possible bugs. If they’re happy with it, I think it may make sense to either integrate it with a existing extension (like Heart Slicer or others) or provide an entirely new one.</li>
</ul>
<p>I’ll keep in touch as I further develop this.</p>

---

## Post #9 by @lassoan (2024-07-16 16:18 UTC)

<aside class="quote no-group" data-username="Miguel_Nobre_Menezes" data-post="8" data-topic="37200">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/miguel_nobre_menezes/48/77210_2.png" class="avatar"> Miguel_Nobre_Menezes:</div>
<blockquote>
<p>I did the current angulation projection on purpose - I did have one at first like you suggested, but the way the module works is precisely replicating what we use in clinical practice for TAVI</p>
</blockquote>
</aside>
<p>I suggest implementing exactly what is shown in the paper you linked to. What is missing in the current implementation is the automatic physical spin of the detector (and 90/180 degrees image rotation in software) as you rotate the C-arm. The projection curve does not specify the detector spin. The spin is computed from simple rules that help the clinician orient himself, by aligning directions on screen with anatomical directions. For head first supine position the commonly used rules are:</p>
<ul>
<li>align screen up with patient superior direction</li>
<li>align screen right with patient left direction (except near lateral images, in that case with patient anterior direction)</li>
</ul>
<aside class="quote no-group" data-username="Miguel_Nobre_Menezes" data-post="8" data-topic="37200">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/miguel_nobre_menezes/48/77210_2.png" class="avatar"> Miguel_Nobre_Menezes:</div>
<blockquote>
<p>I’m not aware of any software that does this</p>
</blockquote>
</aside>
<p>Commercial software are generally a couple of years behind. This will be avaialable on most commercial software within a few years.</p>
<aside class="quote no-group" data-username="Miguel_Nobre_Menezes" data-post="8" data-topic="37200">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/miguel_nobre_menezes/48/77210_2.png" class="avatar"> Miguel_Nobre_Menezes:</div>
<blockquote>
<p>I have experimented with the MONAI and Total Segmentator. They’re very impressive, but even on a MacBook M3 Max with 64 Gb of RAM (what I’m running) seems pretty slow, as it takes a couple of minutes running the inference. Don’t know if that’s to be expected or not.</p>
</blockquote>
</aside>
<p>Apple’s AI support is still limited. Pytorch (the toolkit used by most medical image computing AI), is gradually getting some hardware accelaration features on Apple, but it is still quite slow. On CPU or Apple graphics hardware segmentation may take several minutes, so what you experienced is the expected behavior.</p>
<p>If you need speed then you can use a desktop computer with a strong NVIDIA GPU. Currently, the <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/releases/tag/ModelsTestResults">Cardiac TS2 model runs in 20-25 seconds on an NVIDIA GPU</a>.</p>
<p>Even if processing takes a few minutes, it should be generally acceptable, because fully automatic processing does not take any time of the clinician. You could even configure a workflow in your hospital to automatically process the CT image right after it is acquired.</p>
<aside class="quote no-group" data-username="Miguel_Nobre_Menezes" data-post="8" data-topic="37200">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/miguel_nobre_menezes/48/77210_2.png" class="avatar"> Miguel_Nobre_Menezes:</div>
<blockquote>
<p>If they’re happy with it, I think it may make sense to either integrate it with a existing extension</p>
</blockquote>
</aside>
<p>Sounds great! By then hopefully the SlicerHeart cathlab simulator will be released, too, so your module could use/extend features provided by the simulator or features from your module could be integrated into the simulator.</p>

---

## Post #10 by @Miguel_Nobre_Menezes (2024-07-19 17:33 UTC)

<p>Thanks for the feedback. I’m not exactly sure what you meant by the automatic physical spin of the detector, since the module computes the exact angulation of the C arm as it rotates. Currently, the anatomical plane is viewed exactly as we view it in clinical practice, and according to that paper. For example, when doing TAVI (aortic plane), we view the aorta on screen aligned but obliquely and use that to calculate the angle (how horizontal/vertical it is). I even tried applying it to other structures where I also perform interventions (such as the left atrial appendage) and it is working very nicely.</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="37200">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I suggest implementing exactly what is shown in the paper you linked to. What is missing in the current implementation is the automatic physical spin of the detector (and 90/180 degrees image rotation in software) as you rotate the C-arm. The projection curve does not specify the detector spin. The spin is computed from simple rules that help the clinician orient himself, by aligning directions on screen with anatomical directions. For head first supine position the commonly used rules are:</p>
<ul>
<li>align screen up with patient superior direction</li>
<li>align screen right with patient left direction (except near lateral images, in that case with patient anterior direction)</li>
</ul>
</blockquote>
</aside>
<p>In the meantime, I’ll also compare what I’m getting to current state of the art software (3mensio). If looking good, I’ll challenge colleagues to conduct a multicentric validation study - would make it more appealing.</p>
<p>Thanks for all your support, I’ll keep in touch. I’ve cleaned up the code a bit in the meantime, but I’m sure I’ll still find bugs that may require some help.</p>

---

## Post #11 by @lassoan (2024-07-20 12:57 UTC)

<aside class="quote no-group" data-username="Miguel_Nobre_Menezes" data-post="10" data-topic="37200">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/miguel_nobre_menezes/48/77210_2.png" class="avatar"> Miguel_Nobre_Menezes:</div>
<blockquote>
<p>I’m not exactly sure what you meant by the automatic physical spin of the detector, since the module computes the exact angulation of the C arm as it rotates.</p>
</blockquote>
</aside>
<p>I am referring to image rotation:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00965ab747fb4bb490fc8f5d180767a6373bb898.jpeg" data-download-href="/uploads/short-url/5c8ecZAfYyMj0MGQmjUfK6969W.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00965ab747fb4bb490fc8f5d180767a6373bb898_2_527x500.jpeg" alt="image" data-base62-sha1="5c8ecZAfYyMj0MGQmjUfK6969W" width="527" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00965ab747fb4bb490fc8f5d180767a6373bb898_2_527x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00965ab747fb4bb490fc8f5d180767a6373bb898_2_790x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00965ab747fb4bb490fc8f5d180767a6373bb898_2_1054x1000.jpeg 2x" data-dominant-color="9C9898"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1252×1186 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For a specific anatomical orientation (RAO/LAU, CRA/CAU) the up direction in the image is not constrained by a simple sequential rotation around two orthogonal axes, but the image can be rotated due to several reasons:</p>
<ul>
<li>Simple software rotation</li>
</ul>
<div class="youtube-onebox lazy-video-container" data-video-id="rLkiq094LFk" data-video-title="Basic Usage of a C-Arm" data-video-start-time="692" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=rLkiq094LFk&amp;t=692" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/rLkiq094LFk/hqdefault.jpg" title="Basic Usage of a C-Arm" width="480" height="360">
  </a>
</div>

<ul>
<li>C-arm base rotation: up direction for a specific anatomical orientation depends on the C-arm base angle (or wig/wag). Floor-mounted systems automatically compute anatomical angles that take into account the base (L-arm) angle.</li>
<li>On some systems the detector can be rotated completely independently:</li>
</ul>
<p>Philips Allura:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5ec475a95db7fdb1858f65e77bbecfc2b51a446.jpeg" data-download-href="/uploads/short-url/z5xcIo3runJmJeoORhJRNY7jzQa.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5ec475a95db7fdb1858f65e77bbecfc2b51a446_2_690x498.jpeg" alt="image" data-base62-sha1="z5xcIo3runJmJeoORhJRNY7jzQa" width="690" height="498" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5ec475a95db7fdb1858f65e77bbecfc2b51a446_2_690x498.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5ec475a95db7fdb1858f65e77bbecfc2b51a446_2_1035x747.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5ec475a95db7fdb1858f65e77bbecfc2b51a446.jpeg 2x" data-dominant-color="EAEBEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1150×831 90.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Siemens Artis Zee:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a914d7a8a96906c1115251397a9c71110e82440d.jpeg" alt="image" data-base62-sha1="o7LlwyutbfkHNaUJ5yHrYP8kk7b" width="600" height="450"></p>

---

## Post #12 by @Miguel_Nobre_Menezes (2024-07-20 14:07 UTC)

<p>I see what you mean now. Actually, from a strictly intervention perspective, calculating the spin is not that relevant. So long as we know the RAO/LAO CAU/CRA angles we already know which way is up. We seldom use it, except for applying filters, like the one in the image you sent. For example, I know just from looking at the image you sent that it is an RAO CAU projection of the left coronary artey. In that image, left is (kind of) posterior (in terms of heart anatomy) and vice versa.</p>
<p>The paper I sent you does not calculate the spin, only those 2 angle pairs, as does current structural intervention software that we’re using in clinical practice (3mension).</p>
<p>Having said that, the module is not entirely devoid of spin calculations - in fact, when the rotate button is pressed, the sagital and coronal planes are rotated so that the specified plane is facing perfectly upwards and horizontal (as per the plane, not the patient).</p>
<p>Calculating the spin would be interesting though. If I can find the time I’ll consider doing it. But first, i’d like to see how colleagues react to thr module prior to adding further stuff, as I’m sure I’ll run into bugs as, like I said, I’m not a developer, just an enthusiast who loves these challenges.</p>

---

## Post #13 by @pengwang0126 (2026-01-08 04:01 UTC)

<p>Hi Miguel,</p>
<p>I came across your CArmAngulation plugin and found the idea very interesting. I wanted to ask whether the plugin has been fully completed or if it is still a work in progress.</p>
<p>I am currently working on C-arm geometry and angulation modeling, and I am particularly interested in how you compute the C-arm angles and derive the associated sine (or sinusoidal) curves for angulation representation. If you are willing to share some details about the mathematical model or implementation approach you used, I would greatly appreciate it.</p>
<p>Thank you for your work and for any insights you might be able to share.</p>
<p>Best regards,</p>

---

## Post #14 by @lassoan (2026-01-08 13:50 UTC)

<p>Virtual Cath Lab C-arm simulator is publicly available now in SlicerHeart.</p>
<p>Your could add a section to the module GUI that takes 1 or 2 line markups as inputs and lets you align the C-arm to be perpendicular to those lines.</p>

---
