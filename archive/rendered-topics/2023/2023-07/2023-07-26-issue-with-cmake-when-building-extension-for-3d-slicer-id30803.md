# Issue with cmake when building extension for 3D Slicer

**Topic ID**: 30803
**Date**: 2023-07-26
**URL**: https://discourse.slicer.org/t/issue-with-cmake-when-building-extension-for-3d-slicer/30803

---

## Post #1 by @haphantran (2023-07-26 16:02 UTC)

<p>Hi guys,<br>
I’m trying to build the extension using cmake gui on Windows<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#windows" rel="noopener nofollow ugc">Extensions — 3D Slicer documentation</a><br>
Here is the error:</p>
<blockquote>
<p>Blockquote<br>
CMake Error: The source “C:/Users/hapha/OneDrive/Documents/python/SlicerTrack/CMakeLists.txt” does not match the source “C:/Users/hapha/OneDrive/Documents/python/SlicerTrack/Track/CMakeLists.txt” used to generate cache.  Re-run cmake with a different source directory.</p>
</blockquote>
<p>The error seems very generic so I have no idea where to fix. Please help me check this. Thank you.</p>
<p>Here is my folder structure</p>
<blockquote>
<p>Blockquote<br>
tree -I ‘Data’<br>
.<br>
├── CMakeLists.txt<br>
├── LICENSE<br>
├── README.md<br>
├── Track<br>
│   ├── CMakeLists.txt<br>
│   ├── README.md<br>
│   ├── Resources<br>
│   │   ├── Icons<br>
│   │   │   ├── Track.png<br>
│   │   │   └── media-control-icons<br>
│   │   │       ├── next.png<br>
│   │   │       ├── pause.png<br>
│   │   │       ├── play.png<br>
│   │   │       ├── previous.png<br>
│   │   │       └── stop.png<br>
│   │   └── UI<br>
│   │       └── Track.ui<br>
│   ├── Testing<br>
│   │   ├── CMakeLists.txt<br>
│   │   └── Python<br>
│   │       └── CMakeLists.txt<br>
│   ├── Track.py<br>
│   ├── <strong>pycache</strong><br>
│   │   ├── Track.cpython-39.pyc<br>
│   │   └── test.cpython-39.pyc<br>
│   └── requirements.txt<br>
├── Track.png<br>
├── TrackingDataProcessor<br>
│   ├── README.md<br>
│   ├── TrackingDataProcessor.cpp<br>
│   ├── TrackingDataProcessor.sln<br>
│   └── TrackingDataProcessor.vcxproj<br>
└── original_UI.png</p>
</blockquote>
<p>Here is the CMakeList.txt in main extension folder (SlicerTrack)</p>
<blockquote>
<p>Blockquote<br>
cmake_minimum_required(VERSION 3.13.4)<br>
project(Track)<br>
set(EXTENSION_HOMEPAGE “<a href="https://slicertrack.github.io/" rel="noopener nofollow ugc">https://slicertrack.github.io/</a>”)<br>
set(EXTENSION_CATEGORY “Tracking”)<br>
set(EXTENSION_CONTRIBUTORS "HaPhan Tran, Mubariz Afzal ")<br>
set(EXTENSION_DESCRIPTION “Module providing tracking tools and displacement visualizations”)<br>
set(EXTENSION_ICONURL “<a href="http://www.example.com/Slicer/Extensions/Track.png" rel="noopener nofollow ugc">http://www.example.com/Slicer/Extensions/Track.png</a>”)<br>
set(EXTENSION_SCREENSHOTURLS “<a href="http://www.example.com/Slicer/Extensions/Track/Screenshots/1.png" rel="noopener nofollow ugc">http://www.example.com/Slicer/Extensions/Track/Screenshots/1.png</a>”)<br>
set(EXTENSION_DEPENDS “NA”) # Specified as a list or “NA” if no dependencies<br>
find_package(Slicer REQUIRED)<br>
include(${Slicer_USE_FILE})<br>
add_subdirectory(Track)<br>
include(${Slicer_EXTENSION_GENERATE_CONFIG})<br>
include(${Slicer_EXTENSION_CPACK})</p>
</blockquote>
<p>Here is the cmake in the Track module</p>
<blockquote>
<p>Blockquote<br>
<span class="hashtag-raw">#-----------------------------------------------------------------------------</span><br>
set(MODULE_NAME Track)<br>
<span class="hashtag-raw">#-----------------------------------------------------------------------------</span><br>
set(MODULE_PYTHON_SCRIPTS<br>
${MODULE_NAME}.py<br>
)<br>
set(MODULE_PYTHON_RESOURCES<br>
Resources/Icons/${MODULE_NAME}.png<br>
Resources/UI/${MODULE_NAME}.ui<br>
)<br>
<span class="hashtag-raw">#-----------------------------------------------------------------------------</span><br>
slicerMacroBuildScriptedModule(<br>
NAME ${MODULE_NAME}<br>
SCRIPTS ${MODULE_PYTHON_SCRIPTS}<br>
RESOURCES ${MODULE_PYTHON_RESOURCES}<br>
WITH_GENERIC_TESTS<br>
)<br>
<span class="hashtag-raw">#-----------------------------------------------------------------------------</span><br>
if(BUILD_TESTING)<br>
slicer_add_python_unittest(SCRIPT ${MODULE_NAME}.py)<br>
add_subdirectory(Testing)<br>
endif()</p>
</blockquote>

---
