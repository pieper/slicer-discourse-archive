# Problems with fibers' directions

**Topic ID**: 10759
**Date**: 2020-03-20
**URL**: https://discourse.slicer.org/t/problems-with-fibers-directions/10759

---

## Post #1 by @doc-xie (2020-03-20 09:27 UTC)

<p>Version: 4.11.0-2020-02-26<br>
System: Mac<br>
MR scanner: GE, 3.0T<br>
Problem:<br>
The components of the diffusion data can be checked successfully in Volume module and the FA map can be derived with Diffusion Tensor Estimation. The orientation of the map is marked correctly with anterior to posterior. But after running the whole brain fibers tractography with UKF method, the orientation changed into the directions (posterior to anterior) and contrary to the FA map. But if the data was loaded into Slicer using Dcm2niixGUI, the result was correct. What the reason about this and how to solve this problem?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/262e0437aabbdad0df2329fc86d854267043ceb7.jpeg" data-download-href="/uploads/short-url/5rKJupJsiabRDZPmAayi8rnEMWr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/262e0437aabbdad0df2329fc86d854267043ceb7_2_484x500.jpeg" alt="image" data-base62-sha1="5rKJupJsiabRDZPmAayi8rnEMWr" width="484" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/262e0437aabbdad0df2329fc86d854267043ceb7_2_484x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/262e0437aabbdad0df2329fc86d854267043ceb7_2_726x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/262e0437aabbdad0df2329fc86d854267043ceb7_2_968x1000.jpeg 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1950×2014 347 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e19b4f58ae436f9548e17a53687d207cd329fa85.jpeg" data-download-href="/uploads/short-url/wbObdida5gctl8fa9c2ePX20WJT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e19b4f58ae436f9548e17a53687d207cd329fa85_2_690x307.jpeg" alt="image" data-base62-sha1="wbObdida5gctl8fa9c2ePX20WJT" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e19b4f58ae436f9548e17a53687d207cd329fa85_2_690x307.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e19b4f58ae436f9548e17a53687d207cd329fa85_2_1035x460.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e19b4f58ae436f9548e17a53687d207cd329fa85_2_1380x614.jpeg 2x" data-dominant-color="0C0B09"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1947×868 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/077c6003e10567ff731763eba376668b187bee0d.jpeg" data-download-href="/uploads/short-url/14dOvqMoMMY7GXxjlNio6ncILX7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/077c6003e10567ff731763eba376668b187bee0d_2_559x500.jpeg" alt="image" data-base62-sha1="14dOvqMoMMY7GXxjlNio6ncILX7" width="559" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/077c6003e10567ff731763eba376668b187bee0d_2_559x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/077c6003e10567ff731763eba376668b187bee0d_2_838x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/077c6003e10567ff731763eba376668b187bee0d_2_1118x1000.jpeg 2x" data-dominant-color="54566A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1950×1743 894 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
the information after UKF tractography showed as below:<br>
UKF Tractography standard output:</p>
<p>Using the 1T simple model. Setting the default parameters accordingly:<br>
“*”: set by user<br>
“-”: default setting</p>
<ul>
<li>stoppingFA: 0.06</li>
<li>seedingThreshold: 0.1</li>
</ul>
<ul>
<li>Qm: 0.005</li>
<li>Ql: 300</li>
<li>Rs: 0.01</li>
</ul>
<ul>
<li>stepLength: 0.3</li>
<li>recordLength: 0.9</li>
<li>stoppingThreshold: 0.06</li>
<li>seedsPerVoxel: 2<br>
Found 12 cores on your system.<br>
Running tractography with 12 thread(s).<br>
Number of non-zero gradients: 25<br>
Number of zero gradients: 1<br>
Permuting the axis order to: 0 1 2 3<br>
Resizing the data to: 25 256 256 39<br>
Computing the baseline image<br>
Dividing the signal by baseline image<br>
Data normalization finished!</li>
</ul>
<p>Using 1-tensor simple model.<br>
Branching disabled</p>
<p>Using unconstrained filter<br>
nmse_avg=0<br>
vtkDebugLeaks has found no leaks.</p>
<p>UKF Tractography completed without errors<br>
Very interesting, for another subject, after the diffusion data was loaded into Slicer with Dcm2niiGUI, the FA map looks normal but the fibers were in wrong direction again. If I handle the data with DTIPrep for motion and eddy current correction and load the data again, the fibers turned up down and only showed the superior part of the whole brain fibers.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14091ffe885e3b495fb1bca2deae33911b5f30f5.jpeg" data-download-href="/uploads/short-url/2Rf6aNuZZRUv2IVcKM2YWCVdeZf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14091ffe885e3b495fb1bca2deae33911b5f30f5_2_587x500.jpeg" alt="image" data-base62-sha1="2Rf6aNuZZRUv2IVcKM2YWCVdeZf" width="587" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14091ffe885e3b495fb1bca2deae33911b5f30f5_2_587x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14091ffe885e3b495fb1bca2deae33911b5f30f5_2_880x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14091ffe885e3b495fb1bca2deae33911b5f30f5_2_1174x1000.jpeg 2x" data-dominant-color="9BA0D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1947×1656 331 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> The information of UKF Tractography showed as below:<br>
UKF Tractography standard output:</p>
<p>Using the 1T simple model. Setting the default parameters accordingly:<br>
“*”: set by user<br>
“-”: default setting</p>
<ul>
<li>stoppingFA: 0.15</li>
</ul>
<ul>
<li>seedingThreshold: 0.18</li>
</ul>
<ul>
<li>Qm: 0.005</li>
<li>Ql: 300</li>
<li>Rs: 0.01</li>
</ul>
<ul>
<li>stepLength: 0.3</li>
<li>recordLength: 0.9</li>
<li>stoppingThreshold: 0.1</li>
<li>seedsPerVoxel: 2<br>
Found 8 cores on your system.<br>
Running tractography with 8 thread(s).<br>
Number of non-zero gradients: 25<br>
Number of zero gradients: 1<br>
Permuting the axis order to: 0 1 2 3<br>
Resizing the data to: 25 256 256 40<br>
Computing the baseline image<br>
Dividing the signal by baseline image<br>
Data normalization finished!</li>
</ul>
<p>Using 1-tensor simple model.<br>
Branching disabled</p>
<p>Using unconstrained filter<br>
nmse_avg=0<br>
vtkDebugLeaks has found no leaks.</p>

---

## Post #2 by @zhangfanmark (2020-03-20 13:22 UTC)

<p>Hi <a class="mention" href="/u/doc-xie">@doc-xie</a></p>
<p>Given our conversation offline, I thought we have managed to run UKF in an appropriate way on these datasets.  For the two screenshots you attached here, the tractography datasets were all visually wrong. This is related to the gradient table that is not in the format that SlicerDMRI wants.</p>
<p>Regards,<br>
Fan</p>

---

## Post #3 by @doc-xie (2020-03-25 09:00 UTC)

<p>Maybe the reason about this problem is the version of Slicer. After I changed the software into 4.10.0, the direction of the fibers showed normally.<br>
Thank you very much.<br>
Xie</p>

---
