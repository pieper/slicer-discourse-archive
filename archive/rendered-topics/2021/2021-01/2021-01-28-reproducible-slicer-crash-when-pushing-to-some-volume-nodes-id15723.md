---
topic_id: 15723
title: "Reproducible Slicer Crash When Pushing To Some Volume Nodes"
date: 2021-01-28
url: https://discourse.slicer.org/t/15723
---

# Reproducible Slicer crash when pushing to some volume nodes using sitkUtils PushVolumeToSlicer

**Topic ID**: 15723
**Date**: 2021-01-28
**URL**: https://discourse.slicer.org/t/reproducible-slicer-crash-when-pushing-to-some-volume-nodes-using-sitkutils-pushvolumetoslicer/15723

---

## Post #1 by @mikebind (2021-01-28 19:40 UTC)

<p>I have run into a reproducible Slicer crash when using sitkUtils PushVolumeToSlicer().  If the output volume node exists and has some characteristic, then Slicer crashes.  I have not been able to figure out what the characteristic is which leads to the crash, but I have several example volumes that this occurs for.  The crash does not occur for the MRHead example volume.</p>
<p>The crash also occurs when using the SimpleFilters module, so it does not have to do with my code. Any time one of these volumes is selected as the “Output Volume”, running the filter leads to a crash.</p>
<p>If I crop one of the suspect volumes using the CropVolume module, the cropped version works fine as an “Output Volume” of the SimpleFilters module and in my code; it is only the uncropped original which causes problems.  It also works fine if one of the problem volumes is the “Input Volume” for the filter, the problem only occurs if a problem volume is set as the “Output Volume”.</p>
<p>I have an anonymized minimal data set that can demonstrate the problem, but it is a head MR which includes the face, so I cannot share it publicly, and when I modify it (e.g. by cropping) the crash no longer occurs.  If someone can take a look at this privately I would greatly appreciate it. Thanks!</p>

---

## Post #2 by @mikebind (2021-01-28 22:49 UTC)

<p>I found a workaround.  I created a temporary node, applied the filter so that the output went to the temporary node, and then linked the problematic node to the temporary node’s imagedata, and then removed the temporary node.  This did not lead to a crash.</p>
<pre><code># Code used for exploring SITK crash bug
import SimpleITK as sitk
import sitkUtils

inputVolNode = getNode('vtkMRMLScalarVolumeNode130')
tempNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode', 'tempVol')

wantACrash = False # change to true if you want a crash

inputImage = sitkUtils.PullVolumeFromSlicer(inputVolNode)
filt = sitk.NormalizeImageFilter()
outputImage = filt.Execute(inputImage)
if wantACrash:
  # The next line causes a crash
  sitkUtils.PushVolumeToSlicer(outputImage, inputVolNode)
else:
  # This section causes no problems
  sitkUtils.PushVolumeToSlicer(outputImage, tempNode)
  inputVolNode.SetAndObserveImageData(tempNode.GetImageData())
  slicer.mrmlScene.RemoveNode(tempNode)</code></pre>

---

## Post #3 by @mikebind (2021-01-29 16:33 UTC)

<p>After some investigation, it was determined that the “Sandbox” extension is the culprit.  Disabling that extension is another way to avoid the crash.</p>

---

## Post #4 by @lassoan (2021-01-29 23:02 UTC)

<p>The root cause of the problem has been fixed now:</p>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/ed9ba08ed724acbd173233357385e26ca05454eb" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/ed9ba08ed724acbd173233357385e26ca05454eb" target="_blank" rel="noopener">BUG: Remove node modified calls from background thread</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2021-01-29" data-time="21:25:37" data-timezone="UTC">09:25PM - 29 Jan 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
        
      </div>

      <div class="lines" title="changed 6 files with 187 additions and 90 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/ed9ba08ed724acbd173233357385e26ca05454eb" target="_blank" rel="noopener">
          <span class="added">+187</span>
          <span class="removed">-90</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">Problem:
itkMRMLIDImageIO is used in a background thread when running CLI modules or Simple Filters module and it called node Modified events...</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
