# Write python bindings

**Topic ID**: 18066
**Date**: 2021-06-10
**URL**: https://discourse.slicer.org/t/write-python-bindings/18066

---

## Post #1 by @keri (2021-06-10 16:32 UTC)

<p>Hi,</p>
<p>I have some Qt derived classes (widgets) written in C++ and used in SlicerCAT and I would like to bind them in python.</p>
<p>I have some experience of working with <a href="https://github.com/pybind/pybind11" rel="noopener nofollow ugc">pybind11</a> and I do use it in my libraries that are not connected to Qt.<br>
There is also automatic code generator <a href="https://github.com/RosettaCommons/binder" rel="noopener nofollow ugc">rosetta-binder</a> based on pybind11.</p>
<p>I also know that <a href="https://www.qt.io/blog/2018/05/31/write-python-bindings" rel="noopener nofollow ugc">Qt also provides its method</a> to convert C++ to python using <a href="https://doc.qt.io/qtforpython/shiboken6/" rel="noopener nofollow ugc">Shiboken tool</a>. Though I have not tested it yet.</p>
<p>So I would appreciate if someone could give an advice wich way is better and what should I use to convert C++ Qt based widget to python and use it in SlicerCAT</p>

---

## Post #2 by @jamesobutler (2021-06-10 18:37 UTC)

<p>Is there a reason you choose to create your Qt based widget in C++ rather than creating the widget in python? Are you using it in other C++ code?</p>
<p>You can create a custom QWidget from the python interface for use in other python code.</p>

---

## Post #3 by @keri (2021-06-10 21:49 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="18066">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Is there a reason you choose to create your Qt based widget in C++ rather than creating the widget in python? Are you using it in other C++ code?</p>
</blockquote>
</aside>
<p>That is the question that I ask myself.<br>
I think there are two reasons:</p>
<ol>
<li>I already implemented them in C++</li>
<li>I think that in the future I encounter a situation when I will need to bind C++ class to python and thus it means that I will simply postpone this task if I decide not to use bindings now.</li>
</ol>

---

## Post #4 by @pieper (2021-06-10 21:55 UTC)

<p><a class="mention" href="/u/keri">@keri</a> did you look at how other Qt classes are wrapped in Slicer using PythonQt?  This would be more consistent, and hopefully easier, than introducing another python wrapping method.  I haven’t tried it in SlicerCAT, but I believe all the same functionality is available.</p>

---

## Post #5 by @keri (2021-06-10 22:29 UTC)

<p>Hi,</p>
<p>I have made an attempt but didn’t find a file (or class) where it is done. If you know an example in Slicer please say where to look for it.</p>
<p>Also as I know <a href="https://www.riverbankcomputing.com/software/pyqt/" rel="noopener nofollow ugc">PyQt</a>, <a href="https://wiki.qt.io/Qt_for_Python" rel="noopener nofollow ugc">PySide2 (official)</a> and <a href="https://mevislab.github.io/pythonqt/index.html" rel="noopener nofollow ugc">PythonQt</a> they are all different projects am I right? Which ones Slicer is using?</p>

---

## Post #6 by @pieper (2021-06-10 22:37 UTC)

<p>Slicer uses PythonQt very extensively so you can look at any QObject or QWidget subclass in Slicer and the API will be exposed to Python through PythonQt.  Basically, the public interface is wrapped, so Signals, Slots, and Properties are all available.  In addition methods marked with the Q_INVOKABLE macro will also be wrapped.  All <a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers">the python-related developer tutorials</a> make use of this.</p>

---

## Post #7 by @keri (2021-06-10 22:43 UTC)

<p>thank you! I will focus on this and try to sort it out</p>

---

## Post #8 by @keri (2021-06-29 00:25 UTC)

<p>Hi,</p>
<p>I can’t actually find a comprehensive example how Slicer uses PythonQt to wrap C++ classes to python.<br>
I’ve seen examples on PythonQt github but can’t apply it to my class.</p>
<p>For example I can do:</p>
<pre><code class="lang-python">import PythonQt

dir(PythonQt)
</code></pre>
<p>the output would be:</p>
<pre><code class="lang-auto">['BoolResult', 'CTKCore', 'CTKScriptingPythonWidgets', 'CTKVisualizationVTKCore', 
'CTKVisualizationVTKWidgets', 'CTKWidgets', 'Debug', 'Qt', 'QtCore', 'QtGui', 'QtNetwork', 'QtUiTools', 
'__doc__', '__loader__', '__name__', '__package__', '__spec__', 'private', 'qMRMLWidgets', 
'qSlicerAnnotationsModuleWidgets', 'qSlicerBaseQTApp', 'qSlicerBaseQTCLI', 'qSlicerBaseQTCore', 
'qSlicerBaseQTGUI', 'qSlicerMarkupsModuleWidgets', 'qSlicerMarkupsSubjectHierarchyPlugins', 
'qSlicerModelsModuleWidgets', 'qSlicerModelsSubjectHierarchyPlugins', 'qSlicerPlotsModuleWidgets', 
'qSlicerPlotsSubjectHierarchyPlugins', 'qSlicerSegmentationsEditorEffects', 
'qSlicerSegmentationsModuleWidgets', 'qSlicerSegmentationsSubjectHierarchyPlugins', 
'qSlicerSequencesModuleWidgets', 'qSlicerSubjectHierarchyModuleWidgets', 
'qSlicerTablesModuleWidgets', 'qSlicerTablesSubjectHierarchyPlugins', 
'qSlicerTerminologiesModuleWidgets', 'qSlicerTextsModuleWidgets', 
'qSlicerTextsSubjectHierarchyPlugins', 'qSlicerTransformsModuleWidgets', 
'qSlicerTransformsSubjectHierarchyPlugins', 'qSlicerUnitsModuleWidgets', 
'qSlicerVolumeRenderingModuleWidgets', 'qSlicerVolumeRenderingSubjectHierarchyPlugins', 
'qSlicerVolumesModuleWidgets', 'qSlicerVolumesSubjectHierarchyPlugins']
</code></pre>
<p>then I look to GUI elements:</p>
<pre><code class="lang-python">dir(PythonQt.qSlicerBaseQTGUI)
</code></pre>
<p>and among many output classes I can see <code>qSlicerDirectoryListView</code> for example. Assuming that this class was written in C++ and binded to python I search for <code>qSlicerDirectoryListView.h</code> and <code>qSlicerDirectoryListView.cxx</code>. I have found them in <code>Base/QTGUI/</code> folder. To my surprise these files doesn’t contain any <code>PythonQt</code> mentionning…</p>
<p>From my point of view to bind C++ class to python I need to add somwhere <code>#include &lt;PythonQt.h&gt;</code> and <code>PythonQt::self()-&gt;registerClass(&amp;qMyClass::staticMetaObject);</code>. And to check if it works I should run my application and in python interpreter do something like:</p>
<pre><code class="lang-python">import PythonQt
dir(PythonQt)
</code></pre>
<p>and among the output I should be able to find <code>qMyClass</code>. Am I right? Though suspiciously simple <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #9 by @lassoan (2021-06-29 01:20 UTC)

<p>Python wrapping is done fully automatically, by CMake macros (at the lowest level, it is implemented in <code>ctkMacroWrapPythonQt</code> in CTK library). As long as you build the library using Slicer macros, specify <code>WRAP_PYTHONQT</code> flag, and the Python wrapper can parse your header file, all your Qt classes will be automatically available in Python.</p>

---

## Post #10 by @keri (2021-06-29 20:12 UTC)

<p>Thank you! I just got first positive results by using <code>WRAP_PYTHONQT</code> inside <code>slicerMacroBuildAppLibrary</code> and I’m able to use my Qt based custom widgets</p>

---

## Post #11 by @keri (2021-06-30 00:04 UTC)

<p>What maybe the reason why not all my widgets were binded to python?<br>
For example I have:</p>
<pre><code class="lang-auto">slicerMacroBuildAppLibrary(
  NAME ${APPLIB_NAME}    # qColadaApp
  DESCRIPTION_SUMMARY ${${PROJECT_NAME}_DESCRIPTION_SUMMARY}
  DESCRIPTION_FILE ${${PROJECT_NAME}_DESCRIPTION_FILE}
  APPLICATION_NAME ${${PROJECT_NAME}_APPLICATION_NAME}
  EXPORT_DIRECTIVE "Q_COLADA_APP_EXPORT"
  FOLDER ${${PROJECT_NAME}_FOLDER}
  SRCS ${APPLIB_SRCS}
  MOC_SRCS ${APPLIB_MOC_SRCS}
  UI_SRCS ${APPLIB_UI_SRCS}
  RESOURCES ${APPLIB_RESOURCES}
  WRAP_PYTHONQT
  TARGET_LIBRARIES ${APPLIB_TARGET_LIBRARIES}
  INCLUDE_DIRECTORIES ${APPLIB_DIRS}
  )
</code></pre>
<p>CMake variable <code>APPLIB_SRCS</code> contains a list of <code>.cxx</code> and <code>.h</code> files that implement both Qt derived widgets and non Qt classes.<br>
<code>APPLIB_MOC_SRCS</code> contains a list of <code>.h</code> files that declare all Qt derived objects with <code>Q_OBJECT</code> macro.</p>
<p>Generated module is called <code>qColadaAppPythonQt</code>. Then I can check binded classes:</p>
<pre><code class="lang-python">import qColadaAppPythonQt

dir(qColadaAppPythonQt)
</code></pre>
<p>There I can see that only half of my classes were binded (half of <code>APPLIB_MOC_SRCS</code> var-list classes)</p>
<p>Also I tried it on both Windows and Ubuntu and seems that on Ubuntu a little more classes were binded than on Windows.</p>

---

## Post #12 by @lassoan (2021-06-30 01:10 UTC)

<p>If a class is not wrapped then most likely it contains something that the wrapper cannot parse. You can determine what it is by commenting out everything in the .h file and gradually adding back lines and see which line is troublesome. If it is not clear why that specific line caused the wrapping to fail then you can ask us here, we may have suggestions for how to change it.</p>

---

## Post #13 by @keri (2021-06-30 14:09 UTC)

<p>I’m afraidn that the very simple exmple doesn’t work.</p>
<p>In my project I have <code>qColadaH5TreeView</code> base class that is inherited by some other classes. But it is difficult to comment something directly in this class as it would lead to many code changes in project.</p>
<p>Thus I created <code>qColadaH5TreeView_TEST</code> class wich is the same but with postfix <code>_TEST</code>. I have cut almost everything from it. Here it is:<br>
<strong>qColadaH5TreeView_TEST.h</strong></p>
<pre><code class="lang-cpp">#ifndef __qColadaH5TreeView_TEST_h
#define __qColadaH5TreeView_TEST_h

// Qt includes
#include &lt;QTreeView&gt;

// Colada includes
#include "qColadaAppExport.h"

class qColadaH5TreeView_TESTPrivate;

class Q_COLADA_APP_EXPORT qColadaH5TreeView_TEST : public QTreeView {
  Q_OBJECT

public:
  explicit qColadaH5TreeView_TEST(QWidget *parent = nullptr);
  virtual ~qColadaH5TreeView_TEST() override;

protected:
  QScopedPointer&lt;qColadaH5TreeView_TESTPrivate&gt; d_ptr;

  explicit qColadaH5TreeView_TEST(qColadaH5TreeView_TESTPrivate *pimpl,
                             QWidget *parent);

private:
  Q_DECLARE_PRIVATE(qColadaH5TreeView_TEST);
  Q_DISABLE_COPY(qColadaH5TreeView_TEST);
};

#endif
</code></pre>
<p><strong>qColadaH5TreeView_TEST.cxx</strong></p>
<pre><code class="lang-cpp">// Colada includes
#include "qColadaH5TreeView_TEST.h"
#include "qColadaH5TreeView_TEST_p.h"

qColadaH5TreeView_TESTPrivate::qColadaH5TreeView_TESTPrivate(qColadaH5TreeView_TEST &amp;q)
    : q_ptr(&amp;q) {}

qColadaH5TreeView_TESTPrivate::~qColadaH5TreeView_TESTPrivate() {}

void qColadaH5TreeView_TESTPrivate::init() {
  Q_Q(qColadaH5TreeView_TEST);
  // do some initialization
}

qColadaH5TreeView_TEST::qColadaH5TreeView_TEST(QWidget *parent)
    : QTreeView(parent), d_ptr(new qColadaH5TreeView_TESTPrivate(*this)) {
  Q_D(qColadaH5TreeView_TEST);
  d-&gt;init();
}

qColadaH5TreeView_TEST::qColadaH5TreeView_TEST(qColadaH5TreeView_TESTPrivate *pimpl, QWidget *parent)
    : QTreeView(parent), d_ptr(pimpl) {
  // init() is called by derived class.
}

qColadaH5TreeView_TEST::~qColadaH5TreeView_TEST() {}
</code></pre>
<p><strong>qColadaH5TreeView_TEST_p.h</strong></p>
<pre><code class="lang-cpp">#ifndef __qColadaH5TreeView_TEST_p_h
#define __qColadaH5TreeView_TEST_p_h

// Colada includes
#include "qColadaH5TreeView_TEST.h"

class Q_COLADA_APP_EXPORT qColadaH5TreeView_TESTPrivate
{
	Q_DECLARE_PUBLIC(qColadaH5TreeView_TEST);

protected:
	qColadaH5TreeView_TEST* const q_ptr;

public:
	typedef qColadaH5TreeView_TESTPrivate Superclass;
	qColadaH5TreeView_TESTPrivate(qColadaH5TreeView_TEST&amp; q);
	virtual ~qColadaH5TreeView_TESTPrivate();

	virtual void init();
};

#endif
</code></pre>
<p>For this class I still can’t get bindings. These files are included to my project but I don’t use this <code>qColadaH5TreeView_TEST</code> anywhere (I don’t know should I use it to make bindings?) but <code>qColadaH5TreeView</code> is in use of course.</p>
<p>The build output is:</p>
<pre><code class="lang-auto">Build started...
1&gt;------ Build started: Project: SlicerConfigureVersionHeader, Configuration: Debug x64 ------
2&gt;------ Build started: Project: vtkITKHierarchy, Configuration: Debug x64 ------
3&gt;------ Build started: Project: vtkAddonHierarchy, Configuration: Debug x64 ------
4&gt;------ Build started: Project: vtkSegmentationCoreHierarchy, Configuration: Debug x64 ------
1&gt;Configuring vtkSlicerVersionConfigure.h
4&gt;For vtkSegmentationCore - updating vtkSegmentationCoreHierarchy.txt
1&gt;-- Configuring Colada release type [Experimental]
1&gt;-- Found Git: C:/Program Files/Git/cmd/git.exe
1&gt;-- Configuring Slicer version [4.13.0-2021-05-10]
1&gt;-- Configuring Slicer revision [29890]
1&gt;-- Configuring Colada version [0.1.0-2021-03-30]
1&gt;-- Configuring Colada revision [2]
5&gt;------ Build started: Project: vtkTeemHierarchy, Configuration: Debug x64 ------
6&gt;------ Build started: Project: MRMLCoreHierarchy, Configuration: Debug x64 ------
7&gt;------ Build started: Project: MRMLLogicHierarchy, Configuration: Debug x64 ------
8&gt;------ Build started: Project: MRMLCLIHierarchy, Configuration: Debug x64 ------
9&gt;------ Build started: Project: SlicerBaseLogicHierarchy, Configuration: Debug x64 ------
10&gt;------ Build started: Project: qColadaApp, Configuration: Debug x64 ------
10&gt;Generating moc_qColadaH5TreeView_TEST.cpp
10&gt;qColadaH5TreeView_TEST.cxx
10&gt;moc_qColadaH5TreeView_TEST.cpp
10&gt;Generating Code...
10&gt;qColadaApp.vcxproj -&gt; C:\C\d\Slicer-build\bin\Debug\qColadaApp.dll
========== Build: 10 succeeded, 0 failed, 18 up-to-date, 0 skipped ==========
</code></pre>
<p>By the way more complex classes that uses third party libraries inside the logic and are inherited from <code>QDialog</code> or <code>QTableView</code> are binded without problems.</p>

---

## Post #14 by @lassoan (2021-07-02 18:23 UTC)

<p>Thank you, this will be useful. Could you attach your CMakeLists.txt file as well?</p>

---

## Post #15 by @keri (2021-07-02 23:29 UTC)

<p>sure, here is the <code>CMakeLists.txt</code> where I use Slicer’s macro to build libs:</p>
<pre><code class="lang-auto">#============================================================================
#
# Copyright (c) Kitware, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0.txt
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#============================================================================

project(ColadaApp)

include(SlicerMacroBuildApplication)

# --------------------------------------------------------------------------
# Properties
# --------------------------------------------------------------------------
SlicerReadApplicationProperties()

# --------------------------------------------------------------------------
# Folder
# --------------------------------------------------------------------------
set(${PROJECT_NAME}_FOLDER "App-${PROJECT_NAME}")

find_package(OpenMP REQUIRED) # Colada needs OpenMP
find_package(ZLIB REQUIRED)
find_package(HDF5 REQUIRED CONFIG)  # based on HDF5_DIR
find_package(h5geo REQUIRED CONFIG)  # based on h5geo_DIR
find_package(GDAL REQUIRED)

# GDAL::GDAL depends on many libs (TIFF, GEOS etc). Here we are linking them
if(DEFINED GDAL_LIBS)
  target_link_libraries(GDAL::GDAL INTERFACE ${GDAL_LIBS})
endif()

# --------------------------------------------------------------------------
# Application library
# --------------------------------------------------------------------------
set(APPLIB_NAME "q${PROJECT_NAME}")

set(APPLIB_SRCS
  qColadaH5TreeView_TEST.cxx
  qColadaH5TreeView_TEST.h


  qColadaAppMainWindow.cxx
  qColadaAppMainWindow.h

  ColadaDBCore.cxx
  ColadaDBCore.h
  ColadaUtil.cxx
  ColadaUtil.h
  
  qAppStyle.cxx
  qAppStyle.h
  qColadaNewProject.cxx
  qColadaNewProject.h
  qCRSDropTableView.h
  qCRSDropTableView.cxx
  qCRSWidget.cxx
  qCRSWidget.h
  qREValidator.cxx
  qREValidator.h
  qColadaH5TreeView.cxx
  qColadaH5TreeView.h
  qColadaH5SeisTreeView.cxx
  qColadaH5SeisTreeView.h
  qColadaH5SurfTreeView.cxx
  qColadaH5SurfTreeView.h
  qColadaH5WellTreeView.cxx
  qColadaH5WellTreeView.h
  qColadaH5Item.cxx
  qColadaH5Item.h
  qColadaH5ItemDelegate.cxx
  qColadaH5ItemDelegate.h
  qColadaH5Model.cxx
  qColadaH5Model.h
  qColadaH5SeisModel.cxx
  qColadaH5SeisModel.h
  qColadaH5SurfModel.cxx
  qColadaH5SurfModel.h
  qColadaH5WellModel.cxx
  qColadaH5WellModel.h
  qColadaH5ProxyModel.cxx
  qColadaH5ProxyModel.h
  qColadaReader.h
  qColadaReader.cxx
  qCopyPasteTableView.h
  qCopyPasteTableView.cxx
  qScienceSpinBox.h
  qScienceSpinBox.cxx
  qColadaSegyReader.h
  qColadaSegyReader.cxx
  qComboBoxDelegate.h
  qComboBoxDelegate.cxx
  qSpinBoxDelegate.h
  qSpinBoxDelegate.cxx
  qScienceSpinBoxDelegate.h
  qScienceSpinBoxDelegate.cxx
  qLineEditDelegate.h
  qLineEditDelegate.cxx
  qPathEditDelegate.h
  qPathEditDelegate.cxx
  SegyRead.h
  SegyRead.cxx
  )

set(APPLIB_MOC_SRCS
  qColadaH5TreeView_TEST.h


  qColadaAppMainWindow.h
  qAppStyle.h
  qColadaNewProject.h
  qCRSDropTableView.h
  qCRSWidget.h
  qREValidator.h
  qColadaH5TreeView.h
  qColadaH5SurfTreeView.h
  qColadaH5SeisTreeView.h
  qColadaH5WellTreeView.h
  qColadaH5ItemDelegate.h
  qColadaH5Model.h
  qColadaH5SurfModel.h
  qColadaH5SeisModel.h
  qColadaH5WellModel.h
  qColadaH5ProxyModel.h
  qColadaReader.h
  qCopyPasteTableView.h
  qScienceSpinBox.h
  qColadaSegyReader.h
  qComboBoxDelegate.h
  qSpinBoxDelegate.h
  qScienceSpinBoxDelegate.h
  qLineEditDelegate.h
  qPathEditDelegate.h
  )

set(APPLIB_UI_SRCS
  )

set(APPLIB_RESOURCES
  Resources/App.qrc
  )

set(APPLIB_TARGET_LIBRARIES 
  # ColadaCore  # this may be useful when splitting qColadaApp by few subprojects
  OpenMP::OpenMP_CXX
  hdf5::hdf5-shared
  h5geo
  GDAL::GDAL
  ${julia_LIBS}
  )

# Sanity checks
set(include_dirs
  ${Eigen3_INCLUDE_DIR}
  ${h5gt_INCLUDE_DIR}
  ${magic_enum_INCLUDE_DIR}
  ${julia_INCLUDE_DIR}
  )

foreach(var ${include_dirs})
  if(NOT EXISTS "${var}")
    message(FATAL_ERROR "Path to include dir: ${var} doesn't exist!")
  endif()
endforeach()

set(APPLIB_DIRS 
  ${Eigen3_INCLUDE_DIR}
  ${h5gt_INCLUDE_DIR}
  ${magic_enum_INCLUDE_DIR}
  ${julia_INCLUDE_DIR}
  )

slicerMacroBuildAppLibrary(
  NAME ${APPLIB_NAME}
  DESCRIPTION_SUMMARY ${${PROJECT_NAME}_DESCRIPTION_SUMMARY}
  DESCRIPTION_FILE ${${PROJECT_NAME}_DESCRIPTION_FILE}
  APPLICATION_NAME ${${PROJECT_NAME}_APPLICATION_NAME}
  EXPORT_DIRECTIVE "Q_COLADA_APP_EXPORT"
  FOLDER ${${PROJECT_NAME}_FOLDER}
  SRCS ${APPLIB_SRCS}
  MOC_SRCS ${APPLIB_MOC_SRCS}
  UI_SRCS ${APPLIB_UI_SRCS}
  RESOURCES ${APPLIB_RESOURCES}
  WRAP_PYTHONQT
  TARGET_LIBRARIES ${APPLIB_TARGET_LIBRARIES}
  INCLUDE_DIRECTORIES ${APPLIB_DIRS}
  )

# --------------------------------------------------------------------------
# Application executable
# --------------------------------------------------------------------------

# Configure launcher only for the main application
set(extra_args)
if(${PROJECT_NAME} STREQUAL ${Slicer_MAIN_PROJECT})
  set(extra_args CONFIGURE_LAUNCHER)
endif()

set(APP_SRCS
  Main.cxx
  )

set(APP_TARGET_LIBRARIES ${APPLIB_NAME})

slicerMacroBuildApplication(
  NAME ${PROJECT_NAME}
  APPLICATION_NAME ${${PROJECT_NAME}_APPLICATION_NAME}
  LAUNCHER_SPLASHSCREEN_FILE ${${PROJECT_NAME}_LAUNCHER_SPLASHSCREEN_FILE}
  APPLE_ICON_FILE ${${PROJECT_NAME}_APPLE_ICON_FILE}
  WIN_ICON_FILE ${${PROJECT_NAME}_WIN_ICON_FILE}
  LICENSE_FILE ${${PROJECT_NAME}_LICENSE_FILE}
  FOLDER ${${PROJECT_NAME}_FOLDER}
  SRCS ${APP_SRCS}
  TARGET_LIBRARIES ${APP_TARGET_LIBRARIES}
  TARGET_NAME_VAR "APP_TARGET_NAME"
  DEFAULT_SETTINGS_FILE Resources/Settings/DefaultSettings.ini
  ${extra_args}
  )

#-----------------------------------------------------------------------------
message("Slicer_INSTALL_ROOT: ${Slicer_INSTALL_ROOT}")
message("Slicer_INSTALL_BIN_DIR: ${Slicer_INSTALL_BIN_DIR}")
message("julia_ROOT: ${julia_ROOT}")
# Install extension deps packages
# install(CODE "message(\"CPack: - Install directory: ${julia_ROOT}\")")
install(
  DIRECTORY ${julia_ROOT}/  # '/' in the end is necessary
  DESTINATION ${Slicer_INSTALL_ROOT}/julia
  COMPONENT RuntimeLibraries  # 'ALL' doesn't work
  )

# Install libraries
include(${Slicer_SOURCE_DIR}/CMake/SlicerFunctionInstallLibrary.cmake)
slicerInstallLibrary(
  FILE ${HDF5_ROOT}/lib/hdf5
  DESTINATION ${Slicer_INSTALL_BIN_DIR}
  COMPONENT RuntimeLibraries
  )
slicerInstallLibrary(
  FILE ${h5geo_ROOT}/lib/h5geo
  DESTINATION ${Slicer_INSTALL_BIN_DIR}
  COMPONENT RuntimeLibraries
  )

set(EXTENSION_NAME Colada)
set(CPACK_INSTALL_CMAKE_PROJECTS "${CPACK_INSTALL_CMAKE_PROJECTS};${HDF5_ROOT};HDF5;ALL;/")
set(CPACK_INSTALL_CMAKE_PROJECTS "${CPACK_INSTALL_CMAKE_PROJECTS};${h5geo_ROOT};h5geo;ALL;/")
set(CPACK_INSTALL_CMAKE_PROJECTS "${CPACK_INSTALL_CMAKE_PROJECTS};${julia_ROOT};julia;ALL;/")

#-----------------------------------------------------------------------------
# list(APPEND CPACK_INSTALL_CMAKE_PROJECTS "${CMAKE_BINARY_DIR};${EXTENSION_NAME};ALL;/")
# list(APPEND CPACK_INSTALL_CMAKE_PROJECTS "${${EXTENSION_NAME}_CPACK_INSTALL_CMAKE_PROJECTS}")
# include(${Slicer_EXTENSION_GENERATE_CONFIG})
# include(${Slicer_SOURCE_DIR}/CMake/SlicerCPack.cmake)
include(${Slicer_SOURCE_DIR}/CMake/SlicerExtensionGenerateConfig.cmake)
include(${Slicer_SOURCE_DIR}/CMake/SlicerExtensionCPack.cmake)

message("HDF5_ROOT: ${HDF5_ROOT}")
message("CPACK_INSTALL_CMAKE_PROJECTS: ${CPACK_INSTALL_CMAKE_PROJECTS}")
</code></pre>

---

## Post #16 by @keri (2021-07-13 23:26 UTC)

<p>I’m sorry, that was my carelessness…<br>
I simply had to rebuild project <code>qColadaAppPythonQt</code> in visual studio (previously I only used to rebuild <code>qColadaApp</code> project)</p>
<p>Now I can see that all my widgets are binded in python</p>

---

## Post #17 by @lassoan (2021-07-14 01:29 UTC)

<p>It’s great that you’ve figured it out. I reviewed the code and did not find anything wrong and wanted to build these files - but now I don’t need to!</p>

---

## Post #18 by @keri (2021-07-17 10:10 UTC)

<p>Is it possible to bind C++ functions in namespace using PythonQt?</p>
<p>For example I have:</p>
<pre><code class="lang-cpp">namespace dbcore {
///
/// \brief createDB creates new database as a DEFAULT connection
/// \param fullName
/// \return NOT opened DB
///
QSqlDatabase Q_COLADA_APP_EXPORT createDB(const QString &amp;prjPath, QString &amp;prjName){
  if (QFileInfo(prjName).suffix().compare("db", Qt::CaseInsensitive) != 0) {
    prjName += ".db";
  }
  QDir dir(prjPath + "/" + prjName);
  QString DBFullName = dir.absolutePath();
  QSqlDatabase DB =
      QSqlDatabase::addDatabase("QSQLITE"); // it will be default connection
  DB.setDatabaseName(DBFullName);
  return DB;
}

} // dbcore
</code></pre>
<p>and I’m thinking to make python bindings for <code>dbcore::createDB(const QString &amp;prjPath, QString &amp;prjName)</code> function.<br>
Using <code>WRAP_PYTHONQT</code> flag inside cmake script doesn’t work of course.<br>
I guess it should be done in similar way as it is done in <a href="https://github.com/MeVisLab/pythonqt/blob/8137f1fff3d3996d8fb6a49c0f502852c29b929f/tests/PythonQtTests.cpp#L74" rel="noopener nofollow ugc">PythonQt tests</a> but here I bind function and not a class…</p>
<p>Maybe somebody has experience of doing that?</p>

---

## Post #19 by @lassoan (2021-07-17 22:49 UTC)

<p>If you use PythonQt for Python wrapping then you can use decorators to make static or global functions available. See fore example here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/CTK/blob/693c99ab5e76ebc664194219d1583508df758879/Libs/Core/ctkCorePythonQtDecorators.h#L239-L253">
  <header class="source">

      <a href="https://github.com/commontk/CTK/blob/693c99ab5e76ebc664194219d1583508df758879/Libs/Core/ctkCorePythonQtDecorators.h#L239-L253" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/693c99ab5e76ebc664194219d1583508df758879/Libs/Core/ctkCorePythonQtDecorators.h#L239-L253" target="_blank" rel="noopener">commontk/CTK/blob/693c99ab5e76ebc664194219d1583508df758879/Libs/Core/ctkCorePythonQtDecorators.h#L239-L253</a></h4>



  <pre class="onebox">    <code class="lang-h">
      <ol class="start lines" start="239" style="counter-reset: li-counter 238 ;">
          <li>class PythonQtWrapper_CTKCore : public QObject</li>
          <li>{</li>
          <li>  Q_OBJECT</li>
          <li>
          </li>
<li>public Q_SLOTS:</li>
          <li>  QString static_ctkCoreUtils_absolutePathFromInternal(const QString&amp; internalPath, const QString&amp; basePath)</li>
          <li>    {</li>
          <li>    return ctk::absolutePathFromInternal(internalPath, basePath);</li>
          <li>    }</li>
          <li>
          </li>
<li>  QString static_ctkCoreUtils_internalPathFromAbsolute(const QString&amp; absolutePath, const QString&amp; basePath)</li>
          <li>    {</li>
          <li>    return ctk::internalPathFromAbsolute(absolutePath, basePath);</li>
          <li>    }</li>
          <li>};</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #20 by @keri (2021-07-19 23:35 UTC)

<p>One more question about PythonQt wrapper:</p>
<p>I’m trying to wrap C++ class that has a method that accept third party-library’s type argument and that third party library is C++ library that also has python bindings using <strong>pybind11</strong>. So PythonQt doesn’t know how that third party class looks in python and thus I cannot pass object of that class as an argument in python.</p>
<p><strong>For examle:</strong><br>
I have a simple class:</p>
<pre><code class="lang-cpp">#ifndef __qColadaTreeTEST_h
#define __qColadaTreeTEST_h

// Qt includes
#include &lt;QTreeView&gt;

// Colada includes
#include "qColadaAppExport.h"

// h5gt includes
#include &lt;h5gt/H5File.hpp&gt;  // has python bindings using pybind11 

class Q_COLADA_APP_EXPORT qColadaTreeTEST : public QTreeView {
  Q_OBJECT

public:
  explicit qColadaTreeTEST(QWidget *parent = nullptr);
  ~qColadaTreeTEST() = default;

public slots:
  bool addH5File(h5gt::File file);  // file -  is of type `h5gt::File` -&gt; it has python bindings
};

#endif
</code></pre>
<p>Here <code>bool addH5File(h5gt::File file)</code> accepts <code>h5gt::File</code>-type argument. <code>h5gt</code> is a C++ library and I wrote python bindings for it using <code>pybind11</code>. <code>h5gt</code> library is available in my SlicerCAT.</p>
<p>After PythonQt has successfully created bindings for <code>qColadaTreeTEST</code> I do in SlicerCAT’s python:</p>
<pre><code class="lang-python">import qColadaAppPythonQt
q = qColadaAppPythonQt.qColadaTreeTEST()

from h5gtpy import h5gt
file_name = 'D:/tmp/test.h5'
file = h5gt.File(file_name, h5gt.OpenFlag(h5gt.ReadWrite | h5gt.Create | h5gt.Truncate))

q.addH5File(file) // here I get the following error:

Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
ValueError: Called addH5File(h5gt::File file) -&gt; bool with wrong arguments: (&lt;h5gtpy._h5gt.File object at 0x0000022035169730&gt;,)
</code></pre>
<p>thus python (and PythonQt) can’t match C++ class <code>h5gt::File</code> with python <code>h5gtpy._h5gt.File</code> python type. How to inform PythonQt that <code>h5gt::File</code> C++ class is the same as <code>h5gtpy._h5gt.File</code> in python?</p>
<p>P.S.<br>
I did exactly the same using pybind when I was writing python wrapper for my <code>h5geo</code> C++ library that depends on <code>h5gt</code> and I solved this by preliminary importing <code>h5gt</code> module inside wrapping code:</p>
<pre><code class="lang-cpp">PYBIND11_MODULE(_h5geo, m) {
  py::module_::import("h5gtpy._h5gt"); // this code informs pybind about h5gt types

...
}
</code></pre>
<p>Probably I should act in similar way? Can’t understand where should I import <code>h5gt</code> module as it needs to be compiled (it must be already known) before <code>qColadaTreeTEST</code> class is compiled.</p>
<p>Now the wrapper for <code>qColadaTreeTEST</code> is done automatically using <code>WRAP_PYTHONQT</code> key word inside Slicer’s macro in CMakeLists.txt</p>

---

## Post #21 by @lassoan (2021-07-20 00:07 UTC)

<p>PythonQt does not know anything about VTK either and it just works fine. See some more information <a href="https://mevislab.github.io/pythonqt/Developer.html">here</a> (CPP wrapping section). You can have a look how it is all set up for VTK in CTK and if you cannot figure out how this all works from VTK’s example then you can <a href="https://github.com/MeVisLab/pythonqt/issues">ask help from PythonQT developers</a>.</p>

---

## Post #22 by @keri (2021-07-20 16:54 UTC)

<p>One more thing:</p>
<p>As I see only classes that has default constructors (in sense they can be constructed with no arguments passed) are wrapped automatically using <code>WRAP_PYTHONQT</code>.</p>
<p>For example slicer’s <code>qSlicerModulesMenu</code> (from <code>qSlicerBaseQTGUI</code> lib) has two constructors:</p>
<pre><code class="lang-cpp">  qSlicerModulesMenu(const QString&amp; title, QWidget* parent = nullptr);
  qSlicerModulesMenu(QWidget* parent = nullptr);
</code></pre>
<p>but only one (the second one) is available in python.</p>
<p>Is it possible to bind the first constructor as well?</p>

---

## Post #23 by @lassoan (2021-07-20 19:35 UTC)

<p>Yes, you just need to create the appropriate methods in the decorator classes. These are not simple things and not easy to find documentation, but there are several examples for these in CTK, that you can copy-paste and adapt to your classes.</p>

---
