# RegistrationQA extension does not work on Linux but work on Windows

**Topic ID**: 22762
**Date**: 2022-03-30
**URL**: https://discourse.slicer.org/t/registrationqa-extension-does-not-work-on-linux-but-work-on-windows/22762

---

## Post #1 by @Aki (2022-03-30 13:41 UTC)

<p>Hello</p>
<p>Does anyone successfully run the RegistrationQA on Slicer 4.13.0 for Linux?<br>
I tried but the RegistrationQA menu (Registration Quality Assuarance in the Registration module menu) did not appeared.<br>
I built the Slicer4.13.0 for Linux from source on 28 March.  I pulled the source from Slicer master branch on <a href="http://Github.com" rel="noopener nofollow ugc">Github.com</a> on that date. The build was done fine. the built 3D slicer worked fine. Installation of the registrationQA extension was done without problem. Of course, I installed SlicerRT extension because the RegistrationQA required it.</p>
<p>I built the same revision Slicer on Windows11. the built Slicer for Windows works fine and the registrationQA is also work fine. I can see the Registration Quality Adssurance menu in the Registration module menu.</p>
<p>My environment<br>
Linux<br>
OS ubuntu20.04<br>
Cmake 3.23.0-rc2<br>
gcc 9</p>
<p>Windows11<br>
Cmake 3.21.5<br>
compiler  Visual studio 2019 (free version)</p>
<p>Could you give me an advice?<br>
Thank you.</p>

---

## Post #2 by @lassoan (2022-03-31 22:56 UTC)

<p>The official linux build of RegistrationQA extensions seems to work well on Linux. If you build the extension yourself then you need to add all SlicerRT module folders and RegistrationQA module folders to the additional module paths.</p>

---

## Post #3 by @Aki (2022-04-01 01:27 UTC)

<p>Lassoan</p>
<p>Thank you for your rapid reply.<br>
I built the 3D slicer, but the RegistrationQA and SlicerRT was installed from the extension manager.<br>
Thanks for the information that the RegistrationQA should work on the Slicer for Linux. I will straggle more for it.</p>

---

## Post #4 by @lassoan (2022-04-01 01:53 UTC)

<p>It is hard to guarantee ABI compatibility (that your executable can successfully load a dynamic library) if you build them on different computers. You may need to use the exact same versions of runtime libraries, Qt, etc. with the exact same build options.</p>
<p>Therefore, if you build Slicer it is also recommended to build all the extensions that you need.</p>

---

## Post #5 by @Aki (2022-04-01 02:40 UTC)

<p>lassoan</p>
<p>Thank for the advice.<br>
I have tried to build the RegistrationQA extension several times from source for the revision fo Slicer after building Slicer and SlicerRT. But, I encountered a compile error during the build.</p>
<p>My purpose is to use a modified Plastimach DIR of SlicerRT which I modified the source code to be enable to use the “-demon” option. that work fine. but when I install the RegistrationQA ext. to the same Slicer, I could find it on the module list. I thought that my modification might affect the execution of the registrationQA because the registrationQA denpends upon the SliceRT, so I removed my SlicerRT and reinstalled original SlicerRT ext. and the registrationQA ext via the extension manager. but the registrationQA did not showup in the module list,  lathough the original SlilcerRT works well.<br>
I could not have found a cause of this problem, yet. I will check the library versions and/or try to find a way to run the modified SlicerRT and the RegistrationQA properly.</p>

---

## Post #6 by @lassoan (2022-04-01 02:42 UTC)

<aside class="quote no-group" data-username="Aki" data-post="5" data-topic="22762">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aki/48/10110_2.png" class="avatar"> Aki:</div>
<blockquote>
<p>I have tried to build the RegistrationQA extension several times from source for the revision fo Slicer after building Slicer and SlicerRT.</p>
</blockquote>
</aside>
<p>Pull the latest version of SlicerRT and RegistrationQA. They build without problems on the linux factory machine.</p>

---

## Post #7 by @Aki (2022-04-01 02:44 UTC)

<p>lassoan,</p>
<p>OK, I will try and reply a result.</p>

---
