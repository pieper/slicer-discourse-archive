# Access MONAI Label server from 3D Slicer with authentication

**Topic ID**: 36355
**Date**: 2024-05-23
**URL**: https://discourse.slicer.org/t/access-monai-label-server-from-3d-slicer-with-authentication/36355

---

## Post #1 by @vivit98 (2024-05-23 16:21 UTC)

<p>Hi,</p>
<p>I am trying to access the MONAI Label app which is running on an external sever in OpenShift, while 3D Slicer is running locally. To my understanding, once the MONAI Label extension is installed, I should specify the IP and port where the app is on. This is actually the Jupyter Environment inside OpenShift AI, so I must address the URL of the notebook, ask access is being redirected by proxy and the hosts file (locally).</p>
<p>But once I try to connect to the server I get accros an authentication issue, the URL redirects to OpenShift’s Oauth page, so I need to authenticate before accessing the notebook.</p>
<p>Is there any way I could do that from Slicer or the MONAI extension? I have tried with the “<a href="https://user:password@domain" rel="noopener nofollow ugc">https://user:password@domain</a>” method, but it is not working either.</p>
<p>I would appreciate any help.</p>
<p>Thanks in advance!</p>

---
