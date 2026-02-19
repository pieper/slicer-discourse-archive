---
topic_id: 28394
title: "There Are No Extensions In The Extension Manager 5 3 0 Build"
date: 2023-03-15
url: https://discourse.slicer.org/t/28394
---

# There are no extensions in the extension manager-5.3.0 build

**Topic ID**: 28394
**Date**: 2023-03-15
**URL**: https://discourse.slicer.org/t/there-are-no-extensions-in-the-extension-manager-5-3-0-build/28394

---

## Post #1 by @MikhayEeer (2023-03-15 08:43 UTC)

<p>Hi, I built slicer from source, but I can’t find the extension in the extension manager, nor can I install it from the file. I click to open the webpage, and the expanded webpage doesn’t have any extensions either.<br>
In the past two days, I tried to build the source code of the 5.2 and 5.3 versions, and also tried the release and debug modes. Only once in the 5.3 debug mode can I see the extension in the extension manager.<br>
I confirm that it is not a network problem, what should I do so that my slicer can download and use the extension normally. I will be very grateful for your help!</p>

---

## Post #2 by @MikhayEeer (2023-03-15 08:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/932051fdc98cdade026c47617cb11d91a2933a4d.png" data-download-href="/uploads/short-url/kZxqUqpWEJsnDfZwXYDCEOInkdf.png?dl=1" title="Snipaste_2023-03-15_16-43-30" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/932051fdc98cdade026c47617cb11d91a2933a4d.png" alt="Snipaste_2023-03-15_16-43-30" data-base62-sha1="kZxqUqpWEJsnDfZwXYDCEOInkdf" width="690" height="344" data-dominant-color="FBFBFB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snipaste_2023-03-15_16-43-30</span><span class="informations">935×467 7.25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is what the interface looks like, and the extension has been unable to load. In the <code>build</code> directory, I found that the number of <code>ini </code>format files in the <code>Slicer-build\NA-MIC</code> directory is incorrect, and the<code>json</code>file in the<code>extension</code>folder is empty. Really don’t know how to proceed. Hope to get your help.</p>

---

## Post #3 by @jamesobutler (2023-03-15 12:20 UTC)

<p>Factory built extensions are only available for specific revision numbers corresponding to the commit used for the nightly build of extensions each night. However since you have built Slicer from source you cannot expect factory built extensions to appropriately work due to ABI compatibility issues. Therefore you should build the extensions you need from source as well. As a reminder you don’t generally need to build Slicer or extensions from source if they are Slicer scripted loadable modules which are written in python.</p>
<aside class="quote quote-modified" data-post="2" data-topic="8412">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/extensions-are-not-working-when-building-slicer-from-scratch/8412/2">Extensions are not working when building Slicer from scratch</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    You cannot use factory-built extensions with your locally built Slicer. In that case you’ll need to clone and build the extensions you want to use. 
See also for example 

or
  </blockquote>
</aside>

<p>How to build extensions from source:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-an-extension" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-an-extension</a></p>

---

## Post #4 by @MikhayEeer (2023-03-16 07:48 UTC)

<p>Thanks for your reply, after building the extension locally I was able to use it, thanks a lot!</p>

---
