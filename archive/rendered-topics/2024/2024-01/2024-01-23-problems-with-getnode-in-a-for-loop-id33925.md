# Problems with getNode in a for loop

**Topic ID**: 33925
**Date**: 2024-01-23
**URL**: https://discourse.slicer.org/t/problems-with-getnode-in-a-for-loop/33925

---

## Post #1 by @paleomariomm (2024-01-23 12:04 UTC)

<p>I have a <code>for</code> loop that:</p>
<ul>
<li>load DICOM files in subfolders</li>
<li>show volume rendering of each CT</li>
<li>segment using thresholding</li>
<li>save in ply format</li>
</ul>
<p>The way I develop the <code>for</code> loop is:</p>
<pre><code class="lang-auto">import os
from DICOMLib import DICOMUtils

yourpath = r"C:/Users/mario.modesto/Desktop/DICOM"

#walk through DICOM directory
for dir in os.scandir(yourpath):
    # Load DICOM files
    dicomDataDir = dir.path  # path to input folder with DICOM files
    baboon_skull  = dir.name
    loadedNodeIDs = []  # this list will contain the list of all loaded node IDs

    with DICOMUtils.TemporaryDICOMDatabase() as db:
        DICOMUtils.importDicom(dicomDataDir, db)
        patientUIDs = db.patients()
        for patientUID in patientUIDs:
            loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
    # Display volume rendering
    # https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#display-volume-using-volume-rendering
    logic = slicer.modules.volumerendering.logic()
    volumeNode = slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode1')
    displayNode = logic.CreateVolumeRenderingDisplayNode()
    displayNode.UnRegister(logic)
    slicer.mrmlScene.AddNode(displayNode)
    volumeNode.AddAndObserveDisplayNodeID(displayNode.GetID())
    logic.UpdateDisplayNodeFromVolumeNode(displayNode, volumeNode)
    
    # find the files NodeID
    volumeNode = getNode('2: Facial Bones  0.75  H70h')

&lt; more code here - not all displayed &gt;
</code></pre>
<p>As you can see, each CT has a volume called <code>2: Facial Bones  0.75  H70h</code>, and can be seen in the last line of previous code.</p>
<p>If I have 3 CTs in the DICOM directory, as in here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a84a1a00915d430e2b53dea7195a579c30780d7c.png" data-download-href="/uploads/short-url/o0KYzhgagLZYKO97yn7Z0xKFH3u.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a84a1a00915d430e2b53dea7195a579c30780d7c_2_690x419.png" alt="image" data-base62-sha1="o0KYzhgagLZYKO97yn7Z0xKFH3u" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a84a1a00915d430e2b53dea7195a579c30780d7c_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a84a1a00915d430e2b53dea7195a579c30780d7c_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a84a1a00915d430e2b53dea7195a579c30780d7c.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1208×735 52.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I run the full code, I have three <code>*.ply</code> files in that directory with exactly the same size:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40ab98f54cdd5f698bb98532801d901253968eb7.png" data-download-href="/uploads/short-url/9e6cEkTAENdWYxNUohMI6GelWOX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40ab98f54cdd5f698bb98532801d901253968eb7_2_690x282.png" alt="image" data-base62-sha1="9e6cEkTAENdWYxNUohMI6GelWOX" width="690" height="282" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40ab98f54cdd5f698bb98532801d901253968eb7_2_690x282.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40ab98f54cdd5f698bb98532801d901253968eb7_2_1035x423.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40ab98f54cdd5f698bb98532801d901253968eb7_2_1380x564.png 2x" data-dominant-color="F6F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1490×610 57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The subject hierarchy is this one:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42d07173a05fbb79ca8a76af2463ba6540e65bf6.png" data-download-href="/uploads/short-url/9x46efTK8CwtIOQgrBtgRQcfqHs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42d07173a05fbb79ca8a76af2463ba6540e65bf6_2_405x500.png" alt="image" data-base62-sha1="9x46efTK8CwtIOQgrBtgRQcfqHs" width="405" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42d07173a05fbb79ca8a76af2463ba6540e65bf6_2_405x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42d07173a05fbb79ca8a76af2463ba6540e65bf6_2_607x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42d07173a05fbb79ca8a76af2463ba6540e65bf6_2_810x1000.png 2x" data-dominant-color="F6F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1046×1289 60.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you can see, the volumes of W102 and W103 were renamed with <code>2: Facial Bones  0.75  H70h_1</code> and <code>2: Facial Bones  0.75  H70h_2</code> and inserted in the first skull [1X3805 (101)].</p>
<p>Obviously, the three <code>*.ply</code> files are the same skull (the first one).</p>
<p>I am almost sure that the problem comes from the name of the volume in the last line of the code I copied above:</p>
<p><code>volumeNode = getNode('2: Facial Bones  0.75  H70h')</code></p>
<p>Then the loop goes to the second it works only with that volume and not with the other two that were renamed.</p>
<p>Any suggestion to solve this?</p>

---

## Post #2 by @lassoan (2024-01-23 23:16 UTC)

<p>It seems that you have not changed the source volume in the segment editor but you segmented the same image 3 times.</p>
<p>If you are processing independent subjects then it makes sense to clear the scene after each subject.</p>

---

## Post #3 by @paleomariomm (2024-01-24 08:10 UTC)

<p>Thanks for the tip, it worked!</p>
<p>I added the next code as the last line:</p>
<p><code>slicer.mrmlScene.Clear(0)</code></p>

---
