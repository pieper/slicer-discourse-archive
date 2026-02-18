# 3D Slicer Nighttime Queueing

**Topic ID**: 37455
**Date**: 2024-07-18
**URL**: https://discourse.slicer.org/t/3d-slicer-nighttime-queueing/37455

---

## Post #1 by @dstern1 (2024-07-18 16:50 UTC)

<p>Hello, I am a student intern working with Dr. Alkalay. We are working on a project using already segmented spines and analyzing them using the radiomics function. We are trying to code the software to be able to run these radiomics overnight.</p>
<p>Thank you,<br>
Doug Stern</p>

---

## Post #2 by @muratmaga (2024-07-18 17:41 UTC)

<p>You mean as in running Slicer at a specified time? There is no built-in feature for that, as that’s typically done using operating system tools (e.g., event scheduler in Windows, crontab in Linux/mac).</p>
<p>If you already created a python script that will run the tasks you want to accomplish, all you have to do is to specify the time using the tools I mentioned above, and then full path to your python script and with full path to Slicer executable, like this (in this case on Mac):</p>
<pre><code class="lang-auto">/Applications/Slicer.app/Contents/MacOS/Slicer --no-splash --no-main-window --python-script "/full/path/to/myscript.py"
</code></pre>
<p>You can find more informaiton in script repository.<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#run-a-python-script-file-in-the-slicer-environment" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#run-a-python-script-file-in-the-slicer-environment</a></p>

---

## Post #3 by @dstern1 (2024-07-18 18:12 UTC)

<p>Dear Murat,</p>
<p>I may have misrepresented the question. We have a number of spines that have been segmented. What we would like to do is to be able to run radiomics analysis on these spines out of work hours. So, what we are hoping to do is to be able to have a script that A) select the spine to be processed, B) for each spine select the segmentation file, and C) create the radiomics table as a result. With this regard how would we select the features within the radiomics analysis module. I hope this better explains  the ask.</p>
<p>Thank you</p>

---

## Post #4 by @muratmaga (2024-07-18 18:38 UTC)

<p>I am still a little fuzzy on the ask here (I know nothing about radiomics). Are you asking how to create this script?  Also what do you mean by ‘select spine to be processed’. Normally the script specifies what subjects to be processed.</p>
<p>Does this mean it will go to a database and look for new scans from that day and process them for radiomics?</p>
<p>if you clarify your ask, perhaps other can chime in.</p>

---
