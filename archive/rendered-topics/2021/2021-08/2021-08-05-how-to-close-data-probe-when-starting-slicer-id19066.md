---
topic_id: 19066
title: "How To Close Data Probe When Starting Slicer"
date: 2021-08-05
url: https://discourse.slicer.org/t/19066
---

# How to close Data Probe when starting Slicer?

**Topic ID**: 19066
**Date**: 2021-08-05
**URL**: https://discourse.slicer.org/t/how-to-close-data-probe-when-starting-slicer/19066

---

## Post #1 by @slicer365 (2021-08-05 01:03 UTC)

<p>Dear experts,</p>
<p>I have a question , this option is always expanded every time I start Slicer.</p>
<p>In fact, I don’t use this option often, so I need to close it manually every time.</p>
<p>Is there a way to change the unexpanded state as the default.</p>
<p>Any scripts?</p>
<p>As is shown in this picture.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d173387364c3163e95da9d9120064231ef5ce65e.jpeg" alt="捕获" data-base62-sha1="tSSEj66qMPYA1tJVkT6c4UbAJJQ" width="674" height="339"></p>

---

## Post #2 by @jamesobutler (2021-08-05 02:06 UTC)

<p>You can use the method <code>setDataProbeVisible</code>. See here for more details</p>
<aside class="quote quote-modified" data-post="2" data-topic="10544">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/simple-way-to-disable-data-probe-for-some-modules/10544/2">Simple way to disable Data Probe for some modules</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    slicer.util has this function: 
 
 
which you can use with detecting when your module is entered/exited to hide the data probe.  This can be done by defining the enter() / exit() functions in your module.  See:
  </blockquote>
</aside>

<p>as part of the application startup script</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html?highlight=Slicerrc#application-startup-file" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/settings.html?highlight=Slicerrc#application-startup-file</a></p>

---
