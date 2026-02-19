---
topic_id: 1607
title: "Weird Security Error On Macos When Restarting Under Lldb Som"
date: 2017-12-06
url: https://discourse.slicer.org/t/1607
---

# Weird security error on macOS when restarting under lldb, sometimes

**Topic ID**: 1607
**Date**: 2017-12-06
**URL**: https://discourse.slicer.org/t/weird-security-error-on-macos-when-restarting-under-lldb-sometimes/1607

---

## Post #1 by @ihnorton (2017-12-06 21:47 UTC)

<p>I keep getting this error randomly every few times I restart Slicer under lldb. The first run after launching lldb always works, but if I relaunch in the same lldb process (<code>proc launch</code>), then I get this anywhere from the 2nd to maybe maximum 10th run. I use lldb like this very often, but have never seen such an error before…</p>
<p>Has anyone else seen this?</p>
<pre><code class="lang-auto">(lldb) proc lau
...
(lldb) bt
* thread #1, queue = 'com.apple.main-thread', stop reason = c++ exception
  * frame #0: 0x00007fffc0002450 libc++abi.dylib`__cxa_allocate_exception
    frame #1: 0x00007fffb213848a Security`Security::MacOSError::throwMe(int) + 20
    frame #2: 0x00007fffb2018673 Security`Security::CodeSigning::SecStaticCode::signature() + 87
    frame #3: 0x00007fffb2018953 Security`Security::CodeSigning::SecStaticCode::verifySignature() + 135
    frame #4: 0x00007fffb20186d0 Security`Security::CodeSigning::SecStaticCode::validateDirectory() + 92
    frame #5: 0x00007fffb201925b Security`Security::CodeSigning::SecStaticCode::validateNonResourceComponents() + 15
    frame #6: 0x00007fffb200d309 Security`Security::CodeSigning::SecCode::checkValidity(unsigned int) + 205
    frame #7: 0x00007fffb2011710 Security`SecCodeCheckValidityWithErrors + 59
    frame #8: 0x000000010441b507 QtCore`QSettingsPrivate::create(QSettings::Format, QSettings::Scope, QString const&amp;, QString const&amp;) + 139
    frame #9: 0x0000000104401af8 QtCore`QSettings::QSettings(QSettings::Scope, QString const&amp;, QString const&amp;, QObject*) + 20
    frame #10: 0x0000000104421fd0 QtCore`QFactoryLoader::update() + 94
    frame #11: 0x0000000104421dcc QtCore`QFactoryLoader::QFactoryLoader(char const*, QString const&amp;, Qt::CaseSensitivity) + 216
    frame #12: 0x00000001038b893d QtGui`loaderV2() + 94
    frame #13: 0x00000001038b80ec QtGui`QIcon::addFile(QString const&amp;, QSize const&amp;, QIcon::Mode, QIcon::State) + 112
    frame #14: 0x00000001038b845c QtGui`QIcon::QIcon(QString const&amp;) + 40
    frame #15: 0x0000000100de3e2e libCTKScriptingPythonWidgets.0.1.dylib`ctkPythonConsole::ctkPythonConsole(this=0x000000011ccce3e0, parentObject=0x0000000000000000) at ctkPythonConsole.cpp:534
    frame #16: 0x0000000100de40ad libCTKScriptingPythonWidgets.0.1.dylib`ctkPythonConsole::ctkPythonConsole(this=0x000000011ccce3e0, parentObject=0x0000000000000000) at ctkPythonConsole.cpp:532
    frame #17: 0x00000001004dc76f libqSlicerBaseQTGUI.dylib`qSlicerApplicationPrivate::init(this=0x000000011cc9d660) at qSlicerApplication.cxx:190
    frame #18: 0x00000001004de9ac libqSlicerBaseQTGUI.dylib`qSlicerApplication::qSlicerApplication(this=0x00007fff5fbff498, _argc=0x00007fff5fbff540, _argv=0x00007fff5fbff648) at qSlicerApplication.cxx:351
    frame #19: 0x00000001004debb5 libqSlicerBaseQTGUI.dylib`qSlicerApplication::qSlicerApplication(this=0x00007fff5fbff498, _argc=0x00007fff5fbff540, _argv=0x00007fff5fbff648) at qSlicerApplication.cxx:349
    frame #20: 0x000000010003ab39 Slicer`(anonymous namespace)::SlicerAppMain(argc=10, argv=0x00007fff5fbff648) at Main.cxx:141
    frame #21: 0x000000010003a672 Slicer`main(argc=10, argv=0x00007fff5fbff648) at Main.cxx:302
    frame #22: 0x00007fffc13f9235 libdyld.dylib`start + 1
    frame #23: 0x00007fffc13f9235 libdyld.dylib`start + 1
</code></pre>

---

## Post #2 by @pieper (2017-12-07 00:18 UTC)

<p>Very weird - looks like an OS bug, like maybe a race condition?  It seems to be happening while opening your settings file.  Launching again after the crash works?</p>

---

## Post #3 by @lassoan (2017-12-07 00:59 UTC)

<p>Is it Qt4 or Qt5? Have you built Qt yourself? Are the binaries signed?</p>

---

## Post #4 by @ihnorton (2017-12-07 01:28 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="1607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Launching again after the crash works?</p>
</blockquote>
</aside>
<p>[edit] re-launching again in the same process? Good point - not sure.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="1607" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is it Qt4 or Qt5? Have you built Qt yourself? Are the binaries signed?</p>
</blockquote>
</aside>
<p>Qt4 from Homebrew, not signed as far as I know.</p>
<p>It’s not a huge issue, just really weird. Maybe Apple is mad because I keep ignoring update notices <img src="https://emoji.discourse-cdn.com/twitter/laughing.png?v=12" title=":laughing:" class="emoji" alt=":laughing:" loading="lazy" width="20" height="20">.</p>

---
