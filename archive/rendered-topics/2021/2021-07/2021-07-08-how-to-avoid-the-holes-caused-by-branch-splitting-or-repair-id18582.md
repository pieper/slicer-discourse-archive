# How to avoid the holes caused by branch splitting, or repair it

**Topic ID**: 18582
**Date**: 2021-07-08
**URL**: https://discourse.slicer.org/t/how-to-avoid-the-holes-caused-by-branch-splitting-or-repair-it/18582

---

## Post #1 by @JunjieWu (2021-07-08 15:34 UTC)

<p>I have something trouble in branch splitting of vascular bifurcation. Holes are created at the junction of the dividing lines, and i can’t use vmtksurfacecapper to fix it. How can i avoid it, or repair it ?</p>
<pre><code class="lang-auto">vmtkbranchclipper -ifile open_rmsh.vtp -centerlinesfile open_rmsh_clsp.vtp -ofile open_rmsh_sp.vtp --pipe \
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4458f4c2433503a39ccd00b3d59fa815e958e372.png" data-download-href="/uploads/short-url/9KD3rsZGhVL4aFqOcG3S4TStClI.png?dl=1" title="wanghuaxing_buquan_centerlines_GroupIds" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4458f4c2433503a39ccd00b3d59fa815e958e372_2_572x500.png" alt="wanghuaxing_buquan_centerlines_GroupIds" data-base62-sha1="9KD3rsZGhVL4aFqOcG3S4TStClI" width="572" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4458f4c2433503a39ccd00b3d59fa815e958e372_2_572x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4458f4c2433503a39ccd00b3d59fa815e958e372.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4458f4c2433503a39ccd00b3d59fa815e958e372.png 2x" data-dominant-color="1A1A34"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">wanghuaxing_buquan_centerlines_GroupIds</span><span class="informations">840×733 20.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba779feca8284c680fad6b7a01afc9f8f3c14ffc.png" data-download-href="/uploads/short-url/qBz6sK5goQkihRUci7fh4jmIQgI.png?dl=1" title="wanghuaxing_buquan分割效果" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba779feca8284c680fad6b7a01afc9f8f3c14ffc_2_557x500.png" alt="wanghuaxing_buquan分割效果" data-base62-sha1="qBz6sK5goQkihRUci7fh4jmIQgI" width="557" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba779feca8284c680fad6b7a01afc9f8f3c14ffc_2_557x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba779feca8284c680fad6b7a01afc9f8f3c14ffc_2_835x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba779feca8284c680fad6b7a01afc9f8f3c14ffc.png 2x" data-dominant-color="2E2F4D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">wanghuaxing_buquan分割效果</span><span class="informations">963×864 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b21318c4fa990cba04ce894fea50c6b1d188bbfc.png" data-download-href="/uploads/short-url/ppjU4jYWu5DFR6ziimqPLPrGa6w.png?dl=1" title="holes" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b21318c4fa990cba04ce894fea50c6b1d188bbfc.png" alt="holes" data-base62-sha1="ppjU4jYWu5DFR6ziimqPLPrGa6w" width="665" height="499" data-dominant-color="B4B3B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">holes</span><span class="informations">1191×895 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-07-11 15:41 UTC)

<p>Fixing self-intersections or non-manifold edges in a mesh is extremely difficult.</p>
<p>You can try various semi-automatic mesh cleaning tools in MeshMixer, MeshLab, Blender, etc.</p>
<p>Alternatively, you can convert the mesh to binary image and convert it back to mesh. You can do this in 3D Slicer:</p>
<ul>
<li>load the mesh as Segmentation (in Add data dialog, select “Segmentation” in Description column)</li>
<li>in Segmentations module: create binary labelmap representation</li>
<li>remove Closed surface representation</li>
<li>create Closed surface representation</li>
<li>export segmentation as surface mesh (in “Export to files” section)</li>
</ul>

---

## Post #3 by @JunjieWu (2021-07-14 09:03 UTC)

<p>Thanks for your advice@lassoan<br>
I have been tried in 3D Slicer with your suggestion, and it indeed can repair the holes int the surface. However, the surface mesh totally changed, and the splitting lines of branch disappeared which is contrary to my original intention<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7ca489d563e651d22f9c1d8a5a737d4f2143227.png" alt="image" data-base62-sha1="zm3kcQNhlRPFjKNc4DgVcZ0JG4f" width="502" height="419"><br>
I can manual repair holes with creating triangle in mesh tools. But it’s time-consuming. And mesh tools have difficult to identify the splitting results, usually identify the vascular as a whole.<br>
I need to try other way.</p>

---

## Post #4 by @lassoan (2021-07-14 22:33 UTC)

<p>Why do you need the branches to be split? What is your end goal?</p>

---

## Post #5 by @JunjieWu (2021-07-15 01:11 UTC)

<p>splitting vascular branch, forming multiple domains, statistical analysis of the calculation of different areas (WSS, TAWSS, OSI,etc), convenient for post-processing analysis.</p>

---

## Post #6 by @lassoan (2021-07-15 02:57 UTC)

<p>What do you need the branch splitting for? So that you can compute average/min/max/percentiles of WSS, TAWSS, OSI for a vessel section? For that it should not matter that you have small errors in the mesh.</p>

---
