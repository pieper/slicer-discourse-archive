# Feedback about other algorithm improving the efficiency of Slicer

**Topic ID**: 24250
**Date**: 2022-07-09
**URL**: https://discourse.slicer.org/t/feedback-about-other-algorithm-improving-the-efficiency-of-slicer/24250

---

## Post #1 by @mau_igna_06 (2022-07-09 12:22 UTC)

<p>Here is the change:</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/mauigna06/VTK/commit/f330f7a16128fec9aa2edc0d612cbf72446ad060">
  <header class="source">

      <a href="https://github.com/mauigna06/VTK/commit/f330f7a16128fec9aa2edc0d612cbf72446ad060" target="_blank" rel="noopener">github.com/mauigna06/VTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/mauigna06/VTK/commit/f330f7a16128fec9aa2edc0d612cbf72446ad060" target="_blank" rel="noopener">ENH: change Jacobi algorithm by GaussSeidel for performance improvement reasons</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-07-09" data-time="12:16:55" data-timezone="UTC">12:16PM - 09 Jul 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/mauigna06" target="_blank" rel="noopener">
          <img alt="mauigna06" src="https://avatars.githubusercontent.com/u/19158307?v=4" class="onebox-avatar-inline" width="20" height="20">
          mauigna06
        </a>
      </div>

      <div class="lines" title="changed 1 files with 189 additions and 2 deletions">
        <a href="https://github.com/mauigna06/VTK/commit/f330f7a16128fec9aa2edc0d612cbf72446ad060" target="_blank" rel="noopener">
          <span class="added">+189</span>
          <span class="removed">-2</span>
        </a>
      </div>
    </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It appears it doesn’t breaks anything in the build or while using Slicer.</p>
<p>It was implemented according to this (and it is said to have a faster convergence):</p><aside class="onebox pdf" data-onebox-src="https://college.cengage.com/mathematics/larson/elementary_linear/5e/students/ch08-10/chap_10_2.pdf">
  <header class="source">

      <a href="https://college.cengage.com/mathematics/larson/elementary_linear/5e/students/ch08-10/chap_10_2.pdf" target="_blank" rel="noopener">college.cengage.com</a>
  </header>

  <article class="onebox-body">
    <a href="https://college.cengage.com/mathematics/larson/elementary_linear/5e/students/ch08-10/chap_10_2.pdf" target="_blank" rel="noopener"><span class="pdf-onebox-logo"></span></a>

<h3><a href="https://college.cengage.com/mathematics/larson/elementary_linear/5e/students/ch08-10/chap_10_2.pdf" target="_blank" rel="noopener">chap_10_2.pdf</a></h3>

  <p class="filesize">123.72 KB</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/pieper">@pieper</a> I would appreciate your opinion. VerySleepy said that Slicer used a lot of time on this function.</p>

---

## Post #2 by @pieper (2022-07-09 17:30 UTC)

<p>Nice work <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> That’s just the way it is meant to be done <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---

## Post #3 by @jcfr (2022-07-11 20:33 UTC)

<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> Could you submit a merge request against the upstream VTK project and reference the link here ?</p>
<p>See <a href="https://gitlab.kitware.com/vtk/vtk/-/blob/master/CONTRIBUTING.md">https://gitlab.kitware.com/vtk/vtk/-/blob/master/CONTRIBUTING.md</a></p>
<p>While working on the merge request, considering including details like these ones in the commit description:</p>
<ul>
<li>performance improvement benchmarks</li>
<li>tradeoff &amp; limitation of the new approach (if any)</li>
</ul>

---

## Post #4 by @mau_igna_06 (2022-07-12 17:37 UTC)

<p>I did a pseudo benchmark with Slicer (when I have more free time I’ll create a standalone VTK app to test this) by building it with the “original” and “modified” version of vtkMath::JacobiN.</p>
<p>The pseudo benchmark test was set the scene with 500 points in one MarkupsFiducial and to turn on the auto rotate 3D view for 100 seconds, and by analyzing the call stack with VerySleepy.</p>
<p>These are the results:</p>
<blockquote>
<p>original<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/788244a836349e4861fd12248485b64f884c58eb.png" data-download-href="/uploads/short-url/hc4otu8drdqnHCIYuKuHWteK40b.png?dl=1" title="benchmark100seconds_original" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/788244a836349e4861fd12248485b64f884c58eb.png" alt="benchmark100seconds_original" data-base62-sha1="hc4otu8drdqnHCIYuKuHWteK40b" width="690" height="387" data-dominant-color="EBEBE8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">benchmark100seconds_original</span><span class="informations">1366×768 89.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
<blockquote>
<p>modified<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d5e4974a8db47b064472d0b976a862946fed80a.png" data-download-href="/uploads/short-url/6tluGMh7UUSqIqC27gOiiNQpyjg.png?dl=1" title="benchmark100seconds_modified" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d5e4974a8db47b064472d0b976a862946fed80a.png" alt="benchmark100seconds_modified" data-base62-sha1="6tluGMh7UUSqIqC27gOiiNQpyjg" width="690" height="387" data-dominant-color="ECECE9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">benchmark100seconds_modified</span><span class="informations">1366×768 76 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
<p>As you can see the exclusive time of execution reduced from 0.21seconds to 0.14seconds (and it cannot be seen in the pictures but the execution count of these functions was approx 750 and 850 correspondingly).</p>
<p>These agrees with what is said on the book I linked in my first post:</p>
<blockquote>
<p>GaussSeidel 5 iterations have the same accuracy than Jacobi 7 iterations.</p>
</blockquote>
<hr>
<p>Also, from this source:"Yang, King H. (2018). Basic Finite Element Method as Applied to Injury Biomechanics || Stepping Through Finite Element Analysis. , (), 281–308. doi:10.1016/B978-0-12-809831-8.00007-6 ": you can see the tables of the solution of a 3x3 linear system with Jacobi and GaussSeidel, my yellow highlight shows when solution reaches 1% accuracy:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/eda3c1f90a86e0df08b6e50e26aa37f70b5ae0cc.png" alt="JacobiTable" data-base62-sha1="xUg0Bx3JRsO83GGwNjc0fJdF7Bi" width="552" height="478"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65d27f3e0851b6824c1de18ab92267d10690062f.png" alt="GaussSeidelTable" data-base62-sha1="ewLdafzTqFZjiyTdURxKY1ppvoX" width="408" height="404"></p>
<p>The book says the only reason to give Jacobi preference from GaussSeidel is that Jacobi can be parallelized, so we could have it mind for some GPU implementation on the future. Because we are executing in CPU we should use GaussSeidel.</p>
<p>There is no final word yet because I have to create a pure VTK example to test this out, but I’ll do it, probably, this next weekend</p>

---

## Post #5 by @lassoan (2022-07-12 19:27 UTC)

<p>Thank you for looking into this!</p>
<p>We do performance profiling from time to time and whenever any specific performance problem comes up, but I don’t recall any performance bottlenecks related to <code>vtkMath::JacobiN</code>. Do you have a use case where this method plays a significant role?</p>
<p>Note that VerySleepy is a very simple, convenient tool that can give hints about performance bottlenecks, but it is not very specific or reliable (it may give misleading results, so never rely on it as a single source). I would recommend to use Visual Studio’s built in performance profiler in addition to VerySleepy.</p>
<p>I’ve also found profilers are great for pinpointing very signficiant bottlenecks, but once you fixed those then they start to give misleading results. Always check elapsed time for a complete end-user function to see if any performane optimization leads to actually faster performance. For some quantitive testing, you can use the FPS marker in 3D views, Performance Tests module, or Node Modified Statistics module in DeveloperTools extension.</p>
<p>Make sure to do performance profiling on an application built in RelWithDebInfo mode. Debug mode builds have very different performance bottlenecks; and Release mode without debug information does not give you specific information.</p>
<p>Even if the proposed change does not to lead to any user-perceivable performance improvements (performance would only improve if this method was used in a hot loop), it may still make sense to proceed with it, as it does not seem to have any disadvantages (it is not more complicated or less robust or less accurate as the current implementation).</p>

---

## Post #6 by @mau_igna_06 (2022-07-12 21:58 UTC)

<p>I finally found a book that talks about calculating eigenvalues and eigenvectors with iterative methods</p>
<aside class="onebox pdf" data-onebox-src="https://math.mit.edu/classes/18.086/2006/am62.pdf">
  <header class="source">

      <a href="https://math.mit.edu/classes/18.086/2006/am62.pdf" target="_blank" rel="noopener nofollow ugc">math.mit.edu</a>
  </header>

  <article class="onebox-body">
    <a href="https://math.mit.edu/classes/18.086/2006/am62.pdf" target="_blank" rel="noopener nofollow ugc"><span class="pdf-onebox-logo"></span></a>

<h3><a href="https://math.mit.edu/classes/18.086/2006/am62.pdf" target="_blank" rel="noopener nofollow ugc">am62.pdf</a></h3>

  <p class="filesize">105.28 KB</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>According to it:</p>
<blockquote>
<p>one Gauss-Seidel step is worth two Jacobi steps</p>
</blockquote>
<p>But now I have to go deep into implementation, it isn’t so simple as it appeared in the beginning but I’ll work more on it on the weekend</p>

---

## Post #7 by @lassoan (2022-07-13 12:42 UTC)

<p>Before digging into this, I would recommend to verify that this will lead to perceivable speed improvement for users. For example, see if anything gets visibly faster if you manually limit the maximum number of iterations. If the method is only responsible for 0.1% of the computation time then even a 10x speed improvement might not worth a lot of development time investment. The same effort might be better spent on more impactful changes.</p>

---
