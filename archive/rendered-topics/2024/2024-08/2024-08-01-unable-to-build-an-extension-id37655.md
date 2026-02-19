---
topic_id: 37655
title: "Unable To Build An Extension"
date: 2024-08-01
url: https://discourse.slicer.org/t/37655
---

# Unable to build an extension

**Topic ID**: 37655
**Date**: 2024-08-01
**URL**: https://discourse.slicer.org/t/unable-to-build-an-extension/37655

---

## Post #1 by @andrew_why_not (2024-08-01 10:48 UTC)

<p>Hello,</p>
<p>Trying to build a Python extension for distribution. It is highly required to prepare a .zip file so that users would be able to install it quickly.</p>
<p>After performing <strong>make package</strong> on MacOS, I have a .tar.gz file. But when I try to install it to a Windows machine, it does not appear in the list of modules. Took a look into the archive and discovered that it contains some kind of application (<strong>Slicer.app</strong>) with the module files inside. It does not seem to be exactly the same as in the folder with modules on the Windows machine, so I am wondering: am I doing smth wrong? Can a module archived in MacOS be used on Windows machines in general?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2024-08-01 12:40 UTC)

<p>The extension builds are platform-specific (even if they are just python) since they take into account the possibility of machine-code binary files that need to be handle correctly for the platform.  One option is to submit to the extension process (public) and then correct packages will be made for each platform.</p>
<p>But another option is just to bundle up the python code and give it to users directly.  I don’t think there’s a good example of that, but it shouldn’t be too hard.</p>

---
