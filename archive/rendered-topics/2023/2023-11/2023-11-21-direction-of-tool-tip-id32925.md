# Direction of tool tip

**Topic ID**: 32925
**Date**: 2023-11-21
**URL**: https://discourse.slicer.org/t/direction-of-tool-tip/32925

---

## Post #1 by @saeedeh_lavasany (2023-11-21 10:59 UTC)

<p>Hello,</p>
<p>I tracked a tool using the EMT system and restored transformation matrices. I have obtained the position of the tool in a 3D space, which I’ve derived from CT/SPECT images in MATLAB. Now, I aim to represent the tool’s orientation accurately. Although everything appears correctly aligned in 3D Slicer, I’m encountering issues displaying the tool’s direction accurately in MATLAB.</p>
<p>I’m seeking guidance on converting a rotation matrix to Euler angles. The rotm2eul function isn’t providing the correct directional information. Any advice on how to achieve accurate representation would be greatly appreciated.</p>

---

## Post #2 by @lassoan (2023-11-21 12:21 UTC)

<p>You can use Pivot calibration module’s Spin calibration to determine the shaft direction of a rod-shape tool. See U-11 <a href="https://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorial</a>. The module is in SlicerIGT extension.</p>
<p>If your tool has a more complex shape then you can determine the transform between the coordinate system of the tool’s model and the tool-attached sensor using landmark registration. See U-12 <a href="https://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorial</a>.</p>

---

## Post #3 by @saeedeh_lavasany (2023-11-21 12:54 UTC)

<p>I have completed the entire process of Pivot calibration and Landmark registration, resulting in the Tool to CT transformation matrices. These matrices accurately map the tool’s tip position to the CT-based model. Now, I am seeking guidance on displaying the tool’s direction within this space using the Tool to CT Transformation matrix in MATLAB.</p>

---

## Post #4 by @lassoan (2023-11-21 15:15 UTC)

<p>Regarding Matlab, the only advice I can give is that it is time to move on. 15 years ago, Matlab was one of the best environment for scientific computing and computational algorithm prototyping, but in recent years Python has made Matlab largely irrelevant. Specifically, prototyping surgical navigation systems in Matlab would be so much inferior due to lack of frameworks, libraries, licensing hassles, and difficulties in deployment and product translation that switching to Python would pay off very quickly.</p>

---

## Post #5 by @saeedeh_lavasany (2023-11-22 08:00 UTC)

<p>Thank you for your advice. I’ll attempt it using Python.</p>

---
