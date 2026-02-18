# Faster DICOM loading

**Topic ID**: 19723
**Date**: 2021-09-17
**URL**: https://discourse.slicer.org/t/faster-dicom-loading/19723

---

## Post #1 by @S_Arbabi (2021-09-17 09:36 UTC)

<p>Hi, I’m loading DICOM series this way:</p>
<pre><code class="lang-auto">    from DICOMLib import DICOMUtils
    loadedNodeIDs = []
    
    with DICOMUtils.TemporaryDICOMDatabase() as db:
      DICOMUtils.importDicom(image_dicom_folder, db)
      patientUIDs = db.patients()
      for patientUID in patientUIDs:
        loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
    #print("image loaded:",image_dicom_folder)
    slicer.app.applicationLogic().GetInteractionNode().SetCurrentInteractionMode(slicer.vtkMRMLInteractionNode.AdjustWindowLevel)
</code></pre>
<p>for a DICOM series to load it takes around 25 seconds on a intel quad core 4.00GHz cpu and 32 GB of Ram.</p>
<p>I was wondering if this is something that I can improve in some way?</p>
<p>Best</p>

---

## Post #2 by @lassoan (2021-09-17 21:37 UTC)

<p>If you know that you only need to load 3D images (no 4D data, no 2D+t data, no DICOM segmentation objects, RT structure sets, etc.) then you can disable all DICOM plugins except the basic scalar volume reader plugin. To do that run these before starting the loading:</p>
<pre><code class="lang-python"># Temporarily remove all DICOM plugins except DICOMScalarVolumePlugin
originalDicomPlugins = slicer.modules.dicomPlugins
slicer.modules.dicomPlugins = {'DICOMScalarVolumePlugin': originalDicomPlugins['DICOMScalarVolumePlugin']}
</code></pre>
<p>and in the end restore the original plugin list by running this:</p>
<pre><code class="lang-python"># Restore original DICOM plugin list
slicer.modules.dicomPlugins = originalDicomPlugins
</code></pre>

---
