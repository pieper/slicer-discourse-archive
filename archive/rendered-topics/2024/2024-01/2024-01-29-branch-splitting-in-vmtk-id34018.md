# branch splitting in vmtk

**Topic ID**: 34018
**Date**: 2024-01-29
**URL**: https://discourse.slicer.org/t/branch-splitting-in-vmtk/34018

---

## Post #1 by @MicheleIng (2024-01-29 13:48 UTC)

<p>Hi! I am fairly new to both 3d slicer and vmtk.<br>
Is it possible to do the branch splitting in vmtk (<a href="http://www.vmtk.org/tutorials/BranchSplitting.html" rel="noopener nofollow ugc">link</a>) with 3d slicer?<br>
I want to create those spheres and know the coordinates of the nodes as in the picture.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b1de20173c3ec4e665cf85e2783e477de4bc534.png" data-download-href="/uploads/short-url/3RSUKII1Wiq4kKrHHzrbBCJdbYo.png?dl=1" title="ppp" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b1de20173c3ec4e665cf85e2783e477de4bc534_2_278x500.png" alt="ppp" data-base62-sha1="3RSUKII1Wiq4kKrHHzrbBCJdbYo" width="278" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b1de20173c3ec4e665cf85e2783e477de4bc534_2_278x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b1de20173c3ec4e665cf85e2783e477de4bc534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b1de20173c3ec4e665cf85e2783e477de4bc534.png 2x" data-dominant-color="DFDFDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ppp</span><span class="informations">346×621 42.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2024-01-29 14:08 UTC)

<aside class="quote no-group" data-username="MicheleIng" data-post="1" data-topic="34018">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/8e8cbc/48.png" class="avatar"> MicheleIng:</div>
<blockquote>
<p>with 3d slicer</p>
</blockquote>
</aside>
<p>You may investigate ‘Branch clipper’ and ‘Centerline disassembly’ modules in <a href="https://github.com/vmtk/SlicerExtension-VMTK" rel="noopener nofollow ugc">SlicerVMTK</a> extension, that you can install using the ‘Extensions manager’. They won’t create the <em>spheres</em> though.</p>

---

## Post #3 by @MicheleIng (2024-01-29 15:19 UTC)

<p>Should I download the ‘Branch clipper’ and ‘Centerline disassembly’ modules from link? I have already installed the ‘SlicerVMTK’ extension from ‘manage extensions’.</p>

---

## Post #4 by @chir.set (2024-01-29 15:44 UTC)

<aside class="quote no-group" data-username="MicheleIng" data-post="3" data-topic="34018">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/8e8cbc/48.png" class="avatar"> MicheleIng:</div>
<blockquote>
<p>Should I download the ‘Branch clipper’ and ‘Centerline disassembly’ modules from link?</p>
</blockquote>
</aside>
<p>Not at all.</p>
<p>Type ‘Ctrl + F’ to look for any module by a part of its name.</p>
<p>If you don’t find them, you are probably using an old version of Slicer. Install Slicer Preview instead, specially for ‘Centerline disassembly’ module which is a very recent addition.</p>
<p><em>Hint: always use Slicer Preview.</em></p>

---

## Post #5 by @MicheleIng (2024-01-29 16:44 UTC)

<p>Thanks! I actually updated my version of 3Dslicer and found the two modules.<br>
Are there video tutorials on these modules?<br>
I would like to be able to visualise the centres of those spheres even if I cannot visualise them!</p>

---
