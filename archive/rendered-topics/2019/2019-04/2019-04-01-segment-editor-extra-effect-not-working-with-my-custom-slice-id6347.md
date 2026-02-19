---
topic_id: 6347
title: "Segment Editor Extra Effect Not Working With My Custom Slice"
date: 2019-04-01
url: https://discourse.slicer.org/t/6347
---

# Segment editor extra effect not working with my custom Slicer version

**Topic ID**: 6347
**Date**: 2019-04-01
**URL**: https://discourse.slicer.org/t/segment-editor-extra-effect-not-working-with-my-custom-slicer-version/6347

---

## Post #1 by @imuy5733 (2019-04-01 04:24 UTC)

<h2><a name="p-22686-hello-i-installed-the-segment-editor-extra-effect-however-i-get-an-error-message-like-attached-the-icons-also-seem-to-be-incorrect-what-can-i-do-error690x371upload792cwhq2vaucsavs8hshrvsgav7jpeg-1" class="anchor" href="#p-22686-hello-i-installed-the-segment-editor-extra-effect-however-i-get-an-error-message-like-attached-the-icons-also-seem-to-be-incorrect-what-can-i-do-error690x371upload792cwhq2vaucsavs8hshrvsgav7jpeg-1" aria-label="Heading link"></a>Hello,<br>
I installed the Segment editor extra effect. However, I get an error message like attached.<br>
The icons also seem to be incorrect.<br>
What can I do?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/3214e2c8a254cfb1402360f34adf465ae1c56949.jpeg" data-download-href="/uploads/short-url/792Cwhq2VAUcSAvs8hshrVSGAv7.jpeg?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3214e2c8a254cfb1402360f34adf465ae1c56949_2_690x371.jpeg" alt="error" data-base62-sha1="792Cwhq2VAUcSAvs8hshrVSGAv7" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3214e2c8a254cfb1402360f34adf465ae1c56949_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/3214e2c8a254cfb1402360f34adf465ae1c56949.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/3214e2c8a254cfb1402360f34adf465ae1c56949.jpeg 2x" data-dominant-color="AFADAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1001×539 99.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></h2>
<p>Win10<br>
Slicer 4.10.1<br>
Extra effect 4.9</p>

---

## Post #2 by @jamesobutler (2019-04-01 11:39 UTC)

<p>How did you install the SegmentEditorExtraEffects extension? Did you install this extension using the extensions manager? Or did you do a manual copy/manual install from file? I see the path …/SegmentEditorExtraEffects/lib/Slicer4.9/… which would indicate this was originally from a Slicer 4.9 install and is likely not compatible with Slicer 4.10.1 stable. You should uninstall this extension and reinstall using the extensions manager.</p>

---

## Post #3 by @imuy5733 (2019-04-01 23:53 UTC)

<p>I installed the segment editor extra effect on a manual copy,because My Extention manager did not work.<br>
Is there any better way to do a manual installation?</p>

---

## Post #4 by @cpinter (2019-04-02 01:15 UTC)

<aside class="quote no-group" data-username="imuy5733" data-post="3" data-topic="6347">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/7c8e57/48.png" class="avatar"> imuy5733:</div>
<blockquote>
<p>My Extention manager did not work</p>
</blockquote>
</aside>
<p>Did you build your own Slicer? You can only use the extension manager for installed Slicer.<br>
If not, what version do you use?</p>

---

## Post #5 by @imuy5733 (2019-04-02 01:18 UTC)

<p>I built my Slicer and I use extension manager on my installed slicer.<br>
I think that it is the influence of the proxy environment. But I do not know how to set it.<br>
I can not move forward from 0%.</p>

---

## Post #6 by @cpinter (2019-04-02 13:39 UTC)

<aside class="quote no-group" data-username="imuy5733" data-post="5" data-topic="6347">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/7c8e57/48.png" class="avatar"> imuy5733:</div>
<blockquote>
<p>I built my Slicer and I use extension manager on my installed slicer</p>
</blockquote>
</aside>
<p>Okay so this is the issue, you cannot generally do it like this. The extensions in the extension manager were built against the factory Slicer build and in the same environment. Even if you have an apparently identical environment you still cannot expect those dlls to work perfectly.</p>
<p>If you build Slicer then you need to build your extensions too.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_build_an_extension_.3F" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_build_an_extension_.3F</a></p>

---
