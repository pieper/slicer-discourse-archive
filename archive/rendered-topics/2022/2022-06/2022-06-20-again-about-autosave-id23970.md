# Again about autosave

**Topic ID**: 23970
**Date**: 2022-06-20
**URL**: https://discourse.slicer.org/t/again-about-autosave/23970

---

## Post #1 by @volkodavmyx (2022-06-20 19:37 UTC)

<p>Hello! I just tried the Autosave utility from the sandbox. It’s very handy, but saving all scene in to a MRB file is too expensive.</p>
<p>How can I modify the AutoSave.py if i need to save only Segmentation.seg.nrrd file automatically?</p>
<p>I understand that I need to use myNode = getNode(“Segmentation”) script, but i have no idea how to paste it in AutoSave.py</p>
<p>Thank you for your assistance!</p>

---

## Post #2 by @pieper (2022-06-20 19:47 UTC)

<p>You should need to rewrite this code.  Probably save only segmentation nodes would be much faster than making the mrb.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerSandbox/blob/master/AutoSave/AutoSave.py#L178">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/AutoSave/AutoSave.py#L178" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerSandbox/blob/master/AutoSave/AutoSave.py#L178" target="_blank" rel="noopener">PerkLab/SlicerSandbox/blob/master/AutoSave/AutoSave.py#L178</a></h4>



    <pre class="onebox">      <code class="lang-py">
        <ol class="start lines" start="168" style="counter-reset: li-counter 167 ;">
            <li>    self.autoSaveTimer.stop()</li>
            <li>  elif (not self.autoSaveTimer.active) and self.getAutoSaveEnabled():</li>
            <li>    self.autoSaveTimer.start()</li>
            <li>
            </li>
<li>def onAutoSaveTimeout(self):</li>
            <li>  directory = self.getSaveDirectory()</li>
            <li>  self.autoSaveCallback(directory)</li>
            <li>
            </li>
<li>def saveScene(self, directory):</li>
            <li>  # Generate file name</li>
            <li class="selected">  sceneSaveFilename = directory + "/" + time.strftime("%Y%m%d-%H%M%S") + ".mrb"</li>
            <li>  # Save scene</li>
            <li>  if slicer.util.saveScene(sceneSaveFilename):</li>
            <li>    logging.info("Scene saved to: {0}".format(sceneSaveFilename))</li>
            <li>  else:</li>
            <li>    logging.error("Scene saving failed")</li>
            <li>
            </li>
<li>def setDefaultParameters(self, parameterNode):</li>
            <li>  if parameterNode is None:</li>
            <li>    return</li>
            <li>  if not parameterNode.GetParameter(self.AUTO_SAVE_ENABLED_PARAMETER_NAME):</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @volkodavmyx (2022-06-20 20:24 UTC)

<p>Yap, saving only Segmentation is much faster, but i didn’t know how to rewrite this code <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @pieper (2022-06-20 20:36 UTC)

<p>Haha, yes, well it depends on how general purpose you want to be vs. hard-coding your use case.<br>
Simplest would be something like this, just to save a series of segmentations you could browse through later if needed.</p>
<pre><code class="lang-auto">slicer.util.exportNode(slicer.modules.SegmentEditorWidget.parameterSetNode.GetSegmentationNode(), "/tmp/ausosave" + time.strftime("%Y%m%d-%H%M%S") + ".seg.nrrd")
</code></pre>
<p>But there are other things you may want, like only saving if there are changes, saving different segmentations with different names, etc.</p>

---

## Post #5 by @lassoan (2022-06-20 22:56 UTC)

<p>You may also find the <code>Export to file by pressing Ctrl+Shift+S key</code> <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-labelmap-node-from-segmentation-node">example in the script repository</a> useful. It allows you to export the segmentation to a file on a keypress combination. You can modify it to save the segmentation node instead of a labelmap node, generate a new filename automatically (so that you don’t overwrite previous saves), etc.</p>
<p><a class="mention" href="/u/volkodavmyx">@volkodavmyx</a> What is the reason for autosave?</p>
<p>Were you able to make Slicer crash? If yes, then we want to know more about it (what operating system, how much memory you used, how big your data was, what operations caused trouble, etc.). We rather keep the software so robust that users don’t need to resort to autosave. If you find that sometimes you run out of memory then you can increase the swap/virtual memory size in your system settings (Windows/Linux) or make more disk space available (macOS).</p>
<p>If you just want to keep more undo states than the default then you can set it to a higher value by typing this into the Python console: <code>slicer.util.getModuleWidget('SegmentEditor').editor.maximumNumberOfUndoStates=15</code> (it changes the number of undo states from the default 10 to 15). Just make sure you have enough memory to store the increased number of undo states.</p>

---
