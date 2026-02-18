# SimpleITK fails to load DICOM metadata

**Topic ID**: 6822
**Date**: 2019-05-16
**URL**: https://discourse.slicer.org/t/simpleitk-fails-to-load-dicom-metadata/6822

---

## Post #1 by @Ulla (2019-05-16 17:54 UTC)

<p>I’m using SimpleITK inside my Python scripted module to read metadata from DICOMs. It worked on older Slicer versions (4.6 and 4.8) but I cannot make it work on Slicer 4.10.1. The problem happens on all DICOM files I have tried.</p>
<p>Works:<br>
SimpleITK version is 1.1.0dev (ITK 4.12) on Slicer-4.8 and 1.1.0 (ITK 4.13) on Slicer 4-10.1</p>
<p>Doesn’t work:<br>
SimpleITK version 1.1.0 (ITK 4.13). (This SimpleITK works on system Python but not inside Slicer)</p>
<p>Example codes:</p>
<pre><code class="lang-auto"># This example worked on old Slicer
i = sitk.ReadImage('image.dcm')
i.GetMetaDataKeys()
</code></pre>
<pre><code class="lang-auto">imageReader= sitk.ImageSeriesReader()
path='/directory/'
series_ids = imageReader.GetGDCMSeriesIDs(path)
imageReader.MetaDataDictionaryArrayUpdateOn()
series_file_names = imageReader.GetGDCMSeriesFileNames(path, series_ids[0])
imageReader.SetFileNames(series_file_names)
imageReader.MetaDataDictionaryArrayUpdateOn()
reader.LoadPrivateTagsOn();
image = imageReader.Execute()
print(image.GetMetaDataKeys())
</code></pre>
<pre><code class="lang-auto">reader = sitk.ImageFileReader()
reader.SetFileName('image.dcm')
reader.ReadImageInformation();
reader.GetMetaDataKeys();
</code></pre>

---

## Post #2 by @cpinter (2019-05-16 19:44 UTC)

<p>DICOM importing and loading is quite difficult in general, and that’s why Slicer provides advanced tools for this. Please see convenience functions here, with special attention to the <code>importDicom</code> and <code>loadPatient</code> functions:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py</a></h4>
<pre><code class="lang-py">import os
import vtk, qt, ctk, slicer
import logging

#########################################################
#
#
comment = """

  DICOMUtils is a collection of static-like DICOM
  utility functions facilitating convenient scripted
  use of the DICOM database

"""
#
#########################################################

#------------------------------------------------------------------------------
def loadPatientByUID(patientUID):
  """ Load patient by patient UID from DICOM database
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #3 by @lassoan (2019-05-17 03:14 UTC)

<p>SimpleITK’s capabilities for accessing DICOM tags are very limited anyway, so I would not bother trying to make that work. You can access some common tags in Slicer database and you can get proper, full access to all fields using pydicom (bundled with Slicer).</p>

---

## Post #4 by @Ulla (2019-05-17 04:19 UTC)

<p>Thanks for the answers. I’m not trying to load or import DICOMs on Slicer. My goal is to make a dicom series writer which suits for my work better than the “create a DICOM series” -module. In my module, I am selecting a file from the DicomDatabase and then I want to copy parts of the header to a new DICOM file. I have also tried to access the “create a DICOM series” -module from python script but couldn’t found out how to use it from <code>slicer.modules.createdicomseries</code>.</p>
<p>With Slicer-4.8 GetMetaDataKeys returns a list of tags but with Slicer-4.10.1 GetMetaDataKeys returns an empty list without errors. My module works on Slicer-4.8 as expected and I’m interested to know why it doesn’t work with newer versions since the header reading works with the same SimpleITK version outside Slicer.</p>

---

## Post #5 by @lassoan (2019-05-17 04:24 UTC)

<aside class="quote no-group" data-username="Ulla" data-post="4" data-topic="6822">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/u/c67d28/48.png" class="avatar"> Ulla:</div>
<blockquote>
<p>I have also tried to access the “create a DICOM series” -module from python script but couldn’t found out how to use it from <code>slicer.modules.createdicomseries</code> .</p>
</blockquote>
</aside>
<p><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMExportScalarVolume.py">DICOM exporter</a> is implemented in Python and uses createdicomseries module. You can use it as an example.</p>
<aside class="quote no-group" data-username="Ulla" data-post="4" data-topic="6822">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/u/c67d28/48.png" class="avatar"> Ulla:</div>
<blockquote>
<p>I want to copy parts of the header to a new DICOM file</p>
</blockquote>
</aside>
<p>For this purpose, pydicom is the best tool in Python (in C++ I would recommend DCMTK or GDCM). For example, this is how the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPatcher/DICOMPatcher.py">DICOM Patcher module</a> works.</p>

---

## Post #6 by @Ulla (2019-05-21 13:27 UTC)

<p>Thank you! I think I got it working with Create a DICOM series -module and pydicom.</p>

---
