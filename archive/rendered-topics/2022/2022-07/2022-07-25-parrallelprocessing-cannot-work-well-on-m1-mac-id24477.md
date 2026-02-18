# ParrallelProcessing cannot work well on M1 Mac

**Topic ID**: 24477
**Date**: 2022-07-25
**URL**: https://discourse.slicer.org/t/parrallelprocessing-cannot-work-well-on-m1-mac/24477

---

## Post #1 by @wrc (2022-07-25 12:41 UTC)

<p>Hi, I am developing an extension based on ParrallelProcessing. This extension will run a python script in another CPU core. If the process ends, the script will be run again. It works well in most cases but fails <strong>sometimes</strong> (after several loops) on my M1 Mac. The 3D Slicer window closes automatically during calculation. I tried to run it on Windows PC. It <strong>never</strong> failed and everything is well. So, I think the problem comes from Rosetta2 on M1 Mac. I first checked the last line in error log:</p>
<p><code>[Python] (/Applications/Slicer.app/Contents/Extensions-30822/ParallelProcessing/lib/Slicer-5.0/qt-scripted-modules/Processes.py:230) - Name: state: Starting, last error: UnknownError</code></p>
<p>If it works fine, the next five lines should be:</p>
<pre><code class="lang-auto">[] (unknown:0) - Name: state: Starting, last error: UnknownError
[Python] (/Applications/Slicer.app/Contents/Extensions-30822/ParallelProcessing/lib/Slicer-5.0/qt-scripted-modules/Processes.py:230) – Name: state: Running, last error: UnknownError
Python] (/Applications/Slicer.app/Contents/Extensions-30822/ParallelProcessing/lib/Slicer-5.0/qt-scripted-modules/Processes.py:244) - Name: writing input
[] (unknown:0) - Name: state: Running, last error: UnknownError
[] (unknown:0) - Name: writing input
</code></pre>
<p>Therefore, there is something wrong on <strong>starting</strong>, not running. The error does not come from my script, but in line 227 of <code>Processes.py</code>:</p>
<p><code>self.start("PythonSlicer", [self.scriptPath,])</code></p>
<p>I added two logs before and after this line and only the first one is logged correctly.</p>
<p>Another interesting thing is, this phenomenon depends on the script. If I change some function in my script but remain the same input and output, it will work well on my M1 Mac. However, it seems to contradict the previous conclusion.</p>
<p>I think the problem comes from qt.QProcess. It may be not compatible with M1 Mac. I will be thankful if an ARM version 3DSlicer is provided.</p>

---

## Post #2 by @pieper (2022-07-25 19:11 UTC)

<p>Thanks for the report.  I recently got an M2 mac and I didn’t see any problems with Slicer but I didn’t try the ParallelProcessing extension.  Are you able to run the SelfTests?  Or can you provide an example that replicates the error?  Perhaps there’s a way to catch the error and retry.</p>
<p>Regarding a native ARM version of Slicer it’ll probably happen at some point but I don’t know a timeline, so better to see if this can bedebugged.</p>

---

## Post #3 by @wrc (2022-07-28 08:09 UTC)

<p>Yes, I can run the test in ParrallelProcessing extension. Would you please open the Processes module, click “reload and test” and close the Slicer window after finished? The MacOS will tell you Slicer quit unexpectedly. I think it is the similar problem as I faced. Thank you.</p>

---

## Post #4 by @pieper (2022-07-28 13:35 UTC)

<p>Hmm, I’m not seeing that behavior.  I ran did the Reload and Test on the Processes module with Slicer 5.0.3 on a macbook air M2 and did not get an unusual messages or crash at exit.  Mine is a pretty much fresh install.  Maybe you have something else installed in your Slicer python environment?  You can download a new copy of Slicer and test it in isolation.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19be054df9a16a19f07ae787e4cce42c3dc2e081.png" alt="Screen Shot 2022-07-28 at 9.32.10 AM" data-base62-sha1="3FJ3mE566Nra7qeWyMRxPCRL6cF" width="269" height="155"></p>

---

## Post #5 by @wrc (2022-07-29 11:43 UTC)

<p>There is no crash at exit. But after exit about 3 seconds, the MacOS system will tell you Slicer quit unexpectedly. I have uninstalled Slicer 5.0.2 (just move to trash and clean it) and installed Slicer 5.0.3. Then, I installed ParrallelProcessing and did Reload and Test. I got the same result. Maybe there are other files I haven’t deleted. Do you know how to uninstall thoroughly?<br>
PS: I am using MacOS 12.5 and M1Pro chip.</p>

---

## Post #6 by @pieper (2022-07-29 20:55 UTC)

<p>I had  macOS 12.4 before, but today it updated to 12.5 so I tested again and this time I get the same message about quitting unexpectedly.  This may not be related to the OS version though, because the stack trace indicates that <code>PythonQtShell_QProcess::event(QEvent*)</code> is being invoked during the application destruction process.</p>
<p>I take this to mean that the <code>Process</code> python class (which inherits from <code>QProcess</code>) still has signal/slot connections being invoked even though the object is out of scope or partially destructed.  Inheriting a Python class from a PythonQt superclass isn’t something we typically do so maybe we need to be careful with the teardown process, especially when there are signal/slot connections.</p>
<p>One possible solution would be to call <code>disconnect</code> in <code>onFinished</code> for all the <code>connect</code> calls made in <code>__init__</code>.</p>
<pre><code class="lang-auto">0   libpython3.9.dylib            	       0x138713f12 PyErr_Occurred + 18
1   libpython3.9.dylib            	       0x138645955 find_name_in_mro + 165
2   libpython3.9.dylib            	       0x13864581f _PyType_Lookup + 111
3   libpython3.9.dylib            	       0x138633133 _PyObject_GenericGetAttrWithDict + 131
4   libPythonQt.dylib             	       0x11626aa5a PythonQtShell_QProcess::event(QEvent*) + 106
5   QtWidgets                     	       0x10f2eca1a QApplicationPrivate::notify_helper(QObject*, QEvent*) + 266
6   QtWidgets                     	       0x10f2ede41 QApplication::notify(QObject*, QEvent*) + 497
7   QtCore                        	       0x111dbf9d4 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 212
8   QtCore                        	       0x111dea316 QObjectPrivate::setParent_helper(QObject*) + 374
9   QtCore                        	       0x111de9ebd QObject::~QObject() + 2125
10  libPythonQt.dylib             	       0x11620fab4 PythonQtSignalReceiver::~PythonQtSignalReceiver() + 212
11  libPythonQt.dylib             	       0x11620fc1e PythonQtSignalReceiver::~PythonQtSignalReceiver() + 14
12  libPythonQt.dylib             	       0x1161a78ee PythonQt::removeSignalHandlers() + 190
13  libPythonQt.dylib             	       0x1161a7805 PythonQt::cleanup() + 21
14  libCTKScriptingPythonCore.0.1.dylib	       0x10d6a612b ctkAbstractPythonManager::~ctkAbstractPythonManager() + 43
15  libqSlicerBaseQTGUI.dylib     	       0x10dbbdc7e qSlicerPythonManager::~qSlicerPythonManager() + 14
16  libqSlicerBaseQTCore.dylib    	       0x10eaec9bd qSlicerCoreApplicationPrivate::~qSlicerCoreApplicationPrivate() + 173
17  libqSlicerBaseQTGUI.dylib     	       0x10db21b1e qSlicerApplicationPrivate::~qSlicerApplicationPrivate() + 14
18  libqSlicerBaseQTCore.dylib    	       0x10eaf7ff6 qSlicerCoreApplication::~qSlicerCoreApplication() + 38
19  Slicer                        	       0x104cc4b0f main + 527
20  dyld                          	       0x204e5352e start + 462
</code></pre>

---

## Post #7 by @pieper (2022-08-04 14:52 UTC)

<p>I went ahead and <a href="https://github.com/pieper/SlicerParallelProcessing/commit/2cf7d7d61e7b17cc949cb8fd31acefe9e4de25a1">made the change I had in mind</a> and the crash on exit is now gone on my M2 mac.  <a class="mention" href="/u/wrc">@wrc</a> can you see if this makes a difference for your issue?</p>
<p>It’s funny that this only showed up (that we know) on macOS with Apple processors and Rosetta but I’d guess it reveals an inconsistency in the destructor cleanup when python classes inherit from Qt classes so we should be careful anywhere we use that pattern.</p>

---
