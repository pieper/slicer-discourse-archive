# Is there a Lasso tool in the Segment Editor module in Slicer?

**Topic ID**: 29383
**Date**: 2023-05-09
**URL**: https://discourse.slicer.org/t/is-there-a-lasso-tool-in-the-segment-editor-module-in-slicer/29383

---

## Post #1 by @Russell_Engelman (2023-05-09 18:38 UTC)

<p>I am currently segmenting a number of fossil and extant mammal specimens where I have to manually separate key ROIs from a threshholded volume due to insufficient differences in density between elements (example: separating upper and lower teeth in modern specimens scanned with their jaws closed).</p>
<p>I am used to segmenting in Avizo. One feature that has been very useful for me for separating segmented regions in Avizo is their lasso tool, which lets me draw a circle around the area I want to subtract from a layer. I was wondering if there was any way to do this with the Segment Editor module in Slicer?</p>
<p>The closest I have been able to find is the Scizzors function and the Eraser function. However, with Scizzors if I try to edit the model slice by slice the tool is applied to all slices along that axis, which means I cannot edit a single slice by itself. Eraser gets closer to what I am looking for but it only allows for a brush stroke, which does not give me the dexterity I need to separate the segmentation along its boundaries.</p>
<p>Is there any lasso function for segmentation in Slicer?</p>

---

## Post #2 by @lassoan (2023-05-09 18:42 UTC)

<p>You can set the slice thickness for Scissors tool (set thickness to 0 to limit it to the current slice). You can also use the Draw tool (if you draw another segment then it will be erased from the current segment). You can use masking settings to limit editing inside a selected segment (so that you only need to pay attention when you draw the contour inside the segment).</p>
<p>You may save time by segmenting manually on every 5th slice and then fill between using the “Fill between slices” effect.</p>

---

## Post #3 by @Russell_Engelman (2023-05-12 01:10 UTC)

<p>The slick thickness option works. Thank you.</p>
<p>For anyone new to Slicer reading this you have to go to the “slice cut” option and select “symmetric”, that is how to use scizzors by slice thickness.</p>

---

## Post #4 by @Russell_Engelman (2023-05-23 19:27 UTC)

<p>Is there a way to do the reverse of the Scizzors tool? Select a region of interest using a lasso-like tool and then add it to the materials of interest? This is necessary in my case to manually separate bones out into layers, manually segmenting the zones of articulation between bones and then using Magic Wand or something like it to move the different bones into their own materials.</p>

---

## Post #5 by @lassoan (2023-05-23 19:40 UTC)

<p>Yes, you can choose to fill/erase, inside/outside, and use masking settings to restrict editing to inside outside specific segments or image intensity range.</p>

---
