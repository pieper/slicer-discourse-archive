# SlicerOpenIGTLink error

**Topic ID**: 23891
**Date**: 2022-06-15
**URL**: https://discourse.slicer.org/t/sliceropenigtlink-error/23891

---

## Post #1 by @priya.vada4 (2022-06-15 14:26 UTC)

<p>Hi</p>
<p>I am running into issues building SlicerOpenIGTLink using different versions of Slicer (4.13 and 5.1) on macOS Monterey 12.3.1 as follows:</p>
<pre><code class="lang-auto"> unknown library ordinal -11 in ../SlicerOpenIGTLink-build/inner-build/lib/Slicer-5.1/qt-loadable-modules/libqSlicerOpenIGTLinkIFModule.dylib when binding '__ZN20vtkDebugLeaksManagerC1Ev')
  Error(s):
    Cannot load library ../SlicerOpenIGTLink-build/inner-build/lib/Slicer-5.1/qt-loadable-modules/libqSlicerOpenIGTLinkRemoteModule.dylib unknown library ordinal -9 when binding '__ZN20vtkDebugLeaksManagerC1Ev')
</code></pre>
<p>Can someone let me know what is the source of the error and a possible solution.</p>
<p>Thanks<br>
Priya</p>

---

## Post #2 by @priya.vada4 (2022-06-22 01:13 UTC)

<p>For anyone facing this problem, upgrading to Xcode 13.4.1 fixed the problem.</p>
<p>Priya</p>

---
