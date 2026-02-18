# Tranformation of labelmap not working on script

**Topic ID**: 25499
**Date**: 2022-09-30
**URL**: https://discourse.slicer.org/t/tranformation-of-labelmap-not-working-on-script/25499

---

## Post #1 by @justomont (2022-09-30 11:04 UTC)

<p><strong>Operating system:</strong> MacOS BigSur 11.6<br>
<strong>Slicer version:</strong> 5.0.3<br>
<strong>Expected behavior:</strong> Transform labelmap volume node<br>
<strong>Actual behavior:</strong> Labelmap volume node is not transformed</p>
<p>Hello everyone,</p>
<p>I’m developing a script, that among other things, registers an MNI template onto the T1 brain scan of some patients for anatomical research purposes. For that, I just register the MNI template as the moving volume to the scan of each patient (fixed), which works wonderful. However, this MNI template also comes with a label map naming each region of the cortex, which I would like to transform too, so I could identify specific points in the brain. For that, I just apply the transformation matrix from the previous registration to the label map volume, like this:</p>
<pre><code class="lang-auto">labelmapVolumeNode = slicer.util.loadVolume(labelmapPath,properties={"name":"MNI_labels","labelmap":True,"center":True})
transform = slicer.util.getFirstNodeByName("Transform2MNI")
transformedLabels = slicer.mrmlScene.CopyNode(labelmapVolumeNode)
transformedLabels.SetName("transformed_MNI_labels")
transformedLabels.ApplyTransformMatrix(transform.GetMatrixTransformToParent())
</code></pre>
<p>Where MNI_labels is the label map volume I would like to transform, and Transform2MNI is the transformation from the previous and successful registration. However, the code is not working. It creates the new “transformed_MNI_labels” Node but is just a replica of the original label map. What’s also interesting is that if I copy and paste the lines of code onto the python interactor, it works!</p>
<p>Finally, all the commands are in a simple function with no conditionals or structures of any kind that could prevent that part of the code from running. I’ve also checked that it was running adding logging info in between the lines. And as said, the label map is loaded and copied, the problem is that it is not transformed.</p>
<p>Am I missing something? Is there a better way to transform the label map?<br>
Thanks in advance</p>

---

## Post #2 by @ebrahim (2022-09-30 14:26 UTC)

<p>Could it be that the transform is being applied, but the view is also being corrected so as to undo the effect visually? Sometimes I get thrown off by this. Like I’ll apply a transform to a volume and not see any effect, except the subtle effect that the slice views go from Axial/Sagittal/Coronal to “Reformat”.</p>
<p>(My comment applies to affine transforms only; not sure if that is what you have)</p>
<p>One way to see if that’s happening: you said that when you paste your snippet into the python interactor, it works. So after pasting it, try toggling the visibility of the successfully transformed label map. When it comes back into visibility do the slice views change to remove the visual effect of the transformation?</p>
<p>Alternatively: if you make the transformed labelmap visible at the same time that the transformed T1 image is visible, do they actually successfully line up?</p>

---

## Post #3 by @justomont (2022-10-03 09:16 UTC)

<p>Thank you so much for your response,</p>
<aside class="quote no-group" data-username="ebrahim" data-post="2" data-topic="25499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar"> ebrahim:</div>
<blockquote>
<p>Could it be that the transform is being applied, but the view is also being corrected so as to undo the effect visually? Sometimes I get thrown off by this. Like I’ll apply a transform to a volume and not see any effect, except the subtle effect that the slice views go from Axial/Sagittal/Coronal to “Reformat”.</p>
</blockquote>
</aside>
<p>The slice view is kept as Axial/Sagittal/Coronal, it doesn’t change to Reformat.</p>
<aside class="quote no-group" data-username="ebrahim" data-post="2" data-topic="25499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar"> ebrahim:</div>
<blockquote>
<p>(My comment applies to affine transforms only; not sure if that is what you have)</p>
</blockquote>
</aside>
<p>Yes! It is an affine transform</p>
<aside class="quote no-group" data-username="ebrahim" data-post="2" data-topic="25499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar"> ebrahim:</div>
<blockquote>
<p>One way to see if that’s happening: you said that when you paste your snippet into the python interactor, it works. So after pasting it, try toggling the visibility of the successfully transformed label map. When it comes back into visibility do the slice views change to remove the visual effect of the transformation?</p>
</blockquote>
</aside>
<p>No, the slice views are not changing after pasting the snippet in the python interactor either</p>
<aside class="quote no-group" data-username="ebrahim" data-post="2" data-topic="25499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar"> ebrahim:</div>
<blockquote>
<p>Alternatively: if you make the transformed labelmap visible at the same time that the transformed T1 image is visible, do they actually successfully line up?</p>
</blockquote>
</aside>
<p>They successfully line up <strong>only after</strong> running the snippet from the Python interactor. In the following image you can see the MNI template registered to the subject (ICBM152_registered) and the labelmap after transforming it with the script:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/0725ba124f2bd8ba6372412b3e0ffac1e64594d4.png" alt="Captura de pantalla 2022-10-03 a las 10.38.57" data-base62-sha1="11eaDVVPvDujP8HfiL7yF03bev2" width="388" height="312"></p>
<p>where the transformed labelmap (transformed_MNI_labels) is clearly not transformed. However, the following figure shows in the same slice how the transformation is performed after running the snippet from the interactor:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e0e90e2fd55d568dd2601722972d4774a9f5768.png" alt="Captura de pantalla 2022-10-03 a las 10.39.18" data-base62-sha1="6zraBBEF5UaS6k5y7nK1THYtA4E" width="388" height="312"></p>
<p>Any other ideas on what could be causing this script issue?</p>

---

## Post #4 by @ebrahim (2022-10-03 13:58 UTC)

<p>How are you running the script when it’s not by pasting into the python interactor?</p>
<p>I wonder if some of the objects (<code>transform</code>, <code>transformedLabels</code>, <code>labelmapVolumeNode</code>,…) are coming out as <code>None</code> and no error is being reported because the later funcitons do not complain when given <code>None</code>. Maybe you could print out those objects in the snippet to make sure they’re as expected</p>

---

## Post #5 by @justomont (2022-10-04 09:25 UTC)

<p>I’m running the script from a Scripted Module.</p>
<p>I already checked and that part of the script is running, the line that is apparently the issue is <code>transformedLabels.ApplyTransformMatrix(transform.GetMatrixTransformToParent())</code> as it is not applying the transform. I’ve also tried with <code>labelmapVolumeNode.ApplyTransform(transform.GetTransformToParent())</code> but it’s not working either.</p>
<p>All the objects are coming out as they are expected (<code>labelmapVolumeNode</code> and <code>transform</code>), with the exception of the <code>transformedLabels</code>, which is just the copy of <code>labelmapVolumeNode</code>, but it’s not <code>None</code>.</p>

---

## Post #6 by @ebrahim (2022-10-05 14:42 UTC)

<p>What if you apply the transform using <code>SetAndObserveTransformNodeID</code> as <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#apply-a-transform-to-a-transformable-node" rel="noopener nofollow ugc">seen here</a>, then does it work from the scripted module?</p>
<p>I’m not sure I understand the difference between the <code>SetAndObserveTransformNodeID</code> and the <code>ApplyTransform</code> approach, but if the difference is that <code>ApplyTransform</code> hardens the transform and this is something you want then you can call <code>HardenTransform</code> on the segmentation node afterwards.</p>

---

## Post #7 by @S_Arbabi (2022-10-10 19:25 UTC)

<p>I also have the same question, did you find the solution <a class="mention" href="/u/justomont">@justomont</a> ?</p>

---

## Post #8 by @justomont (2022-10-11 10:23 UTC)

<p>Since the transformation was working from the Python Interactor, I just moved the section of the script that registered the label map to a different new function (called right after finishing the registration of the MNI template) and it worked. To be honest, I don’t really understand why it is working now, but it does.</p>

---

## Post #9 by @lassoan (2022-10-19 06:35 UTC)

<aside class="quote no-group" data-username="justomont" data-post="1" data-topic="25499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/justomont/48/16814_2.png" class="avatar"> justomont:</div>
<blockquote>
<p><code>slicer.mrmlScene.CopyNode(labelmapVolumeNode)</code></p>
</blockquote>
</aside>
<p>CopyNode is a very low-level function. It makes a copy only of the data node, but still keeps referencing the same display, storage, etc. nodes. If you want to create an independent copy of a node then you can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#clone-a-node">clone feature of Subject Hierarchy</a>.</p>

---
