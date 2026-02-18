# Medical record integration

**Topic ID**: 14084
**Date**: 2020-10-16
**URL**: https://discourse.slicer.org/t/medical-record-integration/14084

---

## Post #1 by @Amn3s14 (2020-10-16 17:26 UTC)

<p>Hello,</p>
<p>I have written a number of tools using Slicer that aid in surgical planning and have packaged them as their own applications and focused on ease-of-use etc. in order to increase accessibility to clinicians without a technical background. Still, expecting them to be able to download DICOMs and the software may be asking too much. I was wondering if there have been any efforts to integrate some 3D Slicer functionality into an Electronic Medical Record or PACS. Right now the steps are:</p>
<p>Download DICOM from PACS (requires the export feature to be activated by tech support at my institution)<br>
Download software from website<br>
Run software<br>
Select DICOM in software<br>
Run analysis</p>
<p>If there’s any way to cut down the number of steps I’d greatly appreciate any advice. Any kind of web-based software with PACS integration or something along those lines would be perfect. Could anyone recommend similar projects or where to start looking? Thanks.</p>

---

## Post #2 by @pieper (2020-10-16 19:21 UTC)

<p>There are hooks in various commercial systems that let you call out to external services.  They need to include instructions how to access the data and also account for whatever security issues there may be.   Unfortunately such hooks are limited and the functionality varies widely across vendors.</p>
<p>Here’s an example where we integrated Slicer with Siemens teamplay system:</p><div class="youtube-onebox lazy-video-container" data-video-id="vTGQMDIqL9k" data-video-title="teamplay+Slicer 2017 02 10" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=vTGQMDIqL9k" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/vTGQMDIqL9k/maxresdefault.jpg" title="teamplay+Slicer 2017 02 10" width="" height="">
  </a>
</div>


---

## Post #3 by @chir.set (2020-10-17 17:37 UTC)

<aside class="quote no-group" data-username="Amn3s14" data-post="1" data-topic="14084">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/7feea3/48.png" class="avatar"> Amn3s14:</div>
<blockquote>
<p>I have written a number of tools</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="Amn3s14" data-post="1" data-topic="14084">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/7feea3/48.png" class="avatar"> Amn3s14:</div>
<blockquote>
<p>expecting them to be able</p>
</blockquote>
</aside>
<p>While I am not answering your question, as a clinician, I wish to comment on your intention.</p>
<p>You will have a hard time because clinicians are not willing to invest time and do elementary research work so as to master common GUI software. They keep demanding for a UI and processes that they expect, every one according to their own ideas. They don’t accept the software as it is, and don’t resolve to exploring all its functionalities to their advantage. They do have the potential so to do, but the will is missing. And the demands never tarry. Be it Slicer or a word processor, each one already hiding complexities behind a nice GUI.</p>
<p>Probably, it’s a vicious attitude originating from the  way Windows or Mac considers users. These OS have a very wide audience and we may understand many must be spoon fed. Doctors should be able to transcend that, but they don’t.</p>
<p>Younger, I used to help colleagues a lot. Older, I abandoned.</p>
<p>These few lines are intended to give you some insight in your endeavour.</p>
<aside class="quote no-group" data-username="Amn3s14" data-post="1" data-topic="14084">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/7feea3/48.png" class="avatar"> Amn3s14:</div>
<blockquote>
<p>that aid in surgical planning</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="Amn3s14" data-post="1" data-topic="14084">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/7feea3/48.png" class="avatar"> Amn3s14:</div>
<blockquote>
<p>expecting them to be able</p>
</blockquote>
</aside>
<p>Good luck with that.</p>

---
