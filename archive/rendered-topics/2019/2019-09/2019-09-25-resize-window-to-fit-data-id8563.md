# Resize window to fit data

**Topic ID**: 8563
**Date**: 2019-09-25
**URL**: https://discourse.slicer.org/t/resize-window-to-fit-data/8563

---

## Post #1 by @rbahegne (2019-09-25 14:10 UTC)

<p>Hello,</p>
<p>I’m searching for a function which i think exist to resize window to fit correctly the image resolution. The function CenterVolume just move the origin but do not fit to the size the window to the data.</p>
<p>It’s automatically done when loading a dicom, but i couldn’t find it.</p>
<p>Thank you.</p>

---

## Post #2 by @Sunderlandkyl (2019-09-25 14:17 UTC)

<p>You’re looking for the FitSliceToAll function:</p>
<pre><code>layoutManager = slicer.app.layoutManager()
redWidget = layoutManager.sliceWidget('Red')
redLogic = redWidget.sliceLogic()
redLogic.FitSliceToAll() 
</code></pre>
<p>There are also functions for FitSliceToVolume and FitSliceToBackground:<br>
<a href="http://apidocs.slicer.org/master/classvtkMRMLSliceLogic.html" class="onebox" target="_blank" rel="nofollow noopener">http://apidocs.slicer.org/master/classvtkMRMLSliceLogic.html</a></p>

---

## Post #3 by @rbahegne (2019-09-25 15:20 UTC)

<p>This is it indeed, thank you !</p>

---

## Post #4 by @rbahegne (2019-09-26 11:02 UTC)

<p>In fact FitSliceToAll resize all windows, if i have differents nodes with data of different size they are all resized the same way wich could be problematic.</p>
<p>Is it possible to resize windows volume by volume ? I guess FitSliceToVolume could do the job.</p>
<p>For now i did a this-&gt;GetMRMLApplicationLogic()-&gt;FitSliceToAll();<br>
But I cant access FitSliceToVolume (i’m in c++), and i cant find sliceLogic since slice is not a module.</p>
<p>Any suggestions ?<br>
Thanks</p>

---

## Post #5 by @Sunderlandkyl (2019-09-26 13:31 UTC)

<p>You can get the layout manager in C++ with:</p>
<pre><code>qSlicerApplication::application()-&gt;layoutManager()
</code></pre>
<p>From there, you should be able to use the code snippet above to get the Slice logic, and call FitSliceToAll() separately on each slice view.</p>
<p>Ex.</p>
<pre><code>qSlicerApplication::application()-&gt;layoutManager()-&gt;sliceWidget("Red")-&gt;sliceLogic()-&gt;FitSliceToAll();</code></pre>

---

## Post #6 by @rbahegne (2019-10-02 09:05 UTC)

<p>Thank you it’s clear.</p>
<p>I got it to work but it have a problematic behavior on my workflow. The FitSliceToAll function seems to have effect only if I am actually watching something in the software. For instance if there is no node in slicer, then i receive data, create a node, fill it with imagedata, do a FitSliceToAll, it’s not resized (unless if with my speed of light reflex i watch the create data on the app before the FitSliceToAll occur). I could FitSliceToAll everytime i receive images, but any manual zoom would be negated as it would resize constantly.</p>
<p>I though i could bypass the problem with FitSliceToVolume, but it did’nt workout either, unlike FitSliceToAll it occur even when not watching anything but proportion are not respected and clicking on the view cancel the resizing.</p>
<p>Do I miss something, maybe i need to register nodes on the views or something ? I tried some UpdateImageData, or UpdateSliceNodeFromLayout but that did not worked.</p>

---

## Post #7 by @pieper (2019-10-02 15:49 UTC)

<p>FitSliceToAll is a per-slice viewer operation that fits to whatever is currently displayed in the viewer layers (which is controlled by the SliceCompositeNode for the slice viewer).  You can use the viewer’s SliceLogic to fit to arbitrary volume nodes (<a href="https://apidocs.slicer.org/v4.8/classvtkMRMLSliceLogic.html" rel="nofollow noopener">https://apidocs.slicer.org/v4.8/classvtkMRMLSliceLogic.html</a>).</p>

---

## Post #8 by @rbahegne (2019-10-04 09:00 UTC)

<p>You mean doing something like this :</p>
<blockquote>
<p>qSlicerApplication::application()-&gt;layoutManager()-&gt;sliceWidget(“Red”)-&gt;sliceLogic()-&gt;FitSliceToVolume(volumeNode,int(width),int(height));<br>
qSlicerApplication::application()-&gt;layoutManager()-&gt;sliceWidget(“Yellow”)-&gt;sliceLogic()-&gt;FitSliceToVolume(volumeNode,int(width),int(height));<br>
qSlicerApplication::application()-&gt;layoutManager()-&gt;sliceWidget(“Green”)-&gt;sliceLogic()-&gt;FitSliceToVolume(volumeNode,int(width),int(height));</p>
</blockquote>
<p>It does work indeed but not as well as a proper FitSliceToAll, the windows resize to fit height and width, but since it does not have the same ration height/width that the actual window, the image is distorted. I think FitSliceToAll automatically zoom back to fix this problem. But i did manage to isolate the code that does it.</p>

---
