---
topic_id: 3503
title: "Using The Openigtlink Library In A Loadable Module"
date: 2018-07-17
url: https://discourse.slicer.org/t/3503
---

# Using the OpenIGTLink library in a loadable module

**Topic ID**: 3503
**Date**: 2018-07-17
**URL**: https://discourse.slicer.org/t/using-the-openigtlink-library-in-a-loadable-module/3503

---

## Post #1 by @Tiffas (2018-07-17 14:26 UTC)

<p>Hi,</p>
<p>I am trying to use the OpenIGTLink library in a C++ module with the following code:</p>
<pre><code>igtl::ClientSocket::Pointer socket;
socket = igtl::ClientSocket::New();

int r = socket-&gt;ConnectToServer("172.31.1.2", 18944); 
</code></pre>
<p>I got a linker error at the third line: undefined reference to ’ igtl::ClientSocket::ConnectToServer(char const*, int, bool) ’</p>
<p>Is there a special command to add to the module CMakeLists so that the linker knows it must search for the OpenIGTLink libraries ? I tried to add set(EXTENSION_DEPENDS “OpenIGTLink”) in the extension CMakeLists but it did not work.</p>
<p>Many thanks,<br>
Loïc</p>

---

## Post #2 by @adamrankin (2018-07-17 14:43 UTC)

<p>In your CMake code, you’ll also need to add</p>
<pre><code class="lang-auto">FIND_PACKAGE(OpenIGTLink REQUIRED)

....

target_link_libraries(&lt;yourTargetName&gt; PUBLIC OpenIGTLink)
</code></pre>

---

## Post #3 by @lassoan (2018-07-17 15:21 UTC)

<p>Typically you don’t need such low-level access to OpenIGTLink library. You just create a connector node in the scene to open a connection and content of messages (transforms, images, models, etc.) are turned into MRML nodes. If you have new custom message types then you only need to define a custom converter, which creates/updates MRML nodes from OpenIGTLink messages (and may also create OpenIGTLink messages from MRML nodes).</p>

---
