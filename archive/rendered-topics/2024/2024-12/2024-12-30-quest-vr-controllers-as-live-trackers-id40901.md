---
topic_id: 40901
title: "Quest Vr Controllers As Live Trackers"
date: 2024-12-30
url: https://discourse.slicer.org/t/40901
---

# Quest VR controllers as live trackers

**Topic ID**: 40901
**Date**: 2024-12-30
**URL**: https://discourse.slicer.org/t/quest-vr-controllers-as-live-trackers/40901

---

## Post #1 by @sberns (2024-12-30 08:19 UTC)

<p>Hi,<br>
I recently came across 3d slicer and I was wondering if this software is capable of assisting me with a research project. I would like to do real time 2d ultrasound scanning and 3d volumetric reconstruction in virtual reality using a meta quest 3 vr controller as the spatial tracker for the ultrasound probe. Is this currently possible using 3d slicer and its extensions??</p>
<p>Thank you!</p>

---

## Post #2 by @sberns (2024-12-30 14:20 UTC)

<p>I should clarify that I am interested in doing this using quest 3’s augmented reality mode and 3d printing a mount for the quest controller that will attach to the ultrasound probe.</p>

---

## Post #3 by @sberns (2025-01-01 20:23 UTC)

<p>Is anyone able to tell me if this is currently possible? Thank you.</p>

---

## Post #4 by @cpinter (2025-01-07 10:55 UTC)

<p>Do you mean this?</p>
<ol>
<li>Load a 3D volume that you want to virtually scan with ultrasound</li>
<li>Show the volume in AR using Quest 3</li>
<li>Simulate ultrasound images at the probe position determined by the controller</li>
</ol>
<p>1 and 3 are possible, about 2 I’m not sure. Or if you thought about a different workflow please describe yours in detail.</p>

---

## Post #5 by @sberns (2025-01-07 13:24 UTC)

<p>Thanks for your reply!</p>
<p>Workflow would be:</p>
<ol>
<li>attach a quest 3 controller to an ultrasound probe using a 3d printed mount (in order to use the controller as a tracker in 3d slicer for the ultrasound probe)</li>
<li>Put on the quest 3 in passthrough mode (AR)</li>
<li>Slowly live scan a model with the ultrasound probe, displaying each slice superimposed over the model in AR directly below the ultrasound probe</li>
<li>Once a sufficient 2d scan is collected, have 3d Slicer then do a 3d volumetric reconstruction of the images and display the 3d reconstruction in AR superimposed over the model (below the ultrasound probe) instead of just displaying the 2d ultrasound images.</li>
</ol>
<p>Hope that makes sense. Thanks again for your help.</p>

---

## Post #6 by @cpinter (2025-01-07 13:38 UTC)

<p>Yes, thank you for the description!</p>
<ol>
<li>I’m not sure how practical it is to attach a controller, but it is possible, if you want to avoid the need of an external tracker. Maybe Meta manufactures smaller hardware that supports this better. In any case 1) there needs to exist a reference coordinate system fixed to the “patient”, and 2) the US probe needs to be calibrated in reference to the tracked controller to obtain the ControllerToImage transform</li>
<li>The Kitware team must know where the OpenXR support stands currently in Slicer. I haven’t tried this feature and not following the efforts on the commit level so cannot give you an answer whether this is already possible or not</li>
<li>This should be OK if the above 2 are solved</li>
<li>Also possible, using SlicerIGT features</li>
</ol>

---

## Post #7 by @sberns (2025-01-07 13:44 UTC)

<p>Ok so it sounds like I need to check with the Kitware team. Do you know who to contact there?</p>

---

## Post #8 by @cpinter (2025-01-07 13:46 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> or <a class="mention" href="/u/lucasgandel">@LucasGandel</a> might be able to tell you if there is AR support via OpenXR in the current version.</p>

---

## Post #9 by @lassoan (2025-01-07 15:11 UTC)

<p>For tracking and volume reconstruction using the VR controller as tracker you don’t need any developments, it all works, just enable the controller transforms in the Virtual Reality module in Slicer. For volume reconstruction (and for meaningful display of the ultrasound image) you need to figure out the transform between the controller’s coordinate system and the image. You can do this visually or by using any ultrasound probe calibration tools (see <a href="https://www.slicerigt.org/wp/user-tutorials/">SlicerIGT tutorials</a>).</p>
<p>That said, the VR controllers are very bulky and inaccurate. The good visual alignment of the controller and its AR rendering is misleading: the actual absolute tracking accuracy is quite bad compared to even an inexpensive tracker like the <a href="https://www.optitrack.com/cameras/v120-duo/">OptiTrack Duo</a>.</p>
<p>For augmented reality display using Meta Quest 3, you need to improve the Virtual Reality module in Slicer: the module needs to request the camera stream from the headset and then display those images in the view’s background. Since Microsoft discontinued the HoloLens2, it is quite likely that new projects will use Meta Quest 3 for augmented reality (due to quality, availability, and price) and eventually somebody will implement this, but I don’t know about anyone working on this right now.</p>

---

## Post #10 by @sberns (2025-01-08 03:41 UTC)

<p>Thank you very much for your input. It was very informative!</p>

---

## Post #11 by @LucasGandel (2025-01-10 10:35 UTC)

<p>We don’t have anyone working on VTK rendering in passthrough mode at Kitware Europe currently, but we have submitted a few open calls for projects to do so recently (including integration in SlicerVR). I’ll make sure to let you know if things move forward.<br>
When using Quest 3, I think you must use Air Link as opposed to connecting it using the Quest Link cable, otherwise it will request OpenGLES as the rendering backend which is not supported by SlicerVR as far as I know.</p>

---

## Post #12 by @LucasGandel (2025-03-11 09:15 UTC)

<p>We investigated the possibility to enable passthrough in the VTK-OpenXR code and while using the XR_FB_passthrough extension works as expected, the very low framerate we get with the Meta Quest 2 connected with AirLink makes the approach unusable. We will do further testing with higher bandwidth or using a Link cable, stay tuned.</p>

---

## Post #13 by @LucasGandel (2025-03-14 07:28 UTC)

<p>Connecting the MetaQuest 2 to the workstation with Link (i.e. using a cable) gives real-time performances with passthrough enabled.</p>

---
