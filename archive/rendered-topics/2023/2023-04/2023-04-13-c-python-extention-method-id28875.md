# C++ & python extention method

**Topic ID**: 28875
**Date**: 2023-04-13
**URL**: https://discourse.slicer.org/t/c-python-extention-method/28875

---

## Post #1 by @dsa934 (2023-04-13 02:39 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>Hi, slicer users !<br>
I’ve asked a similar question before, but I don’t quite understand it.<br>
(<a href="https://discourse.slicer.org/t/can-i-create-c-extensions-via-dlls/28393/2" class="inline-onebox">Can I create c++ extensions via DLLs? - #2 by RafaelPalomar</a>)<br>
To be honest, I don’t quite understand, so I’m looking for help again.</p>
<ul>
<li>
<p>What i want<br>
I want to perform a specific inference process through my AI model with the mesh data loaded into the slicer. I’m trying to get this behavior to work within slicer.</p>
</li>
<li>
<p>Challenge</p>
</li>
</ul>
<ol>
<li>
<p>The AI inference process is implemented in Python, but the code to generate the input datasets used by this model consists of C++.</p>
</li>
<li>
<p>The process I was thinking of was as follows.</p>
<p>load mesh data in slicer → make appropriate input dataset (via c++) → Ai inference (via python)</p>
</li>
</ol>
<ul>
<li>Want to know<br>
The above work is being done through the VS community, and I wonder if this process is possible in Slicer as well.</li>
</ul>
<p>====================================<br>
The previous question told me to use the CLI and lodable module, but I’m not sure how to apply this to my task.</p>
<p>I know roughly how to extend a module composed of python, so can you elaborate a bit on how to make a module composed of c++ work in slicer?</p>
<p>The original purpose was to modularize the dataset generation code and inference code at once, but I don’t understand how to modularize c++ and python at the same time. Can you show me just one example case?</p>

---

## Post #2 by @pieper (2023-04-13 13:43 UTC)

<p>Referring to the previous thread, several options were presented depending on the use case.  Pleas provide more details about how you intend to use the resulting code.  For example, if you want it to be a cross-platform Slicer extension you should follow that pattern.  If you just want to experiment on your machine you might be able to do something simpler.</p>

---
