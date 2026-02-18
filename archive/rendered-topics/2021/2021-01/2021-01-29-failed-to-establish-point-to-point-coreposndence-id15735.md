# Failed to establish point to point coreposndence

**Topic ID**: 15735
**Date**: 2021-01-29
**URL**: https://discourse.slicer.org/t/failed-to-establish-point-to-point-coreposndence/15735

---

## Post #1 by @Maxibers (2021-01-29 08:15 UTC)

<p>I’m having trouble in establishing point to point corespondence.<br>
Long story short i’m trying to analyze tmj condyle heads remodeling. So after the SPHARM-PDM process on some, but not all, the condyle heads i cannot get the correct correspondence. In the attached pics there’s an example, sometimes is way more off.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a90c89d277536b4236167678df25e9c26228df3.png" alt="PRE SURG" data-base62-sha1="jLO5u1ODu7ZnqwveRUzUWKgudkn" width="468" height="399"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21458d17cefa83599cf4eec433e650aa8d5fd688.png" alt="POST SURG" data-base62-sha1="4KkLGFuQZW33GQdcJzWtE670qRq" width="377" height="355"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4ddfaf1ec99801e144cd88f1c94b730a0d94e3d.png" alt="BOTH" data-base62-sha1="wEEs8gsgIasEzu0lE0qV4RZ5Cl7" width="457" height="386"></p>
<p>Am i missing something or doing something wrong? Maybe the original mesh is too round and spharm fails to align it?<br>
Thanks in advance</p>

---

## Post #2 by @juanprietob (2021-02-01 18:17 UTC)

<p>Hi Massimo,<br>
Sometimes SPHARM-PDM is not enough to produce the correct alignment of your shape population.<br>
When this is the case, you should use the RigidAlignment module to further increase shape correspondence.</p>
<p>This module has been renamed in the latest <a href="http://salt.slicer.org/download/" rel="noopener nofollow ugc">SlicerSALT</a> to SPHARM-PDM Shape Correspondence Improvement.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f4eb7b09014ec1573a1f8518d1490fc7b063d77.png" data-download-href="/uploads/short-url/4sXs5POimoJ6qvh8ptBFogkbTdd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f4eb7b09014ec1573a1f8518d1490fc7b063d77_2_303x500.png" alt="image" data-base62-sha1="4sXs5POimoJ6qvh8ptBFogkbTdd" width="303" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f4eb7b09014ec1573a1f8518d1490fc7b063d77_2_303x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f4eb7b09014ec1573a1f8518d1490fc7b063d77_2_454x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f4eb7b09014ec1573a1f8518d1490fc7b063d77.png 2x" data-dominant-color="D5E2EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">483×797 74.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is a link to a <a href="https://docs.google.com/presentation/d/1_Od20WHcl6IKxN-n1yIYMmDC9sUmkZXFj2YXCAkHQKA/edit?usp=sharing" rel="noopener nofollow ugc">tutorial</a>, please keep in mind that the module is now named differently.</p>
<p>I hope this helps,</p>
<p>Juan</p>

---

## Post #3 by @Maxibers (2021-02-01 21:20 UTC)

<p>thank you very much for your help</p>

---
