# Save transformation matrix programmatically after landmark registration

**Topic ID**: 10732
**Date**: 2020-03-18
**URL**: https://discourse.slicer.org/t/save-transformation-matrix-programmatically-after-landmark-registration/10732

---

## Post #1 by @Tokai (2020-03-18 13:19 UTC)

<p>Operating system: Win10<br>
Slicer version:4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi guys,<br>
I am new to slicer programming. I am loading two volume data( fixed and moving one). Then using slicer’s landmark registration module and selecting some landmark.<br>
After registration is done I want to save the transformation matrix programmatically. If possible getting the transformation matrix after every landmark is selected.<br>
can you please provide an example  to do that?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-03-18 13:25 UTC)

<p>You can save node to file using <code>slicer.util.saveNode()</code> method. Slicer saves transforms in ITK transform file format (binary .h5 file or text .txt file).</p>

---

## Post #3 by @Tokai (2020-03-18 13:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>slicer.util.saveNode()</p>
</blockquote>
</aside>
<p>I used it like below lines:<br>
&gt;&gt;&gt; slicer.util.saveNode(transformNode,“C:\Users\Johar\Desktop\CheckIT\transmat.txt”)<br>
&gt;     False<br>
And as you can see, I get nothing. Can you correct me and show, how to get the transform node correctly and then save?</p>

---

## Post #4 by @pieper (2020-03-18 14:09 UTC)

<p>Use forward slashes not backslashes <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #5 by @lassoan (2020-03-18 14:15 UTC)

<aside class="quote no-group" data-username="Tokai" data-post="3" data-topic="10732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tokai/48/4851_2.png" class="avatar"> Tokai:</div>
<blockquote>
<p>slicer.util.saveNode(transformNode,“C:\Users\Johar\Desktop\CheckIT\transmat.txt”)</p>
</blockquote>
</aside>
<p>You can also use raw strings (add an <code>r</code> character before the string literal), to prevent interpreting backslash as an escape character:</p>
<p><code>slicer.util.saveNode(transformNode,r"C:\Users\Johar\Desktop\CheckIT\transmat.txt")</code></p>

---

## Post #6 by @Tokai (2020-03-18 14:39 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/pieper">@pieper</a><br>
I tried both of your ideas. But I think I am not catching the transform node correctly.</p>
<pre><code>&gt;&gt;&gt; slicer.util.saveNode("Transform",r"C:/Users/transmat.txt")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Slicer 4.10.2\bin\Python\slicer\util.py", line 512, in saveNode
    properties["nodeID"] = node.GetID();
AttributeError: 'str' object has no attribute 'GetID'  
</code></pre>
<p>This is how transform matrix looks like after landmark registration:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39c5a678fe074db472402c22d915c92eb7bf66e1.png" data-download-href="/uploads/short-url/8f4G8mChjCoUEZpzc2aUcWbMpax.png?dl=1" title="Unbenannt" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39c5a678fe074db472402c22d915c92eb7bf66e1.png" alt="Unbenannt" data-base62-sha1="8f4G8mChjCoUEZpzc2aUcWbMpax" width="481" height="500" data-dominant-color="F1F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Unbenannt</span><span class="informations">607×630 20.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2020-03-18 14:42 UTC)

<aside class="quote no-group quote-modified" data-username="Tokai" data-post="6" data-topic="10732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tokai/48/4851_2.png" class="avatar"> Tokai:</div>
<blockquote>
<p>slicer.util.saveNode(“Transform”,r"C:/Users/transmat.txt")</p>
</blockquote>
</aside>
<p>“Transform” is the node’s name. You can use <code>slicer.util.getNode()</code> method to get the node object from its name:</p>
<p><code>slicer.util.saveNode(slicer.util.getNode("Transform"),r"C:/Users/transmat.txt")</code></p>
<p>Please complete one of the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">Slicer programming tutorials</a>. All these basic concepts are described there.</p>

---
