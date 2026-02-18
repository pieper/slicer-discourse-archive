# Problems with general registration elastix

**Topic ID**: 7556
**Date**: 2019-07-12
**URL**: https://discourse.slicer.org/t/problems-with-general-registration-elastix/7556

---

## Post #1 by @zahiraabdala (2019-07-12 17:05 UTC)

<p>Good afternoon,</p>
<p>I try to use “General Registration Elastix” module extension but it tells me</p>
<p>Volume registration is started in working directory: /Volumes/Slicer-4.10.2-macosx-amd64/Slicer.app/Contents/Extensions-28257/Elastix/20190712_135520_600<br>
Register volumes…<br>
Error: Command ‘elastix’ returned non-zero exit status 254</p>
<p>I don´t know what that error means.  I have installed 4.10.2 version for MAC.</p>
<p>Thank you!</p>

---

## Post #2 by @jcfr (2019-07-13 01:11 UTC)

<p>Is there any other relevant information displayed in the log ?</p>

---

## Post #3 by @Alex_Vergara (2019-07-15 10:12 UTC)

<p>You are running Slicer from a read-only working directory, you need to move Slicer to /Users/YourUser/Applications/ . This will solve all your problems</p>

---

## Post #4 by @zahiraabdala (2019-07-17 14:02 UTC)

<p>Hi Jean<br>
No, only showed me this.<br>
Thanks for answer to me.</p>

---

## Post #5 by @zahiraabdala (2019-07-17 14:05 UTC)

<p>Hi Alex, I am running Slicer from a /Users/Your User/Applications/ and doesn’t work. I think that there is other problem.</p>

---

## Post #6 by @lassoan (2019-07-17 14:18 UTC)

<p>I think this problem has been fixed recently. You need to <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#Updating_installed_extensions" rel="nofollow noopener">update SlicerElastix extension</a> (or uninstall and reinstall SlicerElastix).</p>

---
