---
topic_id: 26888
title: "Chatgpt Knows A Little About Slicer"
date: 2022-12-22
url: https://discourse.slicer.org/t/26888
---

# ChatGPT knows a little about Slicer

**Topic ID**: 26888
**Date**: 2022-12-22
**URL**: https://discourse.slicer.org/t/chatgpt-knows-a-little-about-slicer/26888

---

## Post #1 by @mhalle (2022-12-22 17:41 UTC)

<p>I tried to ask ChatGPT about 3D Slicer. Here is it’s frighteningly good responses. In some (most?) cases, the responses are convincing but wrong. In general, ChatGPT is very good at writing code, though. I include several questions and answers here:</p>
<h3><a name="p-88000-q-how-do-i-write-an-extension-module-for-3d-slicer-1" class="anchor" href="#p-88000-q-how-do-i-write-an-extension-module-for-3d-slicer-1" aria-label="Heading link"></a>Q: How do I write an extension module for 3D Slicer?</h3>
<p>A: To write an extension module for 3D Slicer, follow these steps:</p>
<ol>
<li>Install 3D Slicer on your computer.</li>
<li>Create a new folder in the “Modules” directory in the 3D Slicer installation folder. This will be the directory for your extension module.</li>
<li>In your extension module directory, create a file called “CMakeLists.txt” and include the following code:</li>
</ol>
<pre><code class="lang-auto">slicerMacroBuildScriptedModule(
  NAME MyModule
  SCRIPT_FILENAME MyModule.py
  RESOURCES MyModule.png
)
</code></pre>
<ol start="4">
<li>Create a Python script called “MyModule.py” in your extension module directory. This script will contain the code for your extension module.</li>
<li>In the “MyModule.py” script, define a class that subclasses “vtk.vtkMRMLAbstractLogic”. This class will contain the logic and functionality of your extension module.</li>
<li>In the class definition, define a method called “processMRMLNodesEvents(self, caller, event, callData)” which will be called whenever a MRML node is modified in 3D Slicer.</li>
<li>Define any additional methods or functions that you want your extension module to have.</li>
<li>In the “MyModule.py” script, create an instance of your class and call the “register()” method on it to register the extension module with 3D Slicer.</li>
<li>In the “Modules” directory, run the “build_all.py” script to build your extension module.</li>
<li>In 3D Slicer, go to the “Modules” menu and select “MyModule” to use your extension module.</li>
</ol>
<h3><a name="p-88000-q-how-do-i-create-a-3d-slicer-module-using-qt-and-python-2" class="anchor" href="#p-88000-q-how-do-i-create-a-3d-slicer-module-using-qt-and-python-2" aria-label="Heading link"></a>Q: How do I create a 3D Slicer module using Qt and Python?</h3>
<p>A: To create a 3D Slicer module using Qt and Python, follow these steps:</p>
<ol>
<li>Install 3D Slicer on your computer and make sure that Qt is included in the installation.</li>
<li>Create a new folder in the “Modules” directory in the 3D Slicer installation folder. This will be the directory for your module.</li>
<li>In your module directory, create a file called “CMakeLists.txt” and include the following code:</li>
</ol>
<pre><code class="lang-auto">slicerMacroBuildScriptedModule(
  NAME MyModule
  SCRIPT_FILENAME MyModule.py
  RESOURCES MyModule.png
  WITH_PYTHONQT
)
</code></pre>
<ol start="4">
<li>Create a Python script called “MyModule.py” in your module directory. This script will contain the code for your module.</li>
<li>In the “MyModule.py” script, import the necessary modules from Qt and Slicer:</li>
</ol>
<pre><code class="lang-auto">from PythonQt import QtCore, QtGui
import slicer
</code></pre>
<ol start="6">
<li>Define a class that subclasses “slicer.qSlicerAbstractModuleWidget” and “QtGui.QWidget”. This class will contain the GUI and functionality of your module.</li>
<li>In the class definition, override the “setup()” method to set up the GUI for your module. Use Qt designer to design the GUI and then use the “loadUi()” method to load the GUI into your module.</li>
<li>Define any additional methods or functions that you want your module to have.</li>
<li>In the “MyModule.py” script, create an instance of your class and call the “register()” method on it to register the module with 3D Slicer.</li>
<li>In the “Modules” directory, run the “build_all.py” script to build your module.</li>
<li>In 3D Slicer, go to the “Modules” menu and select “MyModule” to use your module.</li>
</ol>
<h3><a name="p-88000-q-how-about-a-c-slicer-extension-using-qt-3" class="anchor" href="#p-88000-q-how-about-a-c-slicer-extension-using-qt-3" aria-label="Heading link"></a>Q: How about a C++ Slicer extension using Qt?</h3>
<p>A: To create a 3D Slicer extension using C++ and Qt, follow these steps:</p>
<ol>
<li>Install 3D Slicer on your computer and make sure that Qt is included in the installation.</li>
<li>Create a new folder in the “Modules” directory in the 3D Slicer installation folder. This will be the directory for your extension.</li>
<li>In your extension directory, create a file called “CMakeLists.txt” and include the following code:</li>
</ol>
<pre><code class="lang-auto">slicerMacroBuildModule(
  NAME MyModule
  SRCS MyModule.cxx
  MOC_SRCS MyModule.h
  RESOURCES MyModule.qrc
)
</code></pre>
<ol start="4">
<li>Create a C++ file called “MyModule.cxx” in your extension directory. This file will contain the code for your extension.</li>
<li>In the “MyModule.cxx” file, include the necessary Qt and Slicer headers:</li>
</ol>
<pre><code class="lang-auto">#include &lt;QtGui&gt;
#include &lt;vtkSlicerConfigure.h&gt;
#include "MyModule.h"
</code></pre>
<ol start="6">
<li>Define a class that subclasses “vtkSlicerModuleLogic” and “QObject”. This class will contain the logic and functionality of your extension.</li>
<li>In the class definition, override the “SetMRMLSceneInternal(vtkMRMLScene* newScene)” method to set up the extension when it is added to the MRML scene.</li>
<li>Define any additional methods or functions that you want your extension to have.</li>
<li>In the “MyModule.cxx” file, create an instance of your class and call the “Register()” method on it to register the extension with 3D Slicer.</li>
<li>In the “Modules” directory, run the “build_all.py” script to build your extension.</li>
<li>In 3D Slicer, go to the “Modules” menu and select “MyModule” to use your extension.</li>
</ol>
<h3><a name="p-88000-q-how-do-i-volume-render-a-nifti-file-containing-ct-data-in-3d-slicer-4" class="anchor" href="#p-88000-q-how-do-i-volume-render-a-nifti-file-containing-ct-data-in-3d-slicer-4" aria-label="Heading link"></a>Q: how do I volume render a nifti file containing CT data in 3D Slicer?</h3>
<p>A: To volume render a NIFTI file containing CT data in 3D Slicer, follow these steps:</p>
<ol>
<li>Load the NIFTI file into 3D Slicer by going to the “File” menu and selecting “Add Data”.</li>
<li>In the “Modules” menu, select “Volume Rendering” to open the volume rendering module.</li>
<li>In the “Volume Rendering” module, select the NIFTI file in the “Input Volume” dropdown menu.</li>
<li>Click the “Apply” button to display the volume in the 3D view.</li>
<li>In the “Volume Rendering” module, adjust the rendering settings as desired, such as the color map, threshold, and opacity.</li>
<li>Click the “Apply” button to update the volume rendering with the new settings.</li>
<li>To save the volume rendering, go to the “File” menu and select “Save Screenshot”. Choose a file name and location, and select “Volume” in the “What to Save” dropdown menu. Click “Save” to save the volume rendering.</li>
</ol>
<h3><a name="p-88000-q-what-is-openanatomy-5" class="anchor" href="#p-88000-q-what-is-openanatomy-5" aria-label="Heading link"></a>Q: What is OpenAnatomy?</h3>
<p><strong>[oops! ChatGPT is confidently wrong!]</strong><br>
OpenAnatomy is a software platform that enables users to view, explore, and analyze 3D anatomy data. It is designed to facilitate the development and dissemination of open anatomy resources, including segmented models of organs, bones, and other structures. OpenAnatomy can be used in a variety of settings, including education, research, and clinical practice. It is developed and maintained by the BioMedical Informatics Research Network (BIRN) and is open source, meaning that users can access and modify the source code.</p>
<h3><a name="p-88000-q-can-you-describe-the-dicom-coordinate-system-6" class="anchor" href="#p-88000-q-can-you-describe-the-dicom-coordinate-system-6" aria-label="Heading link"></a>Q: Can you describe the DICOM coordinate system?</h3>
<p><strong>[I believe this isn’t correct.]</strong><br>
The DICOM (Digital Imaging and Communications in Medicine) coordinate system is a standardized system used to represent the location of points and objects in 3D space. It is used in medical imaging to describe the position and orientation of images, as well as the position of structures within the images.</p>
<p>In the DICOM coordinate system, the origin is located at the center of the imaging volume. The x-axis points to the right [is this subject right or observer right?], the y-axis points anteriorly (towards the front of the body) [I believe that’s wrong], and the z-axis points superiorly (towards the head). The orientation of the axes is determined by the orientation of the patient’s body during the imaging process.</p>
<p>The DICOM coordinate system is a right-handed coordinate system, meaning that if the x-axis, y-axis, and z-axis are visualized as three perpendicular lines, then the direction in which the lines form a positive rotation (like the hands on a clock) is considered “right-handed”.</p>
<p>In the DICOM coordinate system, the unit of measure is the millimeter (mm). The dimensions of the imaging volume are also specified in millimeters.</p>

---

## Post #2 by @jamesobutler (2022-12-22 18:11 UTC)

<p>The instructions ChatGPT gave for Slicer are also wrong too haha. They are snippets of things you might do in various places, but put together don’t make sense.</p>
<aside class="quote no-group" data-username="mhalle" data-post="1" data-topic="26888">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar"> mhalle:</div>
<blockquote>
<p>A: To create a 3D Slicer extension using C++ and Qt, follow these steps:</p>
<ol>
<li>Install 3D Slicer on your computer and make sure that Qt is included in the installation.</li>
<li>Create a new folder in the “Modules” directory in the 3D Slicer installation folder. This will be the directory for your extension.</li>
</ol>
</blockquote>
</aside>
<p>To start developing a C++ module you’re not going to install Slicer, but rather build Slicer from source. Creating a new folder in the modules directory is also not going to work out well as described.</p>
<p>ChatGPT using GPT-3.5 model which has info up to Q4 2021 has some snippets of info about Slicer, but nothing that a new person could use. An experienced developer could filter out the junk, but unclear how much time it would save at this point.</p>
<p>What it can do pretty well is help with code that has a really good documented API doc which it knows about from its learning. From my experience if you ask it a basic task to create a function to do something with say <code>numpy</code>, it can do it fairly well.</p>

---

## Post #3 by @mhalle (2022-12-22 18:33 UTC)

<p>Yes, I asked it to write some code for a Babylon.js and React integration, for instance, and the answer was basically right on target. It’s pretty neat that it even attempts to do anything with 3D Slicer. Maybe that’s its biggest weakness as well: it’s eager to please, and doesn’t know when to say “I don’t know” or “I’m not sure”.</p>

---

## Post #4 by @lassoan (2022-12-22 19:02 UTC)

<aside class="quote no-group" data-username="mhalle" data-post="3" data-topic="26888">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar"> mhalle:</div>
<blockquote>
<p>Maybe that’s its biggest weakness as well: it’s eager to please, and doesn’t know when to say “I don’t know” or “I’m not sure”.</p>
</blockquote>
</aside>
<p>I agree, a big limitation that it provides correct and completely wrong information with the exact same confidence. I think Google search is still more effective for finding usage instructions for Slicer, but I would expect that the same technology could work very well if we could restrict it to mine information only from the current Slicer user manual (and maybe recent Slicer forum posts) and make it a bit less confident in answering questions that it doesn’t actually know the answers for.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="26888">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>An experienced developer could filter out the junk, but unclear how much time it would save at this point.</p>
</blockquote>
</aside>
<p>Students in our lab use ChatGPT to generate Python code for Slicer and they say it is already useful for them. The provided code rarely runs correctly as is, but it often contains the necessary methods that they can use. It kind of automates the process of typing the question in Google search, clicking on the top 10 hits, and finding the commonly used coding patterns.</p>

---

## Post #5 by @pieper (2022-12-22 19:31 UTC)

<p>Yes, it would be nice if it combined the code suggestions with links back to the source so that people could learn the context and not just be stuck with a wrong answer.</p>
<p>User interface questions may be even better than programming questions.  I asked “how do I make a segmentation in 3D slicer show as a thick outline with no fill?”, a question which comes up from time to time here on discourse, and I got an answer that is kind of incorrect but maybe useful.  I used google translate to try the same question in Spanish and French and the answers in those languages were similarly potentially helpful as far as I could tell.</p>
<p>It’s easy enough to use and if people find it worth the time investment I guess we’ll just see where that takes us.</p>

---

## Post #6 by @lassoan (2023-02-03 10:28 UTC)

<p>I was just curious and typed one of the <a href="https://discourse.slicer.org/t/dicom-images-raw-or-processed-ones/27611">recent forum questions</a> into chatgpt and it gave remarkably accurate answer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fcd3f16d59460135f6a44c09de2d4e5375f9a75.png" data-download-href="/uploads/short-url/fX2JJHaCIYgZCKn9gD3PIcv5ea9.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fcd3f16d59460135f6a44c09de2d4e5375f9a75_2_690x236.png" alt="image" data-base62-sha1="fX2JJHaCIYgZCKn9gD3PIcv5ea9" width="690" height="236" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fcd3f16d59460135f6a44c09de2d4e5375f9a75_2_690x236.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fcd3f16d59460135f6a44c09de2d4e5375f9a75_2_1035x354.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fcd3f16d59460135f6a44c09de2d4e5375f9a75.png 2x" data-dominant-color="444653"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1216×417 36.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It lacks detailed reasoning and some nuances/exceptions, so it is not ready to completely replace us here, but I find it really impressive.</p>

---

## Post #7 by @lassoan (2023-02-03 10:35 UTC)

<p>Asking more specific question provided some more details, which were also very accurate and comprehensive:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9e73570fb5bab6c7d92ebc70c1e98deb1b1f078.png" data-download-href="/uploads/short-url/sO7kI1Axj0R1zxzqXY82R4Lmrt6.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9e73570fb5bab6c7d92ebc70c1e98deb1b1f078_2_635x500.png" alt="image" data-base62-sha1="sO7kI1Axj0R1zxzqXY82R4Lmrt6" width="635" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9e73570fb5bab6c7d92ebc70c1e98deb1b1f078_2_635x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9e73570fb5bab6c7d92ebc70c1e98deb1b1f078_2_952x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9e73570fb5bab6c7d92ebc70c1e98deb1b1f078.png 2x" data-dominant-color="4A4C5A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1223×962 86.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It is clear, short, I don’t find anything important is missed, it is ordered correctly - starting with the most common/important.</p>

---

## Post #8 by @chir.set (2023-02-03 14:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="26888">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I don’t find anything important is missed</p>
</blockquote>
</aside>
<p>I note ‘Raw images are generally not given to patients’.</p>
<p>If this is generally the case in North America, I would be sorry for private practitioners. They would request an exam and have processed images, and not being able to further analyze the exam so as to better fit their reasoning and hence choose between therapeutic options. I’m speaking here of surgery. Without the CT DICOM volumes that patients hand over to me on DVD, I would not have been here typing this, and many patients would have been very sorry for many reasons.</p>
<p>This is not to discredit ChatGPT. Just an incremental comment. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @lassoan (2023-02-03 14:38 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="8" data-topic="26888">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>If this is generally the case in North America, I would be sorry for private practitioners.</p>
</blockquote>
</aside>
<p>Unfortunately, ChatGPT is right. In North America, the original images are often retained only for a short time and only the poorer quality processed images are archived (and made available for patients on request).</p>
<p>This is clearly a mistake and we try to make clinicians and hospital IT staff aware of this issue, but it is hard to change this practice, because 3D review is not the standard for most cases, and for 2D slice-by-slice review the processed images appear to be sufficient.</p>

---
