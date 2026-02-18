# How to use TotalSegmentator from Script with "--no-main-window" option

**Topic ID**: 28144
**Date**: 2023-03-02
**URL**: https://discourse.slicer.org/t/how-to-use-totalsegmentator-from-script-with-no-main-window-option/28144

---

## Post #1 by @Sergio (2023-03-02 17:03 UTC)

<p>Hi everyone,</p>
<p>I am new 3DSlicer user. I was able to develop my own script which can use TotalSegmentator automatically. But I would like to run it without graphical interface.</p>
<p>The script is working well with graphical interface, but when I use the command “–no-splash --no-main-window”, the program returns me an error because it requires the main-window.</p>
<p>This is the error:</p>
<blockquote>
<p><em>Traceback (most recent call last):</em></p>
<ul>
<li>File “”, line 5, in *</li>
<li>File “”, line 26, in *</li>
<li>File “/usr/local/apps/3DSlicer/5.2.1/bin/Python/slicer/util.py”, line 1156, in selectModule*</li>
<li>selector = moduleSelector()*</li>
<li>File “/usr/local/apps/3DSlicer/5.2.1/bin/Python/slicer/util.py”, line 1141, in moduleSelector*</li>
<li>raise RuntimeError(“Could not find main window”)*<br>
<em>RuntimeError: Could not find main window</em></li>
</ul>
</blockquote>
<p>Could I have any help with this? It is possible to run the module without the main-window?</p>
<p>Thanks in advance,<br>
-Sergio</p>

---

## Post #2 by @pieper (2023-03-02 18:06 UTC)

<p>If you want to run headless, you can just use the original tool.  <a href="https://github.com/wasserth/TotalSegmentator" class="inline-onebox">GitHub - wasserth/TotalSegmentator: Tool for robust segmentation of 104 important anatomical structures in CT images</a></p>

---

## Post #3 by @rbumm (2023-03-02 18:07 UTC)

<p>In that case, you would probably want to install TotalSegmentator in a separate Python instance on your machine <a href="https://github.com/wasserth/TotalSegmentator#installation">as described here</a> and run your script independently.</p>
<p>But you could also write a script that calls the logic of the TotalSegmentator extension in 3D Slicer which will in turn, perform a TotalSegmentator run.</p>

---

## Post #4 by @Sergio (2023-03-02 18:26 UTC)

<p>Thank you very much for your quick response.</p>
<p>Yes, I considered also that way. However, I am using the “DicomRtImportExportPlugin” at the end of the segmentation to export the results to DICOM files (Images and RTstructures).</p>
<p>So, what I did is to create an script that is working well when I call it using the following command:</p>
<blockquote>
<p>Slicer --python-script “/full/path/to/myscript.py” --no-splash</p>
</blockquote>
<p>But it is not working when I use the next one:</p>
<blockquote>
<p>Slicer --python-script “/full/path/to/myscript.py” --no-splash --no-main-window</p>
</blockquote>
<p>Because it seems that TotalSegmentator module requires “main-window”.</p>
<p>Is it possible to run this without main-window?</p>
<p>Thanks,<br>
-Sergio</p>

---

## Post #5 by @pieper (2023-03-02 21:49 UTC)

<p>This thread should help:</p>
<aside class="quote" data-post="1" data-topic="28118">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/c2a13f/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/python-script-crashes-when-running-w-o-gui-due-to-smoothing-effect/28118">Python script crashes when running w/o GUI due to smoothing effect</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I try to run a python script via the command ./Slicer --no-splash --no-main-window --python-script ‘customScript.py’. 
It crashes when executing the following line: segmentEditorWidget.setActiveEffectByName("Smoothing"), however, it works when I remove the flag --no-main-window and also when the same code is run via a Jupyter Notebook. 
Is there any way to apply smoothing effect w/o a GUI? 
Slicer version: 5.2.2 
Thanks!
  </blockquote>
</aside>


---

## Post #6 by @Xiaojie_Guo (2024-04-24 02:22 UTC)

<p>Hi, sir, could you give an example of a script that calls the logic of TotalSegmentator extension?</p>

---

## Post #7 by @Xiaojie_Guo (2024-04-24 05:44 UTC)

<p>I know how to do it. I forgot to import it.</p>

---
