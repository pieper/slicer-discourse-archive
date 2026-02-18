# Volume reslice driver crashes Slicer

**Topic ID**: 7265
**Date**: 2019-06-20
**URL**: https://discourse.slicer.org/t/volume-reslice-driver-crashes-slicer/7265

---

## Post #1 by @zapaishchykova (2019-06-20 18:09 UTC)

<p>Hi there!<br>
I’m trying to use Volume reslice driver from python script ( since from console it works fine):</p>
<pre><code>  def onTransformImageClicked(self):
    logic = ModuleLogic()
    result = logic.transformationImage()
    driver = slicer.vtkSlicerVolumeResliceDriverLogic()  # .MODE_TRANSVERSE = 6
    layoutManager = slicer.app.layoutManager()
    redView = layoutManager.layoutLogic().GetViewNodes().GetItemAsObject(0)
    driver.SetModeForSlice(6, redView)
    driver.SetDriverForSlice('vtkMRMLScalarVolumeNode1', redView)

    qt.QMessageBox.information(slicer.util.mainWindow(), 'Slicer Python', result)
</code></pre>
<p>And It just crashes without any error. I want to change following params (see image)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e13d01fb1a67d630eb046a34895df6d8a9c4ffb5.png" data-download-href="/uploads/short-url/w8y8DznQ2ccOLsdpSaQ9oM0fq5f.png?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e13d01fb1a67d630eb046a34895df6d8a9c4ffb5.png" alt="3" data-base62-sha1="w8y8DznQ2ccOLsdpSaQ9oM0fq5f" width="690" height="288" data-dominant-color="F0EBDE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">826×345 6.18 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Any ideas what is wrong here?</p>

---

## Post #2 by @zapaishchykova (2019-06-20 18:23 UTC)

<p>Just figured it out, forgot to set scene before, now it doesn’t crush anymore. But still, small error will be nicer than a crash:)</p>
<pre><code>    driver = slicer.vtkSlicerVolumeResliceDriverLogic()  # .MODE_TRANSVERSE = 6
    layoutManager = slicer.app.layoutManager()
    redView = layoutManager.layoutLogic().GetViewNodes().GetItemAsObject(0)
    driver.SetMRMLScene(slicer.mrmlScene) 
    driver.SetModeForSlice(6, redView)
    driver.SetDriverForSlice('vtkMRMLScalarVolumeNode1', redView)</code></pre>

---

## Post #3 by @lassoan (2019-06-20 18:42 UTC)

<p>For loadable modules, module logic is instantiated by the application and there should be only one instance. So, instead of creating a new module logic, use the existing one:</p>
<pre><code>driver = slicer.modules.volumereslicedriver.logic()</code></pre>

---
