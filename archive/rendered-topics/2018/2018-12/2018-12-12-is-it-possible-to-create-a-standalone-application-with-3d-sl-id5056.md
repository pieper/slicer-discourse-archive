# Is it possible to create a standalone application with 3D slicer and run it without 3D Slicer launching?

**Topic ID**: 5056
**Date**: 2018-12-12
**URL**: https://discourse.slicer.org/t/is-it-possible-to-create-a-standalone-application-with-3d-slicer-and-run-it-without-3d-slicer-launching/5056

---

## Post #1 by @wpgao (2018-12-12 14:51 UTC)

<p>Operating system: win 10<br>
Slicer version: 4.8<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi Guys,</p>
<p>Is it possible to create a standalone application with 3D slicer and run it without 3D Slicer launching? I mean the application can works in other computers without 3D Slicer.<br>
Thanks a lot!</p>

---

## Post #2 by @cpinter (2018-12-12 15:00 UTC)

<p>These standalone applications based on Slicer are called Slicelets. Here’s a wiki page about how to create them:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets</a><br>
This page is a bit outdated so could use an update, but you can start with that.</p>
<p>The main new piece are the custom applications:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/KitwareMedical/SlicerCustomAppTemplate">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/4ca0a13bdcd7815768073521e808ea6a1cc4a0643f94bdf0cdc79e2b9bf4367e/KitwareMedical/SlicerCustomAppTemplate" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" target="_blank" rel="noopener">GitHub - KitwareMedical/SlicerCustomAppTemplate: Template to be used as a...</a></h3>

  <p>Template to be used as a starting point for creating a custom 3D Slicer application - GitHub - KitwareMedical/SlicerCustomAppTemplate: Template to be used as a starting point for creating a custom ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2018-12-12 20:38 UTC)

<p>You can also run Slicer Python scripts in a web browser, without installing anything on the user’s computer, using <em>Binder</em>. See more information on <a href="https://github.com/Slicer/SlicerJupyter/" rel="nofollow noopener">SlicerJupyter extension documentation</a>.</p>

---

## Post #4 by @wpgao (2018-12-13 02:28 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a>,</p>
<p>Slicerlets is an option. However, it just prevents showing the main application UI interface and still depends on 3D Slicer? Is that right? If so, a customized  Slicerlets can not run on a computer without 3D Slicer. Is that right?</p>
<p>Alternatively, SlicerCustomAppTemplate seems to be more flexible, however, I can get too much information about how to use it! Does it can package the prerequisite modules of 3D slicer into the new application?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>,<br>
These two options are dependent on the internet. If the internet is not available, it will not work!</p>
<p>Many thanks for your important information!</p>

---

## Post #5 by @jcfr (2018-12-13 02:48 UTC)

<aside class="quote no-group" data-username="wpgao" data-post="4" data-topic="5056">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/8e8cbc/48.png" class="avatar"> wpgao:</div>
<blockquote>
<p>Does it can package the prerequisite modules of 3D slicer into the new application?</p>
</blockquote>
</aside>
<p>Yes, it takes care of packaging your custom module along with all dependencies (VTK, Qt, Slicer libraries, etc …)</p>

---

## Post #6 by @wpgao (2018-12-13 04:13 UTC)

<p>Great! Does it work now? or is under development?<br>
There is another module called “CustomSlicerGenerator” （<a href="http://www.slicer.org/slicerWiki/index.php/Documentation/Labs/CustomSlicerGenerator%EF%BC%89" rel="nofollow noopener">http://www.slicer.org/slicerWiki/index.php/Documentation/Labs/CustomSlicerGenerator）</a>?<br>
I had tried it in windows but failed! It seems that it just supports linux and mac!</p>
<p>Thanks!</p>

---

## Post #7 by @jcfr (2018-12-13 04:50 UTC)

<h3><a name="p-18843-slicercustomapptemplate-1" class="anchor" href="#p-18843-slicercustomapptemplate-1" aria-label="Heading link"></a>SlicerCustomAppTemplate</h3>
<aside class="quote no-group" data-username="wpgao" data-post="6" data-topic="5056">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/8e8cbc/48.png" class="avatar"> wpgao:</div>
<blockquote>
<p>Does it work now?</p>
</blockquote>
</aside>
<p>Yes, we use it to create custom application. To illustrate, here are few examples I can disclose:</p>
<ul>
<li><a href="https://blog.kitware.com/kitware-customer-highlight-muriplan-from-xstrahl-a-3d-slicer-based-radiotherapy-treatment-planning-system/">MuriPlan from Xstrahl – A 3D Slicer based radiotherapy treatment planning system</a></li>
<li><a href="https://blog.kitware.com/kitware-customer-highlight-radiopharmaceutical-imaging-and-dosimetry-llc-rapid/">Kitware customer highlight: Radiopharmaceutical Imaging and Dosimetry, LLC (RAPID)</a></li>
<li><a href="https://blog.kitware.com/kitware-customer-highlight-sonovol/">Kitware customer highlight: SonoVol</a></li>
<li><a href="https://blog.kitware.com/xoran-technologies-and-kitware-collaborate-on-image-guided-platform-for-deep-brain-stimulation-surgery/">Xoran Technologies and Kitware Collaborate on Image-guided Platform for Deep Brain Stimulation Surgery</a></li>
</ul>
<aside class="quote no-group quote-modified" data-username="wpgao" data-post="6" data-topic="5056">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/8e8cbc/48.png" class="avatar"> wpgao:</div>
<blockquote>
<p>Is under development?</p>
</blockquote>
</aside>
<p>Since Slicer and associated libraries are consistently improved and we use the template regularly, you can consider it is actively maintained.</p>

---

## Post #8 by @wpgao (2018-12-13 05:26 UTC)

<aside class="quote no-group quote-modified" data-username="jcfr" data-post="7" data-topic="5056">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<blockquote>
<p>Does it work now?</p>
</blockquote>
<p>Yes, we use it to create custom application. To illustrate, here are few examples I can disclose:</p>
<ul>
<li><a href="https://blog.kitware.com/kitware-customer-highlight-muriplan-from-xstrahl-a-3d-slicer-based-radiotherapy-treatment-planning-system/" rel="noopener nofollow ugc">MuriPlan from Xstrahl – A 3D Slicer based radiotherapy treatment planning system</a></li>
<li><a href="https://blog.kitware.com/kitware-customer-highlight-radiopharmaceutical-imaging-and-dosimetry-llc-rapid/" rel="noopener nofollow ugc">Kitware customer highlight: Radiopharmaceutical Imaging and Dosimetry, LLC (RAPID) </a></li>
<li><a href="https://blog.kitware.com/kitware-customer-highlight-sonovol/" rel="noopener nofollow ugc">Kitware customer highlight: SonoVol </a></li>
<li><a href="https://blog.kitware.com/xoran-technologies-and-kitware-collaborate-on-image-guided-platform-for-deep-brain-stimulation-surgery/" rel="noopener nofollow ugc">Xoran Technologies and Kitware Collaborate on Image-guided Platform for Deep Brain Stimulation Surgery </a></li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df84136137514ef83e32e2c81e07ab038b960196.png" alt="" data-base62-sha1="vTjrHudOfjMmn9HvD24HEohgTDU" width="20" height="20" role="presentation"> wpgao:</p>
</blockquote>
</aside>
<p>Excellent works! I agree with you that Slicer and associated libraries are consistently improved, which require frequent maintenance!</p>

---

## Post #9 by @jcfr (2018-12-13 05:30 UTC)

<aside class="quote no-group" data-username="wpgao" data-post="8" data-topic="5056">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/8e8cbc/48.png" class="avatar"> wpgao:</div>
<blockquote>
<p>which require frequent maintenance!</p>
</blockquote>
</aside>
<p>To clarify, if the Slicer version associated with a custom application must be updated, this is usually a one line change that consist in updating the Git SHA in the top-level CMakeLists.txt of the custom application.</p>

---

## Post #10 by @wpgao (2018-12-13 05:33 UTC)

<p>Is there any userguide of SlicerCustomAppTemplate which can be referred to?</p>

---

## Post #11 by @jcfr (2018-12-13 05:49 UTC)

<p>After following, the <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate#getting-started" rel="nofollow noopener">Getting Started</a> instructions, you will have a custom application source tree ready.</p>
<p>Then to compile your custom application, follow the regular instructions to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">Build Slicer Application</a></p>
<p>Finally, reading the comment of the top-level <code>CMakeLists.txt</code> of the custom application should provide enough details to get started.</p>

---

## Post #12 by @wpgao (2018-12-13 05:55 UTC)

<p>Great! I really appreciate your help! Thank you very much!</p>

---

## Post #13 by @lassoan (2021-09-02 15:22 UTC)

<p>A post was split to a new topic: <a href="/t/create-slicer-with-customized-user-interface/19485">Create Slicer with customized user interface</a></p>

---
