# RT phantom drawing

**Topic ID**: 21189
**Date**: 2021-12-22
**URL**: https://discourse.slicer.org/t/rt-phantom-drawing/21189

---

## Post #1 by @naninano1 (2021-12-22 21:08 UTC)

<p>Hello,</p>
<p>I want to draw a patient phantom with regular shapes (ellipse, sphere, cube, etc) as body, organs at risk, tumor, etc. as CT Dicom images, but I am not sure whether it is possible with Slicer 3d or not.</p>
<p>I have some ideas, but I couldn’t find any toolkit to convert my 3d structures to Dicom CT.<br>
For example, drawing 3d volumes in Autocad and converting the stl or cad files to CT slides.<br>
Or drawing regular masks on a given ct image in slicer3d and removing the main CT. However, I could not find any segmentation tools for drawing regular shapes in the extentions of slicer3d.</p>
<p>I would appreciate it if you would help me in this regard</p>

---

## Post #2 by @naninano1 (2021-12-23 08:58 UTC)

<p>I also tried Creator Models module, and created some 3D models. Subsequently, I converted them to segmentation. However, the models contours are not visible in the axial, sagital, or coronal planes of CT. The models are only visible on 3D window</p>

---

## Post #3 by @cpinter (2021-12-23 16:25 UTC)

<p>Have you made sure that these objects are in the place you actually want them to be? I.e. if you show your volume using volume rendering does it appear in the same place as your phantom objects in the 3D view?</p>
<p>On another note you can create sphere, box, cylinder in Segment Editor. Sphere using the Paint effect, and the rest with Scissors.</p>

---

## Post #4 by @naninano1 (2021-12-24 20:45 UTC)

<p>Thank you very much for your prompt and detailed reply. It solved my problem.</p>
<p>Sincerely Yours,<br>
Navid</p>

---
