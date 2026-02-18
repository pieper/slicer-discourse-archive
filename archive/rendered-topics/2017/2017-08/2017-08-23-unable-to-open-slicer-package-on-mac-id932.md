# Unable to open Slicer package on Mac

**Topic ID**: 932
**Date**: 2017-08-23
**URL**: https://discourse.slicer.org/t/unable-to-open-slicer-package-on-mac/932

---

## Post #1 by @fedorov (2017-08-23 17:35 UTC)

<p>I downloaded today’s nightly package, but when I click on the .dmg file, nothing happens - the volume is not mounted.</p>
<p>I searched around, and the only reason I can see is that download was corrupted in the process. I computed the checksum, and it matches 7b265f06b75b83e763f5e25537fc0a8a listed on <a href="http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;name=Slicer-4.7.0-2017-08-22-macosx-amd64.dmg&amp;checksum=7b265f06b75b83e763f5e25537fc0a8a">http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;name=Slicer-4.7.0-2017-08-22-macosx-amd64.dmg&amp;checksum=7b265f06b75b83e763f5e25537fc0a8a</a>.</p>
<p>Anyone has any hints what could be causing this, or how to debug this issue?</p>
<p>Anyone experienced a similar problem on mac?</p>

---

## Post #2 by @fedorov (2017-08-23 17:46 UTC)

<p>I was able to “resolve” this problem by downloading Slicer package 3 times. I was able to mount “the 3rd dmg file”. md5 checksum is the same in the last 2 of the downloaded dmg files.</p>

---

## Post #3 by @lassoan (2017-08-23 21:37 UTC)

<p>2 posts were split to a new topic: <a href="/t/slicer-installation-on-mac-using-homebrew/933">Slicer installation on Mac using homebrew</a></p>

---

## Post #5 by @lassoan (2017-08-23 21:38 UTC)

<p>9 posts were merged into an existing topic: <a href="/t/slicer-installation-on-mac-using-homebrew/933">Slicer installation on Mac using homebrew</a></p>

---
