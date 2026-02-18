# Why fontSize of vtkTextActor() not working as setup-values (via Python)?

**Topic ID**: 15901
**Date**: 2021-02-08
**URL**: https://discourse.slicer.org/t/why-fontsize-of-vtktextactor-not-working-as-setup-values-via-python/15901

---

## Post #1 by @aiden.zhu (2021-02-08 16:57 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11.0-2019-06-23 r28335<br>
Expected behavior:  font-size adjustment<br>
Actual behavior: X</p>
<p>Hi All, I tried to use vtk.vtkTextActor() to set up a text-info in a window as in the following code, but The fontsize did not change as expected, instead it showed as the original size (12). Why? Thanks a lot in advance!</p>
<pre><code class="lang-python">lm = slicer.app.layoutManager()
layout = lm 
import os 
redRenderer = layout.sliceWidget('Red').sliceView().renderWindow().GetRenderers().GetFirstRenderer()
redRenderWindow =  redRenderer.GetRenderWindow()
redRenderWindow.Render()
vn_red = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed')
slicer.app.layoutManager().layout = 6
sliceLogic = lm.sliceWidget(vn_red.GetLayoutName()).sliceLogic()
originalSliceOffset = sliceLogic.GetSliceOffset()
interactor =  redRenderWindow.GetInteractor()
text = vtk.vtkTextActor()
text.SetInput('Testing Info Text')
textProperty = text.GetTextProperty()
print('Before changing = ', textProperty.GetFontSize())
fontsize_text = 60
textProperty.SetFontSize(fontsize_text)
print('After Changing = ', textProperty.GetFontSize())
textProperty.SetColor(1, 1, 0)
textProperty.SetBold(1)
text_representation = vtk.vtkTextRepresentation()
text_representation.GetPositionCoordinate().SetValue( 0.025, 0.92850     )
text_widget = vtk.vtkTextWidget(); 
text_widget.SetRepresentation(text_representation)
text_widget.SetInteractor(interactor); 
text_widget.SetTextActor(text);text_widget.SelectableOff()
text_widget.EnabledOn(); text_widget.On()
slicer.app.processEvents()
</code></pre>
<p>Aiden</p>

---

## Post #2 by @lassoan (2021-02-08 21:01 UTC)

<p>If you put your text actor into a vtkTextWidget then the text widget will take care of the font size. You can make the text bigger by clicking the edge or corner of the textbox and drag it to make it larger.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07653011603e057df96105d05e79ee154c25b6ba.jpeg" data-download-href="/uploads/short-url/13q8r5HlO9dZNhdzZ9Zr9adARjs.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07653011603e057df96105d05e79ee154c25b6ba_2_690x449.jpeg" alt="image" data-base62-sha1="13q8r5HlO9dZNhdzZ9Zr9adARjs" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07653011603e057df96105d05e79ee154c25b6ba_2_690x449.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07653011603e057df96105d05e79ee154c25b6ba.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07653011603e057df96105d05e79ee154c25b6ba.jpeg 2x" data-dominant-color="3F3F34"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">866×564 72.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @aiden.zhu (2021-02-17 20:12 UTC)

<p>Thanks,  Andras.<br>
I know that dragging works there. What I would expect is that I would like to control it by user-GUI to adjust/input a number as needed.</p>

---

## Post #4 by @lassoan (2021-02-17 20:20 UTC)

<p>The text actor does now know that it is embedded in a text widget, so if you want to modify the text size then you have to do it in the widget. Maybe simply calling <a href="https://vtk.org/doc/nightly/html/classvtkBorderWidget.html#aec722ff199d9ef7db3ee580f37e1db81">ResizableOff</a> on the widget is sufficient, but if not then you need to check out the implementation and maybe you’ll have to add a two-way synchronization mechanism between the widget and the actor.</p>
<p>Why do you need a custom widget? You can use markups fiducials to display labels in slice and 3D views.</p>

---
