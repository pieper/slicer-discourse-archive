# How can I import NIFTI files to DSCMRIAnalysis module?

**Topic ID**: 3645
**Date**: 2018-08-03
**URL**: https://discourse.slicer.org/t/how-can-i-import-nifti-files-to-dscmrianalysis-module/3645

---

## Post #1 by @Kyu_Sung_Choi (2018-08-03 12:05 UTC)

<p>Dear Dr. Fedorov,</p>
<p>I’ve decided to correct motion of 4D DSC dicom files.<br>
However, after motion correction,  the 4D DSC dicom files should be in NIFTI format.<br>
So I saved the NIFTI output file into NRRD file using slicer.util.loadVolume, and slicer.util.saveNode using Python.<br>
However, I can’t load 4D images using slicer.util.loadVolume.<br>
<strong>Could you please make NIFTI files imported to DSCMRIAnalysis module as well as DICOM files?</strong><br>
<em>I tried to do it on my own using Python script, which did not work well.</em><br>
I referred to this <a href="https://discourse.slicer.org/t/how-to-load-4d-images-in-slicer-fmri-or-asl-datasets/1157/21">post</a> and <a href="https://github.com/fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporter.py#L190-L192" rel="noopener nofollow ugc">link</a>.<br>
If it’s impossible, then I’m gonna trying to do it by myself, but I think I need your hint.</p>
<p>So sorry to bother you again.<br>
Thank you for your help!</p>
<p>Best,<br>
Kyu Sung</p>

---

## Post #2 by @fedorov (2018-08-03 21:40 UTC)

<p>Recently we added a functionality that allows import of 4D NIfTI as MultiVolumes. It has not been thoroughly tested, so it would be great if you could try it out and see if it helps.</p>
<p>To use it, you will need to place your 4D NIfTI file into a separate directory, and use MultiVolumeImporter module. Since your NIfTI file will not contain the metadata needed for the analysis (such as timing information), you will need to use MultiVolumeImporter to initialize those.</p>
<p>If the import is working for you from the GUI, you could then look into <a href="https://github.com/fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporter.py#L309">this function</a> to automate the load process.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> added this functionality to MultiVolumeImporter, so I cc him here so that he can follow the conversation.</p>
<p>p.s. In the future, if you want to bring my attention to your post, you should mention me with <a class="mention" href="/u/fedorov">@fedorov</a> - this way I will receive notification about your message. I do not regularly check all posts on the forum, so just mentioning my name does not mean I will read your message!</p>

---

## Post #3 by @Kyu_Sung_Choi (2018-08-09 13:20 UTC)

<p>Dear Dr. <a class="mention" href="/u/fedorov">@fedorov</a> ,</p>
<p>Following your instruction, the import of a 4D NIFTI file did work for me from the GUI.<br>
However, I cannot make python file to load 4D NIFTI file and save as NRRD file.<br>
A simple python code I wrote to load a 3D NIFTI file to save as a NRRD file is attached below (actually, I am quite a beginner to python), which works good for me.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/372032603bfcd700b6c44a88be0fd7d7f2c81fd7.png" data-download-href="/uploads/short-url/7RFf0RqMIExWUavTGRq9xHrK8JN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/372032603bfcd700b6c44a88be0fd7d7f2c81fd7.png" alt="image" data-base62-sha1="7RFf0RqMIExWUavTGRq9xHrK8JN" width="690" height="103" data-dominant-color="0D0D0D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1403×211 12.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">import os 
import slicer 

path1 = "/home/cndl/DSC/test/3d_nifti/"
path2 = "/home/cndl/DSC/test/nrrd/"
os.mkdir(path2)
list = os.listdir(path1)

for filename in sorted(list):
  [success, loadedVolumeNode] = slicer.util.loadVolume(path1+filename, returnNode=True)
  fn_ext = os.path.splitext(filename)
  true_fn_ext = os.path.splitext(fn_ext[0])
  slicer.util.saveNode(loadedVolumeNode, path2+true_fn_ext[0]+".nrrd")

exit()
</code></pre>
<p>So I tried to write similar codes with the <a href="https://github.com/fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporter.py#L46" rel="noopener nofollow ugc">function</a> you mentioned.<br>
In the function, “read4DNIfTI” was the method of class “MultiVolumeImporterWidget”, so I wrote like,</p>
<pre><code class="lang-auto">import os 
import slicer 

path1 = "/home/cndl/DSC/test/4d_nifti/"
path2 = "/home/cndl/DSC/test/nrrd/"
os.mkdir(path2)
list = os.listdir(path1)

for filename in sorted(list):
  [success, loadedVolumeNode] = slicer.util.loadVolume(path1+filename, returnNode=True)
  mvNode = MultiVolumeImporterWidget.read4DNIfTI(loadedVolumeNode, path1+filename)
  fn_ext = os.path.splitext(filename)
  true_fn_ext = os.path.splitext(fn_ext[0])
  slicer.util.saveNode(mvNode , path2+true_fn_ext[0]+".nrrd")

exit()
</code></pre>
<p>,which gave me an error that ‘MultiVolumeImporterWidget’ is not defined.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/657dce54470a594227622e95bee55d5519c5c949.png" data-download-href="/uploads/short-url/etPLhjSNsv0Mw9gZer6rQ8nDtFL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/657dce54470a594227622e95bee55d5519c5c949.png" alt="image" data-base62-sha1="etPLhjSNsv0Mw9gZer6rQ8nDtFL" width="690" height="116" data-dominant-color="10100F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1112×187 9.88 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I know there are a lot of mistakes in the code, which I can’t fix.<br>
<strong>Could you please help me fix this code?</strong></p>
<p>All the best,<br>
Kyu Sung</p>

---

## Post #4 by @fedorov (2018-08-09 18:06 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> could you help <a class="mention" href="/u/kyu_sung_choi">@Kyu_Sung_Choi</a> with programmatically invoking the 4d NIfTI read function you wrote?</p>

---

## Post #5 by @pieper (2018-08-09 21:27 UTC)

<p>The MultiVolumeImporter doesn’t have a Logic class, the code below creates the widget and then runs the converter.  It’s a little ugly but it looks like it works (I don’t have any 4D nii data to try but it works on a 3D volume).  If you find you are doing a lot of this and don’t like the widget popping up then you could easily refactor this method for use outside of the widget.</p>
<pre><code class="lang-auto">import os 
import slicer 

import MultiVolumeImporter

importer = MultiVolumeImporter.MultiVolumeImporterWidget()


mvNode = slicer.mrmlScene.CreateNodeByClass('vtkMRMLMultiVolumeNode')
slicer.mrmlScene.AddNode(mvNode)

niiFilePath = "/Users/pieper/data//prostate-MR-US/MRProstate.nii"

importer.read4DNIfTI(mvNode, niiFilePath)

slicer.util.saveNode(mvNode , "/tmp/converted.nrrd")

exit()
</code></pre>

---

## Post #6 by @Kyu_Sung_Choi (2018-08-10 03:19 UTC)

<p>Dear Dr. <a class="mention" href="/u/pieper">@pieper</a> and Dr. <a class="mention" href="/u/fedorov">@fedorov</a>,</p>
<p><strong>Thank you so much!</strong><br>
<strong>It works perfectly, and moreover, I think reading multiple DSC files in the folder works fine with the code below.</strong> (There are a few warnings, though.)</p>
<p>import os<br>
import slicer<br>
import MultiVolumeImporter</p>
<p>path1 = “/home/cndl/DSC/test/4d_nifti/”<br>
path2 = “/home/cndl/DSC/test/nrrd/”<br>
os.mkdir(path2)<br>
list = os.listdir(path1)</p>
<p>for filename in sorted(list):<br>
#[success, loadedVolumeNode] = slicer.util.loadVolume(path1+filename, returnNode=True) ## for 3D NIFTI<br>
importer = MultiVolumeImporter.MultiVolumeImporterWidget()</p>
<p>mvNode = slicer.mrmlScene.CreateNodeByClass(‘vtkMRMLMultiVolumeNode’)<br>
slicer.mrmlScene.AddNode(mvNode)</p>
<p>importer.read4DNIfTI(mvNode, path1+filename)<br>
fn_ext = os.path.splitext(filename)<br>
true_fn_ext = os.path.splitext(fn_ext[0])<br>
slicer.util.saveNode(mvNode, path2+true_fn_ext[0]+“.nrrd”)</p>
<p>exit()</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35b234170779e4786673e23ee00cebcb3590c55c.png" data-download-href="/uploads/short-url/7F16w5jku62ho0PRqGLKMbcyd7C.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35b234170779e4786673e23ee00cebcb3590c55c.png" alt="image" data-base62-sha1="7F16w5jku62ho0PRqGLKMbcyd7C" width="690" height="281" data-dominant-color="131313"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1076×439 18 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong><em>However, after I load these 3 NRRD files (test_DSC, test2_DSC, and TCGA-08-0524_DSC.nrrd) and enter as input to DSCMRIAnalysis module in command line, it does not recognize frame identifying DICOM tag</em></strong> (error msg below). When I enter just 1 NRRD file saved with the code above as an input file, same error msg pops up. Maybe this NRRD file is not the same NRRD file that I obtained using mpReviewPreprocessor.py (the post you answer is linked <a href="https://discourse.slicer.org/t/how-can-i-convert-dicom-series-to-nrrd-files-in-batch-mode/3421/9">here</a>)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5389aa06ab1967604e5a10569fc6d69ef26733f7.png" data-download-href="/uploads/short-url/bV0zB48ZHHZYwy3CMusFPCxgEpV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5389aa06ab1967604e5a10569fc6d69ef26733f7.png" alt="image" data-base62-sha1="bV0zB48ZHHZYwy3CMusFPCxgEpV" width="690" height="288" data-dominant-color="090909"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1413×591 25.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you please fix this problem?<br>
I always appreciate it.</p>
<p>All the best,<br>
Kyu Sung</p>

---

## Post #7 by @kristjanq (2020-04-24 20:25 UTC)

<p>I need to make a volume reconstruction evaluation form:  Imagedata.nii,  transformdata.npy and timespampdata.npy. These data are collected form tracked ultrasound images using PLUS libraray.</p>
<p>I am not being able on getting around this problem. I tried MultivolumeImporter volume giving the directory of imagedata.nii and transformdata.npy, but there is an error coming out: Select outpot node… after I created a new node! I know it is possible to merge all above mentioned data into one nrrd file, but I am not that experienced in programming!</p>
<p>Thank you!</p>

---

## Post #8 by @lassoan (2020-04-24 21:45 UTC)

<p>PLUS toolkit does not use nifti or npy file formats. How did you create these images?</p>
<p>Anyway, if you can save your data in PLUS sequence file format (.mha or .nrrd) and install SlicerIGSIO extension then you can load the files into Slicer (by drag-and-drop or “Add data”) and reconstruct it using “Volume Reconstruction” module.</p>

---

## Post #9 by @kristjanq (2020-04-24 22:03 UTC)

<p>Thank you for your reply!</p>
<p>I have been working with “SlicerIGSIO”  and “Volume Reconstruction” modules, but with .nrrd files (generated from PLUS toolkit, as you mentioned)!</p>
<p>The data output from the PLUS toolkit was .nrrd file format. After recording, the data was converted to .npy (transform data and timestamps) and .nii (image data) for storage and transmission feasibility. Is it possible to make such a merge of data in Slicer or through Python Interactor in Slicer?</p>

---

## Post #10 by @lassoan (2020-04-24 22:40 UTC)

<p>It is probably easier to write the content of your nii/npy files back to a nrrd/nhdr file. It has a simple text file header, followed by images as a binary blob - complete specification is available <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceFile.html">here</a>.</p>
<p>Nifti (.nii) file format is developed specifically for functional brain imaging and not well suited for any other application areas. There seems to be a confusion among machine learning people and they use it for all kinds of images, but don’t follow them.</p>
<p>Npz is not widely supported by anything else than numpy, but there seem to be some relatively lightweight npz file readers/writers in C++ (<a href="https://github.com/ceptontech/cnpy">https://github.com/ceptontech/cnpy</a>, <a href="https://github.com/pmontalb/NpyCpp">https://github.com/pmontalb/NpyCpp</a>), so we may consider supporting a numpy-based file format in the future. PLUS supports compressed streaming writing of tracked image data, which may not be feasible with npz though, so it may not be that easy to fully switch to that in PLUS/IGSIO.</p>
<p>For now, I think sequence meta/nrrd files are still your best bet for exchanging and archiving tracked image data (of course you can convert them into other formats during a processing workflow).</p>

---

## Post #11 by @kristjanq (2020-04-24 23:10 UTC)

<p>I also thought <code>meta/nrrd</code> is the best option. A module supporting Nifti format would be great tho!</p>
<p>Thanks for the support!</p>

---

## Post #12 by @lassoan (2020-04-24 23:18 UTC)

<p>Nifti header cannot contain more than a couple of bytes of custom data, so it cannot be used for storing tracked image data. Neuroimaging people use json sidecar files as a workaround, but that’s quite inconvenient and error-prone. Nifti has other limitations, too, and lots of complexities that are only necessary if someone is storing neuro MRI images. So, I don’t think we’ll add support for it in PLUS/IGSIO.</p>

---
