# How to build module dependencies with CMakeLists.txt?

**Topic ID**: 20371
**Date**: 2021-10-26
**URL**: https://discourse.slicer.org/t/how-to-build-module-dependencies-with-cmakelists-txt/20371

---

## Post #1 by @joachim (2021-10-26 20:24 UTC)

<p>Consider an extension with two modules <em>Wheel</em> and <em>Car</em> :</p>
<pre><code class="lang-auto">.
├── CMakeLists.txt
├── Car
│   ├── CMakeLists.txt
│   ├── Widgets
│   │   ├── CMakeLists.txt
│   │   ├── qSlicerCarFooBarWidget.cxx
│   │   └── qSlicerCarFooBarWidget.h
│   ├── qSlicerCarModule.cxx
│   ├── qSlicerCarModule.h
│   ├── qSlicerCarModuleWidget.cxx
│   └── qSlicerCarModuleWidget.h
└── Wheel
    ├── CMakeLists.txt
    ├── Widgets
    │   ├── CMakeLists.txt
    │   ├── qSlicerWheelFooBarWidget.cxx
    │   └── qSlicerWheelFooBarWidget.h
    ├── qSlicerWheelModule.cxx
    ├── qSlicerWheelModule.h
    ├── qSlicerWheelModuleWidget.cxx
    └── qSlicerWheelModuleWidget.h
</code></pre>
<p>The module <em>Car</em> depends on some of the classes in module <em>Wheel</em> (for example <code>qSlicerWheelFooBarWidget</code>). What do I need to put in <code>./Car/CMakeLists.txt</code> and <code>./CMakeLists.txt</code> in order to successfully build <em>Car</em>?</p>
<p><em>Extension Wizard</em> just creates an extension with two independent module projects;  my build fails because project <em>Car</em> can’t find header files located in project <em>Wheel</em>.</p>
<p>Should I also manually override the virtual <code>qSlicerCarModule::dependencies() const</code> method and add <code>Wheel</code>?</p>

---

## Post #2 by @lassoan (2021-10-26 21:08 UTC)

<p>Nothing special is needed, just add the library that you want to use to the list of target libraries and add the directory that contains header files to the include directories. See for example how CropVolume uses the Volumes module.</p>

---

## Post #3 by @joachim (2021-10-26 22:36 UTC)

<p>Thanks, this did actually work! Funny that I had actually been looking at the  <code>CMakeLists.txt</code> of <em>CropVolume</em> but couldn’t get it right the first time.</p>
<p>I guess I should add <code>Wheel</code> to the implementation of <code>qSlicerWheelModule::dependencies()</code> too:</p>
<pre><code class="lang-auto">QStringList qSlicerCarModule::dependencies() const
{
    return Superclass::dependencies() &lt;&lt; "Wheel";
}
</code></pre>

---

## Post #4 by @lassoan (2021-10-27 03:57 UTC)

<p>Yes, you need to add the modules that your modules depends on in <code>dependencies()</code> method. It is used for determining startup order of the modules.</p>

---
