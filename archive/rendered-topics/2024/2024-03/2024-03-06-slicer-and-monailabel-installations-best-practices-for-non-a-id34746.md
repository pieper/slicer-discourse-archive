# Slicer and MonaiLabel installations - best practices for non admin user

**Topic ID**: 34746
**Date**: 2024-03-06
**URL**: https://discourse.slicer.org/t/slicer-and-monailabel-installations-best-practices-for-non-admin-user/34746

---

## Post #1 by @evaherbst (2024-03-06 16:41 UTC)

<p>Hi all,</p>
<p>I finally acquired a computer where I can run MonaiLabel.<br>
I will have students working on segmenting the data, and I want them to be able to iteratively train the model (so use it to infer, then adjust, then use the adjustment to infer again, etc).</p>
<p>I have a very basic question about installations for Slicer, python, and MonaiLabel.</p>
<p>Ideally I would have my computer have a student user account (without admin rights) and one for myself.<br>
The student needs to be able to run Slicer and MonaiLabel.</p>
<p>As far as I can see, Python and Slicer are usually stored in a user’s AppData.<br>
So do I install Python and Slicer in both accounts?</p>
<p>Also, when I run: pip install git+https://github.com/Project-MONAI/MONAILabel#egg=monailabel<br>
I guess I do this in the same folder Python is installed?<br>
So once for each user if stored in user’s AppData?</p>
<p>Will I run into any issues with the student user not having admin rights?</p>
<p>Thank you very much!<br>
Eva</p>

---

## Post #2 by @muratmaga (2024-03-06 20:24 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="1" data-topic="34746">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>I will have students working on segmenting the data, and I want them to be able to iteratively train the model (so use it to infer, then adjust, then use the adjustment to infer again, etc).</p>
</blockquote>
</aside>
<p>You should install the monailabel under your account, start the server and keep it running, and then your student can access Slicer running on the same computer through the MonaiLabel Slicer extension to do what you need to do. Student does not need admin rights, just need to be able to communicate with the MonaiLabel server, which shouldn’t be a problem on a local installation.</p>
<p>However, read the MonaiLabel installation instructions carefully, as you there more than one way of installing. <a href="https://github.com/Project-MONAI/MONAILabel?tab=readme-ov-file#getting-started-with-monai-label" class="inline-onebox">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</a></p>

---

## Post #3 by @evaherbst (2024-03-07 10:05 UTC)

<p>Thank you so much Murat!</p>
<p>When you say start the server and keep it running, what does this mean?<br>
In practice, do I start it every time the student comes in? What happens when the computer is shut down?</p>
<p>Sorry for the super basic question, I’ve never set up a server before.</p>
<p>Thank you,<br>
Eva</p>

---

## Post #4 by @muratmaga (2024-03-07 16:49 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="3" data-topic="34746">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>When you say start the server and keep it running, what does this mean?</p>
</blockquote>
</aside>
<p>This kind of depends on the OS you are using? It is windows or Linux? There are different ways of doing it. On linux, you can simply run the server in a terminal and keep the terminal open (if you close that it will shutdown the MonaiLabel server). You can register this even as a background service, and have it run automatically as the computer starts. Your student should be able to access this server under his/her account.</p>
<p>On windows, things are a little different. Only one person can use the computer at any given time, so I suspect your student will need to be able launch the server Whether they can do this without admin rights I think will depend on the installation route you choose (e.g., docker will probably require admin rights).  (registering monailabel server as a background task is also an option in windows, but it is a lot more complicated than Linux, and I am not sure anyone has tried it).</p>
<p>Things have changed a bit since I last used MonaiLabel, that’s why you should read the latest server installation procedures and figure out which one is going to work for your particular set of constraints (OS, admin issues, computer location etc). Client side is simple, you just install the extension from Slicer and point it out to the server.</p>

---

## Post #5 by @evaherbst (2024-03-08 07:34 UTC)

<p>Thank you so much Murat for the quick and detailed reply.</p>
<p>I am using Windows. I will look into this more and report back if I get it to work without admin rights.</p>
<p>Thank you!<br>
Eva</p>

---
