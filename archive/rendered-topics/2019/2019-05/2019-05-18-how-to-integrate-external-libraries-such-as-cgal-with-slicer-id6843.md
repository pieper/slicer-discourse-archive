# How to integrate external libraries such as CGAL with slicer 3D?

**Topic ID**: 6843
**Date**: 2019-05-18
**URL**: https://discourse.slicer.org/t/how-to-integrate-external-libraries-such-as-cgal-with-slicer-3d/6843

---

## Post #1 by @Baseer_Piracha (2019-05-18 13:54 UTC)

<p>How to integrate external libraries such as CGAL with slicer 3D?</p>

---

## Post #2 by @lassoan (2019-05-18 14:09 UTC)

<p>If you work in Python then you can pip install cgal. If you work in C++ then you can create a superbuild-type extension (that downloads and builds its own dependent libraries, for example how SlicerRT extension builds Plastimatch library).</p>

---

## Post #3 by @adamrankin (2019-05-18 14:26 UTC)

<p>For C++, an example is OpenCV</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Slicer/SlicerOpenCV">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/SlicerOpenCV" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/a8fbd874814de7897123b119d1a1b52a9570135881834bd5fca8b8b7880f6146/Slicer/SlicerOpenCV" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Slicer/SlicerOpenCV" target="_blank" rel="noopener nofollow ugc">GitHub - Slicer/SlicerOpenCV: Slicer Extension wrapping OpenCV</a></h3>

  <p>Slicer Extension wrapping OpenCV. Contribute to Slicer/SlicerOpenCV development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Baseer_Piracha (2019-06-08 14:28 UTC)

<p>I have already downloaded and build the 3D slicer from github, and its running. Now the question is I’m not under standing how add some external libraries from other opensource softwares like CGAL etc…<br>
and how to remove the existing libraries from 3D slicer which I don’t want…<br>
Kindly elaborate please.</p>

---

## Post #5 by @pieper (2019-06-08 16:12 UTC)

<aside class="quote no-group" data-username="Baseer_Piracha" data-post="4" data-topic="6843">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/baseer_piracha/48/3753_2.png" class="avatar"> Baseer_Piracha:</div>
<blockquote>
<p>I’m not under standing how add some external libraries from other opensource softwares like CGAL etc…<br>
and how to remove the existing libraries from 3D slicer</p>
</blockquote>
</aside>
<p>That’s a big topic, but the basics are that Slicer is at the core a C++ application with a build system based on CMake, so you can add or remove libraries as needed using pretty standard methods.</p>
<p>Of course there are also lots of conventions, so you would do well to study the examples that <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/adamrankin">@adamrankin</a> pointed to already.</p>
<p>And you can review any of <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers">the developer documentation</a> to learn how Slicer is built.</p>

---
