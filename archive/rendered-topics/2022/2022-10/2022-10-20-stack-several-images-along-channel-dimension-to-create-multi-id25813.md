# Stack several images along channel dimension to create multichannel images (e.g. 4D volume)

**Topic ID**: 25813
**Date**: 2022-10-20
**URL**: https://discourse.slicer.org/t/stack-several-images-along-channel-dimension-to-create-multichannel-images-e-g-4d-volume/25813

---

## Post #1 by @mangotee (2022-10-20 15:19 UTC)

<p>Hi,<br>
I sometimes need to stack several 2D/3D images/volumes along the channel dimension, create a multichannel image and save it as a 4D Nifti/Nrrd. For simplicity’s sake, you can assume that I already have co-registered the images, and that they are all resampled into the first image’s pixel/voxel grid as reference. Fwiw, I know how to convert the images to numpy arrays and stack them along a channel dimension, but I don’t know how to create a new multichannel volume from that and make sure that it has an identical geometry as in the reference image header.<br>
Thanks for any tips in advance!<br>
Best,<br>
Ahmad</p>

---

## Post #2 by @lassoan (2022-10-20 16:02 UTC)

<aside class="quote no-group" data-username="mangotee" data-post="1" data-topic="25813">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c57346/48.png" class="avatar"> mangotee:</div>
<blockquote>
<p>w to convert the images to numpy arrays and stack them along a channel dimension, but I don’t know how to create a new multichannel volume from that and make sure that it has an identical geometry as</p>
</blockquote>
</aside>
<p>You can use sequences for this. If all the volumes in the sequence have the same geometry then they will be saved as a single 4D nrrd file. You can pick one of the channels and display it in the scene by adding a sequence browser node for each. See examples for getting/setting data in sequences in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#sequences">script repository</a>.</p>
<p>Alternatively, you can store all the channels in a single vector volume. For example, you can create a 6-channel volume with random content like this:</p>
<pre data-code-wrap="python"><code class="lang-python">import numpy as np
volumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLVectorVolumeNode')
voxels = np.random.rand(3,4,5,6)
slicer.util.updateVolumeFromArray(volumeNode, voxels)
</code></pre>
<p>The disadvantage is that you cannot easily browse the channels but for example you can extract any of them using the “Vector to scalar volume” module (or in Python, using <code>slicer.util.arrayFromVolume()</code>).</p>

---

## Post #3 by @mangotee (2022-10-24 11:04 UTC)

<p>Hi Andreas,</p>
<p>thanks for the tip. If I use your numpy-based code example…:</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="25813">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">import numpy as np
volumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLVectorVolumeNode')
voxels = np.random.rand(3,4,5,6)
slicer.util.updateVolumeFromArray(volumeNode, voxels)
</code></pre>
</blockquote>
</aside>
<p>…, except that <code>voxels</code> is a stacked 4D array volume <code>[0,1,2,...,N]</code>, how would I assign the same reference geometry as e.g. <code>volume0</code> to the newly-created <code>volumeNode</code>, such that when I save that node as Nifti/Nrrd, it would overlap perfectly with <code>volume0</code>?</p>

---

## Post #4 by @lassoan (2022-10-24 11:42 UTC)

<p>You also need set the image geometry, by copying it from the original image:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/415aee60cdb6b23dad60ddf874216139c499453d/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py#L411-L413">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/415aee60cdb6b23dad60ddf874216139c499453d/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py#L411-L413" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/415aee60cdb6b23dad60ddf874216139c499453d/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py#L411-L413" target="_blank" rel="noopener">Slicer/Slicer/blob/415aee60cdb6b23dad60ddf874216139c499453d/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py#L411-L413</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="411" style="counter-reset: li-counter 410 ;">
          <li>ijkToRAS = vtk.vtkMatrix4x4()</li>
          <li>inputVolumeNode.GetIJKToRASMatrix(ijkToRAS)</li>
          <li>outputVolumeNode.SetIJKToRASMatrix(ijkToRAS)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
