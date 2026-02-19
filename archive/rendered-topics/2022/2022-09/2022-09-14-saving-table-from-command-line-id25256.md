---
topic_id: 25256
title: "Saving Table From Command Line"
date: 2022-09-14
url: https://discourse.slicer.org/t/25256
---

# Saving table from command line

**Topic ID**: 25256
**Date**: 2022-09-14
**URL**: https://discourse.slicer.org/t/saving-table-from-command-line/25256

---

## Post #1 by @lukasvanderstricht (2022-09-14 10:13 UTC)

<p>Hi everyone,</p>
<p>I have made a lung segmentation on an MRI and used the <code>Segment Statistics</code> module to create a table with measurements about the segmentations (such as the volume of the segments). I know how to save this table as a <code>.csv</code> file by going to <code>Save</code> at the top of the Slicer window.</p>
<p>However, I would want to automate certain of the processes I go through, such as the saving of this table. I wondered if there was anything I could do from command line or with  I have found some existing blogposts about how to do this, for example this one: <a href="https://discourse.slicer.org/t/how-to-programmatically-export-data-from-segment-statistics/17390">How to programmatically export data from segment statistics?</a>.</p>
<p>I could however not work out how to do this. I don’t know where I have to run this command. I am working in Windows and I tried running it in a cmd terminal, but to no avail. I explored my filesystem a bit and found some directories that according to me allude to the path that is used in the command in the blogpost. I can navigate to <code>AppData/Local/NA-MIC/Slicer 5.0.3/bin/Python/slicer</code> and this directory indeed contains the file <code>util.py</code>.</p>
<p>I do not know however how to go about saving the table now? What terminal should I run the command in?</p>
<p>Thank you a lot in advance!</p>
<p>Kind regards</p>
<p>Lukas</p>

---

## Post #2 by @jamesobutler (2022-09-14 11:31 UTC)

<p>You should run that python code using the Python Interactor in the 3D Slicer application. You can toggle it to show/hide by a python button in the toolbar area, View-&gt;Python Interactor, or by keyboard shortcuts Ctrl+3/Ctrl+`</p>

---

## Post #4 by @jamesobutler (2022-09-14 14:09 UTC)

<aside class="quote no-group quote-post-not-found" data-username="lukasvanderstricht" data-post="3" data-topic="25256">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/7ba0ec/48.png" class="avatar"> lukasvanderstricht:</div>
<blockquote>
<pre><code class="lang-auto">tablenode = getNode('T')
slicer.util.getNode(tablenode,"test.csv")
</code></pre>
</blockquote>
</aside>
<p>Make sure to use <code>saveNode</code> to save the file. In your code above you used <code>getNode</code>. Also if you just specify the filename and not the full absolute path it will attempt to save in some last known position or working directly I believe. To be more explicit to where you save, specify the full path. It would be as follows.</p>
<pre data-code-wrap="python"><code class="lang-python">tablenode = getNode('T')
slicer.util.saveNode(tablenode, "C:/Users/James/Downloads/Table.csv")
</code></pre>

---

## Post #5 by @lukasvanderstricht (2022-09-14 14:47 UTC)

<p>Yes, sorry that was a typo of mine. I indeed found the files I was looking for now.<br>
I was wondering if I could accomplish the same result by using an external python file. I made such a file with only the following contents:</p>
<pre><code class="lang-auto">def saveTable():
	tablenode = slicer.util.getNode('T')
	slicer.util.saveNode(tablenode,"grap.csv")
</code></pre>
<p>I loaded this python file into Slicer’s Python environment with <code>sys.path.append(filepath)</code> and then <code>import</code>. This all seems to work without problems. If I now want to execute the function above (with the command <code>file.saveTable()</code>), I get the following error:</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\lukas\OneDrive\Documenten\saveAsGrap.py”, line 2, in saveTable<br>
tablenode = slicer.util.getNode(‘T’)<br>
NameError: name ‘getNode’ is not defined</p>
</blockquote>
<p>Is there any way around this?</p>
<p>Thank you in advance!</p>

---

## Post #6 by @pieper (2022-09-14 14:54 UTC)

<p>See the notes linked below.  <code>slicer.util</code> is imported to the interactive console as a convenience.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-mrml-node-from-the-scene" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-mrml-node-from-the-scene</a></p>

---

## Post #7 by @lukasvanderstricht (2022-09-14 15:00 UTC)

<p>Hi, thank you for your response!</p>
<p>However, I don’t see how this can help me to solve my issue.<br>
Sorry for the inconvienence, I’m a beginner at Slicer.</p>
<p>Thank you!</p>

---

## Post #8 by @lukasvanderstricht (2022-09-14 15:02 UTC)

<p>If I remove the <code>slicer.util</code>-part in front of <code>getNode</code>, I still have the same issue.</p>

---

## Post #9 by @pieper (2022-09-14 15:10 UTC)

<p>Try running using this form instead:</p>
<p><code>exec(open(f"{path_to_script}").read())</code></p>

---

## Post #10 by @lukasvanderstricht (2022-09-14 15:15 UTC)

<p>Hi, thank you for your answer!</p>
<p>This indeed seems to work.</p>
<p>Thank you very much!</p>

---
