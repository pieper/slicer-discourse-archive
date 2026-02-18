# How vmtkboundaryreferencesystems works?

**Topic ID**: 14082
**Date**: 2020-10-16
**URL**: https://discourse.slicer.org/t/how-vmtkboundaryreferencesystems-works/14082

---

## Post #1 by @Jana_Trdlicova (2020-10-16 17:01 UTC)

<p>Hi all,</p>
<p>I am trying to implement a non-interactive clipping and meshing of an aneurysm geometry and I have problems with understanding what vmtkboundaryreferencesystems does. More specifically, I need to control that my inlet goes to the first line so that the centerlines can be computed correctly (and also because of the labelling). How does the function decide what’s first? Is there a possibility to specify the order of lines in the output file (corresponding to inlet/outlets reference systems)?</p>
<p>Thank you,<br>
Best wishes,</p>
<p>Jana Trdlicová</p>

---

## Post #2 by @lantiga (2020-10-18 13:07 UTC)

<p>Hello <a class="mention" href="/u/jana_trdlicova">@Jana_Trdlicova</a>, the job of <code>vmtkboundaryreferencesystems</code> is to create a dataset with as many vertices as there are open boundaries, with each vertex placed at the barycenter of each open boundary. For each boundary, the script computes the average radius, the outward normal (or an approximation if the boundary is not planar), as well as two points so that <code>(n+o, o)</code>, <code>(p1, o)</code> and <code>(p2, o)</code> are orthogonal (see <a href="https://github.com/vmtk/vmtk/blob/master/vtkVmtk/ComputationalGeometry/vtkvmtkBoundaryReferenceSystems.cxx#L243" rel="noopener nofollow ugc">https://github.com/vmtk/vmtk/blob/master/vtkVmtk/ComputationalGeometry/vtkvmtkBoundaryReferenceSystems.cxx#L243</a>).</p>
<p>Now, regarding the issue of having inlets on the first line, the order of reference systems coincides with the order of the open boundaries that are found on the mesh, which is not easily predicted (<a href="https://github.com/vmtk/vmtk/blob/master/vtkVmtk/Misc/vtkvmtkPolyDataBoundaryExtractor.cxx#L82" rel="noopener nofollow ugc">https://github.com/vmtk/vmtk/blob/master/vtkVmtk/Misc/vtkvmtkPolyDataBoundaryExtractor.cxx#L82</a>).</p>
<p>Your best bet with the current algorithms is try to match the reference system coordinates (the coordinates of the vertices of the output poly data) to your inlet/outlet specifications after the fact.</p>
<p>For instance, if you had a <code>vtkPolyData</code> with a PointData integer for inlet/outlet points (e.g. 0 for inlet, 1 for outlet), you could use <code>vmtksurfaceprojection</code> to bring that information into the output of <code>vmtkboundaryeferencesystems</code>.</p>
<p>Hope this helps.</p>

---

## Post #3 by @Jana_Trdlicova (2020-10-24 08:09 UTC)

<p>Hi Luca,</p>
<p>thank you for your quick response. It seems to me that the code is quite complicated and I’m glad that I can just use it. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>In my code, I compute the reference systems first, then I use these points as source and target points to compute centerlines and finally, I generate (and label) the mesh. So, the easiest solution is probably to read the vmtk-computed reference system file and test what’s my input (because I can see the approximate coordinates in ParaView).</p>
<p>Have a nice day,<br>
Jana</p>

---
