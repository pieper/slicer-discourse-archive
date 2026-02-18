# Visualization of live reconstruction

**Topic ID**: 17424
**Date**: 2021-05-03
**URL**: https://discourse.slicer.org/t/visualization-of-live-reconstruction/17424

---

## Post #1 by @agp (2021-05-03 20:36 UTC)

<p>Operating system: Windows10<br>
Slicer version: 4.11.20210226<br>
Plus version: 2.9.0.20210217<br>
Expected behavior: visualizing the reconstructed volume as the reconstruction goes by<br>
Actual behavior: the reconstructed volume is visible once the acquisition completed</p>
<p>Hello everyone,</p>
<p>I’ve been testing to reconstruct in real-time a pelvis sawbone using SlicerIGT (using a Telemed ultrasound probe and a NDI polaris tracker) and I had trouble visualizing the live reconstruction.<br>
I have followed both tutorials from <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="noopener nofollow ugc">power point presentation U34</a> and <a href="https://www.youtube.com/watch?v=2vXeJxYFou4" rel="noopener nofollow ugc">youtube video</a> but I did not manage to configure Slicer such as it shows the reconstructed volume during the ultrasound acquisition.<br>
I have been able with both SlicerIGT modules Volume Reconstruction and Plus Remote, to launch the Live Reconstruction, but I could visualize the reconstructed volume in the 3D window only when I finished the acquisition.<br>
Is there a specific setting in the Volume Rendering module to show the reconstructed volume in real-time during the acquisition ?</p>
<p>Also I noticed a weird behaviour of the US image parameters  (depth, gain, frequency,…):<br>
when I had the US probe in the water tank containing the sawbone before setting the Volume Reslice Driver to view the US image, the US image was nice,<br>
but when I set the Volume Reslice Driver before putting the US probe in of the water tank, the US image was getting blurred and very noisy, it seemed like the US parameters set in the configuration file were not applied at all<br>
Is there a default behaviour for the US image visualization that could change the input US parameters when visualizing the US image for the first time ?</p>
<p>Thanks in advance for any help !</p>

---

## Post #2 by @agp (2021-05-06 08:12 UTC)

<p>UPDATE</p>
<p>for my first problem of not seeing the reconstructed volume in real-time during the US acquisition, I noticed that having the reference I used for the spatial calibration, visible by the tracker solved the problem. I think I wrongly configure the xml configuration file and made the reference presence necessary for the volume reconstruction. Is there an example of configuration file for live reconstruction that does imply using the US probe only (without reference) ?</p>
<p>And if it can be of help for anyone, I solved the US image quality problem by setting the US parameters in the visualization software Echo Wave II, while Slicer is running. And with the help of <a href="https://discourse.slicer.org/t/ultrasound-image-always-overexposed/14755">this post</a> I tuned the contrast and brightness in Slicer viewer using the window/level mouse mode</p>

---
