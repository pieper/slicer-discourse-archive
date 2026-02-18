# Private Extension my own python code

**Topic ID**: 27285
**Date**: 2023-01-17
**URL**: https://discourse.slicer.org/t/private-extension-my-own-python-code/27285

---

## Post #1 by @dsa934 (2023-01-17 05:54 UTC)

<p>Operating system: window 11<br>
Slicer version: 4.13.0</p>
<p>Hello,<br>
I have two questions regarding ‘private extension’.</p>
<p>Q1. Is it correct that the extension created through the extension wizard works locally by default and becomes public only when it is submitted to Slicer’s index(?)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5582779b3c1905a2e12814b76ced2d991a336ad9.png" data-download-href="/uploads/short-url/ccs6NGYQtK2pthOCzKuVwmFrQiR.png?dl=1" title="Question" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5582779b3c1905a2e12814b76ced2d991a336ad9.png" alt="Question" data-base62-sha1="ccs6NGYQtK2pthOCzKuVwmFrQiR" width="437" height="500" data-dominant-color="EDEDEC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Question</span><span class="informations">438×501 15.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ul>
<li>
<p>Create an extension file through ‘create extension’ of the extension wizard. ( I got it )</p>
</li>
<li>
<p>Add Module to Extention</p>
</li>
</ul>
<p>Q2) What is ‘Add Module to Extension’ ?<br>
Since a Python code file (.py) is usually called a module, I thought it was to add the function file I created in this part. However, I think I am wrong. Where should I add the source code files that I have implemented and other files necessary for source code operation?</p>

---

## Post #2 by @RafaelPalomar (2023-01-17 08:53 UTC)

<blockquote>
<p>Q1. Is it correct that the extension created through the extension wizard works locally by default and becomes public only when it is submitted to Slicer’s index(?)</p>
</blockquote>
<p>That is correct. The <code>Extension Wizard</code> module will create the local files that make up an extension. Once you have developed your extension, you need to make a PR to the <code>ExtensionsIndex</code> (<a href="https://github.com/slicer/extensionsindex" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/ExtensionsIndex: Slicer extensions index</a>).</p>
<blockquote>
<p>Q2) What is ‘Add Module to Extension’ ?<br>
Since a Python code file (.py) is usually called a module, I thought it was to add the function file I created in this part. However, I think I am wrong. Where should I add the source code files that I have implemented and other files necessary for source code operation?</p>
</blockquote>
<p>An extension is made up of one or more modules (there are also different types of modules). You need to add at least one module for your extension to work, so in your case, you would probably want to add a <code>Python</code> module. This will generate the structure of a basic module, including a <code>.py</code> file where you can move your code.</p>
<p>It is worth mentioning that 3D slicer will ask you whether the path to your module should be added to the list of modules that Slicer will load. Doing it so, will have your module loaded in your current installation/build of 3D Slicer.</p>

---

## Post #3 by @dsa934 (2023-01-17 09:46 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b98ae4f71668c22b801f4eec16d82a126c1bf293.png" alt="image" data-base62-sha1="qtnUxlTzcBPiP96vHiLEJSzf8Ov" width="645" height="81"></p>
<p>I tried the method you told me before asking the question.</p>
<p>But I have qt module problems (I have included a key board shortcut custom function in my code.)</p>
<p>In my opinion, it seems to be a problem that occurs because the act of loading my custom module precedes the loading of the qt module. Should I do add  Pyqt5 in my codes?</p>

---

## Post #4 by @RafaelPalomar (2023-01-17 13:44 UTC)

<p>What is exactly the error that you get? Which version of Slicer are you<br>
using?</p>
<p>I’ve just created a new extension with a scripted module (all defaults)<br>
and it works flawlessly (3D Slicer git main branch).</p>

---

## Post #5 by @ebrahim (2023-01-17 14:28 UTC)

<aside class="quote no-group" data-username="dsa934" data-post="1" data-topic="27285">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>Since a Python code file (.py) is usually called a module, I thought it was to add the function file I created in this part.</p>
</blockquote>
</aside>
<p>Note that “Slicer module” is a separate concept from “Python module”<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/module_overview.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/module_overview.html</a></p>

---

## Post #6 by @dsa934 (2023-01-18 00:53 UTC)

<p>As I wrote above, I am using slicer -4.13.0-2021-08-24 version.</p>
<p>My code contains code to customize the ‘short cut’ of the 3d slicer.</p>
<p>If you delete the ‘short cut’ custom part and proceed with extension, the following error occurs.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/696d23e51b0b9e2b3834e60344c9995500443e5e.png" data-download-href="/uploads/short-url/f2DXUbjTXisrmxYmrHBoGAahEUm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/696d23e51b0b9e2b3834e60344c9995500443e5e.png" alt="image" data-base62-sha1="f2DXUbjTXisrmxYmrHBoGAahEUm" width="690" height="37" data-dominant-color="FDF4F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">884×48 3.14 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you don’t remove the ‘short cut’ part, you will get an error like below.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01a2af5983cf68d0ceee18527f5413f16331707a.png" alt="image" data-base62-sha1="et1L7T2sVoMsoWpC06cjsqBVwu" width="672" height="256"></p>
<p>The order in which I proceeded with the extension is as follows.</p>
<p>step 1) extension wizard - create extension - name( test )</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0d81325057ea9d2c6ff632e6edf926927f9f87b.png" alt="image" data-base62-sha1="rvYBY7FYxTVUuCN1VC46sPNUQQz" width="263" height="197"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7dddfe977e8179ecb341f0fa05bafba3ffced1ae.png" alt="image" data-base62-sha1="hXtiTKNr9JvbOWGlUL4xAzLYBJ4" width="363" height="476"></p>
<p>step 2) Add module to Extension (test_my_code)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/393469ba7a36476fa6777adc94113a4cc6435874.png" alt="image" data-base62-sha1="8a3vD1VBOMGryCDD7iOHQA2KjTC" width="380" height="186"></p>
<p>step 3) Add my custom code into test_my_code folder</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/756f390df7301132b6db768ccfba3c345ae6d3cf.png" data-download-href="/uploads/short-url/gKS9N7N0XOuuzZUt6ymNuqsQJWL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/756f390df7301132b6db768ccfba3c345ae6d3cf.png" alt="image" data-base62-sha1="gKS9N7N0XOuuzZUt6ymNuqsQJWL" width="690" height="297" data-dominant-color="F6F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">791×341 16.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>===============<br>
I thought adding the module in step 2) was adding the code file I created.<br>
However, when I click ‘add module to extension’, the screen that appears is as follows.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e6ee4326200593edde64fa4e845e0a1f5affc4b.png" alt="image" data-base62-sha1="fKW6xpe0NaXNQVoV5oogg7X9ONt" width="321" height="145"><br>
I think my understanding of this part is wrong, but since the Python code file itself is called a module, shouldn’t I be able to add the code I created in step 2?</p>

---

## Post #7 by @RafaelPalomar (2023-01-18 13:32 UTC)

<p>Hello,</p>
<p>I would recommend you to switch to Slicer 5 (probably nothing to do with this issue, though).</p>
<p>Using Slicer 5, through the <code>ExtensionWizard</code> I got this structure:</p>
<pre><code class="lang-auto">/tmp/TestExtension/
├── CMakeLists.txt
├── TestExtension.png
└── TestModule
    ├── CMakeLists.txt
    ├── __pycache__
    │   └── TestModule.cpython-39.pyc
    ├── Resources
    │   ├── Icons
    │   │   └── TestModule.png
    │   └── UI
    │       └── TestModule.ui
    ├── Testing
    │   ├── CMakeLists.txt
    │   └── Python
    │       └── CMakeLists.txt
    └── TestModule.py
</code></pre>
<p>I added the following path to the Slicer module paths: <code>/tmp/TestExtension/TestModule</code>.</p>
<p>Maybe as a starting point use only the files generated by the extensions wizard.</p>
<p>You could verify that you have similar structure and your modules path<br>
looks similar.</p>

---

## Post #8 by @dsa934 (2023-01-18 15:01 UTC)

<p>Hello again</p>
<p>Unfortunately, since the slicer version has been unified( in my company), it cannot be changed.<br>
There is no problem with this configuration in my version either.<br>
The current problem situation is that the problem occurs from the moment the custom code is added.<br>
I temporarily solved the problem by replacing it with a method of adding code through the ‘Ctrl+r’ short cut key, but I’m still curious about the sure method for the extension.</p>
<aside class="quote no-group" data-username="RafaelPalomar" data-post="7" data-topic="27285">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<pre><code class="lang-auto">/tmp/TestExtension/
├── CMakeLists.txt
├── TestExtension.png
└── TestModule
    ├── CMakeLists.txt
    ├── __pycache__
    │   └── TestModule.cpython-39.pyc
    ├── Resources
    │   ├── Icons
    │   │   └── TestModule.png
    │   └── UI
    │       └── TestModule.ui
    ├── Testing
    │   ├── CMakeLists.txt
    │   └── Python
    │       └── CMakeLists.txt
    └── TestModule.py

</code></pre>
</blockquote>
</aside>
<p>The above structure is automatically formed after the ‘Create Extension’ and ‘Add module to entension’ processes.<br>
If so, where is your custom code included in the structure above?<br>
In my slicer, I included my custom code directly in the directory after the above structure was created automatically.</p>
<p>like this</p>
<pre><code class="lang-auto">/tmp/TestExtension/
├── CMakeLists.txt
├── TestExtension.png
└── TestModule
    ├── CMakeLists.txt
    ├── __pycache__
    │   └── TestModule.cpython-39.pyc
    ├── Resources
    │   ├── Icons
    │   │   └── TestModule.png
    │   └── UI
    │       └── TestModule.ui
    ├── Testing
    │   ├── CMakeLists.txt
    │   └── Python
    │       └── CMakeLists.txt
    └── TestModule.py
    │
    └── my_custom_code.py (new !)

</code></pre>
<p>The part I found odd in the previous question is the ‘TestModule’ part.<br>
This part is the output of the ‘Add module to extension’ process, I thought I was adding my custom code here, but it actually seemed to create a dummy folder.<br>
Is it correct way to add custom code additions directly under these dummy modules?</p>

---

## Post #9 by @jamesobutler (2023-01-18 15:28 UTC)

<p>Place your custom code in the template/example Slicer scripted loadable module that is TestModule.py. You must maintain the template structure contained in TestModule.py. It will not work to copy all code in my_custom_code.py and replace everything in TestModule.py.</p>

---

## Post #10 by @dsa934 (2023-01-18 15:39 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a><br>
What you mean is not to add custom code inside TestModule, but to copy and add my CustomCode inside the TestModule.py code while keeping the contents of the existing TestModule.py?</p>

---

## Post #11 by @jamesobutler (2023-01-18 15:54 UTC)

<p>TestModule.py is an example/template of a Slicer scripted loadable module that does some example functionality. You will replace that with your custom code, however you need to keep the framework of the classes in place (ScriptedLoadableModule/ScriptedLoadableModuleWidget/ScriptedLoadableModuleLogic). The framework makes sure the Slicer scripted loadable module is setup correctly upon starting Slicer.</p>

---

## Post #12 by @dsa934 (2023-01-19 00:40 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b8614223db0b505b7946e21b52bef1041becac8.png" data-download-href="/uploads/short-url/d3EI8SJuo2DUH1qDpEO5VGqPPuM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b8614223db0b505b7946e21b52bef1041becac8.png" alt="image" data-base62-sha1="d3EI8SJuo2DUH1qDpEO5VGqPPuM" width="690" height="78" data-dominant-color="FFF8F8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1008×114 3.78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As you said, I think I can just copy-paste my custom code into the generated code file, but it’s frustrating because there are so many unknown errors. you’re driving me crazy 3D slicer~~~</p>
<p>edit :</p>
<p>I often use argparser in code, but I don’t know why it doesn’t work, so I just changed it to a global variable and solved it. but it doesn’t seem clean</p>

---

## Post #13 by @jamesobutler (2023-01-19 01:01 UTC)

<p>The error you show looks like pure python issues rather than Slicer. Does your code take command line input arguments or is it built with GUI input/selection in mind? Are you creating a Slicer scripted module or a Slicer scripted CLI module? See module types at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/module_overview.html#module-overview" class="inline-onebox" rel="noopener nofollow ugc">Module Overview — 3D Slicer documentation</a>. A scripted CLI is an option in the extension wizard of the latest stable Slicer.</p>

---

## Post #14 by @dsa934 (2023-01-19 06:49 UTC)

<p>The problem didn’t occur in all cases except when pasting the custom code into the extension module file. I don’t think it’s a code problem. I’ll have to keep thinking about why argparser only gives an error in this case.</p>

---
