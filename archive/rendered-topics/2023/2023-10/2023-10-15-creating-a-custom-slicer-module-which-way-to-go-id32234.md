# Creating a Custom Slicer Module - which way to go?

**Topic ID**: 32234
**Date**: 2023-10-15
**URL**: https://discourse.slicer.org/t/creating-a-custom-slicer-module-which-way-to-go/32234

---

## Post #1 by @seanchoi0519 (2023-10-15 23:02 UTC)

<p>Hello everyone</p>
<p>I’m a long-time slicer lurker, who has received much help from everyone here and just want to extend my thanks. After a few years of using Slicer, I feel ready to start developing a few custom modules of my own. I did a brief search on what the best way to go about this would be and ran into many options which confused me. I wanted to know the difference as far as the options go:</p>
<ol>
<li>SlicerIGT (<a href="https://www.slicerigt.org/wp/developer-tutorial/" class="inline-onebox" rel="noopener nofollow ugc">Developer tutorial | SlicerIGT</a>)</li>
<li>Guidelet (?) is this the same thing as option 1?</li>
<li>Slicelet (<a href="https://www.slicer.org/w/index.php/Documentation/Nightly/Developers/Slicelets" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Slicelets - Slicer Wiki</a>). Is this similar to Guidelet?</li>
<li>Kitware (<a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" class="inline-onebox" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerCustomAppTemplate: Template to be used as a starting point for creating a custom 3D Slicer application</a>)</li>
</ol>
<p>What is the difference between the three? They appear similar to me in that they are all meant to provide templates in creating custom modules.</p>
<p>I’m looking to create a very specific workflow oriented software, where it would hide most of the default slicer functionalities/GUI and focus on simplicity. The software would ideally be launched with a click of a button from the desktop, instead of needing to search for it in the modules tab, download the extension, etc. to load it.</p>
<p>Which option would be best?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2023-10-16 17:25 UTC)

<p>A slicelet is definitely the most straightforward way to get started.  You can just repackage the binaries you get from <a href="http://slicer.org">slicer.org</a>.  If you’re mainly automating existing workflows and streamlining the UI you can do everything conveniently in Python.  SlicerIGT and Guidelets are for surgical navigation applications and you don’t seem t be doing that.  Only do a custom app if you need to add C++ code or otherwise change the whole application.</p>

---

## Post #3 by @mikebind (2023-10-16 17:52 UTC)

<p>Just FYI, a search for “slicelet” on the current documentation site has no hits: <a href="https://slicer.readthedocs.io/en/latest/search.html?q=slicelet&amp;check_keywords=yes&amp;area=default" class="inline-onebox">Search — 3D Slicer documentation</a></p>

---

## Post #4 by @pieper (2023-10-16 19:54 UTC)

<p>True, not all the wiki material has been migrated to readthedocs, so sometimes you need to look both places.</p>

---

## Post #5 by @seanchoi0519 (2023-10-17 05:30 UTC)

<p>Thanks for your reply!<br>
Could I clarify what you mean by " You can just repackage the binaries you get from <a href="http://slicer.org" rel="noopener nofollow ugc">slicer.org</a>"?</p>
<p>Also, do you mind delving deeper into what a slicelet is capable of vs. a custom app (kitware)? Is there perhaps an example of each so I have an idea of what each of the option is used for?</p>
<p>The way I understand it at the moment, a slicelet is essentially simply hiding unnecessary UI elements, showing only the necessary parts on Slicer, while a custom app is a complete renovation?</p>

---

## Post #6 by @Sam_Horvath (2023-10-17 14:42 UTC)

<p>So , the custom app uses the same techniques to modify the Slicer UI as the slicelet, (by grabbing and hiding existing widgets in the QT environment), but also has many other options for customization.  We have two blogs on using the custom app template:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/">
  <header class="source">
      <img src="https://www.kitware.com/main/wp-content/themes/kitwarean/assets/img/favicon/android-icon-192x192.png" class="site-icon" width="192" height="192">

      <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" target="_blank" rel="noopener">kitware.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:351/224;"><img src="https://www.kitware.com/main/wp-content/uploads/2019/10/SlicerCATSplash2.png" class="thumbnail" width="351" height="224"></div>

<h3><a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" target="_blank" rel="noopener">SlicerCAT:  Creating custom applications based on 3D Slicer</a></h3>

  <p>This blog presents a framework for making custom applications based on 3D Slicer. What is 3D Slicer? 3D Slicer is a software platform for the analysis and visualization of medical images and for research in image guided therapy. It is free, open...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.kitware.com/slicercat-and-python-creating-custom-slicer-applications-with-qt-stylesheets/">
  <header class="source">
      <img src="https://www.kitware.com/main/wp-content/themes/kitwarean/assets/img/favicon/android-icon-192x192.png" class="site-icon" width="192" height="192">

      <a href="https://www.kitware.com/slicercat-and-python-creating-custom-slicer-applications-with-qt-stylesheets/" target="_blank" rel="noopener">kitware.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/276;"><img src="https://www.kitware.com/main/wp-content/uploads/2021/08/xSlicerCAT-1024x410-2.webp" class="thumbnail" width="690" height="276"></div>

<h3><a href="https://www.kitware.com/slicercat-and-python-creating-custom-slicer-applications-with-qt-stylesheets/" target="_blank" rel="noopener">SlicerCAT and Python: Creating Custom Slicer Applications with Qt Stylesheets</a></h3>

  <p>What is SlicerCAT? Our previous blog post on the Slicer Custom App Template (SlicerCAT) explained how to build a custom application based on 3D Slicer with CMake. In this follow-up blog, we present a framework for creating a custom Python scripted...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The custom app template allows you to:</p>
<ul>
<li>pick and choose what core modules you want enabled</li>
<li>bundle in extensions at build time</li>
<li>bundle in custom modules (python and C++)</li>
<li>use custom versions of the Slicer code or other dependencies (if needed)</li>
<li>replace the Slicer logos with your own</li>
</ul>
<p>I highly recommend starting your development work in the ‘slicelet’ format.  If you decide to do a custom app, this work can be reused in the custom app.  The custom amp template contains a ‘Home’ module that functions very similarly to a slicelet and uses the same methods to modify the Slicer UI.</p>

---
