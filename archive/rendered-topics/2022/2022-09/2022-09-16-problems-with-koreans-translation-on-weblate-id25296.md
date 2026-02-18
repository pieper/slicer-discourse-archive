# Problems with Korean's translation on Weblate

**Topic ID**: 25296
**Date**: 2022-09-16
**URL**: https://discourse.slicer.org/t/problems-with-koreans-translation-on-weblate/25296

---

## Post #1 by @DDinghoya (2022-09-16 05:57 UTC)

<p>HI everyone!!!</p>
<p>First of all, I am honored to have had the opportunity to experience this great program.</p>
<p>Basically the Korean translation was 100% completed on weblate, and there were two problems.</p>
<ol>
<li>Korean translation was made, but some items are not reflected. (Photos to be attached later)</li>
</ol>
<p>Even if I downloaded the language pack from github and applied it manually, it was not reflected.</p>
<ol start="2">
<li>Some HTML tags disappear after saving the translation on Weblate as below;</li>
</ol>
<pre><code class="lang-auto">&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name="qrichtext" content="1" /&gt;&lt;style type="text/css"&gt;
</code></pre>
<p>is changed to</p>
<pre><code class="lang-auto">&amp;lt;html&amp;gt;&lt;meta name="qrichtext" content="1"&gt;&lt;style type="text/css"&gt;
</code></pre>
<p>Also, some style strings are changed, like</p>
<pre><code class="lang-auto">&lt;/span&gt;&lt;span style=" font-size:8pt; font-weight:600;"&gt;
</code></pre>
<p>to</p>
<pre><code class="lang-auto">&lt;/span&gt;&lt;span style=""&gt;
</code></pre>
<p>I think the problem arises when using a 2 byte charset.</p>
<p>It is hoped that the cause of the problem and improvement will be addressed through this post.</p>
<p>Best regards.</p>

---

## Post #2 by @pieper (2022-09-16 16:32 UTC)

<p>Thank you for reporting this and for your translation contributions <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>Internationalization of the full interface is complex, with many special cases that need to be handled carefully to avoid breaking core functionality.  Fortunately we have a team in Senegal, Canada, and the US working to make improvements with funding from CZI:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://chanzuckerberg.com/eoss/proposals/3d-slicer-in-my-language-internationalization-and-usability-improvements/">
  <header class="source">
      <img src="https://chanzuckerberg.com/wp-content/uploads/2018/04/new-logo.png?w=32" class="site-icon" width="32" height="32">

      <a href="https://chanzuckerberg.com/eoss/proposals/3d-slicer-in-my-language-internationalization-and-usability-improvements/" target="_blank" rel="noopener">Chan Zuckerberg Initiative</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/386;"><img src="https://chanzuckerberg.com/wp-content/uploads/2020/06/Science_RFA_Opensource_Banner_wBG-1-1.png" class="thumbnail" width="690" height="386"></div>

<h3><a href="https://chanzuckerberg.com/eoss/proposals/3d-slicer-in-my-language-internationalization-and-usability-improvements/" target="_blank" rel="noopener">3D Slicer in My Language: Internationalization and Usability Improvements -...</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Could you file your findings on the github issues for the effort?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Slicer/SlicerLanguagePacks/issues">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/SlicerLanguagePacks/issues" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/c7d2802847bb5ebb613c5455b679fef15d049a0d0fb2bb1ccb8d58417a0d4ab1/Slicer/SlicerLanguagePacks" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Slicer/SlicerLanguagePacks/issues" target="_blank" rel="noopener">Issues · Slicer/SlicerLanguagePacks</a></h3>

  <p>3D Slicer extension for creating, editing, and storing translations for Slicer core and extensions - Issues · Slicer/SlicerLanguagePacks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @DDinghoya (2022-09-17 05:28 UTC)

<p>Thank you for your strong reply! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I’ll try it! → Done</p>

---
