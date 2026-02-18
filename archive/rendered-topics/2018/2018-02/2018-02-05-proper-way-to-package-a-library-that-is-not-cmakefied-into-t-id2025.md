# Proper way to package a library that is not cmakefied into the extension

**Topic ID**: 2025
**Date**: 2018-02-05
**URL**: https://discourse.slicer.org/t/proper-way-to-package-a-library-that-is-not-cmakefied-into-the-extension/2025

---

## Post #1 by @leochan2009 (2018-02-05 18:08 UTC)

<p>Dear Slicer developers,</p>
<p>i have a question regarding the extension packaging.<br>
Currently i have an external added library in my extension, the external added library is not cmakefied.<br>
Basically i just download the library and header file and linked to my extension.<br>
For the cmakefied projects, we use CPACK_INSTALL_CMAKE_PROJECTS to add the library into the package.<br>
What about the non-cmakefied library, are there any variable i could set to include the library into the package?<br>
Your suggestions are appreciated!</p>
<p>Best,<br>
Longquan</p>

---

## Post #2 by @leochan2009 (2018-02-05 21:35 UTC)

<p>never mind.<br>
I think the OpenSSL library in Slicer seems to be a good example to look into. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #3 by @ihnorton (2018-02-05 22:24 UTC)

<p>For only one platform (assuming Windows), you could either use <code>add_custom_command</code>, or use ExternalProject which can run arbitrary commands. For multiple platforms it will get a little tricky because you have to do everything in cmake, and need to handle extension and package layout differences.</p>

---

## Post #4 by @leochan2009 (2018-02-06 00:47 UTC)

<p>Hi Isaiah,</p>
<p>Thanks for your suggestion.<br>
I am looking into the file:<br>
I think they are using exactly the same method as you mentioned!<br>
Just test the installation, it is working for Mac OS!<br>
Still need to fix a lot of things for other platform.<br>
Best,<br>
Longquan</p>

---
