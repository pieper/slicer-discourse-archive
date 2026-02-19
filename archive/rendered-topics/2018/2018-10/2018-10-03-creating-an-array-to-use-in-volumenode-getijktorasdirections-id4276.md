---
topic_id: 4276
title: "Creating An Array To Use In Volumenode Getijktorasdirections"
date: 2018-10-03
url: https://discourse.slicer.org/t/4276
---

# Creating an array to use in: volumeNode.GetIJKToRASDirections (array)

**Topic ID**: 4276
**Date**: 2018-10-03
**URL**: https://discourse.slicer.org/t/creating-an-array-to-use-in-volumenode-getijktorasdirections-array/4276

---

## Post #1 by @Nassir (2018-10-03 18:54 UTC)

<p>Hello,</p>
<p>I’m trying to use the function GetIJKToRASDirections on a volume to get its IJK to RAS direction matrix. I previously transformed this image, and will now use the matrix to transform (using the set functions) another image that was acquired at about the same time. Unfortunately, I did not save the transform matrix.</p>
<p>The GetIJKToRASDirections function requires an output array with type ‘double’ and dimensions “dirs[3][3]” (<a href="http://apidocs.slicer.org/master/classvtkMRMLVolumeNode.html#a486704c0cef8b42bf5505967669ab674" class="inline-onebox" rel="noopener nofollow ugc">Slicer: vtkMRMLVolumeNode Class Reference</a>). I was not able to use normal python methods to create a 3 by 3 array. I also think there’s probably a simple way to do this Slicer, but I can’t find it on the script repositories.</p>
<p>TLDR: how do I create a 3 by 3 array of type ‘double’ to use in volumeNode.GetIJKToRASDirections (array).</p>
<p>Thank you for your help.</p>
<p>PS: I’m slicer Slicer 4.9</p>

---

## Post #2 by @ihnorton (2018-10-03 19:25 UTC)

<p>Here is a post with some example code that should help:</p>
<aside class="quote quote-modified" data-post="2" data-topic="3525">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/acpc-transform-question/3525/2">ACPC transform question</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi Alexis, 
You can try this code on the Python console: 
import numpy as np
import SampleData

def getSampleVolume():
    # Download MRHead
    sampleDataLogic = SampleData.SampleDataLogic()
    volumeNode = sampleDataLogic.downloadMRHead()
    return volumeNode


def getMatrixToACPC(ac, pc, ih):
    # Anteroposterior axis
    pcAc = ac - pc
    yAxis = pcAc / np.linalg.norm(pcAc)
    # Lateral axis
    acIhDir = ih - ac
    xAxis = np.cross(yAxis, acIhDir)
    xAxis /= np.linalg.norm(xAxis)
  …
  </blockquote>
</aside>


---

## Post #3 by @Nassir (2018-10-04 23:11 UTC)

<p>Did not answer the question directly but got me where I should have been looking.</p>
<p>Thanks!</p>

---
