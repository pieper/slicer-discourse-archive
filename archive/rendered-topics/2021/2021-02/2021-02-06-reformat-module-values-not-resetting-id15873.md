# Reformat module Values not resetting

**Topic ID**: 15873
**Date**: 2021-02-06
**URL**: https://discourse.slicer.org/t/reformat-module-values-not-resetting/15873

---

## Post #1 by @manjula (2021-02-06 15:55 UTC)

<p>Hi,<br>
Why the values in reformat module do not reset by default? Even if I close the scene (Ctlr W) still the what ever the rotation values remain there in the next scene.</p>
<p>Also when I change the rotation value in red slice, and click the yellow slice the values i change in the red slice is what i get from default.</p>
<p>Is this expected?</p>
<p>I guess after closing the scene the sliders should reset at least.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83165bd808780e98d12039a15657faa8b9716e0e.png" data-download-href="/uploads/short-url/iHEs1J5wKDHDpdoK894gkcxDFJI.png?dl=1" title="Screenshot from 2021-02-06 16-51-50" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83165bd808780e98d12039a15657faa8b9716e0e_2_690x350.png" alt="Screenshot from 2021-02-06 16-51-50" data-base62-sha1="iHEs1J5wKDHDpdoK894gkcxDFJI" width="690" height="350" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83165bd808780e98d12039a15657faa8b9716e0e_2_690x350.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83165bd808780e98d12039a15657faa8b9716e0e_2_1035x525.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83165bd808780e98d12039a15657faa8b9716e0e_2_1380x700.png 2x" data-dominant-color="B0AFBF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-02-06 16-51-50</span><span class="informations">1501×762 87.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-02-06 17:22 UTC)

<p>The sliders are used only for relative rotations. See more details here: <a href="https://discourse.slicer.org/t/is-the-rotation-of-the-3d-slicers-transform-module-euler-or-quaternion/11944/2" class="inline-onebox">Is the rotation of the 3D Slicer's Transform module Euler or Quaternion? - #2 by lassoan</a></p>
<p>We should reset them to 0 more often to make sure users don’t mistake it for Euler angles or something similar.</p>
<p>Euler angles (and similar representations that rely on successive rotations along multiple axes) are not well suited for representing arbitrary orientations, as it suffers from gimbal lock and there are multiple parametrizations for the same orientation. Having multiple parametrizations for the same orientation means that conversion between Euler&lt;-&gt;matrix representations is not invertible, which means that in general it is not possible to create 3 independent sliders for specifying orientation using Euler angles.</p>
<p>Just to illustrate the problem, you can copy-paste the code snippet below to get orientation sliders that operate in Euler angles (YXZ order). Note how the angles are modified after you release the slider if any of the angles &gt;=90 deg (numerical instabilities may start to appear a few degrees before 90deg).</p>
<pre><code class="lang-python">transformNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode')
# transformNode = getNode('Transform')

### 

def updateTransformFromWidget(value):
    transform = vtk.vtkTransform()
    transform.RotateZ(axisSliderWidgets[2].value)
    transform.RotateX(axisSliderWidgets[0].value)
    transform.RotateY(axisSliderWidgets[1].value)
    transformNode.SetMatrixTransformToParent(transform.GetMatrix())

def updateWidgetFromTransform(caller, event):
    transformMatrix = transformNode.GetMatrixTransformToParent()
    transform = vtk.vtkTransform()
    transform.SetMatrix(transformMatrix)
    orientation = transform.GetOrientation()
    for i in range(3):
        axisSliderWidget = axisSliderWidgets[i]
        wasBlocked = axisSliderWidget.blockSignals(True)
        axisSliderWidget.value = orientation[i]
        axisSliderWidget.blockSignals(wasBlocked)

def resetTransform():
    transformNode.SetMatrixTransformToParent(vtk.vtkMatrix4x4())

# Create widget

widget = qt.QFrame()
layout = qt.QFormLayout()
widget.setLayout(layout)
axisSliderWidgets = []
for i in range(3):
    axisSliderWidget = ctk.ctkSliderWidget()
    axisSliderWidget.singleStep = 1.0
    axisSliderWidget.minimum = -180
    axisSliderWidget.maximum = 180
    axisSliderWidget.value = 0
    axisSliderWidget.tracking = False
    layout.addRow(f"Axis {i+1}: ", axisSliderWidget)
    axisSliderWidgets.append(axisSliderWidget)
    axisSliderWidget.connect("valueChanged(double)", updateTransformFromWidget)

resetButton = qt.QPushButton("Reset")
layout.addWidget(resetButton)
resetButton.connect("clicked()", resetTransform)

widget.show()

transformObserver = transformNode.AddObserver(slicer.vtkMRMLTransformableNode.TransformModifiedEvent, updateWidgetFromTransform)

# transformNode.RemoveObserver(transformObserver)
</code></pre>

---
