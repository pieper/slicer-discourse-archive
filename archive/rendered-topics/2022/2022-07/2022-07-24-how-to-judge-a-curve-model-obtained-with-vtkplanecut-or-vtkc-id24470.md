---
topic_id: 24470
title: "How To Judge A Curve Model Obtained With Vtkplanecut Or Vtkc"
date: 2022-07-24
url: https://discourse.slicer.org/t/24470
---

# How to judge a curve model obtained with vtkplanecut or vtkcutter is closed?

**Topic ID**: 24470
**Date**: 2022-07-24
**URL**: https://discourse.slicer.org/t/how-to-judge-a-curve-model-obtained-with-vtkplanecut-or-vtkcutter-is-closed/24470

---

## Post #1 by @jumbojing (2022-07-24 18:01 UTC)

<p>How to judge a curve model obtained with vtkplanecut or vtkcutter is closed?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1hrCsY3-2dZxRI4_Z1dilN3F5clqqpTfB%2Fview%3Fusp%3Dsharing&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1hrCsY3-2dZxRI4_Z1dilN3F5clqqpTfB%2Fview%3Fusp%3Dsharing&amp;ifkv=AaSxoQwr6Ah4bcpuff7nmepNzbiWmFlvFPtz6GvOwRdxTbUv8Om4oyazHZHqhlz8-7qeQCEGrXoKUQ&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S-50260005%3A1715915191449189&amp;ddm=0">
  <header class="source">

      <a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1hrCsY3-2dZxRI4_Z1dilN3F5clqqpTfB%2Fview%3Fusp%3Dsharing&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1hrCsY3-2dZxRI4_Z1dilN3F5clqqpTfB%2Fview%3Fusp%3Dsharing&amp;ifkv=AaSxoQwr6Ah4bcpuff7nmepNzbiWmFlvFPtz6GvOwRdxTbUv8Om4oyazHZHqhlz8-7qeQCEGrXoKUQ&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S-50260005%3A1715915191449189&amp;ddm=0" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1hrCsY3-2dZxRI4_Z1dilN3F5clqqpTfB%2Fview%3Fusp%3Dsharing&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1hrCsY3-2dZxRI4_Z1dilN3F5clqqpTfB%2Fview%3Fusp%3Dsharing&amp;ifkv=AaSxoQwr6Ah4bcpuff7nmepNzbiWmFlvFPtz6GvOwRdxTbUv8Om4oyazHZHqhlz8-7qeQCEGrXoKUQ&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S-50260005%3A1715915191449189&amp;ddm=0" target="_blank" rel="noopener nofollow ugc">Google Drive: Sign-in</a></h3>

  <p>Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52051d7cd6aacf10930f0f4c0d49ff6dbd10e1d6.png" alt="image" data-base62-sha1="bHA6VO49hiY0T7QBofkAbWak4Gq" width="603" height="297"></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>@ jmhuie <a class="mention" href="/u/manjula">@manjula</a> <a class="mention" href="/u/szhang">@szhang</a></p>

---

## Post #2 by @jumbojing (2022-07-24 20:15 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39244b453341c5798449c1f69eb952056eaf154f.png" data-download-href="/uploads/short-url/89uYtshd1K3TpXYQNr4BtndPSGP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39244b453341c5798449c1f69eb952056eaf154f_2_455x500.png" alt="image" data-base62-sha1="89uYtshd1K3TpXYQNr4BtndPSGP" width="455" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39244b453341c5798449c1f69eb952056eaf154f_2_455x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39244b453341c5798449c1f69eb952056eaf154f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39244b453341c5798449c1f69eb952056eaf154f.png 2x" data-dominant-color="B4C1E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">590×647 36 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I try to use the <a href="https://vtk.org/doc/release/6.0/html/classvtkFeatureEdges.html" rel="noopener nofollow ugc">vtkFeatureEdges</a>, but got the wrong result👆🏻, what’s wrong?</p>

---

## Post #3 by @mau_igna_06 (2022-07-24 23:17 UTC)

<p>One solution is to traverse the curve and check if you arrive to the starting point</p>

---

## Post #4 by @jumbojing (2022-07-24 23:33 UTC)

<p>but howto traverse the model to the curve?</p>

---

## Post #5 by @jumbojing (2022-07-25 10:07 UTC)

<p>I trasverse the model to the curve, and <code>IsA('vtkMRMLOpenCurveNode')</code> , but got the wrong result too👇🏻…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b29950f99986153c007cd23e22acc2ef74a873a0.jpeg" data-download-href="/uploads/short-url/ptXt2AGvU3GnPEhyYkcHh5oqIFO.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b29950f99986153c007cd23e22acc2ef74a873a0_2_342x499.jpeg" alt="image" data-base62-sha1="ptXt2AGvU3GnPEhyYkcHh5oqIFO" width="342" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b29950f99986153c007cd23e22acc2ef74a873a0_2_342x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b29950f99986153c007cd23e22acc2ef74a873a0_2_513x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b29950f99986153c007cd23e22acc2ef74a873a0.jpeg 2x" data-dominant-color="858182"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">669×976 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><img src="https://emoji.discourse-cdn.com/twitter/cold_sweat.png?v=12" title=":cold_sweat:" class="emoji only-emoji" alt=":cold_sweat:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/imp.png?v=12" title=":imp:" class="emoji only-emoji" alt=":imp:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f11e30a51a6d535aff12a48d744bf344aa4f25ab.jpeg" data-download-href="/uploads/short-url/yp1KDrpVYq0FQ5DgI071EMUxJ8f.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f11e30a51a6d535aff12a48d744bf344aa4f25ab_2_305x500.jpeg" alt="image" data-base62-sha1="yp1KDrpVYq0FQ5DgI071EMUxJ8f" width="305" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f11e30a51a6d535aff12a48d744bf344aa4f25ab_2_305x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f11e30a51a6d535aff12a48d744bf344aa4f25ab_2_457x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f11e30a51a6d535aff12a48d744bf344aa4f25ab.jpeg 2x" data-dominant-color="8B8986"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">580×948 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @jumbojing (2022-07-25 22:01 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>@ jmhuie <a class="mention" href="/u/manjula">@manjula</a> <a class="mention" href="/u/szhang">@szhang</a></p>

---
