# Changing Input/Ouput for Module from Volume Nodes to Directories

**Topic ID**: 12469
**Date**: 2020-07-09
**URL**: https://discourse.slicer.org/t/changing-input-ouput-for-module-from-volume-nodes-to-directories/12469

---

## Post #1 by @lennymartinez (2020-07-09 17:09 UTC)

<p>Hi, working on the GUI for an extension. It was originally a CLI extension that took in an input directory of dcm files and an ouput directory for storing an obj file made with dcm images. Trying to do the same thing but with the GUI and I was able to edit it down to what I need in terms of elements:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d62f2c3861217719971d685eaeb6b2d88008bdd.png" data-download-href="/uploads/short-url/4bXQe8YHKzaOpjPPw9BHRH7usPP.png?dl=1" title="Screenshot 2020-07-09 13.02.06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d62f2c3861217719971d685eaeb6b2d88008bdd_2_517x104.png" alt="Screenshot 2020-07-09 13.02.06" data-base62-sha1="4bXQe8YHKzaOpjPPw9BHRH7usPP" width="517" height="104" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d62f2c3861217719971d685eaeb6b2d88008bdd_2_517x104.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d62f2c3861217719971d685eaeb6b2d88008bdd_2_775x156.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d62f2c3861217719971d685eaeb6b2d88008bdd_2_1034x208.png 2x" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-07-09 13.02.06</span><span class="informations">1140×230 7.21 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However I’m having a hard time figuring out what the <code>qMRMLNodeComboBox</code> elements should be. I tried looking in the API for anything related to directory and I tried looking at the nodeTypes to see if I could find an alternative for <code>vtkMRMLScalarVolumeNode</code> that would better suit my need, but I’m stumped.</p>
<p>Is there anywhere else I should be looking? I want to use directories instead of the volume nodes because the point is to create a specific obj from the files and the end-user doesn’t need to access the other features of slicer.</p>

---

## Post #2 by @pieper (2020-07-09 17:49 UTC)

<p>Hi - you can use something like this (search the code for similar examples that use this).</p>
<pre><code>self.outputDirSelector = ctk.ctkPathLineEdit()
self.outputDirSelector.filters = ctk.ctkPathLineEdit.Dirs</code></pre>

---
