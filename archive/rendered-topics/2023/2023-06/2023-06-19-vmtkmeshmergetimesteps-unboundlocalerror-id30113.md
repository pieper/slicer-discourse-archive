---
topic_id: 30113
title: "Vmtkmeshmergetimesteps Unboundlocalerror"
date: 2023-06-19
url: https://discourse.slicer.org/t/30113
---

# vmtkmeshmergetimesteps UnboundLocalError

**Topic ID**: 30113
**Date**: 2023-06-19
**URL**: https://discourse.slicer.org/t/vmtkmeshmergetimesteps-unboundlocalerror/30113

---

## Post #1 by @Krentos_Iliakopoulos (2023-06-19 03:02 UTC)

<p>Hi,</p>
<p>I try to trace particles using the  tutorial <a href="http://www.vmtk.org/tutorials/ParticleTracing.html" class="inline-onebox" rel="noopener nofollow ugc">Particle Tracing | vmtk - the Vascular Modelling Toolkit</a> . Following the steps one by one, when i tried to execute vmtkmeshmergetimesteps like:</p>
<p>vmtkmeshmergetimesteps -directory ~C:/Users/Desktop/thesis/thesis1/kalokalo/Simulations/kalokalo/5/kalokalo-converted-results<br>
-firststep 0 -laststep 2800 -intervalstep 10 -velocityvector 1 -vector velocity<br>
-pattern all_results_%5s.vtu -ofile total_results.vtu</p>
<p>i get the error message :</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\DELL\anaconda3\envs\foo\lib\site-packages\vmtk\pypeserver.py”, line 46, in RunPypeProcess<br>
pipe.Execute()<br>
File “C:\Users\DELL\anaconda3\envs\foo\lib\site-packages\vmtk\pype.py”, line 324, in Execute<br>
scriptObject.Execute()<br>
File “C:\Users\DELL\anaconda3\envs\foo\lib\site-packages\vmtk\vmtkmeshmergetimesteps.py”, line 116, in Execute<br>
if (self.Pattern%step).replace(’ ',‘0’) in fileList:<br>
UnboundLocalError: local variable ‘fileList’ referenced before assignment</p>
<p>The pattern of the files is all_results_01234.vtu.<br>
Any help regarding the UnboundLocalError would be much appreciated!</p>
<p>Kind Regards,<br>
Krentos</p>

---

## Post #2 by @lassoan (2023-06-20 19:00 UTC)

<p>It <a href="https://github.com/vmtk/vmtk/blob/e9ebb8c420d7e2aba7a7e68c11355794e63f3716/vmtkScripts/vmtkmeshmergetimesteps.py#LL90C47-L90C65">looks like <code>InputDirectoryName</code> was not set correctly</a>, for example you have set invalid path or there were no files in the directory.</p>
<p>It would be nice if you update the script to show a more detailed error message (e.g., input folder does not exist; no files were found in folder…) and send a pull request.</p>

---
