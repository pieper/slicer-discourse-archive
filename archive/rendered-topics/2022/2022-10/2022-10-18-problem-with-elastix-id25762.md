# Problem with Elastix

**Topic ID**: 25762
**Date**: 2022-10-18
**URL**: https://discourse.slicer.org/t/problem-with-elastix/25762

---

## Post #1 by @Alex_Vergara (2022-10-18 18:06 UTC)

<p>I have a problem lately with elastix, it doesn’t execute anything.</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/alex/GIT/opendose3d/OpenDose3D/OpenDose3D.py", line 944, in onRunTestButton
    self.test.FullTest_positive()
  File "/home/alex/GIT/opendose3d/OpenDose3D/Logic/OpenDose3DTest.py", line 544, in FullTest_positive
    self.logic.createTransforms(referenceNode.data)
  File "/home/alex/GIT/opendose3d/OpenDose3D/Logic/OpenDose3DLogic.py", line 963, in createTransforms
    elastixLogic.registerVolumes(
  File "/home/alex/.config/NA-MIC/Extensions-31204/SlicerElastix/lib/Slicer-5.1/qt-scripted-modules/Elastix.py", line 818, in registerVolumes
    self.logProcessOutput(ep)
  File "/home/alex/.config/NA-MIC/Extensions-31204/SlicerElastix/lib/Slicer-5.1/qt-scripted-modules/Elastix.py", line 739, in logProcessOutput
    raise subprocess.CalledProcessError(return_code, "elastix")
subprocess.CalledProcessError: Command 'elastix' returned non-zero exit status 127.
</code></pre>
<p>This is probably due to the use of older version libraries as it also throws at launch</p>
<pre><code class="lang-auto">libdcmjpls.so.16: cannot open shared object file: No such file or directory
</code></pre>
<p>I have libdcmjpls.so.17 but not libdcmjpls.so.16<br>
I presume this will also be true for a lot of other libraries so I don’t want to manually create links to each of the missing ones.<br>
Any solution to recompile elastix and include it into Slicer?</p>

---

## Post #2 by @lassoan (2022-10-19 05:30 UTC)

<p>Elastix is compiled and bundled with the extension. If you want to use this version that is already included then remove the <code>Custom Elastix toolbox location</code> that you specified in the Advanced section.</p>

---

## Post #3 by @Alex_Vergara (2022-10-19 08:07 UTC)

<p>Using custom elastix binary (compiled myself) I get</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/alex/GIT/opendose3d/OpenDose3D/OpenDose3D.py", line 944, in onRunTestButton
    self.test.FullTest_positive()
  File "/home/alex/GIT/opendose3d/OpenDose3D/Logic/OpenDose3DTest.py", line 544, in FullTest_positive
    self.logic.createTransforms(referenceNode.data)
  File "/home/alex/GIT/opendose3d/OpenDose3D/Logic/OpenDose3DLogic.py", line 969, in createTransforms
    elastixLogic.registerVolumes(
  File "/home/alex/.config/NA-MIC/Extensions-31204/SlicerElastix/lib/Slicer-5.1/qt-scripted-modules/Elastix.py", line 817, in registerVolumes
    ep = self.startElastix(inputParamsElastix)
  File "/home/alex/.config/NA-MIC/Extensions-31204/SlicerElastix/lib/Slicer-5.1/qt-scripted-modules/Elastix.py", line 498, in startElastix
    return subprocess.Popen([executableFilePath] + cmdLineArguments, env=self.getElastixEnv(),
  File "/home/alex/.config/NA-MIC/Extensions-31204/SlicerElastix/lib/Slicer-5.1/qt-scripted-modules/Elastix.py", line 444, in getElastixEnv
    elastixEnv["PATH"] = elastixBinDir + os.pathsep + elastixEnv["PATH"] if elastixEnv.get("PATH") else elastixBinDir
TypeError: unsupported operand type(s) for +: 'PosixPath' and 'str'
</code></pre>

---

## Post #4 by @Alex_Vergara (2022-10-19 08:48 UTC)

<p>On top of that look, this is most likely a problem of an ITK version upgrade (I have previous version 5.2)</p>
<pre><code class="lang-auto">[alex@alex-b450aoruselite ~]$ /opt/3dslicer/NA-MIC/Extensions-31118/SlicerElastix/lib/Slicer-5.1/elastix --help
/opt/3dslicer/NA-MIC/Extensions-31118/SlicerElastix/lib/Slicer-5.1/elastix: error while loading shared libraries: libITKConvolution-5.3.so.1: cannot open shared object file: No such file or directory
</code></pre>
<p>this does not happen with my custom elastix</p>
<pre><code class="lang-auto">[alex@alex-b450aoruselite ~]$ elastix --help
elastix version: 5.000

elastix registers a moving image to a fixed image.
The registration-process is specified in the parameter file.
  --help, -h displays this message and exit
  --version  output version information and exit
  --extended-version  output extended version information and exit

Call elastix from the command line with mandatory arguments:
  -f        fixed image
  -m        moving image
  -out      output directory
  -p        parameter file, elastix handles 1 or more "-p"

Optional extra commands:
  -fMask    mask for fixed image
  -mMask    mask for moving image
  -t0       parameter file for initial transform
  -priority set the process priority to high, abovenormal, normal (default),
            belownormal, or idle (Windows only option)
  -threads  set the maximum number of threads of elastix

The parameter-file must contain all the information necessary for elastix to run properly. That includes which metric to use, which optimizer, which transform, etc. It must also contain information specific for the metric, optimizer, transform, etc. For a usable parameter-file, see the website.

Need further help?
Check the website http://elastix.isi.uu.nl, or mail elastix@bigr.nl.
</code></pre>
<p>I will retry after upgrading my local ITK version</p>

---

## Post #5 by @Alex_Vergara (2022-10-19 09:38 UTC)

<p>It didn’t worked, Slicer insists in installing itk 5.2 while elastix expects 5.3. I will recompile Slicer using system ITK 5.3</p>

---

## Post #6 by @lassoan (2022-10-19 16:19 UTC)

<p>Different ITK versions are not ABI compatible. You have several options:</p>
<ul>
<li>use Elastix bundled with the SlicerElastix extension: this is the case for the Elastix binary already bundled with the extension. I would recommend this. It works well on Windows and Linux (just tested the latest Slicer Preview Release). As usual, there may be additional issues on macOS, maybe due to rpaths - let us know if this does not seem to work for you.</li>
<li>build Slicer and SlicerElastix extensions: they will then use the same ITK version.</li>
<li>build a custom Elastix executable: it is important to link ITK statically or fiddle with the environment (<code>getElastixEnv</code> function) if you use a different ITK version for Elastix, to make sure it does not pick up ITK DLLs from Slicer</li>
</ul>

---

## Post #7 by @Alex_Vergara (2022-10-19 16:52 UTC)

<p>I am using slicer and elastix compiled by myself, but I install slicerElastix from manager. Maybe its a good idea to compile it too, thanks for the idea</p>

---

## Post #8 by @Alex_Vergara (2022-10-19 19:30 UTC)

<p>I have to modify the lines 444 and 449 of elastix.py to</p>
<pre><code class="lang-auto">#line 444
elastixEnv["PATH"] = os.path.join(elastixBinDir,elastixEnv["PATH"]) if elastixEnv.get("PATH") else elastixBinDir
#line 449
elastixEnv["LD_LIBRARY_PATH"] = os.path.join(elastixLibDir,elastixEnv["LD_LIBRARY_PATH"]) if elastixEnv.get("LD_LIBRARY_PATH") else elastixLibDir
</code></pre>
<p>Then no more exceptions, but elastix is still not running and segfaults Slicer with the error</p>
<pre><code class="lang-auto">error: [/home/alex/Programas/Slicer-5.1.0-2022-10-18-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p>I also have a lot of errors at start (maybe unrelated)</p>
<pre><code class="lang-auto">qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in ""
QVariant::save: unable to save type 'PythonQtSafeObjectPtr' (type id: 1132).

QVariant::save: unable to save type 'PythonQtSafeObjectPtr' (type id: 1132).

QVariant::save: unable to save type 'PythonQtSafeObjectPtr' (type id: 1132).

QVariant::save: unable to save type 'PythonQtSafeObjectPtr' (type id: 1132).

QVariant::save: unable to save type 'PythonQtSafeObjectPtr' (type id: 1132).

QVariant::save: unable to save type 'PythonQtSafeObjectPtr' (type id: 1132).

QVariant::save: unable to save type 'PythonQtSafeObjectPtr' (type id: 1132).

QVariant::save: unable to save type 'PythonQtSafeObjectPtr' (type id: 1132).

Switch to module:  "Welcome"
</code></pre>

---

## Post #9 by @lassoan (2022-10-19 19:51 UTC)

<p>It would be great if you could submit a pull request with a proposed change that fixes the issue for you.</p>
<blockquote>
<p>qt.qpa.plugin: Could not find the Qt platform plugin “wayland”</p>
</blockquote>
<p>This is due to Qt5’s limited wayland support. If it does not cause any visible rendering issues for you then you can safely ignore it.</p>
<blockquote>
<p>QVariant::save: unable to save type ‘PythonQtSafeObjectPtr’ (type id: 1132).</p>
</blockquote>
<p>I haven’t seen this issue before. It would be nice if you could add a breakpoint into <code>ctkErrorLogModelQtMessageOutput</code> method in <code>CTK\Libs\Core\ctkErrorLogQtMessageHandler.cpp</code> and see where it is triggered from.</p>

---

## Post #10 by @Alex_Vergara (2022-10-19 19:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="25762">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be great if you could submit a pull request with a proposed change that fixes the issue for you.</p>
</blockquote>
</aside>
<p>This is already done in <a href="https://github.com/lassoan/SlicerElastix/pull/34" rel="noopener nofollow ugc">SlicerElastix github</a></p>

---

## Post #11 by @Alex_Vergara (2022-10-19 19:53 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="9" data-topic="25762">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<blockquote>
<p>qt.qpa.plugin: Could not find the Qt platform plugin “wayland”</p>
</blockquote>
<p>This is due to Qt5’s limited wayland support. If it does not cause any visible rendering issues for you then you can safely ignore it.</p>
</blockquote>
</aside>
<p>No problem visually, my system just treat it as XWayland (ugly but functional)</p>

---

## Post #12 by @Alex_Vergara (2022-10-19 20:05 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="9" data-topic="25762">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<blockquote>
<p>QVariant::save: unable to save type ‘PythonQtSafeObjectPtr’ (type id: 1132).</p>
</blockquote>
<p>I haven’t seen this issue before. It would be nice if you could add a breakpoint into <code>ctkErrorLogModelQtMessageOutput</code> method in <code>CTK\Libs\Core\ctkErrorLogQtMessageHandler.cpp</code> and see where it is triggered from.</p>
</blockquote>
</aside>
<p>Well, this error I can say with a good certainty is because I am using top edge software. So this has to be unrelated to the original issue.</p>
<p>The original problem persisted with fresh copy of Slicer, fresh cache, fresh everything.<br>
Download from internet the binary, extracted to home folder, installed SlicerElastix, executing it (Switching to Module) gives segfault with no further information.</p>
<pre><code class="lang-auto">error: [/home/alex/Programas/Slicer-5.1.0-2022-10-18-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>

---

## Post #13 by @lassoan (2022-10-19 20:39 UTC)

<p>The startup issue occurs before you install anything, the first time to try to run Slicer? If yes, then it is not related to Elastix, so please create a new topic for it. Thanks!</p>

---

## Post #14 by @Alex_Vergara (2022-10-19 22:39 UTC)

<p>It started occurring when I moved to kernel 6.0, but thinking better now, this might be actually related as elastix stopped working at the same time.</p>

---
