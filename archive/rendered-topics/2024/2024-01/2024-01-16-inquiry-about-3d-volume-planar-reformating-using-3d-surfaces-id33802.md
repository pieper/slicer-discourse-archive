---
topic_id: 33802
title: "Inquiry About 3D Volume Planar Reformating Using 3D Surfaces"
date: 2024-01-16
url: https://discourse.slicer.org/t/33802
---

# Inquiry About 3D Volume Planar Reformating Using 3D Surfaces in 3D Slicer

**Topic ID**: 33802
**Date**: 2024-01-16
**URL**: https://discourse.slicer.org/t/inquiry-about-3d-volume-planar-reformating-using-3d-surfaces-in-3d-slicer/33802

---

## Post #1 by @fmarcano (2024-01-16 17:31 UTC)

<p>I am exploring the capabilities of 3D Slicer for medical imaging visualization and analysis, and I have a specific question regarding 3D volume planar reformating functionalities. I understand that 3D Slicer allows for the reformating of 3D volumes into planar representations using a path defined by a 3D curve. My question is whether there is a similar functionality to use a 3D surface as a guide for reformating.</p>
<p>My specific interest lies in the ability to consider curvatures in multiple directions simultaneously, which is particularly relevant for structures with complex geometries, such as the surface of a person’s head. I understand that reformating using a 3D curve is limited in this regard, as it only accounts for changes in direction along the curve.</p>
<p>Is there a functionality in 3D Slicer that would allow me to use a 3D surface to guide the process of reformating a 3D volume into a planar representation? If not, would this be feasible through the development of a custom module, or are there alternatives within the software that might approximate this functionality?</p>
<p>Any guidance or suggestions would be greatly appreciated. Thank you in advance. Best Regards.</p>

---

## Post #2 by @pieper (2024-01-16 18:42 UTC)

<p>One way to do this in Slicer would be to make a nonlinear transform that implements the curve, such a grid transform where the displacement vectors are defined by the shape.  <a href="https://github.com/Slicer/Slicer/issues/7179">This discussion</a> has some links.</p>

---

## Post #3 by @lassoan (2024-01-18 05:44 UTC)

<p>Curved Planar Reformat module does exactly that: builds a grid transform where the transformed rectangle coordinates corresponds to a rectangle that is swept along the curve. You can very similarly sweep a rectangle along a surface. There are two sweep strategies even for a curve (straightening or stretching) and for a surface there could be even more, but one simple strategy could be to draw a curve on the surface and use the “stretching” method.</p>
<p>If you only need to map surface points (don’t need 3D mapping between the original and the straightened space) then you can have a look at texture mapping methods. These methods map the surface points to coordinates on a planar surface. For a person’s head a good mapping could be the projection to a sphere or ellipsoid (using <a href="https://vtk.org/doc/nightly/html/classvtkTextureMapToSphere.html">VTK texture mapping filters</a>); or you can use a least-square conformal mapping algorithm (LSCM, available in a module in SlicerHeart extension), which can flatten an arbitrary surface patch to plane with minimal distortion.</p>

---

## Post #4 by @fmarcano (2024-01-18 13:49 UTC)

<p>Thank you very much for the answer. Indeed, the coordinates of the transformed rectangle correspond to a rectangle that moves along the curve. This would be appropriate if we consider, for example, a cylinder, and trace a curve along its circumference, say at half the height of the cylinder. The result would be the cylinder ‘unrolled’ like a map.</p>
<p>If we consider a sphere I would like, for instance, to have a planar representation in a single rectangle of a spherical zone located between two parallels of the sphere. As I understand, this could not be achieved with just a curve along any parallel, since the transformed rectangle moves along the curvature of the parallel, but there is no indication of how the rectangle should deform orthogonally (along the meridian), which might be possible with a second guiding curve, at least in the case of the sphere. For more complex 3D geometries, something more than a couple of directional curves might be necessary, such as a 3D surface. Is it correct, or am I wrong?</p>

---

## Post #5 by @lassoan (2024-01-18 16:09 UTC)

<p>If you resample with warped surfaces (and not planes) then the operation is no longer curved <em>planar</em> reformatting. Curved planar reformatting is useful because you can make measurements in the straightened image (if you use stretching method then distance measurements in the entire center slice will be accurate, if you use straightening method then measurements near the centerline of the center slice will be accurate).</p>
<p>If you don’t need to be able to perform any measurements then you can get a 3D warping transform by arbitrarily specifying a grid transform or thin-plate spline transform as you see fit. I cannot make any specific recommendation on what makes sense for your application.</p>
<p>If you don’t need a 3D-to-3D transform but you only need to straighten a surface (3D surface to 2D plane mapping) then you can use texture mapping methods that I described above. They are well understood and studied methods.</p>
<p>If you want to discuss any further then we cannot remain at this very generic level but we would need to know more about your application and what you would like to ultimately achieve.</p>

---
