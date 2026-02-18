# macOS build on the factory failed with "No Java runtime present ... Alarm clock: 14"

**Topic ID**: 2321
**Date**: 2018-03-15
**URL**: https://discourse.slicer.org/t/macos-build-on-the-factory-failed-with-no-java-runtime-present-alarm-clock-14/2321

---

## Post #1 by @jcfr (2018-03-15 06:06 UTC)

<p>The build failed reporting error like the following:</p>
<pre><code class="lang-auto">Unable to find any JVMs matching version "(null)".
No Java runtime present, try --request to install.
Unable to find any JVMs matching version "(null)".
No Java runtime present, try --request to install.
make[6]: *** [all] Alarm clock: 14
make[5]: *** [SimpleITK-prefix/src/SimpleITK-stamp/SimpleITK-build] Error 2
make[4]: *** [CMakeFiles/SimpleITK.dir/all] Error 2
make[3]: *** [all] Error 2
</code></pre>
<p>Short story: This should soon be fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27081">r27081</a></p>
<h4><a name="p-9480-more-details-1" class="anchor" href="#p-9480-more-details-1" aria-label="Heading link"></a>more details …</h4>
<p>It turns out that on macOS, despite of not having Java installed, there are stub executables that all return a message like the following:</p>
<pre><code class="lang-auto">No Java runtime present, requesting install.
</code></pre>
<p>I suspect that a popup dialog asking the user to install java was shown (using a background process) and in that situation … no user clicked and it timed out reporting. This would explain the <code>Alarm clock: 14</code></p>
<p>This was confirm connecting using VNC (instead of SSH):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb3f2f56b431d7c088f33c46150f6351857f6270.png" data-download-href="/uploads/short-url/zQDdwxsZ3cQBCpcIpcdlBjObZCw.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb3f2f56b431d7c088f33c46150f6351857f6270.png" alt="image" data-base62-sha1="zQDdwxsZ3cQBCpcIpcdlBjObZCw" width="308" height="115"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">308×115 15.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I also suspect this is due to the following call in SimpleITK:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SimpleITK/blob/67872f823dc35250fa8a1457a25c64e57fb1245f/CMake/sitkLanguageOptions.cmake#L114-L119">
  <header class="source">

      <a href="https://github.com/Slicer/SimpleITK/blob/67872f823dc35250fa8a1457a25c64e57fb1245f/CMake/sitkLanguageOptions.cmake#L114-L119" target="_blank" rel="noopener">github.com/Slicer/SimpleITK</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SimpleITK/blob/67872f823dc35250fa8a1457a25c64e57fb1245f/CMake/sitkLanguageOptions.cmake#L114-L119" target="_blank" rel="noopener">CMake/sitkLanguageOptions.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/SimpleITK/blob/67872f823dc35250fa8a1457a25c64e57fb1245f/CMake/sitkLanguageOptions.cmake#L114-L119" rel="noopener"><code>67872f823</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="114" style="counter-reset: li-counter 113 ;">
          <li>#-----------------------------------------------------------</li>
          <li># Java</li>
          <li></li>
          <li>set_QUIET( WRAP_JAVA )</li>
          <li>find_package ( Java COMPONENTS Development Runtime ${_QUIET} )</li>
          <li>find_package ( JNI ${_QUIET} )</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Indeed, both  JNI and JAVA CMake modules are doing a call to <code>java_home</code> executable during the configuration process:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Kitware/CMake/blob/07f9f41f503985dbd1fb0a657beadcfee95347e0/Modules/CMakeFindJavaCommon.cmake#L20-L27">
  <header class="source">

      <a href="https://github.com/Kitware/CMake/blob/07f9f41f503985dbd1fb0a657beadcfee95347e0/Modules/CMakeFindJavaCommon.cmake#L20-L27" target="_blank" rel="noopener">github.com/Kitware/CMake</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/CMake/blob/07f9f41f503985dbd1fb0a657beadcfee95347e0/Modules/CMakeFindJavaCommon.cmake#L20-L27" target="_blank" rel="noopener">Modules/CMakeFindJavaCommon.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Kitware/CMake/blob/07f9f41f503985dbd1fb0a657beadcfee95347e0/Modules/CMakeFindJavaCommon.cmake#L20-L27" rel="noopener"><code>07f9f41f5</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="20" style="counter-reset: li-counter 19 ;">
          <li>if(APPLE AND EXISTS /usr/libexec/java_home)</li>
          <li>  execute_process(COMMAND /usr/libexec/java_home</li>
          <li>    OUTPUT_VARIABLE _CMD_JAVA_HOME OUTPUT_STRIP_TRAILING_WHITESPACE)</li>
          <li>endif()</li>
          <li>if(_CMD_JAVA_HOME AND IS_DIRECTORY "${_CMD_JAVA_HOME}")</li>
          <li>  set(_JAVA_HOME "${_CMD_JAVA_HOME}")</li>
          <li>  set(_JAVA_HOME_EXPLICIT 0)</li>
          <li>endif()</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>To avoid call to this executable, I even looked into removing the symlink from <code>/usr/lib</code>, but doesn’t seem possible without restarting the machine (even with root access). See <a href="https://stackoverflow.com/questions/32659348/operation-not-permitted-when-on-root-el-capitan-rootless-disabled#32661637" class="inline-onebox">macos - Operation Not Permitted when on root - El Capitan (rootless disabled) - Stack Overflow</a></p>
<p>To address this for all developers, we will update the SimpleITK external  project to explicitly mark Java and JNI as not found, This can be done using this option: <a href="https://cmake.org/cmake/help/latest/variable/CMAKE_DISABLE_FIND_PACKAGE_PackageName.html#variable:CMAKE_DISABLE_FIND_PACKAGE_%3CPackageName%3E" class="inline-onebox">CMAKE_DISABLE_FIND_PACKAGE_&lt;PackageName&gt; — CMake 4.2.0 Documentation</a></p>
<p>List of executable with stub is the following:</p>
<pre><code class="lang-auto">$ for cmd in $(ls /System/Library/Frameworks/JavaVM.framework/Versions/Current/Commands/); do 
  ($cmd 2&gt;&amp;1 | grep "No Java runtime present" &gt; /dev/null) &amp;&amp; echo $(which $cmd) || true;
done
/usr/bin/appletviewer
/usr/bin/apt
/usr/bin/extcheck
/usr/bin/idlj
/usr/bin/jar
/usr/bin/jarsigner
/usr/bin/java
/usr/bin/javac
/usr/bin/javadoc
/usr/bin/javah
/usr/bin/javap
/usr/bin/jcmd
/usr/bin/jconsole
/usr/bin/jdb
/usr/bin/jdeps
/usr/bin/jhat
/usr/bin/jinfo
/usr/bin/jjs
/usr/bin/jmap
/usr/bin/jmc
/usr/bin/jps
/usr/bin/jrunscript
/usr/bin/jsadebugd
/usr/bin/jstack
/usr/bin/jstat
/usr/bin/jstatd
/usr/bin/jvisualvm
/usr/bin/keytool
/usr/bin/native2ascii
/usr/bin/orbd
/usr/bin/pack200
/usr/bin/policytool
/usr/bin/rmic
/usr/bin/rmid
/usr/bin/rmiregistry
/usr/bin/schemagen
/usr/bin/serialver
/usr/bin/servertool
/usr/bin/tnameserv
/usr/bin/unpack200
/usr/bin/wsgen
/usr/bin/wsimport
/usr/bin/xjc
</code></pre>
<p>And the only one that do not out the message are:</p>
<pre><code class="lang-auto">$ for cmd in $(ls /System/Library/Frameworks/JavaVM.framework/Versions/Current/Commands/); do 
  ($cmd 2&gt;&amp;1 | grep "No Java runtime present" &gt; /dev/null) || echo $(which $cmd);
done

javaws
</code></pre>
<p>and the one that is not in the path is <code>java_home</code> and it outputs:</p>
<pre><code class="lang-auto">Unable to find any JVMs matching version "(null)".
No Java runtime present, try --request to install.
</code></pre>

---

## Post #2 by @jcfr (2018-03-15 08:22 UTC)

<p>After testing locally, that last fix didn’t work out.</p>
<p>A different approach along with a patch to the upstream project was implemented. See <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27082">r27082</a> and <a href="https://github.com/SimpleITK/SimpleITK/pull/424">https://github.com/SimpleITK/SimpleITK/pull/424</a></p>
<p>The build on macOS has been manually re-triggered using the following command:</p>
<pre><code class="lang-auto">run_ctest_with_disable_clean=TRUE \
run_ctest_with_update=FALSE \
/Volumes/Dashboards/DashboardScripts/factory-south-macos.sh &gt; /Volumes/Dashboards/Logs/factory-south-macos.log
</code></pre>
<p>Since this is a nightly build, the existing report on CDash will be updated and any additional errors will be appended to the report.</p>
<p>For reference:</p>
<pre><code class="lang-nohighlight">    COMP: Update SimpleITK to effectively avoid unwanted find_package calls
    
    This commit reverts the approach implemented in the previous commit. It
    failed because SimpleITK has a superbuild structure and the CMAKE_DISABLE_FIND_PACKAGE_*
    options are not propagated down to the inner build.
    
    Instead, a patch improving the handling of SimpleITK wrapping options
    has been proposed to the upstream project (and in the mean time integrated
    in our Slicer fork).
    
    The implemented solution consists in avoiding the call to "find_package()"
    if the corresponding WRAP_&lt;languageName&gt; option has explicitly been set or
    if WRAP_DEFAULT is set to OFF.
    Indeed, there is no need to do these call to find an appropriate default value
    for the option since the user (in this case Slicer build system) explicitly
    set of value of for the options (eiter directly or by setting WRAP_DEFAULT).
    
    See https://github.com/SimpleITK/SimpleITK/pull/424
    
    List of changes:
    
    $ git shortlog 67872f8..7572225 --no-merges
    Jean-Christophe Fillion-Robin (1):
          sitkLanguageOptions: Improve setting of default value for wrap options

</code></pre>

---

## Post #3 by @jcfr (2018-03-16 19:53 UTC)

<p>To follow up on this, by working with the maintainer of SimpleITK (thanks <a class="mention" href="/u/blowekamp">@blowekamp</a>), issue has been addressed in the upstream project:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/SimpleITK/SimpleITK/commit/2d3f1088a00e874669fba99a8c405ff65aab67cf">
  <header class="source">

      <a href="https://github.com/SimpleITK/SimpleITK/commit/2d3f1088a00e874669fba99a8c405ff65aab67cf" target="_blank" rel="noopener">github.com/SimpleITK/SimpleITK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SimpleITK/SimpleITK/commit/2d3f1088a00e874669fba99a8c405ff65aab67cf" target="_blank" rel="noopener">sitkLanguageOptions: Improve setting of default value for wrap options</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2018-03-16" data-time="12:28:58" data-timezone="UTC">12:28PM - 16 Mar 18 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/blowekamp" target="_blank" rel="noopener">
          <img alt="blowekamp" src="https://avatars.githubusercontent.com/u/321061?v=4" class="onebox-avatar-inline" width="20" height="20">
          blowekamp
        </a>
      </div>

      <div class="lines" title="changed 1 files with 138 additions and 78 deletions">
        <a href="https://github.com/SimpleITK/SimpleITK/commit/2d3f1088a00e874669fba99a8c405ff65aab67cf" target="_blank" rel="noopener">
          <span class="added">+138</span>
          <span class="removed">-78</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This commit makes sure no calls to "find_package(&lt;languageName&gt;)" are
done if th<span class="show-more-container"><a href="https://github.com/SimpleITK/SimpleITK/commit/2d3f1088a00e874669fba99a8c405ff65aab67cf" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">e options WRAP_DEFAULT or WRAP_&lt;languageName&gt; is explicitly
set to OFF.

Indeed, systematically calling "find_package()" can have side-effects.
See https://discourse.slicer.org/t/nightly-mac-slicer-4-9-0-2018-03-13-macosx-amd64-does-not-open/23

Co-authored-by: Jean-Christophe Fillion-Robin &lt;jchris.fillionr@kitware.com&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @fausto_milletari (2018-03-18 06:23 UTC)

<p>I have noticed that extension <strong>for stable</strong> are not being build anymore for Mac since a couple of days. Can you confirm this? can this be fixed?</p>
<p>Regards,</p>
<p>Fausto</p>

---

## Post #5 by @jcfr (2018-03-18 07:32 UTC)

<p>Hi <a class="mention" href="/u/fausto_milletari">@fausto_milletari</a>,</p>
<p>It should be back in order. See <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=factory-macos.kitware">http://slicer.cdash.org/index.php?project=Slicer4&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=factory-macos.kitware</a></p>
<p>Also, crontab associated with this build machine is now backed up. See:</p>
<ul>
<li><a href="https://github.com/Slicer/DashboardScripts/blob/master/maintenance/factory-macos/crontab">maintenance/factory-macos/crontab</a></li>
<li>Maintenance Guide: <a href="https://github.com/Slicer/DashboardScripts/blob/master/maintenance/guides/push-pull-crontab-settings.md">push-pull-crontab-settings.md</a>
</li>
</ul>

---

## Post #6 by @fausto_milletari (2018-03-18 09:27 UTC)

<p>now it’s all good. many thanks!</p>

---
