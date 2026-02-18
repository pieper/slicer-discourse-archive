# Cannot download extension file

**Topic ID**: 32797
**Date**: 2023-11-14
**URL**: https://discourse.slicer.org/t/cannot-download-extension-file/32797

---

## Post #1 by @park (2023-11-14 02:02 UTC)

<p>Hi all,</p>
<p>I am currently unable to download extension files from the Slicer server these days, although it worked well before.</p>
<p>The error message is:<br>
“Failed downloading: <a href="https://slicer-packages.kitware.com/api/v1/file" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/file</a>”<br>
The issue persists with any extension module.</p>
<p>The strange thing is that it works well in version 4.x, but there is a problem in version 5.x.</p>
<p>I have tried removing Slicer and reinstalling it, but the problem persists.</p>
<p>Could you please tell me the reason and provide a solution?</p>

---

## Post #2 by @pieper (2023-11-14 16:11 UTC)

<aside class="quote no-group" data-username="park" data-post="1" data-topic="32797">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/park/48/5717_2.png" class="avatar"> park:</div>
<blockquote>
<p>problem in version 5.x.</p>
</blockquote>
</aside>
<p>Is this true for any version of 5.x?  E.g. did you try the 5.4.0 release from <a href="http://download.slicer.org">download.slicer.org</a>?  Extensions from preview versions are not kept forever.  Also what OS are you using?</p>
<p>You might also have a network proxy so maybe you can try on a different network?</p>
<p>Let us know how this goes for you.</p>

---

## Post #3 by @park (2023-11-15 00:50 UTC)

<p>I tested this on versions 5.0, 5.2, and 5.4, and the results were all the same.</p>
<p>My operating system is Windows. I also attempted the same process on a different computer (Windows) within the same network, and the results were consistent.</p>
<p>But it works on same network different computer in MAC OS.</p>
<p>Do you think is this proxy problem?</p>
<p>Morever, downloding files in here <a href="https://extensions.slicer.org/catalog/All/30893/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a><br>
works well.</p>
<p>Thank you</p>

---

## Post #4 by @pieper (2023-11-15 15:43 UTC)

<p>Yes, we discussed this a bit on the developer call yesterday and the consensus was that there is an probably and incompatibility with some proxy being used on your network.  Unfortunately it’s not clear what if anything we could do as a general solution for this.  If you have a chance to research this with your local network experts and suggest workarounds that would be appeciated.</p>

---
