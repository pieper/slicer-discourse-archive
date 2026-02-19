---
topic_id: 278
title: "Error With New Extension Elastix"
date: 2017-05-06
url: https://discourse.slicer.org/t/278
---

# Error with new extension Elastix

**Topic ID**: 278
**Date**: 2017-05-06
**URL**: https://discourse.slicer.org/t/error-with-new-extension-elastix/278

---

## Post #1 by @KaiWei_Han (2017-05-06 16:08 UTC)

<p>Operating system:MacOS 10.12.4<br>
Slicer version:Slicer-4.7.0-2017-05-02-macosx-amd64<br>
Expected behavior:successful registration between two volume<br>
Actual behavior:“KeyError: ‘LD_LIBRARY_PATH’”<br>
Hey there, I am trying to register with this new extension Elastix. I have installed the extension and the Elastix toolbox from its official website. I can call elastix successfully in the terminal. However, when I am trying to register two volume, I have got this error:</p>
<blockquote>
<p>Volume registration is started in working directory: /var/folders/z8/4grvc78d4nn0d4nhy2l4869w0000gn/T/Slicer/Elastix/20170507_000009_410<br>
Register volumes…<br>
Register volumes using: /Applications/elastix_macosx64_v4.8/bin/elastix: [‘-f’, u’/var/folders/z8/4grvc78d4nn0d4nhy2l4869w0000gn/T/Slicer/Elastix/20170507_000009_410/input/fixed.mha’, ‘-m’, u’/var/folders/z8/4grvc78d4nn0d4nhy2l4869w0000gn/T/Slicer/Elastix/20170507_000009_410/input/moving.mha’, ‘-out’, u’/var/folders/z8/4grvc78d4nn0d4nhy2l4869w0000gn/T/Slicer/Elastix/20170507_000009_410/result-transform’, ‘-p’, ‘/Applications/Slicer.app/Contents/Extensions-25996/SlicerElastix/lib/Slicer-4.7/qt-scripted-modules/Resources/RegistrationParameters/Parameters_Rigid.txt’, ‘-p’, ‘/Applications/Slicer.app/Contents/Extensions-25996/SlicerElastix/lib/Slicer-4.7/qt-scripted-modules/Resources/RegistrationParameters/Parameters_BSpline.txt’]<br>
‘LD_LIBRARY_PATH’<br>
<strong>Traceback (most recent call last):</strong><br>
File “/Applications/Slicer.app/Contents/Extensions-25996/SlicerElastix/lib/Slicer-4.7/qt-scripted-modules/Elastix.py”, line 327, in onApplyButton<br>
movingVolumeMaskNode = self.movingVolumeMaskSelector.currentNode())<br>
File “/Applications/Slicer.app/Contents/Extensions-25996/SlicerElastix/lib/Slicer-4.7/qt-scripted-modules/Elastix.py”, line 556, in registerVolumes<br>
ep = self.startElastix(inputParamsElastix)<br>
File “/Applications/Slicer.app/Contents/Extensions-25996/SlicerElastix/lib/Slicer-4.7/qt-scripted-modules/Elastix.py”, line 466, in startElastix<br>
return subprocess.Popen([executableFilePath] + cmdLineArguments, env=self.getElastixEnv(),<br>
File “/Applications/Slicer.app/Contents/Extensions-25996/SlicerElastix/lib/Slicer-4.7/qt-scripted-modules/Elastix.py”, line 433, in getElastixEnv<br>
elastixEnv[“LD_LIBRARY_PATH”] = elastixLibDir + os.pathsep + elastixEnv[“LD_LIBRARY_PATH”]<br>
<strong>KeyError: ‘LD_LIBRARY_PATH’</strong></p>
</blockquote>
<p>I could not figure this problem out, Any help will be appreciated.<br>
Sincerely<br>
Kaiwei Han M.D.<br>
Department of Neurosurgery, Changzheng Hospital, Shanghai, China.</p>

---

## Post #2 by @lassoan (2017-05-06 19:00 UTC)

<p>I’ve made the path setup more robust, which hopefully will fix the problem.</p>
<p>To try the fix right now, update “/Applications/Slicer.app/Contents/Extensions-25996/SlicerElastix/lib/Slicer-4.7/qt-scripted-modules/Elastix.py” file on your computer: change <code>elastixEnv["LD_LIBRARY_PATH"]...</code> line to the one shown here: <a href="https://github.com/lassoan/SlicerElastix/blob/master/Elastix/Elastix.py#L433">https://github.com/lassoan/SlicerElastix/blob/master/Elastix/Elastix.py#L433</a></p>
<p>Or, use Slicer’s nightly version that you download tomorrow or later.</p>

---

## Post #3 by @KaiWei_Han (2017-05-08 15:17 UTC)

<p>to Andras Lasso，thank you very much，problem solved.</p>

---
