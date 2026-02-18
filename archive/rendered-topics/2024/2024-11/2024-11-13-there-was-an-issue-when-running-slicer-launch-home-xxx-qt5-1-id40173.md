# There was an issue when running ./Slicer --launch /home/xxx/Qt5.14.2/Tools/QtCreator/bin/qtcreator on Ubuntu 18.04.

**Topic ID**: 40173
**Date**: 2024-11-13
**URL**: https://discourse.slicer.org/t/there-was-an-issue-when-running-slicer-launch-home-xxx-qt5-14-2-tools-qtcreator-bin-qtcreator-on-ubuntu-18-04/40173

---

## Post #1 by @tthh7 (2024-11-13 14:09 UTC)

<p>I successfully built Slicer version 5.7.0-2024-11-08 on Ubuntu 18.04 following the instructions in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html" rel="noopener nofollow ugc">Slicer documentation</a>. However, when I try to debug using Qt, I run into an issue. I launched Qt Creator using the command:<br>
<strong>./Slicer --launch /home/xxx/Qt5.14.2/Tools/QtCreator/bin/qtcreator</strong></p>
<p>and received this error:<br>
<strong>Cannot mix incompatible Qt library (version 0x50e02) with this library (version 0x50e01)</strong><br>
<strong>error: [/home/xxx/Qt5.14.2/Tools/QtCreator/bin/qtcreator] exit abnormally - Report the problem.</strong></p>
<p>When building, I used the following cmake command:<br>
<strong>cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DQt5_DIR=/home/xxx/Qt5.14.2/5.14.2/gcc_64/lib/cmake/Qt5 …/Slicer</strong></p>
<p>Could you advise on how to resolve this issue?</p>

---

## Post #2 by @lassoan (2024-11-13 14:13 UTC)

<p>I don’t think this would be something specific to Slicer, but it seems to be a quite widely reported problem on Linux with Qt. Please try some of the suggestions that fixed it for others, for example:</p>
<aside class="onebox stackexchange" data-onebox-src="https://stackoverflow.com/questions/40372537/cannot-mix-incompatible-qt-library-version-0x50501-with-this-library-version">
  <header class="source">

      <a href="https://stackoverflow.com/questions/40372537/cannot-mix-incompatible-qt-library-version-0x50501-with-this-library-version" target="_blank" rel="noopener">stackoverflow.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/6190887/rico" target="_blank" rel="noopener">
    <img alt="Rico" src="https://i.sstatic.net/tQVBC.png?s=256" class="thumbnail onebox-avatar" width="256" height="256">
  </a>

<h4>
  <a href="https://stackoverflow.com/questions/40372537/cannot-mix-incompatible-qt-library-version-0x50501-with-this-library-version" target="_blank" rel="noopener">Cannot mix incompatible Qt library (version 0x50501) with this library (version 0x50201)</a>
</h4>

<div class="tags">
  <strong>qt, ubuntu</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://stackoverflow.com/users/6190887/rico" target="_blank" rel="noopener">
    Rico
  </a>
  on <a href="https://stackoverflow.com/questions/40372537/cannot-mix-incompatible-qt-library-version-0x50501-with-this-library-version" target="_blank" rel="noopener">04:32AM - 02 Nov 16 UTC</a>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @tthh7 (2024-11-14 01:17 UTC)

<p>I think I may have identified the problem: on Ubuntu 18.04, I installed Qt 5.14.2 and ran the cmake command <code>-DQt5_DIR=/home/xxx/Qt5.14.2/5.14.2/gcc_64/lib/cmake/Qt5</code>. This makes Slicer pull the required libraries from this path, where all the libraries are version 5.14.2. However, when launching Qt Creator using <code>./Slicer --launch /home/xxx/Qt5.14.2/Tools/QtCreator/bin/qtcreator</code>, the libraries used by Qt Creator are not from <code>/home/xxx/Qt5.14.2/5.14.2/gcc_64/lib</code> but instead from <code>/home/xxx/Qt5.14.2/Tools/QtCreator/lib/Qt/lib</code>. The libraries in this path are linked to version 5.14.1</p>

---
