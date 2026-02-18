# How to work with vtkParametricFunction in SlicerJupyter?

**Topic ID**: 34833
**Date**: 2024-03-11
**URL**: https://discourse.slicer.org/t/how-to-work-with-vtkparametricfunction-in-slicerjupyter/34833

---

## Post #1 by @Juergen (2024-03-11 18:17 UTC)

<p>Hello,<br>
This is a question not directly related to Slicer, however I am using the SlicerJupyter kernel to interface with vtk.<br>
I am trying to create my own parametric surface with the abstract class vtkParametricFunction but I don’t seem to define the necessary methods of my derived class to make it work. Has anybody worked with vtkParametricFunction in Python before and gotten it to work?<br>
Thanks for any suggestions.</p>

---

## Post #2 by @lassoan (2024-03-12 03:57 UTC)

<p>You can override methods of VTK classes in C++ but I don’t think you can override methods of a VTK object in Python. See <a href="https://discourse.vtk.org/t/python-custom-render-pass/5743" class="inline-onebox">python custom render pass - Support - VTK</a> and <a href="https://vtkusers.public.kitware.narkive.com/CmEWpTLI/vtkparametricfunction-sub-classes-in-python" class="inline-onebox">[vtkusers] vtkParametricFunction sub-classes in Python</a>. You can ask David Gobbi on the VTK forum to confirm that it is still the case.</p>
<p>However, even if you could override VTK methods in Python, you would probably not want do it for a parametric function because the function evaluation has to be extremely fast. If you implement the function in Python then an operation on the parametric function could take a minute, while if you used C++ it could take just a second.</p>

---

## Post #3 by @Juergen (2024-03-13 17:15 UTC)

<p>Thanks, Andras.</p>
<p>It seems that it is still the case that it is not possible to subclass from an abstract base class that was implemented in C++ in the VTK code.</p>
<p>I thought that speed would not matter too much. Even if it was much slower than a C++ implementation, the surface would only need to be created once, no?</p>
<p>Right now I’m trying to create a surface that has cross-sections made of two half-ellipses, each with a different minor radius, but both with the same major radius. In the third dimension these cross-sections then linearly change in terms of their major and minor radius.</p>
<p>Initially I’ve used only two of these cross sections, at the beginning and at the end. Then I tried to use <code>vtkRuledSurfaceFilter</code> to connect them. Unless I used a really high number of points along the combined half-ellipses, something on the order of 2000, I would not get the right shape, especially around the areas of largest slopes/curvature: <code>arc.SetResolution(2000, 40); arc.SetRuledModeToResample()</code>. I also tried to experiment with <code>arc.SetOrientLoops(True)</code> but I’m not sure this did anything in my case. This seems to me not to be a very efficient way of doing things and I have to experiment with the resolution to create a kink-free shape. Now I created more cross-sectional contours between the end contours but that just adds complexity to this procedure.</p>
<p>Another things I was struggling with is that when I try to “combine” the two half-ellipses (created with <code>vtkEllipseArcSource</code>) via the <code>vtkAppendPolyData</code> tool, I always ended up with a contour with two cells in it. Then the <code>RuledSurfaceFilter</code> doesn’t work correctly because it combines lines (aka cells) <code>i</code> with <code>i+1</code>. I ended up writing boiler-plate code to manually merge the two half-ellipses so that they are one line (aka one cell).</p>
<p>Thanks for any suggestions you might have.</p>

---
