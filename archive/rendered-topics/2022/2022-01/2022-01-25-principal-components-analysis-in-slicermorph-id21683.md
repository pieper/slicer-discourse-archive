---
topic_id: 21683
title: "Principal Components Analysis In Slicermorph"
date: 2022-01-25
url: https://discourse.slicer.org/t/21683
---

# Principal components analysis in SlicerMorph

**Topic ID**: 21683
**Date**: 2022-01-25
**URL**: https://discourse.slicer.org/t/principal-components-analysis-in-slicermorph/21683

---

## Post #1 by @stevenagl12 (2022-01-25 22:01 UTC)

<p>Is there a limit to the number of points that the principal components can be calculated for using SlicerMorph? Also, if possible, could we create a method for SlicerMorph for iterative closest points in addition to the principal axes? That would probably improve performance on more complex shapes, I believe, and given the inherent nature of SlicerMorph for landmarking and the PseudoLM generator, this doesn’t seem all that infeasible.</p>

---

## Post #2 by @muratmaga (2022-01-25 22:38 UTC)

<p>No, there is no limit to the number of points as PCA input. Although the more points you have, the bigger VCV matrix and longer it will take for its decomposition.</p>
<p>For SlicerMorph feature suggestions, please use <a href="https://github.com/SlicerMorph/SlicerMorph/issues" rel="noopener nofollow ugc">SlicerMorph’s github issues page</a> and provide a detailed description of feature request. It will be great if there is an existing implementation you can refer to for us to better understand what you want to do.</p>
<p>We need to keep track of these in a central location.</p>

---

## Post #3 by @stevenagl12 (2022-01-27 17:00 UTC)

<p>Just to check, the module you helped make is part of SLicerMorph now right? I am having a difficult time downloading it if it is.</p>

---

## Post #4 by @muratmaga (2022-01-27 17:02 UTC)

<p>No, it is not part of the SlicerMorph. AFAIK, at this point it only exists as a script. It needs to be converted to a module, and then we can incorporate as part of the utilities group.<br>
You are welcomed to send PR for it.</p>

---

## Post #5 by @stevenagl12 (2022-01-28 16:06 UTC)

<p>Oh ok. <a class="mention" href="/u/smrolfe">@smrolfe</a> had said that you were going to plan on adding this as a utility to the SlicerMorph extension. Is there anything I can do to help with that process?</p>
<blockquote>
<p>That’s great news. Your previous Slicer installation was much older than the current stable. There have been many bug fixes and new features added since then, so is a good idea to update (either the preview or stable). Thanks for the feedback, we will plan to add this as a utility to the SlicerMorph extension.</p>
</blockquote>

---

## Post #6 by @muratmaga (2022-01-28 16:26 UTC)

<p>There are bunch of things we are working on, and this is not a high priority for us.</p>
<p>But if you want to take on turning it to a module (you can follow the IDAVLMConverter example <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/IDAVLMConverter" class="inline-onebox" rel="noopener nofollow ugc">SlicerMorph/IDAVLMConverter at master · SlicerMorph/SlicerMorph · GitHub</a>), send a PR with changes that will be great.</p>

---

## Post #7 by @stevenagl12 (2022-01-28 16:52 UTC)

<p>Didn’t we do this already? I am able to use the module within my 3D Slicer window that has buttons and text options to enter information into it?</p>

---

## Post #8 by @muratmaga (2022-01-28 16:56 UTC)

<p>That’s only the python code. For a module to be included into the extension, you need an icon located resources/Icon, you need to specify that it need to be build as part of the extension.<br>
Look at the example I sent above for IDAVLandmarkEditor. For MorphoJExporter to be a module, you need to have the same structure.</p>
<p>Fork the latest SlicerMorph repo, create a branch for your MorphoJ utility, add the existing python file, create cmakelist  and icon, and send a PR.</p>

---

## Post #9 by @stevenagl12 (2022-01-28 18:48 UTC)

<p>So I think I managed to do everything. Is this workable: <a href="https://github.com/stevenagl12/SlicerMorph-additions.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - stevenagl12/SlicerMorph-additions: Additional SlicerMorph Extensions</a></p>

---

## Post #10 by @stevenagl12 (2022-01-28 18:54 UTC)

<p>Sorry, missed that last step.</p>

---

## Post #11 by @stevenagl12 (2022-01-28 19:46 UTC)

<p>Ok, so I am sorry. I am very confused. I forked the latest SlicerMorph repo, created a branch called additional-extensions, and added in the necessary information, but for some reason it is not only saying that the branch I have is identical to the master repo, but it is also saying that smrolfe edited it 2 days ago…</p>

---

## Post #12 by @muratmaga (2022-01-28 20:22 UTC)

<p>Looks like you kept your MorphoJ module as a separate repo. Your fork doesn’t contain any changes:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/stevenagl12/SlicerMorph">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/stevenagl12/SlicerMorph" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/090b6629d5ac02ceff14781d875ea77bc191701b3efbf0788f50a2dc21ee9994/stevenagl12/SlicerMorph" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/stevenagl12/SlicerMorph" target="_blank" rel="noopener nofollow ugc">GitHub - stevenagl12/SlicerMorph: Extensions to conduct 3D morphometrics in...</a></h3>

  <p>Extensions to conduct 3D morphometrics in Slicer. Contribute to stevenagl12/SlicerMorph development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You need to create a folder for the module in SlicerMorph (e.g., ExportMorphoJFile) copy the contents you kept at this repository <a href="https://github.com/stevenagl12/SlicerMorph-additions" class="inline-onebox" rel="noopener nofollow ugc">GitHub - stevenagl12/SlicerMorph-additions: Additional SlicerMorph Extensions</a> into that folder.</p>
<p>Then commit and do PR.</p>

---

## Post #13 by @stevenagl12 (2022-01-28 20:43 UTC)

<p>So, I had done that already. Here’s a screenshot of the repository on my computer:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae27cb805f739700b63dc1a82c22f681c5dc037d.png" alt="image" data-base62-sha1="oQEl5kGSEf4xoEFnHLOUxDsvD2Z" width="587" height="278"></p>

---

## Post #14 by @muratmaga (2022-01-28 20:49 UTC)

<p>OK. that’s only on your computer.</p>
<p>You need to commit those changes under a new branch, push to your remote repository on GH then request PR.</p>
<p>This might be helpful: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/contributing.html#how-to-submit-a-pr" class="inline-onebox" rel="noopener nofollow ugc">Contributing to Slicer — 3D Slicer documentation</a><br>
Step <span class="hashtag">#2</span> is not relevant for our case.</p>

---

## Post #15 by @stevenagl12 (2022-01-28 20:58 UTC)

<p>I think I managed to do it, and create a pull request. Please let me know if i did it right or if I need to make more changes.</p>

---

## Post #16 by @muratmaga (2022-01-28 21:08 UTC)

<p>Looks like it worked <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #17 by @stevenagl12 (2022-01-28 21:11 UTC)

<p>I apologize for being so unfamiliar with all this. I never had any formal programming or computer science training, besides MATLAB and LabView, so it is all being picked up as I go along. But thank you for all of your help.</p>

---

## Post #18 by @muratmaga (2022-01-28 22:35 UTC)

<p>Np. It is part of the learning. Now you know <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
