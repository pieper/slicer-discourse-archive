# Extension settings in C++ code

**Topic ID**: 28251
**Date**: 2023-03-09
**URL**: https://discourse.slicer.org/t/extension-settings-in-c-code/28251

---

## Post #1 by @dsa934 (2023-03-09 08:06 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>Hi, slicer users</p>
<p>I know how to extend python code in 3D slicer. but this time I need to add C++ code to the 3d slicer…<br>
I know that there is cmake in 3d slicer, but I am not familiar with it, so I ask a question.</p>
<ol>
<li>How to add c++ code in 3d slicer</li>
<li>How to run custom c++ code in 3d slicer ( for testing )</li>
</ol>
<p>Are there any resources I can refer to?</p>

---

## Post #2 by @jamesobutler (2023-03-09 12:20 UTC)

<p>The 3D Slicer documentation includes details about developing C++ Loadable modules as part of an extension. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#create-an-extension" class="inline-onebox" rel="noopener nofollow ugc">Extensions — 3D Slicer documentation</a></p>
<blockquote>
<ul>
<li>If developing <a href="https://slicer.readthedocs.io/en/latest/developer_guide/module_overview.html" rel="noopener nofollow ugc">C++ loadable or CLI modules</a>(not needed if developing in Python):
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html" rel="noopener nofollow ugc">build Slicer application</a>.</li>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html?highlight=Extension#build-an-extension" rel="noopener nofollow ugc">build your extension</a></li>
</ul>
</li>
</ul>
</blockquote>

---

## Post #3 by @dsa934 (2023-03-10 02:40 UTC)

<p>Hi, <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>I asked the question too roughly.</p>
<p>I know about python extension method for 3d slicer.<br>
In the above method, I had to combine the custom code I implemented into one file.</p>
<p><strong>convert file below</strong></p>
<pre><code class="lang-auto">data_preprocessing.py 

def preprocessing():
...

def show():                                          
...

def set_domain_knowledge():
 ...

data_training.py

def train() : 
...

def val():
...

</code></pre>
<p><strong>to</strong></p>
<pre><code class="lang-auto">extension_code.py
def preprocessing():
...
def show():                                          
...
def set_domain_knowledge():
 ...
def train() : 
...
def val():
...

</code></pre>
<p>In order to extend a module composed of multiple files in python and c++ extension to 3d slicer, do I always have to combine them into one file?<br>
( It does not mean that python files and cpp files are mixed, but means the case of the extension of the python version and the extension of the cpp version. )</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1ecbdcca5864741a018a4d5fc98527f9d098dbd.png" alt="image" data-base62-sha1="rFxmOgvTrJmkmmE4n7C90AkUpfT" width="475" height="270"></p>
<p>Can I paste only the main part of the custom code I developed at the bottom of custom_extension.py in the above file, and add the necessary additional modules in the form of files to the custom_extension folder?</p>

---

## Post #4 by @jamesobutler (2023-03-10 11:55 UTC)

<p>I do not quite understand what you are asking.</p>
<p>A Slicer extension can contain multiple Slicer modules of various types (python scripted loadable module, c++ loadable module, or CLI module). The ExtensionWizard module can help set up the necessary template of files needed for each Slicer module type.</p>
<p>You will observe that when you create the template of files for a c++ loadable module that there are multiple files created. You should follow this organization. A scripted loadable module can be a single .py file or it can also have a supporting library of .py files. However you will need to be careful with imports and modify the module’s CMakeLists.txt to make sure you include those supporting library files. That type of code organization for a scripted loadable module is not shown in the template of files created by the ExtensionWizard.</p>

---

## Post #5 by @dsa934 (2023-03-10 16:31 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>To clarify the question, let’s assume that we are going through an extension with a python version.</p>
<p>Through the extension wizard, you can create the following structure through the process of creating an extension and adding a module.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edc78fcd1f3b49750d082bdd4f182bdd1e8d3f58.png" alt="image" data-base62-sha1="xVuIBPaeDQ566GSfGVTp9qkMljG" width="490" height="283"></p>
<p>Now I need to add my module to custom_extenion.py .</p>
<aside class="quote quote-modified" data-post="8" data-topic="27285">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/private-extension-my-own-python-code/27285/8">Private Extension my own python code</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hello again 
Unfortunately, since the slicer version has been unified( in my company), it cannot be changed. 
There is no problem with this configuration in my version either. 
The current problem situation is that the problem occurs from the moment the custom code is added. 
I temporarily solved the problem by replacing it with a method of adding code through the ‘Ctrl+r’ short cut key, but I’m still curious about the sure method for the extension. 

The above structure is automatically formed …
  </blockquote>
</aside>

<p>If I didn’t misunderstand your previous reply, I understood that I had to keep the framework for class (ScriptedLoadableModule/ScriptedLoadableModuleWidget/ScriptedLoadableModuleLogic) of custom_extension.py and paste my code below it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c18e1e6a3a1c9db51edc14b600d4cf5de9235b5a.png" data-download-href="/uploads/short-url/rCgDFVt9nZJjTJlG6tR1aOe3pea.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c18e1e6a3a1c9db51edc14b600d4cf5de9235b5a_2_535x500.png" alt="image" data-base62-sha1="rCgDFVt9nZJjTJlG6tR1aOe3pea" width="535" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c18e1e6a3a1c9db51edc14b600d4cf5de9235b5a_2_535x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c18e1e6a3a1c9db51edc14b600d4cf5de9235b5a_2_802x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c18e1e6a3a1c9db51edc14b600d4cf5de9235b5a.png 2x" data-dominant-color="050304"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1063×993 22.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Therefore, I pasted my code in the empty space above(red rectangle) and declared a shortcut key function to perform the extension of the python version. To achieve the above method, I went through the process of modifying my module, which was previously composed of several files, into a single file.</p>
<p>I was curious about how to extend without merging into one file. Isn’t the cmakelist.txt you mentioned used when building in code using c++?</p>
<p>Are you saying that when adding a module composed of multiple files to 3d slicer, regardless of the version(python, c++ ), all cmakelist.txt should be modified?</p>

---

## Post #6 by @jamesobutler (2023-03-10 16:36 UTC)

<p>There is a CMakeLists.txt for each module whether it is python based or C++ based. It is all necesssary for building the extension and creating the “.zip” file in the case of windows which is the final package of the extension. To create this “.zip” file, even python based Slicer scripted loadable modules have to be built against a local Slicer build.</p>
<p>Going back to your original post, are you creating a C++ Slicer Loadable module in your extension?<br>
Have you been able to build the Slicer Loadable module template created by the ExtensionWizard?</p>

---

## Post #7 by @dsa934 (2023-03-11 03:46 UTC)

<p>I haven’t tried extending the C++ code yet.</p>
<p>In c++, the build proceeds by reading cmakelist through cmake.</p>
<p>I understood what you said if it is correct to proceed with extensions for modules composed of multiple files in the same way as above in 3d slicer.</p>

---

## Post #8 by @lassoan (2023-03-11 06:44 UTC)

<aside class="quote no-group" data-username="dsa934" data-post="7" data-topic="28251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>I understood what you said if it is correct to proceed with extensions for modules composed of multiple files in the same way as above in 3d slicer.</p>
</blockquote>
</aside>
<p>Yes, you can have many modules in an extension; and you may implement a Python scripted module in one or many files.</p>
<p>I would advise to implement your Python scripted module in a single file if the module is not too large or complex. If the file grows bigger than 30-40kB then it may make sense to split it up to more files. If you already have a Python package/library then you don’t need to merge them and move everything into the Slicer module file, you can keep it in a subfolder as <a class="mention" href="/u/jamesobutler">@jamesobutler</a> explained above.</p>

---
