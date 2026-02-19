---
topic_id: 9496
title: "Developing Slicer Modules In Visual Studio Visual Studio Cod"
date: 2019-12-14
url: https://discourse.slicer.org/t/9496
---

# Developing Slicer modules in Visual Studio / Visual Studio Code?

**Topic ID**: 9496
**Date**: 2019-12-14
**URL**: https://discourse.slicer.org/t/developing-slicer-modules-in-visual-studio-visual-studio-code/9496

---

## Post #1 by @apparrilla (2019-12-14 14:58 UTC)

<p>I´m a newbie in module scripting and I should like to manage code with Visual Studio or Visual Studio Code instead of Notepad++.<br>
How can I setup VS/VSC for this porpuse? Is there any tutorial o video about?</p>
<p>Thanks on advance</p>

---

## Post #2 by @lassoan (2019-12-14 17:56 UTC)

<p>Slicer will open .py files with the editor you configured in you Windows system settings (file associations), but you can open the files in any editor. You can also do <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools#Visual_Python_debugging_in_PyCharm">step-by-step debugging in Visual Studio Code, Visual Studio, PyCharm, Eclipse, LiClipse, etc.</a>.</p>

---

## Post #3 by @apparrilla (2019-12-14 18:03 UTC)

<p>I have Debug Connection made, but Slicer Python libraries are not recognited by Visual Studio Code. This is my real issue. How can I add them?</p>

---

## Post #4 by @Alex_Vergara (2019-12-14 20:23 UTC)

<p>In VScode you need to configure your python module, just let VSCode know you want the one in Slicer, <code>{"python.pythonpath"="/path/to/slicer/bin/PythonSlicer"} </code> in your project configuration <code>/project/folder/.vscode/settings.json</code>. Thats it, now you need to install pylint, rope and autopep8 inside Slicer with normal <code>slicer.util.pip_install("pylint")</code> , now your vscode works natively in Slicer.</p>

---

## Post #5 by @apparrilla (2019-12-15 15:56 UTC)

<p>Thanks <a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> for your reply.<br>
It looks a not so easy procedure for newbies…<br>
It should be nice to have any kind of stpe-by-step tutorial. I´ve been surfing Developer Documentation and I couldn´t find it.</p>

---

## Post #6 by @lassoan (2019-12-15 23:34 UTC)

<p>I’ve executed <code>slicer.util.pip_install("pylint rope autopep8")</code> in Slicer’s Python console and set <code>python.pythonpath</code> in VS Code to <code>c:\Users\andra\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-11\bin\PythonSlicer.exe</code>. After this I restarted VS Code, opened a file, and entered:</p>
<pre><code class="lang-python">import vtk
a=vtk.vtkImageData()
a.Get
</code></pre>
<p>At this point, I would expect pressing Ctrl-space would bring up Get… methods of vtkImageData, but only a few method names show up (that are used in the file).</p>
<p><a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> does auto-complete or documentation work for you for VTK and Slicer classes? Do you use Jedi as IntelliSense engine (<code>python.jediEnabled</code>)? Seeing a few screenshots and/or videos about what you have working in VS Code would be great.</p>

---

## Post #7 by @Alex_Vergara (2019-12-16 08:47 UTC)

<p>Here you can see VSCode recognizes the python inside Slicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5489b1f30c7d96098721ba239fc5db2336250fa6.png" data-download-href="/uploads/short-url/c3R7jmAyQAIuXfu4q4923y7Zgma.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5489b1f30c7d96098721ba239fc5db2336250fa6_2_642x500.png" alt="image" data-base62-sha1="c3R7jmAyQAIuXfu4q4923y7Zgma" width="642" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5489b1f30c7d96098721ba239fc5db2336250fa6_2_642x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5489b1f30c7d96098721ba239fc5db2336250fa6_2_963x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5489b1f30c7d96098721ba239fc5db2336250fa6_2_1284x1000.png 2x" data-dominant-color="282A2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1848×1439 518 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My settings.json inside project .vscode folder<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf08e6c3490960a5f41c447ab55050ae159866ad.png" alt="image" data-base62-sha1="rfYgCoS71YE0IoOjyYfed726ug5" width="669" height="156"></p>
<p>the vscode general settings.json<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81a5ea4937688733ef802ac2282c817d180c776f.png" data-download-href="/uploads/short-url/iuV435P7lz7bWLBUsiSDvpICLJt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81a5ea4937688733ef802ac2282c817d180c776f.png" alt="image" data-base62-sha1="iuV435P7lz7bWLBUsiSDvpICLJt" width="690" height="399" data-dominant-color="282727"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">704×408 48.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You need to add the extrapaths to your python, I know I have them in the wrong place, but I  am being lazy to move them. anyways, you need the python.autocomplete.extrapaths added to your settings too.<br>
As you can see ctrl+space already gives me all necesary hints<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e092cfd6da8c0c11ed6759580d8cb4f98c79dbae.png" data-download-href="/uploads/short-url/w2FuM1Vd3If4zLPyJhkAFnmBTKm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e092cfd6da8c0c11ed6759580d8cb4f98c79dbae_2_690x128.png" alt="image" data-base62-sha1="w2FuM1Vd3If4zLPyJhkAFnmBTKm" width="690" height="128" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e092cfd6da8c0c11ed6759580d8cb4f98c79dbae_2_690x128.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e092cfd6da8c0c11ed6759580d8cb4f98c79dbae.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e092cfd6da8c0c11ed6759580d8cb4f98c79dbae.png 2x" data-dominant-color="222426"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">943×176 14.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @apparrilla (2019-12-16 21:20 UTC)

<p>This is for Linux, right? What “settings.json” and “extrapaths” should I have to change in Windows?<br>
Thanks</p>

---

## Post #9 by @lassoan (2019-12-16 22:11 UTC)

<p>On Windows, I’ve tried to add the extra paths but nothing changed. It still does not recognize anything.</p>

---

## Post #10 by @Alex_Vergara (2019-12-18 10:09 UTC)

<p>Ok, I have fixed my settings to be module specific, now they are as<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56ba227d72d5156243014c84a591ce1af8332632.png" data-download-href="/uploads/short-url/cndQXOMvH3J3lX297CZVHMsq2Ns.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56ba227d72d5156243014c84a591ce1af8332632_2_690x261.png" alt="image" data-base62-sha1="cndQXOMvH3J3lX297CZVHMsq2Ns" width="690" height="261" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56ba227d72d5156243014c84a591ce1af8332632_2_690x261.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56ba227d72d5156243014c84a591ce1af8332632.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56ba227d72d5156243014c84a591ce1af8332632.png 2x" data-dominant-color="292727"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">801×304 41.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and this worked for me in mac, linux and windows</p>

---

## Post #11 by @lassoan (2019-12-18 14:04 UTC)

<p>This sounds very promising! Can you copy here your settings for Windows? (and if possible, not as screenshot, but as text) Thank you.</p>

---

## Post #12 by @jamesobutler (2019-12-18 17:59 UTC)

<p>I was able to get auto completion within Visual Studio Code on Windows following these settings:</p>
<p>“C:\Users\JamesButler\AppData\Roaming\Code\User\settings.json”</p>
<pre data-code-wrap="json"><code class="lang-json">{
    "python.pythonPath": "C:\\Program Files\\Slicer 4.11.0-2019-12-06\\bin\\SlicerPython",
    "python.autoComplete.extraPaths": [
        "C:\\Program Files\\Slicer 4.11.0-2019-12-06\\",
        "C:\\Program Files\\Slicer 4.11.0-2019-12-06\\lib\\Python",
        "C:\\Program Files\\Slicer 4.11.0-2019-12-06\\lib\\QtPlugins",
        "C:\\Program Files\\Slicer 4.11.0-2019-12-06\\lib\\Slicer-4.11",
        "C:\\Program Files\\Slicer 4.11.0-2019-12-06\\bin",
    ],
}
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cca409297d451a71b3efaf4fcb5fbad2c6046311.png" data-download-href="/uploads/short-url/tckQDFtzZXvwXLAvvfgPNIMR5i9.png?dl=1" title="autocomplete-vscode" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cca409297d451a71b3efaf4fcb5fbad2c6046311.png" alt="autocomplete-vscode" data-base62-sha1="tckQDFtzZXvwXLAvvfgPNIMR5i9" width="690" height="320" data-dominant-color="323134"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">autocomplete-vscode</span><span class="informations">900×418 32.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2019-12-18 19:13 UTC)

<p>Thanks! Do you have auto-complete for VTK or Slicer MRML classes, too?</p>

---

## Post #14 by @jamesobutler (2019-12-18 19:57 UTC)

<p>It appears to only be working for these pure python modules like <code>util</code> with the settings that I used.</p>
<p>In the image below you can see some of the auto-complete for the slicer module (there are more if I scrolled down in the pop-up).  There is no mrmlScene so unfortunately no <code>slicer.mrmlScene.XX</code> auto-complete. Also missing items for vtk. Maybe a setting can be changed, but I was just using the reference from <a class="mention" href="/u/alex_vergara">@Alex_Vergara</a>.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73ee0c0c78999f5ed5c0cb3480730997760b418c.png" alt="autocomplete-vscode2" data-base62-sha1="gxyVcqhFy9v3h1E1U0oCzbGX11y" width="423" height="299"></p>

---

## Post #15 by @apparrilla (2019-12-18 23:04 UTC)

<p>Ok. Now, I have libraries recognition and it´s really cool. I still have problems with pylint rope and autopep8. Python console throw this error.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2418717e6aeb0a0145d80beb62d5ac0ca011797e.png" alt="image" data-base62-sha1="59jyD1Obz1E60z5v6pUVJSYycrk" width="614" height="92"></p>
<p>Thank you all.</p>

---

## Post #16 by @lassoan (2019-12-19 04:05 UTC)

<p>The package name is <code>slicer.util</code> (and not <code>slicer.utils</code>).</p>

---

## Post #17 by @Alex_Vergara (2019-12-19 05:50 UTC)

<p>In windows project settings does not work, you need to edit global settings for vscode for it to work. Here it is my settings.json in <code>C:\Users\alexv\AppData\Roaming\Code\User\settings.json</code></p>
<pre data-code-wrap="json"><code class="lang-json">{
    "python.pythonPath": "C:\\Users\\alexv\\AppData\\Local\\NA-MIC\\Slicer 4.11.0-2019-11-05\\bin\\PythonSlicer.exe",
    "python.linting.pylintPath": "C:\\Users\\alexv\\AppData\\Local\\NA-MIC\\Slicer 4.11.0-2019-11-05\\lib\\Python\\Scripts\\pylint.exe",
    "python.formatting.autopep8Path": "C:\\Users\\alexv\\AppData\\Local\\NA-MIC\\Slicer 4.11.0-2019-11-05\\lib\\Python\\Scripts\\autopep8.exe",
    "python.autoComplete.extraPaths": [
        "C:\\Users\\alexv\\AppData\\Local\\NA-MIC\\Slicer 4.11.0-2019-11-05\\",
        "C:\\Users\\alexv\\AppData\\Local\\NA-MIC\\Slicer 4.11.0-2019-11-05\\bin\\",
        "C:\\Users\\alexv\\AppData\\Local\\NA-MIC\\Slicer 4.11.0-2019-11-05\\lib\\Python\\",
        "C:\\Users\\alexv\\AppData\\Local\\NA-MIC\\Slicer 4.11.0-2019-11-05\\lib\\QtPlugins\\",
        "C:\\Users\\alexv\\AppData\\Local\\NA-MIC\\Slicer 4.11.0-2019-11-05\\lib\\Slicer-4.11\\",
        "C:\\Users\\alexv\\AppData\\Local\\NA-MIC\\Slicer 4.11.0-2019-11-05\\lib\\Python\\Scripts\\",
    ],
    "python.linting.enabled": true,
    "git.autofetch": true
}
</code></pre>
<p>And you don’t need any python installed in your system, just python extension in vscode.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ead30756b76bebc3c3d905314ed916fafb9192b.png" data-download-href="/uploads/short-url/dvxWbR7ifDE1wTSGc8eWisBviav.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ead30756b76bebc3c3d905314ed916fafb9192b.png" alt="image" data-base62-sha1="dvxWbR7ifDE1wTSGc8eWisBviav" width="690" height="305" data-dominant-color="29292A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">993×439 32.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @lassoan (2019-12-20 03:28 UTC)

<p>Thank you. With the above settings I get auto-complete for native python classes (slicer.util, etc). This is good! Even VTK and other C++ wrapped libraries show up and classes are listed, but unfortunately method names and method documentation does not show up and auto-complete does not work either.</p>
<p>Maybe VTK’s Python wrapping could be made more friendly to IDEs, but with this we’ll have to wait until we upgrade to latest VTK master early next year.</p>

---

## Post #19 by @Alex_Vergara (2019-12-20 08:53 UTC)

<p>I think that is because vtk and ctk are located in a very different folder</p>
<pre><code class="lang-auto">E15TY:dosimetry4d alexvergaragil$ ls /Applications/Slicer.app/Contents/bin/Python/
SlicerWizard            ctk                     mrml.py                 qt                      slicer                  vtkAddon.py             vtkSegmentationCore.py  vtkmodules
__pycache__             freesurfer.py           mrmlDisplayableManager  sitkUtils.py            vtk.py                  vtkITK.py               vtkTeem.py
</code></pre>
<p>So adding it to autocomplete paths<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a99666b980f719501b6815e286ea8202d507a8ed.png" data-download-href="/uploads/short-url/oceVowWUN60ninLqCzYN5tHC1u5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a99666b980f719501b6815e286ea8202d507a8ed_2_690x244.png" alt="image" data-base62-sha1="oceVowWUN60ninLqCzYN5tHC1u5" width="690" height="244" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a99666b980f719501b6815e286ea8202d507a8ed_2_690x244.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a99666b980f719501b6815e286ea8202d507a8ed.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a99666b980f719501b6815e286ea8202d507a8ed.png 2x" data-dominant-color="27292B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">803×284 36.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
and<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/697b8c0cd794bc9980eb863ee9510cb890524a95.png" data-download-href="/uploads/short-url/f38PDbOs2Wf0dIsOJEkyjULuRoN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/697b8c0cd794bc9980eb863ee9510cb890524a95_2_690x36.png" alt="image" data-base62-sha1="f38PDbOs2Wf0dIsOJEkyjULuRoN" width="690" height="36" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/697b8c0cd794bc9980eb863ee9510cb890524a95_2_690x36.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/697b8c0cd794bc9980eb863ee9510cb890524a95_2_1035x54.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/697b8c0cd794bc9980eb863ee9510cb890524a95_2_1380x72.png 2x" data-dominant-color="2D2E2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1448×76 15.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My configuration file is now</p>
<pre><code class="lang-auto">{
    "python.pythonPath": "/Applications/Slicer.app/Contents/bin/SlicerPython",
    "python.autoComplete.extraPaths": [
        "/Applications/Slicer.app/Contents",
        "/Applications/Slicer.app/Contents/lib/Python",
        "/Applications/Slicer.app/Contents/lib/QtPlugins",
        "/Applications/Slicer.app/Contents/lib/Slicer-4.11",
        "/Applications/Slicer.app/Contents/bin/",
        "/Applications/Slicer.app/Contents/bin/Python/",
        "/Applications/Slicer.app/Contents/bin/Python/vtkmodules"
    ],
    "python.linting.pylintPath": "/Applications/Slicer.app/Contents/lib/Python/bin/pylint",
    "python.formatting.autopep8Path": "/Applications/Slicer.app/Contents/lib/Python/bin/autopep8",
    "python.linting.enabled": true,
    "git.autofetch": true
}
</code></pre>

---

## Post #20 by @apparrilla (2019-12-21 19:09 UTC)

<p>I still have problems  trying to fix Visual Studio Code configuration for Windows.</p>
<p>Proposed steps:</p>
<p>1º - Open Slicer Python Interector and install pylint, rope and autopep8:<br>
slicer.util.pip_install(“pylint rope autopep8”)</p>
<p>2º - Open Visual Studio Code settings.json (located in C:\Users"user"\AppData\Roaming\Code\User)</p>
<p>3º - Items to add:</p>
<blockquote>
<p>{<br>
“python.pythonpath”: “C:\Users\<strong>user</strong>\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\bin\SlicerPython.exe”,<br>
“python.linting.pylintPath”: “C:\Users\<strong>user</strong>\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\site-packages\pylint\”,<br>
“python.formatting.autopep8Path”: “C:\Users\<strong>user</strong>\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Scripts\autopep8.exe”,<br>
“python.autoComplete.extraPaths”: [<br>
“C:\Users\<strong>user</strong>\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\”,<br>
“C:\Users\<strong>user</strong>\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\”,<br>
“C:\Users\<strong>user</strong>\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\QtPlugins\”,<br>
“C:\Users\<strong>user</strong>\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Slicer-4.11\”,<br>
“C:\Users\<strong>user</strong>\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\bin\”,<br>
“C:\Users\<strong>user</strong>\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\site-packages\”,<br>
“C:\Users\<strong>user</strong>\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Scripts\”,<br>
],<br>
“python.linting.enabled”: true,<br>
“git.autofetch”: true<br>
}</p>
</blockquote>
<p>Now I have no errors in VSC but autocomplete is not working.</p>
<p>I´ve tried <a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> code but VSCode throws error in import libraries and others…</p>
<p>I have no clear idea of which are the right directies of Slicer we need to add to extraPaths nor there is any difference between pythonpath “SlicerPython” or “PythonSlicer.exe”.</p>
<p>If this issue is fixed, muybe it should be added to documentation …</p>
<p>Thanks to all</p>

---

## Post #21 by @lassoan (2019-12-21 19:26 UTC)

<aside class="quote no-group" data-username="apparrilla" data-post="20" data-topic="9496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>there is any difference between pythonpath “SlicerPython” or “PythonSlicer.exe”.</p>
</blockquote>
</aside>
<p>There is no difference. Originally, we added SlicerPython, but then we realized then PyCharm only accept interpreter name if it starts with “python”. We kept “SlicerPython” for backward compatibility but probably we’ll remove it at some point.</p>
<p>Note that autocomplete, breakpoints, step-by-step debugging, stack walking, running local commands, inspecting and modifying variables, etc. all already works perfectly if you <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools">attach Python debugger to a running Slicer</a> and put a breakpoint into the method that you are editing. So, all that we are trying to achieve here would just offer some additional convenience.</p>

---

## Post #22 by @apparrilla (2019-12-25 22:05 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="21" data-topic="9496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Note that autocomplete, breakpoints, step-by-step debugging, stack walking, running local commands, inspecting and modifying variables, etc. all already works perfectly if you <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools" rel="noopener nofollow ugc">attach Python debugger to a running Slicer</a> and put a breakpoint into the method that you are editing. So, all that we are trying to achieve here would just offer some additional convenience.</p>
</blockquote>
</aside>
<p>I agree with you debugger features are better than python config in VS Code…</p>
<p>If anyone want just to fix VS Code in Windows as we have been talking about can follow these steps:</p>
<p>1º - Open Slicer Python Interector and install pylint, rope and autopep8:<br>
slicer.util.pip_install(“pylint rope autopep8”)</p>
<p>2º - Open Visual Studio Code settings.json (located in C:\Users\“user”\AppData\Roaming\Code\User)</p>
<p>3º - Items to add:</p>
<blockquote>
<p>{<br>
“python.pythonPath”: “C:\Users\“user”\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\bin\SlicerPython.exe”,<br>
“python.linting.pylintPath”: “C:\Users\“user”\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\site-packages\pylint\”,<br>
“python.formatting.autopep8Path”: “C:\Users\“user”\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Scripts\autopep8.exe”,<br>
“python.autoComplete.extraPaths”: [<br>
“C:\Users\“user”\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\”,<br>
“C:\Users\“user”\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\”,<br>
“C:\Users\“user”\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\QtPlugins\”,<br>
“C:\Users\“user”\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Slicer-4.11\”,<br>
“C:\Users\“user”\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Scripts\”,<br>
“C:\Users\“user”\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\”,<br>
“C:\Users\“user”\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\site-packages\”,<br>
“C:\Users\“user”\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\site-packages\pylint\”,<br>
“C:\Users\“user”\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\bin\”,<br>
“C:\Users\“user”\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\bin\Python\”,<br>
“C:\Users\“user”\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\bin\Lib\site-packages\”,<br>
“C:\Users\“user”\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\bin\Lib\site-packages\vtkmodules\”,<br>
],<br>
“python.linting.enabled”: true,<br>
“git.autofetch”: true<br>
}</p>
</blockquote>
<p>Thanks so much for your support…</p>

---

## Post #23 by @lassoan (2019-12-26 19:07 UTC)

<p>I’ve created a script that collects all the above paths from the current Slicer instance and updates Visual Studio Code settings file automatically:</p>
<pre><code class="lang-python">import os
import json

# Make sure all required packages are installed
slicer.util.pip_install("pylint rope autopep8 jedi")

binPath = slicer.app.applicationDirPath()  # 'C:/Users/(username)/AppData/Local/NA-MIC/Slicer (version)/bin'
appPath = os.path.dirname(slicer.app.applicationDirPath())  # 'C:/Users/(username)/AppData/Local/NA-MIC/Slicer (version)'
pythonHomePath = os.getenv('PYTHONHOME')  # 'C:/Users/(username)/AppData/Local/NA-MIC/Slicer (version)/lib/Python'
vsCodeUserSettingsFilePath = os.path.join(os.getenv("APPDATA"),"Code/User/settings.json")

# Read VS code settings file
with open(vsCodeUserSettingsFilePath) as vsCodeUserSettingsFile:
    vsCodeUserSettings = json.load(vsCodeUserSettingsFile)

# Update settings

vsCodeUserSettings["python.pythonPath"] = os.path.normpath(os.path.join(binPath, "SlicerPython.exe"))

vsCodeUserSettings["python.linting.pylintPath"] = os.path.normpath(os.path.join(pythonHomePath, "Scripts/pylint.exe"))
vsCodeUserSettings["python.linting.enabled"] = True

vsCodeUserSettings["python.formatting.autopep8Path"] = os.path.normpath(os.path.join(pythonHomePath, "Scripts/autopep8.exe"))

vsCodeUserSettings["python.autoComplete.extraPaths"].append(os.path.normpath(appPath))
vsCodeUserSettings["python.autoComplete.extraPaths"].append(os.path.normpath(binPath))
vsCodeUserSettings["python.autoComplete.extraPaths"].append(os.path.normpath(pythonHomePath))
vsCodeUserSettings["python.autoComplete.extraPaths"].append(os.path.normpath(os.path.join(pythonHomePath, "Scripts")))
vsCodeUserSettings["python.autoComplete.extraPaths"].append(os.path.normpath(os.path.join(pythonHomePath, "Lib")))
vsCodeUserSettings["python.autoComplete.extraPaths"].append(os.path.normpath(os.path.join(pythonHomePath, "Lib/site-packages")))
vsCodeUserSettings["python.autoComplete.extraPaths"].append(os.path.normpath(os.path.join(pythonHomePath, "Lib/site-packages/pylint")))
vsCodeUserSettings["python.autoComplete.extraPaths"].append(os.path.normpath(os.path.join(binPath, "Lib/site-packages/vtkmodules")))
vsCodeUserSettings["python.autoComplete.extraPaths"].append(os.path.normpath(os.path.join(appPath, "lib/QtPlugins")))
# Remove duplicates
vsCodeUserSettings["python.autoComplete.extraPaths"] = list(set(vsCodeUserSettings["python.autoComplete.extraPaths"]))

# Write VS code settings file
with open(vsCodeUserSettingsFilePath, "w") as vsCodeUserSettingsFile:
    json.dump(vsCodeUserSettings, vsCodeUserSettingsFile, indent=4)
</code></pre>
<p>Unfortunately, it does not do much for me. For example, if I type:</p>
<pre><code class="lang-python">import vtkSegmentationCore as sc
s = sc.vtkSegmentation()
</code></pre>
<p>then methods of object <code>s</code> do not show up. If anybody can make VTK, MRML, CTK, or Qt method name auto-complete work in VS Code then please let me know.</p>

---

## Post #24 by @DhruvKoolRajamani (2020-10-20 06:58 UTC)

<p>C++ Tips: Using the CMake Tool by Microsoft really helped as it also provides the option to add generated build files to intellisense automatically (also need to have the c++ extension by microsoft installed). I’ve also attached my tasks.json and launch.json that launches slicer with my loadable c++ extension by pressing F5.</p>
<p><strong>I open vscode in the base directory of my extension </strong><br>
<strong>Make sure to change  to your extensions name to launch correctly</strong></p>
<p><strong>launch.json</strong></p>
<pre><code class="lang-auto">{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "(Linux) Launch Extension",
      "type": "cppdbg",
      "request": "launch",
      "program": "${workspaceFolder}/build/SlicerWith&lt;NAME OF EXTENSION&gt;",
      "args": [
        "--attach-process"
      ],
      "preLaunchTask": "(Linux) build",
      "stopAtEntry": true,
      "cwd": "${workspaceFolder}",
      "launchCompleteCommand": "exec-run",
      "linux": {
        "MIMode": "gdb",
        "miDebuggerPath": "/usr/bin/gdb"
      },
      "symbolLoadInfo": {
        "loadAll": true,
        "exceptionList": ""
      },
      "environment": [],
      "externalConsole": true,
      "additionalSOLibSearchPath": "${workspaceFolder}/build/lib/Slicer-4.11/qt-loadable-modules;&lt;PATH TO SLICER BUILD&gt;/Slicer-build/lib/Slicer-4.11/qt-loadable-modules"
    }
  ]
}
</code></pre>
<p><strong>tasks.json</strong></p>
<pre><code class="lang-auto">{
  "tasks": [
    {
      "label": "(Linux) build",
      "type": "shell",
      "command": "cmake --build ${workspaceFolder}/build --config Debug --target all -- -j &lt;NUMBER OF CORES&gt; ../"
    }
  ],
  "version": "2.0.0"
}
</code></pre>
<p><em>Notes</em></p>
<ul>
<li>Make sure to change all instances with angle brackets inside to match your computers settings.</li>
<li>I’m still trying to figure out how to debug cpp with vscode instead of having to use gdb. As of now, you will have to open gdb separately in a terminal after starting the above code (basically running your extension <code>./SlicerWith(Extension Name) --atach-process)</code> to get your process id. Then in a new terminal:</li>
</ul>
<pre><code class="lang-bash">gdb -p &lt;process_id&gt;
(gdb) # place breakpoints
(gdb) continue # to run
</code></pre>

---

## Post #25 by @smoudour (2023-11-06 10:42 UTC)

<p>I have followed the conversation and have set up my settings.json as such:</p>
<blockquote>
<p>“python.pythonPath”: “C:\Users\smoudour\AppData\Local\slicer.org\Slicer 5.4.0\bin\PythonSlicer.exe”,<br>
“python.linting.pylintPath”: “C:\Users\smoudour\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\pylint.exe”,<br>
“python.formatting.autopep8Path”: “C:\Users\smoudour\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\autopep8.exe”,<br>
“python.autoComplete.extraPaths”: [<br>
“C:\Users\smoudour\AppData\Local\slicer.org\Slicer 5.4.0”,<br>
“C:\Users\smoudour\AppData\Local\slicer.org\Slicer 5.4.0\bin\”,<br>
“C:\Users\smoudour\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\”,<br>
“C:\Users\smoudour\AppData\Local\slicer.org\Slicer 5.4.0\lib\QtPlugins\”,<br>
“C:\Users\smoudour\AppData\Local\slicer.org\Slicer 5.4.0\lib\Slicer-5.4\”,<br>
“C:\Users\smoudour\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\”,<br>
],<br>
“python.linting.enabled”: true,<br>
“git.autofetch”: true,<br>
“python.analysis.extraPaths”: [<br>
“C:\Users\smoudour\AppData\Local\slicer.org\Slicer 5.4.0”,<br>
“C:\Users\smoudour\AppData\Local\slicer.org\Slicer 5.4.0\bin\”,<br>
“C:\Users\smoudour\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\”,<br>
“C:\Users\smoudour\AppData\Local\slicer.org\Slicer 5.4.0\lib\QtPlugins\”,<br>
“C:\Users\smoudour\AppData\Local\slicer.org\Slicer 5.4.0\lib\Slicer-5.4\”,<br>
“C:\Users\smoudour\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\”<br>
],<br>
“editor.fontLigatures”: false</p>
</blockquote>
<p>Problems are:</p>
<ol>
<li>it still doesn’t work. Do I need to instal slicer using conda for this to work?</li>
<li>python.pythonPath, python.linting.pylinPath and some other keywords in vscode settings.json are labelled as “Unknown configuration setting”, so that’s why it probably does not work. Any help with this?</li>
</ol>

---
