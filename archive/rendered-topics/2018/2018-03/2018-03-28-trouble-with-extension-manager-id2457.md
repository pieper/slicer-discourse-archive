# Trouble with Extension Manager

**Topic ID**: 2457
**Date**: 2018-03-28
**URL**: https://discourse.slicer.org/t/trouble-with-extension-manager/2457

---

## Post #1 by @lsmith (2018-03-28 14:55 UTC)

<p>I just downloaded 4.8.1 on my MacBook to test out the program for our work with DTI and tractography, and when I open the extension manager, it fails to load any of the extensions. It stops around 66% every time. I’ve tried shutting down the program and opening it back up, uninstalling and reinstalling, etc. I even downloaded the nightly build to see if it would work, and while it said it had loaded to 100%, no extensions would show up. Any suggestions?</p>

---

## Post #2 by @ihnorton (2018-03-28 14:57 UTC)

<p>Do you know if you are behind a firewall? Please try accessing this address in your web browser:</p>
<p><a href="https://slicer.kitware.com/midas3/slicerappstore" class="onebox" target="_blank">https://slicer.kitware.com/midas3/slicerappstore</a></p>

---

## Post #3 by @lsmith (2018-03-28 14:59 UTC)

<p>Yes, I am- that would explain it! I was able to download the extensions I needed from the site you linked. I appreciate your help!</p>

---

## Post #4 by @ihnorton (2018-03-28 15:01 UTC)

<p>Which OS? In principle we should be able to respect OS proxy settings in the extension manager, but we may not do it on all platforms right now.</p>

---

## Post #5 by @lsmith (2018-03-28 15:02 UTC)

<p>Right now I’m on OS Sierra 10.12.6</p>

---

## Post #6 by @Steve_W (2018-04-03 11:11 UTC)

<p>Adding a PROXY option.   I cant add plugins at work due to proxy!.</p>

---

## Post #7 by @ihnorton (2018-04-03 15:40 UTC)

<p>Hi <a class="mention" href="/u/steve_w">@Steve_W</a>, I moved your message over to this thread where there is a similar issue. For now, please see this document:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#How_to_manually_download_an_extension_package.3F" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#How_to_manually_download_an_extension_package.3F</a></p>

---

## Post #8 by @ihnorton (2018-04-03 15:50 UTC)

<p><a class="mention" href="/u/lsmith">@lsmith</a> <a class="mention" href="/u/steve_w">@Steve_W</a> I did a quick test running through a local proxy on my computer (macOS 10.12; Slicer-4.8.1 and Slicer preview/nightly 3/22/18). The proxy was configured with <a href="http://squidman.net/squidman/">SquidMan</a> and enabled in Network Preferences.</p>
<p>The extension manager seems to work correctly (loads the list and installs an extension), and watching the squid access log after starting Slicer, I was able to verify that all traffic (both HTTP and HTTPS) is running through the proxy. So given that the issue can’t be reproduced in a simple way, we will need some debugging on your side… To start, please look at the <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog">error log</a> and terminal, and post any error messages that may be there.</p>

---

## Post #9 by @jcfr (2018-04-04 05:18 UTC)

<p>This is where we configure the proxy settings:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/c30c6be815aa0c3a0fd8c31f6ad9f9ff272df12c/Base/QTCore/qSlicerCoreApplication.cxx#L322-L323" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/c30c6be815aa0c3a0fd8c31f6ad9f9ff272df12c/Base/QTCore/qSlicerCoreApplication.cxx#L322-L323" target="_blank">Slicer/Slicer/blob/c30c6be815aa0c3a0fd8c31f6ad9f9ff272df12c/Base/QTCore/qSlicerCoreApplication.cxx#L322-L323</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="322" style="counter-reset: li-counter 321 ;">
<li>// Set up Slicer to use the system proxy</li>
<li>QNetworkProxyFactory::setUseSystemConfiguration(true);</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>And to learn more about how Qt use the system configuration:</p>
<p>See <a href="https://doc.qt.io/qt-5/qnetworkproxyfactory.html#setUseSystemConfiguration">https://doc.qt.io/qt-5/qnetworkproxyfactory.html#setUseSystemConfiguration</a></p>

---
