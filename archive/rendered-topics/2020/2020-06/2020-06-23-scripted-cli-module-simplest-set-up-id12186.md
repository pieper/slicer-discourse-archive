# Scripted CLI Module simplest set-up

**Topic ID**: 12186
**Date**: 2020-06-23
**URL**: https://discourse.slicer.org/t/scripted-cli-module-simplest-set-up/12186

---

## Post #1 by @Queen_Rei (2020-06-23 21:34 UTC)

<p>Hi there, I have a python script that converts a directory of .dcm’s into a .obj.<br>
In its simplest form the script looks like this:</p>
<pre><code>inputFilePath = "My Input File Path"
(Create .obj from .dcm directory)
outputFilePath = "My Output File Path"
</code></pre>
<p>I was thinking of having the input and output file paths be parameters for a subprocess, so the module can be run multiple times for multiple folder directories of .dcm’s. I am currently running off of the template Andros provided to get a decent understanding. I’ve been looking through other posts, script repos, and the nightly documentation, but I don’t seem to have the clearest view of what I would need to do so I have some questions.</p>
<ol>
<li>Is a .xml file required? I wouldn’t need a GUI for what I want to do. If it is required, then I can just do the basic requirements on the nightly docs, so it still executes?</li>
<li>Would making it run in the command line look like so:<br>
[I’m on Windows and would also like to know for Linux]<br>
python DICOM2OBJ.py inputPath outputPath<br>
OR<br>
“slicer path” --python-code “DICOM2OBJ(inputPath, outputPath”)</li>
<li>Considering Slicer is open already, would I need to run another line before the module execution or would the one line be enough?</li>
</ol>
<p>Happy to clarify anything that needs it~ I am learning about scripted modules only recently, so I want to make sure I get the most updated information. Thank you and stay safe &lt;3</p>

---

## Post #2 by @Queen_Rei (2020-06-24 13:58 UTC)

<p>I am still stuck on these questions. Any helps goes a long way &lt;3</p>

---

## Post #3 by @pieper (2020-06-24 14:21 UTC)

<p>The command line example in the post below should give you an idea.  Yes, you can run it as a subprocess launched from Slicer.  HTH.</p>
<aside class="quote quote-modified" data-post="2" data-topic="3421">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-can-i-convert-dicom-series-to-nrrd-files-in-batch-mode/3421/2">How can I convert DICOM series to NRRD files in batch mode?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Here is how you can do the conversion in batch mode. 
First, install mpReview extension. This will add two new modules: mpReview and mpReviewPreprocessor. 
mpReviewPreprocessor can be used to volume-reconstruct any collection of DICOM files in batch mode using Slicer DICOM plugins. It can be accessed from the Slicer GUI, but you can also run the script as from the command line follows (you will need to update the path to the preprocessor to the on your system after installing the script, or you …
  </blockquote>
</aside>


---

## Post #4 by @BigBrotherHui (2021-12-24 08:12 UTC)

<p>could you please help me sovle a problem about the bug:“AttributeError: module ‘slicer’ has no attribute ‘dicomDatabaseDirectorySettingsKey’”? i’m not understand the reply they told you in the past post</p>

---

## Post #5 by @BigBrotherHui (2021-12-24 08:14 UTC)

<aside class="quote no-group" data-username="Queen_Rei" data-post="2" data-topic="12186">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/queen_rei/48/6348_2.png" class="avatar"> Queen_Rei:</div>
<blockquote>
<p>Any helps goes a long way &lt;3</p>
</blockquote>
</aside>
<p>any helps goes a long way for me too</p>

---

## Post #6 by @lassoan (2021-12-28 16:45 UTC)

<p>Do you need a GUI for your module or you just want to run a Python script in Slicer?</p>

---
