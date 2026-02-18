# How to Add a Python Script for Brain Extraction in a Custom 3D Slicer Template

**Topic ID**: 42158
**Date**: 2025-03-15
**URL**: https://discourse.slicer.org/t/how-to-add-a-python-script-for-brain-extraction-in-a-custom-3d-slicer-template/42158

---

## Post #1 by @software (2025-03-15 17:19 UTC)

<p>Hello everyone,</p>
<p>I want to integrate a Python script for brain extraction into a custom 3D Slicer template created using Kitware’s SlicerCAT framework. My goal is to add my own scripted module and make it functional within the custom application.</p>
<p>Could anyone guide me on how to:</p>
<ol>
<li>Properly add a Python-scripted module to the custom template?</li>
<li>Ensure the script runs correctly within 3D Slicer?</li>
<li>Build and test the changes effectively?</li>
</ol>
<p>Additionally, I have two solution (<code>.sln</code>) files:</p>
<ul>
<li><code>build/safe.sln</code></li>
<li><code>build/slicer_build/slicer.sln</code></li>
</ul>
<p>Which one should I open in Visual Studio to see my changes and work on the project?</p>
<p>Any help, guidance, or references would be greatly appreciated. Thanks in advance!</p>

---

## Post #2 by @tas47 (2025-03-18 07:26 UTC)

<p>Hey,</p>
<p>I’m still learning about creating modules, but I found a YouTube playlist that clarified many concepts and provides a great starting point. It covers topics like module templates and setting up/debugging with IDE:</p>
<p><a href="https://www.youtube.com/playlist?list=PLTuWbByD80TORd1R-J7j7nVQ9fot3C2fK" rel="noopener nofollow ugc">YouTube Playlist</a><br>
Start with <a class="hashtag-cooked" href="/tag/tutorial" data-type="tag" data-slug="tutorial" data-id="51"><span class="hashtag-icon-placeholder"><svg class="fa d-icon d-icon-square-full svg-icon svg-node"><use href="#square-full"></use></svg></span><span>tutorial</span></a> 1</p>
<p>I recommend downloading the Python debugger extension first and then following along with the playlist. I also use vscode so i would recommend following the python debugger documentation instead because the vids uses pycharm.</p>
<p>From what I understand, a module generally consists of three parts:</p>
<ul>
<li><strong>GUI Component:</strong> The user interface.</li>
<li><strong>Logic Component:</strong> Where your main script or functionality resides.</li>
<li><strong>Test Component:</strong> For testing your module.</li>
</ul>
<p>When you create the template using the extension wizard, it generates all the necessary template files and set up, allowing you to integrate your module directly into Slicer.</p>
<p>Hope this helps!<br>
tas</p>

---
