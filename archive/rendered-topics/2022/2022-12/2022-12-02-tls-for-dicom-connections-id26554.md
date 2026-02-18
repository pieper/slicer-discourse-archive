# TLS for DICOM Connections?

**Topic ID**: 26554
**Date**: 2022-12-02
**URL**: https://discourse.slicer.org/t/tls-for-dicom-connections/26554

---

## Post #1 by @sscotti (2022-12-02 15:37 UTC)

<p>Is there an option to connect to a PACS (Orthanc in my case) using DICOM TLS ?  I have Orthanc setup to use DICOMTLS, and that works fine between different Orthanc instances, but I would also like the capability to connect 3DSlicer and probably HOROS also to Orthanc.  Orthanc has a self-signed certificate and key file currently, but I see no way to add the certificate file or a different one to the 3DSlicer configuration ?</p>

---

## Post #2 by @pieper (2022-12-02 15:44 UTC)

<p>I don’t think anyone has worked with TLS and Slicer’s DICOM.  It would probably be possible to expose dcmtk’s implementation via CTK and then Slicer.  There would be some work required for that.</p>
<p>In my experience it’s more common to use DICOM only on trusted networks and rely on firewalls and / or VPNs.</p>

---

## Post #3 by @lassoan (2022-12-02 17:03 UTC)

<p><a class="mention" href="/u/sscotti">@sscotti</a> Are you required to use DICOM TLS inside the trusted hospital network? It may make sense, I just don’t see this happening in the hospitals that we have been working with. I don’t think this question has ever come up in Slicer Forum discussions either.</p>
<p>That said, as <a class="mention" href="/u/pieper">@pieper</a> wrote above, DCMTK seems to support DICOM TLS. Since we already use OpenSSL in Slicer, it would be mainly GUI work to allow the user to specify the extra connection information and pass it to DCMTK. If you are interested in working on it, we can help you getting started and with answering any specific questions.</p>

---

## Post #4 by @sscotti (2022-12-02 18:38 UTC)

<p>I am just the consultant, and you are right, inside the facility, usually do not use TLS.  The use case is that Orthanc is in the Cloud, and there is a teleradiology component where readers wish to connect to the PACS remotely, using something like Radiant, Horos, Osirix, etc.  The only Web-based certified viewer than is decent is MedDream and that is very expensive.  Radiant is not certified, but pretty decent software, and OSIRIX I think is.</p>
<p>Basically looking for a way to provide readers some Desktop software that they can use as part of a reading workstation remotely.  The end users for this are in Africa.</p>
<p>I am new to 3DSlicer, and it seems like it is mostly designed for developers and researchers, but it would be nice to have TLS.</p>
<p>I can connect all of those without TLS, and my Orthanc instances are using TLS among themselves, but there might some trouble getting to work with those viewers.</p>
<p>It is interesting that the DCMTK command like this:</p>
<p><code>echoscu -v 147.182.xxx.xx xxxx -ic --anonymous-tls +cf /Users/sscotti/Downloads/orthanc.crt</code></p>
<p>does work though.  HOROS does not, and I am not sure if Radiant supports that either.</p>
<p>Otherwise, they might have to set up VPN, tunneling or something like that.  They have an IP whitelist to restrict access also, but there would be no encryption.  I presume that would be vulnerable to hackers in some ways.  Thanks.</p>
<p>I’m interested in 3DSlicer because it apparently has some extensions for AI, MONAI, etc. ?</p>
<p>I am surprised that no one every asked about TLS before.</p>

---

## Post #5 by @pieper (2022-12-02 18:56 UTC)

<p>Thanks for the extra context.  I would suggest avoiding traditional dicom networking (DIMSE) in a cloud environment.  TLS would only give you encryption of the network traffic, not real protection from hackers or other security issues.  A VPN would be better, or you can tunnel with ssh.  But still, my understanding is that DIMSE is not efficient over wide area networks.</p>
<p>You should look at DICOMweb as an alternative because you can use state of the art web security methods.  For example <a href="https://discourse.slicer.org/t/new-dicomweb-features-launch-slicer-from-web-browser-and-download-upload-data-sets-to-the-cloud-using-dicomweb/17811">Slicer’s DICOMweb extension</a> can use a Google dicom store that authenticates with a Google account so you have finer grained access control.  I haven’t used it, but I understand Orthanc supports DICOMweb, as does dcm4chee.</p>
<p>In terms of web viewers you may wish to look at <a href="https://ohif.org">OHIF</a>.</p>
<p>You are correct that Slicer is not intended for clinical use as-is so be sure to follow local laws and institutional practices.  But yes, MONAI is very promising for ML work and many clinicians use Slicer for their research studies.</p>

---

## Post #6 by @lassoan (2022-12-02 19:44 UTC)

<p>I agree, TLS would not offer enough protection for accessing real patient data via public internet. IP whitelisting does not work for end users, because they use random dynamic IP addresses; and whitelisted IP address can be very easily spoofed, so anybody could send malicious requests that could compromise the server.</p>
<p>Web application for light workloads (quick image review from a phone or tablet anywhere) and VPN for more serious applications (download DICOM data from server and do local processing) seems to be the standard, and I think the same would apply for your use case, too.</p>
<p>By the way, we have lots of active collaborations and developments of modules and Slicer core features specifically for Africa. It would be nice if you could join one of our <a href="https://discourse.slicer.org/c/community/hangout/20">weekly meetings</a> or maybe for a discussion at the upcoming <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/">Slicer Project Week</a> to talk about what you need and what we are working on.</p>
<aside class="quote no-group" data-username="sscotti" data-post="4" data-topic="26554">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sscotti/48/17558_2.png" class="avatar"> sscotti:</div>
<blockquote>
<p>I am surprised that no one every asked about TLS before.</p>
</blockquote>
</aside>
<p>I guess it is because there are several essential requirements for network security, access control, authentication, etc. that are not addressed by TLS. Instead of setting up some custom solutions for remote access, such as proxy servers with authentication, etc. it is much easier to ask users to connect via a VPN. This means users already communicate through secure, encrypted connection and all users and applications are in the same trusted network. In this environment, TLS does not add a lot of value, while there are extra costs due to configuration complexity, software compatibility, and extra computation load. So, I can understand if hospital IT admins choose not to use it.</p>

---

## Post #7 by @sscotti (2022-12-02 20:20 UTC)

<p>Thanks for the input.  DICOMweb would be an option, but I’m not sure if the Radiant Viewer support that.  Orthanc does.  I did test the Radiant Viewer with TLS disabled and the performance was pretty decent still with DIMSE.  I am familiar with OHIF and I do use that sometimes, but the PDF support seems to have some issues.  It does support SR types, and I think there is ongoing development for MONAI integration, etc.  Orthanc’s Stone Viewer isn’t bad, but needs to be developed much more.</p>
<p>I’ll look into those meetings.  I have one that I attend on Monday’s via Zoom with some people in the US, Chris Hafey, et. al. along with about 6-12 others in Informatics / Radiology.  That one is posted on Github.</p>
<p>Thanks.</p>

---

## Post #8 by @pieper (2022-12-02 22:01 UTC)

<aside class="quote no-group" data-username="sscotti" data-post="7" data-topic="26554">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sscotti/48/17558_2.png" class="avatar"> sscotti:</div>
<blockquote>
<p>I attend on Monday’s via Zoom with some people in the US, Chris Hafey, et. al. along with about 6-12 others in Informatics / Radiology</p>
</blockquote>
</aside>
<p>Yes, I’m on that from time to time when I don’t have a conflict.  That would be a good group to ask for advice on this topic.</p>

---

## Post #9 by @ebrahim (2025-11-21 02:40 UTC)

<p>Updating this thread for posterity: <a href="https://github.com/Slicer/Slicer/pull/8121">Since Slicer 5.10, TLS authentication is supported for DICOM sender and listener</a>.</p>

---
