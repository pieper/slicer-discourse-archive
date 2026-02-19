---
topic_id: 8120
title: "Test Extension In Docker"
date: 2019-08-21
url: https://discourse.slicer.org/t/8120
---

# Test extension in Docker

**Topic ID**: 8120
**Date**: 2019-08-21
**URL**: https://discourse.slicer.org/t/test-extension-in-docker/8120

---

## Post #1 by @unnmdnwb3 (2019-08-21 12:23 UTC)

<p>Hello everyone,</p>
<p>I’d like to set up a CI-pipeline with <strong>Gitlab CI</strong>, which should enable continuous testing of our extension (in python). However, it’s not quite obvious to me which dependencies I therefore have to integrate. The imports i need from Slicer are basically <code>slicer</code> and <code>qt</code>.</p>
<p>To fasten up the process, I’ve used the docker-image <code>slicer/slicer-build</code> mentioned in <a href="https://discourse.slicer.org/t/slicer-docker-images/508">this thread</a> and described on <a href="https://github.com/thewtex/SlicerDocker" rel="nofollow noopener">github</a>.</p>
<p>However, I still have the following questions:</p>
<ol>
<li>Is it correct that <a href="https://github.com/thewtex/SlicerDocker" rel="nofollow noopener">these images</a> are the <strong>official</strong> slicer docker-images?</li>
<li>Is it correct that they represent the lastest <strong>nightly build</strong>?</li>
<li>What is the <strong>path</strong> I have to add to <code>PYTHONPATH</code>, in order to import these distributions? (I’d have guessed <code>/usr/src/Slicer-build/Slicer-build/bin/Python</code> but I’m not quite sure…)</li>
</ol>
<p>Thank you for any help or suggestions in advance!</p>
<p>Once I have everything in place, I’d like to share it so that others can profit as well.</p>

---

## Post #2 by @jcfr (2019-08-21 12:38 UTC)

<aside class="quote no-group" data-username="unnmdnwb3" data-post="1" data-topic="8120">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/unnmdnwb3/48/4527_2.png" class="avatar"> unnmdnwb3:</div>
<blockquote>
<ul>
<li>Is it correct that <a href="https://github.com/thewtex/SlicerDocker">these images</a> are the <strong>official</strong> slicer docker-images?</li>
</ul>
</blockquote>
</aside>
<p>There are two type of official images:</p>
<ul>
<li>
<p>The  <a href="https://github.com/thewtex/SlicerDocker">slicer/slicer-base</a> image is published daily and only contain the dependencies of Slicer in the form of build trees (VTK, ITK, …). It is used to make sure the changes proposed as Slicer pull request can compile. This image depends on <code>slicer/buildenv-qt5-centos7</code></p>
</li>
<li>
<p>The <a href="https://github.com/Slicer/SlicerBuildEnvironment/#docker-based-environments">slicer/buildenv-*</a> images are used to build Slicer.</p>
</li>
</ul>
<aside class="quote no-group" data-username="unnmdnwb3" data-post="1" data-topic="8120">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/unnmdnwb3/48/4527_2.png" class="avatar"> unnmdnwb3:</div>
<blockquote>
<ul>
<li>Is it correct that they represent the lastest <strong>nightly build</strong> ?</li>
</ul>
</blockquote>
</aside>
<p>yes</p>
<aside class="quote no-group" data-username="unnmdnwb3" data-post="1" data-topic="8120">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/unnmdnwb3/48/4527_2.png" class="avatar"> unnmdnwb3:</div>
<blockquote>
<ul>
<li>What is the <strong>path</strong> I have to add to <code>PYTHONPATH</code> , in order to import these distributions?</li>
</ul>
</blockquote>
</aside>
<p>To clarify, we are not yet publishing an official image that contain Slicer binaries.</p>
<p>To have a usable image for CI, I suggest to build on the following work:</p>
<ul>
<li>
<p>from <a class="mention" href="/u/ihnorton">@ihnorton</a>: <a href="https://github.com/ihnorton/dockerfiles/tree/master/slicer2binder" class="inline-onebox">dockerfiles/slicer2binder at master · ihnorton/dockerfiles · GitHub</a></p>
</li>
<li>
<p>from <a class="mention" href="/u/pieper">@pieper</a> : <a href="https://github.com/pieper/SlicerDockers/tree/master/slicer" class="inline-onebox">SlicerDockers/slicer at master · pieper/SlicerDockers · GitHub</a></p>
</li>
<li>
<p>from <a class="mention" href="/u/thewtex">@thewtex</a>: <a href="https://github.com/thewtex/docker-opengl/tree/master" class="inline-onebox">GitHub - thewtex/docker-opengl: A docker image that supports rendering graphical applications.</a></p>
</li>
</ul>

---

## Post #3 by @unnmdnwb3 (2019-08-22 11:10 UTC)

<p>Hi <a class="mention" href="/u/jcfr">@jcfr</a>, thanks for your answer!</p>
<p>If I understand you correctly though, <code>slicer/slicer-build</code> should already include the compiled build, right? Since it can also be used for <a href="https://github.com/Slicer/Slicer/blob/master/.circleci/config.yml" rel="nofollow noopener">circle-ci</a>?</p>
<p>I’ve also taken a look into for testing from <strong><a href="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/master/Docker/test.sh#L15" rel="nofollow noopener">SlicerITKUltrasound</a></strong>, which is based on <code>slicer/slicer-base</code>.</p>
<p>The only piece failing for me is <code>import qt</code>. Do you know where I can import <code>qt</code> from?</p>
<p>Thanks in advance!</p>

---

## Post #4 by @unnmdnwb3 (2019-08-22 14:28 UTC)

<p>Short update:</p>
<p>I’ve now built a docker image based on <code>slicer/slicer-build</code>, to which I copy my extension into (also via a container).</p>
<p>Using the <code>cmake</code> command from <a href="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/master/Docker/test.sh#L15" rel="nofollow noopener">SlicerITKUltrasound</a>, I managed to build my extension.</p>
<p>I think the only thing I now need is to set up a <code>CTestTestfile.cmake</code> for my <strong>python tests</strong>, that I have already written and which run trough locally.</p>
<p>Do you agree with my thought process?</p>
<p>Btw. my <code>Dockerfile</code> currently looks like this:</p>
<pre><code class="lang-auto">FROM alpine:latest as base 

RUN apk add git

RUN git clone my_extension

FROM slicer/slicer-build as build

RUN cd /usr/src &amp;&amp; mkdir my_extension-build

COPY --from=base /my_extension /usr/src/my_extension

RUN cd /usr/src/ &amp;&amp; mkdir my_extension-build &amp;&amp; cmake -DSlicer_DIR:PATH=/usr/src/Slicer-build/Slicer-build -DBUILDNAME:STRING=my_extension /usr/src/my_extension

RUN cd MyExtension &amp;&amp; make</code></pre>

---

## Post #5 by @lassoan (2019-08-22 16:15 UTC)

<p>Thanks for the update.</p>
<p>I cannot comment on that if it is correct or optimal (<a class="mention" href="/u/jcfr">@jcfr</a> should give feedback on that), but we should probably use this in our extensions and also add it to our extension template. <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> what do you think?</p>

---

## Post #6 by @pieper (2019-08-22 18:07 UTC)

<p>I don’t think there should be anything special about running in the container - if you build the extension structure using the wizard then all the build and test infrastructure should be set up automatically.  But yes, if there’s a way to build containerized testing infrastructure into the extension template we should.</p>
<p><a class="mention" href="/u/unnmdnwb3">@unnmdnwb3</a> - do you really want to do the cmake/make commands in the <code>RUN</code> statement?  I’d think you’d want this container to be doing the checkout and build in the instance and not in the <code>docker build</code> step.</p>

---

## Post #7 by @lassoan (2019-08-22 18:33 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="8120">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>if there’s a way to build containerized testing infrastructure into the extension template we should.</p>
</blockquote>
</aside>
<p>We could add all the necessary files to the extension template (docker subfolder, travis &amp; circleci configuration files, badges in the readme.md file, etc.). It should be easy if there is a good example to follow.</p>

---

## Post #8 by @unnmdnwb3 (2019-08-23 05:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="8120">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We could add all the necessary files to the extension template (docker subfolder, travis &amp; circleci configuration files, badges in the readme.md file, etc.). It should be easy if there is a good example to follow.</p>
</blockquote>
</aside>
<p>That’s a great idea! Everything that automates testing is awesome. Facilitating the CI could support teams to start using it, which supposedly results in better tested and hence more robust extensions.</p>
<p>I’d be happy to later contribute by <code>Dockerfile</code> and <code>gitlab-ci.yml</code> once everything’s in place - if you’re interested of course. And I could also propose a <code>.travis.yml</code> for those working with Github.</p>
<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="8120">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><a class="mention" href="/u/unnmdnwb3">@unnmdnwb3</a> - do you really want to do the cmake/make commands in the <code>RUN</code> statement? I’d think you’d want this container to be doing the checkout and build in the instance and not in the <code>docker build</code> step.</p>
</blockquote>
</aside>
<p>Thanks for pointing that out. I honestly don’t have a rich experience with <code>cmake</code> and joined the extension project a few days ago. If you advice me to do it differently, I’ll follow your suggestion!</p>

---

## Post #9 by @unnmdnwb3 (2019-08-23 11:29 UTC)

<p>I’ve now managed to get a correct build (as described in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_build_an_extension_.3F" rel="nofollow noopener">wiki</a>) and configuration in my <code>CMakeLists.txt</code>, so that the correct tests are run.</p>
<p>But now I have the following issue:</p>
<pre><code class="lang-auto">3: Test command: /usr/src/Slicer-build/Slicer-build/Slicer "--no-splash" "--testing" "--launcher-additional-settings" "/usr/src/extension-build/AdditionalLauncherSettings.ini" "--additional-module-paths" "/usr/src/extension-build/lib/Slicer-4.9/qt-scripted-modules" "/usr/src/extension-build/lib/Slicer-4.9/cli-modules" "/usr/src/extension-build/lib/Slicer-4.9/qt-loadable-modules" "--python-code" "import slicer.testing; slicer.testing.runUnitTest(['/usr/src/extension-build/Extension', '/usr/src/extension/Extension'], 'extensionTest')"
3: Test timeout computed to be: 1500
3: SlicerApp-real: cannot connect to X server 
3: vtkDebugLeaks has found no leaks.
3/3 Test #3: py_extensionTest ...................................***Failed    0.38 sec
</code></pre>
<p>However, <strong>X11</strong> is installed in <code>/etc/X11</code>…</p>

---

## Post #10 by @pieper (2019-08-23 13:56 UTC)

<p><a class="mention" href="/u/unnmdnwb3">@unnmdnwb3</a>, looks close, but you need to have X up running for slicer to run.</p>
<p>If you look at the X11 example in <a href="https://github.com/pieper/SlicerDockers" rel="nofollow noopener">the SlicerDockers repository</a> you can see how to set this up.  Also in the readme there is an example of running a script inside the instance that uses Slicer and the X server.  This approach could be adapted to run the testing as well, probably using the <a href="https://github.com/thewtex/SlicerDocker" rel="nofollow noopener">build images</a>.</p>
<p>There’s clearly a lot of potential benefit here, but things aren’t really documented or coordinated.  It’ll be good to see a good clean end to end solution.</p>

---

## Post #11 by @unnmdnwb3 (2019-08-27 13:57 UTC)

<p>Short update: I’ve now managed to (mostly) resolve the X issues.</p>
<p>When running <code>ctest -V</code> though, the following error occurs:</p>
<pre><code class="lang-auto">2: Test command: /usr/src/Slicer-build/Slicer-build/Slicer "--no-splash" "--testing" "--launcher-additional-settings" "/usr/src/extension-build/AdditionalLauncherSettings.ini" "--additional-module-paths" "/usr/src/extension-build/lib/Slicer-4.9/qt-scripted-modules" "/usr/src/extension-build/lib/Slicer-4.9/cli-modules" "/usr/src/extension-build/lib/Slicer-4.9/qt-loadable-modules" "--python-code" "import slicer.testing; slicer.testing.runUnitTest(['/usr/src/extension-build/Extension/Logic', '/usr/src/extension/Extension/Logic'], 'DExtensionTest')"
2: Test timeout computed to be: 1500
Could not init font path element unix/:7100, removing from list!
2: Number of registered modules: 101 
2: Traceback (most recent call last):
2:   File "&lt;string&gt;", line 1, in &lt;module&gt;
2:   File "/usr/src/extension-build/lib/Slicer-4.9/qt-scripted-modules/Extension.py", line 15, in &lt;module&gt;
2:     from pathlib import Path
2: ImportError: No module named pathlib
2: loadSourceAsModule - Failed to load file "/usr/src/extension-build/lib/Slicer-4.9/qt-scripted-modules/Extension.py"  as module "Extension" ! 
2: Fail to instantiate module  "Extension" 
2: Number of instantiated modules: 100 
2: Number of loaded modules: 100 
2: Switch to module:  "Welcome" 
2: -------------------------------------------
2: path: ['/usr/src/extension-build/Extension/Logic', '/usr/src/extension/Extension/Logic']
2: testname: ExtensionTest
2: -------------------------------------------
2: Traceback (most recent call last):
2:   File "&lt;string&gt;", line 1, in &lt;module&gt;
2:   File "/usr/src/Slicer-build/Slicer-build/bin/Python/slicer/testing.py", line 22, in runUnitTest
2:     suite = unittest.TestLoader().loadTestsFromName(testname)
2:   File "/usr/src/Slicer-build/python-install/lib/python2.7/unittest/loader.py", line 91, in loadTestsFromName
2:     module = __import__('.'.join(parts_copy))
2:   File "/usr/src/extension/Extension/Logic/ExtensionTest.py", line 3, in &lt;module&gt;
2:     from .ExtensionLogic import *
2: ValueError: Attempted relative import in non-package
2: Switch to module:  "" 
error opening security policy file /usr/lib64/xserver/SecurityPolicy
2: vtkDebugLeaks has found no leaks.
</code></pre>
<p>It seems like a <strong>relative import</strong> is not possible. However the Slicer Python should be <strong>3.+</strong>, right?<br>
Possibly, this is because Slicer is not correctly integrated into the project and uses the default installation?</p>
<pre><code class="lang-auto">which python
&gt; /usr/local/bin/python
</code></pre>
<p>Do you have any insight into this?</p>

---

## Post #12 by @lassoan (2019-08-27 14:03 UTC)

<aside class="quote no-group" data-username="unnmdnwb3" data-post="11" data-topic="8120">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/unnmdnwb3/48/4527_2.png" class="avatar"> unnmdnwb3:</div>
<blockquote>
<p>However the Slicer Python should be <strong>3.+</strong> , right?</p>
</blockquote>
</aside>
<p>Slicer-4.10 and earlier uses Python2. From Slicer-4.11.x Slicer uses Python3.</p>
<aside class="quote no-group" data-username="unnmdnwb3" data-post="11" data-topic="8120">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/unnmdnwb3/48/4527_2.png" class="avatar"> unnmdnwb3:</div>
<blockquote>
<pre><code class="lang-auto">which python
&gt; /usr/local/bin/python
</code></pre>
<p>Do you have any insight into this?</p>
</blockquote>
</aside>
<p>Slicer’s Python executable is called <code>PythonSlicer</code> and not <code>python</code>.</p>

---

## Post #13 by @unnmdnwb3 (2019-08-29 09:22 UTC)

<p>Thank you for the information!</p>
<p>Accordingly to your answer, cloning from <a href="https://github.com/Slicer/Slicer/tree/master" rel="nofollow noopener">https://github.com/Slicer/Slicer/tree/master</a> results in a <code>v4.10.2</code>, which only supports <code>python2</code>. Whereas, pulling from <a href="https://github.com/Slicer/Slicer/tree/nightly-master" rel="nofollow noopener">https://github.com/Slicer/Slicer/tree/nightly-master</a> results in a <code>v4.11.x</code>, which supports <code>python3</code> - right?</p>
<p>And is it correct, that <a href="https://github.com/thewtex/SlicerDocker/tree/master/slicer-base" rel="nofollow noopener">slicer/slicer-base</a> pulls from the <code>master</code> and hence ends up with <code>python2</code>?</p>
<p>I tried to find <code>PythonSlicer</code> (and found it locally on my mac), but wasn’t able to locate it on the <code>slicer/slicer-build</code> image. However, I found a <code>SlicerPython</code> which is an executable as well. Can you elaborate on the difference between them?</p>

---

## Post #14 by @unnmdnwb3 (2019-08-30 07:26 UTC)

<p>Nevermind. I’ve build a docker image, which builds <code>Slicer/Slicer#nightly-build</code> from the <a href="https://github.com/Slicer/Slicer/tree/nightly-master" rel="nofollow noopener">official repo</a>, and can now use <code>python3</code>!</p>

---

## Post #15 by @lassoan (2019-08-30 12:40 UTC)

<aside class="quote no-group" data-username="unnmdnwb3" data-post="13" data-topic="8120">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/unnmdnwb3/48/4527_2.png" class="avatar"> unnmdnwb3:</div>
<blockquote>
<p>tried to find <code>PythonSlicer</code> (and found it locally on my mac), but wasn’t able to locate it on the <code>slicer/slicer-build</code> image. However, I found a <code>SlicerPython</code> which is an executable as well. Can you elaborate on the difference between them?</p>
</blockquote>
</aside>
<p>We renamed “SlicerPython” to “PythonSlicer” , because PyCharm only accepts custom Python interpreter names that start with “python”. We kept “SlicerPython” for backward compatibility for a while, but it will be removed in the future. The two processes do exactly the same.</p>

---
