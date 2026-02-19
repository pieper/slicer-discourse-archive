---
topic_id: 2239
title: "Gui Libraries And Licenses"
date: 2018-03-05
url: https://discourse.slicer.org/t/2239
---

# GUI libraries and licenses

**Topic ID**: 2239
**Date**: 2018-03-05
**URL**: https://discourse.slicer.org/t/gui-libraries-and-licenses/2239

---

## Post #1 by @terajnol (2018-03-05 15:03 UTC)

<p>Hi everyone,</p>
<p>The default GUI library for modules is Qt, used by the great majority of extensions.<br>
I have few questions about GUi libraries:</p>
<ul>
<li>
<p>Are other GUI libraries supported by Slicer 3D? It is possible to use Tkinter but that’s because, I think, it is natively included into Python. Are there examples of existing extensions using another GUI lib than Qt ?</p>
</li>
<li>
<p><strong>In the development of a Python-scripted module:</strong> Is it possible to attach non-Qt windows to Slicer program as it is possible for the windows “SlicerApp real” ? Or maybe it is possible to include non-Qt buttons direclty into the “SlicerApp real” windows ?</p>
</li>
<li>
<p>Slicer is under a BSD-style license, which authorizes commercial use, but most of the GUIs are made with Qt, which is not commercial-use free. Isn’t there a conflict here ?</p>
</li>
</ul>
<p>Thank you for your advices !</p>

---

## Post #2 by @lassoan (2018-03-05 15:28 UTC)

<aside class="quote no-group" data-username="terajnol" data-post="1" data-topic="2239">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/eb8c5e/48.png" class="avatar"> terajnol:</div>
<blockquote>
<p>Are other GUI libraries supported by Slicer 3D</p>
</blockquote>
</aside>
<p>You can bring in additional GUI toolkits, but Qt is by far the best (most comprehensive, nicest-looking) free, open-source, multi-platform GUI toolkit. Why would you even consider using TkInter when Qt is already available?</p>
<blockquote>
<p>Is it possible to attach non-Qt windows to Slicer program as it is possible for the windows “SlicerApp real”</p>
</blockquote>
<p>Usage of Slicer application and GUI classes are optional. MRML core libraries, module logics, CLI modules, etc. do not depend on Qt and can be used independently from the Slicer application. Some features, such as Subject Hierarchy and Segment Editor uses Qt classes as base classes for their plugins, so those will not work without Qt, but most everything else should.</p>
<blockquote>
<p>Slicer is under a BSD-style license, which authorizes commercial use, but most of the GUIs are made with Qt, which is not commercial-use free. Isn’t there a conflict here ?</p>
</blockquote>
<p>Qt comes with LGPL license, which is free to use, even for commercial purposes. The only practical limitation is that you cannot link Qt to your application as a static library (it must be used as a dynamically-loaded library).</p>

---

## Post #3 by @terajnol (2018-03-05 16:19 UTC)

<p>Thank you for your answer.<br>
Actually, yes, if it is possible to use Slicer for commercial purposes with Qt linked as dynamically-loaded lib, the rest of my question makes no sense. For sure Qt is easier to use.</p>
<p>So if I understand well, a home-made Slicelet using Qt as GUI lib can be sold under LGPL license and th only limitation is that Qt needs to be dynamically-loaded. Since Qt can be quite expensive, I didn’t know it was possible. What are the disadvantages in this case ?<br>
I am not an expert but I think it is then not possible to only have 1 .exe file as a final product. Maybe there are some dependances with Qt updates ?</p>

---

## Post #4 by @lassoan (2018-03-05 16:28 UTC)

<p>There are no practically relevant disadvantages of using Qt with LGPL license. Qt website tries to convince people to buy commercial license and support, which makes sense for them (and useful for the Qt user community if some people pay for Qt development), but paying is not necessary.</p>

---

## Post #5 by @terajnol (2018-03-05 16:33 UTC)

<p>Ok thank you very much for your answer !<br>
It is always good to know that about Qt !</p>

---

## Post #6 by @jcfr (2018-03-06 03:03 UTC)

<aside class="quote no-group" data-username="terajnol" data-post="3" data-topic="2239">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/eb8c5e/48.png" class="avatar"> terajnol:</div>
<blockquote>
<p>Actually, yes, if it is possible to use Slicer for commercial purposes with Qt linked as dynamically-loaded lib, the rest of my question makes no sense. For sure Qt is easier to use.</p>
</blockquote>
</aside>
<p>Indeed, here are just few examples of commercial applications made possible by the underlying awesome collaborative work of the 3D Slicer community and beyond:</p>
<ul>
<li><a href="https://blog.kitware.com/kitware-customer-highlight-muriplan-from-xstrahl-a-3d-slicer-based-radiotherapy-treatment-planning-system/">Kitware customer highlight: MuriPlan from Xstrahl – A 3D Slicer based radiotherapy treatment planning system</a></li>
<li><a href="https://blog.kitware.com/kitware-customer-highlight-sonovol/">Kitware customer highlight: SonoVol</a></li>
</ul>
<aside class="quote no-group" data-username="terajnol" data-post="3" data-topic="2239">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/eb8c5e/48.png" class="avatar"> terajnol:</div>
<blockquote>
<p>So if I understand well, a home-made Slicelet using Qt as GUI lib can be sold under LGPL license and th only limitation is that Qt needs to be dynamically-loaded. Since Qt can be quite expensive, I didn’t know it was possible. What are the disadvantages in this case ?</p>
</blockquote>
</aside>
<p>Technically your application wouldn’t be sold under a LGPL license, it would have its own license and would include a list of open-source libraries associated with it and acknowledge with one of them based on their corresponding license.</p>
<p>Distributing as single executable could be easier and ensure a faster startup time. That said:</p>
<ul>
<li>Using tools like <a href="https://cmake.org/cmake/help/latest/manual/cpack.1.html">cpack</a> can definitively help.</li>
<li>I also suggest to run some benchmark to clearly understand what is the bottleneck. Building a cross-platform and static application also comes with its own challenges.</li>
</ul>
<aside class="quote no-group" data-username="terajnol" data-post="3" data-topic="2239">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/eb8c5e/48.png" class="avatar"> terajnol:</div>
<blockquote>
<p>I am not an expert but I think it is then not possible to only have 1 .exe file as a final product.</p>
</blockquote>
</aside>
<p>As indicated by the <a href="https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License#Differences_from_the_GPL">LGPL license</a>, user of your application should be able to provide its own Qt libraries. Unless you provide the source code of your application, this is possible only with dynamic libraries.</p>
<p>See <a href="https://softwareengineering.stackexchange.com/a/86158" class="inline-onebox">What exactly do I need to do if I use a LGPL licensed library? - Software Engineering Stack Exchange</a></p>
<p><em>Note that I am not a lawyer, and this is not a legal advice.</em></p>
<aside class="quote no-group" data-username="terajnol" data-post="3" data-topic="2239">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/eb8c5e/48.png" class="avatar"> terajnol:</div>
<blockquote>
<p>Maybe there are some dependances with Qt updates ?</p>
</blockquote>
</aside>
<p>I am not sure to understand this last question.</p>

---

## Post #7 by @pieper (2018-03-06 12:51 UTC)

<aside class="quote no-group" data-username="terajnol" data-post="3" data-topic="2239">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/eb8c5e/48.png" class="avatar"> terajnol:</div>
<blockquote>
<p>I am not an expert but I think it is then not possible to only have 1 .exe file as a final product. Maybe there are some dependances with Qt updates ?</p>
</blockquote>
</aside>
<p>Also of course you can make a single .exe that is an installer, like Slicer’s, that is what many windows users will expect.  This can include a <a href="http://www.commontk.org/index.php/Tools:_Application_launcher">launcher</a> like Slicer’s to handle the shared libraries as required by the LGPL and also isolates you from any other Qt libraries that might be installed by other apps.</p>

---

## Post #8 by @ihnorton (2018-03-06 14:48 UTC)

<p>For the sake of completeness:</p>
<p><a href="https://www.gnu.org/licenses/gpl-faq.en.html#LGPLStaticVsDynamic" class="onebox" target="_blank" rel="noopener">https://www.gnu.org/licenses/gpl-faq.en.html#LGPLStaticVsDynamic</a></p>
<blockquote>
<p>(1) If you statically link against an LGPL’d library, you must also provide your application in an object (not necessarily source) format, so that a user has the opportunity to modify the library and relink the application.</p>
</blockquote>
<p>The only place one might practically need this is embedded/resource-constrained contexts. In the context of Slicer, as Andras said, there’s no downside to dynamic linking (excluding webengine, which is basically Chromium, Qt libraries are “only” ~30 MB, a fraction of the total, and load faster than most of the others).</p>

---

## Post #9 by @jcfr (2018-03-06 21:55 UTC)

<p>Finally, this page also provides useful information:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.qt.io/product/features">
  <header class="source">
      <img src="https://www.qt.io/hubfs/2016_Qt_Logo/qt_logo_green_rgb_16x16.png" class="site-icon" width="" height="">

      <a href="https://www.qt.io/product/features" target="_blank" rel="noopener">qt.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://www.qt.io/product/features" target="_blank" rel="noopener">Qt Features, Framework Essentials, Modules, Tools &amp; Add-Ons</a></h3>

  <p>See the features of the latest Qt version to see new functionality, which development platforms, operating systems and coding languages are supported.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @terajnol (2018-03-07 09:16 UTC)

<p>Thank you all for this complete answer. It gives me (and maybe other users) a better overview of Qt use with 3D Slicer.<br>
Indeed, it seems easier to use Qt under the LGPL license for a commercial use of 3D Slicer, with the few constraints described above. This is good to know for any preparatory work for applications running with Slicer.</p>

---
