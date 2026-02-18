# Problem with Animator and VolumeProperty

**Topic ID**: 20834
**Date**: 2021-11-29
**URL**: https://discourse.slicer.org/t/problem-with-animator-and-volumeproperty/20834

---

## Post #1 by @Krzysztof_Grandys (2021-11-29 23:46 UTC)

<p>Hi All<br>
Sorry about my English<br>
I’d like to create animation based Animator and Volume Property action.</p>
<ol>
<li>I used Volume rendering and set Volume Property 1 at start</li>
<li>I set Volume property 2 at end</li>
<li>When I used Animator and Volume property action first time all looks good, but second time not</li>
<li>When restarting the action, it turns out that volume property 1 looks the same as volume property 2, looks as if volume property 2 was copied to volume property 1 (and sometimes the other way around), or there is no change during the animation, all look like volume property 1<br>
Could some one explain step by step how to use Animator with Volume property action?  I suppose I’m making a stupid mistake somewhere and therefore can’t deal with it.<br>
Regards<br>
Krzysztof</li>
</ol>

---

## Post #2 by @muratmaga (2021-11-30 00:05 UTC)

<p>There is a specific sequence you need to set the properties. Start should be set to VP1, End should be set to VP2, and interpolated VP should be set to the same property node as it is specifed in the Volume Rendering module.</p>
<p>Please read the documentation and the associated step by step instructions at</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/Animator">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/Animator" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/Animator" target="_blank" rel="noopener nofollow ugc">SlicerMorph/Docs/Animator at master · SlicerMorph/SlicerMorph</a></h3>

  <p><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/Animator" target="_blank" rel="noopener nofollow ugc">master/Docs/Animator</a></p>

  <p><span class="label1">Extensions to conduct 3D morphometrics in Slicer. Contribute to SlicerMorph/SlicerMorph development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
