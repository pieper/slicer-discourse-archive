# how to response vtkButtonWidget?such as LeftButtonPressEvent

**Topic ID**: 8937
**Date**: 2019-10-29
**URL**: https://discourse.slicer.org/t/how-to-response-vtkbuttonwidget-such-as-leftbuttonpressevent/8937

---

## Post #1 by @pingdan (2019-10-29 11:47 UTC)

<p>I created a vtkButtonWidget and want to do some work when I click the buttonwidget with the left button of mouse, so I add a observer to the buttonwidget, but when I click ,it has no action. what is wrong with the codes?</p>
<p>class vtkButtonCallback : public vtkCommand<br>
{<br>
public:<br>
static vtkButtonCallback *New()<br>
{<br>
return new vtkButtonCallback;<br>
}<br>
virtual void Execute(vtkObject <em>caller, unsigned long, void</em>)<br>
{<br>
if (ev == vtkCommand::LeftButtonPressEvent)<br>
{<br>
return;<br>
}<br>
}<br>
};</p>
<pre><code>// Create the widget and its representation
vtkSmartPointer&lt;vtkTexturedButtonRepresentation2D&gt; buttonRepresentation =
	vtkSmartPointer&lt;vtkTexturedButtonRepresentation2D&gt;::New();
buttonRepresentation-&gt;SetNumberOfStates(1);
buttonRepresentation-&gt;SetButtonTexture(0, image1);

vtkSmartPointer&lt;vtkButtonWidget&gt; buttonWidget =
	vtkSmartPointer&lt;vtkButtonWidget&gt;::New();
buttonWidget-&gt;SetInteractor(renderWindowInteractor);
buttonWidget-&gt;SetRepresentation(buttonRepresentation);

vtkButtonCallback *myBtnCallback = vtkButtonCallback::New();
buttonWidget-&gt;AddObserver(vtkCommand::LeftButtonPressEvent, myBtnCallback);</code></pre>

---

## Post #2 by @lassoan (2019-10-29 12:20 UTC)

<p>We have tried to use VTK widgets in Slicer but there they had so many problems and limitations that we gave up on them.</p>
<p>I would recommend to add custom buttons in the view controller bars:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_widgets_in_view_controller_bars" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_widgets_in_view_controller_bars</a></p>

---
