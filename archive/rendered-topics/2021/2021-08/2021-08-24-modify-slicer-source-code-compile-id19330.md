---
topic_id: 19330
title: "Modify Slicer Source Code Compile"
date: 2021-08-24
url: https://discourse.slicer.org/t/19330
---

# Modify slicer source code. compile,

**Topic ID**: 19330
**Date**: 2021-08-24
**URL**: https://discourse.slicer.org/t/modify-slicer-source-code-compile/19330

---

## Post #1 by @xianger-qi (2021-08-24 08:40 UTC)

<p>There are a problem confusing me. I clone the slicer custom application template from <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" class="inline-onebox" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerCustomAppTemplate: Template to be used as a starting point for creating a custom 3D Slicer application</a>. AND, When i modify the source code such as  project,  project, and commit the modification to git. THEN, I compile the application base on last commit, but the cmake always checkout current commit to the original commit(picture below). How can i modify the project configure to solve this problem? Thanks for reading!<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37230c1cd354ba9c30e0410db080011421fcf65c.png" data-download-href="/uploads/short-url/7RLlF5UlwdHpCqY1LSWpGIdexFa.png?dl=1" title="git" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37230c1cd354ba9c30e0410db080011421fcf65c_2_689x302.png" alt="git" data-base62-sha1="7RLlF5UlwdHpCqY1LSWpGIdexFa" width="689" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37230c1cd354ba9c30e0410db080011421fcf65c_2_689x302.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37230c1cd354ba9c30e0410db080011421fcf65c_2_1033x453.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37230c1cd354ba9c30e0410db080011421fcf65c.png 2x" data-dominant-color="3E1E32"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">git</span><span class="informations">1299×569 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-08-24 20:31 UTC)

<p>Normally you don’t modify upstream repositories, such as VTK or Slicer, just repository in your own code. If for some reason you need to modify content of upstream repositories then you can fork them and use your forked repositories.</p>
<p>Also, you normally don’t rebuild the top-level superbuild, just whatever you need. For example, if you modified Slicer source code then you don’t have to rebuild VTK and all other dependencies.</p>

---
