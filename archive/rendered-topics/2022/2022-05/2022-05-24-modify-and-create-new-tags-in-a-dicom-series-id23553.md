---
topic_id: 23553
title: "Modify And Create New Tags In A Dicom Series"
date: 2022-05-24
url: https://discourse.slicer.org/t/23553
---

# Modify and create new Tags in a dicom series

**Topic ID**: 23553
**Date**: 2022-05-24
**URL**: https://discourse.slicer.org/t/modify-and-create-new-tags-in-a-dicom-series/23553

---

## Post #1 by @SergioReinosa (2022-05-24 09:52 UTC)

<p>Hi,</p>
<p>I’m developing an extension that has to add to the series Metadata a tag that indicates a URL and also update some other tags, like actual Date or Time.</p>
<p>My issue is that I can read without any problem the metadata with a extract of code like the following:</p>
<pre><code class="lang-auto">    db = slicer.dicomDatabase

    patientList = db.patients()
    studyList = db.studiesForPatient(patientList[0])
    seriesList = db.seriesForStudy(studyList[0])
    fileList = db.filesForSeries(seriesList[0])

    accn = db.fileValue(fileList[0], "0008,0050")
    stuyInstanceUID = db.fileValue(fileList[0], "0020,000D")
    patientID = db.fileValue(fileList[0], "0010,0020")
    patientName = db.fileValue(fileList[0], "0010,0010")
    patientBirthdate = db.fileValue(fileList[0], "0010,0030")
</code></pre>
<p>But when I want to modify and existing tag or create a new one, as I need to save my URL, I don’t know how to do.</p>
<p>In order to modify tags, I have tried things like:</p>
<pre><code class="lang-auto">    from pydicom import dcmread
    ds = dcmread(fileList[0])
    ds[0x0010, 0x0020].value = 'New name'
</code></pre>
<p>But it doesn’t modify. I know that there is a ‘setTag’ method in pydicom but I dont know with which object can I use it. I have checked the Script repository but I haven’t seen anything that I can use. If anyone can help me it would be great.</p>
<p>Thank you very much,</p>

---

## Post #2 by @pieper (2022-05-24 12:25 UTC)

<p>You can have a look at the DICOMParser for ideas.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPatcher/DICOMPatcher.py">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPatcher/DICOMPatcher.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPatcher/DICOMPatcher.py" target="_blank" rel="noopener">Slicer/Slicer/blob/master/Modules/Scripted/DICOMPatcher/DICOMPatcher.py</a></h4>


      <pre><code class="lang-py">import logging
import os

import ctk
import qt

import slicer
from slicer.ScriptedLoadableModule import *


#
# DICOMPatcher
#

class DICOMPatcher(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPatcher/DICOMPatcher.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2022-05-24 12:51 UTC)

<aside class="quote no-group" data-username="SergioReinosa" data-post="1" data-topic="23553">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/91b2a8/48.png" class="avatar"> SergioReinosa:</div>
<blockquote>
<p>But it doesn’t modify.</p>
</blockquote>
</aside>
<p>DICOM standard does not let you modify an instance that was made available outside your software. No modification of an existing instance is allowed, because an instance UID must uniquely identify the entire content. Therefore, if you received a DICOM file from somewhere and want to make changes then you must create a new instance (with new instance UIDs), preferably add references to the original UIDs, and then hide or delete the original version.</p>
<p>The DICOM patcher in Slicer can modify an instance without regenerating UIDs, but this is for cases when the input data has already violated the DICOM standard.</p>

---

## Post #4 by @SergioReinosa (2022-06-23 09:30 UTC)

<p>Ok, I haven’t been working on it lately but I have started again. I searched and i didn’t find anything about creating a new instance from the DICOM file I originally had. Is it possible? Being able to create a duplicate with a different UID and some other different parameters would solve my problem.</p>
<p>Thank you very much.</p>

---

## Post #5 by @pieper (2022-06-23 14:33 UTC)

<p>Creating valid dicom files is a complex topic, and everything depend on what you are really trying to accomplish.  Have a look at the <code>export</code> methods in some of the plugins for examples.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/Slicer/tree/master/Modules/Scripted/DICOMPlugins">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Scripted/DICOMPlugins" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/Slicer/tree/master/Modules/Scripted/DICOMPlugins" target="_blank" rel="noopener">Slicer/Modules/Scripted/DICOMPlugins at master · Slicer/Slicer</a></h3>

  <p><a href="https://github.com/Slicer/Slicer/tree/master/Modules/Scripted/DICOMPlugins" target="_blank" rel="noopener">master/Modules/Scripted/DICOMPlugins</a></p>

  <p><span class="label1">Multi-platform, free open source software for visualization and image computing.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
