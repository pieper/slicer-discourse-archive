# ParaToSPHARMMesh completed with errors on win10

**Topic ID**: 4814
**Date**: 2018-11-20
**URL**: https://discourse.slicer.org/t/paratospharmmesh-completed-with-errors-on-win10/4814

---

## Post #1 by @lxgwd1983 (2018-11-20 14:44 UTC)

<p>Operating system:win 10<br>
version:SlicerSALT 1.1.0-2018-10-25</p>
<p>I use the example data download from the web. The output of  step1 and   step2 are correct. but I meet an error on step3. there isn’t any more debug information about this error. is there anybody meets the same problem?<br>
The flowing is the running information and the example data name.</p>
<p>debug imformation<br>
D:/Program Files/SlicerSALT/bin/…/lib/SlicerSALT-4.9/cli-modules/ParaToSPHARMMeshCLP.exe --subdivLevel 10 --spharmDegree 15 --thetaIteration 100 --phiIteration 100 --paraOut --FinalFlip 0 C:/Users/X711/AppData/Local/Temp/SlicerSALT/GAEI_vtkMRMLModelNodeG.vtp C:/Users/X711/AppData/Local/Temp/SlicerSALT/GAEI_vtkMRMLModelNodeH.vtp D:/Program Files/SlicerSALT/data/OutData/Step3_ParaToSPHARMMesh/InputImage_pp_surf<br>
ParaToSPHARMMesh terminated with an unknown exception.</p>
<p>data name<br>
Aim 2.0. SPHARM-PDM00</p>

---

## Post #2 by @bpaniagua (2018-12-16 14:32 UTC)

<p>Hi,</p>
<p>We have uploaded new nightly packages to our SlicerSALT repository.<br>
Could you please try this one and let us know how it goes?<br>
<a href="https://data.kitware.com/#item/5c13c83b8d777f2179ea5d1f" class="onebox" target="_blank" rel="nofollow noopener">https://data.kitware.com/#item/5c13c83b8d777f2179ea5d1f</a></p>
<p>Thank you,<br>
Beatriz</p>

---

## Post #3 by @Maugust (2019-01-15 22:53 UTC)

<p>Hi Beatriz,</p>
<p>I was having the same problem. I downloaded the nightly packages using the link you posted, but the ParaToSPHARMMesh step was once again completed with errors.<br>
I have attached the screenshot of the error (the file names do not correspond to patient data as this project does not involve any):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7cff0165e9b03b6f40d6bda577b0c94ba5224f6.jpeg" data-download-href="/uploads/short-url/qe4SFSxRzcZqmm3DrLYu5PMfT70.jpeg?dl=1" title="ParatoSpharmMesh%20Error%202" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7cff0165e9b03b6f40d6bda577b0c94ba5224f6_2_666x500.jpeg" alt="ParatoSpharmMesh%20Error%202" data-base62-sha1="qe4SFSxRzcZqmm3DrLYu5PMfT70" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7cff0165e9b03b6f40d6bda577b0c94ba5224f6_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7cff0165e9b03b6f40d6bda577b0c94ba5224f6_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7cff0165e9b03b6f40d6bda577b0c94ba5224f6_2_1332x1000.jpeg 2x" data-dominant-color="4E504E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ParatoSpharmMesh%20Error%202</span><span class="informations">1548×1161 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Steps SegPostProcess and GenParaMesh completed without any errors.</p>
<p>Thank you very much.</p>

---

## Post #4 by @bpaniagua (2019-01-28 20:49 UTC)

<p>Dear Marcellus,</p>
<p>Sorry for the delay in responding. Thank you for reporting this problem. The names do not match patient data because commandline reports the names of the nodes in the Slicer MRML scene.</p>
<p>In order to diagnose the problem, could you please let us know the contents of the three subfolders in the output folder?</p>
<p>Thanks!<br>
Bea</p>

---

## Post #5 by @oradzins (2019-01-29 08:24 UTC)

<p>Dear Beatriz,</p>
<p>I will just chime in on the conversation as I have had the same issue since I tried using the module. I’ve attached an image from the error log showing the saved files, once the ParaToSPHARMMesh fails, as in the last step does not generate any new files whatsoever. As Marcellus mentioned, SegPostProcess and GenParaMesh runs flawlessly. Just to add, I used the available tutorial data for this example, but attempting the process with my own data leads to the same results.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec4bb8c423d8bbfbbb892aa3b2854aaccd2fa00c.png" data-download-href="/uploads/short-url/xImUNx6nNM2clVUs5mRLW5Ddsde.png?dl=1" title="6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec4bb8c423d8bbfbbb892aa3b2854aaccd2fa00c.png" alt="6" data-base62-sha1="xImUNx6nNM2clVUs5mRLW5Ddsde" width="690" height="321" data-dominant-color="D7E4EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">6</span><span class="informations">1205×561 36.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Regards,<br>
Oskars</p>

---

## Post #6 by @bpaniagua (2019-01-29 13:37 UTC)

<p>Hi <a class="mention" href="/u/maugust">@Maugust</a> and <a class="mention" href="/u/oradzins">@oradzins</a></p>
<p>I see, that is weird. Oskars, does your problem also happen in Windows 10?<br>
The problem might be coming from the module or from the ParaToSPHARMMesh executable itself. Could one of you please send the *para.vtk and the *surf.vtk files that produce the problem? I will try to diagnose on my end.</p>
<p>Thank you,<br>
Bea</p>

---

## Post #7 by @oradzins (2019-01-29 13:55 UTC)

<p>Dear Beatriz,<br>
I’ve added a zip file containing the generated output data from the tutorial example I mentioned previously below (should eb available for the next 30 days):</p>
<p><a href="https://ufile.io/6vs6r" class="onebox" target="_blank" rel="noopener nofollow ugc">https://ufile.io/6vs6r</a></p>
<p>It ran through about 20 iterations or so, just to create a quick example, but am fairly certain more iterations just prolonged the process and ran into the same error anyway.</p>
<p>I do indeed run windows 10 (Version 1803, OS build 17134.471 if that is of any help). Also the problem has persisted in both SlicerSalt versions 1.0.0 and 1.1.0.</p>
<p>Let me know if there is anything else I can help with.</p>
<p>Regards,<br>
Oskars</p>

---

## Post #8 by @Maugust (2019-01-29 14:59 UTC)

<p>Dear <a class="mention" href="/u/bpaniagua">@bpaniagua</a>,</p>
<p>Here are the links to the outputs from steps 1 and 2 (step 3 just produced an empty output folder):<br>
<a href="https://ufile.io/998r0" class="onebox" target="_blank" rel="noopener nofollow ugc">https://ufile.io/998r0</a><br>
<a href="https://ufile.io/4hgu8" class="onebox" target="_blank" rel="noopener nofollow ugc">https://ufile.io/4hgu8</a><br>
<a href="https://ufile.io/jj397" class="onebox" target="_blank" rel="noopener nofollow ugc">https://ufile.io/jj397</a></p>
<p>Kind regards,<br>
Marcellus</p>

---

## Post #9 by @bpaniagua (2019-01-31 18:38 UTC)

<p>Hi Marcellus and Oskars</p>
<p>ParaToSPHARMMesh completes in Linux.<br>
See results here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/405341ebdfa574c45f19fd3b5ef1f95785921ab5.png" data-download-href="/uploads/short-url/9b2W3S7fTp9TEPoV3gUDaAFTgpf.png?dl=1" title="image%20(1)"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/405341ebdfa574c45f19fd3b5ef1f95785921ab5_2_690x257.png" alt="image%20(1)" data-base62-sha1="9b2W3S7fTp9TEPoV3gUDaAFTgpf" width="690" height="257" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/405341ebdfa574c45f19fd3b5ef1f95785921ab5_2_690x257.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/405341ebdfa574c45f19fd3b5ef1f95785921ab5_2_1035x385.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/405341ebdfa574c45f19fd3b5ef1f95785921ab5.png 2x" data-dominant-color="2E214B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image%20(1)</span><span class="informations">1246×465 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a7e5fdc72a39068b69ae6e843c064ff1578cc36.png" alt="image" data-base62-sha1="8lsrR9LmXHg8cqnpuPk9bgASReK" width="614" height="455"></p>
<p>It seems to be a problem with the executable itself.<br>
It is possible to do</p>
<p>Slicer --launch ParaToSPHARMMeshCLP in Linux, but not on windows.</p>
<p>$ ./SlicerSALT.exe --launch ParaToSPHARMMeshCLP<br>
error: [C:/Program Files/SlicerSALT 1.1.0-2018-12-13/bin/…/lib/SlicerSALT-4.11/cli-modules/./ParaToSPHARMMeshCLP.exe] exit abnormally - Report the problem.</p>
<p>In the meantime, could you try to use the SPHARM-PDM extension in the latest Slicer release? I have been able to run it through Slicer in windows without problems.</p>
<p>$ ./Slicer.exe --launch ParaToSPHARMMeshCLP<br>
PARSE ERROR:<br>
One or more required arguments missing!</p>
<p>Brief USAGE:<br>
C:\Users\beatriz.paniagua\AppData\Roaming\NA-MIC\Extensions-27498\SPHARM<br>
-PDM\lib\Slicer-4.9\cli-modules.\P<br>
araToSPHARMMeshCLP.exe<br>
[–returnparameterfile<br>
<a>std::string</a>]<br>
[–processinformationaddress<br>
<a>std::string</a>] [–xml] [–echo]<br>
[–deserialize <a>std::string</a>]<br>
[–serialize <a>std::string</a>]<br>
[–FinalFlip ]<br>
[–procrustesTransformationFile<br>
<a>std::string</a>]<br>
[–procrustesTransformationOutputOn<br>
] [–regParaPoints <a>std::string</a>]<br>
[–regParaPointsOn]<br>
[–regParaTemplate <a>std::string</a>]<br>
[–regParaTemplateFileOn] [–verb]<br>
[–medialMesh] [–NoParaAlign]<br>
[–paraOut] [–regTemplate<br>
<a>std::string</a>]<br>
[–regTemplateFileOn]<br>
[–flipTemplate <a>std::string</a>]<br>
[–flipTemplateOn] [–phiIteration<br>
] [–thetaIteration ]<br>
[–spharmDegree ]<br>
[–subdivLevel ] [–]<br>
[–version] [-h] <a>std::string</a><br>
<a>std::string</a> <a>std::string</a></p>
<p>We are looking into it here: <a href="https://github.com/Kitware/SlicerSALT/issues/138" class="inline-onebox">ParaToSPHARMMesh completes with errors · Issue #138 · Kitware/SlicerSALT · GitHub</a></p>
<p>We will keep you posted.<br>
Thank you for reporting the bug!</p>
<p>Bea</p>

---

## Post #10 by @Suji_L_Lee (2019-07-23 02:35 UTC)

<p>Operating system:win 10<br>
version:3D Slicier 4.10.2</p>
<p>Hi,</p>
<p>I meet same problems with test data (SPHARM_Tutorial_Data_July2015)<br>
=&gt; Case 0: groupA_01_hippo - step 2: ParaToSPHARMMesh completed with errors</p>
<p>So, now I have to try Slicer or 3D-slicer in Linux, right?</p>
<p>Thank you,<br>
Suji</p>

---

## Post #11 by @rl00100 (2019-09-17 03:35 UTC)

<p>Has there been a fix for this, i am having a similar error with ParaToSPHARMMesh completing with errors in SlicerSALT 2.2.1 on windows and Linux, and as an extension on 3Dslicer 4.10 ?</p>
<p>Thanks,</p>
<p>Rob</p>

---

## Post #12 by @bpaniagua (2019-09-17 15:18 UTC)

<p>Hi Rob,</p>
<p>Have you tried the example data in our public folders?<br>
<a href="https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5d5c185f85f25b11ff3e1911" class="onebox" target="_blank" rel="nofollow noopener">https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5d5c185f85f25b11ff3e1911</a></p>
<p>Linux: I can reproduce your error message, but for the dataset above the data gets computed correctly.<br>
Windows: We are checking and we will keep you posted.</p>
<p>Thank you for reporting and bringing our attention back to the problem.<br>
Bea</p>

---

## Post #13 by @rl00100 (2019-09-18 00:48 UTC)

<p>Hi Bea,</p>
<p>I’ve been using the example data sets and still getting errors.</p>
<p>“/home/robl/Documents/SlicerSALT-2.2.1-linux-amd64/bin/…/lib/SlicerSALT-4.11/cli-modules/GenParaMeshCLP: error while loading shared libraries: libgfortran.so.3: cannot open shared object file: No such file or directory”</p>
<p>Is there maybe some prerequisites or file paths that i don’t have set that are causing the problems.</p>
<p>Thanks,</p>
<p>Rob</p>

---

## Post #14 by @bpaniagua (2019-09-18 12:18 UTC)

<p>Thanks for reporting. I am not sure why this is happening but for sure we need to look into it further.<br>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Kitware/SlicerSALT/issues/197" target="_blank" rel="nofollow noopener">github.com/Kitware/SlicerSALT</a>
  </header>
  <article class="onebox-body">
    <a href="https://github.com/bpaniagua" rel="nofollow noopener">
<img src="https://avatars1.githubusercontent.com/u/2599368?v=2&amp;s=96" class="thumbnail onebox-avatar" width="60" height="60">
</a>

<h4><a href="https://github.com/Kitware/SlicerSALT/issues/197" target="_blank" rel="nofollow noopener">Issue: Fortran library problems in SPHARM PDM</a></h4>

<div class="date" style="margin-top:10px;">
	<div class="user" style="margin-top:10px;">
	opened by <a href="https://github.com/bpaniagua" target="_blank" rel="nofollow noopener">bpaniagua</a>
	on <a href="https://github.com/Kitware/SlicerSALT/issues/197" target="_blank" rel="nofollow noopener">2019-09-18</a>
	</div>
	<div class="user">
	</div>
</div>

<pre class="content" style="white-space: pre-wrap;">OS: Windows
Data to reproduce: https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5d5c185f85f25b11ff3e1911
Error:
“/..../GenParaMeshCLP: error while loading shared libraries: libgfortran.so.3: cannot open shared object file: No such file or directory”
cc:...</pre>

<div class="labels">
 	<span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>We will keep you posted. Hopefully we can have this fixed this week.</p>

---

## Post #15 by @Sam_Horvath (2019-10-02 19:47 UTC)

<p>Updates:</p>
<p>There are separate bugs for the windows and linux installers involving Fortran packaging.  We are working to address both.  In the meantime, there is a work-around for the linux error.  Installing the missing  fortran library will allow SlicerSALT to run correctly.<br>
For linux, try this terminal command:<br>
<code>sudo apt-get install libgfortran3</code></p>
<p>This will install the library that SlicerSALT is looking for into the path.</p>

---

## Post #16 by @rl00100 (2019-10-03 01:05 UTC)

<p>Thanks, that fixes the ParaToSPARMMesh problem, the function now completes. However, now the outputs crash the population viewer in v2.2.1. I had to go back to v2.0.0 to get a working version.</p>
<p>Rob</p>

---

## Post #17 by @Sam_Horvath (2019-10-03 14:53 UTC)

<p>Could you give an some error output / description?</p>

---

## Post #18 by @rl00100 (2019-10-03 23:48 UTC)

<p>Opening the files in the population viewer from the SPHARM section in v2.2.1 gets this error.</p>
<p>" Traceback (most recent call last):<br>
File “/home/robl/Documents/SlicerSALT-2.2.1-linux-amd64/bin/…/lib/SlicerSALT-4.11/qt-scripted-modules/ShapeAnalysisModule.py”, line 710, in onCheckableComboBoxValueChanged<br>
outputRootname = label.text<br>
AttributeError: ‘NoneType’ object has no attribute ‘text’ "</p>
<p>moving to the population view and opening the Step3_ParaToSPHARMMesh directory crashes and closes SlicerSALT and i am not sure how to get an error message from that. This happens with both the output files i solve, and your example ones.</p>
<p>Rob</p>

---

## Post #19 by @Sam_Horvath (2019-10-04 16:42 UTC)

<p>Thanks for the info, looking into this.</p>

---
