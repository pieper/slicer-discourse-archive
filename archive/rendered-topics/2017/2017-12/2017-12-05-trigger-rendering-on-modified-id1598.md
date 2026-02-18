# Trigger rendering on Modified

**Topic ID**: 1598
**Date**: 2017-12-05
**URL**: https://discourse.slicer.org/t/trigger-rendering-on-modified/1598

---

## Post #1 by @thaenel (2017-12-05 19:09 UTC)

<p>Hello everyone,</p>
<p>I’m currently developing a module that streams 2D images based on custom OpenIGTLink messages. The streaming works good, concurrency is no issue (I use <code>vtkSlicerApplicationLogic::RequestModified</code> from the receiving thread), images are received and the module clones their content continously into the <code>vtkImageData</code> of a <code>vtkMRMLVectorVolumeNode</code>. This <code>vtkImageData</code> object was initialy added with <code>vtkMRMLVolumeNode::SetAndObserveImageData</code>. After each cloning operation <code>vtkObject::Modified()</code> is called on the <code>vtkImageData</code> object.<br>
Here is the problem: the views are only updated/rerenderd when I interact with them.</p>
<p>What do I need to do (besides the <code>Modified()</code> call on the <code>vtkImageData</code> of the <code>vtkMRMLVectorVolumeNode</code>), that all views are updated/rerendered based on the current state of the MRML scene (including the modified node)?</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2017-12-05 20:45 UTC)

<p>What was the reason you had to reimplement receiving of images through OpenIGTLink? OpenIGTLinkIF module was developed exactly for this purpose.</p>
<p>Image update works well if you use OpenIGTLinkIF by doing this:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/openigtlink/OpenIGTLinkIF/blob/98019cf0cac06b3e15eb43a6b2b99428295504e7/MRML/vtkIGTLToMRMLImage.cxx#L562-L565" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/openigtlink/OpenIGTLinkIF/blob/98019cf0cac06b3e15eb43a6b2b99428295504e7/MRML/vtkIGTLToMRMLImage.cxx#L562-L565" target="_blank" rel="nofollow noopener">openigtlink/OpenIGTLinkIF/blob/98019cf0cac06b3e15eb43a6b2b99428295504e7/MRML/vtkIGTLToMRMLImage.cxx#L562-L565</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="562" style="counter-reset: li-counter 561 ;">
<li>volumeNode-&gt;SetAndObserveImageData(imageData);</li>
<li>
</li>
<li>imageData-&gt;Modified();</li>
<li>volumeNode-&gt;Modified();</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>You may attach a debugger and see better what exact series of steps are performed there.</p>

---

## Post #3 by @thaenel (2017-12-05 22:15 UTC)

<p>I thought that you would mention OpenIGTLinkIF. Unfortunately I’m bound to a non-standard extension of the Protocol (an extension of the IMAGE Message). That’s why had to implement the streaming by myself.</p>
<p>Adding the Modified Call() to the volume node did the trick. I thought this was done automatically as the class has a custom <code>ImageDataModifiedEvent</code>. Thanks for the quick and helpful response <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #4 by @lassoan (2017-12-05 23:07 UTC)

<p>For future reference, OpenIGTLinkIF was designed to be extensible. To add support for a new OpenIGTLink node or message type, tou just need to create a simple converter class in your module and register it using a single method call. Small amount of code also means smaller maintenance and bugfixing efforts and you also get new features for free, such as OpenIGTLink 3 compatibility, image compression (available soon), etc. OpenIGTLink3 allows attaching arbitrary metadata (as key:value pairs) to messages, so you need custom messages less often.</p>

---

## Post #5 by @thaenel (2017-12-06 14:05 UTC)

<p>I didn’t know OpenIGTLinkIF was that extensible. Now that I think about it, it is somehow related to VTK. Of course it is extensible <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=5" title=":grin:" class="emoji" alt=":grin:"> …</p>
<p>I implemeted my own Converter and added a dependecy to OpenIGTLinkIF and the work I did before in 5 days was done in 2 hours (and most likely better done).</p>

---

## Post #6 by @lassoan (2017-12-06 14:38 UTC)

<blockquote>
<p>I implemeted my own Converter and added a dependecy to OpenIGTLinkIF and the work I did before in 5 days was done in 2 hours (and most likely better done)</p>
</blockquote>
<p>Nice work!</p>
<p>Can you share with us what your project is about?</p>

---

## Post #7 by @lassoan (2017-12-07 15:35 UTC)

<p>A post was split to a new topic: <a href="/t/showing-real-time-thermography-images-as-overlay/1610">Showing real-time thermography images as overlay</a></p>

---
