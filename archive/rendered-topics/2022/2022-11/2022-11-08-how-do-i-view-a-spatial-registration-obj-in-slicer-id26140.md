---
topic_id: 26140
title: "How Do I View A Spatial Registration Obj In Slicer"
date: 2022-11-08
url: https://discourse.slicer.org/t/26140
---

# How do I view a Spatial Registration Obj in slicer?

**Topic ID**: 26140
**Date**: 2022-11-08
**URL**: https://discourse.slicer.org/t/how-do-i-view-a-spatial-registration-obj-in-slicer/26140

---

## Post #1 by @MikeC (2022-11-08 13:58 UTC)

<p>I have installed a few of the extensions, but it still will not load the SRO dcm file.</p>

---

## Post #2 by @pieper (2022-11-08 14:05 UTC)

<p>You need SlicerRT.  If that’s still not working provide more details.</p>

---

## Post #3 by @MikeC (2022-11-08 14:12 UTC)

<p>Hi Steve. I had installed SlicerRT extension, but slicer just said ‘Failed to load’ when I tried to add an SRO file that I had gotten from a vendor.</p>

---

## Post #4 by @pieper (2022-11-08 14:33 UTC)

<p>See if you can get de-identified sample data that you can share so other people can test and make suggestions.</p>

---

## Post #5 by @MikeC (2022-11-23 13:14 UTC)

<p>Hello Steve. Is it possible that SlicerRT needs more than just an SRO to display anything? I am not sure if it would display the attributes, or if it also expects to have images loaded prior to have something to apply the SRO to? If it should work with just the SRO, then I should be able to get an anonymized file.</p>

---

## Post #6 by @pieper (2022-11-23 18:07 UTC)

<p>If you load the SRO successfully then you should be able to inspect it and even display it in the Transforms module, but generally yes, you need some data to make sense of it.</p>

---

## Post #7 by @MikeC (2022-11-23 21:24 UTC)

<p>Ok thanks. But it just errors with no meaninful details as to why. I have attached here the SRO file that will not load into Slicer. It does load into a couple other DICOM attr viewers just fine. So if you can determine if the issue is with the SRO or SlicerRT, that would be great. Thanks in advance.</p>
<p>Mike</p>
<p>(Attachment cosylab_sro_fixed_tags.dcm is missing)</p>

---

## Post #8 by @pieper (2022-11-23 21:28 UTC)

<p><a class="mention" href="/u/mikec">@MikeC</a> You probably need to share via a different method (dropbox, google drive, etc).</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/gcsharp">@gcsharp</a> do you have input on this?</p>

---

## Post #9 by @MikeC (2022-11-23 21:29 UTC)

<p>Attaching the file again, w/o the dcm extension this time .</p>
<p>(Attachment cosylab_sro_fixed_tags is missing)</p>

---

## Post #10 by @gcsharp (2022-11-23 21:34 UTC)

<p>Mike, did you attach to the discourse?  I don’t see any attachment.</p>
<p>Maybe you can e-mail it to me or create a public download link.</p>

---

## Post #11 by @MikeC (2022-11-23 21:43 UTC)

<p>I had attached it via email notification, but also just tried to upload it here and that didn’t work either. So I would be happy to email it to you if I can get an address. Mine is <a href="mailto:mikecourtney48@yahoo.com">mikecourtney48@yahoo.com</a> if you would rather reach out to me directly rather than post it here. Thanks.</p>

---

## Post #12 by @gcsharp (2022-11-24 00:05 UTC)

<p>File received.  Thanks!  Don’t hesitate to ping me if I am silent too long.</p>

---

## Post #13 by @gcsharp (2022-11-24 18:23 UTC)

<p>Hi Mike.  I don’t yet have a final answer, but this REG has an uncommon format.  Does Cosylab (the manufacturer) provide a DICOM conformance statement?  -Greg</p>

---

## Post #14 by @MikeC (2022-11-25 14:47 UTC)

<p>Hello Greg,</p>
<p>I can reach out to Cosy for a statement. I just searched their web site and didn’t find one there that’s publicly assessible.<br>
But maybe this will be enough for now. Here are the tags that are parsed by another viewer, and here is the log file detailing the parsing is attached. A quick look at the tags by myself doesn’t show anything out of expectations, but maybe I missed something.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d1a44f7849c4f84e846cfed7a45ee4ef87240df.png" data-download-href="/uploads/short-url/k8fBwE6SSYbMo20ZR4l6USK7jrx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d1a44f7849c4f84e846cfed7a45ee4ef87240df.png" alt="image" data-base62-sha1="k8fBwE6SSYbMo20ZR4l6USK7jrx" width="425" height="500" data-dominant-color="EDEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">585×687 17.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks,<br>
Mike</p>
<p>(Attachment CosyLabSROLogFile.txt is missing)</p>

---

## Post #15 by @lassoan (2022-11-25 18:30 UTC)

<aside class="quote no-group" data-username="MikeC" data-post="14" data-topic="26140">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/977dab/48.png" class="avatar"> MikeC:</div>
<blockquote>
<p>I just searched their web site and didn’t find one there that’s publicly assessible</p>
</blockquote>
</aside>
<p>DICOM conformance statements must be made publicly accessible. If the company does not make one available, then it means that they actually do not officially support DICOM in their products. DICOM import/export may be just some untested, experimental feature.</p>

---

## Post #16 by @gcsharp (2022-11-25 23:18 UTC)

<p>Hi Mike,<br>
I fully agree with Andras.  Cosylab needs to publish a conformance statement.  Until that happens we can only guess.<br>
In my experience w awful vendor REG objects, there are two major misunderstanding.  The first is frame of reference issues.  The second is IEC vs DICOM.<br>
We are happy to help, but vendor support is needed.<br>
Greg</p>

---

## Post #17 by @MikeC (2022-11-30 15:12 UTC)

<p>Hi guys,</p>
<p>I will try to get their DCS, although it may not be a released feature yet. More soon.</p>
<p>Thanks,<br>
Mike</p>

---

## Post #18 by @gcsharp (2022-12-01 18:35 UTC)

<p>Meanwhile, what you can do is grab the Transformation Matrix out of the REG and stuff it into an ITK transform file.  The format is below:</p>
<pre><code class="lang-auto">#Insight Transform File V1.0
#Transform 0
Transform: AffineTransform_double_3_3
Parameters: 1 0 0 0 1 0 0 0 1 30 20 10
FixedParameters: 0 0 0
</code></pre>
<p>Note the rotation goes first, followed by the translation.  You might need to transpose (invert) the rotation, and/or negate (invert) the translation.</p>

---

## Post #19 by @MikeC (2022-12-02 18:53 UTC)

<p>Problem solved. They had a formatting error in their xform matrix. It imports now. Thanks for the replies.</p>

---
