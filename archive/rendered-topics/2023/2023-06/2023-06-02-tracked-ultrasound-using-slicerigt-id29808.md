# Tracked ultrasound using SlicerIGT 

**Topic ID**: 29808
**Date**: 2023-06-02
**URL**: https://discourse.slicer.org/t/tracked-ultrasound-using-slicerigt/29808

---

## Post #1 by @farhanbme (2023-06-02 18:45 UTC)

<p>Hi, I want to use SlicerIGT for tracking real-time Ultrasond using aruco markers. Please guide what steps do I need to follow, hardward setup required?</p>
<p>thanks</p>

---

## Post #2 by @ungi (2023-06-03 23:18 UTC)

<p>You need to stream ultrasound and tracking data to Slicer via OpenIGTLink. One option is to configure PLUS for optical marker tracking (<a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOpticalMarkerTracker.html" class="inline-onebox" rel="noopener nofollow ugc">Plus applications user manual: Optical Marker Tracker</a>). You will need to find a way to stream ultrasound too via OpenIGTLink. If your ultrasound device is supported by PLUS, then follow PLUS documentation. If not, an option is to use a frame grabber like Epiphan that captures the video signal from an output port of your ultrasound machine. PLUS supports some frame grabbers.<br>
When you have the synchronized ultrasound and tracking data stream in Slicer already, then you may follow SlicerIGT tutorials for calibration of the ultrasound position: <a href="https://www.slicerigt.org/wp/user-tutorial/" class="inline-onebox" rel="noopener nofollow ugc">User tutorial | SlicerIGT</a></p>
<p>ArUco markers will be unstable and have large tracking error. It is not the best choice for e.g. reconstructing 3D ultrasound volumes. But if your application does not require high accuracy, then it may work for you. There are much more accurate optical tracker devices around the price range of a computer, e.g. OptiTrack Duo.</p>

---

## Post #3 by @farhanbme (2023-06-04 06:08 UTC)

<p>Thanks for guidance, I can see the markers in the slicer, (also added the models of my choice) but can you please guide me more about the ultrasound image visualization in the slicer? how can I do that using PLUS or epiphan along with the optical marker tracking already running in the PLUS. I’ve this N3 NOVADEX MEDICAL SYSTEMS ultrasound machine.</p>
<p>Regards,</p>

---

## Post #4 by @ungi (2023-06-04 12:45 UTC)

<p>That ultrasound machine is not directly supported by PLUS. If the machine has a video output, then the fastest way to grab the images would be to use a frame grabber. A better solution would be to ask the ultrasound manufacturer if they can give you a programming interface to obtain the original images in real time. But most ultrasound machines don’t have a research interface. You could also consider purchasing an ultrasound machine with a research interface.</p>

---
