# Loading MRB file breaks linked views

**Topic ID**: 5951
**Date**: 2019-02-27
**URL**: https://discourse.slicer.org/t/loading-mrb-file-breaks-linked-views/5951

---

## Post #1 by @smrolfe (2019-02-27 21:02 UTC)

<p>This issue can be replicated using by the following steps:</p>
<ul>
<li>load MRIHead and render in Dual 3D</li>
<li>save as an MRB file</li>
<li>reopen Slicer, load MRB file</li>
<li>use link/unlink buttons in 3D view windows to link views</li>
</ul>
<p>The viewers cannot be linked. When the MRB file is loaded, 2 additional cameras are loaded and associated with the 3D views. The link problem can be resolved by deleting one or both of these cameras:</p>
<blockquote>
<p>c1=slicer.mrmlScene.GetNodeByID(‘vtkMRMLCameraNode1’)<br>
c2=slicer.mrmlScene.GetNodeByID(‘vtkMRMLCameraNode2’)<br>
c3=slicer.mrmlScene.GetNodeByID(‘vtkMRMLCameraNode3’)<br>
c4=slicer.mrmlScene.GetNodeByID(‘vtkMRMLCameraNode4’)<br>
slicer.mrmlScene.RemoveNode(c3)<br>
slicer.mrmlScene.RemoveNode(c4)</p>
</blockquote>
<p>Deactivating these same cameras, or associating cameras 1 and 2 with the 3D views does not have an effect. Any insight on how the cameras/views are working would be appreciated. If this is not a known issue, I can start a bug report.</p>

---

## Post #2 by @ezgimercan (2020-04-22 20:13 UTC)

<p>I have a similar problem and I am wondering if it is a known issue.<br>
I usually save MRB files when I am working on a complex visualization. However, if I have double 3D views with different volumes rendered in each, loading the saved MRB file does not setup the same render options. I often end up having both volumes rendered in View1. There is no data loss but the volumes, fiducials and segmentations that are set to be rendered in View2 window are all back in View1 and it defeats the purpose of setting everything nicely and saving an MRB.</p>

---

## Post #3 by @lassoan (2020-04-22 20:25 UTC)

<p>We have an issue in the bugtracker for this, scheduled to be fixed in Slicer5 (planned within a few weeks). What you experience might be related, so please add it as comment to the issue:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/4680" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4680" target="_blank">Loading MRB file breaks linked views</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-13" data-time="01:05:05" data-timezone="UTC">01:05AM - 13 Mar 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
