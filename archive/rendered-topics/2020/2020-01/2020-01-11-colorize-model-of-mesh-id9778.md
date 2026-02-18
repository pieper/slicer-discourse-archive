# Colorize Model of Mesh

**Topic ID**: 9778
**Date**: 2020-01-11
**URL**: https://discourse.slicer.org/t/colorize-model-of-mesh/9778

---

## Post #1 by @lausiv (2020-01-11 08:49 UTC)

<p>I want to Colorize Mesh of the Volumetic Meshes. so i did simple python script from script repository of slicer document. but it does not work.</p>
<pre><code>modelNode = slicer.util.getNode('Model') # select cells in this model

cellScalars = modelNode.GetMesh().GetCellData()  # select cell data in this model

selectionArray = cellScalars.GetArray('labels') # select current active scalar in this model

for i in range(0, 10000):

    selectionArray.SetValue(i, 100) # set selected cell's scalar value to non-zero

selectionArray.Modified()
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3d3edb0cc9d7e9db74372d62723e941e7e44021.png" alt="image" data-base62-sha1="udUNENGXXIAYduPOtY4oIhK9Ctb" width="498" height="414"></p>

---

## Post #2 by @lassoan (2020-01-11 18:05 UTC)

<p>You also need to select the scalar array to be used for coloring (in Models module, Scalars section).</p>

---

## Post #3 by @lausiv (2020-01-13 06:20 UTC)

<p>You also need to select the scalar array to be used for coloring (in Models module, Scalars section).<br>
==&gt; Yes. I did but have no effect on the Display of Meshes</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/befa1d575bac3e046126584e86b515865d0d7ab8.png" data-download-href="/uploads/short-url/rfsAqfIDgXMeXVLhE7amM3qJVJm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/befa1d575bac3e046126584e86b515865d0d7ab8.png" alt="image" data-base62-sha1="rfsAqfIDgXMeXVLhE7amM3qJVJm" width="690" height="170" data-dominant-color="F3F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">914×226 3.84 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/2228ca9eb9d0df57c0deca6a72db8d75eca36c7a.png" alt="image" data-base62-sha1="4SbD1daCwkrguFYviguY7kJAr8K" width="619" height="428"></p>

---

## Post #4 by @lausiv (2020-01-14 05:55 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f022770e992f2a307e5a4c329d5eed80be02f6ec.jpeg" data-download-href="/uploads/short-url/ygkqUbJ7lmMOrdYffvLtHxR3bPe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f022770e992f2a307e5a4c329d5eed80be02f6ec_2_690x457.jpeg" alt="image" data-base62-sha1="ygkqUbJ7lmMOrdYffvLtHxR3bPe" width="690" height="457" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f022770e992f2a307e5a4c329d5eed80be02f6ec_2_690x457.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f022770e992f2a307e5a4c329d5eed80be02f6ec_2_1035x685.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f022770e992f2a307e5a4c329d5eed80be02f6ec.jpeg 2x" data-dominant-color="787264"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1198×795 359 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/423c6c23fefe84fee8979e35dbf35fedbcf3ee22.png" alt="image" data-base62-sha1="9rWXZ3wo7e6ZSUNiRS7mNKArW9A" width="266" height="189"></p>

---

## Post #5 by @lassoan (2020-01-15 03:16 UTC)

<p>I’ve loaded this <a href="https://raw.githubusercontent.com/Slicer/Slicer/master/Libs/MRML/Core/Testing/TestData/PentaHexa.vtk">volumetric mesh</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Select_cells_of_a_model_using_markups_fiducial_points">this script</a> and it worked well for me. Try if it works for you, too. If it does then change things step by step to see what is different in your data or code.</p>

---

## Post #6 by @lausiv (2020-01-15 03:51 UTC)

<p>Good approach, step by step.</p>
<p>previously, i did your code and got the result but i did not capture the result. so i am suspicious about my memory.</p>
<p>i will do it and change the code for my purpose ^^.<br>
and share the code in this page</p>

---

## Post #7 by @lausiv (2020-01-20 22:15 UTC)

<p>It works on the meshed model <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>
<p>Korea time, early morning from 5 AM to 8 for 3 hour. very consenstrate upon slicer open source based image processing &amp; graphics time for enjoyment now^^</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3966ca593d864a3dd6cfb11700ce417af2cfbcb2.png" data-download-href="/uploads/short-url/8bNrtYVR0fsgUk1jzTcJloOv27g.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3966ca593d864a3dd6cfb11700ce417af2cfbcb2.png" alt="image" data-base62-sha1="8bNrtYVR0fsgUk1jzTcJloOv27g" width="690" height="394" data-dominant-color="E1E200"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1078×616 70 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
