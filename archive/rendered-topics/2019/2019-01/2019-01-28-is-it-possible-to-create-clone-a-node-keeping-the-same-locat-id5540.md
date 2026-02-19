---
topic_id: 5540
title: "Is It Possible To Create Clone A Node Keeping The Same Locat"
date: 2019-01-28
url: https://discourse.slicer.org/t/5540
---

# Is it possible to create/clone a node keeping the same location in the hierarchy of the father node?

**Topic ID**: 5540
**Date**: 2019-01-28
**URL**: https://discourse.slicer.org/t/is-it-possible-to-create-clone-a-node-keeping-the-same-location-in-the-hierarchy-of-the-father-node/5540

---

## Post #1 by @Alex_Vergara (2019-01-28 13:56 UTC)

<p>Basically I have a big subject hierarchy (several folders), and inside each I have nodes (volumes, segmentations, transformations). I want to create a table for instance and place it in the same location of the generating data, or clone one of the volumes, make some calculation and save as a new volume in the same hierarchy.</p>
<p>When I do this</p>
<pre><code class="lang-python">    volumeNode = slicer.vtkSlicerVolumesLogic().CloneVolume(slicer.mrmlScene, fatherNode, nodename, True)
    util.updateVolumeFromArray(volumeNode, new_arr)
    volumeNode.Modified()
</code></pre>
<p>the created volume is outside of the hierarchy so I have to move it manually. Is there a way to tell the new volume to be placed where the father is located??</p>

---

## Post #2 by @lassoan (2019-01-29 01:16 UTC)

<p>This feature is already available in Data module. You can convert file folder hierarchy to subject hierarchy by clicking on the empty area of the subject hierarchy tree:</p>
<p>For example, you load a number of images from a folder structure (folder names a, b, c, d, e):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a610a7d7f6055e21d5a704977efdb9d09531c6a.png" data-download-href="/uploads/short-url/3Lmk3N4kZWaDjiYlwijCdeXPtyy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a610a7d7f6055e21d5a704977efdb9d09531c6a_2_439x500.png" alt="image" data-base62-sha1="3Lmk3N4kZWaDjiYlwijCdeXPtyy" width="439" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a610a7d7f6055e21d5a704977efdb9d09531c6a_2_439x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a610a7d7f6055e21d5a704977efdb9d09531c6a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a610a7d7f6055e21d5a704977efdb9d09531c6a.png 2x" data-dominant-color="D3D5D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">629×715 85.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>results in:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8979ee404fa0822539fca25a24caf01f02e00d0f.png" data-download-href="/uploads/short-url/jCaEdCtHM6Q28t8pU6iXvcKBr0H.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8979ee404fa0822539fca25a24caf01f02e00d0f_2_467x500.png" alt="image" data-base62-sha1="jCaEdCtHM6Q28t8pU6iXvcKBr0H" width="467" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8979ee404fa0822539fca25a24caf01f02e00d0f_2_467x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8979ee404fa0822539fca25a24caf01f02e00d0f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8979ee404fa0822539fca25a24caf01f02e00d0f.png 2x" data-dominant-color="E1E1E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">583×624 67.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Alex_Vergara (2019-01-29 09:40 UTC)

<p>I have already a hierarchy:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63065456cad1e7366b47b5c09966d867d160a30c.png" data-download-href="/uploads/short-url/e80PtTm2xf6GdvCYmoDvsL0P100.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63065456cad1e7366b47b5c09966d867d160a30c_2_487x500.png" alt="image" data-base62-sha1="e80PtTm2xf6GdvCYmoDvsL0P100" width="487" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63065456cad1e7366b47b5c09966d867d160a30c_2_487x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63065456cad1e7366b47b5c09966d867d160a30c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63065456cad1e7366b47b5c09966d867d160a30c.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">525×538 33 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>what I need is to coy the object to perform some operations and keep bpoth the new and the old volumes, I am doing like this</p>
<pre data-code-wrap="python"><code class="lang-python">    shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
    itemID = shNode.GetItemByDataNode(node)
    newname = name.replace('CTCT', 'DENS')
    clonedItemID = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, itemID, newname)
    vox_arr = np.array(slicer.util.array(newname)).copy()
    vox_arr = np.where(vox_arr&lt;0, 0.0009990791851848257 * vox_arr + 1, 0.0005116346986394071 * vox_arr + 1)
    clonedNode = shNode.GetItemDataNode(clonedItemID)
    slicer.util.updateVolumeFromArray(clonedNode, vox_arr)
    clonedNode.Modified()
</code></pre>
<p>But then when I visualize both images, THEY ARE BOTH CHANGED!!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7cd365e9e2d463453ea5b0ac8493ad2eb595a45.png" alt="image" data-base62-sha1="zm9Bf5DAM4003VCPdASQSFQFqHr" width="533" height="134"></p>
<p>I need to preserve the hierarchy path, but also to create a new volume and modify it without changing the original. This code preserves the hierarchy, but modifies both volumes:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/755045aa642e0b4eb475619cfbe9cd105c321287.png" data-download-href="/uploads/short-url/gJNQt8IHkFcJHVIAUJ6HamkZtHh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/755045aa642e0b4eb475619cfbe9cd105c321287_2_484x500.png" alt="image" data-base62-sha1="gJNQt8IHkFcJHVIAUJ6HamkZtHh" width="484" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/755045aa642e0b4eb475619cfbe9cd105c321287_2_484x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/755045aa642e0b4eb475619cfbe9cd105c321287.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/755045aa642e0b4eb475619cfbe9cd105c321287.png 2x" data-dominant-color="F1F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">523×540 38.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the code in the original post creates a new volume you can modify safely without modifying the original but it does not preserve the hierarchy.</p>
<p>So how to do this?</p>

---

## Post #4 by @lassoan (2019-01-29 10:15 UTC)

<p>Cloning a volume using <code>CloneSubjectHierarchyItem</code> creates a shallow copy of the image data. You can either use Volume module’s <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Clone_a_volume" rel="nofollow noopener">CloneVolume</a> method or modify your code above to clone the image data by adding <code>clonedNode.SetAndObserveImageData(vtk.vtkImageData())</code> before <code>slicer.util.updateVolumeFromArray(clonedNode, vox_arr)</code>.</p>

---

## Post #5 by @Alex_Vergara (2019-01-29 10:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="5540">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>clonedNode.SetAndObserveImageData(vtk.vtkImageData())</p>
</blockquote>
</aside>
<p>yes, that worked!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a2c7bb3cfb5c7552f91871dcd5b2626d6bda5d9.png" alt="image" data-base62-sha1="jIlc8wj2NGCp6lBWR0niLwQQuNz" width="563" height="134"></p>
<p>not trivial line BTW! Thanks</p>

---

## Post #6 by @lassoan (2019-01-30 01:17 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="5" data-topic="5540">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>not trivial line BTW</p>
</blockquote>
</aside>
<p>Yes, that’s why we added the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Clone_a_volume">clone volume example</a> in the script repository.</p>

---
