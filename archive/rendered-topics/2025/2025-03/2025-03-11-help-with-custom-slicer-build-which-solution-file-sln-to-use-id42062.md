# Help with Custom Slicer Build – Which Solution File (.sln) to Use in Visual Studio?

**Topic ID**: 42062
**Date**: 2025-03-11
**URL**: https://discourse.slicer.org/t/help-with-custom-slicer-build-which-solution-file-sln-to-use-in-visual-studio/42062

---

## Post #1 by @software (2025-03-11 04:42 UTC)

<p>I have built a <strong>custom template of Kitware</strong> in <strong>Release mode</strong> using <strong>CMake GUI</strong> with the following directories:</p>
<ul>
<li><strong>Source code:</strong> <code>E:/Safe</code></li>
<li><strong>Binary build:</strong> <code>E:/Safe/build</code></li>
</ul>
<p>After configuring and generating the project, the build was successful. Now, I have two <strong>.sln</strong> files:</p>
<ol>
<li><code>build/safe.sln</code></li>
<li><code>build/slicer_build/slicer.sln</code></li>
</ol>
<p>I am confused about which <strong>.sln</strong> file I should open in <strong>Visual Studio</strong> to continue compiling and customizing 3D Slicer.</p>
<p>Could someone guide me on the correct approach? I’d really appreciate any help.</p>
<p><strong>Thank you!</strong></p>

---

## Post #2 by @jamesobutler (2025-03-11 08:08 UTC)

<p>The first solution file will build all the dependencies as well as the Slicer core code. The 2nd solution file is only the Slicer core code.</p>
<p>If you’re using Windows and CMake-gui you can press the “open project” button after configure and generate steps as described at:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#using-graphical-user-interface-alternative-solution">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#using-graphical-user-interface-alternative-solution" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#using-graphical-user-interface-alternative-solution" target="_blank" rel="noopener nofollow ugc">Windows — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @software (2025-03-11 09:55 UTC)

<p>First of all, thanks for the reply.</p>
<p>The initial build of my <strong>custom template</strong> is complete using the mentioned method (opening the project from <strong>CMake GUI</strong> and clicking on <strong>ALL_BUILD</strong>). My first build is ready.</p>
<p>However, I am confused about the next steps. If I want to <strong>add custom modules, change the logo, or make other modifications</strong> to my custom application, what are the correct steps? Also, which <strong>.sln</strong> file should I open in <strong>Visual Studio</strong> to build and see my changes?</p>

---

## Post #4 by @software (2025-03-11 10:04 UTC)

<p>As you can see, my application’s name is <strong>SafeSlicerApp</strong>, which I created using the Kitware blog.</p>
<p>I have opened <strong><code>build/slicer_build/slicer.sln</code></strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07cf6dc9cbd3266f7debcab5b5e638a00189756e.png" data-download-href="/uploads/short-url/175KUhttk2czjQV0JRXttkjEBYy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07cf6dc9cbd3266f7debcab5b5e638a00189756e.png" alt="image" data-base62-sha1="175KUhttk2czjQV0JRXttkjEBYy" width="376" height="500" data-dominant-color="292929"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">581×771 28.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
