# 3D slicer for MAC cannot install slicer extensions from files

**Topic ID**: 24972
**Date**: 2022-08-29
**URL**: https://discourse.slicer.org/t/3d-slicer-for-mac-cannot-install-slicer-extensions-from-files/24972

---

## Post #1 by @shai-ikko (2022-08-29 07:56 UTC)

<p>Hi,</p>
<p>I am developing a pure-python extension of Slicer. It is, at this point, private, so I cannot distribute it through the general extension server, and I have distributed it internally as a zip file. Most users are on Windows, and had no issues, but on a Mac the extension could not be installed.</p>
<p>This is not the issue of <a href="https://discourse.slicer.org/t/3d-slicer-for-mac-cannot-install-slicer-extensions/2945">3D slicer for MAC cannot install slicer extensions</a> – extensions from the manager are installed with no problem; but when trying to install the Zip file, we get</p>
<pre><code class="lang-auto">ctk::copyDirRecursively: Failed to copy nonexistent directory "/Applications/Slicer.app/Contents/Extensions-30893/MyExtension/30893-macosx-amd64-MyExtension-git8bf4715-2022-08-22/Slicer.app/Contents/Extensions-30893/MyExtension"
Failed to copy directory /Applications/Slicer.app/Contents/Extensions-30893/MyExtension/30893-macosx-amd64-MyExtension-git8bf4715-2022-08-22/Slicer.app/Contents/Extensions-30893/MyExtension into directory /Applications/Slicer.app/Contents/Extensions-30893/MyExtension-XXXXXX
</code></pre>
<p>(30893 is the build number for Slicer 5.0.3, I’ve replaced my real extension name with “MyExtension” here)</p>
<p>I have constructed the zip file “manually” – its contents are</p>
<pre><code class="lang-auto">+ 30893-macosx-amd64-MyExtension-git8bf4715-2022-08-22
| + lib
  | + Slicer-5.0
    | + qt-scripted-modules
      | MyExtension.py
| + share
  | + Slicer-5.0
    | CMakeLists.txt
    | MyExtension.s4ext
</code></pre>
<p>What am I doing wrong?</p>

---

## Post #2 by @shai-ikko (2022-08-29 15:12 UTC)

<p>… what I was doing wrong was to assume that, because the module code in Python is cross-platform, the packaging should be similar. The archive structure for a Mac extension is completely different, I see.</p>

---
