---
topic_id: 9416
title: "Namic Wiki Offline"
date: 2019-12-06
url: https://discourse.slicer.org/t/9416
---

# NAMIC Wiki offline

**Topic ID**: 9416
**Date**: 2019-12-06
**URL**: https://discourse.slicer.org/t/namic-wiki-offline/9416

---

## Post #1 by @Chris_Rorden (2019-12-06 16:18 UTC)

<p>Hello, in the past the NA-MIC wiki has been a terrific resource for users. Many of my own web pages include links to the wiki, like this one for GE-specific diffusion details:<br>
<a href="https://www.na-mic.org/wiki/NAMIC_Wiki:DTI:DICOM_for_DWI_and_DTI#Private_vendor:_GE" rel="nofollow noopener">NA-MIC Wiki</a></p>
<p>At the moment, all these pages seem to have vanished. If one searches for information on these vanished pages, you see they are still cached. For example, if you enter <code>0043</code> into the search you see <a href="https://www.na-mic.org/w/index.php?title=Special:Search&amp;search=0043&amp;go=Go&amp;searchToken=4c5wix92dsygeq3un40sv7zyv" rel="nofollow noopener">links to pages</a>, but when you click on the links you are told the pages are empty.</p>

---

## Post #2 by @lassoan (2019-12-06 16:36 UTC)

<p>Thanks for reporting this. Probably it is due to the recent migration of the wiki to a different server. <a class="mention" href="/u/freephile">@freephile</a> could you have a look?</p>

---

## Post #3 by @freephile (2019-12-06 18:09 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a>, Thanks for the example.  Could you give me a couple more examples of vanished pages?  I’m trying to work out the exact nature of the problem.  (The NAMIC_Wiki namespace exists, but the specific page you cited does not.)</p>

---

## Post #4 by @Tina_Kapur (2019-12-06 20:44 UTC)

<p>Here is another one that uses the DTI namespace and appears to have vanished:</p>
<p><a href="https://www.na-mic.org/wiki/NAMIC_Wiki:DTI:Nrrd_format" class="onebox" target="_blank" rel="nofollow noopener">https://www.na-mic.org/wiki/NAMIC_Wiki:DTI:Nrrd_format</a></p>

---

## Post #5 by @pieper (2019-12-06 21:18 UTC)

<p>That’s an important page - it’s probably widely linked.</p>
<p>Another note, when I used the search on the wiki for that keyword <code>Wiki:DTI:Nrrd format</code> I got back this link: <code>http://c2.com/cgi/wiki?DTI:Nrrd_format</code> which takes me to an error page with a link to a github repository that’s not obviously related.  <a class="mention" href="/u/freephile">@freephile</a> should I file a separate issue about the search bar? Most other search results seem to work fine.</p>

---

## Post #6 by @freephile (2019-12-06 21:30 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="9416">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><a href="http://c2.com/cgi/wiki?DTI:Nrrd_format" rel="noopener nofollow ugc">http://c2.com/cgi/wiki?DTI:Nrrd_format</a></p>
</blockquote>
</aside>
<p>C2 is the original wiki by Ward Cunningham – unrelated to the na-mic wiki itself.  Did you use Google search rather than on-wiki search?  Or are you saying that the na-mic wiki gave you that result? I don’t see it <a href="https://www.na-mic.org/w/index.php?search=Wiki%3ADTI%3ANrrd+format&amp;title=Special%3ASearch&amp;profile=default&amp;fulltext=1" rel="noopener nofollow ugc">in these search results</a>.</p>
<p>In any case, if you want to open an issue I’d be glad to dig into it. Please use the eQuality Technology discourse for Surgical Planning Lab at <a href="https://discourse.equality-tech.com/c/clients/spl" rel="noopener nofollow ugc">https://discourse.equality-tech.com/c/clients/spl</a>  Thanks ~ Greg</p>

---

## Post #7 by @freephile (2019-12-06 22:02 UTC)

<p>I’ve found several examples.  I’m looking into it. Will probably update tomorrow with a fix, but will need to debug in the development environment to understand what’s going on with these titles.</p>

---

## Post #8 by @pieper (2019-12-06 22:16 UTC)

<p>Thanks <a class="mention" href="/u/freephile">@freephile</a>, I filed a report on the <a href="http://equality-tech.com">equality-tech.com</a> site.  Yes, I mean that when I enter that search term into the wiki’s search entry box on the left it take me to this page:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/4614b317a4435919a1a044c96653a2af07ecf9a8.png" data-download-href="/uploads/short-url/9ZXLPW9GHX1JfpYd0bYUgamAkhW.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4614b317a4435919a1a044c96653a2af07ecf9a8_2_690x349.png" alt="image" data-base62-sha1="9ZXLPW9GHX1JfpYd0bYUgamAkhW" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4614b317a4435919a1a044c96653a2af07ecf9a8_2_690x349.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4614b317a4435919a1a044c96653a2af07ecf9a8_2_1035x523.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/4614b317a4435919a1a044c96653a2af07ecf9a8.png 2x" data-dominant-color="F5F6F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1370×694 81.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Following the link takes me here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd676e6b3dae10be009f3ed0bdb4114152c417b5.png" data-download-href="/uploads/short-url/r1xQeAlNI8hL7QYqn2UtDlRGcZv.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd676e6b3dae10be009f3ed0bdb4114152c417b5_2_690x259.png" alt="image" data-base62-sha1="r1xQeAlNI8hL7QYqn2UtDlRGcZv" width="690" height="259" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd676e6b3dae10be009f3ed0bdb4114152c417b5_2_690x259.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd676e6b3dae10be009f3ed0bdb4114152c417b5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd676e6b3dae10be009f3ed0bdb4114152c417b5.png 2x" data-dominant-color="F2F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">711×267 19.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>which takes me to this github page: <a href="https://github.com/WardCunningham/remodeling/issues/2" class="inline-onebox">full service static site · Issue #2 · WardCunningham/remodeling · GitHub</a></p>

---

## Post #9 by @freephile (2019-12-09 17:01 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a>, <a class="mention" href="/u/tina_kapur">@Tina_Kapur</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a>    The issue with ‘vanishing content’ on NA-MIC wiki is solved.  See <a href="https://www.na-mic.org/wiki/Special:PrefixIndex?prefix=&amp;namespace=4" rel="nofollow noopener">https://www.na-mic.org/wiki/Special:PrefixIndex?prefix=&amp;namespace=4</a> for a list of content that was affected. These pages are all now functional as before.</p>
<p>If you notice any other problems, please feel free to report them at <a href="https://discourse.equality-tech.com" rel="nofollow noopener">https://discourse.equality-tech.com</a></p>

---

## Post #10 by @pieper (2019-12-09 17:44 UTC)

<p>Thank you <a class="mention" href="/u/freephile">@freephile</a> !</p>

---

## Post #11 by @Chris_Rorden (2019-12-09 19:13 UTC)

<ol>
<li>The pages are back, and old links work again. Thanks!</li>
<li>Does the search system need to be refreshed? If I now type “0043” into the search box at the right, I get no hits, while it should have found <a href="https://www.na-mic.org/wiki/NAMIC_Wiki:DTI:DICOM_for_DWI_and_DTI" rel="nofollow noopener">this page</a>.</li>
</ol>

---
