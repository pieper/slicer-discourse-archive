---
topic_id: 23901
title: "Model To Model Distance Computation Is Completed With Error"
date: 2022-06-16
url: https://discourse.slicer.org/t/23901
---

# Model to Model distance computation is "completed with error"

**Topic ID**: 23901
**Date**: 2022-06-16
**URL**: https://discourse.slicer.org/t/model-to-model-distance-computation-is-completed-with-error/23901

---

## Post #1 by @Moh_d_Al-Watary (2022-06-16 11:16 UTC)

<p>Dears in 3D Slicer support,<br>
I am experiencing and old problem: when using Model to Model distance it is suddenly ending with this message: completed with error.<br>
the version I am using is 4.11…2021.0226 ( I am using this as I am used to use this version)<br>
How could I solve this problem, and if can not be solved what is the replacement on the new release version of the 3D Slicer.<br>
Thank you so much in advance.<br>
N.B.: Below is the link to the debug word file and screenshot.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/4655c81e6725b68e4c6743dc61f96d6aa4eed267.jpeg" data-download-href="/uploads/short-url/a2dcYXhzIOEknWc00EjU6bLcPc3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4655c81e6725b68e4c6743dc61f96d6aa4eed267_2_690x387.jpeg" alt="image" data-base62-sha1="a2dcYXhzIOEknWc00EjU6bLcPc3" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4655c81e6725b68e4c6743dc61f96d6aa4eed267_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4655c81e6725b68e4c6743dc61f96d6aa4eed267_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/4655c81e6725b68e4c6743dc61f96d6aa4eed267.jpeg 2x" data-dominant-color="BABCAD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 275 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p><aside class="onebox googledocs" data-onebox-src="https://docs.google.com/document/d/19meznYdz-512znRCLXfFoGlcIp7wca5a/edit?usp=sharing&amp;ouid=103710780158037961301&amp;rtpof=true&amp;sd=true">
  <header class="source">

      <a href="https://docs.google.com/document/d/19meznYdz-512znRCLXfFoGlcIp7wca5a/edit?usp=sharing&amp;ouid=103710780158037961301&amp;rtpof=true&amp;sd=true" target="_blank" rel="noopener nofollow ugc">docs.google.com</a>
  </header>

  <article class="onebox-body">
    <a href="https://docs.google.com/document/d/19meznYdz-512znRCLXfFoGlcIp7wca5a/edit?usp=sharing&amp;ouid=103710780158037961301&amp;rtpof=true&amp;sd=true" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-docs-logo"></span></a>

<h3><a href="https://docs.google.com/document/d/19meznYdz-512znRCLXfFoGlcIp7wca5a/edit?usp=sharing&amp;ouid=103710780158037961301&amp;rtpof=true&amp;sd=true" target="_blank" rel="noopener nofollow ugc">DEBUG.docx</a></h3>

<p>[DEBUG][Qt] 16.06.2022 15:58:39 [] (unknown:0) - Session start time .......: 2022-06-16 15:58:39 [DEBUG][Qt] 16.06.2022 15:58:39 [] (unknown:0) - Slicer version ...........: 4.11.20210226 (revision 29738 / 7a593c8) win-amd64 - installed release...</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @pieper (2022-06-16 11:55 UTC)

<p>Click the two down arrows next to the message to open a box with the specific output and this should help you narrow down why it’s not working.  Perhaps this model is too complex.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15108e8fd5a036f1898a9539e06c746d397b1f17.png" alt="image" data-base62-sha1="30luZmV7mH8wzyG4mFRASPcazsP" width="118" height="88"></p>

---

## Post #3 by @lassoan (2022-06-16 13:51 UTC)

<p>The attached log file includes the information that is shown when the double-down arrow is pressed:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 16.06.2022 18:56:07 [] (unknown:0) - Found CommandLine Module, target is C:/Users/Mohammed Al-watary/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/ModelToModelDistance/lib/Slicer-4.11/cli-modules/ModelToModelDistance.exe
[DEBUG][Qt] 16.06.2022 18:56:07 [] (unknown:0) - ModuleType: CommandLineModule
[DEBUG][Qt] 16.06.2022 18:56:08 [] (unknown:0) - Model To Model Distance command line: 
C:/Users/Mohammed Al-watary/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/ModelToModelDistance/lib/Slicer-4.11/cli-modules/ModelToModelDistance.exe --source C:/Users/Mohammed Al-watary/AppData/Local/Temp/Slicer/BFJCA_vtkMRMLModelNodeE.vtk --target C:/Users/Mohammed Al-watary/AppData/Local/Temp/Slicer/BFJCA_vtkMRMLModelNodeF.vtk --output C:/Users/Mohammed Al-watary/AppData/Local/Temp/Slicer/BFJCA_vtkMRMLModelNodeDA.vtk --distanceType signed_closest_point
[ERROR][VTK] 16.06.2022 18:56:14 [vtkSlicerCLIModuleLogic (000001E5D0E3E050)] (D:\D\S\Slicer-1\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2126) - Model To Model Distance terminated with a fault.
</code></pre>
<p>Unfortunately, this is not very informative, only shows that Model To Model distance module crashes early.</p>
<p>First of all, try with the latest Slicer Stable Release and see if the problem still occurs.</p>
<p>If it does, then a good next step would be to share the input files with us. To do that enable the developer option of preserving CLI module data files (in menu: application settings → Developer → enable <code>Preserve CLI module data files</code>), then upload to dropbox/onedrive/gdrive the source and target files that are mentioned in the application log; and post here the link. We’ll then see if we can reproduce the error on our computers.</p>

---

## Post #4 by @amymanson (2022-08-02 08:49 UTC)

<p>I also get a “completed with errors” message:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cdfa489b8bf0446dc3178a4d8670c85eee96760.png" data-download-href="/uploads/short-url/8GvNDlwpll4eSqieK1Ncc8uCWIw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cdfa489b8bf0446dc3178a4d8670c85eee96760.png" alt="image" data-base62-sha1="8GvNDlwpll4eSqieK1Ncc8uCWIw" width="465" height="500" data-dominant-color="F9F9FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">579×622 7.64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I have tried this with the latest stable release with the same result. Am going to try with some models that I know do work, but in the meantime, does anyone have any ideas for a solution?<br>
Thanks,<br>
Amy</p>

---

## Post #5 by @amymanson (2022-08-02 15:47 UTC)

<p>^^ Answered my own question - I was using .vtk file (volumetric mesh) rather than .stl (surface mesh). It’s working fine now that I’m using .stl</p>

---
