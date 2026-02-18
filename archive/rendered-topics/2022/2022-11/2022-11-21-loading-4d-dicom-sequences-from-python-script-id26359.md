# Loading 4D dicom sequences from python script

**Topic ID**: 26359
**Date**: 2022-11-21
**URL**: https://discourse.slicer.org/t/loading-4d-dicom-sequences-from-python-script/26359

---

## Post #1 by @laurabc (2022-11-21 20:30 UTC)

<p>Dear Community,</p>
<p>I am struggling to load my 4D data, in dicom format, using a python script. What I need is something similar to the example in the script repository “Browse a sequence and access currently displayed nodes”, but I am not able to get the sequenceNode. However, I am able to load this sequence using the GUI.<br>
(I am using Slicer 5.0.3 in linux.)</p>
<p>Regards,<br>
Laura</p>

---

## Post #2 by @lassoan (2022-12-01 06:32 UTC)

<p>Does <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-dicom-files-into-the-scene-from-a-folder">this script</a> load the volume sequence?</p>

---

## Post #3 by @laurabc (2022-12-01 11:47 UTC)

<p>No, I get the following error</p>
<p>DICOM plugin failed to load ‘7: ’ as a ‘MultiVolume’.<br>
Traceback (most recent call last):<br>
File “/home/Slicer-5.0.3-linux-amd64/lib/Slicer-5.0/qt-scripted-modules/DICOMLib/DICOMUtils.py”, line 790, in loadLoadables<br>
loadSuccess = plugin.load(loadable)<br>
File “/home/Slicer-5.0.3-linux-amd64/bin/…/lib/Slicer-5.0/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 586, in load<br>
files = mvNode.GetAttribute(‘MultiVolume.FrameFileList’).split(’,')<br>
AttributeError: ‘NoneType’ object has no attribute ‘split’</p>

---

## Post #4 by @lassoan (2022-12-09 20:48 UTC)

<p>Could you please test with the latest Slicer Stable Release?</p>

---

## Post #5 by @laurabc (2022-12-12 09:19 UTC)

<p>I still get an error</p>
<p>[Python] Geometric issues were found with 1 of the series. Please use caution.<br>
[Python] DICOM plugin failed to load ‘Func  DS_CorCTA  0.75  Bv38  3  10 - 100 %  Matriz 256 - as a 10 frames Volume Sequence by CardiacCycle’ as a ‘MultiVolume’.<br>
[Python] Traceback (most recent call last):<br>
[Python]   File “/home/laura/Downloads/Slicer-5.2.1-linux-amd64/lib/Slicer-5.2/qt-scripted-modules/DICOMLib/DICOMUtils.py”, line 790, in loadLoadables<br>
[Python]     loadSuccess = plugin.load(loadable)<br>
[Python]   File “/home/laura/Downloads/Slicer-5.2.1-linux-amd64/bin/…/lib/Slicer-5.2/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 586, in load<br>
[Python]     files = mvNode.GetAttribute(‘MultiVolume.FrameFileList’).split(‘,’)<br>
[Python] AttributeError: ‘NoneType’ object has no attribute ‘split’<br>
[Python] DICOM plugin failed to load ‘Func  DS_CorCTA  0.75  Bv38  3  10 - 100 %  Matriz 256 - as a 10 frames Volume Sequence by ImagePositionPatient+AcquisitionTime’ as a ‘MultiVolume’.<br>
[Python] Traceback (most recent call last):<br>
[Python]   File “/home/laura/Downloads/Slicer-5.2.1-linux-amd64/lib/Slicer-5.2/qt-scripted-modules/DICOMLib/DICOMUtils.py”, line 790, in loadLoadables<br>
[Python]     loadSuccess = plugin.load(loadable)<br>
[Python]   File “/home/laura/Downloads/Slicer-5.2.1-linux-amd64/bin/…/lib/Slicer-5.2/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 586, in load<br>
[Python]     files = mvNode.GetAttribute(‘MultiVolume.FrameFileList’).split(‘,’)<br>
[Python] AttributeError: ‘NoneType’ object has no attribute ‘split’<br>
[Python] DICOM plugin failed to load ‘7: ’ as a ‘MultiVolume’.<br>
[Python] Traceback (most recent call last):<br>
[Python]   File “/home/laura/Downloads/Slicer-5.2.1-linux-amd64/lib/Slicer-5.2/qt-scripted-modules/DICOMLib/DICOMUtils.py”, line 790, in loadLoadables<br>
[Python]     loadSuccess = plugin.load(loadable)<br>
[Python]   File “/home/laura/Downloads/Slicer-5.2.1-linux-amd64/bin/…/lib/Slicer-5.2/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 586, in load<br>
[Python]     files = mvNode.GetAttribute(‘MultiVolume.FrameFileList’).split(’,')<br>
[Python] AttributeError: ‘NoneType’ object has no attribute ‘split’</p>

---

## Post #6 by @lassoan (2022-12-12 17:39 UTC)

<p>OK, I see now. The problem is reported because the code snippet in the script repository tries to load all possible interpretations of the series and once the series is loaded the <code>MultiVolume.FrameFileList</code> attribute is removed and alternative interpretations will fail to load.</p>
<p>You need to use a bit lower level API to load a specific sequence type with a specific plugin:</p>
<pre><code class="lang-python">dicomDataDir = r"c:\tmp\20221212"  # input folder with DICOM files
loadedNodeIDs = []  # this list will contain the list of all loaded node IDs

pluginClass = "MultiVolumeImporterPlugin"
loadableNameSuffix = "Volume Sequence by CardiacCycle"
from DICOMLib import DICOMUtils
with DICOMUtils.TemporaryDICOMDatabase() as db:
    DICOMUtils.importDicom(dicomDataDir, db)
    patientUIDs = db.patients()
    for patientUID in patientUIDs:
        patientUIDstr = str(patientUID)
        # Select all series in selected patient
        studies = slicer.dicomDatabase.studiesForPatient(patientUIDstr)
        series = [slicer.dicomDatabase.seriesForStudy(study) for study in studies]
        seriesUIDs = [uid for uidList in series for uid in uidList]
        fileLists = []
        for seriesUID in seriesUIDs:
            fileLists.append(slicer.dicomDatabase.filesForSeries(seriesUID))
        if len(fileLists) == 0:
            # No files found for DICOM series list
            continue
        loadablesByPlugin, loadEnabled = DICOMUtils.getLoadablesFromFileLists(fileLists, pluginClassNames=[pluginClass])
        # Only select the specific interpretation to load (whice has name that ends with loadableNameSuffix)
        loadablesBySeries = {}
        for plugin in loadablesByPlugin:
            for loadable in loadablesByPlugin[plugin]:
                loadable.selected = loadable.name.endswith(loadableNameSuffix)
        loadedNodeIDs.extend(DICOMUtils.loadLoadables(loadablesByPlugin))
</code></pre>
<p>We offer many cardiac segmentation, modeling, analysis, and surgical planning and navigation tools in SlicerHeart and other extensions; and many more are in the publish-release pipeline. What are your main interests? What Slicer features you would like to use on these image sequences?</p>

---

## Post #7 by @laurabc (2022-12-13 09:56 UTC)

<p>Thank you, this is working. Now that the images are loaded, how can I move across the different time volumes from python?<br>
I’ll check SlicerHeart and the extensions, now we’re exploring what information we can extract from 4D-CTs, I guess once we get familiar with the tools we’ll set defined objectives. Thank you again <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=12" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @lassoan (2022-12-13 13:05 UTC)

<p>Your can find examples for all commonly needed operations in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#sequences">script repository</a>.</p>
<p>Slicer is a very versatile framework, it already contains lots of tools and you can easily integrate more features and customize or extend them, so you can do anything you want. Therefore, it might not suggest any specific topics to work on. If you have any idea of what you may want to do (automatic segmentation, motion analysis, automated quantification, surgical planning, evaluation or simulation of cardiac device placement, valve replacement, virtual reality, etc) then let us know and we can help you getting started with that in Slicer.</p>

---
