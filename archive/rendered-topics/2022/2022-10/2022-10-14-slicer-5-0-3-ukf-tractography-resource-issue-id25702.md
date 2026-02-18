# Slicer 5.0.3 - UKF Tractography Resource Issue

**Topic ID**: 25702
**Date**: 2022-10-14
**URL**: https://discourse.slicer.org/t/slicer-5-0-3-ukf-tractography-resource-issue/25702

---

## Post #1 by @cnot (2022-10-14 09:47 UTC)

<p>Hi all,</p>
<p>I am trying to run UKF Tractography on my DTI data, and am encountering problems that seem to be related to memory use.<br>
Note: this always worked with the same data and parameters on a previous release of Slicer (4.10.2), so it would appear something has changed in the new release?</p>
<p>OS: Windows 10<br>
Slicer version: 5.0.3<br>
System details: Precision workstation, i9-9940X 14 core CPU, 128GB RAM, M.2 SSD, RTX2080<br>
Input data: DTI data with 1 B0 and 64 directions, 220x220x156 voxels, 1mm³ resolution</p>
<p>Behavior:<br>
UKF Tractography runs, using significant resources (over 35 GB of RAM) for a few hours (see image below).<br>
Upon completion, the created fiber bundle file is empty. However, there are no reported errors (UKF Tractography completes “without errors”).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9ddb1bdd85a00474c412917cfcd8f70600d2888e.jpeg" alt="1mm_resources" data-base62-sha1="mwsoSZSb3mAbWgBXAkzZPMu3cXc" width="444" height="395"><br>
<em>Blue= memory use (GB), Pink = CPU use (%)</em></p>
<p>When I resample my data to 1.2mm isotropic voxels, the tractography runs fine (see figure below for resource use).<br>
Similarly, it runs fine if I significantly crop my data (by excluding some background, brainstem and cerebellum).<br>
In both these cases, memory used by UKF is reduced to &lt;32GB.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b99573755efae975907dae4309b1cb18a83b14c5.jpeg" alt="1.2mm_resources" data-base62-sha1="qtKwONDG049kp5cUdPAkalqMYfP" width="437" height="264"><br>
<em>Blue= memory use (GB), Pink = CPU use (%)</em></p>
<p>I noticed this has been an issue in the past for some users (see <a href="https://discourse.slicer.org/t/ukf-tractography-fails-for-large-scans-1-5mm-iso/23863" class="inline-onebox">UKF tractography fails for large scans (~1.5mm iso)</a>), and that the suggested fix was to add more physical/virtual memory to ensure the process is not running out of resources. However, we definitely have 128GB available, so this does not seem to be the issue in our case.</p>
<p>I have noted, that compared to the previous version we used (Slicer 4.10.2), the memory usage of UKF tractography has more than doubled for processing of the same data.<br>
Could this be related to the switch from VTK 8.2 to VTK 9 in Slicer 5 / Some internal format change? e.g. from integer to floating point?</p>
<p>Apart from what has caused that increased memory usage, from what I can tell, it appears as though when memory use of the UKF Tractography process exceeds 32GB, then no output file is created / the process crashes. Can this be some internal limitation? Some maximum size of something specified somewhere? Explicitly or given by some variable’s format?<br>
Interestingly, the UKF tractography process completes “without errors”, so maybe the UFK-extension is actually fine and the problem occurs just in the very final stage when the resulting tract file is assembled and written out?</p>
<p>Is this something that is known/has been reported before? I am happy to provide a sample dataset to replicate this issue if this would help.</p>
<p>Thanks in advanced for your support!</p>

---

## Post #2 by @pieper (2022-10-17 15:17 UTC)

<p>Thanks for reporting this - does this happen on all datasets or just on a few cases?  E.g. do you see the same issue on the DWI sample data that comes with Slicer in the SampleData module?</p>

---

## Post #3 by @cnot (2022-10-17 22:03 UTC)

<p>Thank you for your reply!</p>
<p>I do not observe this on the sample data, or on any other data where the resolution is not as high / where there are less directions. So I guess it is related to the size of the data?</p>

---

## Post #4 by @pieper (2022-10-17 22:26 UTC)

<p>Interesting.  Okay, then yes, please provide a sample dataset and I hope someone can have a look.</p>

---

## Post #5 by @cnot (2022-10-18 08:56 UTC)

<p>I would really appreciate that, thank you!</p>
<p>Here is a sample set with the DTI data and the mask for tractography.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/74mjs32xvfn4d4v/Sample_DTI_Data.zip?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/s/74mjs32xvfn4d4v/Sample_DTI_Data.zip?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-zip-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/s/74mjs32xvfn4d4v/Sample_DTI_Data.zip?dl=0" target="_blank" rel="noopener nofollow ugc">Sample_DTI_Data.zip</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @pieper (2022-10-20 15:30 UTC)

<p>Thanks for sharing the data - someone from the DMRI team should be able to look into this.  Can you help by providing the exact command line (you can find the exact parameters in the log file if you ran from within Slicer).</p>

---

## Post #7 by @cnot (2022-10-21 07:59 UTC)

<p>Of course! Here is the full command line:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 12.10.2022 17:08:09 [] (unknown:0) - UKF Tractography command line: 

C:/ProgramData/NA-MIC/Slicer 5.0.3/NA-MIC/Extensions-30893/UKFTractography/lib/Slicer-5.0/cli-modules/UKFTractography.exe --dwiFile C:/Users/Administrator/AppData/Local/Temp/Slicer/JAIE_vtkMRMLDiffusionWeightedVolumeNodeB.nhdr --seedsFile C:/Users/Administrator/AppData/Local/Temp/Slicer/JAIE_vtkMRMLLabelMapVolumeNodeB.nhdr --labels 1 --maskFile C:/Users/Administrator/AppData/Local/Temp/Slicer/JAIE_vtkMRMLLabelMapVolumeNodeB.nhdr --tracts C:/Users/Administrator/AppData/Local/Temp/Slicer/JAIE_vtkMRMLFiberBundleNodeB.vtp --seedsPerVoxel 1 --seedingThreshold 0.18 --stoppingFA 0.12 --stoppingThreshold 0.1 --numThreads -1 --numTensor 2 --stepLength 0.3 --Qm 0 --recordLength 0.9 --maxHalfFiberLength 200 --recordFA --recordTensors --Ql 0 --Qw 0 --Qkappa 0.01 --Qvic 0.004 --Rs 0 --sigmaSignal 0 --maxBranchingAngle 0 --minBranchingAngle 0 --minGA 10000

</code></pre>
<p>Thank you!</p>

---

## Post #8 by @cnot (2022-11-14 13:16 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> - Do you happen to know if there has been any progress made from the DMRI team on this front? Any updates would be welcome! Cheers!</p>

---

## Post #9 by @pieper (2022-11-14 15:57 UTC)

<p>I know it’s being investigated but I don’t think it’s been resolved.  Hopefully soon…</p>

---

## Post #10 by @RyanZurrin (2022-11-15 14:34 UTC)

<p>Hello <a class="mention" href="/u/cnot">@cnot</a>, we have been testing the UKFTractography module with the data you have provided. We have noticed that you had an additional seed file that was used when you ran it yourself. Looking at the two files that are within the sample data, there is a Sample_DWI_Volume_4D_1mm.nrrd, and a Sample_Mask_1mm.nrrd, and there is not any JAIE_vtkMRMLLabelMapVolumeNodeB.nhdr.</p>
<p>We are currently testing with our own seedFile which was created using the segmentation editor, but we also tested without any seedFile and have some mixed results.</p>
<p>Another quick note: When running UKFTractography with the initial mask file you provided we would get the following error:</p>
<hr>
<p>implementation only accepts masks of type ‘signed char’, ‘unsigned char’, ‘short’, and ‘unsigned short’</p>
<p>Convert your mask using ‘unu convert’ and rerun.</p>
<hr>
<p>So, we ended up using unu convert to convert the mask you provided to a short data type to perform the following tests.</p>
<p>First, we ran the UKFTractography on your data on our HPC compute nodes outside of slicer just to verify that the data would get results. We did this to make sure the issue was not in the data at all, and we got good results doing that.</p>
<p>Next, we tested data with the newest slicer that was not your sample data just to see if we could get results with any data and we were able to get results using that different data inside the newest slicer.</p>
<p>Then we Used your data without and seedFile using the Slicer GUI and during this test we were not able to generate a usable tracts file (We are still investigating what is causing this issue within the GUI)</p>
<p>Additionally, we were able to use your data without a seedFile using the newest Slicer through the command line and that generated a good tracts file. The command I used for this is as follows:</p>
<hr>
<p>C:\Users\ryanz&gt;“D:\ryanz\AppData\Local\NA-MIC\Slicer 5.0.3\Slicer.exe” -launch “D:\ryanz\AppData\Local\NA-MIC\Slicer 5.0.3\NA-MIC\Extensions-30893\UKFTractography\lib\Slicer-5.0\cli-modules\UKFTractography.exe”</p>
<p>–dwiFile D:\SlicerTest\Sample_DWI_Volume_4D_1mm.nrrd</p>
<p>–maskFile D:\SlicerTest\Sample_Mask_1mmShort.nrrd</p>
<p>–tracts D:\SlicerTest\newTractTest1.vtk</p>
<p>–seedsPerVoxel 1</p>
<p>–seedingThreshold 0.18</p>
<p>–stoppingFA 0.12</p>
<p>–stoppingThreshold 0.1</p>
<p>–numThreads -1</p>
<p>–numTensor 2</p>
<p>–stepLength 0.3</p>
<p>–Qm 0</p>
<p>–recordLength 0.9</p>
<p>–maxHalfFiberLength 200</p>
<p>–recordFA</p>
<p>–recordTensors</p>
<p>–Ql 0 --Qw 0 --Qkappa 0.01 --Qvic 0.004 --Rs 0</p>
<p>–sigmaSignal 0</p>
<p>–maxBranchingAngle 0</p>
<p>–minBranchingAngle 0</p>
<p>–minGA 10000</p>
<p>Link to the tracts file is here: <a href="https://www.dropbox.com/s/k6tns8xp0yp3d4e/newTractTest1.vtk?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - newTractTest1.vtk - Simplify your life</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/872301bbbde40637ac0b8aca801b8d652092f496.jpeg" data-download-href="/uploads/short-url/jhtswTKLgt07Ss6Gnx7otmfqbwa.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/872301bbbde40637ac0b8aca801b8d652092f496_2_643x500.jpeg" alt="image" data-base62-sha1="jhtswTKLgt07Ss6Gnx7otmfqbwa" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/872301bbbde40637ac0b8aca801b8d652092f496_2_643x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/872301bbbde40637ac0b8aca801b8d652092f496.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/872301bbbde40637ac0b8aca801b8d652092f496.jpeg 2x" data-dominant-color="535C81"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">772×600 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It is a 5GB tract file so incase you did not want to DL to view this is a stapshot of the tracts.</p>
<hr>
<p>Currently, we are in the process of running the UKFTractography with a seedFile using the GUI to see if we are able to produce the bug with a seedFile as well.</p>
<p>It takes so long to run without the seed that trying to debug it running on the data without a seedFile will be very time consuming so if we can reproduce it with faster runs that will allow us to generate debug data at a much faster rate. This is the current goal.</p>
<p>Sorry about the delayed response, and thanks you for your patience while we sort out the issue.</p>

---

## Post #11 by @lassoan (2022-11-15 17:05 UTC)

<aside class="quote no-group" data-username="RyanZurrin" data-post="10" data-topic="25702">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ryanzurrin/48/15735_2.png" class="avatar"> RyanZurrin:</div>
<blockquote>
<p>We are still investigating what is causing this issue within the GUI</p>
</blockquote>
</aside>
<p>If you run a CLI module using Slicer GUI then you can find the command-line parameters in the application logs. You might find that the difference is due to computing the tracts with slightly different parameters.</p>

---

## Post #12 by @RyanZurrin (2022-11-15 17:29 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="25702">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you run a CLI module using Slicer GUI then you can find the command-line parameters in the application logs. You might find that the difference is due to computing the tracts with slightly different parameters.</p>
</blockquote>
</aside>
<p>Thanks,  we will check the logs and see what we can find then.  We appreciate the suggestions.</p>

---

## Post #13 by @cnot (2022-11-16 12:54 UTC)

<p>Hi <a class="mention" href="/u/ryanzurrin">@RyanZurrin</a>, thank you so much for your detailed update! I really appreciate it.</p>
<aside class="quote no-group" data-username="RyanZurrin" data-post="10" data-topic="25702">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ryanzurrin/48/15735_2.png" class="avatar"> RyanZurrin:</div>
<blockquote>
<p>We have noticed that you had an additional seed file that was used when you ran it yourself.</p>
</blockquote>
</aside>
<p>Sorry I was not clear with this - I was using essentially the same as the mask as my seeds file, so I was basically telling it to seed from each voxel in the brain.</p>
<aside class="quote no-group" data-username="RyanZurrin" data-post="10" data-topic="25702">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ryanzurrin/48/15735_2.png" class="avatar"> RyanZurrin:</div>
<blockquote>
<p>So, we ended up using unu convert to convert the mask you provided to a short data type to perform the following tests.</p>
</blockquote>
</aside>
<p>Ah, yes, I realize I also did this from within Slicer as I encountered the same error. I must have not saved the converted mask to send you, really sorry about this.</p>
<aside class="quote no-group" data-username="RyanZurrin" data-post="10" data-topic="25702">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ryanzurrin/48/15735_2.png" class="avatar"> RyanZurrin:</div>
<blockquote>
<p>Additionally, we were able to use your data without a seedFile using the newest Slicer through the command line and that generated a good tracts file.</p>
</blockquote>
</aside>
<p>This is interesting to know, thank you! I will try to reproduce this.</p>
<aside class="quote no-group" data-username="RyanZurrin" data-post="10" data-topic="25702">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ryanzurrin/48/15735_2.png" class="avatar"> RyanZurrin:</div>
<blockquote>
<p>It takes so long to run without the seed that trying to debug it running on the data without a seedFile will be very time consuming so if we can reproduce it with faster runs that will allow us to generate debug data at a much faster rate. This is the current goal.</p>
</blockquote>
</aside>
<p>And this all sounds excellent, thanks again so much for all your help and for figuring this out. I look forward to hearing the next update!</p>

---

## Post #14 by @cnot (2023-01-26 10:07 UTC)

<p>Hi <a class="mention" href="/u/ryanzurrin">@RyanZurrin</a>, I hope you had a good start to the New Year! Do you happen to have any updates on this front? Cheers.</p>

---

## Post #15 by @Alou_Diakite (2024-07-18 03:49 UTC)

<p>Hi, how did you Convert your mask using ‘unu convert’? I am getting the same error message regarding the mask datatype. Thank you</p>

---
