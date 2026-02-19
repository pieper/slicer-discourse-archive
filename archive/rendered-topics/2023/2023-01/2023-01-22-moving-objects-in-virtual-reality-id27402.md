---
topic_id: 27402
title: "Moving Objects In Virtual Reality"
date: 2023-01-22
url: https://discourse.slicer.org/t/27402
---

# Moving objects in virtual reality

**Topic ID**: 27402
**Date**: 2023-01-22
**URL**: https://discourse.slicer.org/t/moving-objects-in-virtual-reality/27402

---

## Post #1 by @Vit_P (2023-01-22 13:09 UTC)

<p>Hello good people)</p>
<p>I am new to 3D slicer virtual reality.</p>
<p>I created a 3D object in 3D Slicer 5.2.1 and launched virtual reality extension. I use HTC Vive. The object is visible in the HMG, but controllers look like totally disabled and I cannot manipulate with the object. Any other activities (Fly/Transform entire scene/Transform objects/) as described in <a href="https://github.com/KitwareMedical/SlicerVirtualReality" class="inline-onebox" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerVirtualReality: A Slicer extension that enables user to interact with a Slicer scene using virtual reality.</a> do not work.</p>
<p>I exported the stl file and opened it in VRifier. All manupulations work perfectly.</p>
<p>Could You please suggest how to fix this problem?</p>

---

## Post #2 by @cpinter (2023-01-22 15:27 UTC)

<p>Very briefly, please wait until it is fixed.<br>
For more information do a search on discourse, there are many topics about this, and although we are now much closer to the solution, the situation is the same.</p>

---

## Post #3 by @jcfr (2023-01-23 22:33 UTC)

<p>To follow up, we are working on the issue and expect this to fix this shortly.</p>

---

## Post #4 by @LucasGandel (2023-01-27 12:57 UTC)

<p>A fix is on its way, see <a href="https://github.com/LucasGandel/SlicerVirtualReality/commit/c993cd7c83c9aa6728c24f5b6f95f917e7a8c50c" rel="noopener nofollow ugc">SlicerVirtualReality/c993cd7</a>. This commit brings back the ability to grab objects and fly around.<br>
Although untested (yet), the multi-gesture (Pan, Pinch, Rotate) are also expected to work, but with grip buttons only.<br>
Please check the commit message to get an idea of the next steps.</p>

---

## Post #5 by @cpinter (2023-02-01 12:14 UTC)

<p>Lucas, we tried the very latest commits yesterday and none of the interactions worked unfortunately with the HP headset. Maybe related to the json, not sure. This is why I asked about a way to verify the current settings, to be able to check where things break.</p>

---

## Post #6 by @LucasGandel (2023-02-01 14:05 UTC)

<p>This is very bad news. I bet this is related to the driver, or the json.<br>
Was the HP headset working in previous versions of SlicerVirtualReality? Or were you using another headset?</p>
<p>Without recompiling VTK, I am not sure there is anything you can do to check the current bindings are correctly setup, besides adding an observer to the <code>vtkOpenVRRenderWindowInteractor</code> <code>AnyEvent</code> to see if it fires anything.<br>
If events are fired, the problem is with the interactor style.</p>

---

## Post #7 by @cpinter (2023-02-01 15:37 UTC)

<p>The headset works with the older versions. I just realized there is no <code>OnSelect3D</code> function, so your commit was probably not merged. Let me cherry pick that and see what changes.</p>
<p>Thanks for the suggestions! I’ll add an observer if I need to find out about the events.</p>

---

## Post #8 by @cpinter (2023-02-01 15:45 UTC)

<p>Cherry-picked your commit (<a href="https://github.com/LucasGandel/SlicerVirtualReality/commit/fae17999118b09d113b526090ae3b855d31ee3b4" class="inline-onebox">Rename VR interactor style callback functions · LucasGandel/SlicerVirtualReality@fae1799 · GitHub</a>) and flying and grabbing works!!</p>

---

## Post #9 by @Vit_P (2023-02-03 10:26 UTC)

<p>As far as I follow it, now works. But nothing improved at me. I reloaded the 3DSlicer and still the same</p>
<p>Can You guide me step-by-step what I should do please?</p>

---

## Post #10 by @cpinter (2023-02-03 14:35 UTC)

<p>There is one commit that is not integrated yet. Lucas please let me know if it is ready to integrate (your latest branch in your fork, referenced in the issue about flying in SlicerVR).</p>

---

## Post #11 by @Vit_P (2023-03-18 20:50 UTC)

<p>Unfortunately, still does not work with the controllers to move the object in space. However, the controller does rotate/move the object if used on the Desktop interface as shown on the picture. What can be done?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7ebcdcb4e9fc6c754e6c1ab086648775328b2d5.jpeg" data-download-href="/uploads/short-url/znd8QvjZTNKLit5ILMUjV056P8V.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7ebcdcb4e9fc6c754e6c1ab086648775328b2d5_2_690x317.jpeg" alt="image" data-base62-sha1="znd8QvjZTNKLit5ILMUjV056P8V" width="690" height="317" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7ebcdcb4e9fc6c754e6c1ab086648775328b2d5_2_690x317.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7ebcdcb4e9fc6c754e6c1ab086648775328b2d5_2_1035x475.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7ebcdcb4e9fc6c754e6c1ab086648775328b2d5.jpeg 2x" data-dominant-color="A1B4C5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1087×500 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @cpinter (2023-03-19 15:53 UTC)

<p>I tried it on Friday and it works. You need to use the latest preview version 5.3.0.</p>

---

## Post #13 by @Michele_Bailo (2023-03-20 11:58 UTC)

<p>Hi there,<br>
I tried today with my HTC Vive Pro, but I’m still not able to move the entire scene altogether pressing the trigger in both controllers (which I remember I was able to do some time ago).<br>
I can move single object separately with the latest preview version 5.3.0, but in neurosurgical planning moving the scene altogether would be way more helpful. Is there anything I can do about it?</p>
<p>Thanks in advance</p>

---

## Post #14 by @cpinter (2023-03-20 17:26 UTC)

<p>Two handed gestures are not yet fixed. What you can do is fly using the joystick or use the center view button in the VR module to set the VR camera based on the 3D view in Slicer.</p>

---

## Post #15 by @Michele_Bailo (2023-03-29 11:01 UTC)

<p>Thanks you very much for you kind answer.<br>
Can I ask you if you think that is something that is planned to be fixed in the future?<br>
Alternatively, would it work properly if I install back older version of 3D Slicer?</p>
<p>thank you very much for your patience.</p>

---

## Post #16 by @rbumm (2023-03-29 13:35 UTC)

<p>Although that’s by no means an acceptable solution, Slicer 4.11 should support it.</p>

---

## Post #17 by @Vit_P (2023-08-13 13:25 UTC)

<p>Hi! In 5.2.1 version moving 3D objects in VR still not fixed?</p>

---

## Post #18 by @rbumm (2023-08-13 15:53 UTC)

<p>Please check out the 3D Slicer preview release (5.3.0), where it is fixed.</p>

---

## Post #19 by @Vit_P (2023-09-08 07:47 UTC)

<p>Could not find link to 5.3.0. Instead, updated to 5.4.0. In this, can fly through with touch on the trackpad, but grabbing and other still not possible.</p>

---

## Post #20 by @rbumm (2023-09-08 10:41 UTC)

<p>Yes, correct, in my last test I had the same experience. Sorry!</p>

---

## Post #21 by @Vit_P (2023-10-19 15:56 UTC)

<p>When do You expect it to be fixed?</p>

---
