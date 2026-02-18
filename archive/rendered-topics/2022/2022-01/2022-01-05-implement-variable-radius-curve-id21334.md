# Implement variable radius curve

**Topic ID**: 21334
**Date**: 2022-01-05
**URL**: https://discourse.slicer.org/t/implement-variable-radius-curve/21334

---

## Post #1 by @keri (2022-01-05 00:43 UTC)

<p>Hi,</p>
<p>In SlicerCAT I’m implementing a module to work with curves and scalar values that may be displayed as a radius of the curve or as its color. Thus I need <code>vtkTubeFilter</code>.<br>
There should be an opportunity to interactively change coefficient that multiplies scalar values and thus changing variant radius (for example by QSliderWidget).</p>
<p>I find <code>vtkMRMLMarkupsCurveNode</code> is pretty attractive but I don’t understand how interactively manage such parameters like variant radius i.e. what to connect <code>QSliderWidget</code> to? I suspect I need to have access to the <code>vtkTubeFilter</code> instance wich is stored in <code>vtkSlicerCurveRepresentation</code>. Is it controlled by <code>vtkMRMLMarkupsDisplayNode</code>?</p>

---

## Post #2 by @lassoan (2022-01-05 06:00 UTC)

<p>Currently point scalars (radius, curvature, etc.) can only be used for coloring of the tube, but not for adjusting the tube radius. We anticipated that this will emerge as a need, so we designed markup curves so that with a few little changes this sizing mode can be added:</p>
<ul>
<li>In vtkMRMLMarkupsDisplayNode: add a new <code>UseActiveScalar</code> to CurveLineSizeMode</li>
<li>In vtkSlicerCurveRepresentation2D and vtkSlicerCurveRepresentation3D if you find that <code>CurveLineSizeMode</code> == <code>UseActiveScalar</code> set the <code>TubeFilter</code> to use the active scalar (see <a href="https://github.com/Kitware/VTK/blob/b9f028db9f801258d4c1c0c97716ea7a3c14c289/Filters/Core/Testing/Cxx/TestVaryRadiusTubeFilter.cxx#L68-L73">example</a>)</li>
<li>Expose the new feature on the GUI: probably changing the “Line thickness” <code>absolute</code> toggle button to a combobox (with the options: absolute, relative, active scalar) would be sufficient.</li>
</ul>

---

## Post #3 by @keri (2022-01-05 20:08 UTC)

<p>Thank you, I did as you said and I just got first results, seems pretty good. May I implement this in PR?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67b9fc06b83641494a3039ca741742f8697affa5.jpeg" data-download-href="/uploads/short-url/eNBEg93OD7oUKefGUxjzKZ794Bn.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67b9fc06b83641494a3039ca741742f8697affa5_2_690x336.jpeg" alt="image" data-base62-sha1="eNBEg93OD7oUKefGUxjzKZ794Bn" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67b9fc06b83641494a3039ca741742f8697affa5_2_690x336.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67b9fc06b83641494a3039ca741742f8697affa5_2_1035x504.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67b9fc06b83641494a3039ca741742f8697affa5_2_1380x672.jpeg 2x" data-dominant-color="44424C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×781 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2022-01-05 20:29 UTC)

<p>This looks very promising! Yes, please submit a pull request with the proposed changes.</p>

---

## Post #5 by @keri (2022-01-06 18:01 UTC)

<p>The PR is <a href="https://github.com/Slicer/Slicer/pull/6104" rel="noopener nofollow ugc">here</a>.</p>
<p>As <code>vtkTubeFilter</code> 's variant radius is controlled not only by scalars but also by <code>SetRadius(double)</code> and <code>SetFactorRadius(double)</code> I decided not to edit <code>CurveLineSizeMode</code>so the user can control both these parameters in <code>VariableRadius</code> mode.</p>
<p>Also in my case I expect that scalar values will have both negative and positive values. Using such scalars as radius lead to some unwanted results.<br>
So I would like to have a possibility to translate all scalars to positive range by adding scalar value that is equal to something like <code>abs(min(scalars))</code>.</p>
<p>If someone has ideas how to do that I could probably try to implement that.</p>

---

## Post #6 by @keri (2022-01-22 19:19 UTC)

<p>Hi,</p>
<p>How do you think how to fix the <a href="https://github.com/Slicer/Slicer/pull/6104" rel="noopener nofollow ugc">issue with incorrect diameter and color in slice view</a>? I think I should look in <code>vtkSlicerCurveRepresentation2D</code> implementation but can’t find anything appropriate.</p>

---
