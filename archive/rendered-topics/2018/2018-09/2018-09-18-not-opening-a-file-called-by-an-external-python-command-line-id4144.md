---
topic_id: 4144
title: "Not Opening A File Called By An External Python Command Line"
date: 2018-09-18
url: https://discourse.slicer.org/t/4144
---

# Not Opening a File - Called by an external python Command line

**Topic ID**: 4144
**Date**: 2018-09-18
**URL**: https://discourse.slicer.org/t/not-opening-a-file-called-by-an-external-python-command-line/4144

---

## Post #1 by @Camilla_Tac (2018-09-18 15:18 UTC)

<p>Operating system: Windows Latest version<br>
Slicer version: 4.8.1<br>
Expected behavior: The Slicer program should start running and open the visual file, however it doesn’t do so.<br>
Actual behavior: The Slicer program does not open the file when it is passed through an external Python Command</p>
<p>I am writing a Python (3.6) program which opens an image file directly into 3D Slicer starting from the filepath of the desired image.</p>
<p>When I run the command with the full file path 3D slicer reacts correctly and opens my file:<br>
The line of code which works is the following</p>
<p><code>subprocess.Popen(['C:/Program Files/Slicer 4.8.1/Slicer.exe', '--python-code' , 'slicer.util.loadVolume("C:/Users/Documents/Untitled Folder/sampledata3D.tif")'] , stdout = PIPE, stderr= PIPE)</code></p>
<p>However as soon as I try to pass a variable containing the path of the file, and not the direct path it stops working. This is an example of how the program needs 3D Slicer to open the file:</p>
<p><code>subprocess.Popen(['C:/Program Files/Slicer 4.8.1/Slicer.exe', '--python-code' , 'slicer.util.loadVolume( " %s " )' % openfile ] , stdout = PIPE, stderr= PIPE)</code></p>
<p>However it opens 3D Slicer but in this case does not directly open the file. I have tried all the possible combinations but it doesn’t work!</p>
<p>This is another format I attempted which doesn’t work:</p>
<p><code>subprocess.Popen(['C:/Program Files/Slicer 4.8.1/Slicer.exe', '--python-code' , "slicer.util.loadVolume( self.openfilename )"] , stdout = PIPE, stderr= PIPE)</code></p>
<p>Can anyone help me with this?<br>
It is essential for my project and if this doesn’t work I will have to look for another viewer to support my software!</p>

---

## Post #2 by @lassoan (2018-09-18 19:42 UTC)

<p>Make sure to convert backslashes to forward slashes or add <em>r</em> prefix before the first quotation mark to indicate that it is a raw string. You can check if Slicer receives the correct filename by printing the string to Slicer’s Python console:</p>
<pre><code>print("Trying to open file [%s]" % openfile)</code></pre>

---

## Post #3 by @Camilla_Tac (2018-09-20 07:59 UTC)

<p>Could you please specify what you mean? I attempted specifying the file path with r however it doesn’t accept it.<br>
I do not get any sort of error. 3D slicer opens but simply doesn’t show the file.<br>
This is what I tried under your advice and it still did not work.</p>
<pre><code>self.openfile = C:/Users/Documents/Untitled Folder/sampledata3D.tif

subprocess.Popen(['C:/Program Files/Slicer 4.8.1/Slicer.exe', '--python-code' , "slicer.util.loadVolume(  r' %s'  )" %self.openfile ] , stdout = PIPE, stderr= PIPE)
</code></pre>
<p>I made my python console print what it was passing to your 3D slicer and it was the code you can see below. Which seems correct. The problem I think is that your program doesn’t read variables formatted with % for some reason. I tried the .format() mode for the string and this wasn’t read either.</p>
<p>This is what my python console is passing to 3DSlicer command line now. What is wrong with it and why doesn’t it work.<br>
I have checked that the file exists and can be opened if I manually imput the path in the loadVolume command. However my program needs the path to be stored as a variable:</p>
<p><code>slicer.util.loadVolume( r' C:/Users/Camilla Tac/Documents/Internships/Untitled Folder/sampledata3D.tif ' )</code></p>
<p>Furthermore I tried to get Slicer to print your line of code once I had opened it from my python program and got this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0e9b6f44b41d4a6896d1e3e3f3f9d6d8bc62eb1.jpeg" data-download-href="/uploads/short-url/rwAp9sy70UfYbOs1lgBTUGiksuZ.jpeg?dl=1" title="error-3DSlicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0e9b6f44b41d4a6896d1e3e3f3f9d6d8bc62eb1_2_503x500.jpeg" alt="error-3DSlicer" data-base62-sha1="rwAp9sy70UfYbOs1lgBTUGiksuZ" width="503" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0e9b6f44b41d4a6896d1e3e3f3f9d6d8bc62eb1_2_503x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0e9b6f44b41d4a6896d1e3e3f3f9d6d8bc62eb1_2_754x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0e9b6f44b41d4a6896d1e3e3f3f9d6d8bc62eb1.jpeg 2x" data-dominant-color="A8A8AC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error-3DSlicer</span><span class="informations">961×954 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @ihnorton (2018-09-20 16:25 UTC)

<p>Getting the proper quoting pass-through here was a bit tricky, and I used <a href="https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer">Process Explorer</a> in order to see what was actually passed to Slicer. Here is the working version I ended up with:</p>
<pre><code class="lang-auto">args = [r"C:\Program Files\Slicer 4.9.0-2018-09-10\Slicer.exe", '--python-code', r'slicer.util.loadVolume(r"%s")' % openfile]
subprocess.Popen(args, stdout=PIPE, stderr=PIPE)</code></pre>

---

## Post #5 by @Camilla_Tac (2018-09-20 20:22 UTC)

<p>Thank you very much! Everything sorted!</p>
<p>I would like to pass a command for 3D Slicer to open the Volume rendering automatically from the program python command line. Could you suggest a way of doing it?<br>
I thought the command loadVolume would directly load and open the volume rendering section of 3D Slicer however it doesn’t do so…</p>
<p>Any suggestions on how to run this through the command line???</p>

---

## Post #6 by @ihnorton (2018-10-03 19:34 UTC)

<p>See</p>
<aside class="quote quote-modified" data-post="2" data-topic="3063">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-set-volume-rendering-preset-using-python/3063/2">How to set volume rendering preset using Python</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi Oliver, 
There have been some improvements since 4.8.1 that makes it easier for us to do this. So if you use the latest nightly, then this is what you can do: 
Easier setup of volume rendering (no need to create the display node and update it from the logic): 
volRenLogic = slicer.modules.volumerendering.logic()
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)

This is not very clean, because it uses widgets from the volume rendering module, but you can apply a shift li…
  </blockquote>
</aside>


---
