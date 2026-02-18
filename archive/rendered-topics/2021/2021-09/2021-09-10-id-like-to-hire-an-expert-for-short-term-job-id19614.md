# I'd like to hire an expert for short term job

**Topic ID**: 19614
**Date**: 2021-09-10
**URL**: https://discourse.slicer.org/t/id-like-to-hire-an-expert-for-short-term-job/19614

---

## Post #1 by @matthedd (2021-09-10 18:54 UTC)

<p>Hi everyone I hope it’s ok to post this here. I am looking to hire someone to write something in Slicer that automates the following task for an NSF-funded research project: I have an image stack of multiple bones and I want to “shrinkwrap” each one and export to a separate surface .ply. The bones are not touching so I imagine it is simple for someone with the right expertise.</p>
<p>I used to do this with an Amira script (found here: <a href="https://github.com/evolgenomics/shrinkwrapping/blob/master/baculae_segment_surfaceGen.hx" class="inline-onebox" rel="noopener nofollow ugc">shrinkwrapping/baculae_segment_surfaceGen.hx at master · evolgenomics/shrinkwrapping · GitHub</a>) but I no longer have access to Amira and long term I need something that is open source.</p>
<p>I could pay ~$50 per hour. If you are interested please email matthew.dean@usc.edu<br>
Thanks,<br>
Matt</p>

---

## Post #2 by @muratmaga (2021-09-10 19:27 UTC)

<p>Well not to discourage you to hiring people but this is already very easy with existing tools, without programing. You can perhaps learn to script and think of it as an investment to the future:</p>
<p>Steps are:</p>
<ol>
<li>ImageStacks (SlicerMorph extension) to import the stack.</li>
<li>Open volume in the Segment Editor and use threshold + Island tools to separate the individual bones into separate segments. This should be real simple, if the bones are not touching.</li>
<li>Export the segments to models, and save them as PLY</li>
</ol>
<p>2nd step may benefit from WrapSurfaceSolidy or margin dilation depending on the type of the bone.</p>

---

## Post #3 by @matthedd (2021-09-10 19:47 UTC)

<p>Thanks. I’ll give it a shot. If you know of anyone who might want some extra cash (student?) let them know. It’s probably easy money for them and I don’t mind paying just to get it done.</p>
<p>Thanks again, much appreciated,</p>
<p>Matt</p>

---

## Post #4 by @matthedd (2021-09-10 19:52 UTC)

<p>I’m already stuck <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=10" title=":blush:" class="emoji" alt=":blush:"> ImageStacks not in the Extension Manager?</p>

---

## Post #5 by @muratmaga (2021-09-10 20:13 UTC)

<p>It is part of SLicerMorph extension.</p>

---
