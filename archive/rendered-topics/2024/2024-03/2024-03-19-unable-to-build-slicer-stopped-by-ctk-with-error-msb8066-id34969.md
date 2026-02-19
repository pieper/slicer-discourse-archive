---
topic_id: 34969
title: "Unable To Build Slicer Stopped By Ctk With Error Msb8066"
date: 2024-03-19
url: https://discourse.slicer.org/t/34969
---

# Unable to build Slicer: stopped by CTK with error MSB8066

**Topic ID**: 34969
**Date**: 2024-03-19
**URL**: https://discourse.slicer.org/t/unable-to-build-slicer-stopped-by-ctk-with-error-msb8066/34969

---

## Post #1 by @RolandLau (2024-03-19 08:31 UTC)

<p>Hi,everyone.</p>
<p>I followed instruction at<br>
<a>https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.htm</a>l<br>
trying to build slicer,but build stopped with error MSB8066.</p>
<p>Slicer source: latest main<br>
OS: Windows 10<br>
Visual Studio:MSVC v143<br>
Qt version: 5.15.2<br>
cmake:3.28.3-windows-x86_64</p>
<p>last few build log:</p>
<pre><code class="lang-auto">        正在创建库 E:/D/SD/CTK-build/CTK-build/bin/Debug/CTKWidgetsPlugins.lib 和对象 E:/D/SD/CTK-build/CTK-build/bin/Debug/CTKWidgetsPlugins.exp
      CTKWidgetsPlugins.vcxproj -&gt; E:\D\SD\CTK-build\CTK-build\bin\designer\Debug\CTKWidgetsPlugins.dll
      PythonQt Wrapping - Generating generated_cpp/org_commontk_CTKWidgets/org_commontk_CTKWidgets_init.cpp
      Generating moc_ctkWidgetsPythonQtDecorators.cpp
      Building Custom Rule E:/D/SD/CTK/Libs/Widgets/CMakeLists.txt
      Generating generated_cpp/org_commontk_CTKWidgets/moc_org_commontk_CTKWidgets.cpp
      org_commontk_CTKWidgets_init.cpp
      org_commontk_CTKWidgets_module_init.cpp
      moc_org_commontk_CTKWidgets.cpp
      moc_ctkWidgetsPythonQtDecorators.cpp
      正在生成代码...
        正在创建库 E:/D/SD/CTK-build/CTK-build/bin/Debug/CTKWidgetsPythonQt.lib 和对象 E:/D/SD/CTK-build/CTK-build/bin/Debug/CTKWidgetsPythonQt.exp
      CTKWidgetsPythonQt.vcxproj -&gt; E:\D\SD\CTK-build\CTK-build\bin\Debug\CTKWidgetsPythonQt.pyd
      Copying python Script: ctk/__init__.py
      Copying python Script: qt/__init__.py
      Building Custom Rule E:/D/SD/CTK/Libs/Scripting/Python/Core/Python/CMakeLists.txt
      Compiling python scripts: CTKScriptingPythonCore
      Compiling E:/D/SD/CTK-build/CTK-build/bin/Python/qt/__init__.py ...
      Compiling E:/D/SD/CTK-build/CTK-build/bin/Python/ctk/__init__.py ...
      Building Custom Rule E:/D/SD/CTK/Libs/Scripting/Python/Core/Python/CMakeLists.txt
E:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(254,5): error MSB8066: “E:\D\SD\CTK-build\CMakeFiles\a753c7d83d533641ac03f7e3b7b6df0b\CTK-mkdir.rule;E:\D\SD\CTK-build\CMakeFiles\a753c7d83d533641ac03f7e3b7b6df0b\CTK-download.rule;E:\D\SD\CTK-build\CMakeFiles\a753c7d83d533641ac03f7e3b7b6df0b\CTK-update.rule;E:\D\SD\CTK-build\CMakeFiles\a753c7d83d533641ac03f7e3b7b6df0b\CTK-patch.rule;E:\D\SD\CTK-build\CMakeFiles\a753c7d83d533641ac03f7e3b7b6df0b\CTK-configure.rule;E:\D\SD\CTK-build\CMakeFiles\a753c7d83d533641ac03f7e3b7b6df0b\CTK-build.rule;E:\D\SD\CTK-build\CMakeFiles\a753c7d83d533641ac03f7e3b7b6df0b\CTK-forceconfigure.rule;E:\D\SD\CTK-build\CMakeFiles\a753c7d83d533641ac03f7e3b7b6df0b\CTK-install.rule;E:\D\SD\CTK-build\CMakeFiles\1a8ae1f8c74cff30ec9935fb0b0cdc16\CTK-complete.rule;E:\D\SD\CTK-build\CMakeFiles\a008fdd1d6aeb806b61be6a68242b515\CTK.rule;E:\D\SD\CTK\CMakeLists.txt”的自定义生成已退出，代码为 1。 [E:\D\SD\CTK-build\CTK.vcxproj] [E:\D\SD\CTK.vcxproj]
E:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(254,5): error MSB8066: “E:\D\SD\CMakeFiles\6d7b3d399a4c32175de194ffde57ab2a\CTK-mkdir.rule;E:\D\SD\CMakeFiles\6d7b3d399a4c32175de194ffde57ab2a\CTK-download.rule;E:\D\SD\CMakeFiles\6d7b3d399a4c32175de194ffde57ab2a\CTK-update.rule;E:\D\SD\CMakeFiles\6d7b3d399a4c32175de194ffde57ab2a\CTK-patch.rule;E:\D\SD\CMakeFiles\6d7b3d399a4c32175de194ffde57ab2a\CTK-configure.rule;E:\D\SD\CMakeFiles\6d7b3d399a4c32175de194ffde57ab2a\CTK-build.rule;E:\D\SD\CMakeFiles\6d7b3d399a4c32175de194ffde57ab2a\CTK-generate_project_description.rule;E:\D\SD\CMakeFiles\6d7b3d399a4c32175de194ffde57ab2a\CTK-install.rule;E:\D\SD\CMakeFiles\fb05fce5132104d50a122db3bca492b3\CTK-complete.rule;E:\D\SD\CMakeFiles\5be8eeaac1dcb45c85fd3d72b33c0314\CTK.rule;E:\D\S\CMakeLists.txt”的自定义生成已退出，代码为 1。 [E:\D\SD\CTK.vcxproj]
</code></pre>
<p>Any suggestions? Thanks.</p>

---

## Post #2 by @RolandLau (2024-03-24 13:29 UTC)

<p>After days of research,I finally found the problem is bad network…</p>

---
