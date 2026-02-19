---
topic_id: 3975
title: "Observing And Tracking Scriptedloadablemodulelogic"
date: 2018-09-03
url: https://discourse.slicer.org/t/3975
---

# Observing and tracking ScriptedLoadableModuleLogic

**Topic ID**: 3975
**Date**: 2018-09-03
**URL**: https://discourse.slicer.org/t/observing-and-tracking-scriptedloadablemodulelogic/3975

---

## Post #1 by @dominicrushforth (2018-09-03 15:25 UTC)

<p>I am doing some image processing in a ScriptedLoadableModuleLogic module. I would like to set up a progress bar to show that the logic is running and connect to another routine on completion.</p>
<p>I have been trying to emulate the qSlicerCLIProgressBar with an observer like that below to trigger the status updates and completion routine…</p>
<p>self.cliNodeObserverTag = self.cliNode.AddObserver(‘ModifiedEvent’, self.onCLIEvent)</p>
<p>…however I’ve not been having much success.</p>
<p>I suspect I may be over complicating the problem and that there may be a much more straighforward solution. I’d be grateful for any suggestions <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @pieper (2018-09-03 16:36 UTC)

<p>The CLI runs in a separate process, so there the progress update is event driven/asynchronous.</p>
<p>For a scripted module running in the main thread, you need to update the progress manually based on steps in your computation, something like what is done in the DICOM module:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMWidgets.py#L720-L746" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMWidgets.py#L720-L746" target="_blank">Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMWidgets.py#L720-L746</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="720" style="counter-reset: li-counter 719 ;">
<li>progress = slicer.util.createProgressDialog(parent=self, value=0, maximum=len(plugins))</li>
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
<li>  slicer.app.processEvents()</li>
<li>  try:</li>
<li>    loadablesByPlugin[plugin] = plugin.examineForImport(fileLists)</li>
<li>    # If regular method is not overridden (so returns empty list), try old function</li>
<li>    # Ensuring backwards compatibility: examineForImport used to be called examine</li>
<li>    if not loadablesByPlugin[plugin]:</li>
<li>      loadablesByPlugin[plugin] = plugin.examine(fileLists)</li>
<li>    loadEnabled = loadEnabled or loadablesByPlugin[plugin] != []</li>
<li>  except Exception, e:</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMWidgets.py#L720-L746" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
