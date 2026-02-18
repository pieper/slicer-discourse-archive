# Minimum required version of CMake updated to 3.5.0

**Topic ID**: 828
**Date**: 2017-08-04
**URL**: https://discourse.slicer.org/t/minimum-required-version-of-cmake-updated-to-3-5-0/828

---

## Post #1 by @jcfr (2017-08-04 18:44 UTC)

<p>As discussed in PR <a href="https://github.com/Slicer/Slicer/pull/765">Slicer/Slicer#765</a>, the minimum version of CMake required to build Slicer is now <strong>CMake 3.5.0</strong></p>
<p>Associated changes integrated in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26201">r26201</a>, <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26202">r26202</a> and <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26203">r26203</a></p>
<p>This will ensure the CMake version has:</p>
<ul>
<li>support for VS 2015 (introduced in CMake 3.1)</li>
<li>a decent support for detecting <a href="https://cmake.org/cmake/help/v3.5/manual/cmake-compile-features.7.html">compiler features</a> (useful with C++11 and above)</li>
<li>as well as support for modern cmake that will be used to modernize the Slicer build system. See <a href="https://cmake.org/cmake/help/v3.5/manual/cmake-buildsystem.7.html#build-specification-and-usage-requirements">here</a> and below.</li>
</ul>
<p>CMake 3.5 is also old enough (released in April 2016) and available (same version<br>
or above) in distributions like these ones:</p>
<ul>
<li>Arch Linux</li>
<li>Ubuntu LTS 14.04, 16.04</li>
<li>OpenSUSE Leap 42.2, 42.3</li>
<li>Debian 9, Sid</li>
<li>Fedora 24/25/26</li>
<li>Slackware 14.2</li>
</ul>
<p>See <a href="https://pkgs.org/download/cmake">https://pkgs.org/download/cmake</a></p>
<p>Note that the statement <code>cmake_minimum_required(VERSION 3.5)</code> does <strong>NOT</strong> need to be updated in the extension source trees.</p>
<p>That said:</p>
<ul>
<li>
<p>whenever possible, extension developer are encouraged to update it in the top level <code>CMakeLists.txt</code>. This will most likely avoid confusion …</p>
</li>
<li>
<p>the version of CMake used to build the extension need to be 3.5. To facilitate the overall maintenance, this is a hard requirement (an explicit <code>cmake_minimum_required(VERSION 3.5)</code> statement was added to <code>SlicerConfig.cmake</code> and <code>UseSlicer.cmake</code></p>
</li>
</ul>
<p>If you are interested, this presentation from Tobias Becker is a nice introduction to modern CMake:</p>
<aside class="onebox googledocs">
  <header class="source">
      <a href="https://docs.google.com/presentation/d/18fY0zDtJCMUW5WdY2ZOfKtvb7lXEbBPFe_I6MNJC0Qw/edit#slide=id.p" target="_blank" rel="nofollow noopener">docs.google.com</a>
  </header>
  <article class="onebox-body">
    <a href="https://docs.google.com/presentation/d/18fY0zDtJCMUW5WdY2ZOfKtvb7lXEbBPFe_I6MNJC0Qw/edit#slide=id.p" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-slides-logo"></span></a>

<h3><a href="https://docs.google.com/presentation/d/18fY0zDtJCMUW5WdY2ZOfKtvb7lXEbBPFe_I6MNJC0Qw/edit#slide=id.p" target="_blank" rel="nofollow noopener">Modern CMake</a></h3>

<p>Prerequisites: cmake &amp;gt;= 3.5 git https://github.com/toeb/moderncmake.git 1</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
