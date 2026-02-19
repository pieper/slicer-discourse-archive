---
topic_id: 18852
title: "Qslicerwebwidget Crash On Slicer Built On Win 10 Pro X64"
date: 2021-07-21
url: https://discourse.slicer.org/t/18852
---

# qSlicerWebWidget crash on Slicer built on Win 10 Pro x64

**Topic ID**: 18852
**Date**: 2021-07-21
**URL**: https://discourse.slicer.org/t/qslicerwebwidget-crash-on-slicer-built-on-win-10-pro-x64/18852

---

## Post #1 by @mau_igna_06 (2021-07-21 12:07 UTC)

<p>Hi. I compiled Slicer from source following the instructions <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" rel="noopener nofollow ugc">here</a> on debug mode.</p>
<p>When I run these lines Slicer crashes:</p>
<pre><code class="lang-auto">ww = slicer.qSlicerWebWidget()
ww.url = 'http://www.google.com'
</code></pre>
<p>Does this mean that the compilation failed at some point? why this happens?<br>
I tried the same code on yesterday’s nightly release and it works fine.</p>
<p>This is the terminal output of the compiled Slicer:</p>
<pre><code class="lang-auto">C:\D\S4D\Slicer-build&gt;Slicer.exe
Switch to module:  "Welcome"
Python console user input: ww = slicer.qSlicerWebWidget()

DevTools listening on ws://127.0.0.1:1337/devtools/browser/a863dc15-a302-4012-b699-e365eb7c133d
Remote debugging server started successfully. Try pointing a Chromium-based browser to http://127.0.0.1:1337
Python console user input: ww.url = 'http://www.google.com'
[19120:18372:0721/091624.512:FATAL:visitedlink_writer.h(496)] Check failed: used_count == used_items_ (80 vs. 68)
Backtrace:
        QWebEngineUrlSchemeHandler::qt_static_metacall [0x00007FFBD06424D2+994866]
        QWebEngineUrlSchemeHandler::qt_static_metacall [0x00007FFBD05D76CC+557100]
        QWebEngineUrlSchemeHandler::qt_static_metacall [0x00007FFBD05D7683+557027]
        QWebEngineUrlSchemeHandler::qt_static_metacall [0x00007FFBD054FFAE+2318]
        GetHandleVerifier [0x00007FFBD06D66E1+383121]
        GetHandleVerifier [0x00007FFBD06D8753+391427]
        GetHandleVerifier [0x00007FFBD06D41DE+373646]
        GetHandleVerifier [0x00007FFBD06D4452+374274]
        GetHandleVerifier [0x00007FFBD06D46DF+374927]
        GetHandleVerifier [0x00007FFBD06D99B6+396134]
        GetHandleVerifier [0x00007FFBD06D97F7+395687]
        GetHandleVerifier [0x00007FFBD06D42E4+373908]
        GetHandleVerifier [0x00007FFBD06D44B3+374371]
        GetHandleVerifier [0x00007FFBD06D4763+375059]
        GetHandleVerifier [0x00007FFBD06D9A0D+396221]
        QtWebEngineCore::WebEngineSettings::setWebContentsAdapter [0x00007FFBCC90E1B0+4096]
        QWebEngineUrlSchemeHandler::qt_static_metacall [0x00007FFBD057D40E+187758]
        GetHandleVerifier [0x00007FFBD069283B+104939]
        GetHandleVerifier [0x00007FFBD0691FC0+102768]
        QWebEngineMessagePumpScheduler::~QWebEngineMessagePumpScheduler [0x00007FFBCC90F120+2448]
        QWebEngineMessagePumpScheduler::~QWebEngineMessagePumpScheduler [0x00007FFBCC90E856+198]
        QtWebEngineCore::WebEngineSettings::setWebContentsAdapter [0x00007FFBCC90E48B+4827]
        QtWebEngineCore::WebEngineSettings::setWebContentsAdapter [0x00007FFBCC90E53B+5003]
        QtWebEngineCore::WebEngineSettings::setWebContentsAdapter [0x00007FFBCC90E4AB+4859]
        QWebEngineMessagePumpScheduler::~QWebEngineMessagePumpScheduler [0x00007FFBCC90EEBA+1834]
        TargetGetStockObject [0x00007FFBCCECA39E+4100990]
        QWebEngineMessagePumpScheduler::timerEvent [0x00007FFBD054AFBC+124]
        QTextStream::realNumberPrecision [0x00007FFC18E44F07+5260042]
        QStyleAnimation::frameRate [0x00007FFC2140F9C7+310563]
        QStyleAnimation::frameRate [0x00007FFC21409C68+286660]
        qSlicerApplication::notify [0x00007FFC22C279CC+76] (C:\D\S4\Base\QTGUI\qSlicerApplication.cxx:412)
        QTextStream::realNumberPrecision [0x00007FFC18DE4AAF+4865714]
        QTextStream::realNumberPrecision [0x00007FFC18DE2B92+4857749]
        QTextStream::realNumberPrecision [0x00007FFC18DE69B3+4873654]
        QTextStream::realNumberPrecision [0x00007FFC18EB9092+5735573]
        qt_plugin_instance [0x00007FFBF41D47F4+1033355]
        QTextStream::realNumberPrecision [0x00007FFC18EB70B2+5727413]
        qt_plugin_instance [0x00007FFBF41D47B4+1033291]
        QTextStream::realNumberPrecision [0x00007FFC18DDF39B+4843422]
        QTextStream::realNumberPrecision [0x00007FFC18DDF604+4844039]
        QTextStream::realNumberPrecision [0x00007FFC18DE2919+4857116]
        QOpenGLFunctions_4_3_Compatibility::glLightModeli [0x00007FFC1E36D648+790560]
        QStyleAnimation::frameRate [0x00007FFC2140972A+285318]
        qSlicerCoreApplication::exec [0x00007FFC2544871B+27] (C:\D\S4\Base\QTCore\qSlicerCoreApplication.cxx:861)
        `anonymous namespace'::SlicerAppMain [0x00007FF7AB4D35A0+896] (C:\D\S4\Applications\SlicerApp\Main.cxx:62)
        main [0x00007FF7AB4D362F+47] (C:\D\S4\Base\QTApp\qSlicerApplicationMainWrapper.cxx:57)
        invoke_main [0x00007FF7AB4DB539+57] (D:\agent\_work\10\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl:79)
        __scrt_common_main_seh [0x00007FF7AB4DB41E+302] (D:\agent\_work\10\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl:288)
        __scrt_common_main [0x00007FF7AB4DB2DE+14] (D:\agent\_work\10\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl:331)
        mainCRTStartup [0x00007FF7AB4DB5CE+14] (D:\agent\_work\10\s\src\vctools\crt\vcstartup\src\startup\exe_main.cpp:17)
        BaseThreadInitThunk [0x00007FFC5FE17034+20]
        RtlUserThreadStart [0x00007FFC61502651+33]
Task trace:
Backtrace:
        GetHandleVerifier [0x00007FFBD06D7E0D+389053]
        GetHandleVerifier [0x00007FFBD06D79CB+387963]

error: [C:/D/S4D/Slicer-build/bin/Debug/SlicerApp-real.exe] exit abnormally - Report the problem.
</code></pre>

---

## Post #2 by @pieper (2021-07-21 12:27 UTC)

<p>It could be that the WebEngine code picks up a slightly different set of shared libraries than the main Slicer build because on mac there’s a similar issue where an internationalization library gets the wrong version for a local build while a packaged build works fine.  You could try <a href="https://www.dependencywalker.com/">depends</a> to see if this is the case.  The WebEngine is basically Chrome and it has a big complex build system that’s nicely wrapped in Qt but there are probably some loose ends.</p>

---

## Post #3 by @lassoan (2021-07-21 12:58 UTC)

<p>It might be just a harmless debug exception (Chromium has a number of these). You may be able to choose to continue the execution if Visual Studio displays the exception popup. These exceptions do not occur if you build in release mode.</p>

---

## Post #4 by @Benjamin_Bennett (2025-11-03 05:10 UTC)

<p>delete the QtWebEngine folder ,  under C:\Users\USERNAME\AppData\Local\slicer.org\Slicer</p>

---

## Post #5 by @lassoan (2025-11-03 05:19 UTC)

<p>Have you built Slicer in debug mode?<br>
Or is it an official release that you have downloaded from <a href="http://download.slicer.org">download.slicer.org</a>?</p>

---

## Post #6 by @Benjamin_Bennett (2025-11-03 06:17 UTC)

<p>yes I just ran  it to this randomly .</p>

---
