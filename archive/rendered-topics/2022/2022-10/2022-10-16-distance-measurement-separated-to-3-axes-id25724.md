# Distance Measurement Separated to 3 Axes

**Topic ID**: 25724
**Date**: 2022-10-16
**URL**: https://discourse.slicer.org/t/distance-measurement-separated-to-3-axes/25724

---

## Post #1 by @Marci (2022-10-16 18:19 UTC)

<p>Dear Slicer Community,</p>
<p>is it possible to measure the distance between two fiducials separated to the three main axes (frontal, sagittal, axial)? I not only need the exact distance (hypotenuse of a right triangle) between the two points, but also would like to know the distance projection according to the 3 axes (legs of a right triangle).</p>
<p>Thanks in advance,</p>
<p>Yours sincerely<br>
Marton</p>

---

## Post #2 by @chir.set (2022-10-17 09:01 UTC)

<p>Can you make one or two sketchy drawings of what you’re contemplating ? It’s hard to fully understand your goals.</p>

---

## Post #3 by @Marci (2022-10-17 09:29 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5dcd68fbab60a6315b4afa143ef57769fafa7f05.jpeg" data-download-href="/uploads/short-url/dnOuCjXY0X77cg2O70NwQsxnagB.jpeg?dl=1" title="IMG_0488" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dcd68fbab60a6315b4afa143ef57769fafa7f05_2_690x409.jpeg" alt="IMG_0488" data-base62-sha1="dnOuCjXY0X77cg2O70NwQsxnagB" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dcd68fbab60a6315b4afa143ef57769fafa7f05_2_690x409.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dcd68fbab60a6315b4afa143ef57769fafa7f05_2_1035x613.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dcd68fbab60a6315b4afa143ef57769fafa7f05_2_1380x818.jpeg 2x" data-dominant-color="F6F6F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_0488</span><span class="informations">2127×1263 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @Marci (2022-10-17 09:30 UTC)

<p>Dear chir.set,</p>
<p>thank you for your response, hopefully I can better explain my problem with the sketch.</p>
<p>Yours sincerely<br>
Marton</p>

---

## Post #5 by @chir.set (2022-10-17 10:56 UTC)

<p>Your sketch is very clear, I grant that the drawn orthogonal axes are those of the 3D view without any rotation.</p>
<p>Calculating the distance between the 2 points is quite straightforward :</p>
<pre><code class="lang-auto">import math
lineLength = math.sqrt(vtk.vtkMath().Distance2BetweenPoints(p1, p2))
</code></pre>
<p>The remaining questions will require more time.</p>

---

## Post #6 by @chir.set (2022-10-17 11:51 UTC)

<p>This code snippet should answer your questions, as far as calculating distances is concerned.</p>
<pre><code class="lang-auto">import math

fiducialNode = slicer.util.getNode("ForumProblem")
p1 = fiducialNode.GetNthControlPointPositionWorld(0)
p2 = fiducialNode.GetNthControlPointPositionWorld(1)

# Put p1 at origin. rp2 is p2 relative to p1
rp2 = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])

b = abs(rp2[0]) # LeftRight
a = abs(rp2[1]) # AnteriorPosterior
d = abs(rp2[2]) # InferiorSuperior

e = math.sqrt(vtk.vtkMath().Distance2BetweenPoints(p1, p2))

# Check
c1 = math.sqrt( (a * a) + (b * b) )
c2 = math.sqrt( (e * e) - ( d * d ) )
print(c1, c2)
</code></pre>

---

## Post #7 by @Marci (2022-10-17 13:10 UTC)

<p>Thank you. I copied this into the Python Interactor it shows error unfortunately. What is the problem?</p>

---

## Post #8 by @chir.set (2022-10-17 13:37 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="6" data-topic="25724">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p><code>ForumProblem</code></p>
</blockquote>
</aside>
<p>You should create a Fiducial node with 2 points.<br>
Either you rename the fiducial node to ‘ForumProblem’, or you change this identifier in the code snippet to your fiducial node’s display name, typically ‘F’.</p>
<p>And it’s always a good idea to post error messages when requesting help.</p>

---

## Post #9 by @Marci (2022-10-17 13:54 UTC)

<p>I tried but it does not work:</p>
<pre><code class="lang-auto">... import math
File "&lt;console&gt;", line 7
import math
^
SyntaxError: invalid syntax
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; fiducialNode = slicer.util.getNode("F”)
File "&lt;console&gt;", line 1
fiducialNode = slicer.util.getNode("F”)
^
SyntaxError: EOL while scanning string literal
&gt;&gt;&gt;
&gt;&gt;&gt; p1 = fiducialNode.GetNthControlPointPositionWorld(0)
Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'fiducialNode' is not defined
&gt;&gt;&gt;
&gt;&gt;&gt; p2 = fiducialNode.GetNthControlPointPositionWorld(1)
Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'fiducialNode' is not defined
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; # Put p1 at origin. rp2 is p2 relative to p1
&gt;&gt;&gt;
&gt;&gt;&gt; rp2 = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'p2' is not defined
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; b = abs(rp2[0]) # LeftRight
Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'rp2' is not defined
&gt;&gt;&gt;
&gt;&gt;&gt; a = abs(rp2[1]) # AnteriorPosterior
Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'rp2' is not defined
&gt;&gt;&gt;
&gt;&gt;&gt; d = abs(rp2[2]) # InferiorSuperior
Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'rp2' is not defined
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; e = math.sqrt(vtk.vtkMath().Distance2BetweenPoints(p1, p2))
Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'p1' is not defined
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; # Check
&gt;&gt;&gt;
&gt;&gt;&gt; c1 = math.sqrt( (a * a) + (b * b) )
Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'a' is not defined
&gt;&gt;&gt;
&gt;&gt;&gt; c2 = math.sqrt( (e * e) - ( d * d ) )
Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'e' is not defined
&gt;&gt;&gt;
&gt;&gt;&gt; print(c1, c2)
</code></pre>

---

## Post #10 by @Marci (2022-10-17 13:55 UTC)

<p>First I imported a CT. On the CT I defined two points, namely F1 and F2 as fiducials.</p>

---

## Post #11 by @chir.set (2022-10-17 14:14 UTC)

<p>Funny output <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>What version of Slicer are you using ? It should work with stable or latest preview on any OS.</p>

---

## Post #12 by @cpinter (2022-10-17 14:29 UTC)

<p>Just resolved it. There were a few issues:</p>
<ul>
<li>Quote characters were not good in the getNode call</li>
<li>Method of getting control point position was not correct (expects two arguments in 4.11)</li>
</ul>

---

## Post #13 by @Marci (2022-10-18 15:40 UTC)

<p>Dear chir.set,<br>
dear Csaba</p>
<p>thanks again for your fast response and help! It works all very well. Have a nice day!</p>
<p>Yours sincerely<br>
Marton</p>

---

## Post #14 by @hedmondjohn (2022-12-27 07:28 UTC)

<aside class="quote no-group" data-username="Marci" data-post="9" data-topic="25724">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> Marci:</div>
<blockquote>
<p><code>SyntaxError: EOL while scanning string literal</code></p>
</blockquote>
</aside>
<p>An EOL ( End of Line ) error indicates that the Python interpreter expected a particular character or set of characters to have occurred in a specific line of code, but that those characters were not found before the end of the line . This results in Python stopping the program execution and throwing a syntax error .</p>
<p>The SyntaxError: EOL while <a href="http://net-informations.com/python/err/eol.htm" rel="noopener nofollow ugc">scanning string literal</a> error in python occurs when while scanning a string of a program the python hit the end of the line due to the following reasons:</p>
<ul>
<li>Missing quotes</li>
<li>Strings spanning multiple lines</li>
</ul>

---
