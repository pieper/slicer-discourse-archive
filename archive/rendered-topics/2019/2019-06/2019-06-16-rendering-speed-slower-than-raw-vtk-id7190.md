# Rendering speed slower than "raw" Vtk

**Topic ID**: 7190
**Date**: 2019-06-16
**URL**: https://discourse.slicer.org/t/rendering-speed-slower-than-raw-vtk/7190

---

## Post #1 by @klayman (2019-06-16 22:17 UTC)

<p>Hello, I am loading a CT volume 600x600x312 to slicer4, and playing with the same volume in raw VTK by using a modified Medical4 demo where I use VtkOpenGLGpuMapper (I guess it’s the same I get in slicer4 when I select Vtk GPU raycast), gradient opacity, same colormap as in the slicer4 test, shading disabled in both cases, so all in all should be the same settings.</p>
<p>Question 1: is there a way to share the settings exactly between slicer4 and a VTK c++ program?<br>
Question 2: Slicer4 is way slower in rendering compared to a bare VTK render window. It’s slower during interaction, almost as if Slicer4 is always rendering full quality, and it’s much slower also in the final renders. Am I missing some settings, or is Slicer4 doing something different than VTK?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-06-16 22:36 UTC)

<p>Rendering speed should be exactly the same as in any other VTK-based application.</p>
<p>There might have been a couple of weeks when the 4.11.x preview version always rendered in full quality. Try latest preview version and tune quality settings in Volume rendering module / Advanced / Techniques / Quality and Interactive speed.</p>

---

## Post #3 by @muratmaga (2019-06-17 04:02 UTC)

<p>I don’t know if it is related or not, but I always have been getting poor rendering performance when the quality is set to adaptive, and had better performance with ‘Normal’ quality.</p>

---
