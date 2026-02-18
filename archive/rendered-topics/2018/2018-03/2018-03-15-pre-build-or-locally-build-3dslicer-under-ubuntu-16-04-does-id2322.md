# Pre-build or Locally-build 3dSlicer under Ubuntu 16.04 does NOT start: Failed to obtain launcher executable name!

**Topic ID**: 2322
**Date**: 2018-03-15
**URL**: https://discourse.slicer.org/t/pre-build-or-locally-build-3dslicer-under-ubuntu-16-04-does-not-start-failed-to-obtain-launcher-executable-name/2322

---

## Post #1 by @MGM (2018-03-15 11:44 UTC)

<p>Hi everyone,</p>
<p>I tried to build 3dSlicer under Ubuntu 16.04, following all steps <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="noopener nofollow ugc">here</a><br>
But, still can’t find how to run it ?</p>
<p>Please, anyone, have a simple instruction to make it running?</p>
<p>Thanks</p>

---

## Post #2 by @brhoom (2018-03-15 12:35 UTC)

<p>If the build was successfull:</p>
<p>your_slicer_build_folder_path/Slicer-build/Slicer</p>
<p>If you just want to run and use slicer, no need to build from the source, using the binary for ubuntu is much simpler.</p>

---

## Post #3 by @MGM (2018-03-15 15:16 UTC)

<p>Hi brhoom,</p>
<p>Thank you for your reply.<br>
In fact, I tried with binary with “/Slicer-4.8.1-linux-amd64”<br>
I got " error: Failed to obtain launcher executable name !"</p>
<p>What do you think ?</p>
<p>Thanks</p>

---

## Post #4 by @brhoom (2018-03-15 15:31 UTC)

<p>Try this:</p>
<ul>
<li>right click on the Slicer file</li>
<li>switch to Permissions tab</li>
<li>check the “Allow execution file as program”</li>
</ul>

---

## Post #5 by @MGM (2018-03-15 15:53 UTC)

<p>yes, I verified<br>
already checked</p>

---

## Post #6 by @jcfr (2018-03-15 16:57 UTC)

<p><s>Hi brhoom, </s> Hi <a class="mention" href="/u/mgm">@MGM</a>,</p>
<p>Let’s check that the folder contain all the expected files.</p>
<p>Can you run the following command and check that you get <code>6541</code> as an answer:</p>
<pre><code class="lang-auto">$ cd Slicer-4.8.1-linux-amd64
$ find . | wc -l
6541
</code></pre>

---

## Post #7 by @brhoom (2018-03-15 18:18 UTC)

<p>So you have the same error in both the binary and the build version?</p>
<p>there are similar related problems. Try redownloading both stable and nightly binaries and check if you still get the same error in both of them.</p>
<p>If it does not work, probably something wrong with your system.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a>: I am not the one who has the problem. BTW, There are people who reported similar problem<br>
<a href="http://slicer-devel-archive.65872.n3.nabble.com/Windows-Built-but-gives-following-error-on-execution-td4034740.html" class="onebox" target="_blank" rel="noopener nofollow ugc">http://slicer-devel-archive.65872.n3.nabble.com/Windows-Built-but-gives-following-error-on-execution-td4034740.html</a></p>
<aside class="quote" data-post="1" data-topic="1707">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/839c29/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-open-slicer-in-linux-ubuntu-command-line/1707">how to open slicer in linux ubuntu command line</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I downloaded Slicer-4.8.0-linux-amd64 on my linux ubuntu system, when I tried to open slicer, I first cd to Slicer-4.8.0-linux-amd64 folder, and typed ./Slicer in terminal. It said “error: Failed to obtain launcher executable name !” 
What should I do? I also tried double-click the Slicer file, it still wouldn’t open. 
Thanks. 
Meina
  </blockquote>
</aside>


---

## Post #8 by @jcfr (2018-03-15 19:23 UTC)

<p>The error message indicates that the following code path (associated with the function <code>ctkAppLauncherPrivate::extractLauncherNameAndDir</code>) is executed in the launcher:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/AppLauncher/blob/48b4ae63168e3930e7a4d48da705c27c557e5564/Base/ctkAppLauncher.cpp#L382-L387" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/AppLauncher/blob/48b4ae63168e3930e7a4d48da705c27c557e5564/Base/ctkAppLauncher.cpp#L382-L387" target="_blank" rel="nofollow noopener">commontk/AppLauncher/blob/48b4ae63168e3930e7a4d48da705c27c557e5564/Base/ctkAppLauncher.cpp#L382-L387</a></h4>
<pre class="onebox"><code class="lang-cpp"><ol class="start lines" start="382" style="counter-reset: li-counter 381 ;">
<li>// Make sure the obtained target exists and is a "file"</li>
<li>if (!fileInfo.exists() &amp;&amp; !fileInfo.isFile())</li>
<li>  {</li>
<li>  this-&gt;reportError("Failed to obtain launcher executable name !");</li>
<li>  return false;</li>
<li>  }</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>The input to that function is obtained here using <code>argv[0]</code>:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/AppLauncher/blob/48b4ae63168e3930e7a4d48da705c27c557e5564/Main.cpp#L72-L78" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/AppLauncher/blob/48b4ae63168e3930e7a4d48da705c27c557e5564/Main.cpp#L72-L78" target="_blank" rel="nofollow noopener">commontk/AppLauncher/blob/48b4ae63168e3930e7a4d48da705c27c557e5564/Main.cpp#L72-L78</a></h4>
<pre class="onebox"><code class="lang-cpp"><ol class="start lines" start="72" style="counter-reset: li-counter 71 ;">
<li>QFileInfo launcherFile(QDir::current(), QString(argv[0]));</li>
<li>// Initialize resources in static libs</li>
<li>Q_INIT_RESOURCE(CTKAppLauncherBase);</li>
<li>
</li>
<li>QScopedPointer&lt;ctkAppLauncher&gt; appLauncher(new ctkAppLauncher);</li>
<li>appLauncher-&gt;setArguments(appArguments.arguments());</li>
<li>if (!appLauncher-&gt;initialize(launcherFile.absoluteFilePath()))</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I suspect that on newer Ubuntu, the path the program needs to be obtained from <code>/proc</code> as it is done in qapplication:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/qt/qtbase/blob/17b73b0d2b8e0d643bdf13b543cc23d657a4b330/src/corelib/kernel/qcoreapplication.cpp#L2259-L2266" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/qt/qtbase/blob/17b73b0d2b8e0d643bdf13b543cc23d657a4b330/src/corelib/kernel/qcoreapplication.cpp#L2259-L2266" target="_blank" rel="nofollow noopener">qt/qtbase/blob/17b73b0d2b8e0d643bdf13b543cc23d657a4b330/src/corelib/kernel/qcoreapplication.cpp#L2259-L2266</a></h4>
<pre class="onebox"><code class="lang-cpp"><ol class="start lines" start="2259" style="counter-reset: li-counter 2258 ;">
<li>#  if defined(Q_OS_LINUX) &amp;&amp; (!defined(Q_OS_ANDROID) || defined(Q_OS_ANDROID_EMBEDDED))</li>
<li>// Try looking for a /proc/&lt;pid&gt;/exe symlink first which points to</li>
<li>// the absolute path of the executable</li>
<li>QFileInfo pfi(QString::fromLatin1("/proc/%1/exe").arg(getpid()));</li>
<li>if (pfi.exists() &amp;&amp; pfi.isSymLink()) {</li>
<li>    QCoreApplicationPrivate::setApplicationFilePath(pfi.canonicalFilePath());</li>
<li>    return *QCoreApplicationPrivate::cachedApplicationFilePath;</li>
<li>}</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Few days ago, within Slicer itself (and not the launcher) the needed a function allowing to get the path of the application on all platforms before instantiating the application … but decided to implement a workaround in <a>27030</a></p>
<p>Look like the time has come to have such a function.</p>

---

## Post #9 by @MGM (2018-03-16 08:19 UTC)

<p>Hi <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>yes, 6541 <img src="https://emoji.discourse-cdn.com/twitter/ok_hand.png?v=5" title=":ok_hand:" class="emoji" alt=":ok_hand:"></p>

---

## Post #10 by @MGM (2018-03-16 08:44 UTC)

<p>Hi <a class="mention" href="/u/jcfr">@jcfr</a> and <a class="mention" href="/u/brhoom">@brhoom</a></p>
<p>Same issue with 4.9.0 Nightly Build</p>
<blockquote>
<p>~/Slicer-4.9.0-2018-02-08-linux-amd64$ find . | wc -l<br>
6534<br>
~/Slicer-4.9.0-2018-02-08-linux-amd64$ sudo apt-get update<br>
~/Slicer-4.9.0-2018-02-08-linux-amd64$ ./Slicer<br>
error: Failed to obtain launcher executable name !</p>
</blockquote>
<p>I tried with an old release :</p>
<blockquote>
<p>~/Slicer-4.8.0-linux-amd64$ find . | wc -l<br>
6541<br>
~/Slicer-4.8.0-linux-amd64$ ./Slicer<br>
error: Failed to obtain launcher executable name !</p>
</blockquote>
<p>My system works fine with others software.</p>

---

## Post #11 by @MGM (2018-04-27 08:09 UTC)

<p>Hi,</p>
<p>I finally find a solution, but only with Slicer 4.8.1 release, thanks to <a class="mention" href="/u/brhoom">@brhoom</a><br>
please refer to this topic, if you meet a similar issue</p>
<aside class="quote" data-post="9" data-topic="2694">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ebca7d/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/cant-launch-slicer-on-linux/2694/9">Can't launch Slicer on Linux - failed to obtain launcher executable name</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I placed in ~/Software/Slicer
  </blockquote>
</aside>


---
