# Using OpenIGTLink

**Topic ID**: 8050
**Date**: 2019-08-15
**URL**: https://discourse.slicer.org/t/using-openigtlink/8050

---

## Post #1 by @ahmed_elshreif (2019-08-15 21:12 UTC)

<p>I have build the OpenIGTLink library for cpp and I run some of the examples and they work for me and send the data to Slicer but now I need to use the built library in new cpp project and I don’t know how to include it in the new project as new project has new path and Visual studio don’t see the library.</p>

---

## Post #2 by @lassoan (2019-08-16 00:42 UTC)

<p>For building software that is made up of several libraries, it is strongly recommended to use CMake. If you set up your build system appropriately, CMake can download and build all third-party libraries that can be linked into your application.</p>
<p>Of course, you can do all this work manually, too: build the OpenIGTLink .lib files and add them as additional libraries, and add folders that contain .h files as additional include directories to your project in Visual Studio.</p>

---
