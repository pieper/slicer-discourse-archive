---
topic_id: 6216
title: "Existing Tools For Implant Insertion Planning Trajectory Vis"
date: 2019-03-20
url: https://discourse.slicer.org/t/6216
---

# Existing tools for implant insertion planning, trajectory visualization?

**Topic ID**: 6216
**Date**: 2019-03-20
**URL**: https://discourse.slicer.org/t/existing-tools-for-implant-insertion-planning-trajectory-visualization/6216

---

## Post #1 by @Prashant_Pandey (2019-03-20 01:59 UTC)

<p>OS: Windows 10<br>
Slicer version: 4.8.1</p>
<p>Hi,</p>
<p>I am creating a surgical navigation framework within Slicer for bone fracture procedures. This includes creating preoperative surgical plans using CT scans (i.e. digitizing desired final location of implant). During the procedure, what is the best way to visualize the position of a tracked implant (we are using PLUS + NDI Polaris) compared to the planned position, and is there way to show the optimal live trajectory of the implant? Are there any modules that do this already? I looked at PathExplorer but it didn’t seem to work when I input toy fiducial markers.</p>
<p>Also what is the best way to visualize the overall scene as the tracked implant is being manipulated? The volume reslice driver and Viewpoint modules look promising for showing the implant position with respect to the image and model, but I was wondering if there is a visualization that your team has found is more intuitive for targeting during surgical procedures?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-03-20 05:07 UTC)

<p>You can set up any of the standard visualization found on surgical navigation systems. Slice views usually show resliced image using tracked tool position, optionally orientation (Volume Reslice Driver module); show tool as intersection and/or projection (use Models module to tune intersection/projection parameters). In 3D, you use surface rendering for implant models, volume rendering or segmentation for images, may use Breach Warning module to show tool position relative to target, Viewpoint module to set up view orientation and also to keep object of interest always in the view. Use Watchdog for displaying tool information (out of view, network connection failure, etc.). Enabling ruler and orientation marker in the views may be useful, too.</p>
<p>PathExplorer module is somewhat hard to use and not actively maintained.</p>
<p>We are improving markups widgets (already added line, curve, angle widgets to nightly versions) and plan to improve the line widget to make it a good alternative to annotation ruler and static line models for tool trajectory display.</p>
<p>I would recommend to first replicate very similar views as your surgeons are already got used to and gradually enable more features, experiment with new ideas, based on what you experience in the operating room and what the surgeons ask. Most likely it will be an iterative process, with quick iterations (because you don’t need to implement much, most of the time just configure existing features).</p>

---

## Post #3 by @lassoan (2019-09-19 00:02 UTC)

<p>A post was split to a new topic: <a href="/t/display-line-from-tooltip-to-target/8489">Display line from tooltip to target</a></p>

---
