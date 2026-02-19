---
topic_id: 30784
title: "Problem With Files From Slicermorph In R"
date: 2023-07-25
url: https://discourse.slicer.org/t/30784
---

# Problem with files from SlicerMorph in R

**Topic ID**: 30784
**Date**: 2023-07-25
**URL**: https://discourse.slicer.org/t/problem-with-files-from-slicermorph-in-r/30784

---

## Post #1 by @Kajper (2023-07-25 15:15 UTC)

<p>Dear all,<br>
I have started to learn morphometic methods in biology recently. I was using SlicerMorph to place landmarks and samilandmarks on my segementated structures. I have a problem with geomorph (R pacage), I am trying to use my landmark data (right now just for tests) but it seems like fcvs files from Slicer won’t work. Like you can see in the photo, there are more columns than names in the file.<br>
I must say I beginner in coding and don’t know much, but the commands I am using should work with SlicerMorph files. Maybe I am missing something obvious there?<br>
Thanks in a dance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b828efa596bbe9967d0b91c763b93d27091bac1c.png" data-download-href="/uploads/short-url/qh9yHR6dL4tj6sZkmciSlt7cwc4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b828efa596bbe9967d0b91c763b93d27091bac1c.png" alt="image" data-base62-sha1="qh9yHR6dL4tj6sZkmciSlt7cwc4" width="690" height="210" data-dominant-color="30414D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">790×241 18.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecefee59183d0ed64dc9786a008780a481c33eee.png" data-download-href="/uploads/short-url/xO2Jrm9I1NGBer4yxqceNz6mzsa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecefee59183d0ed64dc9786a008780a481c33eee_2_690x99.png" alt="image" data-base62-sha1="xO2Jrm9I1NGBer4yxqceNz6mzsa" width="690" height="99" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecefee59183d0ed64dc9786a008780a481c33eee_2_690x99.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecefee59183d0ed64dc9786a008780a481c33eee.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecefee59183d0ed64dc9786a008780a481c33eee.png 2x" data-dominant-color="122744"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">980×141 18 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2023-07-25 16:18 UTC)

<p>Instead of geomorph, please use our own SlicerMorph R package you can install</p>
<pre><code class="lang-auto">devtools::install_github("SlicerMorph/SlicerMorphR")
</code></pre>
<p>then follow our tutorials</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/GPA_3">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/GPA_3" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/GPA_3" target="_blank" rel="noopener nofollow ugc"></a></h3>

  <p><a href="https://github.com/SlicerMorph/Tutorials/tree/main/GPA_3" target="_blank" rel="noopener nofollow ugc">//github.com/SlicerMorph/Tutorials/tree/main/GPA_3</a></p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
