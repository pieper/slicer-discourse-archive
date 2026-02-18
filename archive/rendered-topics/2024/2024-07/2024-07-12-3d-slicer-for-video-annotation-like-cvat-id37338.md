# 3D slicer for video annotation? Like CVAT?

**Topic ID**: 37338
**Date**: 2024-07-12
**URL**: https://discourse.slicer.org/t/3d-slicer-for-video-annotation-like-cvat/37338

---

## Post #1 by @MedicalCVEnthusiast (2024-07-12 19:03 UTC)

<p>Does 3D slicer perform video labeling/annotation like CVAT does?</p>
<p>Ideally, I’d like my annotated outputs to be in the coco/yolo format or something similar that I can use when developing CV models for object detection.</p>
<p>Please advise.</p>

---

## Post #2 by @lassoan (2024-07-12 19:05 UTC)

<p>There are a couple of modules in various extensions for time series annotation (2D/3D/4D images, segmentations, transforms, markups, etc.). For example, if you want to annotate 2D+t images then you can use <code>TimeSeriesAnnotation</code> module in <a href="https://github.com/SlicerUltrasound/SlicerUltrasound">Ultrasound</a> extension.</p>

---

## Post #3 by @MedicalCVEnthusiast (2024-07-12 19:08 UTC)

<p>Bear with me if my question sounds rather trivial, as I am not directly working on this project but helping a group use 3D slicer successfully inside a secure environment (no access to the internet). We tried CVAT and it wasn’t approved by the IT. So we’re looking to mimic what CVAT does for video annotations.</p>
<p>By 2D+t, I am assuming you’re referring to a cascade of 2D slices (frames) comprising a video?</p>
<p>The team would like their outputs to be similar to CVAT’s video annotation outputs which they claim are in coco/yolo format.</p>
<p>Please advise how should I approach this.</p>

---

## Post #4 by @lassoan (2024-07-12 19:30 UTC)

<aside class="quote no-group" data-username="MedicalCVEnthusiast" data-post="3" data-topic="37338">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/59ef9b/48.png" class="avatar"> MedicalCVEnthusiast:</div>
<blockquote>
<p>By 2D+t, I am assuming you’re referring to a cascade of 2D slices (frames) comprising a video?</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="MedicalCVEnthusiast" data-post="3" data-topic="37338">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/59ef9b/48.png" class="avatar"> MedicalCVEnthusiast:</div>
<blockquote>
<p>The team would like their outputs to be similar to CVAT’s video annotation outputs which they claim are in coco/yolo format.</p>
</blockquote>
</aside>
<p>Coco/yolo formats are extremely simple, so it should not be easy to implement an exporter (few ten lines of Python code, probably mostly can be written by ChatGPT).</p>
<aside class="quote no-group" data-username="MedicalCVEnthusiast" data-post="3" data-topic="37338">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/59ef9b/48.png" class="avatar"> MedicalCVEnthusiast:</div>
<blockquote>
<p>Please advise how should I approach this.</p>
</blockquote>
</aside>
<p>What kind of images do you annotate? What annotation types would you like to use?</p>

---

## Post #5 by @MedicalCVEnthusiast (2024-07-12 19:39 UTC)

<p>We’re annotating 4k surgery videos.</p>
<blockquote>
<p>What annotation types</p>
</blockquote>
<p>What kind of annotation methods are there for 4k videos? Will appreciate your insight.</p>
<p>Number of videos = 3<br>
Length of each video = 3-4 hours long<br>
Number of frames per second (approx) = 120 frames per second<br>
Total number of frames approximately = 3 (videos) * 4 (hours) * 3600 (seconds) * 120 (fps) = 5184000 frames?</p>
<p>Is this even feasible? Can having a MONAI plugin as a backend accelerate and automate this process?</p>

---

## Post #6 by @RebeccaHisey (2024-07-13 18:37 UTC)

<p>Does the annotation itself need to be done in Slicer? Or is the main requirement just that it does not connect to the internet?<br>
I’ve been working on a basic Qt app for accelerating object annotation for video that just runs locally from command line. It uses both intelligent image selection and active learning to reduce the annotation load and it exports the annotations in both yolo format and as a single csv for each video. It may need a few minor tweaks to work efficiently with such large videos, but I’d be happy to help with that if you’re interested.<br>
The Github is here (sorry for the bare bones ReadME): <a href="https://github.com/RebeccaHisey/Automated_Annotator" class="inline-onebox" rel="noopener nofollow ugc">GitHub - RebeccaHisey/Automated_Annotator</a></p>

---

## Post #7 by @MedicalCVEnthusiast (2024-07-13 22:28 UTC)

<p>Ideally the group would have liked to annotate in CVAT. But the system only has 3D slicer and CVAT installation has been deemed as not-feasible by the IT. Therefore, we are trying to minimize the IT &amp; security overhead, and enable the researchers to successfully use 3D slicer to annotate these videos, and perhaps use MONAI or something parable to accelerate this workflow.</p>
<p>Your tool while very interesting, would not be approved by the IT team to be installed on the secure server as they inspect modules/libraries/softwares to be extensively documented. That doesn’t mean your software isn’t good or useful, because it looks to be, just that it won’t be allowed by IT!</p>

---

## Post #8 by @lassoan (2024-07-14 03:06 UTC)

<p>There are plenty of valid potential security concerns, but the explanations you described coming from your IT folks are vague or irrational and generally non-actionable. It would be useful to talk to your IT department to get a better sense of what they require and why.</p>

---

## Post #9 by @MedicalCVEnthusiast (2024-07-14 11:46 UTC)

<p>So the exact concerns and explanations are:</p>
<p>The environment in which the imaging data lives is a windows VM without wsl2 or linux so CVAT cannot be installed there since CVAT needs ubunut/linux/wsl2. There is a standalone linux based GPU server where a containerized application can be installed and this server can be accessed by remote SSH’ing. But the CVAT container has to be built outside of this server since this too is airtight (no internet access). This is causing a provisioning and id management issue as per IT which is critical since this linux based gpu server is a shared resource among many different departments:</p>
<ol>
<li>
<p>the orchestration of what happens within the docker compose (dynamic volume/port mappings, permissions, etc.) is where the work is.  Along with that, doing it in a maintainable/automated way to ensure security patches, version upgrades, etc. is also a critical part</p>
</li>
<li>
<p>based on CVAT’s docker compose - it is not really suitable for a non-specific/shared-use server (it runs a database, grafana and a host of other applications that are difficult to both persist data for and allow for multiple users (ie other teams) to run separate “versions” of the application at the same time in randomized/open ports)</p>
</li>
</ol>

---

## Post #10 by @lassoan (2024-07-14 13:40 UTC)

<p>Thank you for the additional information, this makes things more clear. The described issues are very common and can be addressed internally by the IT department or by relying on external vendors. Of course some resources are needed for this: additional hardware, IT staff time for setup and maintenance, cost of external services, etc. If these resources are available then this may be the fastest, cleanest solution.</p>
<p>If the needed extra resources are not available, while there are research staff (students, postdocs, research engineers) around whose time is already paid for, then it may make sense to shift down the work of setting up and maintaining applications to them. For the research staff it is a huge learning effort initially to understand and set up everything and then significant continuous effort to operate (managing software updates, users, storage, etc.). If this is your current situation and you are one of this research staff, then you may choose software solution based on what you know already and what you would like to learn. If you are comfortable with Python and desktop development then you will find 3D Slicer very familiar and easy to develop/customize solutions in (and <a class="mention" href="/u/rebeccahisey">@RebeccaHisey</a> and others in this community may be able to help). If you want to learn about containers, databases, IT security, etc. then taking on the task of configuring and maintaining a self-hosted CVAT could be a good learning experience.</p>

---

## Post #11 by @MedicalCVEnthusiast (2024-07-14 13:54 UTC)

<p>Great response, thank you.</p>
<p>We unfortunately do not have additional IT resources (hardware, money for external service, staff time).</p>
<p>The researchers are mostly medical school and comp sci students who’d just like to start annotating these videos asap so I am skeptical if they’d like to take on additional developer-side workload of this scale.</p>
<p>While it is tempting to self-host CVAT and have that learning experience (because it truly is a good one from a development perspective), I don’t have the bandwidth since I have several other projects.</p>
<p>So IT and I both believe if we can make the best of an existing software i.e. 3D slicer to help the researchers with annotating these videos, that’d be ideal. And if we can accelerate the workflow, all the better.</p>
<p>Open to any suggestions on how to successfully use 3D slicer (which is already installed on our gpu server and has the monai plugin available).</p>
<p>Thank you</p>

---

## Post #12 by @RebeccaHisey (2024-07-15 15:06 UTC)

<p>Unfortunately there really isn’t anything pre-existing in Slicer for video-based object detection annotation. MONAI works great for 3D volumes and segmentation annotation, but in my experience it is not set up to handle time series data or object detection. I had originally planned to implement my application as a Slicer module but it ended up being far more complex than it was worth for such a simple task. In my opinion it would make far more sense to use one of the simple applications that already exist such as Yolo Label (<a href="https://github.com/developer0hye/Yolo_Label" class="inline-onebox" rel="noopener nofollow ugc">GitHub - developer0hye/Yolo_Label: GUI for marking bounded boxes of objects in images for training neural network YOLO</a>) than to try to build something custom in Slicer for this. CVAT is the only application that I know of though that supports AI-assisted annotation, and it is an enormous headache to install and configure for self-hosting (which is why I built my own application).</p>
<p>Alternatively I would be happy to work with you to update the documentation on my app to bring it up to the standards required by your IT department.</p>

---

## Post #13 by @MedicalCVEnthusiast (2024-07-15 15:14 UTC)

<blockquote>
<p>Alternatively I would be happy to work with you to update the documentation on my app to bring it up to the standards required by your IT department.</p>
</blockquote>
<p>I am open to this. If you can provide some documentation thereof, I can take this to my IT department. As long as there are no ports that need to be opened and it can work without any internet connectivity inside an airtight server, we can try.</p>
<blockquote>
<p>Unfortunately there really isn’t anything pre-existing in Slicer for video-based object detection annotation. MONAI works great for 3D volumes and segmentation annotation, but in my experience it is not set up to handle time series data or object detection.</p>
</blockquote>
<p>I am assuming you’re referring to a scenario in which we would want to annotate these videos automatically? I should give more context: the researchers will be annotating these videos frame by frame so there is a manual component involved and in that case if all they’re annotating 2D+t frames, shouldn’t 3D slicer suffice? Instead of the usual radiology mri ct’s, it’s just going to be 2D frames in 4k of a surgical procedure.</p>
<p>Again, I am also looking forward to reviewing the documentation regarding your software. Thank you</p>

---

## Post #14 by @RebeccaHisey (2024-07-15 16:14 UTC)

<aside class="quote no-group" data-username="MedicalCVEnthusiast" data-post="13" data-topic="37338">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/59ef9b/48.png" class="avatar"> MedicalCVEnthusiast:</div>
<blockquote>
<p>I am open to this. If you can provide some documentation thereof, I can take this to my IT department. As long as there are no ports that need to be opened and it can work without any internet connectivity inside an airtight server, we can try.</p>
</blockquote>
</aside>
<p>The only thing that internet is needed for is installing the required packages and downloading the initial model weights, which we can probably find a way to package. After installation, everything is done locally so there are no ports opened whatsoever. Is there specific documentation that’s required?</p>
<aside class="quote no-group" data-username="MedicalCVEnthusiast" data-post="13" data-topic="37338">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/59ef9b/48.png" class="avatar"> MedicalCVEnthusiast:</div>
<blockquote>
<p>I am assuming you’re referring to a scenario in which we would want to annotate these videos automatically? I should give more context: the researchers will be annotating these videos frame by frame so there is a manual component involved and in that case if all they’re annotating 2D+t frames, shouldn’t 3D slicer suffice? Instead of the usual radiology mri ct’s, it’s just going to be 2D frames in 4k of a surgical procedure.</p>
</blockquote>
</aside>
<p>To be clear the application is not fully-automated, it just suggests bounding boxes that a human reviewer needs to review and correct. Despite the name (I’m trying to come up with a better one), it does require manual review of all images and proposed annotations. Most of my work is on surgical tool detection in video so it’s been designed to streamline this process.<br>
I’m not saying that it’s impossible to do this annotation in Slicer, but it’s a bit like using a bomb to light a matchstick. By comparison annotating 2D+t surgical videos with bounding boxes is far less complex than segmentation of 3D volumes like CT/MRI. Because Slicer is set up to handle these complex data types so well, it just adds a lot of overhead when you to try to implement these really simple tasks. Also if your videos are 3-4 hours in length and not divided into smaller segments, it would take quite a long time to load them into Slicer.</p>
<p>Please let me know if there’s any specific documentation you need or if it’s just a more detailed overview of how it works.</p>

---
