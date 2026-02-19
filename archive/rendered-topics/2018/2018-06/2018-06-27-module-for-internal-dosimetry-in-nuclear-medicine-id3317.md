---
topic_id: 3317
title: "Module For Internal Dosimetry In Nuclear Medicine"
date: 2018-06-27
url: https://discourse.slicer.org/t/3317
---

# Module for Internal Dosimetry in Nuclear Medicine

**Topic ID**: 3317
**Date**: 2018-06-27
**URL**: https://discourse.slicer.org/t/module-for-internal-dosimetry-in-nuclear-medicine/3317

---

## Post #1 by @Alex_Vergara (2018-06-27 14:46 UTC)

<p>Dear All</p>
<p>I am willing to create a whole module for Internal Dosimetry in Nuclear Medicine, the Module consist on several plugins:</p>
<ol>
<li>Quality Control of Images (Images loaded from DICOM Node must contain a minimum set of data in headers)</li>
<li>Images are supposed to be Registered by acquisition system and they can be easily registered with the already available Registration plugins here.</li>
<li>CT image Segmentation with Atlas (Its been proposed several models from ICRP but the Idea is to have the ability to enter the Model)</li>
<li>CT Rescaling (not confusing with BRAINS rescaling with is useless in this way)</li>
<li>Geant4 (preferred) or Gate  Bridge to perform Dose calculations (currently missing)</li>
<li>Tumor/Health Structures Segmentation (like the PETTumorSegmentation plugin)</li>
<li>Pharmacokinetics per Atlas tissue if possible, otherwise per segmented organ, this leads to a matrix to move from dose rate to absorbed dose</li>
<li>BED calculation</li>
<li>Anything else interesting or missing in the above</li>
</ol>
<p>Most of this is already done by other plugins available here, but everything its messed up and there are missing parts. This is a long term Project, so it will be implemented by stages. If someone is ready already working in something similar and is willing to accept the challenge just let me know.</p>

---

## Post #2 by @tadeukubo (2018-11-01 22:47 UTC)

<p>Hi Alex,</p>
<p>I’m new here but I’m really interested in something like that. I saw a course from EFOMP that will occur in the beginning of 2019.</p>
<p>I hope we keep in touch.</p>
<p>Best regards,<br>
Tadeu</p>

---

## Post #3 by @lassoan (2018-11-02 01:18 UTC)

<p>Looks like a nice, ambitious roadmap. It is great that you plan to work on these. There are many modules and extensions that can help you and if you have any specific questions or problems then let us know and we’ll be happy to help.</p>

---

## Post #4 by @moncef (2018-11-04 21:40 UTC)

<p>Hi Alex,<br>
It’s very interessting to work under that, I would like to collaborate with you.</p>
<p>Best regards,</p>

---

## Post #5 by @Alex_Vergara (2018-11-21 14:40 UTC)

<p>Yes, it is the ESMPE course that will be held in Prague in January 2019. I am one of the teachers <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=6" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #6 by @Alex_Vergara (2018-11-21 14:43 UTC)

<p>I am preparing the ESMPE course, hopefully we will have something already developed (working) in very early stage by then.  I will let you know further when it is finally released. For now I need to be focused on that, after January I will be more active developing.</p>

---

## Post #7 by @Alex_Vergara (2018-11-21 14:45 UTC)

<p>Hi lassoan! I am having troubles setting properly the vtk environment to be detected by both Slicer and VSCode, the one shipped by Slicer has no sources, so it is useless but when I compile Slicer with my own VTK it does not compile at all (bunch of errors). Hopefully I will have this sorted out eventually <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=6" title=":frowning:" class="emoji" alt=":frowning:"></p>
<p>Edit: I am on MacOS 10.4 Mojave, VSCode October 2018 (version 1.29)</p>
<p>Update:</p>
<ul>
<li>Quality Control of Images (Images loaded from DICOM Node must contain a minimum set of data in headers) -&gt; This will be addressed diferently</li>
<li>Images are supposed to be Registered by acquisition system and they can be easily registered with the already available Registration plugins here. -&gt; This is already available in Slicer but too diluted. A working procedure will be shown in the ESMPE course</li>
<li>CT image Segmentation with Atlas (Its been proposed several models from ICRP but the Idea is to have the ability to enter the Model)  -&gt; Not currently available, we stick with RTstruct importation and / or manual segmentation</li>
<li>CT Rescaling (not confusing with BRAINS rescaling with is useless in this way) -&gt; I realize that I can work with transform matrixes directly instead of modifying the images which was a bad idea</li>
<li>Geant4 (preferred) or Gate Bridge to perform Dose calculations (currently missing) -&gt; I already have the goal template for Gate but I need some handler to fill it. The idea of Geant4 is still there but is a lot more difficult path</li>
<li>Tumor/Health Structures Segmentation (like the PETTumorSegmentation plugin) -&gt; I realize that with the combination of PETTumorSegmentation and the rest of segmentation tools this can be achieved, just require a written procedure</li>
<li>Pharmacokinetics per Atlas tissue if possible, otherwise per segmented organ, this leads to a matrix to move from dose rate to absorbed dose -&gt; This is NOT available in SLICER, not even as extension, a module is required!! Basically a module that creates a table with different time points and allows to do a time integral. I am doing this by hand in FIJI.</li>
<li>BED calculation -&gt; I am doing this by hand in FIJI. But theoretical is possible in Slicer, just need an external matrix(table) with BED coefficients per structure.</li>
<li>Anything else interesting or missing in the above -&gt; I really need to understand better how to handle multiple time points SPECT/CT studies, so if anyone has some hint they are greatly appreciated</li>
</ul>

---

## Post #8 by @lassoan (2018-11-21 15:20 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="7" data-topic="3317">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>I am having troubles setting properly the vtk environment to be detected by both Slicer and VSCode</p>
</blockquote>
</aside>
<p>I don’t know what you mean by this. Normally, you let Slicer build all of its dependencies, including VTK.</p>
<p>You’ve posted a lot of questions/ideas. It is more likely that you get feedback if you post one (or maximum a few questions) at a time, about those topics that you are currently working on, preferably in a new topic. You may reference this topic from the new topics to give some background about what you would like to achieve.</p>

---

## Post #9 by @Alex_Vergara (2018-11-21 17:00 UTC)

<p>If you let Slicer do this, using the VTK from the system it will crash (at least on my system). I only made it to work with the bundled VTK setup is has, but in this case VSCode does not see the VTK as valid package but the system VTK which is not compatible with Slicer’s one. I have to figure out how to solve this.</p>

---

## Post #10 by @lassoan (2018-11-21 19:22 UTC)

<p>Have you set PythonSlicer as Python interpreter in your Python IDE?</p>

---

## Post #11 by @Alex_Vergara (2018-11-22 08:56 UTC)

<p>At the end I might surrender and do a python module after all, CLI is really not setting up. But as I can see there is another conflict, PythonSlicer is 2.7 and refers to VTK6, while in my system there is python 3.7.1 and VTK9. If I try to compile Slicer with my setup it just gives a bunch of errors.</p>
<p>Edit: I successfully installed the jupyter kernel, maybe this is the way to go! everything runs fine there!!</p>

---

## Post #12 by @lassoan (2018-11-22 15:19 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="11" data-topic="3317">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>CLI is really not setting up.</p>
</blockquote>
</aside>
<p>If you can describe specific problems then we can help solving them or explain what are some common alternative approaches.</p>
<p>If you want to learn about how to implement Python scripted modules for Slicer, I would recommend completing <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers">programming tutorials</a>, in particular the “Slicer programming tutorial” and the PerkLab’s “Scripting and module development tutorial”.</p>
<aside class="quote no-group" data-username="Alex_Vergara" data-post="11" data-topic="3317">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>I can see there is another conflict, PythonSlicer is 2.7 and refers to VTK6, while in my system there is python 3.7.1 and VTK9</p>
</blockquote>
</aside>
<p>Slicer uses Python 2.7 and latest VTK (VTK 8.2). Various VTK versions are available in other Python distributions. You can certainly not mix different versions, so if you want to call a Python3 script from Slicer then you need to use the startup environment as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Python_Scripting#How_to_run_Python_script_using_a_non-Slicer_Python_environment">here</a>.</p>

---

## Post #13 by @tadeukubo (2018-12-30 22:20 UTC)

<p>I’ll attend Alex. See you there</p>

---

## Post #14 by @Alex_Vergara (2019-01-16 10:46 UTC)

<p>This is a little piece of code that lets you to install any missing package from within the python interpreter itself, just create a file named slicer_python_package_installer.py inside SlicerPlugins folder in your home folder (create if not exists and add it to modules paths). Then add the following</p>
<pre data-code-wrap="python"><code class="lang-python"># import pip main
try:
    from pip import main as pipmain
except:
    from pip._internal import main as pipmain
import importlib

def install_and_import(package):
    try:   
        importlib.import_module(package)
    except:
        pipmain(['install', package])
        importlib.import_module(package)
        pass

def install_package(package):
    try:
        importlib.import_module(package)
    except:
        pipmain(['install', package])
        pass
</code></pre>
<p>Then in the python interpreter write the following:</p>
<pre data-code-wrap="python"><code class="lang-python">from slicer_python_package_installer import *
</code></pre>
<p>And voila! you can easily do</p>
<pre data-code-wrap="python"><code class="lang-python">install_and_import('joblib')
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae7d4ae5cb4f403760a942381c9dbfba7234260b.png" data-download-href="/uploads/short-url/oTBw6ZJyBErglBDg0AlqlSTlhqP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae7d4ae5cb4f403760a942381c9dbfba7234260b_2_690x111.png" alt="image" data-base62-sha1="oTBw6ZJyBErglBDg0AlqlSTlhqP" width="690" height="111" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae7d4ae5cb4f403760a942381c9dbfba7234260b_2_690x111.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae7d4ae5cb4f403760a942381c9dbfba7234260b_2_1035x166.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae7d4ae5cb4f403760a942381c9dbfba7234260b.png 2x" data-dominant-color="F4F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1191×192 37.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @fbaerenfaenger (2021-02-13 17:09 UTC)

<p>Hi Alex!<br>
How is your project coming along? Is there already something usable or a documentation about what you have already achieved?<br>
Best regards<br>
Felix</p>

---

## Post #16 by @Alex_Vergara (2021-03-04 11:15 UTC)

<p>Hello, sorry for late response, I was hospitalised for two weeks!</p>
<p>You have to search for OpenDose3D extension in extension manager. Also you can review the code and user manuals here <a href="https://gitlab.com/opendose/opendose3d" class="inline-onebox" rel="noopener nofollow ugc">OpenDose / SlicerOpenDose3D · GitLab</a></p>
<p>If you have any further question just let me know</p>

---
