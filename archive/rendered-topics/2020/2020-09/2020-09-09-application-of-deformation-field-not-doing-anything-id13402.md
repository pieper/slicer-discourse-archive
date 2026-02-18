# Application of deformation field not doing anything

**Topic ID**: 13402
**Date**: 2020-09-09
**URL**: https://discourse.slicer.org/t/application-of-deformation-field-not-doing-anything/13402

---

## Post #1 by @mmtg (2020-09-09 14:18 UTC)

<p>Hello, I am trying to apply a deformation field to a volume using the BRAINS resample image module but it ends up not doing anything and I am not sure why. Some context is needed:</p>
<p>We are looking at the AAPM TG-132 report and assessing the deformation algorithms at our center compared to gold standard data. As part of this, we are provided a volume, the deformed volume, and the deformation field that was used. I have attached the original dataset. The other dataset can be downloaded here: <a href="https://www.dropbox.com/s/jnyydbcie9bg9fu/TG132P2-1-1%20-%20Dataset%201%20deformed.zip?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/jnyydbcie9bg9fu/TG132P2-1-1%20-%20Dataset%201%20deformed.zip?dl=0</a></p>
<p>The dropbox download contains the deformed image as well as 2 registration dicoms. It is unclear to me why there are two but I tried with both.</p>
<p>In any case my process was as follows:</p>
<ol>
<li>Import the Original dicom, the deformed dicom, and the 2 registrations</li>
<li>Use the BRAINS resample image to apply the transform with the original image as input, a new volume as output, and either of the registrations as the transform</li>
<li>Compare the new image and the original image.</li>
</ol>
<p>Output: They are the same volume with no deformations.</p>
<p>I am wondering if I am running into a memory issue as I am running this on a fairly limited machine. I just didn’t expect it to return a volume in which nothing occurred and no error messages were specified. I also attempted the following:</p>
<p>in the python module in slicer I ran the following commands:<br>
import slicer.util<br>
voxelarray = array(‘<em>SpatialRe</em>’)<br>
print(voxelarray)</p>
<p>which returned None (i.e., the spatial registration is empty?).</p>
<p>I also imported the registration in Matlab and looked at the vector grid header which contains the transform and it was not empty as far as I could tell.</p>
<p>Any help would be great, thanks</p>

---

## Post #2 by @mmtg (2020-09-11 00:40 UTC)

<p>Just curious if there is any additional information I could supply to help resolve this issue. Still stuck on it.</p>

---

## Post #3 by @muratmaga (2020-09-11 01:53 UTC)

<p>It is quite possible that you are not successfully reading deformation fields correctly into Slicer. My cursory examination result in quite a bit of dicom errors importing those two deformation fields into Slicer.</p>
<p>Here are the error logs by the DICOMBrowser, after it asked me to install RT extension.</p>
<pre><code>Warning: Warning: 1811 of 1811 selected files listed in the database cannot be found on disk.

See python console for error message.

W: DcmItem: Dataset not in ascending tag order, at element (0064,0005)

W: DcmItem: Dataset not in ascending tag order, at element (0064,0005)

W: DcmItem: Dataset not in ascending tag order, at element (0064,0005)

W: DcmItem: Dataset not in ascending tag order, at element (0064,0005)

W: DcmItem: Dataset not in ascending tag order, at element (0064,0005)

W: DcmItem: Dataset not in ascending tag order, at element (0064,0005)

MultiVolumeImportPlugin::examine

DICOMMultiVolumePlugin found 0 multivolumes!

MultiVolumeImportPlugin::examine

DICOMMultiVolumePlugin found 0 multivolumes!

MultiVolumeImportPlugin:examineMultiseries

DICOMMultiVolumePlugin found 0 multivolumes!

W: DcmItem: Dataset not in ascending tag order, at element (0064,0005)

Failed to load DICOM registration object from file C:/Users/murat/Downloads/TG132P2-1-1 - Dataset 1 deformed/REG_ImSimQA_20180713.123805.935322.dcm

Could not load: 1: SpatialReg [1] as a REG

Could not load: 1: SpatialReg [1] as a REG

W: DcmItem: Dataset not in ascending tag order, at element (0064,0005)

Failed to load DICOM registration object from file C:/Users/murat/Downloads/TG132P2-1-1 - Dataset 1 deformed/REG_ImSimQA_20180713.123759.932340.dcm

Could not load: 1: SpatialReg [1] as a REG

Could not load: 1: SpatialReg [1] as a REG</code></pre>

---

## Post #4 by @mmtg (2020-09-11 12:06 UTC)

<p>I had forgotten about the error window and see that now. I am not sure what this error means… Does it mean that the file itself is an improperly formed dicom? I think I’ll try and re-create it in matlab as the data loads fine there</p>

---

## Post #5 by @mmtg (2020-09-11 16:42 UTC)

<p>For anyone in the future, note that this is a significant problem with the TG-132 Registration files as supplied. I am not sure what is exactly the issues but it looks like in generating the header data, something went amiss.</p>
<p>To fix this problem, I created a registration between the two datasets, exported this to DICOM and then used pydicom to replace the “DeformableRegistrationSequence” in the created registration file with the TG-132 header information. With this, I was able to load this into 3DSlicer. Even still, I think these deformation fields are not correct but that is a problem with the dataset not slicer.</p>

---

## Post #6 by @lassoan (2020-09-12 04:49 UTC)

<p>What software was used to create the <code>REG_ImSimQA_20180713.123759.932340.dcm</code> and <code>REG_ImSimQA_20180713.123805.935322.dcm</code> files in the zip package?</p>
<aside class="quote no-group" data-username="mmtg" data-post="5" data-topic="13402">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/b5e925/48.png" class="avatar"> mmtg:</div>
<blockquote>
<p>To fix this problem, I created a registration between the two datasets, exported this to DICOM</p>
</blockquote>
</aside>
<p>What software did you use for this?</p>

---

## Post #7 by @mmtg (2020-09-12 11:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="13402" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What software was used to create the <code>REG_ImSimQA_20180713.123759.932340.dcm</code> and <code>REG_ImSimQA_20180713.123805.935322.dcm</code> files in the zip package?</p>
</blockquote>
</aside>
<p>It was the ImSimQA software, I imagine an early version of it. The software package is not free and I am trying to get details on what the problem is. Apparently I am not the only one who has had issues with it including MIMSoftware as well as other authors (see <a href="https://doi.org/10.1002/acm2.12348" rel="noopener nofollow ugc">https://doi.org/10.1002/acm2.12348</a>)</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="6" data-topic="13402" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="mmtg" data-post="5" data-topic="13402">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/b5e925/48.png" class="avatar"> mmtg:</div>
<blockquote>
<p>To fix this problem, I created a registration between the two datasets, exported this to DICOM</p>
</blockquote>
</aside>
<p>What software did you use for this?</p>
</blockquote>
</aside>
<p>I used python with Pydicom. It took about 5 lines to do it this way (just replaced the entire Deformable Registration Sequence field of a dummy dicom with the ImSimQA).</p>
<p>Even with the above, the deformation field doesn’t seem correct. It does not warp the “base” image into the deformed image when using slicer. Even further, while slicer will load this deformation, MIM still won’t (but may be related to memory allocation in settings which I cannot change).</p>

---

## Post #8 by @lassoan (2020-09-12 14:37 UTC)

<p>I’ve checked <code>REG_ImSimQA_20180713.123759.932340.dcm</code> and <code>REG_ImSimQA_20180713.123805.935322.dcm</code> and they are invalid: SOPClassUID is set to <code>SpatialRegistrationStorage</code> but the stored registration is a <code>DeformableRegistrationSequence</code>. For grid transforms, the correct SOPClassUID is <code>DeformableSpatialRegistrationStorage</code>. It is a shame that commercial software developers don’t test their product diligently, as it puts other software developers into a difficult position: Should we add a workaround that allows loading this invalid file, making our code less safe and more complicated? Or keep out software correct and risk losing users because it “does not work” (cannot load a file that other software can load).</p>
<p>Another issue with the file that it stores displacement for every voxel. Since displacement field is smooth, it should be enough to store a vector for every 5th or 10th voxel in the image plane, reducing the image size by a factor of 25x-100x.</p>
<p>I have made SRO reader in SlicerRT more robust (maybe we will even temporarily enable loading of these invalid files). These changes will be available in the Preview Release within a few days.</p>

---

## Post #9 by @lassoan (2020-09-12 17:48 UTC)

<p>Performance and robustness fixes are integrated (will be available in Slicer preview Release from tomorrow). Workaround to enable loading of invalid ImSimQA images is being discussed here: <a href="https://github.com/SlicerRt/SlicerRT/pull/154">https://github.com/SlicerRt/SlicerRT/pull/154</a></p>

---

## Post #10 by @mmtg (2020-09-15 16:44 UTC)

<p>Thank you Andras for going into this - it is really helpful. I am really unsure how this “standard” dataset could be so poorly formed - as I mentioned there are other issues with it.</p>
<p>Thanks again</p>

---

## Post #11 by @mmtg (2020-09-17 12:18 UTC)

<p>Hi Andras,</p>
<p>I tried downloading the Nightly (17/9/2020) and importing the registration file with SlicerRT installed and it still fails to load. I get the following messages:</p>
<blockquote>
<p>Could not load: 1: SpatialReg [1] as a REG<br>
W: DcmItem: Dataset not in ascending tag order, at element (0064,0005)<br>
Warning: In D:\D\P\S-0-E-b\SlicerRT\DicomSroImportExport\Logic\vtkSlicerDicomSroReader.cxx, line 224<br>
vtkSlicerDicomSroReader (0000021E73EC34C0): vtkSlicerDicomS…<br>
Failed to load DICOM registration object from file [removed by mmtg]\REG_ImSimQA_20180713.123759.9323…<br>
Could not load: 1: SpatialReg [1] as a REG</p>
</blockquote>
<p>Not sure if I did something wrong.</p>

---

## Post #12 by @lassoan (2020-09-17 12:25 UTC)

<p>The <a href="https://github.com/SlicerRt/SlicerRT/pull/154">workaround that allowed loading of invalid registration objects created by ImSimQA</a> was not integrated yet. I’ve merged it now, so tomorrow’s Slicer Preview Release will accept these files.</p>

---

## Post #13 by @jhnlbrt (2021-09-22 22:23 UTC)

<p>Hello, <a class="mention" href="/u/mmtg">@mmtg</a>.</p>
<p>How did the Registration Work?<br>
I tried the whole process but the two images didn’t match</p>

---

## Post #14 by @lassoan (2021-09-22 23:54 UTC)

<p>Please post your question in a separate topic and describe in more detail what your overall goal is, and exactly what steps you made, what you expected to happen, and what happened instead.</p>

---
