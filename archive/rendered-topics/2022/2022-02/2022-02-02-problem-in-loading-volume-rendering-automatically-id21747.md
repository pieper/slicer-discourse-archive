---
topic_id: 21747
title: "Problem In Loading Volume Rendering Automatically"
date: 2022-02-02
url: https://discourse.slicer.org/t/21747
---

# Problem in loading volume rendering automatically

**Topic ID**: 21747
**Date**: 2022-02-02
**URL**: https://discourse.slicer.org/t/problem-in-loading-volume-rendering-automatically/21747

---

## Post #1 by @user5 (2022-02-02 07:25 UTC)

<p>I would like to load the volume rendering automatically when I open the Slicer.</p>
<p>I follow the code in this link, but the volume rendering cannot load automatically.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccbda0a463723f46aa258833d53cf20d81ef11e1.jpeg" data-download-href="/uploads/short-url/tddG6cWUwpZgFQmRTIpKK85Byjn.jpeg?dl=1" title="截圖 2022-02-02 下午3.25.28" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ccbda0a463723f46aa258833d53cf20d81ef11e1_2_690x495.jpeg" alt="截圖 2022-02-02 下午3.25.28" data-base62-sha1="tddG6cWUwpZgFQmRTIpKK85Byjn" width="690" height="495" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ccbda0a463723f46aa258833d53cf20d81ef11e1_2_690x495.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ccbda0a463723f46aa258833d53cf20d81ef11e1_2_1035x742.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ccbda0a463723f46aa258833d53cf20d81ef11e1_2_1380x990.jpeg 2x" data-dominant-color="C5C4C6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截圖 2022-02-02 下午3.25.28</span><span class="informations">1688×1212 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How should I solve this error?</p>

---

## Post #2 by @ebrahim (2022-02-02 11:44 UTC)

<p>The code snippet you linked works for me when I include it in my <code>.slicerrc.py</code>, with volume rendering being enabled automatically when I load MRHead.</p>
<p>The error/warning displayed in your console may be due to something else in your <code>.slicerrc.py</code>, since <code>loadNodeFromFile</code> is not part of the code snippet you copied</p>

---

## Post #3 by @user5 (2022-02-02 12:24 UTC)

<p>My main error is the volume rendering cannot be enabled automatically. The warning displayed in my console is the warning of my other functions which is work normally. When I disable those functions, the automatic volume rendering still cannot work.</p>
<p>This is my code in <code>.slicerrc.py</code></p>
<pre><code class="lang-auto">import SampleData

def reportProgress(msg, level=None):
  # Print progress in the console
  print("Loading... {0}%".format(sampleDataLogic.downloadPercent))
  # Abort download if cancel is clicked in progress bar
  if slicer.progressWindow.wasCanceled:
    raise Exception("download aborted")
  # Update progress window
  slicer.progressWindow.show()
  slicer.progressWindow.activateWindow()
  slicer.progressWindow.setValue(int(sampleDataLogic.downloadPercent))
  slicer.progressWindow.setLabelText("Downloading...")
  # Process events to allow screen to refresh
  slicer.app.processEvents()

try:
  volumeNode = None
  slicer.progressWindow = slicer.util.createProgressDialog()
  sampleDataLogic = SampleData.SampleDataLogic()
  sampleDataLogic.logMessage = reportProgress
  loadedNodes = sampleDataLogic.downloadFromURL(
    nodeNames="MRHead",
    fileNames="MR-head25.nrrd",
    uris="https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/cc211f0dfd9a05ca3841ce1141b292898b2dd2d3f08286affadf823a7e58df93",
    checksums="SHA256:cc211f0dfd9a05ca3841ce1141b292898b2dd2d3f08286affadf823a7e58df93")
  volumeNode = loadedNodes[0]
finally:
  slicer.progressWindow.close()

def onNodeAdded(caller, event, calldata):
  node = calldata
  if isinstance(node, slicer.vtkMRMLVolumeNode):
    # Call showVolumeRendering using a timer instead of calling it directly
    # to allow the volume loading to fully complete.
    qt.QTimer.singleShot(0, lambda: showVolumeRendering(node))

def showVolumeRendering(volumeNode):
  print("Show volume rendering of node " + volumeNode.GetName())
  volRenLogic = slicer.modules.volumerendering.logic()
  displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)
  displayNode.SetVisibility(True)
  scalarRange = volumeNode.GetImageData().GetScalarRange()
  if scalarRange[1]-scalarRange[0] &lt; 1500:
    # Small dynamic range, probably MRI
    displayNode.GetVolumePropertyNode().Copy(volRenLogic.GetPresetByName("MR-Default"))
  else:
    # Larger dynamic range, probably CT
    displayNode.GetVolumePropertyNode().Copy(volRenLogic.GetPresetByName("CT-Chest-Contrast-Enhanced"))

slicer.mrmlScene.AddObserver(slicer.vtkMRMLScene.NodeAddedEvent, onNodeAdded)

</code></pre>
<p>This is the result now.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89fba684af374eeb1e14e3ad4a2f7489525da439.jpeg" data-download-href="/uploads/short-url/jGEzt4GmWT82eU4Tm26m8k2ZmWt.jpeg?dl=1" title="截圖 2022-02-02 下午8.34.59" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89fba684af374eeb1e14e3ad4a2f7489525da439_2_690x494.jpeg" alt="截圖 2022-02-02 下午8.34.59" data-base62-sha1="jGEzt4GmWT82eU4Tm26m8k2ZmWt" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89fba684af374eeb1e14e3ad4a2f7489525da439_2_690x494.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89fba684af374eeb1e14e3ad4a2f7489525da439_2_1035x741.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89fba684af374eeb1e14e3ad4a2f7489525da439_2_1380x988.jpeg 2x" data-dominant-color="C5C5C7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截圖 2022-02-02 下午8.34.59</span><span class="informations">1686×1208 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is my code has anything wrong?</p>

---

## Post #4 by @ebrahim (2022-02-02 12:48 UTC)

<p>The decorator <code>@vtk.calldata_type(vtk.VTK_OBJECT)</code> is missing above <code>onNodeAdded</code></p>

---

## Post #5 by @user5 (2022-02-02 12:58 UTC)

<p>I thought that the first line is useless <img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=12" title=":joy:" class="emoji" alt=":joy:">.<br>
It works now. Thanks you so much.</p>

---
