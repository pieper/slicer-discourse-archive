# Working directory of Slicer

**Topic ID**: 6248
**Date**: 2019-03-22
**URL**: https://discourse.slicer.org/t/working-directory-of-slicer/6248

---

## Post #1 by @Alex1 (2019-03-22 13:57 UTC)

<p>Hi, I always have the problem with the working directory of Slicer.<br>
when I use</p>
<blockquote>
<p>nrrd.write(filename,data)</p>
</blockquote>
<p>I have no idea where my filename.nrrd is stored.<br>
And everytime I try to load a model or file to Slicer,  the relative path(./directory) won’t work. So I have to use the full path. Is there a solution to this problem?</p>

---

## Post #2 by @lassoan (2019-03-22 13:58 UTC)

<p>Non-console applications often do not have the notion of a “working directory”. You need to use absolute paths.</p>
<p>You can construct absolute paths from various directories, for example:</p>
<ul>
<li>
<code>slicer.mrmlScene.GetRootDirectory()</code>: all nodes are saved relative to this path</li>
<li>
<code>slicer.app.temporaryPath</code>: write-able folder, you can use this to store any temporary data</li>
<li>
<code>slicer.app.slicerHome</code>: Slicer core binary folder</li>
<li>
<code>slicer.app.extensionsInstallPath</code>: Slicer extensions folder</li>
<li>
<code>slicer.modules.sampledata.path</code>: path of a scripted module (in this example: Sample Data module)</li>
</ul>
<p>You can also pass any folder name to Slicer via the command-line. For example:</p>
<p><code>"c:\Program Files\Slicer 4.10.1\Slicer.exe" --python-code "myDataDir='%cd%';loadVolume(myDataDir+'vol.nrd'); (do some processing here...); saveNode(someNode,myDataDir+'processed.nrrd')"</code></p>

---

## Post #3 by @Alex1 (2019-03-22 15:21 UTC)

<p>Hi, thanks for the answer. This is a very clear explanation.  But I still have some problem here.<br>
In my scripted module, I got an array and I want to save it as a .nrrd file.  I used nrrd.write but I still can’t find my file. I tried to look it up in slicer.modules.sampledata.path, but it’s not there. Where is it or how can I load this file to Slicer?</p>
<p>Thanks for your time.</p>

---

## Post #4 by @lassoan (2019-03-22 15:27 UTC)

<p>If you have a numpy array and you want to show it as an image in Slicer then you don’t need to write it to file. You can directly write it to a volume node using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.updateVolumeFromArray" rel="nofollow noopener">slicer.util.updateVolumeFromArray</a>.</p>
<p>if you want to write a temporary file, you can use <code>slicer.app.temporaryPath</code>, for example:</p>
<pre><code>slicer.util.saveNode(someVolumeNode, slicer.app.temporaryPath+'/tempABC.nrrd')</code></pre>

---

## Post #5 by @Alex1 (2019-03-22 16:00 UTC)

<p>Hi,  Thanks for your help. This is an awesome solution.</p>

---
