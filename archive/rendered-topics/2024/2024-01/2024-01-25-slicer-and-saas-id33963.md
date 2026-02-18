# Slicer and SaaS?

**Topic ID**: 33963
**Date**: 2024-01-25
**URL**: https://discourse.slicer.org/t/slicer-and-saas/33963

---

## Post #1 by @Miri_Trope (2024-01-25 12:58 UTC)

<p>Hello, I’m curious if anyone has experimented with employing Slicer and SaaS, and could you provide insights into how the combination functions?</p>

---

## Post #2 by @lassoan (2024-01-25 14:14 UTC)

<p>For one or few users it is very easy to set this up: you can run Slicer in docker on a server (see for example <a href="https://github.com/pieper/SlicerDockers">@pieper’s dockerfiles</a>) and anybody can connect to them from a web browser. There are enterprise solutions with more scalability, such as Amazon AppStreams - see more details <a href="https://discourse.slicer.org/t/running-slicer-in-a-web-browser-via-amazon-appstreams/21431">here</a>.</p>
<p>For hospital/enterprise environment you need to serve potentially many users, manage data access, etc., so the setup is more complex.</p>
<p>You can set up a Kaapana or Kheops server and configure Slicer to be launched in container on the remote server or <a href="https://youtu.be/60_hzSlptWY?si=uPul-Zf5GwDX5ird">the website can launch an installed Slicer on the local computer</a>. One of the upcoming Slicer Project Week projects will add <a href="https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/Launch3DslicerViaClickableUrlsForViewingIdcDataViaSliceridcbrowserAndIdcIndex/">Slicer launching capability from the web browser for the Imaging Data Commons</a>.</p>
<p>If you don’t want to learn how to set up and maintain such a server or you need an FDA-approved system, then there are companies starting to offer Slicer as a service on their data management platforms. <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> plans to present one of these at the upcoming Slicer Project Week.</p>
<p>Check out the <a href="https://projectweek.na-mic.org/PW40_2024_GranCanaria/#cloud--web">project pages in the Cloud/Web category</a> early next week to get more information on the latest efforts.</p>

---

## Post #3 by @Miri_Trope (2024-01-26 20:09 UTC)

<p>Thank you for responding. Is it feasible to incorporate my widget into Slicer and then follow your suggestions to integrate Slicer with my widget as a SaaS? If this is possible, could you provide guidance on how to integrate my widget to Slicer?</p>

---

## Post #4 by @lassoan (2024-01-26 20:16 UTC)

<p>If you use the simplest options - running a docker container locally with builtin novnc - then all you need to do is to add a line to the dockerfile to copy your module’s .py file into the <code>.../Slicer 5.6.1/lib/Slicer-5.6/qt-scripted-modules</code> folder in the docker image.</p>

---

## Post #6 by @Miri_Trope (2024-01-30 09:03 UTC)

<p>Thank you once more for your thoughtful reply. If I choose to follow the straightforward approach you outlined, running a Docker container locally with built-in NoVNC, what would be visible to the user (physician) and the service provider (me)? For instance, as a user, I observe that my data persists in the database even when I shut down the platform occasionally. If the user uploads certain DICOM files where the data is <strong>confidential</strong>, would I, as the service provider, have visibility into their data (“show DICOM database”) ?</p>

---

## Post #7 by @pieper (2024-01-30 09:12 UTC)

<p>In general the service provider has root / admin access to the computer resources so in general yes, they can see the user’s data if they try.  The user needs to trust (e.g. via a legal contract) that the provider won’t peek.</p>
<p>Part of setting up a hosted solution is providing a secure place to store user data.  Generally the data in docker instances goes away when you close the instance, but there are several ways to transfer it to secure storage.</p>

---

## Post #8 by @Miri_Trope (2024-02-01 07:14 UTC)

<p>I’m exploring your recommendation to use Kaapana or Kheops. I’ve delved into the details of each, and I’m interested in knowing your preference between the two. Additionally, could you highlight the significant distinctions between them?</p>

---

## Post #9 by @Miri_Trope (2024-02-01 08:47 UTC)

<p>I understand that the choice between them likely hinges on the specific requirements of my project. Allow me to outline my needs: I aim to empower physicians at the clinic to employ my algorithm, handling 3D images as both input and output. The development process with the clinic comprises two pivotal stages: trial and product. During the trial phase, it is crucial that images are securely viewable, enabling a radiologist to tag them. I leverage these tags for the subsequent trial model development. Upon transitioning to the productization phase, my objective is to grant the physician (initially one) access to my algorithm, seamlessly integrated as a widget in Slicer, through a <strong>web service or other platform</strong> under a monthly license agreement (this keeps the IP for me). This arrangement allows me the flexibility to terminate the subscription at any time, while also facilitating ongoing monitoring of algorithm results, input images, segmentation outputs, and bug tracking.</p>
<p>Considering this comprehensive overview, I am eager to hear your recommendation on the optimal platform or method for implementing my requirements.</p>

---

## Post #10 by @Miri_Trope (2024-02-06 13:27 UTC)

<p>Dear Andreas,</p>
<p>Firstly, I appreciate all your kind and detailed responses. When I initially posed this question, I wasn’t aware of the efforts already made to address this issue. Nevertheless, I am learning a great deal despite not being an MLOPS person. I took the time to delve into the details and now wish to post my understanding. As a result, I am preparing a table of capabilities for several platforms that I find similar, and I intend to share it here. In this table, I will provide an overview of the capabilities of platforms like Kheops, Kaapana, and Monai, addressing their respective strengths. You are welcome to suggest additional platforms, especially those compatible with Slicer, and provide insights into other relevant aspects.</p>
<p>Thank you.</p>

---

## Post #11 by @lassoan (2024-02-06 16:00 UTC)

<p>If you work with a single person then you can roll your own everything. It can be as simple as running Slicer on a computer (either a machine that you own or rent a virtual machine from a cloud provider) and give access to that computer to the physician you work with.</p>
<p>For later phases of the project:</p>
<ul>
<li>Kheops: It is no longer developed, but severe security vulnerabilities should be mostly addressed. It is not secure enough to expose it to the internet with real patient data, but may be usable internally.</li>
<li>Kaapana: Developed for radiology use (to run custom processing workflows, including semi-automatic steps, such as launching a 3D Slicer instance). It is not intended to be used by clinicians for treating patients. Should be quite secure but expected to be used on an internal network. Requires quite a bit of skill to set up and manage.</li>
<li>ImagineHive and Ebatinca are working on systems that are aimed for exactly the use case you described. They combine open-source components with proprietary ones. They haven’t released any product publicly. You can contact them to get see if they can provide early access.</li>
<li>Kitware has a lot of experience with developing systems that can fulfill your needs, building from open-source components. They can be contracted to provide support or do custom developments.</li>
</ul>

---

## Post #12 by @Miri_Trope (2024-02-07 13:44 UTC)

<p>What, in your view, makes Kheops less secure compared to Kaapana? Could you provide more details to shed light on this?</p>

---

## Post #13 by @lassoan (2024-02-08 04:53 UTC)

<p>Since very little developer time is available for Kheops fixes, it is more likely that some of the vulnerabilities (e.g., that would require larger changes and/or not deemed to be high-risk) remain exploitable.</p>
<p>If you want a system that manages patient data and accessible from the open internet then you need to make sure that there is a knowledgeable security team that monitors security bulletins (operating system and all software application and libraries that are used) and reviews and applies patches; conducts security reviews, security testing, penetration testing, etc. Since there is always a risk that despite all efforts, a security breach occurs, the team also needs to have liability insurance. You can either do all this yourself, or you can use services of a company that does all this for you.</p>
<p>Realistically, your options are:</p>
<ul>
<li>only use your system within a trusted private network</li>
<li>run your module on a commercial platform that guarantees data security</li>
<li>put all responsibility on the users (tell them to only upload deidentified patient data and make them responsible for any consequences of any inappropriate data access)</li>
</ul>

---

## Post #14 by @Miri_Trope (2024-02-11 12:04 UTC)

<p>I drafted all my insights about this topic based on my exploration of some platforms built on top of Slicer. This is the <a href="https://medium.com/@miritrope/3d-slicer-monai-kheops-or-kaapana-3e66a3c03f03" rel="noopener nofollow ugc">draft</a>; feel free to provide remarks or suggestions.</p>

---

## Post #15 by @muratmaga (2024-02-11 18:54 UTC)

<p>It would have been nicer if you used a platform that doesn’t require account creation or registrationt to read. I personally find github’s markdown more than enough to create documents, tutorials, even blogs.</p>

---

## Post #16 by @Miri_Trope (2024-02-12 07:44 UTC)

<p>Thanks for bringing this to my attention; you can use <a href="https://telegra.ph/vfvf-02-12" rel="noopener nofollow ugc">this</a> link without needing any registration.</p>

---

## Post #17 by @lassoan (2024-02-12 21:04 UTC)

<p>Thank you for working on this. I’m sure that many people are interested in solution for this very common task (collect patient images, segment them, train model, use that model for segment other images). Your write-up already contains some useful information, but to make it even more useful and more accurate it would be nice if you could spend a bit more time with it.</p>
<p>For example, MONAI is just a library. Probably you meant MONAILabel instead, which provides a server backend. There are lots of room for improvements in the table. For example:</p>
<ul>
<li>Installation: You can pip-install a library, but how are you going to get an application (frontend, backend) going? “Free building” is not very representative of the actual tasks involved: setting up all the software infrastructure (kubernetes, keycloak, dcm4chee, GPU acceleration on docker containers in a virtual machine, etc.) for Kaapana and Kheops can take several weeks or months for someone who is new to all these.</li>
<li>Database filtering: it is available in all, not clear what you mean</li>
<li>Viewers: all these use VTK as a viewer (C++ or Javascript) at the lowest level; for 3D Slicer you can use 3D Slicer or OHIF (3D Slicer’s WebServer module includes OHIF); it would make sense to distinguish between solutions that launch a viewer on the user’s computer (Kheops) or on the server (Kaapana)</li>
<li>Tagging: this word has way too many meanings; do you mean segmentation or assigning keywords or flags to images? Anyway, Slicer supports cloud, too (via MONAILabel, SlicerDocker, etc.).</li>
<li>Storage: Slicer supports PACS storage, too (you can export and send images and segmentations to the PACS).</li>
<li>Training: Slicer supports this, too (for example via MONAILabel); hardware requirements matter a lot (can training just run on the user’s computer, on any operating system; or the system requires GPU cluster or linux machines with kubernetes orchestration)</li>
<li>Cost: all free (they all need some hardware to run on but otherwise they are all free, open-source software)</li>
</ul>
<p>Ultimately, for a fair and accurate comparison, you would probably need to set up all these systems youself and use each for a while.</p>

---

## Post #18 by @Miri_Trope (2024-02-13 06:27 UTC)

<p>Thank you for your detailed response; I gained valuable insights and appreciate your corrections. I will delve deeper into this and refine my work.</p>

---
