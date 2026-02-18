# SPHARM analysis of 3D slicer

**Topic ID**: 9630
**Date**: 2019-12-27
**URL**: https://discourse.slicer.org/t/spharm-analysis-of-3d-slicer/9630

---

## Post #1 by @keven (2019-12-27 19:24 UTC)

<p>Hello, experts!</p>
<p>Recently, I want to use the 3D Slicer expansion module, SPHARM, to analyze the condylar models of the same patient in different periods. I used 3d-slicer to complete the registration and segmentation of CBCT images of condyle in different periods, and then used itk-snap to complete the modeling and export them to VTK format, but when I imported folder, which contained the condyle VTK files, into the SPHARM module for shape analysis, the first and second steps can be completed, but the third step：ParaToSPHARMMesh completed with errors. The following shows  the error points indicated by 3D Slicer, Can someone help me see where the problem is?<br>
Operating system:win 10<br>
version:3D Slicer 4.10.2</p>
<p>Thanks in advance!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/327b54b004a9cc22c0c3751de5c765c42ed3fb31.png" data-download-href="/uploads/short-url/7cA6JkjMra5YNChxV2FFyEQU4nf.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/327b54b004a9cc22c0c3751de5c765c42ed3fb31.png" alt="1" data-base62-sha1="7cA6JkjMra5YNChxV2FFyEQU4nf" width="690" height="144" data-dominant-color="D9E1F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1897×396 14.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @keven (2020-01-01 03:30 UTC)

<p>When I used SlicerSALT for SPHARM analysis of the same file, ONLY the third step completed with errors, as shown below. Does anyone know where the problem is?<br>
Case 0: 1111 - step 3: ParaToSPHARMMesh completed with errors<br>
loadNodeFromFile <code>returnNode</code> argument is deprecated. Loaded node is now returned directly if <code>returnNode</code> is not specified.</p>

---

## Post #3 by @bpaniagua (2020-01-02 13:21 UTC)

<p>Hi Kaiwen,</p>
<p>Thank you for using SPHARM! Could you please try to repeat this process with the preview version of Slicer or using <a href="https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5898b7ef8d777f07219fcb14">our SlicerSALT package</a>?</p>

---

## Post #4 by @keven (2020-01-02 14:11 UTC)

<p>Thank you very much for your reply!<br>
I tried to reanalyze the data using slicersalt 2.2.0.I changed the number of iterations to 100, and the other parameters remain default.<br>
The first and second steps can be completed, but the third step:ParaToSPHARMMesh completed with errors.<br>
Python Interactor showed me the following information:<br>
– Completing : Case 1: 2222 - step 2: GenParaMesh</p>
<p>– Completed : Case 1: 2222 - step 2: GenParaMesh</p>
<p>– Scheduled : Case 1: 2222 - step 3: ParaToSPHARMMesh</p>
<p>– Completed with errors : Case 1: 2222 - step 3: ParaToSPHARMMesh</p>
<p>Saving 2222.nrrd in D:/CT/2/Step0_MeshToLabelMap</p>
<p>Saving 2222_pp.nrrd in D:/CT/2/Step1_SegPostProcess</p>
<p>Saving 2222_pp_para.vtk in D:/CT/2/Step2_GenParaMesh</p>
<p>Saving 2222_pp_surf.vtk in D:/CT/2/Step2_GenParaMesh</p>
<p>– Completed with errors: Case 1: 2222.vtk</p>
<p>Case 1 (2222.vtk) took 60 sec to run</p>
<p>Case 1: 2222 - step 3: ParaToSPHARMMesh completed with errors</p>
<p>All pipelines took: 182 sec to run</p>
<p>– Completed with errors : ShapeAnalysisModule</p>
<p>Case 1: 2222 - step 3: ParaToSPHARMMesh completed with errors</p>
<p>3.6.7 (default, Sep 6 2019, 16:48:27) [MSC v.1900 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>Status: <i>Idle</i></p>
<p>Widget: Running ShapeAnalysisModule</p>
<p>– Scheduled : ShapeAnalysisModule</p>
<p>2 case(s) found</p>
<p>– Running : ShapeAnalysisModule</p>
<p>loadNodeFromFile <code>returnNode</code> argument is deprecated. Loaded node is now returned directly if <code>returnNode</code> is not specified.</p>
<p>– Scheduled: Case 0: 1111.vtk</p>
<p>– Scheduled : Case 0: 1111 - step 0: Mesh To Label Map</p>
<p>– Running : Case 0: 1111 - step 0: Mesh To Label Map</p>
<p>– Completed : Case 0: 1111 - step 0: Mesh To Label Map</p>
<p>– Scheduled : Case 0: 1111 - step 1: SegPostProcess</p>
<p>– Running : Case 0: 1111 - step 1: SegPostProcess</p>
<p>– Completing : Case 0: 1111 - step 1: SegPostProcess</p>
<p>– Completed : Case 0: 1111 - step 1: SegPostProcess</p>
<p>– Scheduled : Case 0: 1111 - step 2: GenParaMesh</p>
<p>– Running : Case 0: 1111 - step 2: GenParaMesh</p>
<p>– Completing : Case 0: 1111 - step 2: GenParaMesh</p>
<p>– Completed : Case 0: 1111 - step 2: GenParaMesh</p>
<p>– Scheduled : Case 0: 1111 - step 3: ParaToSPHARMMesh</p>
<p>– Running : Case 0: 1111 - step 3: ParaToSPHARMMesh</p>
<p>– Completed with errors : Case 0: 1111 - step 3: ParaToSPHARMMesh</p>
<p>Saving 1111.nrrd in D:/CT/2/Step0_MeshToLabelMap</p>
<p>Saving 1111_pp.nrrd in D:/CT/2/Step1_SegPostProcess</p>
<p>Saving 1111_pp_para.vtk in D:/CT/2/Step2_GenParaMesh</p>
<p>Saving 1111_pp_surf.vtk in D:/CT/2/Step2_GenParaMesh</p>
<p>– Completed with errors: Case 0: 1111.vtk</p>
<p>Case 0 (1111.vtk) took 121 sec to run</p>
<p>– Completed : Case 1: 2222 - step 0: Mesh To Label Map</p>
<p>– Scheduled : Case 1: 2222 - step 1: SegPostProcess</p>
<p>– Running : Case 1: 2222 - step 1: SegPostProcess</p>
<p>– Completed : Case 1: 2222 - step 1: SegPostProcess</p>
<p>– Scheduled : Case 1: 2222 - step 2: GenParaMesh</p>
<p>– Running : Case 1: 2222 - step 2: GenParaMesh</p>
<p>– Scheduled: Case 1: 2222.vtk</p>
<p>– Scheduled : Case 1: 2222 - step 0: Mesh To Label Map</p>
<p>– Running : Case 1: 2222 - step 0: Mesh To Label Map</p>
<p>Is this problem due to my mistake in operation or other reasons？<br>
I look forward to your reply！Thank you in advance！</p>

---

## Post #5 by @keven (2020-01-02 14:14 UTC)

<p>What other information do I need to provide to help you analyze this problem?</p>

---

## Post #6 by @bpaniagua (2020-01-02 14:35 UTC)

<p>What is the content of your paratospharm mesh folder?</p>

---

## Post #7 by @keven (2020-01-02 15:00 UTC)

<p>Hi ,Beatriz Paniagua!<br>
I followed your advice and used the 4.8.0 version of 3D slicer for SPHARM analysis.<br>
Surprisingly, when I import the VTK model file into 3D slicer, I can complete three steps of analysis. Here is a screenshot of the file contained in the third step folder, paratosparm.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f23989e113b3363bc7be782cc205e991a46cf86.png" data-download-href="/uploads/short-url/bi5Z2LwigL9UWl42ykWtzlPRKYu.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f23989e113b3363bc7be782cc205e991a46cf86.png" alt="1" data-base62-sha1="bi5Z2LwigL9UWl42ykWtzlPRKYu" width="627" height="500" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">788×628 13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Does this mean that I have finished the SPHARM analysis？</p>

---
