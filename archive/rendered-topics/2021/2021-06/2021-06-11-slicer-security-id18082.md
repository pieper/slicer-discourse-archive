---
topic_id: 18082
title: "Slicer Security"
date: 2021-06-11
url: https://discourse.slicer.org/t/18082
---

# Slicer Security

**Topic ID**: 18082
**Date**: 2021-06-11
**URL**: https://discourse.slicer.org/t/slicer-security/18082

---

## Post #1 by @spycolyf (2021-06-11 15:55 UTC)

<p>In light of the recent ransomware incidents, physicians are concerned about the security if Slicer and modules developed using it. Do you have any information on how you protect yourselves from being hacked and the security of Slicer installations?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2021-06-11 20:28 UTC)

<p>There are multiple safeguards in place to ensure that Slicer meet current general expectations for a desktop software that a trusted user runs on his local computer. Slicer’s development and build process is completely transparent. You can inspect the source code, you can inspect the scripts that are used to build the source code. You can see that only minimum set of third-party binaries are used to build Slicer (and you can disable or change those if you have any concerns with any of them). Stable Slicer Release binaries are signed so that you know that the binaries have not been tampered with while on the network server or during downloading. Therefore, the chance that malicious code gets into Slicer packages is very low.</p>
<p>Slicer installs file association for scene files (.mrml, .mrb) and recent Slicer versions also register a custom URL handler, which can launch Slicer when the user requests opening a scene file or a <code>slicer://</code> URL. A handcrafted scene file could make Slicer crash in a way that would then allow arbitrary code execution. However, emailing software and web browsers always warn the user before launching an application, so the application will not be started without the user’s explicit approval.  Also, the code would be limited to what the user can do anyway (it does not require user account control elevation), and Slicer is expected to be run by trusted users. Due to all these, the amount that Slicer increases the attack surface on a computer is negligible - compared to having potentially vulnerable operating system components or very commonly used applications, such as MS Office, PDF reader, or network management tools installed on a computer.</p>
<p>If you wanted to make Slicer available on the public internet then you would need to add additional security layers or isolation from the rest of your network. But this is rarely a problem in practice, because if you work with confidential data then you prevent untrusted user access at much higher levels (e.g., by using a VPN). If you just provide a demo with public data, open to the general public, then you would run Slicer on a completely isolated computer with a non-privileged user.</p>

---
