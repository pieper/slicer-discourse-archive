# Cannot launch QT Creator on MacOS

**Topic ID**: 11620
**Date**: 2020-05-19
**URL**: https://discourse.slicer.org/t/cannot-launch-qt-creator-on-macos/11620

---

## Post #1 by @che85 (2020-05-19 13:45 UTC)

<p>Hi all,</p>
<p>I am trying to launch QT Creator for debugging the nightly build, but it’s not launching.</p>
<p>Platform: macOS Mojave<br>
SlicerBuild: succeeded<br>
QT version: 5.14.2<br>
QT creator: 4.12</p>
<p>I created a gist here (using <code>export DYLD_PRINT_LIBRARIES=1</code>):<br>
</p><aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/che85/e20e761a3a42b672c02e0e17df87daa1" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/che85/e20e761a3a42b672c02e0e17df87daa1" target="_blank" rel="nofollow noopener">https://gist.github.com/che85/e20e761a3a42b672c02e0e17df87daa1</a></h4>
<h5>QT_Creator_launch_failing</h5>
<pre><code class="">herzc@28d244e241ba ~/D/S/Slicer-build&gt; ./Slicer --launch /Users/herzc/Qt/Qt\ Creator.app/Contents/MacOS/Qt\ Creator 
dyld: loaded: /Users/herzc/D/S4D/Slicer-build/./Slicer
dyld: loaded: /System/Library/Frameworks/Cocoa.framework/Versions/A/Cocoa
dyld: loaded: /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon
dyld: loaded: /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
dyld: loaded: /usr/lib/libz.1.dylib
dyld: loaded: /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
dyld: loaded: /usr/lib/libstdc++.6.dylib
dyld: loaded: /usr/lib/libSystem.B.dylib
dyld: loaded: /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation</code></pre>
This file has been truncated. <a href="https://gist.github.com/che85/e20e761a3a42b672c02e0e17df87daa1" target="_blank" rel="nofollow noopener">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Does anyone know what could be causing this?</p>
<p>Thank you,<br>
Christian</p>

---

## Post #2 by @pieper (2020-05-19 15:29 UTC)

<p>It seems like that should work as long as creator comes from the same Qt you used to build Slicer.</p>
<p>FWIW, I typically use Xcode for debugging on mac by manually copying the launcher environment into the project settings.  The homebrew Qt comes with creator, and that works for me if I attach to a running instance, but not when I start it with the Slicer launcher.</p>

---

## Post #3 by @che85 (2020-05-19 17:25 UTC)

<p>FYI,</p>
<p>I built Qt Creator from source with my local qt version and now it’s working to launch it.</p>
<p>I followed the instructions given here: <a href="https://wiki.qt.io/Building_Qt_Creator_from_Git" rel="nofollow noopener">https://wiki.qt.io/Building_Qt_Creator_from_Git</a></p>

---
