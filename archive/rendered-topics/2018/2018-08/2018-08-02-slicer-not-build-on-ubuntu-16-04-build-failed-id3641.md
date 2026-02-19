---
topic_id: 3641
title: "Slicer Not Build On Ubuntu 16 04 Build Failed"
date: 2018-08-02
url: https://discourse.slicer.org/t/3641
---

# Slicer not build on Ubuntu 16.04. Build FAILED

**Topic ID**: 3641
**Date**: 2018-08-02
**URL**: https://discourse.slicer.org/t/slicer-not-build-on-ubuntu-16-04-build-failed/3641

---

## Post #1 by @glebdurygin (2018-08-02 21:28 UTC)

<p>I cant build Slicer on Ubuntu 16.04 / Qt5.5.1 / Git 2.7.4<br>
I did all the instructions from the page <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Build Instructions - Slicer Wiki</a><br>
But i have a lot of problems<br>
Please, help me<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd55692fff1dd405c6a67df0ac6699a2e990481c.jpeg" data-download-href="/uploads/short-url/tisS9s6pSZydrYMOtZIyD410nyQ.jpeg?dl=1" title="AjZJ32o5qS8" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd55692fff1dd405c6a67df0ac6699a2e990481c_2_690x388.jpeg" alt="AjZJ32o5qS8" data-base62-sha1="tisS9s6pSZydrYMOtZIyD410nyQ" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd55692fff1dd405c6a67df0ac6699a2e990481c_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd55692fff1dd405c6a67df0ac6699a2e990481c_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd55692fff1dd405c6a67df0ac6699a2e990481c_2_1380x776.jpeg 2x" data-dominant-color="3E1C34"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">AjZJ32o5qS8</span><span class="informations">1920×1080 548 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @tavaughan (2018-08-02 21:54 UTC)

<p>From your screenshot it looks like you’re getting Qt 5.9.6 in there?</p>
<p>What command are you running to build Slicer?</p>
<p>How did you install Qt?</p>

---

## Post #3 by @glebdurygin (2018-08-03 07:09 UTC)

<p>Yes, you are right. Qt version 5.9.6<br>
To install Qt5.9.6 I used this video <a href="https://www.youtube.com/watch?v=1jdjcF7rUDU" rel="nofollow noopener">https://www.youtube.com/watch?v=1jdjcF7rUDU</a></p>
<p>This is the list of all commands that I used to build Slicer:</p>
<ol>
<li>sudo apt-get install subversion git-core git-svn</li>
<li>sudo apt-get install make gcc g++ libx11-dev libxt-dev libgl1-mesa-dev libglu1-mesa-dev libfontconfig-dev libxrender-dev libncurses5-dev</li>
<li>sudo apt-get install libgstreamer-plugins-base0.10-dev</li>
<li>sudo apt-get install curl mkdir ~/Support &amp;&amp; cd ~/Support curl -O <a href="https://cmake.org/files/v3.8/cmake-3.8.2-Linux-x86_64.tar.gz" rel="nofollow noopener">https://cmake.org/files/v3.8/cmake-3.8.2-Linux-x86_64.tar.gz</a> tar -xzvf cmake-3.8.2-Linux-x86_64.tar.gz</li>
<li>mkdir -p ~/bin</li>
<li>ln -s ~/Support/cmake-3.8.2-Linux-x86_64/bin/cmake ~/bin/cmake</li>
<li>ln -s ~/Support/cmake-3.8.2-Linux-x86_64/bin/cmake-gui ~/bin/cmake-gui</li>
<li>I also install Qt 4 from this page <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#BUILD_Slicer" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#BUILD_Slicer</a>
</li>
</ol>
<p>sudo apt-get install qt4-dev-tools libqt4-dev libqtcore4 libqtgui4 libqtwebkit-dev<br>
9) cd MyProjects<br>
git clone git://github.com/Slicer/Slicer.git<br>
10) cd Slicer<br>
./Utilities/SetupForDevelopment.sh<br>
11) cd Slicer<br>
git svn init <a href="http://svn.slicer.org/Slicer4/trunk" rel="nofollow noopener">http://svn.slicer.org/Slicer4/trunk</a><br>
git update-ref refs/remotes/git-svn refs/remotes/origin/master<br>
git checkout master<br>
git svn rebase<br>
12) svn co <a href="http://svn.slicer.org/Slicer4/branches/Slicer-4-8" rel="nofollow noopener">http://svn.slicer.org/Slicer4/branches/Slicer-4-8</a> Slicer-r26813 -r 26813<br>
13) mkdir Slicer-SuperBuild<br>
cd Slicer-SuperBuild<br>
cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DQt5_DIR:PATH=/home/ubuntu-gd/Qt5.9.6/5.9.6/gcc_64/lib/cmake/Qt5 …/Slicer<br>
14) cd Slicer<br>
make -j4</p>

---

## Post #4 by @tavaughan (2018-08-03 14:41 UTC)

<p>As far as I can tell the workflow looks fine. I have my environment working using Qt built from the qt-easy-build script:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/jcfr/qt-easy-build/tree/5.10.0">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/jcfr/qt-easy-build/tree/5.10.0" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/jcfr/qt-easy-build/tree/5.10.0" target="_blank" rel="noopener nofollow ugc">GitHub - jcfr/qt-easy-build at 5.10.0</a></h3>

  <p><a href="https://github.com/jcfr/qt-easy-build/tree/5.10.0" target="_blank" rel="noopener nofollow ugc">5.10.0</a></p>

  <p><span class="label1">Scripts allowing to easily build Qt with OpenSSL support on Linux, macOS or Windows</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I just noticed your console output:</p>
<pre><code class="lang-auto">virtual memory exhausted
</code></pre>
<p>Could you be running out of RAM? How much do you have?</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.linuxquestions.org/questions/linux-newbie-8/solved-virtual-memory-exhausted-cannot-allocate-memory-4175507767/">
  <header class="source">
      <img src="https://www.linuxquestions.org/favicon.ico" class="site-icon" width="" height="">

      <a href="https://www.linuxquestions.org/questions/linux-newbie-8/solved-virtual-memory-exhausted-cannot-allocate-memory-4175507767/" target="_blank" rel="noopener nofollow ugc">linuxquestions.org</a>
  </header>

  <article class="onebox-body">
    <img src="http://images.linuxquestions.org/lqthumb.png" class="thumbnail onebox-avatar" width="200" height="200">

<h3><a href="https://www.linuxquestions.org/questions/linux-newbie-8/solved-virtual-memory-exhausted-cannot-allocate-memory-4175507767/" target="_blank" rel="noopener nofollow ugc">SOLVED: virtual memory exhausted: Cannot allocate memory</a></h3>

  <p>I'm compiling mythtv that I got from https://github.com/MythTV/mythtv on a fedora 20 64 bit machine with 1Gb ram, 60Gb hard drive. The 'make install'</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @glebdurygin (2018-08-03 18:09 UTC)

<p>I have only RAM = 4 GB</p>

---

## Post #6 by @jamesobutler (2018-08-03 19:59 UTC)

<p>The most recent <a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/HardwareConfiguration" rel="nofollow noopener">recommended hardware configuration</a> for using Slicer suggests a 64-bit OS with at least 8GB of RAM.  If you will be working with large volume data sets you will need more RAM.</p>

---
