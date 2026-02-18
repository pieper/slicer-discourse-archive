# Load DICOM series using python

**Topic ID**: 3257
**Date**: 2018-06-21
**URL**: https://discourse.slicer.org/t/load-dicom-series-using-python/3257

---

## Post #1 by @Ben_George (2018-06-21 13:33 UTC)

<p>Hi</p>
<p>I am trying to create a python script that can import a DICOM image series from a folder, however I can’t seem to find a way to make this work.</p>
<p>I can load a single DICOM file (in my case an RTSTRUCT) using this code:</p>
<pre><code>contour_fn = 'contours.dcm'
	
	# Add filename to list for DICOM-RT module
	contour_vtkFileList = vtk.vtkStringArray()
	contour_vtkFileList.InsertNextValue(slicer.util.toVTKString(contour_fn))
	
	# Examine files
	contour_loadablesCollection = vtk.vtkCollection()
	slicer.modules.dicomrtimportexport.logic().ExamineForLoad(contour_vtkFileList, contour_loadablesCollection)
	# Set name for when loaded
	contour_loadablesCollection.GetItemAsObject(0).SetName('RTSTRUCT')
	
	# Load file
	contour_success = slicer.modules.dicomrtimportexport.logic().LoadDicomRT(contour_loadablesCollection.GetItemAsObject(0))
</code></pre>
<p>However, if I create a list of filenames to load, it doesn’t seem to work correctly. Specifically, my ‘loadablesCollection’ is empty.</p>
<p>Is there a way to do this? I have seen options for loading patients from the DICOM browser, but I don’t want to have to import all the data through that if possible. Also, I’m not sure what the patient name will be, so don’t know how I would do a load by name/ID.</p>
<p>Many thanks</p>
<p>Ben</p>

---

## Post #2 by @cpinter (2018-06-21 16:00 UTC)

<p>Hi Ben,</p>
<p>There are many convenience functions just for this in DICOMUtils. So you don’t need to go through the logic classes:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py" target="_blank">Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py</a></h4>
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

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>I see you want to load RT data. The code form this automated test might help:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Testing/Python/DicomRtImportTest.py" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Testing/Python/DicomRtImportTest.py" target="_blank">SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Testing/Python/DicomRtImportTest.py</a></h4>
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

  This file has been truncated. <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Testing/Python/DicomRtImportTest.py" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
or this<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py" target="_blank">SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py</a></h4>
<pre><code class="lang-py">import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from DICOMLib import DICOMUtils
import logging

#
# IGRTWorkflow_SelfTest
#
# IGRT: Calculate isocenter shifting, and evaluate its effect on the dose
#   1. Load planning DICOM-RT data and day 2 volumes
#   2. Add day 2 volumes in Subject Hierarchy
#   3. Compute isodose lines for both dose distributions
#   4. Register day 2 CT to planning CT using rigid registration
#   5. Transform day 2 dose volumes using the result transform
#   6. Compute difference dose using gamma comparison for
#     6A. Planning dose and unregistered day 2 dose
#     6B. Planning dose and registered day 2 dose
#   7. Accumulate
</code></pre>

  This file has been truncated. <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #3 by @Ben_George (2018-06-22 06:49 UTC)

<p>Hi Csaba</p>
<p>Thanks for your response, I’ll take a look through the examples you suggested.</p>

---

## Post #4 by @fedorov (2018-07-30 13:43 UTC)

<p>You can also take a look at <a href="https://github.com/SlicerProstate/mpReview/blob/master/mpReviewPreprocessor.py">this python module</a> that provides a command line tool to essentially take a folder with DICOM data, and organize it into patient/study/series hierarchy of folders accompanied by volumetric reconstructions for each series. It does not handle RT, but it should be easy to add that. You can also find more details here: <a href="https://discourse.slicer.org/t/how-can-i-convert-dicom-series-to-nrrd-files-in-batch-mode/3421">How can I convert DICOM series to NRRD files in batch mode?</a>.</p>

---

## Post #6 by @zgk110 (2018-09-16 03:40 UTC)

<p>Hi, i am trying to import a dicom series directory by python scripting, i just found the command 'slicer.util.loadNodeFromFile /loadScene/loadVolume ’ , is there any other function to load the dicom series from directory ?</p>

---

## Post #7 by @lassoan (2018-09-16 13:36 UTC)

<p>The post above has been moved here, as the same question has been discussed in this topic. If you have any follow-up questions please post them here.</p>

---

## Post #8 by @Markba122 (2025-04-10 15:05 UTC)

<p>Hi all,</p>
<p>Something that I hope could help is a Python class meant to quickly iterate down a series of folders with the help of SimpleITK to identifying unique images by their Series Instance UIDs. The found images can then be saved as SimpleITK Image files (‘.nii’) or NumPy arrays.</p>
<p>The GitHub repo has a Jupyter notebook to show you examples: <a href="https://github.com/brianmanderson/Dicom_RT_and_Images_to_Mask" class="inline-onebox" rel="noopener nofollow ugc">GitHub - brianmanderson/Dicom_RT_and_Images_to_Mask: Tools to help with the conversion of DICOM images, RT Structures, and dose to useful Python objects. Essentially DICOM to NumPy and SimpleITK Images</a></p>
<p>The publication that goes along with the program is also here: <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8102371/" class="inline-onebox" rel="noopener nofollow ugc">Simple Python Module for Conversions between DICOM Images and Radiation Therapy Structures, Masks, and Prediction Arrays - PMC</a></p>
<p>Hope this can help!<br>
Brian</p>

---
