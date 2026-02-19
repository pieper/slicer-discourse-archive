---
topic_id: 14687
title: "Communicate With Slicer From External Python Application"
date: 2020-11-19
url: https://discourse.slicer.org/t/14687
---

# Communicate with Slicer from external Python application

**Topic ID**: 14687
**Date**: 2020-11-19
**URL**: https://discourse.slicer.org/t/communicate-with-slicer-from-external-python-application/14687

---

## Post #1 by @tharisata_c (2020-11-19 13:14 UTC)

<p>Hi,</p>
<p>I’m still a bit unsure about this, so any advice would be great.</p>
<p>What I want to do is create a few fiducial points on my CT Scan and export these into an external python IDE, like Spyder, automatically (as oppose to saving them as a JSON file manually).</p>
<ol>
<li>How do I connect an external python environment (like Spyder) with my Slicer environment so that they can communicate?</li>
</ol>
<p>i.e. to be even more clear, I want to write an external python script that could access the information in Slicer. Is this possible and how can I do it?</p>

---

## Post #2 by @Alex_Vergara (2020-11-19 13:22 UTC)

<p>Why do you need external python IDE when you can use an IDE connected to the Slicer bundled python and access everything from there?<br>
Anyways, you can use either jsons or pickle object for what you want, but it makes no sense to me.</p>

---

## Post #3 by @tharisata_c (2020-11-19 14:07 UTC)

<p>Hi Alex,</p>
<p>Let me be more concise.</p>
<p>My project uses RoboDK to simulate an industrial robot. This has a python interface. I intend to call Slicer through this python interface to take the coordinates of the fiducial points.</p>
<p>I want to this autonomously, i.e. when I select a fiducial point on Slicer, I want it to then be loaded into my RoboDK via interface. I don’t want to be manually pickling or saving objects.</p>
<p>Would this be possible with IDE connected to Slicer bundled python? Please can you expand on what you mean by that and how I can set that up?</p>

---

## Post #4 by @lassoan (2020-11-19 16:09 UTC)

<p>For high-speed streaming of images, transforms, models, etc. we typically use OpenIGLTLink protocol. Slicer can act as OpenIGTLink server and client (provided <a href="https://github.com/openigtlink/SlicerOpenIGTLink">SlicerOpenIGTLink extension</a>), and there are native Python OpenIGTLink clients and servers that you can use in RoboDK. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> does Slicer OpenIGTLink server supports sending of markups fiducial lists?</p>
<p>You can also access Slicer via standard web requests (using <a href="https://github.com/pieper/SlicerWeb">SlicerWeb extension</a>) via Python.</p>

---

## Post #5 by @Sunderlandkyl (2020-11-19 16:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="14687">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> does Slicer OpenIGTLink server supports sending of markups fiducial lists?</p>
</blockquote>
</aside>
<p>No, markups can’t be received via OpenIGTLink currently.</p>

---

## Post #6 by @tharisata_c (2020-11-19 16:13 UTC)

<p>Thank you for your quick response.</p>
<p>Is there any way I could send the mark ups over somehow?</p>

---

## Post #7 by @tharisata_c (2020-11-19 16:16 UTC)

<p>I was thinking of using ROSIGTLink with Slicer, does this support sending of markups fiducial lists? (I wonder if there’s an easier method than this though)</p>
<p>Really grateful for your help.</p>

---

## Post #8 by @lassoan (2020-11-19 18:15 UTC)

<p>Slicer can already transfer positions via TRANSFORM or NDARRAY messages. You could add an observer to a markups list and whenever it is changed, update transform nodes or a table node, which are then automatically sent via OpenIGTLink. I’ll have a look if I can add direct sending of markups as POINT message.</p>
<p>I know that ROSIGTLink already supports TRANSFORM and NDARRAY message types, but you would use ROS not just for getting the point positions from Slicer, but for its openness and flexibility. If you just need the simplest possible solution and don’t need all the features that ROS can offer then you can just use RoboDK and get data via a short Python script (see <a href="https://github.com/SlicerIGT/pyIGTLink/blob/master/pyIGTLink/pyIGTLink.py">pyIGTLink</a>).</p>

---

## Post #9 by @tharisata_c (2020-11-19 18:24 UTC)

<p>Andras, this is brilliant. Thank you very much.</p>
<p>I’ll try it with OpenIGTLink first. And you’re absolutely right, I don’t need all the features of ROS.</p>
<p>Please let me know if you manage to directly send markups as a POINT message.</p>
<p>Very grateful for your help.</p>

---

## Post #10 by @tharisata_c (2020-11-20 18:17 UTC)

<p>Hi <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> and <a class="mention" href="/u/lassoan">@lassoan</a> ,</p>
<p>I’ve just tried setting up the pyIGTLink and I’ve set up the connection node like so: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f923ea03182bd4db6fefe3e0f6e610a8e2d77171.jpeg" data-download-href="/uploads/short-url/zxZPOGGd3MVXEGUlOldx05kDoWt.jpeg?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f923ea03182bd4db6fefe3e0f6e610a8e2d77171_2_690x431.jpeg" alt="Capture1" data-base62-sha1="zxZPOGGd3MVXEGUlOldx05kDoWt" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f923ea03182bd4db6fefe3e0f6e610a8e2d77171_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f923ea03182bd4db6fefe3e0f6e610a8e2d77171.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f923ea03182bd4db6fefe3e0f6e610a8e2d77171.jpeg 2x" data-dominant-color="F0F4F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">804×503 41.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Setting Slicer as a SERVER so I could request its Linear Transforms Message from Python. Does the pyIGTLink only work as a server? If so, can I still extract information about the Slicer Scene such as LinearTransform Nodes and set Slicer as a Client instead?</p>
<p>If this is possible, what code do I write to do it?</p>
<p>Thank you again for your help!</p>

---

## Post #11 by @Sunderlandkyl (2020-11-20 18:33 UTC)

<p>We have an experimental branch that allows pyIGTLink to send as well as receive messages.<br>
You can find the branch here: <a href="https://github.com/SlicerIGT/pyIGTLink/tree/pyIGTLink_client" rel="noopener nofollow ugc">https://github.com/SlicerIGT/pyIGTLink/tree/pyIGTLink_client</a></p>

---

## Post #12 by @lassoan (2020-11-22 03:20 UTC)

<p>I’ve added sending/receiving of markups fiducial lists via OpenIGTLink.</p>
<p>I’ll update the Python client to make it easy to send/receive points in Python, too.</p>

---

## Post #13 by @lassoan (2020-11-22 21:11 UTC)

<p>I’ve created a new OpenIGTLink Python package (originally based on pyIGTlink, but much improved) that can send/receive markups fiducial lists: <a href="https://github.com/lassoan/pyigtl">https://github.com/lassoan/pyigtl</a></p>
<p>I plan to make it available on PyPI within 1-2 weeks, but you can already use it by downloading it and adding it to your Python path.</p>

---

## Post #14 by @tharisata_c (2020-11-23 16:18 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad60d539c57391208bf3e14f9e07d3d6c2212a1d.jpeg" alt="Capture" data-base62-sha1="oJM45uTpkFg0joqnrAqjtfhRY3H" width="628" height="216"></p>
<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Your pyIGTL works amazingly! I’m able to get the linear transforms across.</p>
<p>However, you said above that I can now also send fiducial points? But when I try to select that as an output in I/O Configuration in OpenIGTLinkIF, I’m unable to do so.</p>
<p>Any ideas about this?</p>
<p>Thanks!</p>

---

## Post #15 by @tharisata_c (2020-11-23 17:29 UTC)

<p>Sorry! I was being stupid. Just re-installed the extension and I’ve got it. Thank you Andras! You’ve really, really helped me out with this project.</p>
<p>Extremely grateful.</p>

---

## Post #16 by @lassoan (2020-11-23 21:39 UTC)

<p>Now pyigtl is available on PyPI, so you can install it by <code>pip install pyigtl</code></p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://pypi.org/static/images/favicon.6a76275d.ico" class="site-icon" width="16" height="16">
      <a href="https://pypi.org/project/pyigtl/" target="_blank" rel="noopener">PyPI</a>
  </header>
  <article class="onebox-body">
    <img src="https://pypi.org/static/images/twitter.90915068.jpg" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://pypi.org/project/pyigtl/" target="_blank" rel="noopener">pyigtl</a></h3>

<p>Python interface for OpenIGTLink</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #17 by @tokjun (2020-11-23 23:36 UTC)

<p>This is great! Thanks <a class="mention" href="/u/lassoan">@lassoan</a> !</p>
<p>By the way, I recently reviewed the Python wrapper work by <a class="mention" href="/u/franklinwk">@franklinwk</a> (<a href="https://github.com/franklinwk/openigtlink" rel="noopener nofollow ugc">https://github.com/franklinwk/openigtlink</a>), and it seems to work for some applications.</p>
<p>He hasn’t incorporated it into the C++ library because he had to modify the C++ codes, but it turned out that most of those modifications are not needed. You can find my version of the C++ library with Python Wrapping option at <a href="https://github.com/tokjun/OpenIGTLink/tree/Swig-Python" rel="noopener nofollow ugc">https://github.com/tokjun/OpenIGTLink/tree/Swig-Python</a></p>
<p>I only tested it on Linux, and it still needs some helper functions to make it useful. I will continue to play with it to see if this approach works well.</p>
<p>Junichi</p>

---

## Post #18 by @lassoan (2020-11-24 00:01 UTC)

<p>Native Python implementation is easier to develop, maintain, and install, there is no need to build, it is easier to make it more Pythonic, and interface it with other Python packages (numpy, pandas, json,… ). You can also easily add custom message types in Python.</p>
<p>The only advantage of a Python-wrapped C++ implementation could be speed, but if you prepare the inputs/process outputs in Python anyway then the slight performance gain in the encoding/decoding might not be perceivable. Maybe maintenance workload could be also decreased by reusing an existing implementation (but maintenance of the Python on wrapping may require some of extra non-trivial effort).</p>

---

## Post #19 by @tokjun (2020-11-24 03:27 UTC)

<p>I agree. I’m playing with the wrapped library partly because I have an existing project that depends on it, but I generally prefer native Python implementation to Python-wrapped C++ implementation.</p>
<p>If there is another advantage of wrapping, it’s the potential to wrap with other languages. But I’m not sure if there will be much need other than C++/Python.</p>

---
