# Use Elastix inside my module

**Topic ID**: 713
**Date**: 2017-07-19
**URL**: https://discourse.slicer.org/t/use-elastix-inside-my-module/713

---

## Post #1 by @marlene (2017-07-19 10:28 UTC)

<p>Hello everybody,</p>
<p>I am sorry if this will result you as a silly question,</p>
<p>I need to call the 3DSlicer Elastix extension inside my module. I cannot find informations about how to know which parameters I need to set before calling an external module.</p>
<p>In particular, once I press the apply button on my Module, Elastix should register the input image of my module with a second atlas image that It will be loaded inside the python script (invisible to the user) . The registration needs to be MRI monomodal and the output image needs to be visualized on the screen.</p>
<p>I also need to save the resulting elastix output image and the affine transformation for further processing inside my module.</p>
<p>thank you very much for any help</p>

---

## Post #2 by @lassoan (2017-07-19 12:39 UTC)

<p>Most Python scripted modules contain test that serves as an example of how to use the module from without its user interface, from another Python script.</p>
<p>For Elastix, the test/example is here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/lassoan/SlicerElastix/blob/master/Elastix/Elastix.py#L635-L646" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerElastix/blob/master/Elastix/Elastix.py#L635-L646" target="_blank" rel="nofollow noopener">lassoan/SlicerElastix/blob/master/Elastix/Elastix.py#L635-L646</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="635" style="counter-reset: li-counter 634 ;">
<li>  self.test_Elastix1()
</li>
<li>
</li>
<li>def test_Elastix1(self):
</li>
<li>  """ Ideally you should have several levels of tests.  At the lowest level
</li>
<li>  tests should exercise the functionality of the logic with different inputs
</li>
<li>  (both valid and invalid).  At higher levels your tests should emulate the
</li>
<li>  way the user would interact with your code and confirm that it still works
</li>
<li>  the way you intended.
</li>
<li>  One of the most important features of the tests is that it should alert other
</li>
<li>  developers when their changes will have an impact on the behavior of your
</li>
<li>  module.  For example, if a developer removes a feature that you depend on,
</li>
<li>  your test should break so they know that the feature is needed.
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Note that when you use it from another module then you have to import the Elastix first and use the Elastix namespace. For example, to get the logic:</p>
<pre><code>import Elastix
logic = Elastix.ElastixLogic()
</code></pre>
<p>To use an atlas, add the atlas to the scene right before the registration and then remove it from the scene once the registration is completed. You can keep the volume node in memory in a Python variable so that you don’t need to load it each time you run the registration.</p>

---

## Post #3 by @lassoan (2017-07-19 12:49 UTC)

<aside class="quote no-group" data-username="marlene" data-post="1" data-topic="713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marlene/48/4566_2.png" class="avatar"> marlene:</div>
<blockquote>
<p>I also need to save the resulting elastix output image and the affine transformation for further processing inside my module.</p>
</blockquote>
</aside>
<p>My understanding is that Elastix currently can only save transformation result as a displacement field. I’ve reported this on their bugtracker, hopefully we’ll hear from them soon. Maybe if you add a note at the bug report then they maybe it would motivate them a bit more to look into this issue. The bug report is here: <a href="https://github.com/SuperElastix/elastix/issues/18" class="inline-onebox">Save transformation result as an ITK transform file · Issue #18 · SuperElastix/elastix · GitHub</a></p>

---

## Post #4 by @marlene (2017-07-20 09:25 UTC)

<p>thank you very much Andras, I managed to do everything except keeping the atlas volume node in memory. What I am currently doing  is just loading the volume every time :</p>
<p>image = slicer.util.loadVolume(’/home/marlene/Desktop/atlas+stripping/A1_skull.nii’,returnNode = True)</p>
<p>could you suggest me a more efficient way ?</p>
<p>thank you again</p>

---

## Post #5 by @lassoan (2017-07-20 12:55 UTC)

<aside class="quote no-group" data-username="marlene" data-post="4" data-topic="713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marlene/48/4566_2.png" class="avatar"> marlene:</div>
<blockquote>
<p>image = slicer.util.loadVolume(’/home/marlene/Desktop/atlas+stripping/A1_skull.nii’,returnNode = True)</p>
</blockquote>
</aside>
<p>Probably loading the node from file does not take significant amount of time (compared to how long the registration takes), but for your information, you can remove and add back the volume to the scene like this:</p>
<pre><code>self.maskImage = slicer.util.loadVolume(’/home/marlene/Desktop/atlas+stripping/A1_skull.nii’,returnNode = True)
# Node is in the scene now and also as a class member variable, which is not deleted when you return from the method

slicer.mrmlScene.RemoveNode(self.maskImage)
# Node is not in the scene anymore but is not deleted because it is still referenced by self.maskImage

slicer.mrmlScene.AddNode(self.maskImage)
# Node is in the scene again

slicer.mrmlScene.RemoveNode(self.maskImage)
self.maskImage = None
# Nothing references the volume now, so it is permanently deleted from memory
</code></pre>

---

## Post #6 by @marlene (2017-07-20 13:02 UTC)

<p>Thank you again for your time , this was really useful <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
