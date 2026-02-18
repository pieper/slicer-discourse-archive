# Show color images in Slicer

**Topic ID**: 22619
**Date**: 2022-03-21
**URL**: https://discourse.slicer.org/t/show-color-images-in-slicer/22619

---

## Post #1 by @lb123 (2022-03-21 13:05 UTC)

<p>Hi,</p>
<p>I’m using pyigtl to create a server to send color images to Slicer via IGT Link.<br>
I can successfully receive the images in Slicer creating a client using the OpenIGTLinkIF module.<br>
However I cannot show the received images as color RGB images but I can only show them as 3 separate channels (R, G and B).<br>
Can you please tell me how to show the image as a color image?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2022-03-21 13:46 UTC)

<p>A volume node is created automatically when the first image is received. For single-component images a <code>vtkMRMLScalarVolumeNode</code> is created, while for multi-component images (such as an RGB color image) a <code>vtkMRMLVectorVolumeNode</code> is created. The class of an object cannot be changed, therefore you may end up having a scalar volume node storing multi-component image data if you first send a single-component volume and then a color volume using the same device.</p>
<p>If you need to send both grayscale and color volumes then you can avoid having suboptimal volume node type by using different device names (e.g., <code>Image-BMode</code>, <code>Image-Doppler</code>). Alternatively, you can implement a custom logic that observes the received image data and if it detects that the image data type is changed then delete and recreate the volume node.</p>

---

## Post #3 by @lb123 (2022-03-21 14:57 UTC)

<p>Thank you for your reply.</p>
<p>It seems that the behaviour is not exactly the one you described.</p>
<p>This is my python code:</p>
<pre><code class="lang-auto">import pyigtl  # pylint: disable=import-error
from time import sleep
import numpy as np
import cv2

server = pyigtl.OpenIGTLinkServer(port=18944)
cap = cv2.VideoCapture(0)

while True:
    if not server.is_connected():
        # Wait for client to connect
        sleep(0.1)
        continue
    ret,img = cap.read()
    img = np.transpose(img, axes=(2, 1, 0))
    print(img.shape) # it prints (3, 640, 480) so it is multi-component
    # Send image
    image_message = pyigtl.ImageMessage(img, device_name="Image")
    server.send_message(image_message, wait=True)
</code></pre>
<p>If in Slicer I type:</p>
<pre><code class="lang-auto">a = slicer.util.getNode("Image")
a
</code></pre>
<p>I get this output:<br>
<code>(MRMLCore.vtkMRMLScalarVolumeNode)000001F1864280A8</code></p>
<p>So it seems a vtkMRMLScalarVolumeNode is created instead of a vtkMRMLVectorVolumeNode</p>
<p>What do you think about it?</p>
<p>Thank you</p>

---

## Post #4 by @lassoan (2022-03-21 15:05 UTC)

<aside class="quote no-group" data-username="lb123" data-post="3" data-topic="22619">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/85e7bf/48.png" class="avatar"> lb123:</div>
<blockquote>
<p><code>print(img.shape) # it prints (3, 640, 480) so it is multi-component</code></p>
</blockquote>
</aside>
<p>This defines a 3D scalar volume (with 3 slices), not a multi-component image. See the axes definition here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/pyigtl/blob/f14d582f6fb3f406a706a0b5e928ed509300428d/pyigtl/messages.py#L255-L257">
  <header class="source">

      <a href="https://github.com/lassoan/pyigtl/blob/f14d582f6fb3f406a706a0b5e928ed509300428d/pyigtl/messages.py#L255-L257" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/pyigtl/blob/f14d582f6fb3f406a706a0b5e928ed509300428d/pyigtl/messages.py#L255-L257" target="_blank" rel="noopener">lassoan/pyigtl/blob/f14d582f6fb3f406a706a0b5e928ed509300428d/pyigtl/messages.py#L255-L257</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="255" style="counter-reset: li-counter 254 ;">
          <li>image: image data. Axes are: (k, j, i, components).</li>
          <li>    If a voxel array is created with (i, j, k) axes then it can be converted to</li>
          <li>    (k, j, i) array by calling: ``voxels = np.transpose(voxels, axes=(2,1,0))``</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Therefore, the shape of an RGB image array should be <code>(1, 480, 640, 3)</code>.</p>

---

## Post #5 by @lb123 (2022-03-21 15:46 UTC)

<p>Thank you very much! Now it works properly.</p>
<pre><code class="lang-auto">
import pyigtl  # pylint: disable=import-error
from time import sleep
import numpy as np
import cv2

server = pyigtl.OpenIGTLinkServer(port=18944)
cap = cv2.VideoCapture(0)

while True:
    if not server.is_connected():
        # Wait for client to connect
        sleep(0.1)
        continue
    ret,img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.rotate(img, cv2.ROTATE_180)
    img=np.expand_dims(img, axis=0) # Define multi-component image   
    print(img.shape) # Now it prints (1, 480, 640, 3)
    # Send image
    image_message = pyigtl.ImageMessage(img, device_name="Image")
    server.send_message(image_message, wait=True)
</code></pre>

---
