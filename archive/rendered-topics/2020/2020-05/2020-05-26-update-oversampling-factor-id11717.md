---
topic_id: 11717
title: "Update Oversampling Factor"
date: 2020-05-26
url: https://discourse.slicer.org/t/11717
---

# Update oversampling factor

**Topic ID**: 11717
**Date**: 2020-05-26
**URL**: https://discourse.slicer.org/t/update-oversampling-factor/11717

---

## Post #1 by @Queen_Rei (2020-05-26 16:36 UTC)

<p>I am currently working on an extension to create a segmentation on start-up. One step in that process is to update the oversampling factor under segmentation geometry from 1.0 to 1.5.</p>
<p>I want to know how I can do this in python~<br>
Thank you for all the help! Hope family/friends are safe during these pressing times!</p>

---

## Post #2 by @Queen_Rei (2020-05-29 15:01 UTC)

<p>I could really use the help~ It means a lot.<br>
I can’t seem to find the necessary methods to do this. Not sure if this is a part of the Segmentation Editor Module or the MasterVolumeNode.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1378ccf9b2da032ebc306ff7efe36995a85e929d.png" alt="image" data-base62-sha1="2MfSWBiSOGyqAhvYMQlH9pDnCYB" width="679" height="280"></p>

---

## Post #3 by @cpinter (2020-05-29 15:32 UTC)

<p>Sorry for not noticing your post until now.</p>
<p>Here’s how you can do that:</p>
<pre><code>s = getNode('vtkMRMLSegmentationNode1')
se = s.GetSegmentation()
se.SetConversionParameter('Oversampling factor', '0.5')</code></pre>

---

## Post #4 by @cpinter (2020-05-29 15:33 UTC)

<p>By the way on the UI you can set it by either long-clicking Create in the row oof binary labelmap if you don’t have that representation yet, or click Update if you have one already. Then select the path and you’ll see the parameters:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52d7d66b3cba381389407d8a0b0bc9d8326d1845.png" data-download-href="/uploads/short-url/bORA6VbTDjO0aNvi5jXArDYwCoZ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52d7d66b3cba381389407d8a0b0bc9d8326d1845_2_683x500.png" alt="image" data-base62-sha1="bORA6VbTDjO0aNvi5jXArDYwCoZ" width="683" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52d7d66b3cba381389407d8a0b0bc9d8326d1845_2_683x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52d7d66b3cba381389407d8a0b0bc9d8326d1845.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52d7d66b3cba381389407d8a0b0bc9d8326d1845.png 2x" data-dominant-color="E9ECEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">854×625 55.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Queen_Rei (2020-05-29 17:56 UTC)

<p>Thank you so much for the easy to follow steps! I got it works as I desired <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>

---
