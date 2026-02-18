# Restraining from selecting more than one point

**Topic ID**: 20040
**Date**: 2021-10-06
**URL**: https://discourse.slicer.org/t/restraining-from-selecting-more-than-one-point/20040

---

## Post #1 by @Aamir_Khan (2021-10-06 20:13 UTC)

<p>Hi,</p>
<p>I have been developing a extension where I need to select multiple points and then based on an algorithm transforming the volume. For this purpose, I have used qSlicerSimpleMarkupsWidget() and qSlicerMarkupsPlaceWidget. The algorithm is working perfect. Except for the situation where the user starts selecting more than one point for the same name. This breaks the algorithm as the matrix condition is not satisfied.</p>
<p>I am attaching the code:</p>
<pre><code>    self.a = slicer.qSlicerSimpleMarkupsWidget()
    self.a.objectName = "a"
    self.a.toolTip = "Select a fiducial to use as the ASIS left point."
    self.a.setNodeBaseName("a")
    self.a.defaultNodeColor = qt.QColor(255, 255, 0)
    self.a.tableWidget().hide()
    self.a.markupsSelectorComboBox().noneEnabled = True
    self.a.markupsPlaceWidget().placeMultipleMarkups = (
        slicer.qSlicerMarkupsPlaceWidget.ForcePlaceSingleMarkup
    )
    self.a.markupsPlaceWidget().buttonsVisible = False
    self.a.markupsPlaceWidget().placeButton().show()
    self.a.setMRMLScene(slicer.mrmlScene)

    inputsFormLayout.addRow("a:", self.a)
    self.parent.connect("mrmlSceneChanged(vtkMRMLScene*)", self.a)

    self.b = slicer.qSlicerSimpleMarkupsWidget()
    self.b.objectName = "b"
    self.b.toolTip = "Select a fiducial to use as the ASIS right point."
    self.b.setNodeBaseName("b")
    self.b.defaultNodeColor = qt.QColor(255, 0, 0)
    self.b.tableWidget().hide()
    self.b.markupsSelectorComboBox().noneEnabled = True
    self.b.markupsPlaceWidget().placeMultipleMarkups = (
        slicer.qSlicerMarkupsPlaceWidget.ForcePlaceSingleMarkup
    )
    self.b.markupsPlaceWidget().buttonsVisible = False
    self.b.markupsPlaceWidget().placeButton().show()
    self.b.setMRMLScene(slicer.mrmlScene)

    inputsFormLayout.addRow("b:", self.b)

    self.parent.connect(
        "mrmlSceneChanged(vtkMRMLScene*)",
        self.b,
        "setMRMLScene(vtkMRMLScene*)",
    )
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18f0d903ff8e0cd767cb78f5536b0369549ade83.jpeg" data-download-href="/uploads/short-url/3yDtkLK3LaEIH7QMoatRI22SgPV.jpeg?dl=1" title="Capture.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18f0d903ff8e0cd767cb78f5536b0369549ade83_2_690x298.jpeg" alt="Capture.PNG" data-base62-sha1="3yDtkLK3LaEIH7QMoatRI22SgPV" width="690" height="298" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18f0d903ff8e0cd767cb78f5536b0369549ade83_2_690x298.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18f0d903ff8e0cd767cb78f5536b0369549ade83_2_1035x447.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18f0d903ff8e0cd767cb78f5536b0369549ade83_2_1380x596.jpeg 2x" data-dominant-color="B7B7BA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture.PNG</span><span class="informations">1879×814 219 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72a6e99cc54202a576c1ced2f04d17b5564c70b8.jpeg" data-download-href="/uploads/short-url/gmg2ucXCmTTddcb47kT4nw5Vfde.jpeg?dl=1" title="Capture2.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72a6e99cc54202a576c1ced2f04d17b5564c70b8_2_690x285.jpeg" alt="Capture2.PNG" data-base62-sha1="gmg2ucXCmTTddcb47kT4nw5Vfde" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72a6e99cc54202a576c1ced2f04d17b5564c70b8_2_690x285.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72a6e99cc54202a576c1ced2f04d17b5564c70b8_2_1035x427.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72a6e99cc54202a576c1ced2f04d17b5564c70b8_2_1380x570.jpeg 2x" data-dominant-color="B5B4B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2.PNG</span><span class="informations">1914×792 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>For example, here in capture the node a is selected once as shown in red window. but in capture2, we are again able to select the node a. For the algorithm to work properly, the module must restrict the user from selecting more than one node for the same name.</p>
<p>Please let me know if the question is clear from my side.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2021-10-07 05:30 UTC)

<p>In recent Slicer Preview Releases you can specify a template with predefined control point names and restrict the user to place only those points. Probably all you need is to create a markup fiducial node, add a control point to it (set its name, set its position status to <code>PositionUndefined</code>), and enable set the number of control points to fixed (<code>SetFixedNumberOfControlPoints(True)</code>).</p>
<p>We’ll improve the simple markups widget to work similarly as the point list in Markups module’s Control points section. Then you could just add a single markups fiducial node and use that point list widget to place all your points.</p>

---
