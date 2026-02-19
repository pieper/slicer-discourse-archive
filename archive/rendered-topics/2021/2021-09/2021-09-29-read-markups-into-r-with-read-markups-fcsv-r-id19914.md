---
topic_id: 19914
title: "Read Markups Into R With Read Markups Fcsv R"
date: 2021-09-29
url: https://discourse.slicer.org/t/19914
---

# Read markups into R with read.markups.fcsv.R

**Topic ID**: 19914
**Date**: 2021-09-29
**URL**: https://discourse.slicer.org/t/read-markups-into-r-with-read-markups-fcsv-r/19914

---

## Post #1 by @anromero (2021-09-29 14:15 UTC)

<p>I’d like to read a folder of fixed landmarks into R for asymmetry analysis. I have two trials for each specimen. Should I put files from both trials into the same folder for import into R (e.g., 24LM_1 and 24LM_2 and so on in the same folder)? I’m having trouble figuring out how to import all the landmark files at the same time using the read.markups.fcsv.R function. I’ve only been able to successfully import one landmark file at a time.</p>

---

## Post #2 by @muratmaga (2021-09-29 14:26 UTC)

<p>You need to loop over your files.<br>
Or use the $LM object returned by the parser function in Slicermorph R</p>

---

## Post #3 by @muratmaga (2021-09-29 16:11 UTC)

<p>You can find the relevant tutorial here:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/GPA_3">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/GPA_3" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/GPA_3" target="_blank" rel="noopener nofollow ugc">Tutorials/GPA_3 at main · SlicerMorph/Tutorials</a></h3>

  <p><a href="https://github.com/SlicerMorph/Tutorials/tree/main/GPA_3" target="_blank" rel="noopener nofollow ugc">main/GPA_3</a></p>

  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @anromero (2021-09-29 17:16 UTC)

<p>Okay, great! I’ll look at the tutorial and try it out. Thanks!</p>

---
