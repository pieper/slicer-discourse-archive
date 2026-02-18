# SlicerIGT: Transform to Markup for real-time patient tracking using the Fiducial Registration Wizard

**Topic ID**: 8708
**Date**: 2019-10-08
**URL**: https://discourse.slicer.org/t/slicerigt-transform-to-markup-for-real-time-patient-tracking-using-the-fiducial-registration-wizard/8708

---

## Post #1 by @W.J.Heerink (2019-10-08 11:22 UTC)

<p>Hi, I’m trying to use Slicer IGT to track and correct for changes in patient position in real-time. The patient is tracked with multiple 6DOF NDI aurora sensors that are read out by PlusServer and send to Slicer as transforms. From these sensors, I only use the position.</p>
<p>I would like to use the Fiducial Registration Wizard with Auto-update mode turned on, to register the current patient position with the initial patient position, in order to determine the most suitable average rigid transformation. However, the wizard requires markup fiducials as input and the option: “Place fiducials using transforms” does not update the fiducials when the transforms change in value.<br>
Is there a way to automatically update markup fiducials with the translational part from the transforms that are sent?</p>
<p>I found this thread (<a href="https://github.com/openigtlink/SlicerOpenIGTLink/issues/67" rel="nofollow noopener">https://github.com/openigtlink/SlicerOpenIGTLink/issues/67</a>) and I wonder if, when implemented, this would solve my problem. If so, is there may be a workaround to use in the meantime? Thanks!</p>
<p>Wout</p>

---

## Post #2 by @lassoan (2019-10-08 11:52 UTC)

<p>From Plus you can send a transform for each optical marker as usual. In Slicer, you can write a few lines of Python script that adds an observer to a transform and updates a markup fiducial point. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_notification_if_a_transform_is_modified" rel="nofollow noopener">script repository</a> for examples.</p>

---

## Post #3 by @W.J.Heerink (2019-10-08 11:57 UTC)

<p>Thanks for the quick reply!</p>

---
