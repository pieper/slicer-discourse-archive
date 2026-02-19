---
topic_id: 5692
title: "Elastix Extension For Mac Osx Not Available"
date: 2019-02-08
url: https://discourse.slicer.org/t/5692
---

# Elastix extension for Mac OSX not available

**Topic ID**: 5692
**Date**: 2019-02-08
**URL**: https://discourse.slicer.org/t/elastix-extension-for-mac-osx-not-available/5692

---

## Post #1 by @Mary (2019-02-08 14:51 UTC)

<p>I have been trying to install the Elastix extension for Slicer on my Mac, but it is not in the list of available extensions in ‘Extensions Manager’ on both the stable and nightly Slicer releases. On the web address: <a href="http://slicer.kitware.com/midas3/slicerappstore" rel="nofollow noopener">http://slicer.kitware.com/midas3/slicerappstore</a> it only appears to be available for Windows. Looking at only forum threads, it appears that it has been available for Mac in the past - is there a release version I can download that would support this extension?</p>

---

## Post #2 by @cpinter (2019-02-08 16:05 UTC)

<p>Unfortunately Elastix does not build on Mac for a while, see</p><aside class="quote" data-post="1" data-topic="4531">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicerelastix-extension-not-available-on-mac/4531">SlicerElastix extension not available on Mac</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi all, 
I wanted to show a Mac user the SlicerElastix extension but it was not there. After a bit of investigation, it turns out that it does not build at least since February. 
Here’s the <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=Elastix">latest dashboard</a> and the <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1411238">error</a> (and the <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-02-17&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=Elastix">oldest available dashboard</a>). 
Does anyone know what is needed in order to fix this? Can someone who usually develops on Mac check it out? Elastix is a great registration tool, we should have it in 4.10. 
Thanks, 
csaba
  </blockquote>
</aside>

<p><a class="mention" href="/u/jcfr">@jcfr</a> In our previous investigation we found that SlicerElastix builds OK, just the dashboard script identifies warnings as errors. Would it be possible to build it once manually on the factory Mac and at least push the package for the latest 4.10.1 stable?</p>

---

## Post #3 by @pieper (2019-02-09 20:05 UTC)

<p>Note: there is an issue for this on the elastix repo: <a href="https://github.com/SuperElastix/elastix/issues/110" rel="nofollow noopener">https://github.com/SuperElastix/elastix/issues/110</a></p>

---
