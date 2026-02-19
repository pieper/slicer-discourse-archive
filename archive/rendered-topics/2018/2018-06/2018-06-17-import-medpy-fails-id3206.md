---
topic_id: 3206
title: "Import Medpy Fails"
date: 2018-06-17
url: https://discourse.slicer.org/t/3206
---

# Import medpy fails

**Topic ID**: 3206
**Date**: 2018-06-17
**URL**: https://discourse.slicer.org/t/import-medpy-fails/3206

---

## Post #1 by @virginia_fgc (2018-06-17 08:34 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.8.0</p>
<p>Hello everyone,</p>
<p>I am using the Python Console in Slicer to work with a MR image, and I am facing problems when importing some modules. I wanted to use cv2 and medpy. I managed to find a workaround for which I did not need cv2, but I need to use medpy and I am getting stuck with its import.</p>
<p>I ran the following commands:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import pip<br>
pip.main([‘install’, ‘medpy’])</p>
</blockquote>
</blockquote>
</blockquote>
<p><strong>The errors in the output were:</strong><br>
Failed building wheel for medpy<br>
Failed cleaning build dir for medpy<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.8.0\lib\Python\Lib\site-packages\pip\basecommand.py”, line 215, in main<br>
status = self.run(options, args)<br>
File “C:\Program Files\Slicer 4.8.0\lib\Python\Lib\site-packages\pip\commands\install.py”, line 342, in run<br>
prefix=options.prefix_path,<br>
File “C:\Program Files\Slicer 4.8.0\lib\Python\Lib\site-packages\pip\req\req_set.py”, line 784, in install<br>
**kwargs<br>
File “C:\Program Files\Slicer 4.8.0\lib\Python\Lib\site-packages\pip\req\req_install.py”, line 851, in install<br>
self.move_wheel_files(self.source_dir, root=root, prefix=prefix)<br>
File “C:\Program Files\Slicer 4.8.0\lib\Python\Lib\site-packages\pip\req\req_install.py”, line 1064, in move_wheel_files<br>
isolated=self.isolated,<br>
File “C:\Program Files\Slicer 4.8.0\lib\Python\Lib\site-packages\pip\wheel.py”, line 345, in move_wheel_files<br>
clobber(source, lib_dir, True)<br>
File “C:\Program Files\Slicer 4.8.0\lib\Python\Lib\site-packages\pip\wheel.py”, line 316, in clobber<br>
ensure_dir(destdir)<br>
File “C:\Program Files\Slicer 4.8.0\lib\Python\Lib\site-packages\pip\utils_<em>init</em>_.py”, line 83, in ensure_dir<br>
os.makedirs(path)<br>
File “C:/Program Files/Slicer 4.8.0/lib/Python/Lib\os.py”, line 157, in makedirs<br>
mkdir(name, mode)<br>
WindowsError: [Error 5] Access denied: ‘C:\Program Files\Slicer 4.8.0\lib\Python\Lib\site-packages\scipy’<br>
You are using pip version 9.0.1, however version 10.0.1 is available.<br>
You should consider upgrading via the ‘python -m pip install --upgrade pip’ command.</p>
<p>Now, the upgrade command does not work. I tried to use CMD directly, but the system keeps triggering Syntax Errors and ‘File not found’ errors. Strangely, the default 2.7 Python version of mi computer does not have pip installed; thus, I can’t use pip to install any module. “Import pip” does work with Slicer though. However, it doesn’t seem to be working either due to the errors I mention above.</p>
<p>Questions:</p>
<ol>
<li>Do I have to consider the Python 2.7 version in Slicer and the Python 2.7 version in my computer as different things? Can’t I attempt the installation of a module for the Python console in slicer in CMD, with permits?</li>
<li>How do I run command “python -m pip install --upgrade pip”? In the Slicer console it clearly does not work. In Windows console, neither (because it tells me “pip” does not exist and so on).</li>
</ol>
<p>Thank you for any clarification.</p>
<p>Virginia</p>

---

## Post #2 by @jcfr (2018-06-17 20:03 UTC)

<p>Hi <a class="mention" href="/u/virginia_fgc">@virginia_fgc</a> ,</p>
<p>Following <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27258">r27258</a>, the version of pip bundled in Slicer has been updated to <code>10.0.1</code>. This means that the nightly build of tomorrow will include an updated pip version. See <a href="https://download.slicer.org/">https://download.slicer.org/</a></p>
<blockquote>
<p><code>WindowsError: [Error 5] Access denied: ‘C:\Program Files\Slicer 4.8.0\lib\Python\Lib\site-packages\</code></p>
</blockquote>
<p>Since Slicer is installed in <code>C:\Program Files</code>, you may have to run the command from a windows terminal started with administrator rights.</p>
<blockquote>
<p>I need to use medpy</p>
</blockquote>
<p>If you describe the processing you would like to achieve, we may be able to describe an approach using filters readily available in Slicer.</p>

---

## Post #3 by @lassoan (2018-06-18 14:21 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="3206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>If you describe the processing you would like to achieve, we may be able to describe an approach using filters readily available in Slicer.</p>
</blockquote>
</aside>
<p>I’ve been thinking about the same, too. This medpy package seems pretty basic (random wrapping of selected features from other toolkits) and there are several red flags (essentially a single contributor, overly generic package name - the developer thinks that a single package can cover this vast area; ignoring image axis orientation - an error that an experienced medical image computing software developer would never do; etc.). Overall, I would not recommend to rely on medpy package and instead use directly ITK (SimpleITK), VTK, numpy, etc. These toolkits are already bundled with Slicer and Slicer offers some additional features (for DICOM import, segmentation, quantification, etc.).</p>

---

## Post #4 by @virginia_fgc (2018-06-20 21:59 UTC)

<p>Dear Jean Cristophe, and Andras,</p>
<p>Thank you both for the updates. I am starting using Python and Slicer together, I am still struggling with issues like how after processing an image as an array, I can refresh the screen. I get from Andras’ reply that I can do it with ITK/VTK easily, just have to figure out how exactly. Problem is that I need to address many different issues and I am relying on discussions about similar problems where non-default modules are used.</p>
<p>I will try to go on with numpy and  ITK/VTK only, see if I can. I basically need to process a series of arrays that I need to read from a txt file and external images, and then change the color of some elements in the input volume based on the result of that image + array processing. For now, I’ve managed to go on without other modules. I’ve just found a discussion that might help me with the particular issue I’m having now: <a href="https://discourse.slicer.org/t/trying-to-update-a-slicer-volume-node-from-simpleitkimage/2032">Trying to update a slicer volume node from SimpleITKImage</a>.  Nonetheless, I’ll still implement the last nightly built version just in case I need to use pip in the future.</p>
<p>Thank you very much for the quick replies.</p>
<p>VIrginia</p>

---

## Post #5 by @lassoan (2018-06-21 00:12 UTC)

<p>OK. We will be happy to help, just post on the forum as new topics any specific questions that you cannot find answer for.</p>

---
