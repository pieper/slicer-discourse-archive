---
topic_id: 872
title: "Faster Registration"
date: 2017-08-15
url: https://discourse.slicer.org/t/872
---

# Faster registration

**Topic ID**: 872
**Date**: 2017-08-15
**URL**: https://discourse.slicer.org/t/faster-registration/872

---

## Post #1 by @moselhy (2017-08-15 14:30 UTC)

<p>How do I get my multivolume sequence to register faster?</p>
<p>It is taking approx. 3 min and 2 seconds for the original volume sequence of spacing 1.95,1.95,1.95 and approx. 2 min 50 seconds for a downsampled volume sequence with a spacing of 5,5,5. Only a 12 second difference, which is not very significant…</p>
<p>I am using the <a href="https://github.com/moselhy/SlicerSequenceRegistration" rel="nofollow noopener">Sequence Registration module</a> with the <code>"generic rigid (all)"</code> preset, using frame <code>t=3</code> as the fixed volume</p>
<p><a href="https://moselhy.org/physics/original.seq.nrrd" rel="nofollow noopener">Link to original multivolume sequence</a><br>
<a href="https://moselhy.org/physics/downsampled.seq.nrrd" rel="nofollow noopener">Link to downsampled multivolume sequence</a></p>

---

## Post #2 by @lassoan (2017-08-15 16:54 UTC)

<p>Probably you need a custom preset (list of parameter files) that sets lower number of samples or different stopping condition (lower max number of iterations, larger convergence tolerance value, etc).</p>

---

## Post #3 by @moselhy (2017-08-15 19:11 UTC)

<p>I am doing this to make the <a href="https://github.com/moselhy/SlicerSequenceRegistration/blob/master/SequenceRegistration/SequenceRegistration.py#L378-L449" rel="nofollow noopener">“Reload and Test”</a> of the module faster than 3 minutes, should I just register the first 10 frames?</p>

---

## Post #4 by @lassoan (2017-08-15 19:13 UTC)

<p>For a basic module test it could be enough to register a few frames. Most likely you would detect if anything is wrong from 3 frames as well as from 20.</p>

---
