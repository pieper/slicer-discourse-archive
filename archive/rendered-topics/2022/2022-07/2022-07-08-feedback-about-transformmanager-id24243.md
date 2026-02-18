# Feedback about TransformManager

**Topic ID**: 24243
**Date**: 2022-07-08
**URL**: https://discourse.slicer.org/t/feedback-about-transformmanager/24243

---

## Post #1 by @mau_igna_06 (2022-07-08 15:01 UTC)

<p>This is a module that let’s define a linear transformNode with:</p>
<ul>
<li>till n (currently 8) different relative rotations and a 3D translation</li>
<li>axis of rotation, angle and pivot point</li>
</ul>
<p>Also allows to visualize the transform information as:</p>
<ul>
<li>current intrinsic euler angles of the rotation part</li>
<li>axis of rotation, angle and nearest to the origin point of the rotation axis (also tells you if the pivot point is at infinity)</li>
<li>an angle markup which translates point0, the origin; around point1, the pivot point; to the point2, the transformed_origin.</li>
<li>a plane markup which its objectToNode transform matches the current transformNode matrix.</li>
</ul>
<p>Screenshots:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fc5c886c22853ec73acba7fbd606456c77b115b.png" data-download-href="/uploads/short-url/6OCbLWcViVL84gyEAetD80JfgGn.png?dl=1" title="Screenshot from 2022-07-08 11-57-43" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fc5c886c22853ec73acba7fbd606456c77b115b_2_690x387.png" alt="Screenshot from 2022-07-08 11-57-43" data-base62-sha1="6OCbLWcViVL84gyEAetD80JfgGn" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fc5c886c22853ec73acba7fbd606456c77b115b_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fc5c886c22853ec73acba7fbd606456c77b115b_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fc5c886c22853ec73acba7fbd606456c77b115b.png 2x" data-dominant-color="C0BFD3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-07-08 11-57-43</span><span class="informations">1366×768 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4ba2f7ebc2f4f72f621616369118176fa09666b3.png" data-download-href="/uploads/short-url/aN6Y38DAnXJG0hmSDLSzOuRRLBp.png?dl=1" title="Screenshot from 2022-07-08 11-58-58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4ba2f7ebc2f4f72f621616369118176fa09666b3_2_690x387.png" alt="Screenshot from 2022-07-08 11-58-58" data-base62-sha1="aN6Y38DAnXJG0hmSDLSzOuRRLBp" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4ba2f7ebc2f4f72f621616369118176fa09666b3_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4ba2f7ebc2f4f72f621616369118176fa09666b3_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4ba2f7ebc2f4f72f621616369118176fa09666b3.png 2x" data-dominant-color="C0BFD3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-07-08 11-58-58</span><span class="informations">1366×768 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the repo for you to try:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/mauigna06/TransformManager">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/mauigna06/TransformManager" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/1e5272cfdaa88277b4fce4f0e5e01f575f4928da48eb20641e698988ad5940a7/mauigna06/TransformManager" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/mauigna06/TransformManager" target="_blank" rel="noopener nofollow ugc">GitHub - mauigna06/TransformManager</a></h3>

  <p>Contribute to mauigna06/TransformManager development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You just need to add <code>YOURPATH/TransformManager/TransformManager</code> to your modules list.</p>
<p>I would appreciate feedback about it.</p>

---
