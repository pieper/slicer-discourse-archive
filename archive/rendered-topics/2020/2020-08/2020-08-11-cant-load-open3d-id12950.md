# Can't load open3d

**Topic ID**: 12950
**Date**: 2020-08-11
**URL**: https://discourse.slicer.org/t/cant-load-open3d/12950

---

## Post #1 by @lokpoon (2020-08-11 21:56 UTC)

<p>Hi,</p>
<p>I’m just starting to get Slicer on my mac (os 10.13) ready for the SlicerMorph workshop. When I load ALPACA it prompts me to install open3d. After it is done Slicer crashes and quit. I tried to uninstall and reinstalling open3d, and didn’t receive any error message. But when I import open3d or load ALPACA, Slicer still crashes and quit.</p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2020-08-11 23:05 UTC)

<aside class="quote no-group" data-username="lokpoon" data-post="1" data-topic="12950">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/898d66/48.png" class="avatar"> lokpoon:</div>
<blockquote>
<p>nstall open3d. After it is done Slicer crashes and quit.</p>
</blockquote>
</aside>
<p>Can you:</p>
<ol>
<li>type <code>pip_install("open3d")</code> into your python console and paste log.</li>
<li>After the pip install, type<code> import open3d</code> into your console, and paste the error message (if there is one).</li>
</ol>

---

## Post #3 by @lokpoon (2020-08-11 23:22 UTC)

<p>Below is the log. Import open3d still crashes and quit Slicer, do you want the system crash report?</p>
<p>pip_install(“open3d”)</p>
<p>Requirement already satisfied: open3d in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (0.9.0.0)</p>
<p>Requirement already satisfied: ipywidgets in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from open3d) (7.5.1)</p>
<p>Requirement already satisfied: numpy in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from open3d) (1.19.1)</p>
<p>Requirement already satisfied: notebook in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from open3d) (6.0.3)</p>
<p>Requirement already satisfied: widgetsnbextension in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from open3d) (3.5.1)</p>
<p>Requirement already satisfied: nbformat&gt;=4.2.0 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipywidgets-&gt;open3d) (5.0.7)</p>
<p>Requirement already satisfied: ipykernel&gt;=4.5.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipywidgets-&gt;open3d) (5.3.4)</p>
<p>Requirement already satisfied: ipython&gt;=4.0.0; python_version &gt;= “3.3” in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipywidgets-&gt;open3d) (7.16.1)</p>
<p>Requirement already satisfied: traitlets&gt;=4.3.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipywidgets-&gt;open3d) (4.3.3)</p>
<p>Requirement already satisfied: Send2Trash in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook-&gt;open3d) (1.5.0)</p>
<p>Requirement already satisfied: tornado&gt;=5.0 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook-&gt;open3d) (6.0.4)</p>
<p>Requirement already satisfied: terminado&gt;=0.8.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook-&gt;open3d) (0.8.3)</p>
<p>Requirement already satisfied: ipython-genutils in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook-&gt;open3d) (0.2.0)</p>
<p>Requirement already satisfied: jupyter-core&gt;=4.6.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook-&gt;open3d) (4.6.3)</p>
<p>Requirement already satisfied: jupyter-client&gt;=5.3.4 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook-&gt;open3d) (6.1.6)</p>
<p>Requirement already satisfied: pyzmq&gt;=17 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook-&gt;open3d) (19.0.2)</p>
<p>Requirement already satisfied: nbconvert in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook-&gt;open3d) (5.6.1)</p>
<p>Requirement already satisfied: prometheus-client in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook-&gt;open3d) (0.8.0)</p>
<p>Requirement already satisfied: jinja2 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook-&gt;open3d) (2.11.2)</p>
<p>Requirement already satisfied: jsonschema!=2.5.0,&gt;=2.4 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbformat&gt;=4.2.0-&gt;ipywidgets-&gt;open3d) (3.2.0)</p>
<p>Requirement already satisfied: appnope; platform_system == “Darwin” in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipykernel&gt;=4.5.1-&gt;ipywidgets-&gt;open3d) (0.1.0)</p>
<p>Requirement already satisfied: pickleshare in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipython&gt;=4.0.0; python_version &gt;= “3.3”-&gt;ipywidgets-&gt;open3d) (0.7.5)</p>
<p>Requirement already satisfied: pygments in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipython&gt;=4.0.0; python_version &gt;= “3.3”-&gt;ipywidgets-&gt;open3d) (2.6.1)</p>
<p>Requirement already satisfied: setuptools&gt;=18.5 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipython&gt;=4.0.0; python_version &gt;= “3.3”-&gt;ipywidgets-&gt;open3d) (49.2.0)</p>
<p>Requirement already satisfied: jedi&gt;=0.10 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipython&gt;=4.0.0; python_version &gt;= “3.3”-&gt;ipywidgets-&gt;open3d) (0.17.2)</p>
<p>Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,&lt;3.1.0,&gt;=2.0.0 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipython&gt;=4.0.0; python_version &gt;= “3.3”-&gt;ipywidgets-&gt;open3d) (3.0.6)</p>
<p>Requirement already satisfied: decorator in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipython&gt;=4.0.0; python_version &gt;= “3.3”-&gt;ipywidgets-&gt;open3d) (4.4.2)</p>
<p>Requirement already satisfied: backcall in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipython&gt;=4.0.0; python_version &gt;= “3.3”-&gt;ipywidgets-&gt;open3d) (0.2.0)</p>
<p>Requirement already satisfied: pexpect; sys_platform != “win32” in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipython&gt;=4.0.0; python_version &gt;= “3.3”-&gt;ipywidgets-&gt;open3d) (4.8.0)</p>
<p>Requirement already satisfied: six in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from traitlets&gt;=4.3.1-&gt;ipywidgets-&gt;open3d) (1.15.0)</p>
<p>Requirement already satisfied: ptyprocess; os_name != “nt” in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from terminado&gt;=0.8.1-&gt;notebook-&gt;open3d) (0.6.0)</p>
<p>Requirement already satisfied: python-dateutil&gt;=2.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jupyter-client&gt;=5.3.4-&gt;notebook-&gt;open3d) (2.8.1)</p>
<p>Requirement already satisfied: bleach in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbconvert-&gt;notebook-&gt;open3d) (3.1.5)</p>
<p>Requirement already satisfied: mistune&lt;2,&gt;=0.8.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbconvert-&gt;notebook-&gt;open3d) (0.8.4)</p>
<p>Requirement already satisfied: testpath in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbconvert-&gt;notebook-&gt;open3d) (0.4.4)</p>
<p>Requirement already satisfied: defusedxml in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbconvert-&gt;notebook-&gt;open3d) (0.6.0)</p>
<p>Requirement already satisfied: pandocfilters&gt;=1.4.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbconvert-&gt;notebook-&gt;open3d) (1.4.2)</p>
<p>Requirement already satisfied: entrypoints&gt;=0.2.2 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbconvert-&gt;notebook-&gt;open3d) (0.3)</p>
<p>Requirement already satisfied: MarkupSafe&gt;=0.23 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jinja2-&gt;notebook-&gt;open3d) (1.1.1)</p>
<p>Requirement already satisfied: importlib-metadata; python_version &lt; “3.8” in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jsonschema!=2.5.0,&gt;=2.4-&gt;nbformat&gt;=4.2.0-&gt;ipywidgets-&gt;open3d) (1.7.0)</p>
<p>Requirement already satisfied: attrs&gt;=17.4.0 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jsonschema!=2.5.0,&gt;=2.4-&gt;nbformat&gt;=4.2.0-&gt;ipywidgets-&gt;open3d) (19.3.0)</p>
<p>Requirement already satisfied: pyrsistent&gt;=0.14.0 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jsonschema!=2.5.0,&gt;=2.4-&gt;nbformat&gt;=4.2.0-&gt;ipywidgets-&gt;open3d) (0.16.0)</p>
<p>Requirement already satisfied: parso&lt;0.8.0,&gt;=0.7.0 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jedi&gt;=0.10-&gt;ipython&gt;=4.0.0; python_version &gt;= “3.3”-&gt;ipywidgets-&gt;open3d) (0.7.1)</p>
<p>Requirement already satisfied: wcwidth in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,&lt;3.1.0,&gt;=2.0.0-&gt;ipython&gt;=4.0.0; python_version &gt;= “3.3”-&gt;ipywidgets-&gt;open3d) (0.2.5)</p>
<p>Requirement already satisfied: packaging in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from bleach-&gt;nbconvert-&gt;notebook-&gt;open3d) (20.4)</p>
<p>Requirement already satisfied: webencodings in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from bleach-&gt;nbconvert-&gt;notebook-&gt;open3d) (0.5.1)</p>
<p>Requirement already satisfied: zipp&gt;=0.5 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from importlib-metadata; python_version &lt; “3.8”-&gt;jsonschema!=2.5.0,&gt;=2.4-&gt;nbformat&gt;=4.2.0-&gt;ipywidgets-&gt;open3d) (3.1.0)</p>
<p>Requirement already satisfied: pyparsing&gt;=2.0.2 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from packaging-&gt;bleach-&gt;nbconvert-&gt;notebook-&gt;open3d) (2.4.7)</p>
<p>WARNING: You are using pip version 20.1.1; however, version 20.2.1 is available.</p>
<p>You should consider upgrading via the ‘/Applications/Slicer.app/Contents/bin/./python-real -m pip install --upgrade pip’ command.</p>

---

## Post #4 by @smrolfe (2020-08-11 23:33 UTC)

<p>Thanks, this all looks normal, could you post the crash report also?</p>
<p>In Slicer, if you go to Help -&gt; Report a bug you can see the current Slicer log file. If you change the “Recent log files” selector to the previous log report you may see more information about what caused the crash.</p>

---

## Post #5 by @lokpoon (2020-08-11 23:45 UTC)

<p>There is this message in the system crash report:<br>
Termination Reason:    DYLD, [0x4] Symbol missing</p>
<p>Dyld Error Message:<br>
Symbol not found: ____chkstk_darwin<br>
Referenced from: /Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/open3d/open3d.cpython-36m-darwin.so (which was built for Mac OS X 10.15)<br>
Expected in: /usr/lib/libSystem.B.dylib</p>
<p>Below is the log from the previous crash session after import open3d:</p>
<p>[DEBUG][Qt] 11.08.2020 16:36:43 [] (unknown:0) - Session start time …: 2020-08-11 16:36:43<br>
[DEBUG][Qt] 11.08.2020 16:36:43 [] (unknown:0) - Slicer version …: 4.11.0-2020-08-10 (revision 29263 / 6afabbc) macosx-amd64 - installed release<br>
[DEBUG][Qt] 11.08.2020 16:36:43 [] (unknown:0) - Operating system …: Mac OS X / 10.13.6 / 17G66 - 64-bit<br>
[DEBUG][Qt] 11.08.2020 16:36:43 [] (unknown:0) - Memory …: 8192 MB physical, 2048 MB virtual<br>
[DEBUG][Qt] 11.08.2020 16:36:43 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i7-2820QM CPU @ 2.30GHz, 4 cores, 8 logical processors<br>
[DEBUG][Qt] 11.08.2020 16:36:43 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 11.08.2020 16:36:43 [] (unknown:0) - Qt configuration …: version 5.15.0, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 11.08.2020 16:36:43 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 11.08.2020 16:36:43 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 11.08.2020 16:36:43 [] (unknown:0) - Application path …: /Applications/Slicer.app/Contents/MacOS<br>
[DEBUG][Qt] 11.08.2020 16:36:43 [] (unknown:0) - Additional module paths …: /Applications/Slicer.app/Contents/Extensions-29263/RawImageGuess/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29263/SlicerIGT/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer.app/Contents/Extensions-29263/SlicerIGT/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29263/Auto3dgm/lib/Slicer-4.11/cli-modules, /Applications/Slicer.app/Contents/Extensions-29263/Auto3dgm/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29263/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29263/SlicerDcm2nii/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29263/Sandbox/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29263/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer.app/Contents/Extensions-29263/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29263/SurfaceWrapSolidify/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Python] 11.08.2020 16:36:46 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[WARNING][Qt] 11.08.2020 16:36:46 [] (unknown:0) - libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space<br>
[CRITICAL][Stream] 11.08.2020 16:36:47 [] (unknown:0) - /Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pandas/compat/<strong>init</strong>.py:120: UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.<br>
[CRITICAL][Stream] 11.08.2020 16:36:47 [] (unknown:0) -   warnings.warn(msg)<br>
[WARNING][Qt] 11.08.2020 16:36:47 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[DEBUG][Python] 11.08.2020 16:36:53 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 11.08.2020 16:36:56 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 11.08.2020 16:36:57 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Python] 11.08.2020 16:37:00 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: ExportAs<br>
[DEBUG][Qt] 11.08.2020 16:36:58 [] (unknown:0) - Switch to module:  “Welcome”</p>

---

## Post #6 by @smrolfe (2020-08-11 23:54 UTC)

<p>Thanks. It looks like this version of open3d isn’t compatible with Mac OS before 10.15. Could you try the following:</p>
<blockquote>
<p>pip_uninstall(‘open3d’)<br>
slicer.util.pip_install(‘open3d==0.8.0’)</p>
</blockquote>

---

## Post #7 by @lokpoon (2020-08-12 00:07 UTC)

<p>Installing open3d (0.8.0) works, now it doesn’t crash. Thanks!</p>

---

## Post #8 by @smrolfe (2020-08-12 00:35 UTC)

<p>Thanks for following up <a class="mention" href="/u/lokpoon">@lokpoon</a>, that’s great news.</p>

---
