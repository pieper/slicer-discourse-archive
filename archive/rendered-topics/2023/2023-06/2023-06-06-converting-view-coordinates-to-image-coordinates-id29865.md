---
topic_id: 29865
title: "Converting View Coordinates To Image Coordinates"
date: 2023-06-06
url: https://discourse.slicer.org/t/29865
---

# Converting view coordinates to image coordinates

**Topic ID**: 29865
**Date**: 2023-06-06
**URL**: https://discourse.slicer.org/t/converting-view-coordinates-to-image-coordinates/29865

---

## Post #1 by @asyeda (2023-06-06 15:15 UTC)

<p>I am writing a custom scripted loadable module where one of the features lets the user click on a button, then click &amp; drag to select a region of interest for further analysis. I have written MouseEvents like so:</p>
<pre><code class="lang-auto">class MyModuleWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
	"""
 	Uses ScriptedLoadableModuleWidget base class, available at:
	https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
	"""

	def __init__(self, parent=None):
        ...

    def setup(self):
        ...
        self.ui.myButton.connect("clicked(bool)", self.onButtonClick)
        ...

    def onButtonClick(self):
		sliceWidget = slicer.app.layoutManager().sliceWidget("Red")
		renderWindowInteractor = sliceWidget.sliceView().renderWindow().GetInteractor()
		self.leftButtonPressObserverID = renderWindowInteractor.AddObserver(vtk.vtkCommand.LeftButtonPressEvent, self.onLeftButtonPress)
		self.leftButtonReleaseObserverID = renderWindowInteractor.AddObserver(vtk.vtkCommand.LeftButtonReleaseEvent, self.onLeftButtonRelease)

	def onLeftButtonPress(self, obj, event):
		interactor = obj
		eventPosition = interactor.GetEventPosition()
		if event == "LeftButtonPressEvent":
			self.startPos = eventPosition

	def onLeftButtonRelease(self, obj, event):
		interactor = obj
		eventPosition = interactor.GetEventPosition()

		if event == "LeftButtonReleaseEvent":
			self.endPos = eventPosition

			# Perform analysis on the selected region
			if self.startPos and self.endPos:
				# TODO: convert to image coordinates and perform analysis

			# Reset the start and end positions
			self.startPos = None
			self.endPos = None

			# Remove the observers
			sliceWidget = slicer.app.layoutManager().sliceWidget("Red")
			renderWindowInteractor = sliceWidget.sliceView().renderWindow().GetInteractor()
			renderWindowInteractor.RemoveObserver(self.leftButtonPressObserverID)
			renderWindowInteractor.RemoveObserver(self.leftButtonReleaseObserverID)
</code></pre>
<p>The start and end positions are being correctly captured. However, the coordinates are not image coordinates, but view coordinates, i.e. selecting the top corner of the image should be, for example:</p>
<pre><code class="lang-auto">startPos = (0, 0)
endPos = (30, 30)
</code></pre>
<p>But if I select this region, the coordinates might instead be set to:</p>
<pre><code class="lang-auto">startPos = (30, 30)
endPos = (60, 60)
</code></pre>
<p>How can I convert these view coordinates to image coordinates?</p>

---

## Post #2 by @lassoan (2023-06-06 23:23 UTC)

<p>You can look into implementation of segment editor effects that take mouse clicks as inputs. However, I would recommend to use a markups plane or ROI for selecting a region.</p>

---

## Post #3 by @asyeda (2023-06-08 01:26 UTC)

<p>I see, is there a way to implement it so that the user selects the ROI after clicking the button, and that ROI is used for further analysis? Something like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e382db0980bb11682e2cf03e8a603b94d117371.gif" alt="Slicer question" data-base62-sha1="4jkGwLoJwAbXcvJGZ1fPe9ESZZ7" width="600" height="327" class="animated"></p>

---
