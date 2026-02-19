---
topic_id: 730
title: "Intrasubject Brain Preoperative Mri To Postoperative Ct Regi"
date: 2017-07-20
url: https://discourse.slicer.org/t/730
---

# Intrasubject Brain preoperative MRI to postoperative CT registration

**Topic ID**: 730
**Date**: 2017-07-20
**URL**: https://discourse.slicer.org/t/intrasubject-brain-preoperative-mri-to-postoperative-ct-registration/730

---

## Post #1 by @JNPS (2017-07-20 17:40 UTC)

<p>Hey everyone,<br>
I am looking for the best way to</p>
<ol>
<li>Register intrasubject preoperative T1 MRI to T2 MRI of the brain</li>
<li>Register a postoperative CT (DBS-electrodes) to the coregistered preoperative MRI of the same subject</li>
</ol>
<p>Step 1 is no problem for me but I have trouble registering the reg. MRI to the postOP CT<br>
I was thinking about the following procedure:</p>
<ol>
<li>Align centers with volume modul</li>
<li>Use BRAINs registration with: MRI as fixed and postOP CT as moving volume, percentage of sample 0.01, useCenterOFHeadAlign, Rigid and Affine registration phases.</li>
</ol>
<p>Afterwards my aim is to normalize and register this MRIT1/T2_postOPCT registration to an atlas.<br>
I am particularly interested in subcortical regions as e.g. the STN</p>
<p>Questions:</p>
<ol>
<li>Is the above mentioned way apropriate or am I missing something (e.g. ROI-mask, bias intensity inhomogenity correction) as it doesn’t give me well fitting results…</li>
<li>Is an affine registration still okay as I need the electrode positions as exactly as possible and therefore need to have the best registration result with as much “linearity” as possible?</li>
<li>What ist the best way to check for a good result of the registration of a CT of the brain to an MRI of the brain in your experience?</li>
</ol>
<p>I am very grateful for any help or comment <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @ihnorton (2017-07-20 18:01 UTC)

<p>The procedure you outline sounds ok. I’ve done similar things in the past, and BRAINS typically works fine without too much intervention. For detailed suggestions on CT-&gt;MR, see the <a href="https://na-mic.org/wiki/Projects:RegistrationDocumentation:UseCaseInventory">Slicer registration library</a>. For your specific workflow, two possible issues are:</p>
<ul>
<li>skull-stripping the T1/T2 brains before registration. If you need to use skull-stripped brains for atlas purposes, do the CT-&gt;MR registration against a raw MR and use that transform.</li>
<li>“too much” scatter noise in the CT. You should still be able to clearly see the skull and the brain outline when you adjust the window/level appropriately, even though there is a lot of streaking from the electrode interference.</li>
</ul>
<p>If you still have a problem and can provide 1 or 2 <strong>anonymous(!!)</strong> screenshot comparisons of the registration result, maybe we can suggest some options.</p>
<aside class="quote no-group" data-username="JNPS" data-post="1" data-topic="730">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b5ac83/48.png" class="avatar"> JNPS:</div>
<blockquote>
<p>Is an affine registration still okay as I need the electrode positions as exactly as possible and therefore need to have the best registration result with as much “linearity” as possible?</p>
</blockquote>
</aside>
<p>If there isn’t too much brain shift then rigid should be sufficient – the disturbed craniotomy area is only a small part of the total skull. If there is a lot of brain shift, affine won’t help (see below).</p>
<aside class="quote no-group" data-username="JNPS" data-post="1" data-topic="730">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b5ac83/48.png" class="avatar"> JNPS:</div>
<blockquote>
<p>What ist the best way to check for a good result of the registration of a CT of the brain to an MRI of the brain in your experience?</p>
</blockquote>
</aside>
<p>Usually the gross alignment is easy to inspect manually with the Slicer compare tools (compare the skull overlap), but the issue is that there is often brain shift where the electrodes are placed – typically decompression – so it is difficult to correlate exactly back to the MR. There are many deformable registration approaches available, some in Slicer, but “validation” is then up to expert review as there isn’t really any ground truth.</p>

---

## Post #3 by @JNPS (2017-07-21 07:18 UTC)

<p>Thank you for this detailed answer and for confirming the registration approach.<br>
The decompression because of brainshift is a good point. I will try to add a brainshift correction of the examined area after the general registration to avoid this influence.<br>
I’ll give it a try and see how it works <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
