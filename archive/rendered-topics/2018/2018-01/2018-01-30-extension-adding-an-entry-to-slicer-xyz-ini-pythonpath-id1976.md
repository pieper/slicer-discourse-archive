# Extension adding an entry to Slicer-XYZ.ini [PYTHONPATH]

**Topic ID**: 1976
**Date**: 2018-01-30
**URL**: https://discourse.slicer.org/t/extension-adding-an-entry-to-slicer-xyz-ini-pythonpath/1976

---

## Post #1 by @adamrankin (2018-01-30 16:18 UTC)

<p>Hello,</p>
<p>SlicerOpenCV currently installed cv2.pyd to the root directory, and currently <code>import cv2</code> fails. A fix to this is to install it to the qt-scripted-modules folder, but I was wondering if there was any interest in adding the ability for an extension to add entries to the Slicer-XYZ.ini sections?</p>
<p>For example, the extension could add a path entry to the [PYTHONPATH] section.</p>
<p>Thoughts?<br>
Adam</p>
<p>code of interest:<br>
<a href="http://qSlicerExtensionsManagerModelPrivate::addExtensionPathToLauncherSettings" rel="nofollow noopener">qSlicerExtensionsManagerModelPrivate::addExtensionPathToLauncherSettings</a><br>
<a href="https://github.com/Slicer/Slicer/blob/master/Base/QTCore/qSlicerExtensionsManagerModel.cxx#L737" rel="nofollow noopener">qSlicerExtensionsManagerModelPrivate::extensionPythonPaths</a></p>

---

## Post #2 by @adamrankin (2018-01-30 16:33 UTC)

<p>Alternately, an extension could do this manually in a module’s init function, accessing the qSlicerExtensionsModelManager functionality.</p>
<p>Edit: uninstalling the extension wouldn’t remove the entry though, so this is sub-optimal.</p>

---

## Post #3 by @lassoan (2018-01-30 17:12 UTC)

<p>Any scripted module that calls <code>import cv2</code> could add the dll’s path to Python paths, but this, too, would be just a workaround.</p>
<p>For me, the main question is:</p>
<ul>
<li>why cv2.pyd is installed into <code>26876-win-amd64-SlicerOpenCV-git8ea8ff1-2018-01-29\lib\Slicer-4.9\cv2.pyd</code> instead of in a scripted module directory? (scripted module directories are already added to PYTHONPATH section)</li>
<li>if cv2.pyd current location is preferable for some reason, then why not add that location to PYTHONPATH section as well?</li>
</ul>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Could you comment on these?</p>

---

## Post #4 by @adamrankin (2018-01-30 17:30 UTC)

<p>Not a perfect answer to your first point, but the extension packaging would have to assume that the directory is “qt-scripted-modules”. Probably a reasonable assumption, but if the scripted directory ever changed, the extension would break (extremely unlikely scenario, I agree).</p>
<p>At the moment, point two is not possible, and was the goal of this discussion.</p>

---

## Post #5 by @adamrankin (2018-01-30 17:31 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/nicole_aucoin">@Nicole_Aucoin</a> any thoughts?</p>

---

## Post #6 by @Nicole_Aucoin (2018-01-30 17:55 UTC)

<p>I recall working with <a class="mention" href="/u/jcfr">@jcfr</a> on this problem during OpenCV integration and I think that this bug was the reason why the opencv library was installed where it was. I can’t dig up the details though.</p>
<p>Nicole</p>

---

## Post #7 by @fedorov (2018-01-30 18:03 UTC)

<p>Adam, I don’t have answers to your questions. But to me it seems suboptimal to modify those variables from the module code.</p>

---

## Post #8 by @adamrankin (2018-01-30 18:08 UTC)

<p>The alternative is installing cv2.pyd to qt-scripted-modules.</p>
<p>Edit: or implementing a system for extensions to install/uninstall entries to the settings file.</p>

---

## Post #9 by @ihnorton (2018-01-30 18:25 UTC)

<aside class="quote no-group" data-username="adamrankin" data-post="8" data-topic="1976">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamrankin/48/155_2.png" class="avatar"> adamrankin:</div>
<blockquote>
<p>or implementing a system for extensions to install/uninstall entries to the settings file.</p>
</blockquote>
</aside>
<p>Maybe it could be simpler to have settings aggregated from a folder: Slicer.(app,exe) would look in that folder and append search settings from all the .ini files contained within. I think this would mesh well with the extension manager, and could also make local developer workflow nicer: just symlink .ini files into the aggregate folder from local extension build trees.</p>

---

## Post #10 by @Nicole_Aucoin (2018-01-30 18:33 UTC)

<p>Here’s the commit where I talked about trying to get python wrapping and importing to work:</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/SlicerOpenCV/commit/fdf1dde83d60b721273f486df0f227b5005f7dff">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerOpenCV/commit/fdf1dde83d60b721273f486df0f227b5005f7dff" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/SlicerOpenCV</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/SlicerOpenCV/commit/fdf1dde83d60b721273f486df0f227b5005f7dff" target="_blank" rel="noopener nofollow ugc">ENH: Add python wrapping to OpenCV</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2016-09-13" data-time="14:17:31" data-timezone="UTC">02:17PM - 13 Sep 16 UTC</span>
      </div>

      <div class="user">
        <a href="" rel="noopener">
          <img alt="" src="" class="onebox-avatar-inline" width="20" height="20">
          
        </a>
      </div>

      <div class="lines" title="changed 5 files with 372 additions and 3 deletions">
        <a href="https://github.com/Slicer/SlicerOpenCV/commit/fdf1dde83d60b721273f486df0f227b5005f7dff" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+372</span>
          <span class="removed">-3</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Turn on wrapping OpenCV in python.
This produces the cv2.so python package that <span class="show-more-container"><a href="https://github.com/Slicer/SlicerOpenCV/commit/fdf1dde83d60b721273f486df0f227b5005f7dff" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">can be imported.

Use the OpenCV CMake var -DPYTHON2_PACKAGES_PATH to specify that the
OpenCV python package needs to be installed in the third party library directory,
it will be found there by changes made to the AdditionalLauncherSettings.ini file
in Slicer svn 25305. To get packaged, it has to be in the Slicer third party
library install directory.

Adapted the opencv python example that computes the histogram of an input image to provide a self test.
Uploaded a copy of one of the Slicer Pathology sample slices to midas and download it for this test.

Don't install the ctest command line test on windows as it's not finding the python wrapped
library when the test is run from the build directory. It still runs from the Testing module
gui.

Issue #12</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It referenced:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/NA-MIC/viewvc.slicer.org?view=revision&amp;revision=25305">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/NA-MIC/viewvc.slicer.org?view=revision&amp;revision=25305" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/23cfae1b943a8f56e3378ea412201cab61d1ff80bc95a8c5ade3770b94c1ea29/NA-MIC/viewvc.slicer.org" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/NA-MIC/viewvc.slicer.org?view=revision&amp;revision=25305" target="_blank" rel="noopener nofollow ugc">GitHub - NA-MIC/viewvc.slicer.org: Documents where source code originally...</a></h3>

  <p>Documents where source code originally available at viewvc.slicer.org has been archived. - GitHub - NA-MIC/viewvc.slicer.org: Documents where source code originally available at viewvc.slicer.org h...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @fedorov (2018-01-30 21:21 UTC)

<p>Thanks <a class="mention" href="/u/nicole_aucoin">@Nicole_Aucoin</a>! I added those pointers to the issue.</p>

---

## Post #12 by @jcfr (2018-01-31 04:14 UTC)

<p>Since <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=25959">r25959</a>  introduced in April 2017, extension can already package python modules and packages using <code>PYTHON_SITE_PACKAGES_SUBDIR</code> CMake variable to specify the install destination.</p>
<p>The packages found in this sub directory will be importable.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/5d294412119bf51f14c3a19ec98f055c1cbe30fe/Base/QTCore/qSlicerExtensionsManagerModel.cxx#L735-L751" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/5d294412119bf51f14c3a19ec98f055c1cbe30fe/Base/QTCore/qSlicerExtensionsManagerModel.cxx#L735-L751" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/5d294412119bf51f14c3a19ec98f055c1cbe30fe/Base/QTCore/qSlicerExtensionsManagerModel.cxx#L735-L751</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="735" style="counter-reset: li-counter 734 ;">
<li>#ifdef Slicer_USE_PYTHONQT</li>
<li>// --------------------------------------------------------------------------</li>
<li>QStringList qSlicerExtensionsManagerModelPrivate::extensionPythonPaths(const QString&amp; extensionName)const</li>
<li>{</li>
<li>Q_Q(const qSlicerExtensionsManagerModel);</li>
<li>if (this-&gt;SlicerVersion.isEmpty())</li>
<li>  {</li>
<li>  return QStringList();</li>
<li>  }</li>
<li>QString path = q-&gt;extensionInstallPath(extensionName);</li>
<li>return appendToPathList(QStringList(), QStringList()</li>
<li>                        &lt;&lt; path + "/" + QString(Slicer_QTSCRIPTEDMODULES_LIB_DIR).replace(Slicer_VERSION, this-&gt;SlicerVersion)</li>
<li>                        &lt;&lt; path + "/" + QString(Slicer_QTLOADABLEMODULES_PYTHON_LIB_DIR).replace(Slicer_VERSION, this-&gt;SlicerVersion)</li>
<li>                        &lt;&lt; path + "/" + QString(PYTHON_SITE_PACKAGES_SUBDIR)</li>
<li>                        );</li>
<li>}</li>
<li>#endif</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I suggest to change this line:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SBU-BMI/SlicerOpenCV/blob/74e0f836bdc284e3b73e541c8d770808ccadec55/SuperBuild/External_OpenCV.cmake#L103" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SBU-BMI/SlicerOpenCV/blob/74e0f836bdc284e3b73e541c8d770808ccadec55/SuperBuild/External_OpenCV.cmake#L103" target="_blank" rel="nofollow noopener">SBU-BMI/SlicerOpenCV/blob/74e0f836bdc284e3b73e541c8d770808ccadec55/SuperBuild/External_OpenCV.cmake#L103</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="93" style="counter-reset: li-counter 92 ;">
<li>    -DWITH_OPENCL:BOOL=OFF</li>
<li>    # Disable find_package(Java) so that java wrapping is not done</li>
<li>    -DCMAKE_DISABLE_FIND_PACKAGE_JAVA:BOOL=ON</li>
<li>    # Add Python wrapping, use Slicer's python</li>
<li>    -DBUILD_opencv_python2:BOOL=ON</li>
<li>    -DPYTHON_EXECUTABLE:FILEPATH=${PYTHON_EXECUTABLE}</li>
<li>    -DPYTHON_INCLUDE_DIR:PATH=${PYTHON_INCLUDE_DIR}</li>
<li>    -DPYTHON_LIBRARY:FILEPATH=${PYTHON_LIBRARY}</li>
<li>    -DINSTALL_PYTHON_EXAMPLES:BOOL=OFF</li>
<li>    # install the python package in the third party lib dir</li>
<li class="selected">    -DPYTHON2_PACKAGES_PATH:PATH=${Slicer_INSTALL_THIRDPARTY_LIB_DIR}</li>
<li>	  ${ADDITIONAL_OPENCV_ARGS}</li>
<li>  DEPENDS</li>
<li>    ${${proj}_DEPENDENCIES}</li>
<li>  )</li>
<li>set(OpenCV_DIR ${${proj}_INSTALL_DIR})</li>
<li>if(UNIX)</li>
<li>  set(OpenCV_DIR ${${proj}_INSTALL_DIR}/share/OpenCV)</li>
<li>endif()</li>
<li>else()</li>
<li># The project is provided using OpenCV_DIR, nevertheless since other projects</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #13 by @fedorov (2018-01-31 22:39 UTC)

<p>Thank you <a class="mention" href="/u/jcfr">@jcfr</a> for the suggestion, and <a class="mention" href="/u/adamrankin">@adamrankin</a> for the PR!</p>
<p>The fix is now merged in <a href="https://github.com/SBU-BMI/SlicerOpenCV/pull/50">https://github.com/SBU-BMI/SlicerOpenCV/pull/50</a>. We shall see, tomorrow.</p>

---

## Post #14 by @fedorov (2018-02-19 18:14 UTC)

<p>As a followup, the suggestion above was implemented, but did not fix the <code>import cv2</code> issue.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SBU-BMI/SlicerOpenCV/blob/master/SuperBuild/External_OpenCV.cmake#L103" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SBU-BMI/SlicerOpenCV/blob/master/SuperBuild/External_OpenCV.cmake#L103" target="_blank" rel="nofollow noopener">SBU-BMI/SlicerOpenCV/blob/master/SuperBuild/External_OpenCV.cmake#L103</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="93" style="counter-reset: li-counter 92 ;">
<li>    -DWITH_OPENCL:BOOL=OFF</li>
<li>    # Disable find_package(Java) so that java wrapping is not done</li>
<li>    -DCMAKE_DISABLE_FIND_PACKAGE_JAVA:BOOL=ON</li>
<li>    # Add Python wrapping, use Slicer's python</li>
<li>    -DBUILD_opencv_python2:BOOL=ON</li>
<li>    -DPYTHON_EXECUTABLE:FILEPATH=${PYTHON_EXECUTABLE}</li>
<li>    -DPYTHON_INCLUDE_DIR:PATH=${PYTHON_INCLUDE_DIR}</li>
<li>    -DPYTHON_LIBRARY:FILEPATH=${PYTHON_LIBRARY}</li>
<li>    -DINSTALL_PYTHON_EXAMPLES:BOOL=OFF</li>
<li>    # install the python package in the third party lib dir</li>
<li class="selected">    -DPYTHON2_PACKAGES_PATH:PATH=${PYTHON_SITE_PACKAGES_SUBDIR}</li>
<li>    ${ADDITIONAL_OPENCV_ARGS}</li>
<li>  DEPENDS</li>
<li>    ${${proj}_DEPENDENCIES}</li>
<li>  )</li>
<li>set(OpenCV_DIR ${${proj}_INSTALL_DIR})</li>
<li>if(UNIX)</li>
<li>  set(OpenCV_DIR ${${proj}_INSTALL_DIR}/share/OpenCV)</li>
<li>endif()</li>
<li>else()</li>
<li># The project is provided using OpenCV_DIR, nevertheless since other projects</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #15 by @lassoan (2018-02-19 23:05 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="14" data-topic="1976">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>did not fix the import cv2 issue.</p>
</blockquote>
</aside>
<p>What did you do exactly?</p>
<p>Do you create an extension package and install it or you run from the build tree? If you run from the build tree: did you specify the additional launcher settings ini file on the command line when you started Slicer?</p>

---

## Post #16 by @fedorov (2018-02-19 23:21 UTC)

<blockquote>
<p>What did you do exactly?</p>
</blockquote>
<p>I downloaded the nightly package, installed SlicerOpenCV extension, and did <code>import cv2</code> in the python console.</p>

---

## Post #17 by @lassoan (2018-02-20 01:16 UTC)

<p><code>import cv2</code> works well on Windows (latest nightly).</p>
<p>Do you have this problem on Mac? Maybe it’s the same Apple SIP policy issue that plagues so many other things - see for example <a href="https://discourse.slicer.org/t/tutorial-for-using-pyradiomics-no-module-named-collections/2111/7">Tutorial for using pyradiomics, no module named _collections</a>.</p>

---

## Post #18 by @fedorov (2018-02-20 04:11 UTC)

<p>Yes, I tested on mac</p>

---
