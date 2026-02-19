---
topic_id: 5697
title: "Rawimageguess Module"
date: 2019-02-08
url: https://discourse.slicer.org/t/5697
---

# RawImageGuess module

**Topic ID**: 5697
**Date**: 2019-02-08
**URL**: https://discourse.slicer.org/t/rawimageguess-module/5697

---

## Post #1 by @muratmaga (2019-02-08 17:15 UTC)

<p>This project is potentially useful for our user base to facilitate raw image import from microCT scanners without having to create nhdr header to define them. I have tried with a sample data that I have in <a href="https://blogs.uw.edu/maga/2018/09/importing-microct-data-from-scanco-into-slicer/" rel="nofollow noopener">https://blogs.uw.edu/maga/2018/09/importing-microct-data-from-scanco-into-slicer/</a></p>
<p>But encountered some issues. Specifically, I can’t seem to enter a header size bigger than 2500, I can’t type specific values in the image dimension boxes.</p>
<p>Can one of the developers tell me who we can contribute?</p>

---

## Post #2 by @pieper (2019-02-08 17:38 UTC)

<p><a class="mention" href="/u/nagy.attila">@nagy.attila</a> this one’s for you!</p>

---

## Post #3 by @nagy.attila (2019-02-12 11:15 UTC)

<p>Hi all,</p>
<p>sorry for getting a little bit late here <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Actually there are no restrictions in the code, at least none that I explicitly put there. I checked, and really, no data can be entered that is beyond 2500 header and 5000x2500 (X x Y dimensions) - even worse, if I move the slider for Z up to 1567, then Slicer catches an exception, saying Bad Allocation.</p>
<p>Generic Warning: In D:\D\S\Slicer-4101-build\VTK\IO\Image\vtkImageReader2.cxx, line 757<br>
File operation failed. row = 0, Read = 5000, FilePos = -1</p>
<p>Unable to allocate 19550000000 elements of size 1 bytes.</p>
<p>“Slicer has caught an internal error.\n\nYou may be able to continue from this point, but results are undefined.\n\nSuggested action is to save your work and restart.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="nofollow noopener">http://slicer.org</a>\n\n\nThe message detail is:\n\nException thrown in event: bad allocation”</p>
<p>19550000000 indeed equals 5000 x 2500 x 1564.</p>
<p>This equals around 18GB of data if we take an 8bit pixel color depth, if I calculated correctly.</p>
<p>This part is beyond me, so we still might need someone else to chime in!</p>
<p>As for the header, I will look into this. Also downloading your data right now.</p>

---

## Post #4 by @nagy.attila (2019-02-12 12:58 UTC)

<p>Okay, too long time passed to edit my previous post</p>
<p>So there were restrictions and they were arbitrary. But not in the code but in the UI file…<br>
I edited it and checked in the changes into master.<br>
Also checked in a slightly newer version of the python file.</p>

---

## Post #5 by @pieper (2019-02-12 13:17 UTC)

<p>Thanks <a class="mention" href="/u/nagy.attila">@nagy.attila</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=6" title=":+1:" class="emoji" alt=":+1:"></p>
<p>The memory allocation error is not unexpected.  The machines are finite, so we may as well let people push up to the limits.</p>

---

## Post #6 by @muratmaga (2019-02-12 17:26 UTC)

<p>Thanks <a class="mention" href="/u/nagy.attila">@nagy.attila</a>. I will give a try.<br>
As for the limits, I think it might be useful to precalculate the datasize as you did above, and give a warning about its consequences.</p>
<p>I think in general, we need a consistent way of resampling the stack without needing to load the entire stack into the Slicer. This will come in handy for datasets from high-resolution mCT as well as microscopy to load into computer with limited resources. <a class="mention" href="/u/smrolfe">@smrolfe</a> started one sometime ago, so there might be  some synergy there…</p>

---

## Post #7 by @muratmaga (2019-12-19 15:56 UTC)

<p>For posterity. RawImageGuess is now an official extension. See</p><aside class="quote quote-modified" data-post="1" data-topic="9219">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-extension-rawimageguess-for-loading-of-images-from-unrecognized-file-format/9219">New extension: RawImageGuess - for loading of images from unrecognized file format</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    There are proprietary image file formats the 3D Slicer does not recognize and so refuses to load. <a class="mention" href="/u/nagy.attila">@nagy.attila</a> in collaboration with Slicer core developers created an extension that can be used to load data from files that use an unknown format. 
<a href="https://github.com/acetylsalicyl/SlicerRawImageGuess">RawImageGuess extension</a> offers a number of parameters (image header size, dimensions, pixel type, etc.) that users can adjust and see the resulting image in real-time. This makes it possible to guess the image format in a couple of minutes. 
See a demo …
  </blockquote>
</aside>


---
