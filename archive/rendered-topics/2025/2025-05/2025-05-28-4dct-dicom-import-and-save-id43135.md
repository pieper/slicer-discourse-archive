---
topic_id: 43135
title: "4Dct Dicom Import And Save"
date: 2025-05-28
url: https://discourse.slicer.org/t/43135
---

# 4DCT dicom import and save

**Topic ID**: 43135
**Date**: 2025-05-28
**URL**: https://discourse.slicer.org/t/4dct-dicom-import-and-save/43135

---

## Post #1 by @Amy_Morton (2025-05-28 11:57 UTC)

<p>I found many helpful topics on the discourse, but still have yet to find a full soluiton:</p>
<p>I have 100+ 4dct scans in dicom format, I’d like to import them and save as .nrrd or .seq.nrrd</p>
<p>When loaded using the import dicom from folder in the module, the volume loads as a sequence, and can be saved which generates a .nrrd and .seq.nrrd</p>
<p>Attempting to batch process this, I used similar functions written fro 3dct, but I’m running into unwanted functionality:</p>
<pre><code class="lang-auto">def importDICOM(dicomDataDir) -&gt; list:
 
  loadedNodeIDs = []
  from DICOMLib import DICOMUtils

  with DICOMUtils.TemporaryDICOMDatabase() as db:
    DICOMUtils.importDicom(dicomDataDir, db)
    patientUIDs = db.patients()
    for patientUID in patientUIDs:
      loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
    
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUIDs[0]))

  return loadedNodeIDs
</code></pre>
<p>The DICOMUtils loadPatienBytUID seems to generate a duplicate node.. which makes parsing and saving the appropriate volumes tricky</p>
<p>I can add some more screenshots later today - but any suggestions are welcome!</p>

---

## Post #2 by @pieper (2025-05-28 12:22 UTC)

<p>It looks like you are on the right track.  Different CTs might or might not be detected as sequences depending on the header tags.  You can interate through and see which ones are not and check them interactively.  You might need to go a level lower and use the sequence plugin directly.</p>

---

## Post #3 by @Amy_Morton (2025-05-28 13:59 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a></p>
<p>I dug deeper using the DICOM module , based on the recommendation on <a href="https://discourse.slicer.org/t/load-dicom-series-using-python/3257/2">another topic</a> to view</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Testing/Python/DicomRtImportTest.py">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Testing/Python/DicomRtImportTest.py" target="_blank" rel="noopener nofollow ugc">github.com/SlicerRt/SlicerRT</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Testing/Python/DicomRtImportTest.py" target="_blank" rel="noopener nofollow ugc">DicomRtImportExport/Testing/Python/DicomRtImportTest.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Testing/Python/DicomRtImportTest.py" rel="noopener nofollow ugc"><code>master</code></a>
</div>


      <pre><code class="lang-py">import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging

class DicomRtImportTest(unittest.TestCase):
  def setUp(self):
    """ Do whatever is needed to reset the state - typically a scene clear will be enough.
    """
    slicer.mrmlScene.Clear(0)

    #TODO: Comment out
    #logFile = open('d:/pyTestLog.txt', 'a')
    #logFile.write(repr(slicer.modules.DicomRtImportTest) + '\n')
    #logFile.write(repr(slicer.modules.dicomrtimportexport) + '\n')
    #logFile.close()

  #------------------------------------------------------------------------------
  def runTest(self):
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Testing/Python/DicomRtImportTest.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<pre><code class="lang-auto">slicer.util.selectModule("DICOM")
browserWidget = slicer.modules.DICOMWidget.browserWidget
browserWidget.importDirectory(vol_pth)
#loadables, loadablesByPlugin = selectLoadables(browserWidget)

patient = slicer.dicomDatabase.patients()[0]
studies = slicer.dicomDatabase.studiesForPatient(patient)
series = [slicer.dicomDatabase.seriesForStudy(study) for study in studies]
seriesUIDs = [uid for uidList in series for uid in uidList]
browserWidget.onSeriesSelected(seriesUIDs)
browserWidget.examineForLoading()

loadables = browserWidget.loadableTable.loadables

loadablesByPlugin = browserWidget.loadablesByPlugin
for plugin in loadablesByPlugin:
  print(plugin.loadType)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c3b1bdaecd8c83b509bff7dd69ca6675049aca7.png" data-download-href="/uploads/short-url/aSmVwrhhLjz0I9EzOmvvItyFYRF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c3b1bdaecd8c83b509bff7dd69ca6675049aca7.png" alt="image" data-base62-sha1="aSmVwrhhLjz0I9EzOmvvItyFYRF" width="374" height="218"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">374×218 3.51 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For my 4DCT, is it sufficient to only use the Volume Sequnce import plugin lodable?</p>

---

## Post #4 by @pieper (2025-05-28 14:05 UTC)

<p>Yes, if you want to load everything as a sequence then yes only use the sequence plugin.  By default the high level code picks the loadables that have the highest <code>confidence</code> (i.e. the plugin’s heuristics indicate that the data in question matches the intent of the plugin.  You can look at the <code>examine</code> portion of the plugins to see what they are looking for in the data.  Sequences in particular can be encoded many ways so the heuristics are not always right.  But if you know your data is 4dct, then you should ensure that the sequence plugin is used.</p>

---

## Post #5 by @Deep_Learning (2025-05-30 14:49 UTC)

<p>consider using dcm2niix</p>

---
