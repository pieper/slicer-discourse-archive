# FOV of live ultrasound image

**Topic ID**: 29294
**Date**: 2023-05-04
**URL**: https://discourse.slicer.org/t/fov-of-live-ultrasound-image/29294

---

## Post #1 by @Albags (2023-05-04 14:28 UTC)

<p>Hi,</p>
<p>Through the PLUS toolkit I connect an US scanner with 3D slicer. The image I receive includes the US image plus all text and graphics included on the screen of the scanner, however I would like to display only the ultrasound image. Is there any way to specify the FOV of the live US image that I want to visualize?</p>
<p>Thank you in advance!</p>

---

## Post #2 by @Sunderlandkyl (2023-05-04 14:36 UTC)

<p>You might want to check out the <strong>ClipRectangleOrigin</strong> and <strong>ClipRectangleSize</strong> attributes in Plus:<br>
<a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Configuration.html#ClipRectangleOrigin" class="onebox" target="_blank" rel="noopener nofollow ugc">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Configuration.html#ClipRectangleOrigin</a></p>

---

## Post #3 by @Albags (2023-05-09 10:22 UTC)

<aside class="quote no-group quote-modified" data-username="Sunderlandkyl" data-post="2" data-topic="29294">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p><a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Configuration.html#ClipRectangleOrigin" class="inline-onebox" rel="noopener nofollow ugc">Plus applications user manual: Device set configuration</a></p>
</blockquote>
</aside>
<p>Thanks! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=14" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"> I tried before with <strong>ClipRectangleOriginClipping</strong> and <strong>ClipRectangleSizeClipping</strong> and it didn’t work, but it does work when I use  <strong>ClipRectangleOrigin</strong> and <strong>ClipRectangleSize</strong> instead.</p>

---

## Post #4 by @Sunderlandkyl (2023-05-10 14:28 UTC)

<p>Yeah, there was a issue on the page that appended <strong>Clipping</strong> on the back of <strong>ClipRectangleOrigin</strong>. It should be fixed now.</p>

---
