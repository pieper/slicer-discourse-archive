# Accuracy of Intel RealSense D435

**Topic ID**: 11737
**Date**: 2020-05-27
**URL**: https://discourse.slicer.org/t/accuracy-of-intel-realsense-d435/11737

---

## Post #1 by @qeee (2020-05-27 16:19 UTC)

<p>Hello, I would like to start experimenting with image guided surgery and I would like to ask about your experience with the accuracy of Intel realsense devices, specifically the D435. Is the navigation accuracy within few millimeters? can i use tracked stylus to navigate or just ArUco pictures?</p>

---

## Post #2 by @lassoan (2020-05-27 18:05 UTC)

<p>ArUco accuracy with a simple webcam is typically in the order of a few millimeters within the image plane (moving up/down, left/right, rotate along axis parallel with the camera normal), but it is a magnitude worse (centimeters of error) out of the image plane (moving towards/away from camera, rotate out of plane). This is insufficient for real surgical navigation but may be acceptable for simple educational demos.</p>
<p>If you use a 3D vision system, such as Intel RealSense then you should be able to reduce out of plane translation/rotation error to a similar level as in-plane. We have preliminary, not fully complete implementation for this in <a href="https://www.plustoolkit.org">Plus toolkit</a> (contribution to complete/improve this would be very welcome). Few-millimeter tracking error means total system error (after patient registration, tool calibration, and tracking relative to a reference marker) to the order of 1-2 centimeters. This may be good for some surgical applications, such as vertebral level localization or burr hole placement.</p>
<p>You can buy a fully calibrated professional tracker, such as an <a href="https://www.optitrack.com/products/v120-duo/">Optitrack Duo</a> for $2300, which provides submillimeter tracking error, so you can achieve a total system error of 1-2 millimeters, which is acceptable for many surgical applications.</p>
<p>ArUco + Intel RealSense’s cost advantage ($200 instead of $2300) is negligible compared to total cost of a procedure and all the necessary tools. However, as the RealSense camera is significantly smaller and lighter than traditional optical trackers and it can also acquire surface scan, it could have important clinical applications - mainly where classic surgical navigation systems are impractical (too large, too difficult to calibrate, etc).</p>

---
