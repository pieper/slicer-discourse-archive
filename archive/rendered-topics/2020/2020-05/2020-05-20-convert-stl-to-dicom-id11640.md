# Convert STL to DICOM

**Topic ID**: 11640
**Date**: 2020-05-20
**URL**: https://discourse.slicer.org/t/convert-stl-to-dicom/11640

---

## Post #1 by @Zehra (2020-05-20 14:13 UTC)

<p>Hello,<br>
I’ve been using 3D sicer since today. I am very happy to have discovered this program and I hope to solve my problem with it.<br>
I have a CAD model of a pacemaker. I need to convert this model as DICOM to be able to import it later into radiation simulation programs for further research.<br>
I have exported the CAD model as STL and opened it in 3D slicer. With the tool “Create a Dicom series” I thought to convert this model. Unfortunately I cannot select an “Input Volume”. Am I doing something wrong? Could someone give me a short step-by-step guide?</p>
<p>Thanks a lot.</p>

---

## Post #2 by @Zehra (2020-05-20 13:57 UTC)

<p>Hi, I am very new in with this software. I would like to have a 3D model of an implant converted into dicom CT series. As I understood, it cannot be converted directly to dicom since it is not a solid object it is a surface mesh structure of the object. So what can I do to reach my goal? Whats steps are neccessary to transform a stl to dicom? unfortunately I have no idea and I could also not find any hints online.</p>

---

## Post #3 by @lassoan (2020-05-20 15:13 UTC)

<p>Commercial radiation therapy treatment planning systems have quite rigid workflows, so they cannot import arbitrary images volume and paste it into a patient image. The optimal solution depends on what exactly you would like to achieve (are you interested more in the patient dose or how much radiation the pacemaker is exposed to, how accurately you want to model the pacemaker and its placement under the skin, if you have easy access to a radiation treatment planning system, etc.).</p>
<p>In general, you If you want to create a simulated image of a patient CT with a pacemaker then the best is to start with a real CT image of a patient and a real CT image of a pacemaker and combine them.</p>
<p>You might start with simply positioning the pacemaker image (using Transforms module) and add it to the patient image (using Add Scalar Volumes module).</p>
<p>If you want to be more realistic then you can warp the patient image to make space for the pacemaker. You can do this by image warping using fiducial points. You can do this by using Fiducial registration wizard module.</p>
<p>If you want to create simulated CT image of a pacemaker from a CAD model then you need to know the radiometric density of every component of your device. The easiest is to acquire a CT scan of it, but if that’s not an option then you can measure typical densities from CT scan of another pacemaker and then use that when you create your own image. You can create the image by exporting each piece of the device as a separate model file, load them into Slicer and import them into a segmentation. Then fill the image with the chosen radiometric density value using Mask volume effect in Segment Editor.</p>

---

## Post #4 by @njh (2020-05-22 13:25 UTC)

<p>I have been wondering how to do this with STL files and I haven’t gotten around to asking the forum. Thank you for this helpful explanation!</p>

---

## Post #5 by @Zehra (2020-05-27 11:54 UTC)

<p>Thak you for this helpful reply!</p>
<p>Since metals produce artifacts on CT image reconstructions  the density cannot be determined exactly. For this I developed models with which the density can be calculated from the material composition. Thus the densities of the individual components are known. The radiation simulation software is an experimental platform which allows dose simulations on objects (only importable in dcm format). Generalized implant models were drawn with CAD programs. High accuracy of the geometries is important to me.<br>
If I have understood you correctly, I proceed as follows:</p>
<ul>
<li>import STL files of the individual components into Slicer</li>
<li>with the help of Mask volume effect in Segment Editor the volume is filled with the assigned density (which I define).</li>
<li>the individual components can then be joined together.</li>
</ul>
<p>But I still have the following problem: If I only take the implant case, which is made by a titanium alloy with a certain thickness. The case is than only filled with vacuum.  So I have two seperate volumes the case wall and the case cave. How can I fill these two spaces separately in Slicer?</p>

---
