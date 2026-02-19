---
topic_id: 7207
title: "Build Slicer Error Need Your Help"
date: 2019-06-17
url: https://discourse.slicer.org/t/7207
---

# Build slicer error,need your help

**Topic ID**: 7207
**Date**: 2019-06-17
**URL**: https://discourse.slicer.org/t/build-slicer-error-need-your-help/7207

---

## Post #1 by @zhaobingshuai (2019-06-17 20:41 UTC)

<p>hello, when i build slicer, i enter &lt;ccmake -DCMAKE_BUILD_TYPE:STRING=Release DQt5_DIR:PATH=/home/zbs/package/Qt/5.12.2/gcc_64/lib/cmake/Qt5/Qt5Config.cmake …/Slicer&gt;<br>
i meet errors as follows, maybe the reason is  i install qt more than one.Could you give me some advice? Thank you very much.</p>
<p>CMake Warning at CMake/SlicerBlockFindQtAndCheckVersion.cmake:22 (find_package):<br>
Found package configuration file:</p>
<pre><code> /usr/lib/x86_64-linux-gnu/cmake/Qt5/Qt5Config.cmake
</code></pre>
<p>but it set Qt5_FOUND to FALSE so package “Qt5” is considered to be NOT<br>
FOUND.  Reason given by package:</p>
<p>Failed to find Qt5 component “Multimedia” config file at<br>
“/usr/lib/x86_64-linux-gnu/cmake/Qt5Multimedia/Qt5MultimediaConfig.cmake”</p>
<p>Failed to find Qt5 component “XmlPatterns” config file at<br>
“/usr/lib/x86_64-linux-gnu/cmake/Qt5XmlPatterns/Qt5XmlPatternsConfig.cmake”</p>
<p>Failed to find Qt5 component “Svg” config file at<br>
“/usr/lib/x86_64-linux-gnu/cmake/Qt5Svg/Qt5SvgConfig.cmake”</p>
<p>Failed to find Qt5 component “WebEngine” config file at<br>
“/usr/lib/x86_64-linux-gnu/cmake/Qt5WebEngine/Qt5WebEngineConfig.cmake”</p>
<p>Failed to find Qt5 component “WebEngineWidgets” config file at<br>
“/usr/lib/x86_64-linux-gnu/cmake/Qt5WebEngineWidgets/Qt5WebEngineWidgetsConfig.cmake”</p>
<p>Failed to find Qt5 component “WebChannel” config file at<br>
“/usr/lib/x86_64-linux-gnu/cmake/Qt5WebChannel/Qt5WebChannelConfig.cmake”</p>
<p>Errors occurred during the last pass</p>

---

## Post #2 by @jcfr (2019-06-17 22:01 UTC)

<p>Considering setting <code>Qt5_DIR</code> to <code>/home/zbs/package/Qt/5.12.2/gcc_64/lib/cmake/Qt5</code> instead of <code>/home/zbs/package/Qt/5.12.2/gcc_64/lib/cmake/Qt5/Qt5Config.cmake</code></p>
<p>For more details, see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Unix-like" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Unix-like</a></p>

---

## Post #3 by @alankrutha (2020-03-23 11:54 UTC)

<p>Hi Jean,</p>
<p>I have tried with “cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DQt5_DIR:PATH=/usr/lib/x86_64-linux-gnu/cmake/Qt5/ …/…/Slicer” , but still i’m getting same errors.</p>

---

## Post #4 by @jcfr (2020-03-23 17:32 UTC)

<p>In your last attempt to configure,  you used <code>/usr/lib/x86_64-linux-gnu/cmake/Qt5/</code> instead of <code>/home/zbs/package/Qt/5.12.2/gcc_64/lib/cmake/Qt5</code></p>
<p>I suggest the following:<br>
(1) Use the version of Qt5 installed in <code>/home/zbs/package/Qt/5.12.2/</code><br>
(2) Make sure that WebEngine and QtScript are installed. The files <code>Qt5Script/Qt5ScriptConfig.cmake</code> and <code>Qt5WebEngine/Qt5WebEngineConfig.cmake</code> should exist in the directory <code>/home/zbs/package/Qt/5.12.2/gcc_64/lib/cmake</code>. If not, update your Qt install to install the corresponding components.  See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Linux">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Linux</a></p>
<pre><code class="lang-auto">
</code></pre>

---

## Post #5 by @dlanuza (2020-11-27 03:13 UTC)

<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://s1.wp.com/i/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://ravirnjn.wordpress.com/2015/03/03/installing-buildmlearn-toolkit-on-ubuntu-14-04/" target="_blank" rel="noopener nofollow ugc" title="10:51AM - 03 March 2015">Ravi Ranjan – 3 Mar 15</a>
  </header>
  <article class="onebox-body">
    <img src="https://s0.wp.com/i/blank.jpg" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://ravirnjn.wordpress.com/2015/03/03/installing-buildmlearn-toolkit-on-ubuntu-14-04/" target="_blank" rel="noopener nofollow ugc">Installing BuildmLearn-ToolKit On Ubuntu 14.04</a></h3>

<p>BuildmLearn Toolkit is an easy-to-use program that helps the users make mobile apps without any knowledge of application development. (Github Page , Download Link) Installation instruction for Linu…</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
sudo apt-get install qtmultimedia5-dev

---
