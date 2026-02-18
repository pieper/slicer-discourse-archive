# Proxy Node Attributes lost after scene load

**Topic ID**: 31607
**Date**: 2023-09-07
**URL**: https://discourse.slicer.org/t/proxy-node-attributes-lost-after-scene-load/31607

---

## Post #1 by @pfrwilson (2023-09-07 18:16 UTC)

<p>I have created a sequence, sequence browser and proxy volume node. I gave the proxy volume node a whole bunch of attributes. However, after reloading the scene, the only attribute that is reloaded into the node is the Sequences.BaseName attribute.</p>
<p>Is this a bug? Is there a way to ensure that the node attributes will be preserved throughout scene save/reload?</p>
<p>Any help is greatly appreciated!</p>
<p>Here is how I initially set up the volume node:</p>
<pre><code class="lang-python">volume = slicer.mrmlScene.AddNewNodeByClass(
    "vtkMRMLScalarVolumeNode",
    f"BMode_volume_{cineloop_number}",
)
volume.SetSpacing(bimg_spacing)
for name, parameter in params.items():
    volume.SetAttribute(name, str(parameter))
    volume.SetAttribute('SlicerExactVu.loadedAsType', 'Volume')
    volume.SetAttribute('SlicerExactVu.loadedFromPath', bimg_path)
    volume.SetAttribute('cineloop_number', cineloop_number)
</code></pre>
<p>At each step I updated its data using <code>slicer.util.updateVolumeFromArray</code>.</p>
<p>Paul</p>

---

## Post #2 by @lassoan (2023-09-07 18:29 UTC)

<p>When a volume sequence is saved in .mrb format then all the attributes are preserved. However, currently saving of custom attributes is not implemented in the volume sequence reader, which saves the volume sequence in .seq.nrrd format. It would make sense to implement this - I’ve submitted a feature request to track this task:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7218">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7218" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7218" target="_blank" rel="noopener">Save custom node attributes in volume sequence (.seq.nrrd) files</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-09-07" data-time="18:25:55" data-timezone="UTC">06:25PM - 07 Sep 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Is your feature request related to a problem? Please describe.

When a volu<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">me sequence is saved in MRML sequence bundle (.seq.mrb) format then all the node attributes are preserved.

However, currently saving of custom attributes is not implemented in the volume sequence reader, which saves the volume sequence in .seq.nrrd format.

## Describe the solution you'd like

When a sequence of volumes are saved, volume node attributes should be saved in the .nrrd file.

## Additional context

See user error report here: https://discourse.slicer.org/t/proxy-node-attributes-lost-after-scene-load/31607</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>We’ll probably need this for one of the funded projects at some point, but if you can make any contributions (ideally implement attribute saving/reading in the storage node) then it can happen sooner.</p>
<p>In the meantime, you can force saving into .mrb format (zip file containing each volume as a separate file and a .mrml file storing the node attributes) like this:</p>
<pre><code class="lang-python">storageNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSequenceStorageNode')
getNode('Sequence').SetAndObserveStorageNodeID(storageNode.GetID())
</code></pre>

---

## Post #3 by @pfrwilson (2023-09-08 17:30 UTC)

<p>Thanks so much Andras, the suggested quick fix worked perfectly.</p>
<p>I unfortunately don’t have the bandwidth to help with the feature request right now, but i’ll pay attention in case I do get the time.</p>
<p>Paul</p>

---
