---
topic_id: 31382
title: "Measure Diameter Using Centerline Length And Surface"
date: 2023-08-26
url: https://discourse.slicer.org/t/31382
---

# Measure Diameter using centerline length and surface

**Topic ID**: 31382
**Date**: 2023-08-26
**URL**: https://discourse.slicer.org/t/measure-diameter-using-centerline-length-and-surface/31382

---

## Post #1 by @cams2b (2023-08-26 17:29 UTC)

<p>I am trying to extract the radius at each point on the centerline from my tubular mesh. I am using the vmtk script vmtkDistanceToCenterlines and setting the variable EvaluateCenterlineRadius = True.</p>
<p>I was expecting this function to return a radius for each function on the centerline, however, the number of points returned is equal to the number of points in the surface mesh. I am confused with what this result signifies and I am wondering if there is a way to extract what I am interested in.</p>
<pre><code class="lang-auto">    distance_calculator = vmtkscripts.vmtkDistanceToCenterlines()
    distance_calculator.Surface = output_surface
    distance_calculator.Centerlines = centerline_points
    distance_calculator.UseCombinedDistance = False
    distance_calculator.UseRadiusInformation = False
    distance_calculator.EvaluateCenterlineRadius = True
    distance_calculator.ProjectPointArrays = False
    distance_calculator.UseCombinedDistance = False



    distance_calculator.RadiusArrayName = "Radius"    
    distance_calculator.Execute()
    distance = distance_calculator.Surface
    distance_to_centerline = distance.GetPointData().GetArray("Radius")```

Thank you all in advance for your help.</code></pre>

---

## Post #2 by @chir.set (2023-08-26 18:25 UTC)

<p>If your requirements do not confine you to vmtkscripts, you may consider using Slicer itself.</p>
<p>By installing SlicerVMTK extension using the extensions manager, you’ll find <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/CrossSectionAnalysis.md" rel="noopener nofollow ugc">Cross-section analysis</a> module that does what you want, and much more.</p>

---
