# Elastix components not installed

**Topic ID**: 13660
**Date**: 2020-09-23
**URL**: https://discourse.slicer.org/t/elastix-components-not-installed/13660

---

## Post #1 by @janneke_slicer (2020-09-23 13:29 UTC)

<p>Hello,</p>
<p>I am using Elastix in 3DSlicer. I also used it in Matlab, but Slicer is better for visualization. I’m for example interested in visualizing the deformation field.<br>
However, I noticed that in 3D Slicer Elastix is limited. For example, I want to use the following components (which I can use with Elastix in Matlab):</p>
<ul>
<li>ShrinkingImagePyramid (pyramid)</li>
<li>NearestNeighborInterpolator (interpolator)</li>
<li>AdvandKappaStatistic (metric)<br>
for which I get the following error in Slicer:<br>
“This component is not installed!”</li>
</ul>
<p>Is there a way to install extra components?<br>
If not, does someone know how to import/visualize a displacement field in Slicer from a text (ASCII) transformation file (which thus results from performing Elastix registration in Matlab)?</p>
<p>Thank you,</p>
<p>Janneke</p>

---

## Post #2 by @lassoan (2020-09-23 15:23 UTC)

<p>Elastix bundled with Slicer is built with default options. Maybe some exotic things are not enabled by default, but most features should work. Where and how do you get these error messages? (what steps do you do exactly to get them?)</p>
<p>You can also use any other Elastix installation (which is built with all the special options you need), by setting its path in Advanced / Custom Elastix toolbox location.</p>
<p>You can of course load a displacement field from file, too. You can directly load displacement fields from mhd files that Elastix (transformix) creates. You can also load linear and bspline transform from text files by calling SlicerElastix module logic’s <code>readElastixTransformToVTK</code> methods from Python console or script.</p>

---
