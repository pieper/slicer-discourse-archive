# Finding landmark pairing information from PseudoLMGenerator

**Topic ID**: 19866
**Date**: 2021-09-26
**URL**: https://discourse.slicer.org/t/finding-landmark-pairing-information-from-pseudolmgenerator/19866

---

## Post #1 by @lv_xiao (2021-09-26 12:26 UTC)

<p>I am PseudoLMGenerator to create symmetric pseudolandmarks on a 3D human facial surface mesh.</p>
<ol>
<li>
<p>I have coordinate information for midfacial landmarks, which could be used as the Plane. However, in Markups module, the plane has to be created by manually placing landmark. I wonder if it is possible to directly use the existing coordinate data of midfacial landmarks to define the Plane, without having to do this manually. Manual operation means that there will inevitable be some degree of deviation from the true plane of symmetry, although I am not sure how much this affects the symmetry of the resulting pseudolandmarks.</p>
</li>
<li>
<p>While coordiantes of the symmetric landmarks are stored in SymmetricPseudoLandmarks, I wish to obtain a file that explictly tell me which landmarks on the left pairs which landmarks on the right and which landmarks are midfacial landmarks. It could be a two column file with entries being the landmark index. For example, if row 1 is 34, 35, then I know the point represented by the 34th row of SymmetricPseudoLandmarks pairs with that represented by the 35th row of the file. If row 2 is 20, 20, then I know the point represented by the 20th row of the file is a midfacial landmark.</p>
</li>
<li>
<p>Is there a way to obtain the triangulation file associated with the SymmetricPseudoLandmarks?</p>
</li>
</ol>

---

## Post #2 by @muratmaga (2021-09-26 15:18 UTC)

<aside class="quote no-group" data-username="lv_xiao" data-post="1" data-topic="19866">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lv_xiao/48/8224_2.png" class="avatar"> lv_xiao:</div>
<blockquote>
<p>I have coordinate information for midfacial landmarks, which could be used as the Plane. However, in Markups module, the plane has to be created by manually placing landmark. I wonder if it is possible to directly use the existing coordinate data of midfacial landmarks to define the Plane, without having to do this manually. Manual operation means that there will inevitable be some degree of deviation from the true plane of symmetry, although I am not sure how much this affects the symmetry of the resulting pseudolandmarks.</p>
</blockquote>
</aside>
<p>There is no such requirement. You can create the plane programmatically in whichever you want, and specify that particular plane to be used in PseudoLMGenerator.</p>
<aside class="quote no-group" data-username="lv_xiao" data-post="1" data-topic="19866">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lv_xiao/48/8224_2.png" class="avatar"> lv_xiao:</div>
<blockquote>
<p>While coordiantes of the symmetric landmarks are stored in SymmetricPseudoLandmarks, I wish to obtain a file that explictly tell me which landmarks on the left pairs which landmarks on the right and which landmarks are midfacial landmarks. It could be a two column file with entries being the landmark index. For example, if row 1 is 34, 35, then I know the point represented by the 34th row of SymmetricPseudoLandmarks pairs with that represented by the 35th row of the file. If row 2 is 20, 20, then I know the point represented by the 20th row of the file is a midfacial landmark.</p>
</blockquote>
</aside>
<p>This is already there, midline landmarks have prefix of m_, left of the symmetry plane is n_, right of symmetry plane is i_ See the tutorial <a href="https://github.com/SlicerMorph/Tutorials/tree/main/PseudoLMGenerator#pseudo-landmark-generator-tutorial" class="inline-onebox">Tutorials/PseudoLMGenerator at main · SlicerMorph/Tutorials · GitHub</a></p>
<aside class="quote no-group" data-username="lv_xiao" data-post="1" data-topic="19866">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lv_xiao/48/8224_2.png" class="avatar"> lv_xiao:</div>
<blockquote>
<p>Is there a way to obtain the triangulation file associated with the SymmetricPseudoLandmarks?</p>
</blockquote>
</aside>
<p>Thats already there. After clicking the “generate template” button, switch to data module and you will see a node called templateModel.</p>

---

## Post #3 by @lv_xiao (2021-09-26 16:21 UTC)

<p>Thank you for the response. For Q1, I realised that I could first manually pick the landmarks used to define the Plane first, then manually modify the associated coordinate values so that the Plane lies exactly along the midline. But may I have any idea about how this could be done programmatically? Perhaps directing me to some revevant file will help as well.</p>

---

## Post #4 by @muratmaga (2021-09-26 18:27 UTC)

<p>I am not sure if there is a specific function to create a best fitting plane from a series of points immediately available, but if you browser through the examples in the Slicer’s script repository for Markups, you should be able to do what you want:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups</a></p>
<p>Keep in mind that for practical purposes there is no such thing as an exact midline for any biological structure as there is always subtle asymmetries. If you do want to create perfect midline, you need to reflect your original specimen, and create a symmetrized version by fusing the original and reflected one.</p>

---

## Post #5 by @lassoan (2021-09-27 03:22 UTC)

<p>You can use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/acpctransform.html">ACPC transform module</a> to compute a transform (that can be used to position a plane or to move the object to a canonical pose) from a list of mid-sagittal points and a “horizontal” direction.</p>

---

## Post #6 by @lv_xiao (2021-09-27 07:24 UTC)

<p>For my question on triangulation file associated with the generated pseudolandmarks, I followed Dr. Murat’s suggestion to look at the templateModel. While this file did contain triangulation information, it seems that the triangulation is not complete. I exported the templateModel as ply and visualized it in MeshLab:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7dba5911e3952b30c6655276f49ee416d180292.jpeg" data-download-href="/uploads/short-url/sw1BFCqFzocgUACHj7XurMlRwzM.jpeg?dl=1" title="11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7dba5911e3952b30c6655276f49ee416d180292_2_436x500.jpeg" alt="11" data-base62-sha1="sw1BFCqFzocgUACHj7XurMlRwzM" width="436" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7dba5911e3952b30c6655276f49ee416d180292_2_436x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7dba5911e3952b30c6655276f49ee416d180292_2_654x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7dba5911e3952b30c6655276f49ee416d180292_2_872x1000.jpeg 2x" data-dominant-color="5E5E8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">11</span><span class="informations">1018×1167 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It can be seen that this file contains so many holes which should have been filled by triangular facets. I also check the sample data and here is the MeshLab view:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38173bac76fa265d5bf2b2844838b5a29dbc4f1c.jpeg" data-download-href="/uploads/short-url/80cvVMNVVE1i9MFlVkkayBjQWEk.jpeg?dl=1" title="Snipaste_2021-09-27_15-10-53" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38173bac76fa265d5bf2b2844838b5a29dbc4f1c_2_596x499.jpeg" alt="Snipaste_2021-09-27_15-10-53" data-base62-sha1="80cvVMNVVE1i9MFlVkkayBjQWEk" width="596" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38173bac76fa265d5bf2b2844838b5a29dbc4f1c_2_596x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38173bac76fa265d5bf2b2844838b5a29dbc4f1c_2_894x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38173bac76fa265d5bf2b2844838b5a29dbc4f1c_2_1192x998.jpeg 2x" data-dominant-color="575774"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snipaste_2021-09-27_15-10-53</span><span class="informations">1830×1535 245 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Unwanted holes are there two. My conclusion is that although there is indeed triangulation file associated with the templateModel, it is not complete, leaving many holes. This happens not just to my own data, but also the sample data. So this is unlikely to be due to something specific to my sample, but rather an issue generally associated with PseudoLMGenerator. Have I done something wrong? How to obtain a complete mesh triangulation file that when plotted, leave no holes among vertices?</p>

---

## Post #7 by @muratmaga (2021-09-27 16:11 UTC)

<p>The gaps are there not because there are missing vertices, but because surface normals are not calculated. We don’t need normal for our purposes, only the vertices. It is a model that’s not meant be used beyond visualizing the surface geometry (so that you can decide you need more sparse or dense sampling).  You can’t and shouldn’t use this for anything more than that.</p>
<p>Why do you need this model, what is your goal?</p>

---
