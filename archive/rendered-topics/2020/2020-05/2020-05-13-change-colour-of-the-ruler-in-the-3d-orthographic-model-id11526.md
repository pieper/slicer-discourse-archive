# Change colour of the ruler in the 3D orthographic model

**Topic ID**: 11526
**Date**: 2020-05-13
**URL**: https://discourse.slicer.org/t/change-colour-of-the-ruler-in-the-3d-orthographic-model/11526

---

## Post #1 by @DanielBF (2020-05-13 20:20 UTC)

<p>Dear all,</p>
<p>First of all, I would like to take this opportunity to congratulate you in the making of this excellent software. It is helping me a lot in achieving my segmentation tasks and creating high quality images.</p>
<p>I am posting this question today because I am unable to find an option to change the colour of the ruler. It is white by default and, when I change the background colour to white, the ruler gets lost with it.</p>
<p>Is there an easy way of making this ruler black? I found the below thread where the user was able to change it to yellow from the “pin options”, but I do not find these options.</p>
<aside class="quote quote-modified" data-post="1" data-topic="8238">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rat01/48/4587_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-manipulate-the-orthographic-view-ruler-in-code/8238">How to manipulate the orthographic view ruler in code</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    How can I access this ruler in python? I’m trying to do things such as toggle its visibility and change its color and thickness. I know how to do all of these things from the pin menu, but I’d like to be able to control these with a script. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/149d3c7f2ea3766f15f587c9d0bfb1245ca72754.png" data-download-href="/uploads/short-url/2Wmqs5p2ca9Lea6CbnohR7ZvOII.png?dl=1" title="image" rel="noopener nofollow ugc">[image]</a>
  </blockquote>
</aside>

<p>Unfortunately, I am a very basic user and I do not know how to manipulate the vtkMRMLAbstractViewNode from the Python terminal.</p>
<p>I would really appreciate your support or any suggestions you may have.</p>
<p>Thank you very much and I wish you a lovely day.</p>
<p>Best regards,</p>
<p>Daniel.</p>

---

## Post #2 by @muratmaga (2020-05-13 20:25 UTC)

<p>In slice view you control the color of the ruler from here:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e37e0bf5bc23c80c0510246462ca70cf183da5ca.png" alt="image" data-base62-sha1="wsurfYEF8m8KETu4iVAO8YFJcoy" width="584" height="117"><br>
and in 3D from here:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f12b08a31bb529fb9c5e51c16db190f1bcb8d3e.png" alt="image" data-base62-sha1="fQB2zBNvSpDx7OoiiloPe8UH502" width="258" height="151"></p>

---

## Post #3 by @pieper (2020-05-13 22:19 UTC)

<p>Even more detail (I needed to look for myself since I haven’t used that menu in a long time)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdf39fd895fcdd0018df7c7458abb135d9e4c397.jpeg" data-download-href="/uploads/short-url/r6ocHbbqAqMwY1ThzZpPyGUggLR.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bdf39fd895fcdd0018df7c7458abb135d9e4c397_2_593x500.jpeg" alt="image" data-base62-sha1="r6ocHbbqAqMwY1ThzZpPyGUggLR" width="593" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bdf39fd895fcdd0018df7c7458abb135d9e4c397_2_593x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdf39fd895fcdd0018df7c7458abb135d9e4c397.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdf39fd895fcdd0018df7c7458abb135d9e4c397.jpeg 2x" data-dominant-color="DDDDE0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">762×642 63.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @jamesobutler (2020-05-14 00:31 UTC)

<p>Here is an example for setting the first 3D View to have a thin black ruler.  You can try this out with the python terminal.</p>
<pre><code class="lang-python">three_d_view_node = slicer.app.layoutManager().threeDWidget(0).mrmlViewNode()  # 3D View "1"
three_d_view_node.setRulerType(slicer.vtkMRMLAbstractViewNode.RulerTypeThin)
three_d_view_node.setRulerColor(slicer.vtkMRMLAbstractViewNode.RulerColorBlack)
</code></pre>

---

## Post #5 by @DanielBF (2020-05-15 10:31 UTC)

<p>Dear all,</p>
<p>Thank you for your very detailed answers. I was confused at first because my ruler options are a bit more limited than the ones you showed in your screenshots. Please refer to the below snip from my 3D Slicer</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee71d55a53a567eaefcc36ab84f82e8b33e4ee4b.png" alt="image" data-base62-sha1="y1nwxNBIbPQrHirc3f0DsgQm9cL" width="331" height="131"></p>
<p>Additionally, I tried to put the lines of code that <a class="mention" href="/u/jamesobutler">@jamesobutler</a> suggested in the Python terminal but it throws the following error after I execute the second line:</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
AttributeError: ‘MRMLCorePython.vtkMRMLViewNode’ object has no attribute ‘setRulerType’</p>
<p>Thank you again for your really kind answers and help. I do not understand why the colour options are missing in my software, should I attempt to reinstall 3D Slicer?</p>
<p>By the way, I am using the latest version of 3D Slicer: 4.10.2 r28257</p>
<p>Thank you very much to everyone that posted an answer, you are very kind.</p>
<p>Best regards,</p>
<p>Daniel.</p>

---

## Post #6 by @pieper (2020-05-15 14:48 UTC)

<p>Hi Daniel -</p>
<p>Probably you are using the current release 4.10.2 but the feature has been updated in the current nightly preview versions (4.11, to be released as 5.0).</p>
<p>Let us know if that doesn’t solve it for you.</p>

---

## Post #7 by @DanielBF (2020-05-18 10:01 UTC)

<p>Dear all and <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Indeed, downloading the 4.11 release allowed me to make these changes.</p>
<p>Thank you all for your fantastic support, I wish you a lovely day.</p>
<p>Best regards,</p>
<p>Daniel.</p>

---
