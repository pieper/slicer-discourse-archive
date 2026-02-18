# Bone texture extension errors

**Topic ID**: 12099
**Date**: 2020-06-18
**URL**: https://discourse.slicer.org/t/bone-texture-extension-errors/12099

---

## Post #1 by @muratmaga (2020-06-18 18:59 UTC)

<p>This is to the developers of the bone texture extension:</p>
<p>I am trying to use the calculate bone morphometry properties from proximal mouse femora. While the results are tabulated, it is complaining about a missing tag, and the featuremap cannot be plotted. This is with the preview version yesterday on windows.</p>
<p>Below is the log:</p>
<pre><code>Compute BM Features command line: 

C:/Users/amaga/AppData/Roaming/NA-MIC/Extensions-29148/BoneTextureExtension/lib/Slicer-4.11/cli-modules/ComputeBMFeatures.exe --returnparameterfile C:/Temp/3888_f1leXYpP3q.params --inputMask C:/Temp/DIII_vtkMRMLLabelMapVolumeNodeB.nrrd --threshold 10000 C:/Temp/DIII_vtkMRMLScalarVolumeNodeC.nrrd 

Compute BM Features completed without errors

Missing 'DWMRI_b-value' tag!


vtkMRMLDiffusionWeightedVolumeNode: Cannot parse Diffusion Information


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


BM status: Completed
Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


BM status: Completed
Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420B25D0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420A9E20) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageExtractComponents(0000021C420AD2F0) has 0 connections but is not optional.


Traceback (most recent call last):
  File "C:/Users/amaga/AppData/Roaming/NA-MIC/Extensions-29148/BoneTextureExtension/lib/Slicer-4.11/qt-scripted-modules/BoneTexture.py", line 369, in onFeatureSetChanged
    if node.GetDisplayNode().GetInputImageData().GetNumberOfScalarComponents() == 8:
AttributeError: 'NoneType' object has no attribute 'GetNumberOfScalarComponents'</code></pre>

---

## Post #2 by @lassoan (2020-06-18 20:02 UTC)

<p>This looks like the same error reported here:<br>
</p><aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Kitware/BoneTextureExtension/issues/22" target="_blank">github.com/Kitware/BoneTextureExtension</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Kitware/BoneTextureExtension/issues/22" target="_blank">Bonetexture in 3D Slicer won’t compute/display feature maps</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2019-10-16" data-time="14:40:49" data-timezone="UTC">02:40PM - 16 Oct 19 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lcw918" target="_blank">
          <img alt="lcw918" src="https://avatars2.githubusercontent.com/u/56546797?v=4" class="onebox-avatar-inline" width="20" height="20">
          lcw918
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">3dslicer: 4.10.02
Dell G7 7590
Win10 10.0.17763</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I’m not sure if maintainers of the extension read this topic, so it may be better to add a note there that you have this issue, too (and maybe add a link to this page).</p>
<p>Most probably the issue is trivial to fix (may be due to your data not being exactly the same kind as expected, Slicer API changes, etc.).</p>

---

## Post #3 by @Sam_Horvath (2020-06-19 19:08 UTC)

<p>I’ll be looking at this over the next week.</p>

---

## Post #4 by @muratmaga (2020-06-29 18:32 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> any updates on this?</p>

---

## Post #5 by @Sam_Horvath (2020-06-29 18:35 UTC)

<p>I should be able to get to it this week.</p>

---
