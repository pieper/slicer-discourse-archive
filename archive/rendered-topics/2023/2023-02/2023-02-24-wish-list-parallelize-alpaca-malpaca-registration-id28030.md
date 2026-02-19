---
topic_id: 28030
title: "Wish List Parallelize Alpaca Malpaca Registration"
date: 2023-02-24
url: https://discourse.slicer.org/t/28030
---

# Wish list: parallelize ALPACA / MALPACA registration

**Topic ID**: 28030
**Date**: 2023-02-24
**URL**: https://discourse.slicer.org/t/wish-list-parallelize-alpaca-malpaca-registration/28030

---

## Post #1 by @MrMarkus (2023-02-24 09:10 UTC)

<p>Dear slicerMorph developers,</p>
<p>might it be possible to consider parallelizing the MALPACA registration process?</p>
<p>e.g. run the registration process for each template  and the target mesh set in parallel.</p>
<pre><code>    -&gt; 4 templates, 60 target meshes
          --&gt; 4 "tasks" in parallel:           
                            # template 1 &amp; 60 targets
                            # template 2 &amp; 60 targets
                            # template 3 &amp; 60 targets
                            # template 4 &amp; 60 targets
</code></pre>
<p>I guess that would speed up the alignment process.</p>
<p>Best,<br>
Markus</p>

---

## Post #2 by @muratmaga (2023-02-24 15:32 UTC)

<p>All the computations in ALPACA are already multi-threaded so there is nothing to be gained from running tasks in parallel on the same computer. In fact if you do that outcome will be opposite of what you expect, each task will run longer due to resource competition.</p>
<p>Why do you seek task parallelization? It should be already really fast, on my laptop I can get a registration of a mouse skull in about 50 seconds, faster if I use the my desktop with lots more core.</p>
<p>Usually it is the deformable registration step that takes longest chunk in ALPACA. If you are on windows you can use the Bayesian CPD, which gives about 10X speed up and is available at:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/ohirose/bcpd">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/ohirose/bcpd" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/e2a3daccff6082eb4af54d42ad1c5bbdb8defc1461deb60d7135a17615d7c9ef/ohirose/bcpd" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/ohirose/bcpd" target="_blank" rel="noopener">GitHub - ohirose/bcpd: Bayesian Coherent Point Drift (BCPD/BCPD++/GBCPD/GBCPD++)</a></h3>

  <p>Bayesian Coherent Point Drift (BCPD/BCPD++/GBCPD/GBCPD++) - GitHub - ohirose/bcpd: Bayesian Coherent Point Drift (BCPD/BCPD++/GBCPD/GBCPD++)</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Unfortunately it requires building from scratch for MacOS and Linux, so we don’t distribute it with ALPACA, but it can be enabled under the Advanced options (check the acceleration and point out to the folder where bcpd lives).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fad2e56103f53583fcf637aedc3c43b6756c52e.png" data-download-href="/uploads/short-url/mMyXil8RTydhHZefrwvufgVhnxc.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fad2e56103f53583fcf637aedc3c43b6756c52e.png" alt="image" data-base62-sha1="mMyXil8RTydhHZefrwvufgVhnxc" width="690" height="220" data-dominant-color="F6F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">793×253 10.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @MrMarkus (2023-02-24 19:06 UTC)

<p>Hi,</p>
<p><em>Why do you seek task parallelization? It should be already really fast, on my laptop I can get a registration of a mouse skull in about 50 seconds, faster if I use the my desktop with lots more core.</em></p>
<ul>
<li>the motivation is to speed up the registration process and to make use of the CPU cores / resources.</li>
<li>during the optimiztion a single core is utilized and the remaining cores seem to be idle.</li>
</ul>
<p>I have to mention that the skull registration is done on high resolution microCT data, 36 micron, and no<br>
reduction of the surface mesh is applied. Thus, for a single skull, using 5000 surface points, registration takes roughly 2 - 3 minutes.</p>
<p>Of course, one can debate what fast/slow means.</p>
<p>Anyway, I was not aware that the algorithm is already parallelized.<br>
And for sure  I will take a look at the Bayesian CPD algorithm too.</p>
<p>Thanks.</p>
<p>Best,<br>
Markus</p>

---

## Post #4 by @muratmaga (2023-02-25 00:27 UTC)

<aside class="quote no-group" data-username="MrMarkus" data-post="3" data-topic="28030">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<p>I have to mention that the skull registration is done on high resolution microCT data, 36 micron, and no<br>
reduction of the surface mesh is applied. Thus, for a single skull, using 5000 surface points, registration takes roughly 2 - 3 minutes.</p>
</blockquote>
</aside>
<p>When you are in the 4000-6000 point range, for a desktop with a recent CPU with 8 cores, the speed should be about 1m / sample, but that’s of course entirely dependent on the number of cores, their speed and their cpu generation.</p>
<p>Yes, do try the BCPD if you are going to run lots of these. Improvement should be quite dramatic.</p>

---

## Post #5 by @MrMarkus (2023-03-01 13:08 UTC)

<p>Hi,</p>
<p>thanks for the hint! The BCPD algorithm dramatically boosts the computation;<br>
the registration of ~ 5000 points takes now &lt; 30 sec on a Xeon E3-1240 (3.5GHz, 4 cores).</p>
<p>Best,<br>
Markus</p>

---
