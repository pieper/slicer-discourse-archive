# Error in segment statistics

**Topic ID**: 40283
**Date**: 2024-11-20
**URL**: https://discourse.slicer.org/t/error-in-segment-statistics/40283

---

## Post #1 by @Vikram (2024-11-20 03:07 UTC)

<p>I want to calculate volume of segemented region,but when i use statics tool , i did not see segemted region to apply , i also paste code here</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b57a6b0aeffde244eebf569073cc76189368946.png" data-download-href="/uploads/short-url/aKvBjYyM6YhWYxH2kOGfAahrbQa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b57a6b0aeffde244eebf569073cc76189368946_2_690x345.png" alt="image" data-base62-sha1="aKvBjYyM6YhWYxH2kOGfAahrbQa" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b57a6b0aeffde244eebf569073cc76189368946_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b57a6b0aeffde244eebf569073cc76189368946_2_1035x517.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b57a6b0aeffde244eebf569073cc76189368946_2_1380x690.png 2x" data-dominant-color="B9B8B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1851×928 268 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
[VTK] There is more than one file, use the vtkITKArchetypeImageSeriesReader instead<br>
[ITK] WARNING: In D:\D\S\S-0-build\ITK\Modules\IO\ImageBase\include\itkImageSeriesReader.hxx, line 478<br>
[ITK] ImageSeriesReader (000002A2C0B42FB0): Non uniform sampling or missing slices detected,  maximum nonuniformity:40.2112<br>
[Qt] QWindowsWindow::setGeometry: Unable to set geometry 1920x1254+0+34 (frame: 1942x1310-11-11) on QWidgetWindow/“qSlicerMainWindowWindow” on “\.\DISPLAY1”. Resulting geometry: 1920x974+0+34 (frame: 1942x1030-11-11) margins: 11, 45, 11, 11 minimum size: 952x627 MINMAXINFO maxSize=0,0 maxpos=0,0 mintrack=1926,1310 maxtrack=0,0)<br>
[Qt] QWindowsWindow::setGeometry: Unable to set geometry 1920x1378+0+34 (frame: 1942x1434-11-11) on QWidgetWindow/“qSlicerMainWindowWindow” on “\.\DISPLAY1”. Resulting geometry: 1920x974+0+34 (frame: 1942x1030-11-11) margins: 11, 45, 11, 11 minimum size: 952x689 MINMAXINFO maxSize=0,0 maxpos=0,0 mintrack=1926,1434 maxtrack=0,0)<br>
[Qt] QWindowsWindow::setGeometry: Unable to set geometry 2138x1378+0+34 (frame: 2160x1434-11-11) on QWidgetWindow/“qSlicerMainWindowWindow” on “\.\DISPLAY1”. Resulting geometry: 1920x974+0+34 (frame: 1942x1030-11-11) margins: 11, 45, 11, 11 minimum size: 1069x689 MINMAXINFO maxSize=0,0 maxpos=0,0 mintrack=2160,1434 maxtrack=0,0)<br>
[Qt] QWindowsWindow::setGeometry: Unable to set geometry 2138x1410+0+34 (frame: 2160x1466-11-11) on QWidgetWindow/“qSlicerMainWindowWindow” on “\.\DISPLAY1”. Resulting geometry: 1920x974+0+34 (frame: 1942x1030-11-11) margins: 11, 45, 11, 11 minimum size: 1069x705 MINMAXINFO maxSize=0,0 maxpos=0,0 mintrack=2160,1466 maxtrack=0,0)<br>
[Qt] QWindowsWindow::setGeometry: Unable to set geometry 2138x1456+0+34 (frame: 2160x1512-11-11) on QWidgetWindow/“qSlicerMainWindowWindow” on “\.\DISPLAY1”. Resulting geometry: 1920x974+0+34 (frame: 1942x1030-11-11) margins: 11, 45, 11, 11 minimum size: 1069x728 MINMAXINFO maxSize=0,0 maxpos=0,0 mintrack=2160,1512 maxtrack=0,0)<br>
Traceback (most recent call last):<br>
File “C:\Users\PPBD_test\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SegmentStatistics.py”, line 58, in setup<br>
self.logic = SegmentStatisticsLogic()<br>
File “C:\Users\PPBD_test\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SegmentStatistics.py”, line 394, in <strong>init</strong><br>
self.reset()<br>
File “C:\Users\PPBD_test\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SegmentStatistics.py”, line 430, in reset<br>
params = self.getParameterNode()<br>
File “C:\Users\PPBD_test\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SegmentStatistics.py”, line 399, in getParameterNode<br>
self.setParameterNode(ScriptedLoadableModuleLogic.getParameterNode(self))<br>
File “C:\Users\PPBD_test\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SegmentStatistics.py”, line 409, in setParameterNode<br>
plugin.setParameterNode(parameterNode)<br>
File “C:\Users\PPBD_test\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SegmentStatisticsPlugins\SegmentStatisticsPluginBase.py”, line 124, in setParameterNode<br>
self.createDefaultOptionsWidget()<br>
File “C:\Users\PPBD_test\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SegmentStatisticsPlugins\SegmentStatisticsPluginBase.py”, line 164, in createDefaultOptionsWidget<br>
info = self.getMeasurementInfo(key)<br>
File “C:\Users\PPBD_test\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\PET-IndiC\lib\Slicer-5.6\qt-scripted-modules\PETVolumeSegmentStatisticsPlugin\PETVolumeSegmentStatisticsPlugin.py”, line 106, in getMeasurementInfo<br>
self.createMeasurementInfo(name=“Mean”, description=“Mean uptake value”,<br>
TypeError: createMeasurementInfo() missing 1 required positional argument: ‘title’<br>
Traceback (most recent call last):<br>
File “C:\Users\PPBD_test\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SegmentStatistics.py”, line 170, in enter<br>
if self.parameterNodeSelector.currentNode() is None:<br>
AttributeError: ‘SegmentStatisticsWidget’ object has no attribute ‘parameterNodeSelector’</p>

---

## Post #2 by @muratmaga (2024-11-20 03:18 UTC)

<p>Before you go any further, you should look into why there is this error:</p>
<pre><code class="lang-auto">[ITK] WARNING: In D:\D\S\S-0-build\ITK\Modules\IO\ImageBase\include\itkImageSeriesReader.hxx, line 478
[ITK] ImageSeriesReader (000002A2C0B42FB0): Non uniform sampling or missing slices detected, maximum nonuniformity:40.2112
</code></pre>

---

## Post #3 by @Vikram (2024-11-20 03:39 UTC)

<p>I don’t know why error occurred, can you please help me how i can resolve this issue?</p>

---
