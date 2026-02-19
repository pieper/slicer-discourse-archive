---
topic_id: 29939
title: "Question Extension Wizard With Cmakelist Txt"
date: 2023-06-09
url: https://discourse.slicer.org/t/29939
---

# Question : extension wizard with CmakeList.txt

**Topic ID**: 29939
**Date**: 2023-06-09
**URL**: https://discourse.slicer.org/t/question-extension-wizard-with-cmakelist-txt/29939

---

## Post #1 by @dsa934 (2023-06-09 10:46 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/7498ed11f885ddcddbf243b84d636998a50d5812.png" data-download-href="/uploads/short-url/gDt1NZEibWSPV7IuOUjIIfu6T1E.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/7498ed11f885ddcddbf243b84d636998a50d5812_2_690x268.png" alt="image" data-base62-sha1="gDt1NZEibWSPV7IuOUjIIfu6T1E" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/7498ed11f885ddcddbf243b84d636998a50d5812_2_690x268.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/7498ed11f885ddcddbf243b84d636998a50d5812_2_1035x402.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/7498ed11f885ddcddbf243b84d636998a50d5812_2_1380x536.png 2x" data-dominant-color="252525"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1718×669 51.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Q1. Why is the cmake file always divided into two when I create a module through the extension wizard? Is there any reason not to do it with one?</p>
<p>Q2.Does anyone know about the CUSTOMSLICER build error?</p><aside class="quote quote-modified" data-post="1" data-topic="29910">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/build-error-customslicers-purpose/29910">Build Error &amp; CustomSlicer's Purpose</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Operating system: window 10 
Slicer version: 5.2.1 
Hi all, 
[image] 
Q1. When the Cmake → build process was performed for each of three slicer5.2.1, slicer5.2.2, and CustomSlicer, the same permission error for the vtk folder occurred. What to do in this case? 
Q2. I’ve heard that CustomSlicer allows you to customize many things without changing the slicer’s core, but is the ‘many’ mentioned here only about the GUI?
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="19" data-topic="29821">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/about-creating-customslicer/29821/19">About creating Customslicer</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Please confirm if I am misunderstanding the slicer. 
New function: Can be implemented by adding a module through ‘extension wizard’ 
Modification of existing functions: There is a way to customize without modifying the sclier core. 
So why does CustomSlicer (SlicerCAT) exist? 
Is the purpose of using it to customize the logo, GUI environment, etc. to suit my purpose without simply changing the slicer core? 
For example, there are two ways to save work in slicer as far as I know. 

Click the Save…
  </blockquote>
</aside>


---

## Post #2 by @jamesobutler (2023-06-09 11:33 UTC)

<aside class="quote no-group" data-username="dsa934" data-post="1" data-topic="29939">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>Q1. Why is the cmake file always divided into two when I create a module through the extension wizard? Is there any reason not to do it with one?</p>
</blockquote>
</aside>
<p>The top level one is used for instructing how to build the Slicer Extension. The one inside the directory “VisualInspection” is used for instructing how to build the individual Slicer module. A Slicer extension can have multiple Slicer modules. Through the Extension Wizard you can see what it is like when you add multiple modules to your extension. You can also take a look at other Slicer extensions as examples.</p>
<p>Here is SlicerOpenIGTLink which has a mix of scripted loadable modules (python) and regular loadable modules (c++).</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/openigtlink/SlicerOpenIGTLink">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/openigtlink/SlicerOpenIGTLink" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/38f0f3391c586ff99333ef599e0e7f29154dc6cc0deeb453f804941fa02ee50b/openigtlink/SlicerOpenIGTLink" class="thumbnail" width="" height=""></div>

<h3><a href="https://github.com/openigtlink/SlicerOpenIGTLink" target="_blank" rel="noopener nofollow ugc">GitHub - openigtlink/SlicerOpenIGTLink: OpenIGTLinkIF module as an Slicer...</a></h3>

  <p>OpenIGTLinkIF module as an Slicer Extension. Contribute to openigtlink/SlicerOpenIGTLink development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
