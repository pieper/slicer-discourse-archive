---
topic_id: 22950
title: "Creating A Volume From 4D Echo"
date: 2022-04-13
url: https://discourse.slicer.org/t/22950
---

# Creating a volume from 4D Echo

**Topic ID**: 22950
**Date**: 2022-04-13
**URL**: https://discourse.slicer.org/t/creating-a-volume-from-4d-echo/22950

---

## Post #1 by @jruben4 (2022-04-13 20:18 UTC)

<p>I’ve been able to import 4D echo DICOMs, but need a little help with the next step to create a volume render.</p>
<p>I’ve gotten to this step, and expected that I would see a volume render in the white box, but I must be missing a step?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8013877eb69b94decf889862662a1df9833c7cc.jpeg" data-download-href="/uploads/short-url/sxk6LEh3iBxd5jwWU1HcA2gbtZG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8013877eb69b94decf889862662a1df9833c7cc_2_690x325.jpeg" alt="image" data-base62-sha1="sxk6LEh3iBxd5jwWU1HcA2gbtZG" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8013877eb69b94decf889862662a1df9833c7cc_2_690x325.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8013877eb69b94decf889862662a1df9833c7cc_2_1035x487.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8013877eb69b94decf889862662a1df9833c7cc_2_1380x650.jpeg 2x" data-dominant-color="9495AC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1880×886 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-04-13 20:29 UTC)

<p>We’ll soon (when the accompanying journal paper gets accepted) release our cardiac volume rendering module that uses noise filtering, fine-tuned transfer functions, and a special volume rendering shader (depth-dependent coloring) to produce images that have similar appearance to what you see on commercial systems.</p>
<p>Until this module is released, you can use the built-in volume rendering module, start from the <code>US-Fetal</code> volume rendering preset, and tune the transfer functions manually. You may also try to reach out to the PI, <a href="https://www.research.chop.edu/jolley-laboratory">Dr Matt Jolley</a> to see if you can get early access to the module.</p>

---

## Post #3 by @jruben4 (2022-04-13 20:36 UTC)

<p>Thanks -</p>
<p>I feel like I must be missing a step.  I’ve got the US-Fetal preset selected, but still only seeing my 3 planes but no volume render.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/576e01fb8e1d874ab80e1c29f21258d00548fc98.png" alt="image" data-base62-sha1="ctrehN7E4aF3cPYmVugHkKYD0KI" width="567" height="273"></p>

---

## Post #4 by @lassoan (2022-04-13 20:43 UTC)

<p>It looks like you are not using the very latest Slicer version. Please install the latest Slicer Preview Release. If the volume still does not appear then you can try disabling <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view">“depth peeling”</a> and then enabling it again.</p>

---

## Post #5 by @jruben4 (2022-04-19 17:45 UTC)

<p>This worked with the most recent preview version of slicer.  Thanks!</p>

---
