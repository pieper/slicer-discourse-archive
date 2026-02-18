# Add a colormap table to Slicer

**Topic ID**: 877
**Date**: 2017-08-15
**URL**: https://discourse.slicer.org/t/add-a-colormap-table-to-slicer/877

---

## Post #1 by @jonieva (2017-08-15 21:22 UTC)

<p>Hi!</p>
<p>We would need to use a colormap node that would be used in many of our Slicer scripted modules and also CLIs.</p>
<p>Is it ok if I just add the file to the <a href="https://github.com/Slicer/Slicer/tree/master/Base/Logic/Resources/ColorFiles" rel="nofollow noopener">https://github.com/Slicer/Slicer/tree/master/Base/Logic/Resources/ColorFiles</a> folder and someone integrates the changes in the core?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2017-08-15 21:53 UTC)

<p>We plan to change how color map nodes are stored in Slicer to avoid keeping 100+ unused nodes in the scene (see <a href="https://issues.slicer.org/view.php?id=3955">https://issues.slicer.org/view.php?id=3955</a>). So, it is better not to add any further color nodes, especially not application-specific ones to the current color module.</p>
<p>It would be better (more robust and future-proof) to add a Get…() method to one of the module logic classes in your extension that would add the color node to the scene (if not present already) and return a pointer to it. You may even add it when your module is initialized, but in general it is preferable to add nodes to a scene when they are actually needed.</p>

---

## Post #3 by @jonieva (2017-08-15 22:17 UTC)

<p>That works in modules, but as I said, the same thing applies to dozens of our CLIs. How would you manage to assign a custom colormap node to a labelmap node that is a CLI output?</p>

---

## Post #4 by @lassoan (2017-08-15 22:41 UTC)

<p>I think you can create colormap nodes using mini-scenes, but it is probably simpler to add your custom color nodes in one of your module logic’s initialization method.</p>

---

## Post #5 by @lassoan (2017-08-16 04:04 UTC)

<p>Some more information that you may find helpful:</p>
<p>There are many issues with current default labelmaps. I just referred to one ticket above, but there are a couple of more, related to problems due to having many nodes in the scene, requirement of all color nodes must be hidden, difficulty with sharing color nodes that have the same range, showing color bars in 2D/3D views with absolute range, etc. Due to these issues, eventually the design of these default color tables will be refactored, so I would recommend to only use them for defining qualitative color gradients, and add custom color nodes for anything more complicated. Those recently added perceptually uniform colormaps fell into this category of being some nice color gradients for visualization, and they were completely generic, so it made sense to add to the core, but in general we should avoid adding more color maps to the core.</p>
<p>Therefore, the proposed solution:</p>
<p><strong>Short term:</strong> Since the introduction of extension infrastructure, there is no reason to pollute the Slicer scene with application/extension-specific color maps. Extension-specific color maps can be very easily added to the scene in the extension that needs those - as it is already done in several extensions. Examples for the two main approaches:</p>
<ol>
<li>
<p>Adding color map on-demand with Get…() method:<br>
<a href="https://github.com/QIICR/LongitudinalPETCT/blob/41438ecfafd9470a6dc4d16940256b8005bb9fe4/Logic/vtkSlicerLongitudinalPETCTLogic.cxx#L239-L279">https://github.com/QIICR/LongitudinalPETCT/blob/41438ecfafd9470a6dc4d16940256b8005bb9fe4/Logic/vtkSlicerLongitudinalPETCTLogic.cxx#L239-L279</a><br>
Pro: does not pollute the scene with potentially unused nodes. Con: may be more complicated with CLIs.</p>
</li>
<li>
<p>Example for adding color map in the module logic on initialization:<br>
<a href="https://app.assembla.com/spaces/slicerrt/subversion/source/HEAD/trunk/SlicerRt/src/Isodose/Logic/vtkSlicerIsodoseModuleLogic.cxx#ln108">https://app.assembla.com/spaces/slicerrt/subversion/source/HEAD/trunk/SlicerRt/src/Isodose/Logic/vtkSlicerIsodoseModuleLogic.cxx#ln108</a></p>
</li>
</ol>
<p><strong>Long term:</strong> CIP should use standard terminologies instead of relying on LUTs for labeling structures to make it easier and safer to import, process, and store results in a standard, structured way. Segmentation nodes already associate a standard DICOM coded entry with each segment, Segment Statistics module can compute metrics, results can be exported to/imported from DICOM. Segmentations are not yet supported by CLIs because we always had more important things to do, but if you can spend some time with working on it, then it would happen sooner. Just let us know if you are interested and start the discussion.</p>

---
