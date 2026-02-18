# How to create a color table that doesn't include 0

**Topic ID**: 1451
**Date**: 2017-11-13
**URL**: https://discourse.slicer.org/t/how-to-create-a-color-table-that-doesnt-include-0/1451

---

## Post #1 by @muratmaga (2017-11-13 23:23 UTC)

<p>Hi</p>
<p>I have results from an image analysis that I want to overlay on the intensity values. When I choose the RGB as the color map of the overlay, the green fills everywhere.<br>
I want to exclude values that are very close 0 on either side of the range (say from -.01 to 0.01) from the color table. How can I do it?</p>

---

## Post #2 by @lassoan (2017-11-14 01:38 UTC)

<p>Color tables (vtkMRMLColorTableNode) that are editable using the GUI use <a href="https://www.vtk.org/doc/nightly/html/classvtkLookupTable.html">vtkLookupTable</a>, which uses equally spaced entries. If you want to have an abrupt change in the color map then you need to have many entries.</p>
<p>If you don’t need to edit the entries manually, then you can use procedural color nodes, which use <a href="https://www.vtk.org/doc/nightly/html/classvtkScalarsToColors.html">vtkScalarsToColors</a> object internally. Color transfer functions can use arbitrarily spaced control points, so you don’t have to add a lot of entries. I think eventually even procedural color nodes are converted to color tables internally, so if you need abrupt changes then you need to set number of colors in the color table node to a large number (hundreds, maybe even thousands).</p>

---

## Post #3 by @cpinter (2017-11-14 02:03 UTC)

<p>You can edit a color node after you duplicate it in the Colors module (Informatics category). If you set the alpha value of a color to 0, then you make it transparent, thus “excluding” it - if I understood you question properly.</p>

---

## Post #4 by @lassoan (2017-11-14 02:20 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="3" data-topic="1451">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>If you set the alpha value of a color to 0, then you make it transparent, thus “excluding” it</p>
</blockquote>
</aside>
<p>Yes, exactly. However, if he needs 0.00 to make transparent but &gt;0.01 and &lt;-0.01 non-transparent, then it means that on a mapped value range of (-1;+1), he would need to have 200 color table entries - not easy to edit manually. If the range of values is (-100;+100) then he would need to have 20000 color table entries, which is impossible to edit manually and might have performance impact (maybe not, I haven’t ever tried use such large color table).</p>

---

## Post #5 by @cpinter (2017-11-14 02:33 UTC)

<p>Right. I’d probably have a python function create the color table in <code>.slicerrc.py</code> and define another one setting that color table and a good W/L on the image analysis output volumes.</p>

---

## Post #6 by @muratmaga (2017-11-14 05:14 UTC)

<p>Thanks for the replies. I have been trying to use the RBG continuous color map, but I can’t seem to find a place to to change the opacity. In the screenshot the middle point is 0 and the ones that are on left and right are -.1, and .1 respectively. But where is the opacity setting?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d0cd3121bb12400bbf5109c58ade073881bc7b1.png" data-download-href="/uploads/short-url/mpkrel6dtweo7mldTEPBVvISSZz.PNG?dl=1" title="Capture"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9d0cd3121bb12400bbf5109c58ade073881bc7b1_2_690x297.PNG" alt="Capture" data-base62-sha1="mpkrel6dtweo7mldTEPBVvISSZz" width="690" height="297" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9d0cd3121bb12400bbf5109c58ade073881bc7b1_2_690x297.PNG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9d0cd3121bb12400bbf5109c58ade073881bc7b1_2_1035x445.PNG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9d0cd3121bb12400bbf5109c58ade073881bc7b1_2_1380x594.PNG 2x" data-dominant-color="958CB0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">2277×983 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2017-11-14 11:45 UTC)

<p>There is a new class, <a href="https://www.vtk.org/doc/nightly/html/classvtkDiscretizableColorTransferFunction.html">https://www.vtk.org/doc/nightly/html/classvtkDiscretizableColorTransferFunction.html</a>, which can do opacity mapping as well. It is not available in Slicer GUI yet, but maybe you can create it in Python and set it in a color node using SetAndObserveColorTransferFunction.</p>
<p>A color editor widget has been added for it a couple of weeks ago to CTK library, so the Colors module could be modified to use discretizable color transfer function class by default and this new color editor widget.</p>

---
