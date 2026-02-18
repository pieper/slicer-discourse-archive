# Creating Extension for Phantom Touch from 3D systems to manipulate plane in Slicer3D

**Topic ID**: 18944
**Date**: 2021-07-27
**URL**: https://discourse.slicer.org/t/creating-extension-for-phantom-touch-from-3d-systems-to-manipulate-plane-in-slicer3d/18944

---

## Post #1 by @ajitcpdm (2021-07-27 13:38 UTC)

<p>Guys … please suggest me steps to start with! Integration or creating API interface to work with Phantom Touch!</p>

---

## Post #2 by @lassoan (2021-07-27 18:09 UTC)

<p>There are many solutions to this, depending on what you would like to use the haptic interface for.</p>
<p>If you want to control a robot or provide haptic feedback then you need a very fast control loop, so you would probably want to use ROS and just stream the controller’s pose to Slicer via OpenIGTLink. We have set this up recently using CISST-SAW’s <a href="https://github.com/jhu-saw/sawSensablePhantom/tree/devel">Phantom interface</a> and <a href="https://github.com/jhu-saw/sawOpenIGTLink/tree/devel">OpenIGTLink interface</a>. Alternatively, there are many other ROS node for Phantom haptic devices and you can use <a href="https://github.com/openigtlink/ROS-IGTL-Bridge">ROS IGTL bridge</a> for streaming transforms from ROS to Slicer.</p>
<p>If you just want to use the Phantom as a 3D mouse then you can probably find a Python package that you can pip-install into Slicer’s Python environment to receive the transform and set it into a transform node in Slicer.</p>
<p>You can also create a small C++ loadable module that uses OpenHaptics interface to communicate with the device.</p>
<p>What would you like to achieve?</p>

---

## Post #3 by @ajitcpdm (2021-07-29 09:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="18944">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Phantom as a 3D mouse</p>
</blockquote>
</aside>
<p>Hi,</p>
<p>Thanks. Excellent feedback, I’m trying interact in Slicer for Phantom as 3D mouse.<br>
Could you please guide me landing with a Python Package that can be pip install.</p>
<p>Thanks again.</p>
<p>Best wishes,<br>
Ajit</p>

---

## Post #4 by @lassoan (2021-07-31 22:26 UTC)

<p>If searching on Google and PyPI does not bring up anything usable then ask from 3DSystems Support (or community forum, if they have any). If they cannot help then you still have all the other options. Also, if you just need a 3D mouse (no force feedback) then you have much better options:</p>
<ul>
<li>you can get two full 6-DOF controllers (not just on 5-DOF controller) with lots of buttons and an immersive stereo display from a <a href="https://github.com/KitwareMedical/SlicerVirtualReality">virtual reality headset</a>
</li>
<li>you can just buy an optical tracker, such as <a href="https://www.optitrack.com/cameras/v120-duo/">OptiTrack Duo</a> (for a fraction of the price, with a wireless tool)<br>
and connect using <a href="http://slicerigt.org/">SlicerIGT</a>
</li>
<li>if you don’t need high absolute accuracy (just accurate relative positioning) then you can use a single webcam and <a href="https://www.youtube.com/watch?v=MOqh6wgOOYs">glue a 2D barcode on a pencil and use that as 3D mouse</a>.</li>
</ul>

---
