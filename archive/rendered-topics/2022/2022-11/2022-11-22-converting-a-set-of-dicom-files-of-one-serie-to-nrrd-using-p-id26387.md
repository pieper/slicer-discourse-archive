# Converting a set of dicom files of one serie to nrrd using python API

**Topic ID**: 26387
**Date**: 2022-11-22
**URL**: https://discourse.slicer.org/t/converting-a-set-of-dicom-files-of-one-serie-to-nrrd-using-python-api/26387

---

## Post #1 by @Leyla_Ebrahimpour (2022-11-22 20:49 UTC)

<p>Hi. I wonder if anyone can help me with this. I am using about 400 studies (each study includes couple of series. The DICOM SEG file is also included. Imagine that I have downloaded all the data and I have found the serie to which the segmentation has been applied. Now, for each study I have a set of CT DICOM files that should be converted to one nrrd and an associted DICOM SEG file that should be converted to nrrd so that they can be used in Pyradiomics to extract the radiomics features. I know how to convert dicom files to nrrd  in slicer but if I want to do that I have to do one by one for each study and it does not make sense. I want to know how I can import a set of dicom files (or one dicom SEG file) in a python script and convert (save) it to/as one nrrd file so that it can be used in pyradiomics. This way I can import the data related to all 400 studies, convert them to nrrd files and extract radiomics using one python script. Could you please help me with it?</p>

---

## Post #2 by @pieper (2022-11-23 01:01 UTC)

<p>A general problem is that there’s a lot more flexibility in the SEG+DICOM CT representation than there is in the nrrd version as needed for radiomics.  That is, the SEG could be discontinuous or irregularly spaced compared to the CT, which itself may in general have geometric inconsistencies.  So at some level you have to “know your data” to be sure it will work for your intended use.</p>
<p>That said, the process should be pretty well defined and even the edge cases should be handled by Slicer.  I’d start by importing all the data into the dicom database.  Then you can iterate by patient/study (something <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#batch-processing">like this</a>) and find the SEG for each study.  It should reference the instance UIDs of the source images which should be the CT and you can import both into Slicer.  If there are inconsistencies in spacing or other geometry you can harden any acquisition transform and resample to a common space.  From there you can export to nrrd and run PyRadiomics.</p>

---

## Post #3 by @Leyla_Ebrahimpour (2022-11-23 19:39 UTC)

<p>Thank you so much for the reply. So, you think it is even better to upload the CT dicom images + the associated SEG files for each study one by one for a better analysis and then save them as nrrd to be able to use pyradiomics, right?</p>

---

## Post #4 by @pieper (2022-11-23 19:59 UTC)

<p>If I follow your question correctly I think yes, you should treat each study independently as part of the iteration through the dicom database.  Most likely each study will follow the same pattern and the SEG will correspond to the CT such that you can easily export the loaded volumes as nrrd, ready for PyRadiomics.  If there are issue, like irregular spacing, you could post examples of anything that arises, ideally with some sample datasets illustrating any problems.</p>

---

## Post #5 by @Leyla_Ebrahimpour (2022-12-14 15:53 UTC)

<p>Thank you for the answer. I am looking for a more automated way to convert dicom files to nrrd in order to be used in pyradiomcs. I do not want to use slicer to convert them to nrrd. I need the dicom files to be converted in my python script. Is there any way?</p>

---

## Post #6 by @pieper (2022-12-14 17:07 UTC)

<p>You can use a loop like this to iterate through all the data in your local dicom database.  This makes it easy to sort a large number of dicom studies and provides a framework for adding logic to identify the series of interest that you want to do further processing on:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#iterate-through-dicom-series" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#iterate-through-dicom-series</a></p>
<p>Another option is just to run <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a> or similar and sort through the results.  There are also python packages to convert dicom to other formats like nrrd, but keep in mind that dicom can be messy and it’s not in general a one-to-one mapping from dicom series to a scalar volume.</p>

---

## Post #7 by @tiagoengenheiro (2025-03-15 15:13 UTC)

<p>Hello, I wanted to do something similar. I would like to export some of the nodes to .nrrd for each patient, and also create binary masks for the segments of each patient and save them also in .nrrd. Since I will have close to a 100 patients, I was looking for a way to do this automatically.</p>
<p>A part from the “iterate-through-dicom-series” that you recommended, I also discovered this code in the documentation, which is closer to what I’m looking for:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-dicom-series-from-the-database-to-research-file-format">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-dicom-series-from-the-database-to-research-file-format" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-dicom-series-from-the-database-to-research-file-format" target="_blank" rel="noopener nofollow ugc">Script repository — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Since this loop is already oriented towards the nodes and not the dicom files. However, with just a few patients, it takes a long time to respond and I get this error:</p>
<p>Input:</p>
<pre><code class="lang-auto">from DICOMLib import DICOMUtils
patientUIDs = slicer.dicomDatabase.patients()
for patientUID in patientUIDs:
    loadedNodeIDs = DICOMUtils.loadPatientByUID(patientUID)
    for loadedNodeID in loadedNodeIDs:
        break
    break
</code></pre>
<p>Error logs:</p>
<pre><code class="lang-auto">[Python] Geometric issues were found with 1 of the series. Please use caution.
[Python] Geometric issues were found with 1 of the series. Please use caution.
[Python] Geometric issues were found with 1 of the series. Please use caution.
[Python] Geometric issues were found with 1 of the series. Please use caution.
[Qt] QSqlQuery::prepare: database not open
[Qt] SQL failed: 
[Qt]  
[Qt] Error: 
[Qt] Parameter count mismatch
[ITK] WARNING: In C:\D\S\S-0-build\ITK\Modules\IO\ImageBase\include\itkImageSeriesReader.hxx, line 478
[ITK] ImageSeriesReader (0000027750522C90): Non uniform sampling or missing slices detected,  maximum nonuniformity:50
[Python] Irregular volume geometry detected (maximum error of 75 mm is above tolerance threshold of 0.001 mm).  Adding acquisition transform to regularize geometry.
[VTK] Warning: In vtkOrientedGridTransform.cxx, line 335
[VTK] vtkOrientedGridTransform (00000276B0268130): InverseTransformPoint: no convergence (6.10352e-05, 325.635, -52.0008) error = 0.528551 after 500 iterations.  Further convergence warnings suppressed until transform is modified.
[VTK] Warning: In vtkOrientedGridTransform.cxx, line 335
[VTK] vtkOrientedGridTransform (00000276B0268130): InverseTransformPoint: no convergence (6.10352e-05, 325.635, -43.0508) error = 10.7057 after 500 iterations.  Further convergence warnings suppressed until transform is modified.
[ITK] WARNING: In C:\D\S\S-0-build\ITK\Modules\IO\ImageBase\include\itkImageSeriesReader.hxx, line 478
[ITK] ImageSeriesReader (0000027750523A10): Non uniform sampling or missing slices detected,  maximum nonuniformity:14.7778
[Python] Irregular volume geometry detected (maximum error of 32.1667 mm is above tolerance threshold of 0.001 mm).  Adding acquisition transform to regularize geometry.
[VTK] Warning: In vtkOrientedGridTransform.cxx, line 335
[VTK] vtkOrientedGridTransform (00000276B026B410): InverseTransformPoint: no convergence (368.554, 1.26959, 106.118) error = 10.2159 after 500 iterations.  Further convergence warnings suppressed until transform is modified.
[VTK] Warning: In vtkOrientedGridTransform.cxx, line 335
[VTK] vtkOrientedGridTransform (00000276B026B410): InverseTransformPoint: no convergence (368.554, 1.26959, 21.4076) error = 0.654355 after 500 iterations.  Further convergence warnings suppressed until transform is modified.
[ITK] WARNING: In C:\D\S\S-0-build\ITK\Modules\IO\ImageBase\include\itkImageSeriesReader.hxx, line 478
[ITK] ImageSeriesReader (0000027750521790): Non uniform sampling or missing slices detected,  maximum nonuniformity:2.26471
[Python] Irregular volume geometry detected (maximum error of 6.61765 mm is above tolerance threshold of 0.001 mm).  Adding acquisition transform to regularize geometry.
[ITK] WARNING: In C:\D\S\S-0-build\ITK\Modules\IO\ImageBase\include\itkImageSeriesReader.hxx, line 478
[ITK] ImageSeriesReader (0000027750523410): Non uniform sampling or missing slices detected,  maximum nonuniformity:8.47458
[Python] Irregular volume geometry detected (maximum error of 15.7627 mm is above tolerance threshold of 0.001 mm).  Adding acquisition transform to regularize geometry.
[VTK] Warning: In vtkOrientedGridTransform.cxx, line 335
[VTK] vtkOrientedGridTransform (00000276B02699F0): InverseTransformPoint: no convergence (6.10352e-05, 369.914, -109.47) error = 0.672556 after 500 iterations.  Further convergence warnings suppressed until transform is modified.
[VTK] Warning: In vtkOrientedGridTransform.cxx, line 335
[VTK] vtkOrientedGridTransform (00000276B02699F0): InverseTransformPoint: no convergence (6.10352e-05, 369.914, 24.0042) error = 1.20728 after 500 iterations.  Further convergence warnings suppressed until transform is modified.
[VTK] Warning: In vtkSegmentation.h, line 511
[VTK] vtkSegmentation (00000273BD05A0B0): vtkSegmentation::SetMasterRepresentationName() method is deprecated, please use SetSourceRepresentationName method instead
</code></pre>
<p>How can I solve this? Is there a better way to iterate through the patients and its nodes?</p>
<p>As a side note, I wanted to do all of this in python to take advantage of scalability, but it seems a nightmare to convert it correctly to an nrrd file which is identical to the one obtained with 3D slicer. If someone knows a way to do all of this in python with the same quality as in 3D Slicer, let me know</p>

---

## Post #8 by @pieper (2025-03-15 17:42 UTC)

<p>You should get exactly the same results using a python script as you get through the user interface since they call the same underlying code.  Converting lots of files may take a lot of time, and some dicom studies will have issues like the ones reported in the logs, and you need to handle those cases since nrrd doesn’t handle irregular spacing (either ignore those series or resample them with the acquisition transform).  Try single patients before converting in bulk.</p>

---

## Post #9 by @lassoan (2025-03-16 20:13 UTC)

<aside class="quote no-group" data-username="tiagoengenheiro" data-post="7" data-topic="26387">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tiagoengenheiro/48/79727_2.png" class="avatar"> tiagoengenheiro:</div>
<blockquote>
<p><code>QSqlQuery::prepare: database not open</code></p>
</blockquote>
</aside>
<p>This suggests that you haven’t created a database or it is in an inaccessible location (e.g., was created on a USB stick that has been since removed). You can use the DICOM module GUI to select or create a valid database.</p>

---

## Post #10 by @tiagoengenheiro (2025-03-19 17:13 UTC)

<p>Thank you very much for your insights.</p>
<p>I have another question for you, maybe you can help me.</p>
<p>For context, I have CT scans of most/all phases of the breathing cycle, the avg phase, RT-doses and RT-structures. Most of the phases have irregular spacing so I have been extracting the transformed version as you suggested. A part from that I also need to retrieve structures such as ITV, PTV, Liver-ITV, etc, which were pre-segmented. The objective is then to compute radiomic features using these structures as masks.</p>
<p>I noticed that for some patients I have the possibility of extracting these structures after applying a transformation. I believe this occurs because the structures were segmented with an unaligned phase of the breathing cycle. Given this, I’m not sure what is the best way to proceed from a theoretical point of view, if I should also apply a transformation in the structures, since I have phases with and without irregular spacing</p>

---
