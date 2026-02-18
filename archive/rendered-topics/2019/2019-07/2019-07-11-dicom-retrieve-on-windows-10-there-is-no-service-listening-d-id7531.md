# DICOM Retrieve on Windows 10. There is no service listening DICOM communications (No telnet connection to ports)

**Topic ID**: 7531
**Date**: 2019-07-11
**URL**: https://discourse.slicer.org/t/dicom-retrieve-on-windows-10-there-is-no-service-listening-dicom-communications-no-telnet-connection-to-ports/7531

---

## Post #1 by @MDLSoft (2019-07-11 14:08 UTC)

<p>Hi all! I’m new here. My name is Manuel and I’m HCIS Engineer. I apologize for my English wich is far to be perfect, but I’m sure near to everyone can understand me.</p>
<p>Platform Windows 10 Pro, Ver. 10.0.17134, compilation 17134.<br>
3D Slicer 4.10.2</p>
<p>I’m PACS administrator of a 9 large hospitals inside a grid configuration with 51 hospitals. Now, some radiologyst want to use Slicer and they have it installed and configured correctly. I can see Slicer asking to PACS and received correctly C-Move command, but when PACS try to connect to the workstation with Slicer I see a communication error.</p>
<p>I tryed to do a telnet to default port 11112, localhost and remote and I can’t see any service listening at this port (no telnet connection).</p>
<p>I saw in Slicer documentation that there is a communication service (storescp helper) wich is the one that listen for DICOM communication, but I can’t find this proccess in any workstation where Slicer is installed.</p>
<p>I have installed Ginkgo CAD to do some tests and just when I lauch Ginkgo It lauches a service listening to this port (11112), and no problems with Q/R, but when I close Ginkgo and lauch Slicer, no one service is listening at 11112. I tryed to change port (11113, 104, 2106, etc) but no changes.</p>
<p>I tryed to lauch slicer as administrator, compatibility mode with no better results. In windows event viewer there isn’t any event related to Slicer.</p>
<p>It looks like slicer don’t lauch or haven’t DICOM listener service.</p>
<p>Please, any help will be appreciated! Thank you!</p>

---

## Post #2 by @pieper (2019-07-11 15:15 UTC)

<p>Hi Manuel -</p>
<p>You can start the listener manually and then set it to start automatically when Slicer starts.  Otherwise it sounds like you have everything else you need.  Let us know how it goes.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25f9ef7c21147be9cd5c17776d859635a30824c0.png" alt="image" data-base62-sha1="5pX9lmHO3my9FDH9wjHW8GKL1aE" width="476" height="260"></p>

---

## Post #3 by @MDLSoft (2019-07-12 08:26 UTC)

<p>Thank you Steve, it worked!<br>
I’m somewhat embarrassed for not having seen that, It is in an uncommon place, the same as the dicom configuration is in a bit strange place for me.</p>
<p>After start the listener, I discovered a weird functioning of Slicer.</p>
<p>First of all, when I do a retrieve no one message or proccess bar indicating the proccess of the retrieve, only a text in the left bottom corner that appears and dissapears quickly, but the retrieve takes a while, (I can see it in PACS sending each SOP UID).</p>
<p>The resources consuption of Slicer is very high while retrieving and when it finish I only can see it because consuption resources drops and in the PACS logs.</p>
<p>After retrieve finish, I close the query form, but no data appears in the dicom browser, I have to close Slicer and open it again to see the patient data retrieved.</p>
<p>If I delete study or patient from the dicom browser, ok it’s possible deleted patient data from database, but incoming directory contains all the images of all studies retrieved (a lot of space), and dicom folder have the apparent structure of a dicomdir for each study, but only with StudyInstance UID, Series Instance UID as folders, not contain information and isn’t deleted when I delete study or patient from dicom browser.</p>
<p>When I close Slicer, storescp service is still running.</p>
<p>Maybe I should open new threads whith these problems. I don’t know if are program bugs or I don’t know how to use it as happened with listener.</p>
<p>Thank you!!</p>

---

## Post #4 by @pieper (2019-07-12 13:48 UTC)

<p>Hi Manuel -</p>
<p>Glad it’s working for you, at least at a basic level. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>Thanks for reporting the issues - yes, I think we should put them in <a href="https://issues.slicer.org/my_view_page.php" rel="nofollow noopener">the slicer issue tracker</a>, although to be honest I don’t know when anyone will be working on them.  The dicom networking (dimse) interface was written several years ago and I’m not sure how much use it gets in reality.  The issues you are pointing out appear to be the result of some changes driven by other use cases (focused on the use of dicom files and not dimse networking).  As you know it can be very hard to test and debug these if you aren’t using it for real work.</p>
<p>Some of the issues you raised might be easy to fix if you or others have a strong real world need and interest in helping define and test the fixes.  On the other hand we may deprecate and remove the dimse networking if it doesn’t work well and ends up as a distraction.  I’ve always been a bit reluctant to encourage the use of slicer’s dimse code with clinical equipment given the challenges.</p>
<p>Looking ahead, at least for my own work, I’m more interested in making <a href="https://en.wikipedia.org/wiki/DICOMweb" rel="nofollow noopener">DICOMweb</a> interfaces work well.  I know dimse is still the global standard in the clinic, but DICOMweb has several advantages, not least of which is that it’s easier to interface with.  And of course Slicer is a research tool first and foremost.</p>
<p>I’ve added a link to this thread to the <a href="https://www.slicer.org/wiki/Documentation/Labs/Slicer5-roadmap#Additional_proposed_changes_to_be_discussed" rel="nofollow noopener">Slicer 5 roadmap page</a> for consideration.</p>

---
