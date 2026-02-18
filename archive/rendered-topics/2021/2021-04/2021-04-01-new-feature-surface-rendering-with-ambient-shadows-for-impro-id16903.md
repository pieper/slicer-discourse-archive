# New feature: Surface rendering with ambient shadows for improved depth perception

**Topic ID**: 16903
**Date**: 2021-04-01
**URL**: https://discourse.slicer.org/t/new-feature-surface-rendering-with-ambient-shadows-for-improved-depth-perception/16903

---

## Post #1 by @lassoan (2021-04-01 13:08 UTC)

<p>Slicer Preview Release uses an upgraded version of the VTK rendering library, which has many new rendering features that can make renderings in Slicer more realistic.</p>
<p>We exposed one of these new features: ambient shadows. These shadows make regions darker that are farther than nearby regions in the rendered image. The implementation is very fast, normally there should be no difference in rendering speed (the algorithm is called “screens space ambient occlusion”, as it performs computations in screen space).</p>
<p>Examples:</p>
<ol>
<li>Model with large space inside</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fec9fcf6218d91f97576bd7230bb34b18124875.jpeg" data-download-href="/uploads/short-url/97v2PX3RuxYNaeOID4jLPtal6br.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fec9fcf6218d91f97576bd7230bb34b18124875_2_690x345.jpeg" alt="image" data-base62-sha1="97v2PX3RuxYNaeOID4jLPtal6br" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fec9fcf6218d91f97576bd7230bb34b18124875_2_690x345.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fec9fcf6218d91f97576bd7230bb34b18124875_2_1035x517.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fec9fcf6218d91f97576bd7230bb34b18124875_2_1380x690.jpeg 2x" data-dominant-color="958C85"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2140×1073 728 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="2">
<li>Model with small crevices</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/631ed7785c91c59c9ead6741287cb740bde45acc.jpeg" data-download-href="/uploads/short-url/e8Rly3C7yNR7nCCIxRtNKuREgGg.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/631ed7785c91c59c9ead6741287cb740bde45acc_2_688x500.jpeg" alt="image" data-base62-sha1="e8Rly3C7yNR7nCCIxRtNKuREgGg" width="688" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/631ed7785c91c59c9ead6741287cb740bde45acc_2_688x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/631ed7785c91c59c9ead6741287cb740bde45acc_2_1032x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/631ed7785c91c59c9ead6741287cb740bde45acc_2_1376x1000.jpeg 2x" data-dominant-color="A8A787"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1533×1113 347 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="3">
<li>Model with several flat, parallel surfaces</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac00cd9093f9cf5bc4fcb296ce450f8c02ec969f.jpeg" data-download-href="/uploads/short-url/oxBQpmXHlvxneKi7hMWjUmsvNCv.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac00cd9093f9cf5bc4fcb296ce450f8c02ec969f_2_690x131.jpeg" alt="image" data-base62-sha1="oxBQpmXHlvxneKi7hMWjUmsvNCv" width="690" height="131" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac00cd9093f9cf5bc4fcb296ce450f8c02ec969f_2_690x131.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac00cd9093f9cf5bc4fcb296ce450f8c02ec969f_2_1035x196.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac00cd9093f9cf5bc4fcb296ce450f8c02ec969f_2_1380x262.jpeg 2x" data-dominant-color="B4B281"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1887×360 99.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><strong>How to try:</strong></p>
<ul>
<li>Download latest Slicer Preview Release</li>
<li>Install Sandbox extension (in Examples category)</li>
<li>Go to “Lights” module</li>
<li>Select a 3D view and click “Setup lights”</li>
<li>Scroll down to “Ambient shadows” section and check “Enable”</li>
<li>Adjust the “Size scale” slider (it selects the size scale of relevant features)</li>
</ul>
<p>Notes:</p>
<ul>
<li>The shadows are applied to all nodes that are rendered as polygonal meshes (models, segmentations, fiber bundles, markups, etc.) but not to volume rendering.</li>
<li>Rendering results are typically better when surface normals are available. You can use Surface Toolbox module / Normals option to compute surface normals.</li>
<li>In the near future we will explore with enabling more of the recently added VTK rendering features, such as <a href="https://blog.kitware.com/vtk-pbr/">physically based rendering</a>. If someone wants to explore these features then this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Access_VTK_actor_properties">example in the script repository</a> is a good starting point.</li>
</ul>
<p>Acknowledgment: This work was funded in part by NIH R01 HL153166, PI: M. A. Jolley (Children’s Hospital of Philadelphia - CHOP)</p>

---

## Post #2 by @manjula (2021-04-01 17:17 UTC)

<p>Thank you for the great work. It looks very nice …</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42b3117500c1572c412a4f1788a4dd5eddfe9f48.jpeg" data-download-href="/uploads/short-url/9w3adNGCJcyLbxtUtGTZngZFnh6.jpeg?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42b3117500c1572c412a4f1788a4dd5eddfe9f48_2_683x499.jpeg" alt="Screenshot_2" data-base62-sha1="9w3adNGCJcyLbxtUtGTZngZFnh6" width="683" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42b3117500c1572c412a4f1788a4dd5eddfe9f48_2_683x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42b3117500c1572c412a4f1788a4dd5eddfe9f48_2_1024x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42b3117500c1572c412a4f1788a4dd5eddfe9f48.jpeg 2x" data-dominant-color="CFDAD3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">1250×914 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2021-04-01 17:20 UTC)

<p>Very nice. For comparison, can you also post an image of how the surface looks like without ambient shadows?</p>

---

## Post #4 by @manjula (2021-04-01 17:32 UTC)

<p>View 2 with ambient shadows</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a8715e0d92f7ceedbda9363537e25b5838092a6.jpeg" data-download-href="/uploads/short-url/htVFA1H9yPTOhoqx1klNcEAkOvY.jpeg?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a8715e0d92f7ceedbda9363537e25b5838092a6_2_690x416.jpeg" alt="Screenshot_2" data-base62-sha1="htVFA1H9yPTOhoqx1klNcEAkOvY" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a8715e0d92f7ceedbda9363537e25b5838092a6_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a8715e0d92f7ceedbda9363537e25b5838092a6_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a8715e0d92f7ceedbda9363537e25b5838092a6_2_1380x832.jpeg 2x" data-dominant-color="BDE6E2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">1538×929 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
