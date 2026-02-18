# Trame-Slicer and SlicerLib wheel

**Topic ID**: 41388
**Date**: 2025-01-31
**URL**: https://discourse.slicer.org/t/trame-slicer-and-slicerlib-wheel/41388

---

## Post #1 by @park (2025-01-31 00:18 UTC)

<p>Hi all,</p>
<p>As seen in the LinkedIn and Project Week slider, Trame-Slicer and SlicerLib wheel appear to be remarkable advancements!!</p>
<p>Our team is very eager to test this as soon as possible, ideally within a day. We noticed that the Trame-Slicer repository was uploaded on GitHub today, but we have not yet been able to locate the vtk_mrml wheel.</p>
<ul>
<li>Would you be able to advise on how we might quickly test this?</li>
<li>Additionally, could you share any information regarding the official release schedule for the Slicer wheel and Trame-Slicer?</li>
</ul>
<p>We truly appreciate your guidance and support.<br>
Thank you!</p>

---

## Post #2 by @Thibault_Pelletier (2025-01-31 15:16 UTC)

<p>Hi <a class="mention" href="/u/park">@park</a>,</p>
<p>Thank you for your enthusiasm in trying out trame-slicer!<br>
Demo wheels are available in the release tag and can be manually downloaded here for Windows and Linux WSL : <a href="https://github.com/KitwareMedical/trame-slicer/releases/tag/v0.0.1" class="inline-onebox" rel="noopener nofollow ugc">Release v0.0.1 · KitwareMedical/trame-slicer · GitHub</a></p>
<p>trame-slicer is not production ready and we are waiting for the infrastructure work of the library to be properly merged into 3D Slicer’s main branche and its sister project the <a href="https://github.com/KitwareMedical/slicertrame" rel="noopener nofollow ugc">SlicerTrame 3D Slicer extension</a> to be into the extension index before we consider the two libraries ready for external use.</p>
<p>This should happen in the first half of the year. We will be posting announcements along the way to inform the 3D Slicer community when the different building blocks are ready.</p>
<p>We also plan on communicating around how to use the libraries and how to adapt existing 3D Slicer code to make it compatible with the new framework.</p>
<p>Best,<br>
Thibault</p>

---

## Post #3 by @ruffsl (2025-10-16 21:34 UTC)

<aside class="quote no-group" data-username="Thibault_Pelletier" data-post="2" data-topic="41388">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/thibault_pelletier/48/4767_2.png" class="avatar"> Thibault_Pelletier:</div>
<blockquote>
<p>This should happen in the first half of the year. We will be posting announcements along the way to inform the 3D Slicer community when the different building blocks are ready.</p>
</blockquote>
</aside>
<p>Any more recent new? A quick discourse search returned this as the most recent thread. Just tested the medical viewer app example via SlicerTrame using SLicer 3D v5.9 nightly, and was impressed:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/KitwareMedical/SlicerTrame">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerTrame" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/f1bec8c35abed8e930ef27f7c0d0625a/KitwareMedical/SlicerTrame" class="thumbnail">

  <h3><a href="https://github.com/KitwareMedical/SlicerTrame" target="_blank" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerTrame: 3D Slicer extension to launch trame-slicer server...</a></h3>

    <p><span class="github-repo-description">3D Slicer extension to launch trame-slicer server directly from 3D Slicer</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Appreciate all the efforts.</p>

---

## Post #4 by @Thibault_Pelletier (2025-10-17 05:17 UTC)

<p>Hi <a class="mention" href="/u/ruffsl">@ruffsl</a>,</p>
<p>Thanks for your interest!<br>
As you’ve seen, trame-slicer can now be launched using the SlicerTrame extension with the Slicer nightly release.</p>
<p>We are moving along with the library and we will communicate soon on the current status in the coming weeks.</p>
<p>Along with the communication, we will be polishing the current example and add in more examples and documentation for people to get started with using the library.</p>
<p>Best,<br>
Thibault</p>

---
