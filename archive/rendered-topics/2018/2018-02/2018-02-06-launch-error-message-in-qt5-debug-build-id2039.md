---
topic_id: 2039
title: "Launch Error Message In Qt5 Debug Build"
date: 2018-02-06
url: https://discourse.slicer.org/t/2039
---

# Launch error message in Qt5 debug build

**Topic ID**: 2039
**Date**: 2018-02-06
**URL**: https://discourse.slicer.org/t/launch-error-message-in-qt5-debug-build/2039

---

## Post #1 by @ihnorton (2018-02-06 22:53 UTC)

<p>Has anyone else seen this, immediately on application launch? Slicer still appears to start ok.  Debug build, macOS 10.12, SDK 10.12, Qt5 from upstream. It appeared after the most recent ITK update.</p>
<pre><code class="lang-auto">Error: In /opt/bld/s5nj/ITKv4/Modules/ThirdParty/GDCM/src/gdcm/Source/Common/gdcmSystem.cxx, line 461, function static const char *gdcm::System::GetCurrentProcessFileName()
missing implementation
</code></pre>

---

## Post #2 by @ihnorton (2018-02-06 22:56 UTC)

<p>It looks like ITK disables the relevant flag providing the implementation on mac due to linking errors and/or sdk compatibility policy: <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/b853e6ce32676">https://github.com/InsightSoftwareConsortium/ITK/commit/b853e6ce32676</a> (and a few others).</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> any idea about this, since you were mentioned in that commit?</p>

---

## Post #3 by @pieper (2018-02-06 23:48 UTC)

<p>Yes, I get that same message on my mac builds (Qt4 and Qt5)</p>

---

## Post #4 by @jcfr (2018-02-07 06:46 UTC)

<p>Thanks for reporting the issue, this should be fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26893">r26893</a></p>
<p>In  ITK, we removed the need to explicitly linking against CoreFoundation library in GDCM to help build python wheels that would work on different version of OSX.</p>
<p>The functions with this dependency were used only in GDCM executables there are not built in ITK. The current error was due to the call to <code>GlobalInternal::LoadDefaultPaths()</code> done at load time of the GDCM library … that was adding resources path to a global list. Since these resources path are not useful, we commented to call to <code>GlobalInternal::LoadDefaultPaths()</code>.</p>
<p>If in the future, we need to link against the library, GDCM build system could be updated to use <code>-framework CoreFoundatation</code> instead of an explicit full path to <code>/path/to/Developer/SDKs/MacOSX10.12.sdk/System/Library/Frameworks/CoreFoundation.framework</code>.</p>

---

## Post #5 by @ihnorton (2018-02-07 11:47 UTC)

<p>Great, thanks. ITK/GDCM could use <code>_NSGetExecutablePath()</code> to do the same thing as the CoreFoundation code is doing, but without SDK pinning (cc <a class="mention" href="/u/thewtex">@thewtex</a>).</p>

---
