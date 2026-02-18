# Call script in conda

**Topic ID**: 16473
**Date**: 2021-03-10
**URL**: https://discourse.slicer.org/t/call-script-in-conda/16473

---

## Post #1 by @szhang (2021-03-10 16:58 UTC)

<p>How can I call the script correctly? Here’s how my Miniconda3 window looks like</p>
<blockquote>
<p>(base) PS C:&gt; conda activate foo<br>
(foo) PS C:&gt; vmtkimagereader<br>
vmtkimagereader : The term ‘vmtkimagereader’ is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.</p>
</blockquote>

---

## Post #2 by @mjg (2021-03-16 03:03 UTC)

<p>I use pypes. <a href="http://www.vmtk.org/tutorials/PypesProgrammatically.html" rel="noopener nofollow ugc">Pypes Documentation Link</a></p>
<p>Example (paths are strings):</p>
<pre><code>from vmtk import pypes

vmtkCommand = r'vmtkcenterlines -ifile ' + modelPath + r' -ofile ' + centerlinePath
myPype = pypes.PypeRun(vmtkCommand)</code></pre>

---

## Post #3 by @szhang (2021-04-12 21:50 UTC)

<p>Thank you, mjg.<br>
Regarding my original question, I later realized it needs to be typing command in VMTK interface rather than in a shell command window.</p>

---
