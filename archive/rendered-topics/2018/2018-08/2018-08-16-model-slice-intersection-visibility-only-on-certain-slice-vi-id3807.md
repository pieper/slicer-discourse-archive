# Model slice intersection visibility - only on certain slice views

**Topic ID**: 3807
**Date**: 2018-08-16
**URL**: https://discourse.slicer.org/t/model-slice-intersection-visibility-only-on-certain-slice-views/3807

---

## Post #1 by @mschumaker (2018-08-16 21:55 UTC)

<p>I have a 3D model that I would like to display as intersections on some 2D slice views, but hide it on another. I have a vtkMRMLModelNode called arteryModelNode:</p>
<blockquote>
<p>arteryModelDisplayNode = arteryModelNode.GetModelDisplayNode()<br>
arteryModelDisplayNode.SetSliceIntersectionVisibility(True)</p>
</blockquote>
<p>Below is an image. I want the intersection to show on the Red, Green, and Yellow slices, but not on the grey one “S1”. Is there a way to do this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f69e2f5f387bac1bc5a78654ece48530c22980d4.jpeg" data-download-href="/uploads/short-url/zbGmNawfrd1iM6lQhtdtNvoJFly.jpeg?dl=1" title="intersection-question-arrow" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f69e2f5f387bac1bc5a78654ece48530c22980d4_2_690x384.jpeg" alt="intersection-question-arrow" data-base62-sha1="zbGmNawfrd1iM6lQhtdtNvoJFly" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f69e2f5f387bac1bc5a78654ece48530c22980d4_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f69e2f5f387bac1bc5a78654ece48530c22980d4_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f69e2f5f387bac1bc5a78654ece48530c22980d4_2_1380x768.jpeg 2x" data-dominant-color="635D5F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">intersection-question-arrow</span><span class="informations">2798×1560 630 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2018-08-17 13:09 UTC)

<p>Hi <a class="mention" href="/u/mschumaker">@mschumaker</a> -</p>
<p>Yes, if you explicitly set the view node ids where you want a displayable to appear it won’t be shown in the others.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/e776b54bf2d07a2d6addc32ed2b72a91040c621b/Libs/MRML/Core/vtkMRMLDisplayNode.h#L437-L475" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/e776b54bf2d07a2d6addc32ed2b72a91040c621b/Libs/MRML/Core/vtkMRMLDisplayNode.h#L437-L475" target="_blank">Slicer/Slicer/blob/e776b54bf2d07a2d6addc32ed2b72a91040c621b/Libs/MRML/Core/vtkMRMLDisplayNode.h#L437-L475</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="437" style="counter-reset: li-counter 436 ;">
<li>/// Add View Node ID for the view to display this node in.</li>
<li>/// \sa ViewNodeIDs, RemoveViewNodeID(), RemoveAllViewNodeIDs()</li>
<li>void AddViewNodeID(const char* viewNodeID);</li>
<li>/// Remove View Node ID for the view to display this node in.</li>
<li>/// \sa ViewNodeIDs, AddViewNodeID(), RemoveAllViewNodeIDs()</li>
<li>void RemoveViewNodeID(char* viewNodeID);</li>
<li>/// Remove All View Node IDs for the views to display this node in.</li>
<li>/// \sa ViewNodeIDs, AddViewNodeID(), RemoveViewNodeID()</li>
<li>void RemoveAllViewNodeIDs();</li>
<li>/// Get number of View Node ID's for the view to display this node in.</li>
<li>/// If 0, display in all views</li>
<li>/// \sa ViewNodeIDs, GetViewNodeIDs(), AddViewNodeID()</li>
<li>inline int GetNumberOfViewNodeIDs()const;</li>
<li>/// Get View Node ID's for the view to display this node in.</li>
<li>/// If NULL, display in all views</li>
<li>/// \sa ViewNodeIDs, GetViewNodeIDs(), AddViewNodeID()</li>
<li>const char* GetNthViewNodeID(unsigned int index);</li>
<li>/// Get all View Node ID's for the view to display this node in.</li>
<li>/// If empty, display in all views</li>
<li>/// \sa ViewNodeIDs, GetNthViewNodeID(), AddViewNodeID()</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/e776b54bf2d07a2d6addc32ed2b72a91040c621b/Libs/MRML/Core/vtkMRMLDisplayNode.h#L437-L475" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I don’t know if there’s a model slice intersection example, but here’s how it works for fiducials:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/pieper/LandmarkRegistration/blob/master/LandmarkRegistration.py#L480-L518" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/LandmarkRegistration/blob/master/LandmarkRegistration.py#L480-L518" target="_blank">pieper/LandmarkRegistration/blob/master/LandmarkRegistration.py#L480-L518</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="480" style="counter-reset: li-counter 479 ;">
<li>def restrictLandmarksToViews(self):</li>
<li>  """Set fiducials so they only show up in the view</li>
<li>  for the volume on which they were defined.</li>
<li>  Also turn off other fiducial lists, since leaving</li>
<li>  them visible can interfere with picking.</li>
<li>  Since multiple landmarks will be in the same lists, keep track of the</li>
<li>  lists that have been processed to avoid duplicated updates.</li>
<li>  """</li>
<li>  slicer.mrmlScene.StartState(slicer.mrmlScene.BatchProcessState)</li>
<li>  volumeNodes = self.currentVolumeNodes()</li>
<li>  if self.sliceNodesByViewName:</li>
<li>    landmarks = self.logic.landmarksForVolumes(volumeNodes)</li>
<li>    activeFiducialLists = []</li>
<li>    processedFiducialLists = []</li>
<li>    for landmarkName in landmarks:</li>
<li>      for fiducialList,index in landmarks[landmarkName]:</li>
<li>        if fiducialList in processedFiducialLists:</li>
<li>          continue</li>
<li>        processedFiducialLists.append(fiducialList)</li>
<li>        activeFiducialLists.append(fiducialList)</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/pieper/LandmarkRegistration/blob/master/LandmarkRegistration.py#L480-L518" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @mschumaker (2018-08-17 16:24 UTC)

<p>Thank you! That’s exactly what I was looking for.</p>

---
