# FIducial Registration Wizard through Python Interactor

**Topic ID**: 13641
**Date**: 2020-09-23
**URL**: https://discourse.slicer.org/t/fiducial-registration-wizard-through-python-interactor/13641

---

## Post #1 by @Purva_Suryawanshi (2020-09-23 04:44 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.11.0<br>
Expected behavior:I want to align a DICOM volume and an Image using 3 points (fiducial markers) through python. Is there a way I can assign the fiducial markers using python?<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2020-09-23 14:04 UTC)

<p>Yes, of course. All features of Slicer are available from Python. You can create markups fiducial nodes and add points using Python, create a vtkMRMLFiducialRegistrationWizardNode, set its inputs, and use fiducial registration wizard module logic to compute the results (or enable auto-update in your vtkMRMLFiducialRegistrationWizardNode to automatically update output transform from the input points).</p>
<p>You will find <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">this tutorial</a> useful and you can find lots of examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>.</p>

---

## Post #3 by @Andinet_Enquobahrie (2020-10-07 20:07 UTC)

<p>Hi <a class="mention" href="/u/purva_suryawanshi">@Purva_Suryawanshi</a></p>
<p>Just to give you a short example how you can do this ( to add to <a class="mention" href="/u/lassoan">@lassoan</a> response )</p>
<pre><code> # Create markups node to store "From" fiducials
 fromMarkupsNodeID = slicer.modules.markups.logic().AddNewFiducialNode()
 fromMarkupsNode = getNode(fromMarkupsNodeID)
 fromMarkupsNode.SetName(“From”)

 # Create markup node to store "To" fiducials
 toMarkupsNodeID = slicer.modules.markups.logic().AddNewFiducialNode()
 toMarkupsNode = getNode(toMarkupsNodeID)
 toMarkupsNode.SetName(“To”)

# Add fiducials to the markup list as follows manually
fromPoint1= [1.0, 2.0, 3.0]
fromPoint2= [2.0, 4.0, 6.0]
fromPoint3= [3.0, 6.0, 9.0]
fromMarkupsNode.AddFiducial(fromPoint1[0], fromPoint1[1], fromPoint1[2] )
fromMarkupsNode.AddFiducial(fromPoint2[0], fromPoint2[1], fromPoint2[2] )
fromMarkupsNode.AddFiducial(fromPoint3[0], fromPoint3[1], fromPoint3[2] )

toPoint1= [4.0, 5.0, 6.0]
toPoint2= [8.0, 10.0, 12.0]
toPoint3= [12.0, 15.0, 18.0]
toMarkupsNode.AddFiducial(toPoint1[0], toPoint1[1], toPoint1[2] )
toMarkupsNode.AddFiducial(toPoint2[0], toPoint2[1], toPoint2[2] )
toMarkupsNode.AddFiducial(toPoint3[0], toPoint3[1], toPoint3[2] )

# Create transform node to hold the computed registration result
transformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLinearTransformNode")
transformNode.SetName("Registration Transform")

#Create your fiducial wizard node and set the input parameters
myfiducialRegistrationWizardNode = 
    slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLFiducialRegistrationWizardNode”)

myfiducialRegistrationWizardNode.SetAndObserveFromFiducialListNodeId(fromMarkupsNodeID)
myfiducialRegistrationWizardNode.SetAndObserveToFiducialListNodeId(toMarkupsNodeID)
myfiducialRegistrationWizardNode.SetOutputTransformNodeId(transformNode.GetID())
myfiducialRegistrationWizardNode.SetRegistrationModeToSimilarity()
</code></pre>
<p>Hope this helps<br>
Andinet</p>

---

## Post #4 by @Vincebisca (2021-05-19 09:10 UTC)

<p>Hello,</p>
<p>I want to ask a question on the code you wrote there: when I try to use it, slicer says that vtkMRMLFiducialRegistrationWizardNode doesn’t exist… I don’t really understand what I’m missing since I am not used to coding, but I tried various things like adding slicer.modules etc… But nothing seems to work. Do you have a clue on what’s going on?</p>
<p>Thanks !</p>

---

## Post #5 by @lassoan (2021-05-19 12:32 UTC)

<p>Have you installed SlicerIGT extension?</p>

---

## Post #6 by @Vincebisca (2021-05-19 12:41 UTC)

<p>No indeed I didn’t, but then Fiducial Registration Wizard is not the same as the Fiducial Registration module that there is on the classic version of Slicer? Because that is the one I wish to use.</p>
<p>Searching a bit, I found that the following code works to create a transform from 2 lists of fiducials :</p>
<pre><code>transformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLinearTransformNode")
transformNode.SetName("Registration Transform")
parameters = {}
parameters["saveTransform"] = transformNode.GetID()
parameters["movingLandmarks"] = self.VariableMarkupsNode.GetID()  # fiducial points
parameters["fixedLandmarks"] = self.FixedMarkupsNode.GetID()  # fiducial points
fiduciaReg = slicer.modules.fiducialregistration
slicer.cli.runSync(fiduciaReg, None, parameters)  # run the registration
</code></pre>
<p>Precision : the code is not mine, I found it <a href="https://discourse.slicer.org/t/automate-fiducial-registration/3061/5">here</a>.</p>
<p>I have now to find how to apply the transform to the volume I wish to move</p>

---

## Post #7 by @lassoan (2021-05-19 12:47 UTC)

<aside class="quote no-group" data-username="Vincebisca" data-post="4" data-topic="13641">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<p>slicer says that vtkMRMLFiducialRegistrationWizardNode doesn’t exist…</p>
</blockquote>
</aside>
<p>You got this error because you haven’t installed SlicerIGT extension, therefore there is no such node type as “vtkMRMLFiducialRegistrationWizardNode”.</p>
<aside class="quote no-group" data-username="Vincebisca" data-post="6" data-topic="13641">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<p>I found that the following code works to create a transform from 2 lists of fiducials</p>
</blockquote>
</aside>
<p>Yes, this code snippet looks good.</p>
<aside class="quote no-group" data-username="Vincebisca" data-post="6" data-topic="13641">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<p>I have now to find how to apply the transform to the volume I wish to move</p>
</blockquote>
</aside>
<p>You can find example scripts for all commonly needed tasks in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#apply-a-transform-to-a-transformable-node">Script Repository</a>.</p>

---

## Post #8 by @Vincebisca (2021-05-19 12:54 UTC)

<p>I believe that I found out for the transform part in the script repository yes, I had a little struggle to select the transformed node from a ComboBox but it’s solved.</p>
<p>I have a question : using the fiducial registration as I did, is there a way to change the registration type? Like in the Fiducial Registration module there is the choice between “translation” “rigid” and “similarity”. Can I access those with my code?</p>
<p>Thanks</p>

---

## Post #9 by @lassoan (2021-05-19 15:26 UTC)

<p>You can get the list of CLI parameter nodes as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#get-list-of-parameter-names">here</a>.</p>

---
