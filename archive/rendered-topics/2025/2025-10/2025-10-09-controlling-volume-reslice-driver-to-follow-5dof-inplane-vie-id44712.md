---
topic_id: 44712
title: "Controlling Volume Reslice Driver To Follow 5Dof Inplane Vie"
date: 2025-10-09
url: https://discourse.slicer.org/t/44712
---

# Controlling Volume Reslice Driver to follow 5DOF inplane view of tool

**Topic ID**: 44712
**Date**: 2025-10-09
**URL**: https://discourse.slicer.org/t/controlling-volume-reslice-driver-to-follow-5dof-inplane-view-of-tool/44712

---

## Post #1 by @ruffsl (2025-10-09 19:01 UTC)

<p>I’d like show a 5DOF inplane view of needle using the Volume Reslice Driver extension, with the 6th DOF rotation locked in alignment with respect to a canonical axis in the global RAS reference frame, providing a more grounded view of tool paths that remain orientated with respect to the volume.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerIGT/SlicerIGT/tree/master/VolumeResliceDriver">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/SlicerIGT/SlicerIGT/tree/master/VolumeResliceDriver" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerIGT/SlicerIGT/tree/master/VolumeResliceDriver" target="_blank" rel="noopener nofollow ugc">SlicerIGT/VolumeResliceDriver at master · SlicerIGT/SlicerIGT</a></h3>


  <p><span class="label1">Modules supporting image-guided interventions in 3D Slicer. - SlicerIGT/SlicerIGT</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>While the <code>VolumeResliceDriver</code> easily allows for controlling slice views relative to 6DOF pose transforms, as well as with respect to 3 additional orthogonal axis - either fixed to the global RAS reference frame or the relative to tracked transform itself, the fixed RAS modes are useful in only tracking the 3DOF point of a tool tip, while the relative inplane modes are a little too disorientating for real time use. Thus, I’d like to replicate a hybrid of the two modes, that may be common among many IGT visualizations, by locking one rotation axis of an inline slice view to a chosen RAS axis.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b768081ea5c2ec9e0e2c390d06584570e80eef98.jpeg" data-download-href="/uploads/short-url/qaugmTbFlFzeN65q9nu86GcSXi0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b768081ea5c2ec9e0e2c390d06584570e80eef98_2_690x388.jpeg" alt="image" data-base62-sha1="qaugmTbFlFzeN65q9nu86GcSXi0" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b768081ea5c2ec9e0e2c390d06584570e80eef98_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b768081ea5c2ec9e0e2c390d06584570e80eef98_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b768081ea5c2ec9e0e2c390d06584570e80eef98_2_1380x776.jpeg 2x" data-dominant-color="6B6A70"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9982e9c60f7d87ab42ef9da773967d9f92debb16.jpeg" data-download-href="/uploads/short-url/lU1x3vjw8oWZw4bGhY7vOc5rfbU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9982e9c60f7d87ab42ef9da773967d9f92debb16_2_690x388.jpeg" alt="image" data-base62-sha1="lU1x3vjw8oWZw4bGhY7vOc5rfbU" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9982e9c60f7d87ab42ef9da773967d9f92debb16_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9982e9c60f7d87ab42ef9da773967d9f92debb16_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9982e9c60f7d87ab42ef9da773967d9f92debb16_2_1380x776.jpeg 2x" data-dominant-color="6E6D70"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0c492323945d37cf0f4df68ba2a8d2cbc4f167d.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b73362d23533e598247151413dc597b89d71f63f.jpeg" data-video-base62-sha1="rviPcPWjDmW1etHPFVNZ6dX5Jwx.mp4">
  </div><p></p>
<p>Via scripting, I could publish the aligned transforms for each RAS axis variant for a given tool:</p>
<pre data-code-wrap="python"><code class="lang-python">"""
============================
Position sending server
============================

Simple application that starts a server that provides a stream of tool trajectories.

from slicer.util import pip_install
pip_install("pyigtl")

Adapted from:
https://github.com/lassoan/pyigtl/blob/d28132d8e9e1cef4ac531d795f5284c8aa739408/examples/example_position_server.py
https://github.com/lassoan/pyigtl/blob/d28132d8e9e1cef4ac531d795f5284c8aa739408/pyigtl/tests/test_basic_comm.py#L87-L93
"""

import pyigtl 

from time import sleep
import numpy as np
from scipy.spatial.transform import Rotation as R

server = pyigtl.OpenIGTLinkServer(port=18944)

timestep = 0
while True:
    if not server.is_connected():
        # Wait for client to connect
        sleep(0.1)
        continue

    # Generate periodic trajectory: Lissajous curve on sphere
    timestep += 1
    radius = 50.0
    center = np.array([0.0, 0.0, -100.0])
    # Use two periodic angles for smooth looping
    phi = (timestep * 0.001) % (2 * np.pi)  # azimuthal
    theta = (timestep * 0.002) % (2 * np.pi) # polar
    x = center[0] + radius * np.sin(theta) * np.cos(phi)
    y = center[1] + radius * np.sin(theta) * np.sin(phi)
    z = center[2] + radius * np.cos(theta)
    position = np.array([x, y, z])

    # Orientation: always point toward center
    forward = center - position
    forward = forward / np.linalg.norm(forward)
    # Create a rotation that aligns Z axis with 'forward'
    align_rot, _ = R.align_vectors([forward], [[0, 0, 1]])
    # Add a twist around the forward axis (drill bit effect)
    twist_rot = R.from_rotvec(theta * 10 * forward)
    # Compose the two rotations: first align, then twist
    rot_obj = twist_rot * align_rot
    rot_matrix = rot_obj.as_matrix()
    # Build 4x4 transform
    tf = np.eye(4)
    tf[:3, :3] = rot_matrix
    tf[:3, 3] = position

    tf_axial = tf.copy()
    # Project 'forward' onto RS plane (zero A component)
    f_proj = forward.copy()
    f_proj[1] = 0
    # Directly align projected vector to Z axis (no need to normalize)
    axial_rot, _ = R.align_vectors([f_proj], [[0, 0, 1]])
    tf_axial[:3, :3] = axial_rot.as_matrix()

    tf_sagittal = tf.copy()
    # Project 'forward' onto SA plane (zero R component)
    f_proj = forward.copy()
    f_proj[2] = 0
    # Directly align projected vector to X axis (no need to normalize)
    sagittal_rot, _ = R.align_vectors([f_proj], [[1, 0, 0]])
    tf_sagittal[:3, :3] = sagittal_rot.as_matrix()

    tf_coronal = tf.copy()
    # Project 'forward' onto AR plane (zero S component)
    f_proj = forward.copy()
    f_proj[0] = 0
    # Directly align projected vector to Y axis (no need to normalize)
    coronal_rot, _ = R.align_vectors([f_proj], [[0, 1, 0]])
    tf_coronal[:3, :3] = coronal_rot.as_matrix()

    tf_msg = pyigtl.TransformMessage(tf, device_name='ToolToRAS')
    server.send_message(tf_msg, wait=True)
    tf_msg = pyigtl.TransformMessage(tf_axial, device_name='ToolOnAxial')
    server.send_message(tf_msg, wait=True)
    tf_msg = pyigtl.TransformMessage(tf_sagittal, device_name='ToolOnSagittal')
    server.send_message(tf_msg, wait=True)
    tf_msg = pyigtl.TransformMessage(tf_coronal, device_name='ToolOnCoronal')
    server.send_message(tf_msg, wait=True)
    # Since we wait until the message is actually sent, the message queue will not be flooded
</code></pre>
<p>However, that seems a little excessive in practice, as I’d also like to re-use the <code>Stabilize</code> processing mode via <code>TransformProcessor</code> for low pass filtering of noise from navigation tracking. I tried playing around with the various other processing modes provided by <code>TransformProcessor</code> to collocate all aligned transform computation within Slicer 3D fronted itself, simplifying the use <code>Stabilize</code>d transform trees, but couldn’t figure out how to replicate the same alignment as above in python.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerIGT/SlicerIGT/tree/master/TransformProcessor">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/SlicerIGT/SlicerIGT/tree/master/TransformProcessor" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerIGT/SlicerIGT/tree/master/TransformProcessor" target="_blank" rel="noopener nofollow ugc">SlicerIGT/TransformProcessor at master · SlicerIGT/SlicerIGT</a></h3>


  <p><span class="label1">Modules supporting image-guided interventions in 3D Slicer. - SlicerIGT/SlicerIGT</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Any suggestions using <code>TransformProcessor</code>, or adding such a mode to <code>VolumeResliceDriver</code>?</p>

---

## Post #2 by @ungi (2025-10-10 15:27 UTC)

<p>There is no explicit representation of a 5DOF transformation in Slicer, so I wouldn’t update either VolumeResliceDriver or TransformProcessor. I think 5DOF transformations are relatively rare, the only application I can think of is Aurora needle trackers. I would just observe the incoming “5DOF” transform and run a script like the one you have to convert it to a regular transform every time it updates. And use the modules with that recomputed transform. Is there anything that prevents you from doing that?</p>

---

## Post #3 by @ruffsl (2025-10-10 19:48 UTC)

<aside class="quote no-group" data-username="ungi" data-post="2" data-topic="44712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ungi/48/78573_2.png" class="avatar"> ungi:</div>
<blockquote>
<p>There is no explicit representation of a 5DOF transformation in Slicer</p>
</blockquote>
</aside>
<p>They are expressed in the Bullseye View Mode for the external <a href="https://github.com/SlicerIGT/SlicerIGT/tree/master/Viewpoint" rel="noopener nofollow ugc"><code>Viewpoint</code></a> extension in SlicerIGT:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4ae9de55d8c3942e4a02c0630235d365409bb791.png" data-download-href="/uploads/short-url/aGIopBzF7TkdT9CcYFRNAmtFpg5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4ae9de55d8c3942e4a02c0630235d365409bb791_2_376x500.png" alt="image" data-base62-sha1="aGIopBzF7TkdT9CcYFRNAmtFpg5" width="376" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4ae9de55d8c3942e4a02c0630235d365409bb791_2_376x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4ae9de55d8c3942e4a02c0630235d365409bb791_2_564x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4ae9de55d8c3942e4a02c0630235d365409bb791.png 2x" data-dominant-color="383839"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">584×775 57.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But, yeah, that’s more of an end use case rather than an standard slicer data node type.</p>
<aside class="quote no-group" data-username="ungi" data-post="2" data-topic="44712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ungi/48/78573_2.png" class="avatar"> ungi:</div>
<blockquote>
<p>I think 5DOF transformations are relatively rare, the only application I can think of is Aurora needle trackers.</p>
</blockquote>
</aside>
<p>Wow, I figured it’d be more common, like for elongated tools and volume path views in general.</p>
<aside class="quote no-group" data-username="ungi" data-post="2" data-topic="44712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ungi/48/78573_2.png" class="avatar"> ungi:</div>
<blockquote>
<p>I would just observe the incoming “5DOF” transform and run a script like the one you have to convert it to a regular transform every time it updates. And use the modules with that recomputed transform. Is there anything that prevents you from doing that?</p>
</blockquote>
</aside>
<p>Suppose I could bundle this into the our existing python extension, but was hoping this would already have been available out-of-the-box using a combination of existing IGT extensions. I mostly just wanted to offload this kind of 5DOF computation until after the <code>TransformProcessor</code> has had the chance to apply a low pass noise filter to the main child transform, thus avoid any round trip data flows out and in of Slicer 3D, like with the <code>pyigtl</code> example above.</p>
<hr>
<p>As an aside <a class="mention" href="/u/ungi">@ungi</a> , would you have any suggestions to avoid the jarring discontinuity of the current approach when the z axis of the tool lines up with any RAS axis of the volume? The relative rotation around the 6th axis for the 5DOF transform flips 180 degrees when passing through such Euler angle singularities.</p>
<p>Perhaps there’s better public examples using quaternion for computing 5DOF projections?</p>
<p>Suppose I could borrow from the workaround applied in Viewpoint’s Bullseye View Mode:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerIGT/blob/cc9678a9b6f91aa9ffde3ff0176cad357335616f/Viewpoint/Viewpoint.py#L1137-L1164">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerIGT/blob/cc9678a9b6f91aa9ffde3ff0176cad357335616f/Viewpoint/Viewpoint.py#L1137-L1164" target="_blank" rel="noopener nofollow ugc">github.com/SlicerIGT/SlicerIGT</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerIGT/blob/cc9678a9b6f91aa9ffde3ff0176cad357335616f/Viewpoint/Viewpoint.py#L1137-L1164" target="_blank" rel="noopener nofollow ugc">Viewpoint/Viewpoint.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerIGT/SlicerIGT/blob/cc9678a9b6f91aa9ffde3ff0176cad357335616f/Viewpoint/Viewpoint.py#L1137-L1164" rel="noopener nofollow ugc"><code>cc9678a9b</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="1137" style="counter-reset: li-counter 1136 ;">
          <li>def bullseyeComputeCameraUpDirectionInRAS(self, toolCameraToRASTransform, cameraOriginInRASMm, focalPointInRASMm):</li>
          <li>  upDirectionInRAS = [0,0,0] # placeholder values</li>
          <li>  if (self.bullseyeForcedUpDirection == True):</li>
          <li>    math = vtk.vtkMath()</li>
          <li>    # cross product of forwardDirectionInRAS vector with upInRAS vector is the rightDirectionInRAS vector</li>
          <li>    upInRAS = self.bullseyeUpDirectionRAS</li>
          <li>    forwardDirectionInRAS = self.bullseyeComputeCameraProjectionDirectionInRAS(cameraOriginInRASMm, focalPointInRASMm)</li>
          <li>    rightDirectionInRAS = [0,0,0] # placeholder values</li>
          <li>    math.Cross(forwardDirectionInRAS,upInRAS,rightDirectionInRAS)</li>
          <li>    numberDimensions = 3;</li>
          <li>    lengthMm = math.Norm(rightDirectionInRAS,numberDimensions)</li>
          <li>    epsilon = 0.0001</li>
          <li>    if (lengthMm &lt; epsilon): # must check for this case</li>
          <li>      logging.warning("Warning: length of cross product in bullseyeComputeCameraUpDirectionInRAS is zero. Workaround used")</li>
          <li>      backupUpDirectionInRAS = [1,1,1] # if the previous cross product was zero, then this shouldn't be</li>
          <li>      math.Normalize(backupUpDirectionInRAS)</li>
          <li>      upInRAS = backupUpDirectionInRAS</li>
          <li>      math.Cross(forwardDirectionInRAS,upInRAS,rightDirectionInRAS)</li>
          <li>    math.Normalize(rightDirectionInRAS)</li>
          <li>    # now compute the cross product between the rightDirectionInRAS and forwardDirectionInRAS directions to get a corrected up vector</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/SlicerIGT/SlicerIGT/blob/cc9678a9b6f91aa9ffde3ff0176cad357335616f/Viewpoint/Viewpoint.py#L1137-L1164" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @ruffsl (2025-10-10 21:10 UTC)

<p>Example discontinuity of the current approach shown in inline sagittal slice view:</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5655e5827084a6a47f52e6b8ad813a09841a6172.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b60c0a2c21d9306b3285ae81f6c4a61fd422534.jpeg" data-video-base62-sha1="cjL5SP5zHKy4q1bDwP58kn1t3l8.mp4">
  </div><p></p>

---

## Post #5 by @lassoan (2025-10-10 23:09 UTC)

<p>We usually set the up direction of a slice view from a 5D transform using Python scripting. See a full example in thebscript repository: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-slice-position-and-orientation-from-a-normal-vector-and-position" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
<blockquote>
<p>would you have any suggestions to avoid the jarring discontinuity of the current approach when the z axis of the tool lines up with any RAS axis of the volume?</p>
</blockquote>
<p>The exanple in the script repository takes care of this.</p>
<p>Probably we have not been motivated enough to add this feature to volume reslice driver module because the ideal behavior very application-specific. In each clinical workflow that we developed we ended up using slightly different method. But maybe you can convince us to add a few common strategies.</p>

---
