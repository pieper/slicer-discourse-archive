---
topic_id: 4343
title: "Use Progress Bar From Python"
date: 2018-10-10
url: https://discourse.slicer.org/t/4343
---

# Use progress bar from python

**Topic ID**: 4343
**Date**: 2018-10-10
**URL**: https://discourse.slicer.org/t/use-progress-bar-from-python/4343

---

## Post #1 by @Niels (2018-10-10 12:39 UTC)

<p>The python code in my logic class can take some time to finish its calculations. I would like to add a progress bar in the UI. Is there any way to work with a progressbar info from python?</p>

---

## Post #2 by @cpinter (2018-10-10 13:37 UTC)

<p>You can use this convenience function for that<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L1136" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L1136" target="_blank">Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L1136</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="1126" style="counter-reset: li-counter 1125 ;">
<li>    setattr(mbox, key, value)</li>
<li># Windows 10 peek feature in taskbar shows all hidden but not destroyed windows</li>
<li># (after creating and closing a messagebox, hovering over the mouse on Slicer icon, moving up the</li>
<li># mouse to the peek thumbnail would show it again).</li>
<li># Popup windows in other Qt applications often show closed popups (such as</li>
<li># Paraview's Edit / Find data dialog, MeshMixer's File/Preferences dialog).</li>
<li># By calling deleteLater, the messagebox is permanently deleted when the current call is completed.</li>
<li>mbox.deleteLater()</li>
<li>return mbox.exec_()</li>
<li>
</li>
<li class="selected">def createProgressDialog(parent=None, value=0, maximum=100, labelText="", windowTitle="Processing...", **kwargs):</li>
<li>"""Display a modal QProgressDialog. Go to QProgressDialog documentation</li>
<li>http://pyqt.sourceforge.net/Docs/PyQt4/qprogressdialog.html for more keyword arguments, that could be used.</li>
<li>E.g. progressbar = createProgressIndicator(autoClose=False) if you don't want the progress dialog to automatically</li>
<li>close.</li>
<li>Updating progress value with progressbar.value = 50</li>
<li>Updating label text with progressbar.labelText = "processing XYZ"</li>
<li>"""</li>
<li>import qt</li>
<li>progressIndicator = qt.QProgressDialog(parent if parent else mainWindow())</li>
<li>progressIndicator.minimumDuration = 0</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>See example of usage here<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMWidgets.py#L720" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMWidgets.py#L720" target="_blank">Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMWidgets.py#L720</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="710" style="counter-reset: li-counter 709 ;">
<li>
</li>
<li>if missingFileCount &gt; 0:</li>
<li>  slicer.util.warningDisplay("Warning: %d of %d selected files listed in the database cannot be found on disk."</li>
<li>                             % (missingFileCount, allFileCount), windowTitle="DICOM")</li>
<li>
</li>
<li>if missingFileCount == allFileCount:</li>
<li>  return loadablesByPlugin, loadEnabled</li>
<li>
</li>
<li>plugins = self.pluginSelector.selectedPlugins()</li>
<li>
</li>
<li class="selected">progress = slicer.util.createProgressDialog(parent=self, value=0, maximum=len(plugins))</li>
<li>
</li>
<li>for step, pluginClass in enumerate(plugins):</li>
<li>  if not self.pluginInstances.has_key(pluginClass):</li>
<li>    self.pluginInstances[pluginClass] = slicer.modules.dicomPlugins[pluginClass]()</li>
<li>  plugin = self.pluginInstances[pluginClass]</li>
<li>  if progress.wasCanceled:</li>
<li>    break</li>
<li>  progress.labelText = '\nChecking %s' % pluginClass</li>
<li>  slicer.app.processEvents()</li>
<li>  progress.setValue(step)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #3 by @Niels (2018-10-11 07:39 UTC)

<p>Thanks! My guess is that updating the progress object from inside the python logic is not good practice right. Do I have stick to widget space for this?</p>

---

## Post #4 by @lassoan (2018-10-11 12:27 UTC)

<p>In Python scripted modules, we typically add callback functions in the logic class to provide real-time feedback to widget (or any other component that uses the logic class). See for example how it is done in <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPatcher/DICOMPatcher.py#L125">DICOM Patcher module</a>.</p>

---
