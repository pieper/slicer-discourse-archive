# FPS deteriation after prolonged fiducial registration

**Topic ID**: 15816
**Date**: 2021-02-03
**URL**: https://discourse.slicer.org/t/fps-deteriation-after-prolonged-fiducial-registration/15816

---

## Post #1 by @WoutertenBolscher (2021-02-03 14:22 UTC)

<p>Hi everyone,</p>
<p>Currently, I am working on a tracked phantom and tool setup. I load the segmented phantom model and 4 associated registration points, and start receiving transforms via OpenIGTLink interface. Then the received sensor positions are continuously registered using the Fiducial Registration Wizard (rigid transform, automatic point matching and auto-update). The loaded model is attached to the resulting transform and thus moves accordingly in the 3D view.<br>
I am working on a HP z2 mini g4 running on Windows 10 with Slicer version: 4.11.<br>
Expected behavior: I would expected the framerate to stay constant at the initial +/- 30 fps.<br>
Actual behavior: A gradual decrease in framerate is observed, where fps is halved every 15-20 minutes.<br>
I have tried downsizing the model or setting manual point matching, however both show the same framerate drop. Furthermore, when the FRW is stopped the framerate instantly recovers to the initial 30 fps, and stays there until the FRW is started again. In that case it will directly drop to the fps of before switching off the FRW and continue a gradual decrease from there.</p>
<p>What could be the cause of the framerate drop and what could be done to prevent it from happening?</p>
<p>Thanks for any help!</p>
<p>Greetings,</p>
<p>Wouter ten Bolscher</p>

---

## Post #2 by @pieper (2021-02-03 21:04 UTC)

<p>Thanks for the detailed report.  It does sound like some kind of resource management issue.</p>
<p>Probably the best is to find a way to profile the code and see where it is spending time and how that changes over time and with the wizard turned on and off.  On linux you could use perf and on mac you can use Instruments for this, but I’m not sure what’s suggested on Windows.  I’ll bet <a class="mention" href="/u/lassoan">@lassoan</a> knows though.</p>

---

## Post #3 by @lassoan (2021-02-05 04:22 UTC)

<p>There should be no need to keep fiducial registration wizard running. Once you computed the transform between the patient image and the patient-attached marker, that transform should remain constant. Can you share your scene so that we have a better idea of your setup?</p>

---

## Post #4 by @WoutertenBolscher (2021-02-08 12:48 UTC)

<p>Thanks for the quick responses. I’ve attached a link to the scene.<br>
We use continuous FRW to update the pose of the segmented phantom. Two 5DOF sensors are embedded in the phantom and based on this 5DOF information 2 points per sensor are defined (on x distance from sensor position along the z-axis, see code below), resulting in a total of 4 points. We assume the relationship between the sensors to be rigid and therefore the 4 points (when not placed ambiguously) can be used for 6DOF registration of the phantom.<br>
We could circumvent use of continuous FRW by sensor fusion of the two sensors, resulting in one 6DOF continuously updated transform, which in turn could be transformed to CT coordinates with a constant registration transform. However, to my knowledge there is no easy way of 5DOF-6DOF sensor fusion in Slicer, right?<br>
In short, we use the automatic update option in the FRW to solve a sensor fusion problem.</p><aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1jLxNV_Tm6zAOuUBSJ3gtySkGhNZjuAl_/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1jLxNV_Tm6zAOuUBSJ3gtySkGhNZjuAl_/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1jLxNV_Tm6zAOuUBSJ3gtySkGhNZjuAl_/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">2021-02-08-Scene.mrml</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>def TransformMarkups(caller, event):<br>
M_SensToEM = caller.GetMatrixTransformToParent()<br>
p1 = M_SensToEM.MultiplyPoint([ 0, 0, -10, 1])<br>
p2 = M_SensToEM.MultiplyPoint([ 0, 0, 10, 1])<br>
markupsNode_EM.SetNthFiducialPosition(0, p1[0], p1[1], p1[2])<br>
markupsNode_EM.SetNthFiducialPosition(1, p2[0], p2[1], p2[2])</p>

---

## Post #5 by @WoutertenBolscher (2021-02-15 14:09 UTC)

<p>Best <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Did you have a chance to look into our problem or do you need any additional information? Hope to hear your take on our issue.</p>
<p>Kind regards</p>

---

## Post #7 by @lassoan (2021-02-16 00:15 UTC)

<p>I’ve managed to reproduce and <a href="https://github.com/SlicerIGT/SlicerIGT/commit/39dfcfa3c83e07981054b6e2164c5f26552b93bb">fix the issue</a>. It’ll be available tomorrow: if you use Slicer Stable Release then reinstall SlicerIGT extension; if you use Slicer Preview Release then upgrade to the latest Slicer Preview Release.</p>

---

## Post #8 by @WoutertenBolscher (2021-02-16 08:25 UTC)

<p>Great, thank you so much <a class="mention" href="/u/lassoan">@lassoan</a>! Amazing to see this level of support on the forum!</p>

---

## Post #9 by @lassoan (2021-02-17 03:12 UTC)

<p>Thank you. It would be great if you could write a short post in the “Success stories” category about what you do and how Slicer and the community helped you to achieve your goals. A few sentences (and a nice image, if there is anything that you can share) would suffice. It would help us in getting more grant funding.</p>
<aside class="onebox category-onebox" style="box-shadow: -5px 0px #92278F;">
  <article class="onebox-body category-onebox-body">
    <h3>
      <a class="badge-wrapper bullet" href="/c/community/success-stories/29">
          <span class="badge-category-bg" style="background-color: #92278F"></span>
        <span class="clear-badge"><span>Success stories</span></span>
      </a>
    </h3>
      <div>
        <span class="description">
          <p>This is the place where you can share how Slicer helped your work. Describe your project and how Slicer was useful in achieving your goal. Include reference to any publication(s) and if possible also add a few nice images or links to videos.</p>
        </span>
      </div>
  </article>
  <div class="clearfix"></div>
</aside>


---
