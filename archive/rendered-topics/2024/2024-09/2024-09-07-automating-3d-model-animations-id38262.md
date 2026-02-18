# Automating 3D Model Animations

**Topic ID**: 38262
**Date**: 2024-09-07
**URL**: https://discourse.slicer.org/t/automating-3d-model-animations/38262

---

## Post #1 by @Miri_Trope (2024-09-07 13:02 UTC)

<p>Hi all, I am looking to create an automated animation (video) that includes rotating a model around a tumor at a 45-degree angle, adjusting the opacity of various volumes in the scene, inserting titles during the video, and performing other similar tasks. What tools or methods would you recommend to achieve this?</p>

---

## Post #2 by @pieper (2024-09-07 15:33 UTC)

<p>Generally speaking you can write a python script to implement exactly what you have in mind.</p>
<p>You can look at the <a href="https://github.com/SlicerMorph/SlicerAnimator">Animator module</a> to get ideas about how to control various visualization options and generate a sequence that can be exported using the ScreenCapture module to make movies.</p>
<p>A lot of the complexity comes from variability in the input data making it hard to create consistently nice movies automatically.</p>

---

## Post #3 by @Miri_Trope (2024-09-08 19:11 UTC)

<p>Thank you for your response.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="38262">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Generally speaking you can write a python script to implement exactly what you have in mind.</p>
</blockquote>
</aside>
<p>Could you clarify what you mean? I’m new to animation.</p>
<p>Could SlicerMorph be of help as well?</p>

---

## Post #4 by @pieper (2024-09-08 20:54 UTC)

<p>The Animator module is part of SlicerMorph, if you are just making Animations you probably don’t need any of the other features it provides so you can just ignore them.</p>
<p>The Animator already provides some of what you describe, but it may not be expressive enough to cover everything.  It’s based on key frame values so there’s an interpolation of the parameters so that things like opacity change frame by frame.  But it’s set up to be used interactively and it’s a bit limited. So that’s why I suggest you look at the python code so you can see how to manipulate the view and export the exact animation you have in mind.</p>

---

## Post #5 by @muratmaga (2024-09-08 21:22 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="38262">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>The Animator module is part of SlicerMorph, if you are just making Animations you probably don’t need any of the other features it provides so you can just ignore them.</p>
</blockquote>
</aside>
<p>The latest code for Animator is in: <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Animator" class="inline-onebox" rel="noopener nofollow ugc">SlicerMorph/Animator at master · SlicerMorph/SlicerMorph · GitHub</a></p>
<p>The other repo Steve linked, is an earlier prototype.</p>
<aside class="quote no-group" data-username="Miri_Trope" data-post="3" data-topic="38262">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/miri_trope/48/67690_2.png" class="avatar"> Miri_Trope:</div>
<blockquote>
<p>Could SlicerMorph be of help as well?</p>
</blockquote>
</aside>
<p>Animator can do the opacity/volume rendering changes, cliipping as well as rotation. but it doesn’t do the inserting the text (though it will render markup labels, if you keep them on).</p>
<p>It is a bit complex to use, perhaps first try the tutorial, with tutorial example, and decide it if it is going to help you: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/Animator" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/Animator at main · SlicerMorph/Tutorials · GitHub</a></p>
<p>Tutorial is a few years old, since then Annotation ROIs were replaced by MarkupROIs. You can use MarkupROI where it says annotationROIs.</p>

---

## Post #6 by @AlexBaev (2024-09-09 05:30 UTC)

<p>The free 3d blender editor is completely suitable for performing such a task. Do you have time to teach him? Excuse my English…</p>

---

## Post #7 by @Miri_Trope (2024-09-09 07:24 UTC)

<p>Thank you so much for all your responses. Apologies for being a bit of a bother, but I have a really exciting idea that I’d love to bring to life. Let me clarify what I mean: Here’s a <a href="https://youtu.be/st3w6nHR6ms" rel="noopener nofollow ugc">link</a> to a screen recording I made using MITK. I’m wondering if it’s possible to automate parts of this process completely (by simply inserting an image and a model, then pressing a button to generate the video). I’m open to using another tool you might suggest, as long as it requires minimal effort. What do you think?</p>

---

## Post #8 by @AlexBaev (2024-09-09 09:21 UTC)

<p>There is no such button to make it “fast and beautiful”. I’ll wait for other answers.<br>
The blender is difficult for a beginner.Blender: Converting the model to a 3D grid, simplifying the grid, installing cameras and lights, rendering. You can watch my YouTube, there we just count the teeth of a 7-year-old child. Falling from a height, dizziness, nausea. <a href="https://www.youtube.com/watch?v=a6jDmCkQKMk" rel="noopener nofollow ugc">link</a></p>

---

## Post #9 by @Miri_Trope (2024-09-09 16:17 UTC)

<p>Dear <a class="mention" href="/u/alexbaev">@AlexBaev</a> , your video looks fantastic! I was wondering if you could work with NIfTI images (MRI) in Blender?</p>

---

## Post #10 by @AlexBaev (2024-09-10 08:59 UTC)

<p>This path is not quite easy. First, we get a 3D mesh from Slicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/205218610203027de57a57636efebfef2a2a8542.jpeg" data-download-href="/uploads/short-url/4BVan03QrjBIphDRcB5koC6sZLI.jpeg?dl=1" title="Head" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/205218610203027de57a57636efebfef2a2a8542_2_690x440.jpeg" alt="Head" data-base62-sha1="4BVan03QrjBIphDRcB5koC6sZLI" width="690" height="440" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/205218610203027de57a57636efebfef2a2a8542_2_690x440.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/205218610203027de57a57636efebfef2a2a8542_2_1035x660.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/205218610203027de57a57636efebfef2a2a8542.jpeg 2x" data-dominant-color="838A85"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Head</span><span class="informations">1284×820 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/800e085552de2cebc403a0d2b70630e656e4c728.jpeg" data-download-href="/uploads/short-url/igPbd4MXNclcjvDt9EhrXHx3h0c.jpeg?dl=1" title="Bone" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/800e085552de2cebc403a0d2b70630e656e4c728_2_690x463.jpeg" alt="Bone" data-base62-sha1="igPbd4MXNclcjvDt9EhrXHx3h0c" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/800e085552de2cebc403a0d2b70630e656e4c728_2_690x463.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/800e085552de2cebc403a0d2b70630e656e4c728_2_1035x694.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/800e085552de2cebc403a0d2b70630e656e4c728.jpeg 2x" data-dominant-color="848382"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bone</span><span class="informations">1286×864 235 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Then we open it in a Blender.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4d0a7880854ef89097158fd5d5da119a328eae7.jpeg" data-download-href="/uploads/short-url/umEglV5H4CmBziyn90yYRy0QCkn.jpeg?dl=1" title="BlenderHead" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4d0a7880854ef89097158fd5d5da119a328eae7_2_678x499.jpeg" alt="BlenderHead" data-base62-sha1="umEglV5H4CmBziyn90yYRy0QCkn" width="678" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4d0a7880854ef89097158fd5d5da119a328eae7_2_678x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4d0a7880854ef89097158fd5d5da119a328eae7_2_1017x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4d0a7880854ef89097158fd5d5da119a328eae7.jpeg 2x" data-dominant-color="717171"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">BlenderHead</span><span class="informations">1277×941 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4542cf6f63533295dfc4479927c305b1e3da02a0.jpeg" data-download-href="/uploads/short-url/9SI5k1vSYkOWkbrDoMd8rK4P8Aw.jpeg?dl=1" title="BlenderBone" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4542cf6f63533295dfc4479927c305b1e3da02a0_2_679x499.jpeg" alt="BlenderBone" data-base62-sha1="9SI5k1vSYkOWkbrDoMd8rK4P8Aw" width="679" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4542cf6f63533295dfc4479927c305b1e3da02a0_2_679x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4542cf6f63533295dfc4479927c305b1e3da02a0_2_1018x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4542cf6f63533295dfc4479927c305b1e3da02a0.jpeg 2x" data-dominant-color="717171"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">BlenderBone</span><span class="informations">1279×941 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
We make textures, transparency, set up a camera and light, bones for animation.<br>
This is how this cartoon was created. (My first one, I’m a bad cartoonist, but I’m working on it). You can’t just spin the view - Blender will make a cartoon that you can watch, but not spin. If you want, send me your research, we’ll try to do something together.<br>
<a href="mailto:a46779935b@mail.ru">a46779935b@mail.ru</a></p>

---

## Post #11 by @Miri_Trope (2024-09-10 15:14 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="38262">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Generally speaking you can write a python script to implement exactly what you have in mind.</p>
</blockquote>
</aside>
<p>Dear <a class="mention" href="/u/pieper">@pieper</a><br>
I’m sorry, but I’m not quite sure what you mean. Could you please explain the pipeline in more detail?</p>

---

## Post #12 by @pieper (2024-09-11 16:14 UTC)

<p>What I mean is that you would approach the animation as a programming project, where you would have use loops to control the transitions from one visual state to the next and record frames at steps in the process.  You would use the Slicer API to access the data and set the visual properties incrementally.  If you are doing something simple, like rotating an object or fading a structure in/out this can be pretty straightforward.  If you want to do multiple things at the same time you need to worry a bit about how those get combined, and you probably end up with a code structure something like what is in the Animator where actions are evaluated at each timepoint and set the visual properties accordingly.</p>

---

## Post #13 by @Miri_Trope (2024-09-11 17:57 UTC)

<p>Thanks for the links <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/pieper">@pieper</a> ! I think I can make this work. Just to clarify, should the video be generated by running the script in <code>TransformAction.py</code>? Here’s the introduction in that file: “This is a placeholder for Animator plugins for transforms. For testing:”. Could you guide me on how to create a basic video using a script, so I can modify it according to my needs?</p>

---

## Post #14 by @pieper (2024-09-11 18:41 UTC)

<p>I don’t think we can spell it out in more detail than we have - the Animator is a python scripted module so you can learn from it, but you’ll need to know enough python and slicer scripting to understand how to work with it.</p>
<p>To your specific question, no you would not run <code>TransformAction.py</code>.  The <code>Action</code> classes are specific scene modifications that take place over a set time frame (start and end time) in the context of an overall animation.  Most of the examples are in the main <code>Animator.py</code> script, but the idea is that additional types of actions could be added to the <code>AnimatorLib</code> package.</p>
<p>You could look at the modules <code>SelfTest</code> for an example of how these are used to make an animation:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py#L1185-L1290">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py#L1185-L1290" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py#L1185-L1290" target="_blank" rel="noopener">SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py#L1185-L1290</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="1185" style="counter-reset: li-counter 1184 ;">
          <li>def test_Animator1(self):</li>
          <li>  """ Ideally you should have several levels of tests.  At the lowest level</li>
          <li>  tests should exercise the functionality of the logic with different inputs</li>
          <li>  (both valid and invalid).  At higher levels your tests should emulate the</li>
          <li>  way the user would interact with your code and confirm that it still works</li>
          <li>  the way you intended.</li>
          <li>  One of the most important features of the tests is that it should alert other</li>
          <li>  developers when their changes will have an impact on the behavior of your</li>
          <li>  module.  For example, if a developer removes a feature that you depend on,</li>
          <li>  your test should break so they know that the feature is needed.</li>
          <li>  """</li>
          <li></li>
          <li>  self.delayDisplay("Starting the test", 10)</li>
          <li>  #</li>
          <li>  # first, get some data and make it visible</li>
          <li>  #</li>
          <li>  import SampleData</li>
          <li>  mrHead = SampleData.downloadSample('MRHead')</li>
          <li>  slicer.util.delayDisplay("Head downloaded...",10)</li>
          <li></li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py#L1185-L1290" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #15 by @AlexBaev (2024-09-12 14:52 UTC)

<p>I offered you to learn a 3d program, here you are offered to learn the python programming language. It’s easier to ask developers to make a transparency level for each layer. Maybe I didn’t search well, but the transparency level is set for the entire 3d view at once. Slicer is a great program, but the buttons are not where they are expected, it’s annoying…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/886ac4e7a0c89bd0c5439fc2992e82183283829b.jpeg" data-download-href="/uploads/short-url/jsNGE5UWQzflywmhxCsLYt3VZCH.jpeg?dl=1" title="453453" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/886ac4e7a0c89bd0c5439fc2992e82183283829b_2_690x488.jpeg" alt="453453" data-base62-sha1="jsNGE5UWQzflywmhxCsLYt3VZCH" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/886ac4e7a0c89bd0c5439fc2992e82183283829b_2_690x488.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/886ac4e7a0c89bd0c5439fc2992e82183283829b_2_1035x732.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/886ac4e7a0c89bd0c5439fc2992e82183283829b.jpeg 2x" data-dominant-color="B4B6CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">453453</span><span class="informations">1277×905 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
