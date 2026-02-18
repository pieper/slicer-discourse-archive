# How to load one specific series of a DICOM scanning in Python

**Topic ID**: 34448
**Date**: 2024-02-21
**URL**: https://discourse.slicer.org/t/how-to-load-one-specific-series-of-a-dicom-scanning-in-python/34448

---

## Post #1 by @paleomariomm (2024-02-21 09:54 UTC)

<p>Hi everyone.</p>
<p>I have an issue when loading DICOM files.</p>
<p>I have this code, which iteratively opens different scannings of baboon skulls placed in different folders:</p>
<pre><code class="lang-auto">import os
from DICOMLib import DICOMUtils

yourpath = r"C:/Users/mario.modesto/Desktop/TEST DICOM SLICE"

# walk through DICOM directory
# https://stackoverflow.com/questions/77865010/run-python-script-in-each-subfolder-automatically
for dir in os.scandir(yourpath):
    # Load DICOM files
    dicomDataDir = dir.path  # path to input folder with DICOM files
    baboon_skull  = dir.name
    loadedNodeIDs = []  # this list will contain the list of all loaded node IDs

    # 1. Load DICOM files
    # https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#dicom
    with DICOMUtils.TemporaryDICOMDatabase() as db:
        DICOMUtils.importDicom(dicomDataDir, db)
        patientUIDs = db.patients()
        for patientUID in patientUIDs:
            loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
    
    # 2. Load volume
    # https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#display-volume-using-volume-rendering
    logic = slicer.modules.volumerendering.logic()
    volumeNode = slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode1')
</code></pre>
<p>I have 95 baboon scans (therefore 95 subfolders), and each scan has two series:</p>
<ol>
<li>A  topogram (512x512x1)</li>
<li>Facial bones (512x512x288*) (*although 288 varies from one skull to another)</li>
</ol>
<p>As an example, next image shows only three baboon scans already loaded</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06045f62301322c5d716fcbe1ba6db887944930b.png" data-download-href="/uploads/short-url/ReerScldRZtXVWj2BHiwnBmTij.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06045f62301322c5d716fcbe1ba6db887944930b_2_690x258.png" alt="image" data-base62-sha1="ReerScldRZtXVWj2BHiwnBmTij" width="690" height="258" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06045f62301322c5d716fcbe1ba6db887944930b_2_690x258.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06045f62301322c5d716fcbe1ba6db887944930b_2_1035x387.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06045f62301322c5d716fcbe1ba6db887944930b_2_1380x516.png 2x" data-dominant-color="E9EFF3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2701×1010 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The point in here is that the series which is loaded is always the TOPOGRAM.</p>
<p>So my question is: how can I edit the previous code to import the FACIAL BONES when loading DICOM files rather than the TOPOGRAM?</p>
<p>If you could edit the previous code to adapt this requirement, I would be greatly appreciated.</p>

---

## Post #2 by @pieper (2024-02-21 15:42 UTC)

<p>The <code>loadedNodeIDs</code> will have a list of the ids of all nodes corresponding to that set of dicom instances (based on the default best interpretation).  Instead of using the hard-coded <code>vtkMRMLScalarVolumeNode1</code> as the id, you can use the loaded ids to iterate through the nodes that were loaded.  You can either introspect the name of the node, which is based on the series description, or your an use the node attributes that map slices from a volume back to dicom <code>SOPInstanceUID</code>s that can be used with the dicom database to get any of the instance header values, from which you can decide which series has the data you want.</p>

---

## Post #3 by @paleomariomm (2024-02-23 15:24 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="34448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><code>loadedNodeIDs</code></p>
</blockquote>
</aside>
<p>Thanks for your tip <a class="mention" href="/u/pieper">@pieper</a> .</p>
<p>I walked through and now I solved the problem by adding an if/else statement.</p>
<p>I copy here the code I used in case anyone in the future gets into this question:</p>
<pre><code class="lang-auto">import os
from DICOMLib import DICOMUtils

yourpath = r"C:/Users/mario.modesto/Desktop/TEST DICOM SLICE"
# yourpath = r"D:/Baboons/slice"

# walk through DICOM directory
# https://stackoverflow.com/questions/77865010/run-python-script-in-each-subfolder-automatically
for dir in os.scandir(yourpath):
    # Load DICOM files
    dicomDataDir = dir.path  # path to input folder with DICOM files
    baboon_skull  = dir.name
    loadedNodeIDs = []  # this list will contain the list of all loaded node IDs

    # 1. Load DICOM files
    # https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#dicom
    with DICOMUtils.TemporaryDICOMDatabase() as db:
        DICOMUtils.importDicom(dicomDataDir, db)
        patientUIDs = db.patients()
        for patientUID in patientUIDs:
            loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
    print(loadedNodeIDs)
    print(len(loadedNodeIDs))

    # 2. Load volume
    # https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#display-volume-using-volume-rendering
    logic = slicer.modules.volumerendering.logic()
    # This "if-else" is to select the second volume to skip the Topogram, which is the first
    if len(loadedNodeIDs) == 2:
      volumeNode = slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode2')
    else:
      volumeNode = slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode1')
</code></pre>
<p>With <code>print(loadedNodeIDs)</code> and <code>print(len(loadedNodeIDs))</code> I was able to see which and how many volumes I was having in the scanning. I had two: <code>vtkMRMLScalarVolumeNode1</code> and <code>vtkMRMLScalarVolumeNode2</code>.</p>
<p>This is why in the last part of the code I added an <code>if/else</code> statement.</p>
<p>Hope this is helpful</p>

---
