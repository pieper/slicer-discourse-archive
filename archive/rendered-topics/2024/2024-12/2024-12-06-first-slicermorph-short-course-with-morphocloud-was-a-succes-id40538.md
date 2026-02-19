---
topic_id: 40538
title: "First Slicermorph Short Course With Morphocloud Was A Succes"
date: 2024-12-06
url: https://discourse.slicer.org/t/40538
---

# First SlicerMorph short course with MorphoCloud was a success!

**Topic ID**: 40538
**Date**: 2024-12-06
**URL**: https://discourse.slicer.org/t/first-slicermorph-short-course-with-morphocloud-was-a-success/40538

---

## Post #1 by @muratmaga (2024-12-06 03:01 UTC)

<p>We just wrapped up 4th and final day of SlicerMorph 101 short course. It was a big success. As someone who had done fair number of online short courses like this and do <strong>NOT</strong> like the online format, I should say this worked very well and was a big success. So here are some notes, if anyone is interested</p>
<p>This was the first real test of the <a href="https://instances.morpho.cloud">MorphoCloud infrastructure we have been building</a>. There were total of 28 attendees, and each attendee got their own private <a href="https://docs.jetstream-cloud.org/general/instance-flavors/#jetstream2-gpu">g3.xl instance on JetStream2</a> along with a persistent 100GB private storage volume. We also created a network share with the sample data preloaded, to which the attendees had R/O access.</p>
<p><strong>What worked:</strong></p>
<ul>
<li>No “I cannot find that folder/module/extension”</li>
<li>Ease of direct access to the instances from backdoor for troubleshooting (though we mostly used the screen share so that everyone can benefit).</li>
<li>Connections were pretty good (though everyone was from US and we advised them to use their university wired connections for best performance).</li>
<li>Pretty much everything.</li>
</ul>
<p><strong>What didn’t work:</strong></p>
<ul>
<li>While I thought I emphasized that they should launch their instances prior to the course, this was apparently not clear to about 50% attendees. It takes about 5-15 minutes to fully provision an instance from scratch and for the attendee to receive the email. So this needs to be done earlier.</li>
<li>Learning to unshelve the instances took some time (first 1/2 day).</li>
<li>Linux desktop experienc can be improved (probably need a few more shortcuts) etc…</li>
<li>A driver conflict on the JS2 broke torch. So we werent able to run DL workflows. Funnily enough this had no affect on the 3D rendering performance. (We should be able to update this next week)</li>
</ul>
<p>These are people had no prior cloud experience and except for a few they didn’t know anything about linux terminal and running things from command line. So the first few hours was a bit shaky, but rest of the days were smooth sailing, so much more than I have anticipated. This is backed up by their post-course survey input:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d26560e46050502d25175f2cd6a013640e9cd597.png" data-download-href="/uploads/short-url/u1ftdhetYjBD4PcCCStxvxFTgur.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d26560e46050502d25175f2cd6a013640e9cd597_2_517x216.png" alt="image" data-base62-sha1="u1ftdhetYjBD4PcCCStxvxFTgur" width="517" height="216" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d26560e46050502d25175f2cd6a013640e9cd597_2_517x216.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d26560e46050502d25175f2cd6a013640e9cd597_2_775x324.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d26560e46050502d25175f2cd6a013640e9cd597.png 2x" data-dominant-color="E4E6EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">867×362 32.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you would like to see the instructions from the course it is:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph101">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph101" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/74b3770de576d05acc4148179627548b/SlicerMorph/SlicerMorph101" class="thumbnail">

  <h3><a href="https://github.com/SlicerMorph/SlicerMorph101" target="_blank" rel="noopener">GitHub - SlicerMorph/SlicerMorph101: Introduction to 3D Morphology with 3D Slicer and...</a></h3>

    <p><span class="github-repo-description">Introduction to 3D Morphology with 3D Slicer and SlicerMorph</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I should emphasize the whole infrastructure done by <a class="mention" href="/u/jcfr">@jcfr</a> by <a href="https://gitlab.com/exosphere/exosphere/">repurposing parts of the JS2 Exosphere interface</a>. To be perfectly honest, I was a bit skeptical on github based automation… But at this point I think it is working quite well, and I suspect we might even tweak a bit better. For those of you who are interested looking under the hood, and perhaps even using for your workshops, the whole workflow is available at <a href="https://github.com/MorphoCloud/MorphoCloudWorkflow" class="inline-onebox">GitHub - MorphoCloud/MorphoCloudWorkflow: Reusable GitHub Workflows to manage JetStream2 backed on-demand virtual machines</a></p>

---

## Post #2 by @fedorov (2024-12-12 17:27 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> thank you for sharing this summary - very helpful!</p>
<p>I’ve been trying to follow this development from <a class="mention" href="/u/jcfr">@jcfr</a> presentation and discussions with <a class="mention" href="/u/pieper">@pieper</a>, and I think it has a huge potential. I hope you can make it to the Project Week sometime to chat about this and related topics a bit more!</p>

---

## Post #3 by @muratmaga (2024-12-12 18:14 UTC)

<p>I will be at Las Palmas. Looking forward to chatting.</p>

---

## Post #4 by @muratmaga (2025-12-15 00:40 UTC)

<p>A year and about 300 users later, few more notes:</p>
<ol>
<li>Official website is <a href="https://morphocloud.org" rel="noopener nofollow ugc">https://morphocloud.org</a></li>
<li>In addition to the individual requests, we now support workshop requests for which the organizer can ask for multiple instances that doesn’t shelf themselves when unused (thought they are capped at 5+1 days, so it needs to be short-term event).</li>
<li>If you want to go straight to requests, use <a href="https://request.morphocloud.org" rel="noopener nofollow ugc">https://request.morphocloud.org</a></li>
<li>There is a short-tutorial about the commands, interface options (definitely use TurboVNC instead of web browser for better performance) on SlicerMorph tutorials: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/MorphoCloud#readme" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/MorphoCloud at main · SlicerMorph/Tutorials · GitHub</a></li>
<li>Another short tutorial for getting started quickly (using a preconfigured python virtual environment) with NNInteractive is here: <a href="https://github.com/SlicerMorph/Tutorials/blob/main/MorphoCloud/NNInteractive/NNInteractive.MD" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/MorphoCloud/NNInteractive/NNInteractive.MD at main · SlicerMorph/Tutorials · GitHub</a></li>
<li>A preprint about the infrastructure is forthcoming.</li>
</ol>
<p>What remains a challenge is finding available resources on the JetStream2 due to its popularity. Recent addition of new GPU nodes, and increasing the number of g3.l GPU instances (our default instance type) helped a bit.</p>

---

## Post #5 by @muratmaga (2025-12-29 01:51 UTC)

<p>The new MorphoCloud preprint is now online:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://arxiv.org/abs/2512.21408">
  <header class="source">
      <img src="https://arxiv.org/static/browse/0.3.4/images/icons/favicon-32x32.png" class="site-icon" alt="" width="32" height="32">

      <a href="https://arxiv.org/abs/2512.21408" target="_blank" rel="noopener nofollow ugc">arXiv.org</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/402;"><img src="https://static.arxiv.org/icons/twitter/arxiv-logo-twitter-square.png" class="thumbnail" alt="" width="500" height="500"></div>

<h3><a href="https://arxiv.org/abs/2512.21408" target="_blank" rel="noopener nofollow ugc">MorphoCloud: Democratizing Access to High-Performance Computing for...</a></h3>

  <p>The digitization of biological specimens has revolutionized the field of morphology, creating large collections of 3D data, and microCT in particular. This revolution was initially supported by the development of open-source software tools,...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
