# Problem running slicer in Batch mode

**Topic ID**: 1161
**Date**: 2017-10-03
**URL**: https://discourse.slicer.org/t/problem-running-slicer-in-batch-mode/1161

---

## Post #1 by @Suman_Regmi (2017-10-03 00:02 UTC)

<p>I am trying to batch a number of operations in Slicer 3D to test my hypothesis however I ran into this strange problem of even making through example. Is there any pre-requisite in order to make this example script work?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_run_slicer_operations_from_a_batch_script.3F" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_run_slicer_operations_from_a_batch_script.3F</a></p>

---

## Post #2 by @lassoan (2017-10-03 00:05 UTC)

<p>What did you do exactly (what script you tried to run, what version of Slicer, what operating system, …)?<br>
What did you expect to happen?<br>
What happened instead? What was printed on the console? What was logged in the Slicer application log?</p>

---

## Post #3 by @moselhy (2017-10-04 17:56 UTC)

<p>I think that the new version of Slicer does not produce any output in the command line. For example, try running (I am using Windows) Slicer.exe --help. You won’t get any output…</p>

---

## Post #4 by @lassoan (2017-10-04 18:29 UTC)

<p>On Windows, we decided to disable the console, because showing a console window is not common for Windows applications. Instead you can find all messages in the application log (menu: Help / Report a bug; or menu: View / Error log).</p>

---

## Post #5 by @moselhy (2017-10-04 18:31 UTC)

<p>But I think when it is run from the command line, there should be some output, or at least the --help flag should output some useful flags to use Slicer.exe from the command line</p>

---

## Post #6 by @lassoan (2017-10-04 18:36 UTC)

<p>I agree. This is a known issue (<a href="https://issues.slicer.org/view.php?id=2934">https://issues.slicer.org/view.php?id=2934</a>), but there have been always more important developments or fixes to do. If you add a comment to this issue explaining why it is important for you then it will more likely to get on the radar of a developer.</p>

---
