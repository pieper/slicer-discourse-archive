# Connect Slicer 3D with Hololens 2

**Topic ID**: 20544
**Date**: 2021-11-09
**URL**: https://discourse.slicer.org/t/connect-slicer-3d-with-hololens-2/20544

---

## Post #1 by @Gabriella-Rus (2021-11-09 13:40 UTC)

<p>Hello! I have Hololens 2 and I want to use it to view medical images in Slicer 3D. Is that possible with  Slicer’s VR extension?</p>

---

## Post #2 by @lassoan (2021-11-09 20:07 UTC)

<p>We are in the process of updating Slicer’s VTK version and transition to using OpenXR (instead of the current OpenVR) to connect to headsets. OpenXR will allow rendering Slicer to render directly in a HoloLens2.</p>
<p>This will be one of the topics of the <a href="https://discourse.slicer.org/t/reminder-project-week-36-prep-meetings-start-tomorrow-nov-9th/20534">upcoming Slicer Project Week in January</a>. You may join one of the preparation calls to learn more.</p>

---

## Post #3 by @Gabriella-Rus (2021-11-10 05:45 UTC)

<p>Oh, great! Thank you!</p>

---

## Post #4 by @Honza_Hecko (2022-03-31 18:28 UTC)

<p>is there some result??<br>
Thank you</p>

---

## Post #5 by @lassoan (2022-04-02 01:40 UTC)

<p>Yes, there had been progress. Slicer has switched to the latest VTK master version, which supports both OpenVR and OpenXR. The SlicerVirtualReality extension works with this latest VTK version. I think it still uses the OpenVR interface, but in the mid/long term the interface will be switched to OpenXR.</p>
<p>In the meantime, you can use CloudXR with the HoloLens. It has been recently demonstrated to work well with Slicer and an Oculus Quest headset, and it is supposed to work rieh HoloLens, too.</p>

---
