# Portable installation of Slicer with extension on USB

**Topic ID**: 8582
**Date**: 2019-09-26
**URL**: https://discourse.slicer.org/t/portable-installation-of-slicer-with-extension-on-usb/8582

---

## Post #1 by @muratmaga (2019-09-26 19:08 UTC)

<p>I need a Slicer installation on a USB stick with SlicerMorph and other extensions installed for portability reasons. While I can install Slicer on the USB stick and the extensions to a folder within the USB stick,  those paths seems hard coded. If I try to run Slicer on a different computer off the USB stick with a different drive letter, extensions doesn’t  run.</p>
<p>The reason I want this is because we got couple of computers that are offline, I am just looking for an easy way to update them with new nightlies and their associated extension without having to download installers and the extensions. (This is on windows)</p>

---

## Post #2 by @pieper (2019-09-27 14:24 UTC)

<p>Hi Murat -</p>
<p>It sounds like you want something like the CustomSlicerGenerator.  I haven’t used it myself in a while, but it should be possible to make it work with current Slicer.  Basically Slicer itself is very relocatable but there are a few details about the way extension modules are managed that motivated the creation of this generator script.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Labs/CustomSlicerGenerator" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Labs/CustomSlicerGenerator</a></p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/pieper/CustomSlicerGenerator" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/126077?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/pieper/CustomSlicerGenerator" target="_blank" rel="nofollow noopener">pieper/CustomSlicerGenerator</a></h3>

<p>Tool to help deploy custom applications. Contribute to pieper/CustomSlicerGenerator development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @muratmaga (2019-09-28 02:40 UTC)

<p>No, I don’t think this is what I am looking for. I am looking for something along the lines of this thread, but for windows. <a href="https://discourse.slicer.org/t/installing-extensions-in-binary-distribution-of-slicer/7511/14" class="inline-onebox">Installing extensions in binary distribution of Slicer</a></p>
<p>Would copying the extensions to lib\Slicer-4.11 folder work in windows too? I guess I can try and see…</p>

---

## Post #4 by @pieper (2019-09-28 11:45 UTC)

<p>That’s part of what the generator does - the point is that if you can reconfigure the modules as needed to make something custom without needing to compile the application from scratch.</p>

---

## Post #5 by @lassoan (2019-09-28 12:21 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="8582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Would copying the extensions to lib\Slicer-4.11 folder work in windows too?</p>
</blockquote>
</aside>
<p>Yes, this works on all platforms.</p>

---

## Post #6 by @muratmaga (2019-09-30 17:59 UTC)

<p>I tried this but didn’t work:</p>
<ul>
<li>I installed SlicerMorph and all other dependent applications on a regular windows computer in the usual way.</li>
<li>Then I copied the Slicer installation folder (AppData/Local/Na-mic/Slicer 4.11.0-2019-09-25) to a usb drive (as D:/Slicer 4.11.0-2019-09-25)</li>
<li>then I copied everything in the AppData\Roaming\NA-MIC\Extensions-28523) to D:/Slicer 4.11.0-2019-09-25/lib/Slicer-4.11.</li>
<li>When I took the usb drive to the offline computer and started the Slicer, no extensions were found.</li>
</ul>
<p>Am I missing a step?</p>

---

## Post #7 by @lassoan (2019-10-02 01:38 UTC)

<p>I’ve just tried and it works perfectly for me. Extensions will not be listed, but all the modules should be available. Since these modules are now bundled with core modules, SlicerMorph category will be among other core modules (near the bottom of the category list).</p>

---

## Post #8 by @muratmaga (2019-10-02 03:48 UTC)

<p>himm weird, module search doesn’t find any of the extensions installed (e.g., extraeffects doesn’t show within the segment editor). I will try from the scratch one more time.</p>

---

## Post #9 by @lassoan (2021-01-08 19:16 UTC)

<p>3D Slicer is now fully portable! See announcement with more details here: <a href="https://discourse.slicer.org/t/slicer-is-now-fully-portable/15410" class="inline-onebox">Slicer is now fully portable</a></p>

---
