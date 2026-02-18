# Running python file in Slicer on Mac 

**Topic ID**: 24356
**Date**: 2022-07-18
**URL**: https://discourse.slicer.org/t/running-python-file-in-slicer-on-mac/24356

---

## Post #1 by @ashuashu (2022-07-18 07:36 UTC)

<p>Can anyone help me with the commands here? I want to run a deep learning model in the 3D slicer. I have the file on my desktop. I tried to run it on a mac terminal as well as on 3D-Slicer. I am not able to proceed further. It is showing invalid syntax.</p>
<ul>
<li>Anyone please help me here with the commands.</li>
</ul>
<p>Thank you</p>

---

## Post #2 by @lassoan (2022-07-18 07:44 UTC)

<p>Deep learning works well on Windows and Linux and should work on some macOS systems, too. Please provide more information about your system (what CPU, GPU, and operating system do you use), what commands you execute and errors you get.</p>

---

## Post #3 by @ashuashu (2022-07-18 08:52 UTC)

<p>-Apple M1 chip<br>
-8-core CPU<br>
-8-core GPU</p>
<p>I am completely new to this software. Any references or any links related to this is very helpful for me.</p>
<p>The command I used was  from one of the discussions in this forum</p>
<p>/Applications/Slicer.app/Contents/MacOS/Slicer --no-splash --no-main-window  --python-script /Users/ashu/Desktop/test.py</p>

---

## Post #4 by @lassoan (2022-07-18 13:06 UTC)

<p>This looks good overall. What is in test.py? What error message do you get?</p>

---

## Post #5 by @ashuashu (2022-07-18 15:14 UTC)

<p>The file has a complete python code with nothing related to the slicer. My code does produce results when running on Google Colab. I want it to show output in 3d Slicer</p>
<p>qSlicerMarkupsModulePrivate::addToolBar: no main window is available, toolbar is not added<br>
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added<br>
Traceback (most recent call last):<br>
File “”, line 5, in &lt; module &gt;<br>
File “”, line 421, in &lt; module &gt;<br>
NameError: name ‘null’ is not defined</p>

---

## Post #6 by @Nathalie (2023-11-11 16:51 UTC)

<p>Hi all,<br>
Any solution for this issue? I am facing the same issue on my ubuntu environment.<br>
Thanks!</p>

---

## Post #7 by @pieper (2023-11-11 21:36 UTC)

<p>To better help, it wold be good if you could post a small example and describe how you are trying to run it.</p>

---

## Post #8 by @Nathalie (2023-11-12 16:10 UTC)

<p>Hi Steve,</p>
<p>This is what I run in the command line:</p>
<p>‘/home/dellxpsazdelta/Slicer-5.2.2-linux-amd64/Slicer’ --no-main-window --python-script /home/dellxpsazdelta/Documents/Lukas/automatisation/segmentationVolumes.py</p>
<p>and this is the output:</p>
<p>Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.<br>
qSlicerMarkupsModulePrivate::addToolBar: no main window is available, toolbar is not added<br>
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added<br>
Traceback (most recent call last):<br>
File “”, line 5, in <br>
File “”, line 6, in <br>
File “/home/dellxpsazdelta/Slicer-5.2.2-linux-amd64/bin/Python/slicer/util.py”, line 1145, in moduleSelector<br>
raise RuntimeError(“Could not find main window”)<br>
RuntimeError: Could not find main window</p>
<p>To summarize: I am trying to run the segmentationVolumes.py python script in Slicer without using the GUI. When I execute the script in the 3D Slicer application, I runs without any error.</p>
<p>Thanks for the help.</p>

---

## Post #9 by @pieper (2023-11-12 18:22 UTC)

<p>Ah, okay, you should upgrade to Slicer 5.4.0.  There’s now just a warning.</p>

---

## Post #10 by @Nathalie (2023-11-13 08:30 UTC)

<p>I updated slicer to 5.4.0 but I still have the same issue:</p>
<p>Input: ‘/home/dellxpsazdelta/Slicer-5.4.0-linux-amd64/Slicer’ --no-main-window --python-script /home/dellxpsazdelta/Documents/Lukas/automatisation/segmentationVolumes.py</p>
<p>Output: Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.<br>
qSlicerMarkupsModulePrivate::addToolBar: no main window is available, toolbar is not added<br>
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added<br>
Traceback (most recent call last):<br>
File “”, line 5, in <br>
File “”, line 6, in <br>
File “/home/dellxpsazdelta/Slicer-5.4.0-linux-amd64/bin/Python/slicer/util.py”, line 1163, in moduleSelector<br>
raise RuntimeError(“Could not find main window”)<br>
RuntimeError: Could not find main window</p>
<p>Please not that in the beginning of the output, I indeed receive a warning, but however at the end, I do receive a runtimeError.</p>
<p>Any other solution as updating Slicer did not resolve the issue? Thanks!</p>

---

## Post #11 by @pieper (2023-11-13 15:08 UTC)

<p>Please post the contents of the segmentationVolumes.py script, or better, just enough of it to reproduce the RuntimeError.</p>

---

## Post #12 by @pieper (2023-11-13 19:34 UTC)

<p>I see, you are calling <code>selectModule</code> but you pass the <code>--no-main-window</code> flag which doesn’t work because modules require a user interface in order to be selected (selecting builds their Qt interface).</p>
<p>Since you are using the <code>MONAILabel</code> extension you’ll need to look into the code to see how to use it with no GUI.  Slicer modules should always expose a <code>Logic</code> class that implements the non-GUI aspects of the code for exactly this use case, but sometimes modules aren’t written that way, at least at first, because developers don’t have this use case in mind.  You can read through the MONAILabel code to see how to accomplish what you are doing using just the logic class.  I haven’t looked, but this might require some changes to the module or duplicating some code in your script if you just want a workaround.</p>

---
