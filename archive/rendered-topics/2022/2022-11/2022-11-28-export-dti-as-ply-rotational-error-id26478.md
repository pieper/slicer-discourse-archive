---
topic_id: 26478
title: "Export Dti As Ply Rotational Error"
date: 2022-11-28
url: https://discourse.slicer.org/t/26478
---

# Export DTI as Ply rotational error

**Topic ID**: 26478
**Date**: 2022-11-28
**URL**: https://discourse.slicer.org/t/export-dti-as-ply-rotational-error/26478

---

## Post #1 by @yuanci (2022-11-28 13:14 UTC)

<p>Hi,</p>
<p>I’m still trying to figure out the full capabilities of Slicer, and just recently started using the DMRI extension. I tried to export a tract as PLY using the “Export tractography to PLY (mesh)” tool but every time I export it I notice it has been rotated 180 degrees about the Z axis when I open it in another 3D program such as Blender. Is there a step I’m missing or something I’m not taking to account?</p>
<p>Thanks in advance,<br>
Leanne</p>

---

## Post #2 by @lassoan (2022-11-28 15:21 UTC)

<p>That code snippet exports the tracts as they are in the scene, in RAS coordinate system. If you need the mesh in LPS coordinate system then you can invert the sign of the first two coordinate components. I’ve updated the example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-tract-fiberbundle-to-blender-including-color">here</a>.</p>

---

## Post #3 by @yuanci (2022-12-10 18:50 UTC)

<p>Thanks for the reply, but I don’t know how to follow the instructions on that link. I found the “TractographyExportPLY.py” is this something I need to modify on that file?</p>

---

## Post #4 by @pieper (2022-12-10 19:00 UTC)

<p><a class="mention" href="/u/yuanci">@yuanci</a> -the feature in SlicerDMRI was implemented based on the script example that <a class="mention" href="/u/lassoan">@lassoan</a> pointed to.  He updated the example, but to update the module the same change needs to be made here <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/366d232d8406479fe2ec9fbd391d55978c2dfc11/Modules/Scripted/TractographyExportPLY/TractographyExportPLY.py#L164-L224">in the SlicerDMRI source code</a>. Is there any chance you could make the change, test it, and submit a pull request to SlicerDMRI?  If that’s not something you are familiar with probably someone else can easily do it.</p>
<p>Note the LPS/RAS distinction is <a href="https://www.slicer.org/wiki/Coordinate_systems">described here</a>.</p>

---

## Post #5 by @yuanci (2022-12-10 20:01 UTC)

<p>Figured it out! Thank you so much for the input</p>
<p>I defined the global variable after the imports</p>
<blockquote>
<p>outputCoordinateSystem = “LPS”</p>
</blockquote>
<p>Then I replaced line 206 of the “TractographyExportPLY.py”<br>
From</p>
<blockquote>
<p>plyWriter.SetInputData(triangles.GetOutput())</p>
</blockquote>
<p>To</p>
<blockquote>
<p>if outputCoordinateSystem == “RAS”:<br>
plyWriter.SetInputData(triangles.GetOutput())<br>
elif outputCoordinateSystem == “LPS”:<br>
transformRasToLps = vtk.vtkTransformPolyDataFilter()<br>
rasToLps = vtk.vtkTransform()<br>
rasToLps.Scale(-1, -1, 1)<br>
transformRasToLps.SetTransform(rasToLps)<br>
transformRasToLps.SetInputData(triangles.GetOutput())<br>
plyWriter.SetInputConnection(transformRasToLps.GetOutputPort())<br>
else:<br>
raise RuntimeError(“Invalid output coordinate system”)</p>
</blockquote>

---

## Post #6 by @lassoan (2022-12-10 21:14 UTC)

<p>Could you please add a <code>outputCoordinateSystem == "RAS"</code> argument to <code>exportFiberBundleToPLYPath</code>, test if it all works well, and then send a pull request with the change? You can create a pull request very easily by editing the .py file directly in github and answering yes to when you are asked if you want to fork the repository, create a branch, and submit a pull request.</p>

---

## Post #7 by @yuanci (2022-12-10 22:34 UTC)

<p>It does work! It doesn’t allow me to edit the .py file on github, but I have the .py file here: <a href="https://www.dropbox.com/s/y8dvbibgrbc2s1v/TractographyExportPLY.py?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - TractographyExportPLY.py - Simplify your life</a></p>

---

## Post #8 by @lassoan (2022-12-11 04:38 UTC)

<p>Thank you. I’ve polished it a bit (use None as default to prevent overwriting default; write coordinate system information to image header) and created a pull request:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/SlicerDMRI/SlicerDMRI/pull/162">
  <header class="source">

      <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/162" target="_blank" rel="noopener">github.com/SlicerDMRI/SlicerDMRI</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/162" target="_blank" rel="noopener">Save tracts in LPS coordinate system</a>
      </h4>

    <div class="branches">
      <code>SlicerDMRI:master</code> ← <code>lassoan:patch-1</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-12-11" data-time="04:35:51" data-timezone="UTC">04:35AM - 11 Dec 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 22 additions and 3 deletions">
          <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/162/files" target="_blank" rel="noopener">
            <span class="added">+22</span>
            <span class="removed">-3</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Images are saved in LPS coordinate system to be consistent with image coordinate<span class="show-more-container"><a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/162" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> system.

See discussion here: https://discourse.slicer.org/t/export-dti-as-ply-rotational-error/26478/5</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
