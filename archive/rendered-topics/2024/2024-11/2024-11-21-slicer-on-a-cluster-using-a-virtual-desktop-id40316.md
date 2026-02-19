---
topic_id: 40316
title: "Slicer On A Cluster Using A Virtual Desktop"
date: 2024-11-21
url: https://discourse.slicer.org/t/40316
---

# Slicer on a cluster using a virtual desktop

**Topic ID**: 40316
**Date**: 2024-11-21
**URL**: https://discourse.slicer.org/t/slicer-on-a-cluster-using-a-virtual-desktop/40316

---

## Post #1 by @mandorodriguez (2024-11-21 22:16 UTC)

<p>Greetings,</p>
<p>We users that would like to use Slicer 3D on our compute cluster which has a virtual desktop. We install apps to a common area that they load via a module system (lmod). Are there any examples of someone else doing this?</p>
<p>Or better yet a doc explaining where to copy all base configurations from and how to set all of the environment variables properly to point to an individual users home/work directory?</p>
<p>Thanks!</p>

---

## Post #2 by @muratmaga (2024-11-22 01:13 UTC)

<p>It is almost guaranteed not to work if you try to use slicer through modules. That’s because that directory is not writable to ordinary users, which can break a lot of things.</p>
<p>The simplest solution is everyone to run slicer from their own home directory. If you do want to keep everything fixed for everyone, then consider creating a docker image and use that. If you search the forum for SlicerDocker you will find discussion of those.</p>

---

## Post #3 by @mandorodriguez (2024-11-22 20:01 UTC)

<p>Ok gotcha. Will mostly likely set up a fresh install in the users /work directory.</p>

---
