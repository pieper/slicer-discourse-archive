---
topic_id: 28981
title: "Cmake Setting In Vscode"
date: 2023-04-18
url: https://discourse.slicer.org/t/28981
---

# Cmake setting in vscode

**Topic ID**: 28981
**Date**: 2023-04-18
**URL**: https://discourse.slicer.org/t/cmake-setting-in-vscode/28981

---

## Post #1 by @park (2023-04-18 07:30 UTC)

<p>Hi all,</p>
<p>I am tring to create an enviornment for 3D slicer using vscode.<br>
I have built my project using the “setting.json” as shown below:</p>
<pre><code class="lang-auto">{
    "cmake.configureArgs": [
        "-DCMAKE_BUILD_TYPE=Debug",
        "-G", "Visual Studio 17 2022",
        "-DCMAKE_CONFIGURATION_TYPES:STRING=Debug",
        "-DCMAKE_INSTALL_PREFIX:PATH=install",
        "-DCMAKE_VERBOSE_MAKEFILE:BOOL=OFF",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=ON"
      ],

    "cmake.configureSettings": {
        "CMAKE_GENERATOR_TOOLSET": "host=x64",
        "Qt5_DIR": "C:/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5"
    },
    "cmake.buildDirectory": "D:/BUILD_Slicer/S5D",

}
</code></pre>
<p>The build is successful without any errors. However, whenever I make changes to some code and rebuild, all codes are built again instead of just the edited code. This is very time-consuming. Is there any way to solve this problem?</p>
<p>Tae Young Park</p>

---
