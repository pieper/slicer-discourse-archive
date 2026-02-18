# Is there any way to import 4D perfusion NIFTI image to DSCMRIAnalysis?

**Topic ID**: 3782
**Date**: 2018-08-15
**URL**: https://discourse.slicer.org/t/is-there-any-way-to-import-4d-perfusion-nifti-image-to-dscmrianalysis/3782

---

## Post #1 by @Kyu_Sung_Choi (2018-08-15 06:59 UTC)

<p>Dear Dr. <a class="mention" href="/u/fedorov">@fedorov</a>, and Dr. <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p><strong>Is there any way to import 4D perfusion NIFTI image to DSCMRIAnalysis?</strong><br>
I understand that currently, only DICOM images can be imported as input to DSCMRIAnalysis module.<br>
However, I want to make some preprocessing (e.g. motion correction, registration) of DICOM images which will be saved as NIFTI files.<br>
So I need to figure out if there is any way to import 4D perfusion NIFTI image to DSCMRIAnalysis.<br>
If it’s impossible, then <strong>could you please tell me how to 1) correct motion artifacts and 2) register to T1 contrast enhanced images with NRRD images that were made from mpReviewPreprocessor.py <em>in batch mode (i.e. in command lines)</em> with appropriate Slicer modules?</strong><br>
Always appreciate your response.<br>
Thank you in advance!</p>
<p>Best,<br>
Kyu Sung</p>

---

## Post #2 by @fedorov (2018-08-15 13:54 UTC)

<p>Please see the answer to this question in this post: <a href="https://discourse.slicer.org/t/how-can-i-import-nifti-files-to-dscmrianalysis-module/3645">How can I import NIFTI files to DSCMRIAnalysis module?</a></p>

---

## Post #3 by @Kyu_Sung_Choi (2018-08-15 23:49 UTC)

<p>Dear Dr. <a class="mention" href="/u/fedorov">@fedorov</a>,</p>
<p>Thanks to your help, I’ve already tried <a class="mention" href="/u/pieper">@pieper</a>’s python code, and it was successful in saving NIFTI files in NRRD files.<br>
However, when I enter these NRRD files as inputs to DSCMRIAnalysis module, then <em><strong>it does not recognize frame identifying DICOM tag</strong></em>  (error msg below).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1ca8e949bac4a54f695f57fbfcbe1b3169d81a2.jpeg" alt="image" data-base62-sha1="tVTLAEfjvK7MeigvkaJhq3aJ3fs" width="690" height="288"></p>
<p>I’ll send you a 4D DSC DICOM as well as NIFTI files in email.<br>
Could you please fix this problem?<br>
I always appreciate it.</p>
<p>All the best,<br>
Kyu Sung</p>

---

## Post #4 by @fedorov (2018-08-17 18:45 UTC)

<p>In the NRRD file you sent me, the attributes that are needed for the analysis are not initialized.</p>
<p>You should specify the following (this is how they are initialized if the DICOM series is imported directly from DICOM for the dataset you shared):</p>
<pre><code class="lang-auto">MultiVolume.FrameIdentifyingDICOMTagName:=Time
MultiVolume.FrameIdentifyingDICOMTagUnits:=ms
</code></pre>
<p>In the MultiVolumeImporter UI, you have place to initialize those:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bef49de041b11ffbe197c9b7bbc65ad482f1253.png" alt="image" data-base62-sha1="3Z7z21ALsHCgNauXFubwnQtoH5x" width="491" height="204"></p>
<p>You can also initialize those programmatically, as done here: <a href="https://github.com/fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporter.py#L276-L277" class="inline-onebox">MultiVolumeImporter/MultiVolumeImporter.py at master · fedorov/MultiVolumeImporter · GitHub</a></p>
<p>It does look like those attributes are not initialized from the GUI when import is done from 4D NIfTI, this is probably a bug that we should fix, but you can also fix this in your custom conversion code.</p>
<p>For now, I captured this in a bug report here: <a href="https://github.com/fedorov/MultiVolumeImporter/issues/33" class="inline-onebox">MV attributes not propagated from GUI when imported from 4D NIfTI · Issue #33 · fedorov/MultiVolumeImporter · GitHub</a></p>

---

## Post #5 by @Kyu_Sung_Choi (2018-08-20 11:57 UTC)

<p>Dear Dr. <a class="mention" href="/u/fedorov">@fedorov</a>,</p>
<p>Thank you so much for your kind information.<br>
I managed to add some lines for the code, and the following result is acquired.</p>
<p>import os<br>
import slicer<br>
import MultiVolumeImporter</p>
<p>path1 = “/home/cndl/DSC/test/4d_nifti/”<br>
path2 = “/home/cndl/DSC/test/nrrd/”<br>
<span class="hashtag-raw">#os</span>.mkdir(path2)<br>
list = os.listdir(path1)</p>
<p>for filename in sorted(list):<br>
importer = MultiVolumeImporter.MultiVolumeImporterWidget()</p>
<p>mvNode = slicer.mrmlScene.CreateNodeByClass(‘vtkMRMLMultiVolumeNode’)<br>
slicer.mrmlScene.AddNode(mvNode)</p>
<p>importer.read4DNIfTI(mvNode, path1+filename)<br>
mvNode.SetAttribute(‘MultiVolume.FrameIdentifyingDICOMTagName’,‘Time’)<br>
mvNode.SetAttribute(‘MultiVolume.FrameIdentifyingDICOMTagUnits’,‘ms’)<br>
mvNode.SetAttribute(‘MultiVolume.DICOM.FlipAngle’,‘1.00’)<br>
mvNode.SetAttribute(‘MultiVolume.DICOM.EchoTime’,‘1.00’)<br>
mvNode.SetAttribute(‘MultiVolume.DICOM.RepetitionTime’,‘1.00’)<br>
fn_ext = os.path.splitext(filename)<br>
true_fn_ext = os.path.splitext(fn_ext[0])<br>
slicer.util.saveNode(mvNode, path2+true_fn_ext[0]+“.nrrd”)</p>
<p>exit()</p>
<p>(I’ve set all the additional information such as FlipAngle, EchoTime, and RepititionTime as ‘1.00’, which is default values of MultiVolumeImporter GUI.)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4386d3066df0650776b9a6439007c66cca1e6f20.png" data-download-href="/uploads/short-url/9DmQIv8BDLBKliVzYpSpsoKz6rS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4386d3066df0650776b9a6439007c66cca1e6f20.png" alt="image" data-base62-sha1="9DmQIv8BDLBKliVzYpSpsoKz6rS" width="690" height="117" data-dominant-color="131314"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1419×242 11.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
(Timing: values are seemed to be multiples of 0.00155, i.e. 0.00155 x 0, 1, 2, …, 95, which is the number of time points)</p>
<p>However, the “Timing:” seems a bit different from what I’ve got from the mpReviewPreprocessor.py.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa19b2d7934d3ce8a398dceebcf7152dd1647c7d.png" data-download-href="/uploads/short-url/zGuqrTOeK4Mx3nMussiaZq6ymfP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa19b2d7934d3ce8a398dceebcf7152dd1647c7d.png" alt="image" data-base62-sha1="zGuqrTOeK4Mx3nMussiaZq6ymfP" width="690" height="81" data-dominant-color="090909"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1419×167 6.24 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
(Timing:0,1,2,3,4,)</p>
<p>The resultant CBV map obtained from DSCMRIAnalysis is attached below.</p>
<ol>
<li>
<p>with NRRD from read4DNIfTI<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23a247a4cf067f0857228cd9d56f199aa9171972.jpeg" alt="image" data-base62-sha1="55eosiExoOlvAPkAiVWAPsKIru2" width="442" height="413"></p>
</li>
<li>
<p>with NRRD from mpReviewPreprocessor.py<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d8cf35e53842c06da89ef5b342db9abc17c3c08.jpeg" alt="image" data-base62-sha1="kcdj8JV45dnHv1vaz1qIxYGbkUw" width="455" height="425"></p>
</li>
</ol>
<p>I think 1), and 2) images are a bit different.<br>
<strong>Do you think it’s the problem of setting the FlipAngle, EchoTime, and RepititionTime as ‘1.00’?</strong><br>
<em>However, I’ve changed them to 90,40,1900, which are true values from DICOM header information, and it didn’t make any difference.</em><br>
Thank you in advance!</p>
<p>All the best,<br>
Kyu Sung</p>

---

## Post #6 by @fedorov (2018-08-20 16:44 UTC)

<p>You should also initialize frame labels:</p>
<ul>
<li><a href="https://github.com/fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporter.py#L223-L229">https://github.com/fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporter.py#L223-L229</a></li>
<li><a href="https://github.com/fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporter.py#L274-L277">https://github.com/fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporter.py#L274-L277</a></li>
</ul>
<p>All of this metainformation is not populated when importing 4d NIFTI. If you know the correct timing of the acquisition, you should change the default value of 1.</p>
<p>You should also populate the relevant DICOM attributes if you know them.</p>

---
