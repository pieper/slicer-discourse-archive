# "QOpenGLWidget: Failed to create context" and "composeAndFlush: QOpenGLContext creation failed" and "composeAndFlush: makeCurrent() failed"

**Topic ID**: 12327
**Date**: 2020-07-01
**URL**: https://discourse.slicer.org/t/qopenglwidget-failed-to-create-context-and-composeandflush-qopenglcontext-creation-failed-and-composeandflush-makecurrent-failed/12327

---

## Post #1 by @Lee_Newberg (2020-07-01 19:02 UTC)

<p>I can run Slicer if I download binaries, but when I try to build from sources and then run it, I am getting errors.  Any thoughts on what I should do differently?  I get these errors whether I build using Qt-5.12.9 or Qt-5.15.0.  I am using ITK current sources from github.  The output I get is:</p>
<pre><code>Switch to module:  "Welcome"
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
composeAndFlush: QOpenGLContext creation failed
composeAndFlush: makeCurrent() failed
</code></pre>
<p>… with that last one repeated ad infinitum – I gave up after more than 10^6 occurrences.</p>

---

## Post #2 by @lassoan (2020-07-02 13:48 UTC)

<aside class="quote no-group" data-username="Lee_Newberg" data-post="1" data-topic="12327">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lee_newberg/48/7615_2.png" class="avatar"> Lee_Newberg:</div>
<blockquote>
<p>I am using ITK current sources from github.</p>
</blockquote>
</aside>
<p>Do you mean you are using <em>Slicer</em> current source (latest master version) from github?<br>
Does Slicer start at all?<br>
Could you copy here your application log (menu: Help / Report a bug)?<br>
What operating system do you use?<br>
Are you using a physical computer directly (or some virtual machine or a physical computer via remote desktop)?<br>
Does it make any difference if you build a package, install it, and run it?</p>

---

## Post #3 by @Lee_Newberg (2020-07-02 14:28 UTC)

<p>Thank you for your response.  I am still stuck.  <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"></p>
<p>I am using the latest ITK sources (master branch) from github and setting the SHELL environment variable ITK_DIR to the build directory for that.  I am also using the latest Slicer sources (master branch) from github.</p>
<p>Slicer puts up a box to show that it is starting, which then goes away.  Then it puts up a box to show that it is loading things, which then goes away.  Then it starts to draw what I assume is to be the Slicer scene, but it gets only as far as an outline, and the error messages begin.  I do not get menus such as the “Help” menu.</p>
<p>I am using Ubuntu 20.04 with the very latest patches.  I am running on my physical laptop.  Unfortunately, I do not know what you mean by “package” in “build a package, install it, and run it”.  Are you talking about an add on for Slicer? – not sure how that is relevant.</p>
<p>I tried yet another version of Qt, this time Qt-5.11.3.  If I try to launch Qt apps (regardless of Slicer) I get errors.  I did not try this with the other versions of Qt, but these errors could be relevant:</p>
<pre><code>qSetGlobalQHashSeed: forced seed value is not 0, cannot guarantee that the hashing functions will produce a stable value.qt3ds.trace_info: Studio:  "/home/lee.newberg/Qt-5.11.3/Tools/Qt3DStudio/bin/Qt3DStudio"
qt3ds.trace_info: Version:  "2.7.0"

Unable to select suitable OpenGL context
Warning: No factory found for device 'WebAssembly Device' of type 'WebAssemblyDeviceType'.
Warning: Unable to restore Qt version 'Qt4ProjectManager.QtVersion.WebAssembly' stored in /home/lee.newberg/.config/QtProject/qtcreator/qtversion.xml.

Errors at startup:

    QmlDesigner

        Plugin initialization failed: Cannot create OpenGL context.

    QmlProfiler

        Plugin initialization failed: Cannot create OpenGL context.

    QtCreator starts but says:

        /usr/lib/jvm/java-8-openjdk-amd64/

        Java settings have errors.

       JDK path not is a valid JDK root folder</code></pre>

---

## Post #4 by @Lee_Newberg (2020-07-02 14:34 UTC)

<p>Would it help if, instead of using a fresh download of a Qt-5 version, I instead use the Qt5 directory from the Slicer binaries download: Slicer-4.11.0-2020-06-17-linux-amd64/lib/Slicer-4.11/cmake/Qt5</p>
<p>That is, for the Slicer build I could start with<br>
<code>cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DQt5_DIR:PATH=/home/lee.newberg/Support/Slicer-4.11.0-2020-06-17-linux-amd64/lib/Slicer-4.11/cmake/Qt5 ../Slicer</code></p>

---

## Post #5 by @jcfr (2020-07-02 14:55 UTC)

<blockquote>
<p>I do not know what you mean by “package” in “build a package, install it, and run it”.</p>
</blockquote>
<p>I suspect <a class="mention" href="/u/lassoan">@lassoan</a> asked if downloading preview version of Slicer from <a href="https://download.slicer.org">https://download.slicer.org</a> works as expected.</p>
<blockquote>
<p>from github and setting the SHELL environment variable ITK_DIR to the build directory for that</p>
</blockquote>
<p>How did you build ITK ? Is it linked against a different VTK build tree than the one used in Slicer ?</p>
<blockquote>
<p>I instead use the Qt5 directory from the Slicer binaries download</p>
</blockquote>
<p>This will not work, we are not distributing a SDK with the Slicer installer.</p>
<blockquote>
<p><code>qSetGlobalQHashSeed: forced seed value is not 0, cannot guarantee that the hashing functions will produce a stable value.qt3ds.trace_info: Studio:  "/home/lee.newberg/Qt-5.11.3/Tools/Qt3DStudio/bin/Qt3DStudio</code></p>
</blockquote>
<p>Are you using <code>Qt3DStudio</code> in any way ?  I am not sure why this message is showing up.</p>

---

## Post #6 by @Lee_Newberg (2020-07-02 15:14 UTC)

<blockquote>
<p>How did you build ITK ? Is it linked against a different VTK build tree than the one used in Slicer ?</p>
</blockquote>
<p>Almost surely it is using a different tree!  I will try unsetting the ITK_DIR shell environment variable to see if that helps.</p>
<blockquote>
<p>Are you using <code>Qt3DStudio</code> in any way ? I am not sure why this message is showing up.</p>
</blockquote>
<p>No, I have no need for Qt3DStudio.  After the downloader finishes retrieving Qt5, its last step is to ask me if I want to launch Qt3DStudio and other programs.  I let it do that and got the errors.  I mentioned the errors in the hope that they would be useful clues.</p>

---

## Post #7 by @pieper (2020-07-02 15:45 UTC)

<p>Hi <a class="mention" href="/u/lee_newberg">@Lee_Newberg</a> - my suggestion would be to get a working Slicer build using the default config from Slicer master.  Then change the <a href="https://github.com/slicer/slicer/blob/master/SuperBuild/External_ITK.cmake#L31-L41">config</a> to point to the version of ITK you want to test.  This way you know it will be built against Slicer’s VTK.</p>

---

## Post #8 by @Lee_Newberg (2020-07-02 16:51 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a>.  Unfortunately, it is not a new ITK that I want to test, but a new Slicer.  (I shouldn’t have been using ITK_DIR in the first place.)  Hopefully, my build of Slicer master branch (without ITK_DIR set) will work, … and then I can try my Slicer branch.</p>

---

## Post #9 by @lassoan (2020-07-02 16:59 UTC)

<aside class="quote no-group quote-modified" data-username="jcfr" data-post="5" data-topic="12327">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<blockquote>
<p>I do not know what you mean by “package” in “build a package, install it, and run it”.</p>
</blockquote>
<p>I suspect <a class="mention" href="/u/lassoan">@lassoan</a> asked if downloading preview version of Slicer from <a href="https://download.slicer.org">https://download.slicer.org</a> works as expected.</p>
</blockquote>
</aside>
<p>I meant creating a Slicer installation package by building PACKAGE target and installing it (on linux, just unzipping) and trying to use that. To see if any problems are due to differences in the build/install tree.</p>

---

## Post #10 by @Lee_Newberg (2020-07-02 21:17 UTC)

<p>Rebuilding Slicer (master branch) into Slicer-SuperBuild-Debug-5.15.0 (or other Qt5 version) with the ITK_DIR shell environment variable <em><strong>not</strong></em> set (so that Slicer will use whatever ITK it wants rather than my override) nonetheless gives the same errors as above regardless of the Qt-5 version that I use.</p>
<p>I am giving a try with “make package” in the Slicer-build directory.</p>

---

## Post #11 by @jcfr (2020-07-02 21:59 UTC)

<p>Do you have issue running the preview build downloaded from <a href="https://download.slicer.org">https://download.slicer.org</a> ?</p>
<blockquote>
<p>unsetting the ITK_DIR shell environment variable to see if that helps.</p>
</blockquote>
<p>Could you copy here the command you use to configure Slicer ?  (the goal here is to make sure you are building against Qt5 you installed by passing <code>Qt5_DIR</code>?)</p>
<p>Could you share the result of the following command ?</p>
<pre data-code-wrap="bash"><code class="lang-bash">cd /path/to/Slicer-SuperBuild/Slicer-build
cat CMakeCache.txt | grep "^Qt5"
</code></pre>
<blockquote>
<p>Qt3DStudio […]  I let it do that and got the errors. I mentioned the errors in the hope that they would be useful clues.</p>
</blockquote>
<p>Are you saying that that the error you reported above happen during install of Qt or when Slicer is starting up ?</p>

---

## Post #12 by @Lee_Newberg (2020-07-03 01:24 UTC)

<blockquote>
<p>Do you have issue running the preview build downloaded from <a href="https://download.slicer.org" rel="noopener nofollow ugc">https://download.slicer.org</a> ?</p>
</blockquote>
<p>I downloaded <code>Slicer-4.10.2-linux-amd64.tar.gz</code>, unpacked it, and that runs fine.</p>
<blockquote>
<p>Could you copy here the command you use to configure Slicer ? (the goal here is to make sure you are building against Qt5 you installed by passing <code>Qt5_DIR</code> ?)</p>
</blockquote>
<p>Sometimes I delete all <code>*.o</code> files in the <code>~/git/Slicer-SuperBuild-Debug-5.15.0</code> hierarchy before re-running the following.</p>
<pre data-code-wrap="bash"><code class="lang-bash">cd ~/git/Slicer-SuperBuild-Debug-5.15.0
cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DQt5_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5 ../Slicer
make -j12 -k
make
</code></pre>
<blockquote>
<p>cat CMakeCache.txt | grep “^Qt5”</p>
</blockquote>
<pre><code>Qt5Core_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5Core
Qt5DBus_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5DBus
Qt5Designer_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5Designer
Qt5Gui_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5Gui
Qt5Multimedia_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5Multimedia
Qt5Network_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5Network
Qt5OpenGL_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5OpenGL
Qt5Positioning_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5Positioning
Qt5PrintSupport_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5PrintSupport
Qt5QmlModels_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5QmlModels
Qt5Qml_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5Qml
Qt5QuickWidgets_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5QuickWidgets
Qt5Quick_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5Quick
Qt5Script_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5Script
Qt5Sql_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5Sql
Qt5Svg_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5Svg
Qt5Test_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5Test
Qt5UiPlugin_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5UiPlugin
Qt5UiTools_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5UiTools
Qt5WebChannel_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5WebChannel
Qt5WebEngineCore_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5WebEngineCore
Qt5WebEngineWidgets_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5WebEngineWidgets
Qt5WebEngine_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5WebEngine
Qt5Widgets_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5Widgets
Qt5X11Extras_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5X11Extras
Qt5XmlPatterns_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5XmlPatterns
Qt5Xml_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5Xml
Qt5_DIR:PATH=/home/lee.newberg/Support/Qt-5.15.0/5.15.0/gcc_64/lib/cmake/Qt5
</code></pre>
<blockquote>
<p>Are you saying that that the error you reported above happen during install of Qt or when Slicer is starting up ?</p>
</blockquote>
<p>I apologize for the earlier post that had errors from several soures in one post.  The errors I get from running the Slicer that I have built from the master branch are the messages:</p>
<pre><code>Switch to module:  "Welcome"
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
composeAndFlush: QOpenGLContext creation failed
composeAndFlush: makeCurrent() failed
</code></pre>
<p>… where that last one is produced an arbitrarily large number of times.</p>

---

## Post #13 by @jcfr (2020-07-03 04:12 UTC)

<aside class="quote no-group quote-modified" data-username="Lee_Newberg" data-post="12" data-topic="12327">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lee_newberg/48/7615_2.png" class="avatar"> Lee_Newberg:</div>
<blockquote>
<blockquote>
<p>Do you have issue running the preview build downloaded from <a href="https://download.slicer.org">https://download.slicer.org</a> ?</p>
</blockquote>
<p>I downloaded <code>Slicer-4.10.2-linux-amd64.tar.gz</code> , unpacked it, and that runs fine.</p>
</blockquote>
</aside>
<p>Great. What about the <strong>Preview</strong> build?</p>
<p>There are two types of download available, the <em>Stable</em> and the <em>Preview</em>.</p>
<aside class="quote no-group" data-username="Lee_Newberg" data-post="12" data-topic="12327">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lee_newberg/48/7615_2.png" class="avatar"> Lee_Newberg:</div>
<blockquote>
<p>Sometimes I delete all <code>*.o</code> files in the <code>~/git/Slicer-SuperBuild-Debug-5.15.0</code> hierarchy before re-running the following.</p>
</blockquote>
</aside>
<p>While not relevant in this specific example, note that only deleting the <code>*.o</code> wouldn’t be enough if you already configured against a different version of ITK by passing option like  <code>-DITK_DIR:PATH=/path/to/different/ITK-build</code></p>
<p>Also worth noting that setting shell variable like <code>ITK_DIR</code> or generally speaking <code>&lt;proj&gt;_DIR</code> will have no effect.</p>
<aside class="quote no-group" data-username="Lee_Newberg" data-post="12" data-topic="12327">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lee_newberg/48/7615_2.png" class="avatar"> Lee_Newberg:</div>
<blockquote>
<p>I apologize for the earlier post that had errors from several soures in one post. The errors I get from running the Slicer that I have built from the master branch are the messages:</p>
</blockquote>
</aside>
<p>No worry, thanks for taking the time to clarify and for helping us understand what is happening <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=12" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #14 by @pieper (2020-07-03 12:28 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="13" data-topic="12327">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>No worry, thanks for taking the time to clarify and for helping us understand what is happening <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=12" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
</blockquote>
</aside>
<p>+1 to that!</p>
<p>Another note about the build system, in my experience it’s often best to bite the bullet and just <code>rm -rf * </code> in the superbuild directory if I think the configuration is in any way inconsistent.  I know the build process takes forever but it puts you on solid ground for debugging.  Sometimes you can get away with just deleting, say <code>python*</code> or <code>ITK*</code>.</p>

---

## Post #15 by @Lee_Newberg (2020-07-03 14:08 UTC)

<blockquote>
<p>While not relevant in this specific example, note that only deleting the <code>*.o</code> wouldn’t be enough if you already configured against a different version of ITK by passing option like <code>-DITK_DIR:PATH=/path/to/different/ITK-build</code></p>
</blockquote>
<p>I never did set ITK_DIR via the cmake command line so that may not have been an issue after all, despite that I had been setting the shell environment variable ITK_DIR.</p>
<blockquote>
<p>There are two types of download available, the <em>Stable</em> and the <em>Preview</em> .</p>
</blockquote>
<p>Thank you for clarifying that.  The preview build does not work for me.  I went back to the stable build and now that does not work either – which represents a regression for me, as that worked well enough a few weeks ago for me to go through a number of tutorials.</p>
<p>So, my problem does not seem to be a problem with building from 3D Slicer sources, but instead a problem with my general operating system configuration.  I will go back to the general installation pages and getting started pages for 3D Slicer and try to figure out what I need to change on my Ubuntu 20.04 system.</p>

---

## Post #16 by @Lee_Newberg (2020-07-03 14:40 UTC)

<p>It was a very long trek to a very easy destination … rebooting did the trick.  I can now run 3D Slicer stable and preview releases as well as a version built from 3D Slicer sources.</p>

---

## Post #17 by @jcfr (2020-07-03 20:31 UTC)

<aside class="quote no-group" data-username="Lee_Newberg" data-post="15" data-topic="12327">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lee_newberg/48/7615_2.png" class="avatar"> Lee_Newberg:</div>
<blockquote>
<p>I had been setting the shell environment variable ITK_DIR.</p>
</blockquote>
</aside>
<p>Out of curiosity, what was the original motivation behind setting this shell variable ? What led you to do so ?</p>
<p>By better understanding the reasoning, may be we could improve the documentation or message reported at configuration time.</p>

---

## Post #18 by @Lee_Newberg (2020-07-03 21:37 UTC)

<p>I had the setting of the <code>ITK_DIR</code> shell variable in my <code>~/.bashrc</code> because I was concurrently working on an ITK Module and the build for the module needed to know where it could find the base ITK.  At this point, I have pulled the setting of the  variable out of my <code>~/.bashrc</code> file and am setting the variable only in terminal sessions where I am working with the ITK module.</p>

---
