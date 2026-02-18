# Crash on Slicer Startup on Qt5 Linux Mint

**Topic ID**: 15774
**Date**: 2021-02-01
**URL**: https://discourse.slicer.org/t/crash-on-slicer-startup-on-qt5-linux-mint/15774

---

## Post #1 by @RobinMontferme (2021-02-01 14:09 UTC)

<p>Hello, I have recently tried to build the latest version of Slicer4 (4.13.0-2021-01-30).</p>
<p>I am using Linux Mint 20.1 (based on Ubuntu 20.04 Focal Fossa)</p>
<p>I also opened a github issue related  to said problem <a href="https://github.com/Slicer/Slicer/issues/5420" rel="noopener nofollow ugc">here</a>.</p>
<p>After building from source using the nightly development guide, the application crashes after the startup splash screen. After some debugging with gdb, I’ve found out that the program  <code>SlicerApp-real</code> in the <code>bin</code> dir of the build segfaults.</p>
<p>Here is the stack trace from gdb (which can also be found on the github issue linked):</p>
<pre><code class="lang-auto">#1  0x00007fffe1fa8c3c in QDialogButtonBox::setStandardButtons(QFlags&lt;QDialogButtonBox::StandardButton&gt;) () at /usr/lib/x86_64-linux-gnu/libQt5Widgets.so.5
#2  0x00007ffff73f080f in Ui_ctkSettingsDialog::setupUi(QDialog*) (this=0x555556d0e740, ctkSettingsDialog=0x555556cd1510) at /home/robin/work/Projet/3D_slicer/Slicer-SuperBuild-Debug/CTK-build/CTK-build/Libs/Widgets/ui_ctkSettingsDialog.h:57
#3  0x00007ffff73edbfb in ctkSettingsDialogPrivate::init() (this=0x555556d0e740) at /home/robin/work/Projet/3D_slicer/Slicer-SuperBuild-Debug/CTK/Libs/Widgets/ctkSettingsDialog.cpp:75
#4  0x00007ffff73ee9e4 in ctkSettingsDialog::ctkSettingsDialog(QWidget*) (this=0x555556cd1510, _parent=0x0) at /home/robin/work/Projet/3D_slicer/Slicer-SuperBuild-Debug/CTK/Libs/Widgets/ctkSettingsDialog.cpp:187
#5  0x00007ffff7b98ba1 in qSlicerApplicationPrivate::init() (this=0x555555adbb40) at /home/robin/work/Projet/3D_slicer/Slicer/Base/QTGUI/qSlicerApplication.cxx:267
#6  0x00007ffff7b999a1 in qSlicerApplication::qSlicerApplication(int&amp;, char**) (this=0x7fffffffda90, _argc=@0x7fffffffda3c: 1, _argv=0x7fffffffdc08) at /home/robin/work/Projet/3D_slicer/Slicer/Base/QTGUI/qSlicerApplication.cxx:373
#7  0x000055555555cfc6 in (anonymous namespace)::SlicerAppMain(int, char**) (argc=1, argv=0x7fffffffdc08) at /home/robin/work/Projet/3D_slicer/Slicer/Applications/SlicerApp/Main.cxx:40
#8  0x000055555555d2fe in main(int, char**) (argc=1, argv=0x7fffffffdc08) at /home/robin/work/Projet/3D_slicer/Slicer/Base/QTApp/qSlicerApplicationMainWrapper.cxx:56

</code></pre>
<p>Chances are that it might be  related to Qt only, I’ve tried re-installing the lib and I might try recompiling the super-build again. Aside that I really don’t know where to look.</p>
<p><strong>EDIT</strong><br>
I forgot to add that a colleague managed to get it working on it’s own machine which actually runs Ubuntu 20.04 and it works for him.</p>

---

## Post #2 by @lassoan (2021-02-01 14:39 UTC)

<p>Yes, Qt have lots of issues on Ubuntu 20. Until a linux expert comes to help, you might check out notes in <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux">Slicer install instructions for linux</a> and still open Linux issues (such as <a href="https://github.com/Slicer/Slicer/issues/5286">5286</a> or <a href="https://github.com/Slicer/Slicer/issues/5228">5228</a>).</p>

---

## Post #3 by @RobinMontferme (2021-02-01 14:49 UTC)

<p>I forgot to add that a colleague managed to get it working on it’s own machine which actually runs Ubuntu 20.04 and it works for him.</p>

---

## Post #4 by @pieper (2021-02-01 15:04 UTC)

<p>Yes, Ubuntu 20.04 works very well for me, but 20.10 still has trouble.</p>

---
