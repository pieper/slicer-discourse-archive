---
topic_id: 21878
title: "Can You Use Slicer Modules Within Another Pyqt Project"
date: 2022-02-09
url: https://discourse.slicer.org/t/21878
---

# Can you use slicer modules within another pyqt project

**Topic ID**: 21878
**Date**: 2022-02-09
**URL**: https://discourse.slicer.org/t/can-you-use-slicer-modules-within-another-pyqt-project/21878

---

## Post #1 by @dj_96 (2022-02-09 20:18 UTC)

<p>I want to build a pyqt application that uses a couple of the functions from 3d slicer like loading models and viewing them with vtk but to have a very different UI with extra functionality . Is there a good way to use 3d Slicer modules from a python application or would you have to build slicer and strip out extra functionality?</p>

---

## Post #2 by @lassoan (2022-02-09 20:49 UTC)

<p>Yes, there are several options for this. Slicer uses PythonQt for Qt wrapping, but it was reported to work well pyqt, probably you just need to make sure that you use the same Qt version in pyqt as in Slicer’s Qt. What you may find unusual that the application will not be Python.exe anymore but Slicer.exe.</p>
<p>Hiding everything that you don’t need is a very common use case for custom Slicer applications. The cleanest, most configurable way to customize what is shown of the Slicer user interface can be achieved by using the <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/">Slicer custom application template</a>. It takes care of creating a fully self-contained application that includes Slicer core, Python, and all required Slicer extensions, Python packages, etc. and provides single-file desktop application installer packages that even non-technical end-users can easily use.</p>
<p>Slicer custom application template is a C++ project, so if you are not comfortable with building that then a simpler alternative is to just launch the application and in the startup script hide everything that you don’t need using <code>set...Visible</code> functions in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer.util">slicer.util</a> and add all your Qt widgets to the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.mainWindow">Qt application main window</a>. In this approach you won’t have a single-file installer, but since Slicer is fully portable, users can “install” it by simply making a copy of the entire Slicer folder. See more information and simple example <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">here</a>.</p>

---

## Post #3 by @dj_96 (2022-02-09 21:04 UTC)

<p>Thanks for the quick reply,</p>
<p>I haven’t worked with C++ so hiding the modules seems more approachable. If I just hide all the modules and use my own pyqt5 widgets for the extended functionality will the program be substantially slower than building from the template in C++, or how much overhead does keeping all of slicer add to performance? I mainly want to do some work with opencv in half of the window while making use of some of the modules for 3d models in the remaining window space? And this would be directly adding pyqt widgets in the startup script or does it made sense to build a custom extention?</p>

---

## Post #4 by @lassoan (2022-02-09 22:51 UTC)

<aside class="quote no-group" data-username="dj_96" data-post="3" data-topic="21878">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/3ec8ea/48.png" class="avatar"> dj_96:</div>
<blockquote>
<p>If I just hide all the modules and use my own pyqt5 widgets for the extended functionality will the program be substantially slower than building from the template in C++, or how much overhead does keeping all of slicer add to performance?</p>
</blockquote>
</aside>
<p>There is no difference in performance. Python is just a thin wrapper over various libraries and toolkits implemented in C++. The only difference is in packaging (you don’t get a single-file installer), and when you start the application you may see a flicker in the application window (the default widgets might appear for a fraction of a second before they are replaced by your GUI).</p>
<aside class="quote no-group" data-username="dj_96" data-post="3" data-topic="21878">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/3ec8ea/48.png" class="avatar"> dj_96:</div>
<blockquote>
<p>And this would be directly adding pyqt widgets in the startup script or does it made sense to build a custom extention?</p>
</blockquote>
</aside>
<p>You can simply run your Python code with Slicer (<code>Slicer.exe --python-script c:/folder/myscrip.py</code>) which hides what you don’t need and adds your widgets. However, it probably makes things easier if you put that script into a Slicer module, because you get convenience features, such as reloading the script without restarting the application, a widget in the Slicer module where you can add testing and debugging features (e.g., load some test data, start tests, …).</p>
<aside class="quote no-group" data-username="dj_96" data-post="3" data-topic="21878">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/3ec8ea/48.png" class="avatar"> dj_96:</div>
<blockquote>
<p>I mainly want to do some work with opencv in half of the window while making use of some of the modules for 3d models in the remaining window space?</p>
</blockquote>
</aside>
<p>Are you using OpenCV for tracking the patient? With or without markers? Do you use that for augmented reality or just patient registration? There are a couple of groups using Slicer for such tasks. If you describe what you do then you may connect and work together.</p>

---

## Post #5 by @dj_96 (2022-02-10 16:50 UTC)

<p>It’s for augmented reality but I don’t think I have permission to talk in to much detail but we want to run some custom ml models on videos.</p>
<p>So if I were to only use modules for say viewing organs and everything else is custom qt code from my script/module could I still easily access what points a user clicks on in the model view? And is there a way to extend the functionality of that module? It’s nothing too complicated I just want to be able to mark 3d positions on the model and add some custom styling to the 3d viewer.</p>

---

## Post #6 by @lassoan (2022-02-10 21:05 UTC)

<p>Yes, these all sounds doable.</p>
<p>Probably the simplest is to add a Python scripted module that displays the module GUI as usual (loaded from a .ui file) and calls your Python functions. You don’t need to mess with pyqt5 (install a large Qt package, make sure Qt versions are matched, use GPL code in your software, etc.), but instead you can use PythonQt-wrapped Qt that is already bundled with Slicer.</p>

---
