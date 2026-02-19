---
topic_id: 27259
title: "Export 3D Model To Hololens 2 Device"
date: 2023-01-16
url: https://discourse.slicer.org/t/27259
---

# Export 3d model to Hololens 2 device

**Topic ID**: 27259
**Date**: 2023-01-16
**URL**: https://discourse.slicer.org/t/export-3d-model-to-hololens-2-device/27259

---

## Post #1 by @Caterina (2023-01-16 11:12 UTC)

<p>Good morning,<br>
I need to export a 3d model from Slicer to the Hololens 2 device (MRTK 2.8.3).</p>
<p>I performed segmentation on 3d slicer (Segment Editor) and I used OpenAnatomy module to export the segmentation part as gltf.</p>
<p>Using the 3d viewer library of MRTK 2.8.3, the file cannot be opened.</p>
<p>Can I have information about the best way to export a segmentation model obtained from 3d slicer in order to be imported in Hololens 2 as a hologram?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2023-01-17 05:47 UTC)

<p>Do you use Unity? Do you plan to embed your models into the application and rebuild the application for each patient case?</p>
<p><a href="https://biig-igt.uc3m.es/people/">Javier Pascau’s group</a> implemented solutions for avoiding this tedious rebuilding step of the application for each patient (or using dropbox, etc. to transfer the file) and implemented sending of segmentations to Unity applications directly from Slicer in a few seconds via OpenIGTLink. They also implemented real-time sending of transforms, so you can move objects either using the HoloLens or in Slicer and all positions are synchronized.</p>

---

## Post #3 by @Caterina (2023-01-17 10:38 UTC)

<p>Thank you very much for reply.<br>
We don’t use embedded models but these are loaded from the Hololens file system or from a remote web server.<br>
We use Unity for the development of the Hololens2 app.<br>
Actually we are interested in using the optimal parameters to export 3d model from slicer to Hololens 2. Which is the procedure to do it?<br>
Thanks</p>

---

## Post #4 by @AliciaPose (2023-01-18 15:07 UTC)

<p>Hello Caterina,<br>
If I understood correctly, you want to create a 3D model from a segmentation in 3D Slicer, and then import it to Unity (and ultimately, to Microsoft HoloLens 2). I recommend you follow these steps:</p>
<ol>
<li>Once you have finished your segmentation on Segment Editor, go to Segmentations module.</li>
<li>Scroll down to the “Export/Import models and labelmaps” section.</li>
<li>Set the operation to “Export” and the output type to “Models”. Click on “Export” button.</li>
<li>You should see now all 3D models corresponding to your segmentation in the “Models” module.</li>
<li>Go to “Save” in the upper left corner in 3D Slicer and select the models you want to save. Make sure you save them all as Wavefront OBJ (.obj extension). This is the 3D model format recognized in Unity.</li>
<li>Open Unity and simply drag and drop your .obj files into the desired Assets folder. You can now work with them just like with any GameObject in the scene.</li>
</ol>
<p>NOTE: 3D Slicer and Unity work with different metric (mm vs m). Depending on your application, you may want to scale all your models in Unity with a factor of 0.001.</p>
<p>NOTE 2: Some 3D models may be too large for some applications. Please, consider decimating them using the Surface Toolbox in 3D Slicer.</p>
<p>NOTE 3: When you save the .obj files in 3D Slicer, a .mtl file is also saved. You can also import this file next to the .obj in Unity to preserve your model’s texture.</p>
<p>I hope this helps. Please, reply if you have any more issues.</p>

---

## Post #5 by @Mark_Ryan (2024-08-03 10:29 UTC)

<p>Somewhat related - is there a pathway for displaying volume renderings in Unity or is the actual 3D model from the segmentation required?</p>

---

## Post #6 by @lassoan (2024-08-03 21:53 UTC)

<p>There are some volume renderers for Unity but they are very limited. Overall, Unity is just a poor platform for developing medical image computing applications, as you need to redevelop everything from scratch in an environment that is intended for gaming.</p>

---
