# Cleaning up local Dicom Database files

**Topic ID**: 2828
**Date**: 2018-05-16
**URL**: https://discourse.slicer.org/t/cleaning-up-local-dicom-database-files/2828

---

## Post #1 by @EricWilson (2018-05-16 17:32 UTC)

<p>I noticed that the local dicom database files stick around even when you delete all the patients, and will continue growing in size as more patients are added and removed. I would like to clean up these files to prevent any issues if a computer has to process many patients.</p>
<p>how would i do this in slicer? I know how to delete the files themselves, but they are in use during the runtime of the application as far as i can tell, and will throw an error of ‘File in use’</p>
<p>code i’m using:<br>
import os, shutil<br>
dir = os.path.dirname(slicer.dicomDatabase.databaseFilename)<br>
shutil.rmtree(dir)</p>

---

## Post #2 by @pieper (2018-05-16 17:55 UTC)

<p>Probably the easiest would be to open a new database directory and then it should be possible to delete the old one.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/523cc4c074b8b292959a1ebf7880d8c0e8ca7534/Modules/Scripted/DICOMLib/DICOMUtils.py#L141-L237" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/523cc4c074b8b292959a1ebf7880d8c0e8ca7534/Modules/Scripted/DICOMLib/DICOMUtils.py#L141-L237" target="_blank">Slicer/Slicer/blob/523cc4c074b8b292959a1ebf7880d8c0e8ca7534/Modules/Scripted/DICOMLib/DICOMUtils.py#L141-L237</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="141" style="counter-reset: li-counter 140 ;">
<li>#------------------------------------------------------------------------------</li>
<li># Open specified DICOM database</li>
<li>def openDatabase(databaseDir):</li>
<li>if not hasattr(slicer, 'dicomDatabase') or not hasattr(slicer.modules, 'dicom'):</li>
<li>  logging.error('DICOM module or database cannot be accessed')</li>
<li>  return False</li>
<li>if not os.access(databaseDir, os.F_OK):</li>
<li>  logging.error('Specified database directory ' + repr(databaseDir) + ' cannot be found')</li>
<li>  return False</li>
<li>dicomWidget = slicer.modules.dicom.widgetRepresentation().self()</li>
<li>dicomWidget.onDatabaseDirectoryChanged(databaseDir)</li>
<li>if not slicer.dicomDatabase.isOpen:</li>
<li>  logging.error('Unable to open DICOM database ' + databaseDir)</li>
<li>  return False</li>
<li>return True</li>
<li>
</li>
<li>#------------------------------------------------------------------------------</li>
<li>def openTemporaryDatabase(directory=None):</li>
<li>""" Open temporary DICOM database, return current database directory</li>
<li>"""</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/523cc4c074b8b292959a1ebf7880d8c0e8ca7534/Modules/Scripted/DICOMLib/DICOMUtils.py#L141-L237" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Although this block seems to indicate it’s not possible:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/523cc4c074b8b292959a1ebf7880d8c0e8ca7534/Modules/Scripted/DICOMLib/DICOMUtils.py#L205-L213" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/523cc4c074b8b292959a1ebf7880d8c0e8ca7534/Modules/Scripted/DICOMLib/DICOMUtils.py#L205-L213" target="_blank">Slicer/Slicer/blob/523cc4c074b8b292959a1ebf7880d8c0e8ca7534/Modules/Scripted/DICOMLib/DICOMUtils.py#L205-L213</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="205" style="counter-reset: li-counter 204 ;">
<li>if cleanup:</li>
<li>  slicer.dicomDatabase.initializeDatabase()</li>
<li>  # TODO: The database files cannot be deleted even if the database is closed.</li>
<li>  #       Not critical, as it will be empty, so will not take measurable disk space.</li>
<li>  # import shutil</li>
<li>  # databaseDir = os.path.split(slicer.dicomDatabase.databaseFilename)[0]</li>
<li>  # shutil.rmtree(databaseDir)</li>
<li>  # if os.access(databaseDir, os.F_OK):</li>
<li>    # logging.error('Failed to delete DICOM database ' + databaseDir)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/cpinter">@cpinter</a> may also have ideas why this fails - perhaps we need to find out where the database files (or directory?) are still in use.</p>

---

## Post #3 by @lassoan (2018-05-16 20:12 UTC)

<p>There could be multiple connection to the database from multiple modules. You probably need to restart Slicer to make sure none of them still uses the old database file.</p>

---

## Post #4 by @EricWilson (2018-05-16 20:20 UTC)

<p>so you are saying that the database couldn’t be cleared out in one session? is there any way to close down all the modules that might be using it, maybe when the application is closing, and just run the code for removing the files just before the app quits? or is there a place in slicer where data can be stored to persist until the next session where you could store the last database location and remove it when the next session runs?</p>

---

## Post #5 by @lassoan (2018-05-19 14:51 UTC)

<p>The easiest is to switch to a new (empty) DICOM database folder. The old folder can be deleted once you closed Slicer.</p>

---

## Post #6 by @EricWilson (2018-05-21 16:04 UTC)

<p>that method should work for me. I just need to find how to set the local database folder through python, I’m not currently seeing the method to do that, could you point me in the right direction?</p>
<p>thanks.</p>

---

## Post #7 by @pieper (2018-05-21 17:02 UTC)

<p><code>slicer.dicomDatabase.databaseFilename</code></p>

---

## Post #8 by @EricWilson (2018-05-21 18:53 UTC)

<p>that is a way to access the current database, but it is not a writable variable.</p>
<p>Also, it points to the sql data file in the folder. If i just assigned that to a new path with the same data file name, would it create a new file with the given name or would i have to initialize the database somehow?</p>

---

## Post #9 by @EricWilson (2018-05-21 19:53 UTC)

<p>ok, it looks like I can use the dicom utils to open the database, which will set the current database to the passed path.</p>
<p>example:<br>
import DICOMLib.DICOMUtils as utils<br>
utils.openDatabase(newDir)</p>

---
