# Fiducial Markups cursor 

**Topic ID**: 1967
**Date**: 2018-01-29
**URL**: https://discourse.slicer.org/t/fiducial-markups-cursor/1967

---

## Post #1 by @lgroves (2018-01-29 16:11 UTC)

<p>Hello,</p>
<p>I was wondering if there is a way to within the python script for a scripted loadable module, change the cursor appearance for the markups fiducial placement. Specifically I would like to change it from the circle with the arrow to a cross hair. Any help is appreciated.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2018-01-29 16:30 UTC)

<p>If you want to initiate fiducial placement from your module GUI then you can use qSlicerMarkupsPlaceWidget. See an example in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Markups#Add_a_button_to_module_GUI_to_activate_fiducial_placement">Markups module documentation</a>.</p>

---

## Post #3 by @Nicole_Aucoin (2018-01-29 16:39 UTC)

<p>The appearance of the fiducial marker is controlled via the display node associated with the fiducial list node. If you look at the information for developers here:<br>
<a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/Markups" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/4.8/Modules/Markups</a><br>
you can get the fiducial list and then:</p>
<blockquote>
<p>dispNode = fidNode.GetDisplayNode()<br>
dispNode.SetGlyphTypeFromString(‘Cross2D’)</p>
</blockquote>

---
