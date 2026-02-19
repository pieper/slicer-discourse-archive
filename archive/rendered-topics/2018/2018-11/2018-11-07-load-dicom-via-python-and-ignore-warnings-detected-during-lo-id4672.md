---
topic_id: 4672
title: "Load Dicom Via Python And Ignore Warnings Detected During Lo"
date: 2018-11-07
url: https://discourse.slicer.org/t/4672
---

# Load DICOM via python and ignore 'Warnings detected during load' dialog

**Topic ID**: 4672
**Date**: 2018-11-07
**URL**: https://discourse.slicer.org/t/load-dicom-via-python-and-ignore-warnings-detected-during-load-dialog/4672

---

## Post #1 by @Ben_George (2018-11-07 16:27 UTC)

<p>Hi</p>
<p>The latest version of Slicer has added a pop-up confirmation dialog when DICOM series are loaded which contain errors. This directs the user to look at the Advanced Information panel in the DICOM browser to find the warnings, or press OK to continue.</p>
<p>When using ‘–no-main-window’ and ‘–python-script’ flags to run some code which imports DICOMs, this dialog is not displayed and the script hangs at this point.</p>
<p>Is there any way to accept this warning when loading DICOMs in this way? Either programatically or having the dialog box displayed?</p>
<p>Thanks</p>
<p>Ben</p>

---

## Post #2 by @lassoan (2018-11-07 21:02 UTC)

<p>Unfortunately, widget and logic are mixed in DICOM module. It would need significant rework to nicely separate them - I’ve added a ticket to track this task: <a href="https://issues.slicer.org/view.php?id=4655">https://issues.slicer.org/view.php?id=4655</a></p>
<p>Until it is fixed (probably will not happen soon unless some dedicated funding arrives or somebody volunteers), you can change <code>warnUserIfLoadableWarningsAndProceed</code> function in DICOMWidgets.py in your local Slicer installation to not display a popup but for example write the warnings to a log file instead:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/da6ad88dba4d60b7784953b01e82c5dd21670503/Modules/Scripted/DICOMLib/DICOMWidgets.py#L897-L909" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/da6ad88dba4d60b7784953b01e82c5dd21670503/Modules/Scripted/DICOMLib/DICOMWidgets.py#L897-L909" target="_blank">Slicer/Slicer/blob/da6ad88dba4d60b7784953b01e82c5dd21670503/Modules/Scripted/DICOMLib/DICOMWidgets.py#L897-L909</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="897" style="counter-reset: li-counter 896 ;">
<li>def warnUserIfLoadableWarningsAndProceed(self):</li>
<li>  warningsInSelectedLoadables = False</li>
<li>  for plugin in self.loadablesByPlugin:</li>
<li>    for loadable in self.loadablesByPlugin[plugin]:</li>
<li>      if loadable.selected and loadable.warning != "":</li>
<li>        warningsInSelectedLoadables = True</li>
<li>        logging.warning('Warning in DICOM plugin ' + plugin.loadType + ' when examining loadable ' + loadable.name +</li>
<li>                        ': ' + loadable.warning)</li>
<li>  if warningsInSelectedLoadables:</li>
<li>    warning = "Warnings detected during load.  Examine data in Advanced mode for details.  Load anyway?"</li>
<li>    if not slicer.util.confirmOkCancelDisplay(warning, parent=self):</li>
<li>      return False</li>
<li>  return True</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
