# Translating of a line

**Topic ID**: 32001
**Date**: 2023-10-03
**URL**: https://discourse.slicer.org/t/translating-of-a-line/32001

---

## Post #1 by @Grigoriy_Postolskiy (2023-10-03 01:48 UTC)

<p>Hello!  I assigned the function of moving a line to the left mouse button. But as a result, the function of moving of individual points of the line stopped working.</p>
<p>How can I make it so that when you hover the mouse over the line itself and hold down the left mouse button, the entire line is translated, and when you hover the cursor over a separate point of the line and hold down the left mouse button, only this point of the line begins to translate?</p>
<p>This is my code for translating a line by left mouse button pressing:</p>
<pre><code class="lang-auto">sliceViewLabel = "Red"
sliceViewWidget = slicer.app.layoutManager().sliceWidget(sliceViewLabel)
displayableManager = sliceViewWidget.sliceView().displayableManagerByClassName(
  "vtkMRMLMarkupsDisplayableManager"
)
line = slicer.util.getNode('L')
lineDisplayNode = line.GetDisplayNode()
widget = displayableManager.GetWidget(lineDisplayNode)

widget.SetEventTranslationClickAndDrag(
  widget.WidgetStateOnWidget,
  vtk.vtkCommand.LeftButtonPressEvent,
  vtk.vtkEvent.NoModifier,
  widget.WidgetStateTranslate,
  vtk.vtkWidgetEvent.NoEvent,
  vtk.vtkWidgetEvent.NoEvent
)

widget.SetEventTranslationClickAndDrag(
  widget.WidgetStateOnWidget,
  vtk.vtkCommand.LeftButtonPressEvent,
  vtk.vtkEvent.NoModifier,
  widget.WidgetStateTranslate,
  widget.WidgetEventTranslateStart,
  widget.WidgetEventTranslateEnd
)
</code></pre>

---

## Post #2 by @jamesobutler (2023-10-03 03:47 UTC)

<p>As part of improving functionality for the Slicer community, have you found that the existing events for a Markups line node not sufficient?</p>
<ul>
<li>Mouse wheel click on line to translate entire line</li>
<li>Left click on control point to translate single point</li>
</ul>

---

## Post #3 by @Grigoriy_Postolskiy (2023-10-03 10:38 UTC)

<p>I am making the application for doctors who do not have much professionalism in using a computer and it will be difficult for them to understand that the transfer of the entire line is assigned to the middle mouse button.</p>

---

## Post #4 by @chir.set (2023-10-03 10:48 UTC)

<aside class="quote no-group" data-username="Grigoriy_Postolskiy" data-post="3" data-topic="32001">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/grigoriy_postolskiy/48/15587_2.png" class="avatar"> Grigoriy_Postolskiy:</div>
<blockquote>
<p>doctors who do not have much professionalism in using a computer</p>
</blockquote>
</aside>
<p>I wish to contribute these lines as a surgeon.</p>
<p>When your doctors have finished with your simplification, they would ask you for more simplifications. You will be caught up in an endless whirlwind, reinventing the wheel every time. I think IT pros and developers should rather show doctors how to use computers and software as they are. Lest in 50 years, doctors (in general) would remain at the same level of unfortunately ‘below base’ skill.</p>

---

## Post #5 by @Grigoriy_Postolskiy (2023-10-03 12:59 UTC)

<p>The recording of the problem is below - the entire line translating works by left mouse button pressing, but the point translating stopped working.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d53c90ca89394a1a7d118cdbe6c3bee5181d748.gif" alt="Animation" data-base62-sha1="b24h1cThlsoMWu04cgPZTtbhWaI" width="690" height="471" class="animated"></p>

---
