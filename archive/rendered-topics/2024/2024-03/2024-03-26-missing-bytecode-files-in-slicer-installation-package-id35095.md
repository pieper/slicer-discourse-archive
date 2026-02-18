# Missing bytecode files in Slicer installation package

**Topic ID**: 35095
**Date**: 2024-03-26
**URL**: https://discourse.slicer.org/t/missing-bytecode-files-in-slicer-installation-package/35095

---

## Post #1 by @Albi (2024-03-26 11:01 UTC)

<p>Hi,<br>
I recently tried to create an installation package of Slicer. Thanks to whoever implement this as it is really straightforward with the available <code>make package</code> command.<br>
After installing the freshly packaged version I found out that some .pyc files were created at the first execution of Slicer. After some research it appears that a vast majority of pyc files are already present in the installation package. Executing <code>./python-install/bin/PythonSlicer -m compileall .</code> in my build directory and then <code>make package</code> in the inner build directory does not add all pyc files to the package.<br>
My goal is to make the installation directory as read only for regular user. My current solution is to run compileall on the target machine after extracting Slicer package and before making the installation directory as read only but I was wondering if there was a better way to have all pyc files packaged in the archive. Does someone as any hint on this? I am not familiar with Cpack but I’m willing to dig in it if that the correct path to explore.</p>

---
