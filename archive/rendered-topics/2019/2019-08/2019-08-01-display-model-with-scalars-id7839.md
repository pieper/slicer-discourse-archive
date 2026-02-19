---
topic_id: 7839
title: "Display Model With Scalars"
date: 2019-08-01
url: https://discourse.slicer.org/t/7839
---

# Display model with scalars

**Topic ID**: 7839
**Date**: 2019-08-01
**URL**: https://discourse.slicer.org/t/display-model-with-scalars/7839

---

## Post #1 by @Hamburgerfinger (2019-08-01 17:15 UTC)

<p>I have a model created with Slicer’s ‘Probe volume with model’.  I can display the scalars, and edit the color table, etc., but I can only edit the scalar range up to the maximum (but not exceeding it).</p>
<p>I want to make the maximum value (red in the currently displayed surface) appear yellow.  Why can I not arbitrarily set the maximum value of the color table?</p>
<p>THanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bde5cbeaaf119a098978b1c89fd3334b0b35bdce.jpeg" data-download-href="/uploads/short-url/r5UzSIOSXRNru6877nAwx2DhUVU.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bde5cbeaaf119a098978b1c89fd3334b0b35bdce_2_690x446.jpeg" alt="PNG" data-base62-sha1="r5UzSIOSXRNru6877nAwx2DhUVU" width="690" height="446" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bde5cbeaaf119a098978b1c89fd3334b0b35bdce_2_690x446.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bde5cbeaaf119a098978b1c89fd3334b0b35bdce_2_1035x669.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bde5cbeaaf119a098978b1c89fd3334b0b35bdce_2_1380x892.jpeg 2x" data-dominant-color="344B96"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">3037×1965 793 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-08-01 21:51 UTC)

<p>Manual range setting is limited to the model’s scalar range by default but you can change it by clicking on the triple-dot button right next to it.</p>

---

## Post #3 by @Hamburgerfinger (2019-08-02 14:53 UTC)

<p>I can click the triple dot button and manually enter the intensity range I want, but it doesn’t properly update the range, and when I readjust it with the slider it resets the range I entered manually.</p>
<p>Can I send a video capture?</p>
<p>I’m using Slicer 4.11.0-2019-6-24.</p>

---

## Post #4 by @lassoan (2019-08-02 15:45 UTC)

<p>Indeed, there is a glitch that if you change the displayed range values then the maximum range is automatically reset. We’ll fix this, but in the meantime you should still achieve what you need.</p>
<p>There are two main use cases, and both should work well:</p>
<ul>
<li>A. Shared scalar range: when you want to use the same color mapping across several models. Set “Scalar range mode” to “Color table (LUT)” and set range in Colors module.</li>
<li>B. Set color mapping to an individual segment: When you just want to colorize a model, you can choose an existing color map and tune what range is emphasized (for this you don’t need to set values outside the scalar range of the volume). Or, if you want specific values to have specific colors then edit the colormap using Colors module (for example, make a copy of PET-Heat color table and edit the colors).</li>
</ul>
<p>If you want to create a sparse color table with randomly distributed colors then you can write a few lines of Python script for that:</p>
<pre><code class="lang-python">colorTableNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLProceduralColorNode", "MyColors")
colorTableNode.SetType(slicer.vtkMRMLColorTableNode.User)
colorTransferFunction = vtk.vtkDiscretizableColorTransferFunction()
colorTransferFunction.AddRGBPoint(-1000.0, 1.0, 0.0, 0.0)
colorTransferFunction.AddRGBPoint(0.0, 0.0, 1.0, 0.0)
colorTransferFunction.AddRGBPoint(500.0, 0.6, 0.0, 1.0)
colorTransferFunction.AddRGBPoint(1500.0, 1.0, 1.0, 1.0)
colorTableNode.SetAndObserveColorTransferFunction(colorTransferFunction) 
</code></pre>

---

## Post #5 by @lassoan (2019-08-02 16:46 UTC)

<p>Slider range reset is now fixed in r28421. Will be available in tomorrow’s Preview Release.</p>

---

## Post #6 by @brhoom (2020-06-16 17:49 UTC)

<p>A related question, I tried the above code but the color of the model does not change and it is still gray</p>
<pre><code>    colorTableNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLProceduralColorNode", "MyColors")
    colorTableNode.SetType(slicer.vtkMRMLColorTableNode.User)
    colorTransferFunction = vtk.vtkDiscretizableColorTransferFunction()
    colorTransferFunction.AddRGBPoint(-1000.0, 1.0, 0.0, 0.0)
    colorTransferFunction.AddRGBPoint(0.0, 0.0, 1.0, 0.0)
    colorTransferFunction.AddRGBPoint(500.0, 0.6, 0.0, 1.0)
    colorTransferFunction.AddRGBPoint(1500.0, 1.0, 1.0, 1.0)
    colorTableNode.SetAndObserveColorTransferFunction(colorTransferFunction) 
    modelNode.GetDisplayNode().SetAndObserveColorNodeID(colorTableNode.GetID())
</code></pre>
<p>What I am missing?</p>

---

## Post #7 by @lassoan (2020-06-16 18:18 UTC)

<p>This code snippet just sets a color look-up table. You also need to select an active scalar and enable scalar display, as shown in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Select_cells_of_a_model_using_markups_fiducial_points">this example</a>.</p>

---

## Post #8 by @brhoom (2020-06-16 18:34 UTC)

<p>Thanks, it seems to work (I only see one color)</p>
<pre><code>    colorTableNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLProceduralColorNode", "MyColors")
    colorTableNode.SetType(slicer.vtkMRMLColorTableNode.User)
    colorTransferFunction = vtk.vtkDiscretizableColorTransferFunction()
    colorTransferFunction.AddRGBPoint(-1000.0, 1.0, 0.0, 0.0)
    colorTransferFunction.AddRGBPoint(0.0, 0.0, 1.0, 0.0)
    colorTransferFunction.AddRGBPoint(500.0, 0.6, 0.0, 1.0)
    colorTransferFunction.AddRGBPoint(1500.0, 1.0, 1.0, 1.0)
    colorTableNode.SetAndObserveColorTransferFunction(colorTransferFunction) 
    cellScalars = modelNode.GetMesh().GetCellData()
    selectionArray = cellScalars.GetArray('selection')
    if not selectionArray:
        selectionArray = vtk.vtkIntArray()
        selectionArray.SetName('selection')
        selectionArray.SetNumberOfValues(modelNode.GetMesh().GetNumberOfCells())
        selectionArray.Fill(0)
        cellScalars.AddArray(selectionArray)
    # Set up coloring by selection array
    modelNode.GetDisplayNode().SetActiveScalar("selection", vtk.vtkAssignAttribute.CELL_DATA)
    modelNode.GetDisplayNode().SetAndObserveColorNodeID(colorTableNode.GetID())
    modelNode.GetDisplayNode().SetScalarVisibility(True)</code></pre>

---

## Post #9 by @mau_igna_06 (2024-01-15 20:53 UTC)

<p>How to set RGB colors to the modelNode according to its surface normals, for example: RBGColor = RAS_To_RGBMatrix * normalVector</p>
<p>And see with the 3D camera something that looks like like when you define a 2D normals texture (but only on the 3D model’s surface):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e240d11e92dd74ac424e8a7d7f53f393a392834.jpeg" alt="Screenshot from 2024-01-15 17-41-04" data-base62-sha1="khr2t73IiQQJh4fXr8MbdVraoEA" width="463" height="456"></p>

---

## Post #10 by @mau_igna_06 (2024-01-19 21:29 UTC)

<p>Would that be possible to implement? Would someone like this coloring according to normals as a new feature?</p>

---
