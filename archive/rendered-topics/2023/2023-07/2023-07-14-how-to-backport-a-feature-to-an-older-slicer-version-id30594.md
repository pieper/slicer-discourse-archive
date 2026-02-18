# How to backport a feature to an older Slicer version

**Topic ID**: 30594
**Date**: 2023-07-14
**URL**: https://discourse.slicer.org/t/how-to-backport-a-feature-to-an-older-slicer-version/30594

---

## Post #1 by @jay1987 (2023-07-14 06:48 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d5001717ad1ff043ba7ccf24ee2ca15ac713e10.png" data-download-href="/uploads/short-url/1TLCl93UYOYQUfTiW3yvi5dXU3u.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d5001717ad1ff043ba7ccf24ee2ca15ac713e10_2_690x243.png" alt="image" data-base62-sha1="1TLCl93UYOYQUfTiW3yvi5dXU3u" width="690" height="243" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d5001717ad1ff043ba7ccf24ee2ca15ac713e10_2_690x243.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d5001717ad1ff043ba7ccf24ee2ca15ac713e10.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d5001717ad1ff043ba7ccf24ee2ca15ac713e10.png 2x" data-dominant-color="8B9394"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">753×266 35.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The requirement I received is to use a label to point to a specific spatial point in the 3D view. The latest Slicer version seems to have implemented this feature, but the client’s software was developed based on 5.1.2. I searched for the latest Slicer code on GitHub and couldn’t find this feature. Is there a plugin that implements this feature?</p>

---

## Post #2 by @muratmaga (2023-07-14 07:32 UTC)

<p>This is now available as an extension. Please install it from extension manager. Seach for <strong>ExtraMarkups</strong></p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/chir-set/SlicerExtraMarkups/">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/chir-set/SlicerExtraMarkups/" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/efb02c8aa1fdd72a0ed84f972d4425d0bcdf406c69649d46756c2bd880f46598/chir-set/SlicerExtraMarkups" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/chir-set/SlicerExtraMarkups/" target="_blank" rel="noopener">GitHub - chir-set/SlicerExtraMarkups: Custom markups for Slicer</a></h3>

  <p>Custom markups for Slicer. Contribute to chir-set/SlicerExtraMarkups development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jay1987 (2023-07-15 03:04 UTC)

<p>thank you very much <a class="mention" href="/u/muratmaga">@muratmaga</a></p>

---

## Post #4 by @jay1987 (2023-07-16 01:15 UTC)

<p>is there exist a old version of the extension ExtraMarkups? Slicer5.1.2 can’t compile the extension because the basic framework miss some file to comile the extension.</p>

---

## Post #5 by @lassoan (2023-07-16 12:20 UTC)

<p>Slicer core developers cannot justify spending time with supporting older Slicer versions, because it would take resources away from fixing and improving the current Slicer version.</p>
<p>You have several options:</p>
<ul>
<li>upgrade to a more recent Slicer version to benefit from latest fixes and improvements and get free support</li>
<li>invest your resources to figure out solutions, backport fixes and improvements to older Slicer releases</li>
<li>turn to Slicer commercial partners for getting help with older Slicer releases</li>
</ul>

---

## Post #6 by @jay1987 (2023-07-17 01:15 UTC)

<p>thank you lassoan .<br>
Your advice is always very useful.<br>
I’ll consult with the boss of the company to see his ideas.<br>
if I am looking for a business partner, where can I obtain it?</p>

---

## Post #7 by @lassoan (2023-07-25 11:28 UTC)

<p>You cs an find contact information of Slicer commercial partners <a href="https://www.slicer.org/commercial-use.html">here</a>.</p>

---

## Post #8 by @jay1987 (2023-07-25 11:30 UTC)

<p>the page is out of service noew<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27c8ba589a69b808b67498ac48e9ef8fdb1bd443.png" data-download-href="/uploads/short-url/5FWG5LQYYczYSU5NtzHMFLTJzOP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27c8ba589a69b808b67498ac48e9ef8fdb1bd443_2_690x300.png" alt="image" data-base62-sha1="5FWG5LQYYczYSU5NtzHMFLTJzOP" width="690" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27c8ba589a69b808b67498ac48e9ef8fdb1bd443_2_690x300.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27c8ba589a69b808b67498ac48e9ef8fdb1bd443_2_1035x450.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27c8ba589a69b808b67498ac48e9ef8fdb1bd443_2_1380x600.png 2x" data-dominant-color="D3D4D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1846×805 24.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2023-07-25 12:16 UTC)

<p>I’ve fixed link now, please check again.</p>

---

## Post #10 by @jay1987 (2023-07-25 12:19 UTC)

<p>thank you ! it’s worked now.</p>

---
