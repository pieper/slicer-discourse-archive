# Python interpreter encountered a "no OPENSSL_Applink" error

**Topic ID**: 38135
**Date**: 2024-08-30
**URL**: https://discourse.slicer.org/t/python-interpreter-encountered-a-no-openssl-applink-error/38135

---

## Post #1 by @hushanwsr (2024-08-30 18:33 UTC)

<p>I am building a project on Windows, and the environment meets the requirements specified in the file. During the build process of most Python-related projects (like <code>python-setuptools</code>, <code>python-pip</code>, <code>python-numpy</code>, etc.), the error <code>MSB8066</code> occurs. In the error logs for <code>python-setuptools-install-err.txt</code> (and other projects), the following message appears: <code>OPENSSL_Uplink(00007FF9F1B53B30,08): no OPENSSL_Applink</code>.</p>
<p>I tried rebuilding the Python interpreter, but it had no effect. The OpenSSL project itself did not show any errors. I also removed all other Python environments from my computer, including Anaconda, etc. However, the problem still persists.</p>
<p>Therefore, I am seeking your help here. Thank you very much! As I am just a college student who is new to this field and lack experience, please forgive me if my description is not up to standard.</p>
<p>Regarding the complete build log mentioned in the build document, I did not find it at the following address: <code>&lt;Slicer_BUILD&gt;\Testing\Temporary\LastBuild_&lt;date&gt;-&lt;time&gt;.log</code>. In fact, I don’t know why, but my <code>Temporary</code> folder is empty.</p>
<p>If the description I provided is insufficient, I am very sorry. Please let me know what additional information I need to provide.</p>

---

## Post #2 by @lassoan (2024-08-30 18:36 UTC)

<p>Most likely some application dropped OpenSSL binaries in some system location. You can use sxstrace or maybe dependency walker to find the offending dll. See instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start">here</a>.</p>

---

## Post #3 by @hushanwsr (2024-08-31 14:50 UTC)

<p>Thank you for your help; I have resolved the issue mentioned earlier. <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>
<p>I believe this problem arose because I had been studying cybersecurity and was using tools like Burp Suite, Wireshark, Acunetix, and other similar software for network packet capturing or related activities. It seems that one of these tools made some modifications to OpenSSL, which caused the issue I encountered.</p>
<p>I tried uninstalling these tools, but the uninstallation wasn’t thorough. Given that my technical skills aren’t very strong, I didn’t fully understand the guide you provided or may have made some mistakes during the process. In the end, I decided to restore my computer to factory settings <img src="https://emoji.discourse-cdn.com/twitter/sneezing_face.png?v=12" title=":sneezing_face:" class="emoji" alt=":sneezing_face:" loading="lazy" width="20" height="20">, which directly resolved all the problems. <img src="https://emoji.discourse-cdn.com/twitter/kissing_heart.png?v=12" title=":kissing_heart:" class="emoji" alt=":kissing_heart:" loading="lazy" width="20" height="20"></p>
<p>If anyone else experiencing a similar issue reads this, they should first consider whether, like me, they have been using some cybersecurity or hacking-related software. If you’re not very technically skilled, I would suggest restoring your system to factory settings as it may be more convenient. Some of these tools modify low-level information, which might not be easy to correct directly.</p>
<p>Finally, thank you again for your help. I wish you success in your work and happiness in your life! <img src="https://emoji.discourse-cdn.com/twitter/kissing_heart.png?v=12" title=":kissing_heart:" class="emoji" alt=":kissing_heart:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/kissing_heart.png?v=12" title=":kissing_heart:" class="emoji" alt=":kissing_heart:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/kissing_heart.png?v=12" title=":kissing_heart:" class="emoji" alt=":kissing_heart:" loading="lazy" width="20" height="20"></p>

---
