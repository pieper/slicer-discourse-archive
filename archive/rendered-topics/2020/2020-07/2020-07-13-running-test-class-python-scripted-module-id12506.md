# Running Test Class - Python Scripted Module

**Topic ID**: 12506
**Date**: 2020-07-13
**URL**: https://discourse.slicer.org/t/running-test-class-python-scripted-module/12506

---

## Post #1 by @vertebra (2020-07-13 12:55 UTC)

<p>Hello! We have finished our code and tested it manually through the Python interactor. Now, we are attempting to run it through a module, so it is just a click of the button. In the testing class in our python file, do we actually copy and paste our algorithm into the class or do you somehow use the logic?</p>
<p>Also, when assigning inputVolume, is there a way to assign inputVolume to your current selected volume?</p>
<p>Thanks!</p>

---

## Post #2 by @vertebrae (2020-07-13 14:25 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>
<p>We especially need help setting the input and output volume. We are using CTA-cardio as our input volume and we are wondering how we should export this volume into our scripted module.</p>
<p>Thank You!</p>

---

## Post #3 by @Sunderlandkyl (2020-07-13 14:53 UTC)

<aside class="quote no-group" data-username="vertebra" data-post="1" data-topic="12506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vertebra/48/7475_2.png" class="avatar"> vertebra:</div>
<blockquote>
<p>In the testing class in our python file, do we actually copy and paste our algorithm into the class or do you somehow use the logic?</p>
</blockquote>
</aside>
<p>To run the module test, you should call the logic methods from the test class.</p>
<aside class="quote no-group" data-username="vertebra" data-post="1" data-topic="12506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vertebra/48/7475_2.png" class="avatar"> vertebra:</div>
<blockquote>
<p>Also, when assigning inputVolume, is there a way to assign inputVolume to your current selected volume?</p>
</blockquote>
</aside>
<p>Do you mean that you would like to get image that is displayed in the slice views? You can use something like this:</p>
<pre><code>layoutManager = slicer.app.layoutManager()
    # Use first background volume node in any of the displayed layouts
    for layoutName in layoutManager.sliceViewNames():
      compositeNode = self.getCompositeNode(layoutName)
      if compositeNode.GetBackgroundVolumeID():
        return compositeNode.GetBackgroundVolumeID()
</code></pre>
<aside class="quote no-group" data-username="vertebrae" data-post="2" data-topic="12506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/dec6dc/48.png" class="avatar"> vertebrae:</div>
<blockquote>
<p>We especially need help setting the input and output volume. We are using CTA-cardio as our input volume and we are wondering how we should export this volume into our scripted module.</p>
</blockquote>
</aside>
<p>If you want the user to be able to select input/output nodes from the GUI, you could add <a href="https://apidocs.slicer.org/master/classqMRMLNodeComboBox.html" rel="noopener nofollow ugc">qMRMLNodeComboBox</a> to the module widget.</p>

---

## Post #4 by @vertebra (2020-07-13 14:56 UTC)

<p>Okay thank you so much!</p>
<p>Our project requires the user to upload their own medical images, so we needed the inputVolume to be the image that they have uploaded. We will try out the compositeNode technique.</p>
<p>Then, we have the code that segments the vertebra. So, in the test class, we should call those methods?</p>
<p>Thank you!</p>

---

## Post #5 by @Sunderlandkyl (2020-07-13 15:05 UTC)

<aside class="quote no-group" data-username="vertebra" data-post="4" data-topic="12506">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/vertebra/48/7475_2.png" class="avatar"> vertebra:</div>
<blockquote>
<p>Our project requires the user to upload their own medical images, so we needed the inputVolume to be the image that they have uploaded. We will try out the compositeNode technique.</p>
</blockquote>
</aside>
<p>If you want to let the users select their own inputs/outputs, you should use this approach:</p>
<aside class="quote no-group" data-username="Sunderlandkyl" data-post="3" data-topic="12506">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>If you want the user to be able to select input/output nodes from the GUI, you could add <a href="https://apidocs.slicer.org/master/classqMRMLNodeComboBox.html" rel="noopener nofollow ugc">qMRMLNodeComboBox</a> to the module widget.</p>
</blockquote>
</aside>
<p>Logic method should perform the actual segmentation and accept arguments for all of the inputs and outputs. In the test class you can download the sample data (CTA-cardio) and call the logic method that performs the segmentation.</p>

---

## Post #6 by @vertebra (2020-07-13 15:10 UTC)

<p>Okay, we will begin working on the qMRMLNodeComboBox. Thank you so much!</p>
<p>I have attached the test_VertebraSegmentation1 file if you have any suggestions. We believe this is what the module runs we click reload and test. Lines 17-66 perform the actual segmentation. When we copy them into the python interactor in slicer, our desired result works(given a fiducial point has been marked on a vertebra).</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/kbehlmirusmed/VertebraSeg/blob/master/test_VertebraSeg1" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/kbehlmirusmed/VertebraSeg/blob/master/test_VertebraSeg1" target="_blank" rel="nofollow noopener">kbehlmirusmed/VertebraSeg/blob/master/test_VertebraSeg1</a></h4>
<pre><code class="lang-">def test_VertebraSeg1(self):
    """ Ideally you should have several levels of tests.  At the lowest level
    tests should exercise the functionality of the logic with different inputs
    (both valid and invalid).  At higher levels your tests should emulate the
    way the user would interact with your code and confirm that it still works
    the way you intended.
    One of the most important features of the tests is that it should alert other
    developers when their changes will have an impact on the behavior of your
    module.  For example, if a developer removes a feature that you depend on,
    your test should break so they know that the feature is needed.
    """

    self.delayDisplay("Starting the test")
    #
    # first, get some data
    #
    sampleDataLogic = SampleData.SampleDataLogic()
    masterVolumeNode = sampleDataLogic.downloadCTACardio() ##slicer.mrmlScene
      
    
</code></pre>

  This file has been truncated. <a href="https://github.com/kbehlmirusmed/VertebraSeg/blob/master/test_VertebraSeg1" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>The help is much appreciated! We will add in the qMRMLNodeComboBox so the user can select their own input Volume.</p>

---

## Post #7 by @vertebra (2020-07-13 15:25 UTC)

<p>Furthermore, how do we instantiate a qMRMLNodeComboBox <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>

---

## Post #8 by @vertebrae (2020-07-13 15:45 UTC)

<p>We tried to reload and test and we got an error while running. We put down two fiducial points to test our code but we got an error saying that it “could not find nodes in the scene by name or id ‘F’” (our fiducials were called ‘F’). How can we fix this error <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>?</p>

---

## Post #9 by @lassoan (2020-07-13 15:57 UTC)

<p>Please complete this <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">Slicer programming tutorial</a>, which should answer all these questions. Let us know if something is still not clear.</p>

---

## Post #10 by @vertebra (2020-07-13 16:00 UTC)

<p>We have done the tutorial and gone through old modules. We are very appreciative of everyone’s help. We have our code, lines 17-66 in the link two topics above. This code works perfectly when copied and pasted into the python interactor. We just don’t know how to translate that to the testing function in the testing class in our module.</p>
<p>We think it should be easy since we have the code, we just don’t/understand the tutorial on how to transition it.</p>
<p>Thanks!</p>

---

## Post #11 by @vertebra (2020-07-13 17:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I have just re-read through the tutorial. My understanding is that we put our chunk of code that runs the algorithm(for reference, it is lines 17-66 in the GitHub link above) in the logic class of our python text. I do not know where in the logic class we actually put it though.</p>
<p>Then we run the testing function in the testing class of our python text using the onApplyButton function that takes in some parameters. Is there anything we are missing? We are very confused by the whole process as it is our first time coding.</p>

---

## Post #12 by @vertebrae (2020-07-13 18:53 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> <a class="mention" href="/u/cpinter">@cpinter</a>,</p>
<p>Do you have any solutions for this?</p>

---

## Post #13 by @Sunderlandkyl (2020-07-13 19:51 UTC)

<p>You should move lines 22-66 to the logic class in the run method, then change the arguments of run to accept your inputs (segmentation, fiducial node, etc.). You can call run from the test function.</p>

---

## Post #14 by @vertebra (2020-07-13 19:52 UTC)

<p>Thank you so much! And do we just remove line 17-18 where we set the masterVolumeNode because that will be the inputVolume?</p>

---

## Post #15 by @Sunderlandkyl (2020-07-13 20:24 UTC)

<aside class="quote no-group" data-username="vertebra" data-post="14" data-topic="12506" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vertebra/48/7475_2.png" class="avatar"> vertebra:</div>
<blockquote>
<p>Thank you so much! And do we just remove line 17-18 where we set the masterVolumeNode because that will be the inputVolume?</p>
</blockquote>
</aside>
<p>No, the test should set up the scene and test the logic without any user interaction (ie download sample data, place fiducial points, and then call the run method).</p>

---

## Post #16 by @vertebrae (2020-07-14 13:11 UTC)

<p>Hello <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>,</p>
<p>Thank you very much for the help. We still have one issue where the fiducials dissapear every time we run and we get an error saying that there is no node with id (‘F’) (the name of our fiducial). How can we fix this problem?</p>

---

## Post #17 by @vertebrae (2020-07-14 13:34 UTC)

<p>Also we have set the fiducial points as an input for the run function so I am not sure what to do.</p>

---

## Post #18 by @vertebrae (2020-07-14 14:31 UTC)

<p>In addition, the CTA-Cardio scan that we download deltes every time we run so there is no final volume and nothing in the subject hierarchy. This contributes to the fiducial issue above so I was wondering why this happens and what can I do to fix this?</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>

---

## Post #19 by @Sunderlandkyl (2020-07-14 14:38 UTC)

<p>The scene is cleared by the setUp function every time the test is run. You need to download sample data, add necessary nodes, place fiducials, etc, as needed to run the test.</p>
<p>Take a look at the scripted module template for an example of what should be done: <a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/Scripted/TemplateKey.py#L371-L415" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/Scripted/TemplateKey.py#L371-L415</a></p>

---
