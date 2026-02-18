# Morphological changes analysis

**Topic ID**: 20624
**Date**: 2021-11-15
**URL**: https://discourse.slicer.org/t/morphological-changes-analysis/20624

---

## Post #1 by @SPoloni (2021-11-15 12:08 UTC)

<p>Hi all!<br>
I want to study the morphological changes on 2 models of the same vascular district acquired in time. After the registration and the computation of the distances between the two models, give a point on the centrelines, I would like to radiate 8 equidistant lines and save the coordinates obtained by intersecting the lines and each of the two models. Do you have any suggestions for commands I could use?</p>
<p>Or do you know of other methods to compare morphological changes in a set of points between two models that have changed slightly over time?</p>
<p>Thank you in advance,<br>
Sofia</p>

---

## Post #2 by @lassoan (2021-11-16 14:16 UTC)

<p>What do you mean by morphological changes? Changes in what properties would you like to quantify? Vessel diameter changes, centerline displacements, …?</p>

---

## Post #3 by @SPoloni (2021-11-16 14:28 UTC)

<p>Hi! I want to detect geometrical changes between the models, I mean the surface displacement. Specifically after the registration of the models I want to understand the coordinates of a set of points on a model and the correspondent points coordinates on the second.</p>

---

## Post #4 by @lassoan (2021-11-16 15:32 UTC)

<p>Do you expect primarily vessel dilation (changes in diameter) or movement (displacement of centerline)? The toolset you use to quantify these are quite different.</p>
<p>How can you determine which points correspond to each other in the two models?</p>

---

## Post #5 by @SPoloni (2021-11-16 16:41 UTC)

<p>I mainly expect a vessel dilatation or stenosis in small regions, while the centerline are quite the same. The idea is that after the recording of the models, starting from a point on the centerline of one of them, and irradiate some lines perpendicular to the centerline, the points on the first model met by the line corresponds to the points met by the line on the second model. Briefly the good registration assures the correspondence between the points on the two models. But I don’t know exactly how to implement this procedure</p>

---

## Post #6 by @lassoan (2021-11-16 21:20 UTC)

<p>You can already get centerlines and vessel diameter along the centerline extracted automatically using <a href="https://github.com/vmtk/SlicerExtension-VMTK#readme">SlicerVMTK</a>. If you need displacement vector and magnitude at each mesh point then you can use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ModelToModelDistance">ModelToModelDistance extension</a>, to get a dense displacement field you can use <a href="https://github.com/SlicerRt/SegmentRegistration#segment-registration">SegmentRegistration</a> extension in 3D Slicer. All these provide a convenient graphical user interface, but you can also access the features in Python for automation or batch processing.</p>

---
