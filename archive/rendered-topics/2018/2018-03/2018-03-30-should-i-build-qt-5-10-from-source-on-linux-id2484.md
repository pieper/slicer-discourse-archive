# Should I build Qt 5.10 from source on Linux?

**Topic ID**: 2484
**Date**: 2018-03-30
**URL**: https://discourse.slicer.org/t/should-i-build-qt-5-10-from-source-on-linux/2484

---

## Post #1 by @gaoyi.cn (2018-03-30 23:28 UTC)

<p>Thanks JC!</p>
<p>Should I build Qt5 from source or the binary coming with Ubuntu works?</p>
<p>Best,<br>
yi</p>

---

## Post #2 by @jcfr (2018-03-30 23:35 UTC)

<aside class="quote no-group quote-modified" data-username="gaoyi.cn" data-post="3" data-topic="2482">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gaoyi.cn/48/1422_2.png" class="avatar"><a href="https://discourse.slicer.org/t/why-do-i-get-build-error-class-vtkobjexporter-has-no-member-named-setobjfilecomment-when-building-slicer-against-qt4/2482/3">Why do I get build error "class vtkOBJExporter has no member named SetOBJFileComment" when building Slicer against Qt4?</a></div>
<blockquote>
<p>Should I build Qt5 from source or the binary coming with Ubuntu works?</p>
</blockquote>
</aside>
<p>Assuming you have a recent version of Ubuntu, downloading Qt 5.10 should work well.</p>
<p>Make sure you install (at least) the following components:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerBuildEnvironment/blob/8bb9e47882968d7f23cde1d3a6d5857671171ac1/Docker/qt5-centos7/qt-installer-noninteractive.qs#L50-L54">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerBuildEnvironment/blob/8bb9e47882968d7f23cde1d3a6d5857671171ac1/Docker/qt5-centos7/qt-installer-noninteractive.qs#L50-L54" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerBuildEnvironment/blob/8bb9e47882968d7f23cde1d3a6d5857671171ac1/Docker/qt5-centos7/qt-installer-noninteractive.qs#L50-L54" target="_blank" rel="noopener">Slicer/SlicerBuildEnvironment/blob/8bb9e47882968d7f23cde1d3a6d5857671171ac1/Docker/qt5-centos7/qt-installer-noninteractive.qs#L50-L54</a></h4>



    <pre class="onebox"><code class="lang-qs">
      <ol class="start lines" start="50" style="counter-reset: li-counter 49 ;">
          <li>widget.selectComponent("qt.qt5.5101.gcc_64");</li>
          <li>widget.selectComponent("qt.qt5.5101.qtscript");</li>
          <li>widget.selectComponent("qt.qt5.5101.qtscript.gcc_64");</li>
          <li>widget.selectComponent("qt.qt5.5101.qtwebengine");</li>
          <li>widget.selectComponent("qt.qt5.5101.qtwebengine.gcc_64");</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>These two pages are also useful resources:</p>
<ul>
<li><a href="https://doc.qt.io/qt-5/linux-requirements.html" class="inline-onebox">Qt for X11 Requirements | Qt 5.15</a></li>
<li><a href="https://doc.qt.io/qt-5/supported-platforms-and-configurations.html#qt-5-10" class="inline-onebox">Supported Platforms | Qt 5.15</a></li>
</ul>

---

## Post #3 by @gaoyi.cn (2018-03-30 23:46 UTC)

<p>Hi Jc,</p>
<p>On the page of</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/jcfr/qt-easy-build">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/jcfr/qt-easy-build" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <img src="https://opengraph.githubassets.com/e7aa4abeb3038ba92b9428953bc2816b736ba03fa80f583604e217eecacc3b9b/jcfr/qt-easy-build" class="thumbnail" width="" height="">

<h3><a href="https://github.com/jcfr/qt-easy-build" target="_blank" rel="noopener nofollow ugc">GitHub - jcfr/qt-easy-build: Scripts allowing to easily build Qt with OpenSSL...</a></h3>

  <p>Scripts allowing to easily build Qt with OpenSSL support on Linux, macOS or Windows - GitHub - jcfr/qt-easy-build: Scripts allowing to easily build Qt with OpenSSL support on Linux, macOS or Windows</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I went in the link behind “Scripts available for these Qt versions: 5.10.0”, this leads me to:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/jcfr/qt-easy-build/tree/5.10.0#readme">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/jcfr/qt-easy-build/tree/5.10.0#readme" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/jcfr/qt-easy-build/tree/5.10.0#readme" target="_blank" rel="noopener nofollow ugc">GitHub - jcfr/qt-easy-build at 5.10.0</a></h3>

  <p><a href="https://github.com/jcfr/qt-easy-build/tree/5.10.0#readme" target="_blank" rel="noopener nofollow ugc">5.10.0</a></p>

  <p><span class="label1">Scripts allowing to easily build Qt with OpenSSL support on Linux, macOS or Windows</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Then in the script:<br>
curl -s <a href="https://raw.githubusercontent.com/jcfr/qt-easy-build/5.9.1/Build-qt.sh" rel="noopener nofollow ugc">https://raw.githubusercontent.com/jcfr/qt-easy-build/5.9.1/Build-qt.sh</a> -o Build-qt.sh &amp;&amp; chmod u+x Build-qt.sh<br>
./Build-qt.sh -j 4</p>
<p>I assume I should change the 5.9.1 in the path to 5.10.0?</p>

---

## Post #4 by @jcfr (2018-03-30 23:49 UTC)

<p>Note: We still need to update the build instruction.</p>
<p>Since you are using  Ubuntu 16.04 (based on the message of your last post), you do not need to build Qt.</p>
<p>Could could even do it from the command line doing something like this:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/SlicerBuildEnvironment/blob/8bb9e47882968d7f23cde1d3a6d5857671171ac1/Docker/qt5-centos7/Dockerfile#L72-L75" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerBuildEnvironment/blob/8bb9e47882968d7f23cde1d3a6d5857671171ac1/Docker/qt5-centos7/Dockerfile#L72-L75" target="_blank" rel="nofollow noopener">Slicer/SlicerBuildEnvironment/blob/8bb9e47882968d7f23cde1d3a6d5857671171ac1/Docker/qt5-centos7/Dockerfile#L72-L75</a></h4>
<pre class="onebox"><code class="lang-"><ol class="start lines" start="72" style="counter-reset: li-counter 71 ;">
<li>curl -LO http://download.qt.io/official_releases/online_installers/qt-unified-linux-x64-online.run &amp;&amp; \</li>
<li>chmod u+x qt-unified-linux-x64-online.run &amp;&amp; \</li>
<li>./qt-unified-linux-x64-online.run --verbose --platform minimal --script ./qt-installer-noninteractive.qs &amp;&amp; \</li>
<li>rm -f qt-installer-noninteractive.qs qt-unified-linux-x64-online.run &amp;&amp; \</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Just make sure to update <code>qt-installer-noninteractive.qs</code> and change the location.</p>

---

## Post #5 by @jcfr (2018-03-30 23:54 UTC)

<aside class="quote no-group" data-username="gaoyi.cn" data-post="3" data-topic="2484">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gaoyi.cn/48/1422_2.png" class="avatar"> gaoyi.cn:</div>
<blockquote>
<p>I assume I should change the 5.9.1 in the path to 5.10.0?</p>
</blockquote>
</aside>
<p>Indeed. And thanks for reporting the issue. Is is now fixed in <a href="https://github.com/jcfr/qt-easy-build/commit/fe97a49bf32d15ac951b4ba6380c86985229ae29" class="inline-onebox">README: Fix documentation · jcfr/qt-easy-build@fe97a49 · GitHub</a></p>

---

## Post #6 by @gaoyi.cn (2018-03-30 23:55 UTC)

<p>Yes I’m doing both ways. It’s always healthy to build from source. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #7 by @jcfr (2018-03-31 00:04 UTC)

<aside class="quote no-group" data-username="gaoyi.cn" data-post="6" data-topic="2484">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gaoyi.cn/48/1422_2.png" class="avatar"> gaoyi.cn:</div>
<blockquote>
<p>always healthy to build from source</p>
</blockquote>
</aside>
<p>That said, note that the version of openssl we are still using in qt-easy-build is obsolete, since 2 days ago, version <code>1.0.2o</code> should be used.</p>
<p>See <a href="https://www.openssl.org/news/secadv/20180327.txt">https://www.openssl.org/news/secadv/20180327.txt</a></p>

---

## Post #8 by @ihnorton (2018-03-31 20:04 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="2484">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>qt-unified-linux-x64-online.run</p>
</blockquote>
</aside>
<p>Maybe this should be a pinned release? (reproducible build…)</p>

---

## Post #9 by @GalKer (2018-11-07 16:48 UTC)

<p>Hi,<br>
Trying to install from qt-east-build, however installation fail during QT configuration phase.</p>
<p>I get this output:</p>
<ul>
<li>cd qtbase</li>
<li>/home/qt-easy-build/qt-easy-build/qt-everywhere-src-5.10.0/qtbase/configure -top-level -prefix /home/qt-easy-build/qt-easy-build/qt-everywhere-build-5.10.0 -release -opensource -confirm-license -c++std c++11 -nomake examples -nomake tests -silent -openssl -I /home/qt-easy-build/qt-easy-build/qt-everywhere-deps-5.10.0/openssl-1.0.2n/include -L /home/qt-easy-build/qt-easy-build/qt-everywhere-deps-5.10.0/openssl-1.0.2n<br>
Creating qmake…<br>
.Done.<br>
<strong>Could not find qmake configuration file .</strong><br>
Error processing project file: /home/qt-easy-build/qt-easy-build/qt-everywhere-src-5.10.0</li>
</ul>
<p>any idea which configuration file is missing and where to place it?</p>

---
