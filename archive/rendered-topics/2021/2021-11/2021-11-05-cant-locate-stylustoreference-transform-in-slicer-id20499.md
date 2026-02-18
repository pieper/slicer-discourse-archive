# Can't locate StylustoReference transform in Slicer

**Topic ID**: 20499
**Date**: 2021-11-05
**URL**: https://discourse.slicer.org/t/cant-locate-stylustoreference-transform-in-slicer/20499

---

## Post #1 by @askaderd (2021-11-05 16:30 UTC)

<p>Hi there,</p>
<p>I ran an XML file in PLUS server (code shown below). Following the Hardware Connections slide deck on the SlicerIGT website, I was trying to locate the StylustoReference transform within the scene configuration (slide 9) however I don’t see it. Here is what I currently see:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c5a4353193c652961e2215d68ae9767414cec97.png" alt="image" data-base62-sha1="mj9S7BLER0pWyUEJHmq5qrpouI7" width="526" height="419"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/277b2496b49cc61de1217af66541b8f92842f2d9.png" data-download-href="/uploads/short-url/5Dgs8AmBRs8tdwoGhA378lYtkV3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/277b2496b49cc61de1217af66541b8f92842f2d9.png" alt="image" data-base62-sha1="5Dgs8AmBRs8tdwoGhA378lYtkV3" width="690" height="466" data-dominant-color="FBF8FD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">952×643 16.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8862d9d530f7bd2c276de7b5631cbe1964fb9abe.png" data-download-href="/uploads/short-url/jswIPvBIZhOhTvVMR057p6B1pcG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8862d9d530f7bd2c276de7b5631cbe1964fb9abe.png" alt="image" data-base62-sha1="jswIPvBIZhOhTvVMR057p6B1pcG" width="361" height="500" data-dominant-color="F9F4F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">571×790 17 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am also unable to get recording the stream to work in Slicer. I can press the start recording button but it doesn’t actually start.</p>
<p>Any help would be appreciated!</p>

---

## Post #2 by @Sunderlandkyl (2021-11-05 16:43 UTC)

<p>There is no data stream from the tracker to the PlusOpenIGTLink server.<br>
The output channel from the tracker is “TrackerStream”, while the channel used by PlusOpenIGTLink is “TrackedVideoStream”.</p>
<p>You also don’t currently have an imaging device in your config file. You may need to remove the Image related elements from PlusOpenIGTLink.</p>

---

## Post #3 by @askaderd (2021-11-26 02:06 UTC)

<p>Thanks for the help! With the modifications it works now!</p>

---
