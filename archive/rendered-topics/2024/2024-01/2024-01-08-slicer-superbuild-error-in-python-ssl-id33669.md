# Slicer superbuild error in Python/SSL

**Topic ID**: 33669
**Date**: 2024-01-08
**URL**: https://discourse.slicer.org/t/slicer-superbuild-error-in-python-ssl/33669

---

## Post #1 by @cpinter (2024-01-08 12:49 UTC)

<p>Hi all,</p>
<p>I have updated the Slicer source code to the latest and trying to build it. On one computer the build succeeded, but on the other one I keep getting the same error. I tried it several times during the last days at the latest commit so it is not something very recent.</p>
<p>The error is:</p>
<pre><code class="lang-auto">  CMake Error at C:/d/S5R/python-setuptools-prefix/src/python-setuptools-stamp/python-setuptools-install-Release.cmake:49 (message):
    Command failed: 1
     'C:/d/S5R/python-install/bin/PythonSlicer.exe' '-m' 'pip' 'install' '--require-hashes' '-r' 'C:/d/S5R/python-setuptools-requirements.txt'
    See also
      C:/d/S5R/python-setuptools-prefix/src/python-setuptools-stamp/python-setuptools-install-*.log
</code></pre>
<p>and in the referred file I have this:</p>
<pre><code class="lang-auto">  WARNING: Certificate did not match expected hostname: files.pythonhosted.org. Certificate: {'subject': ((('commonName', 'r.shared-319-default.ssl.fastly.net'),),), 'issuer': ((('countryName', 'BE'),), (('organizationName', 'GlobalSign nv-sa'),), (('commonName', 'GlobalSign Atlas R3 DV TLS CA 2023 Q1'),)), 'version': 3, 'serialNumber': '01D06257899F0DD2481ECE65A0533F7E', 'notBefore': 'Apr 10 04:55:11 2023 GMT', 'notAfter': 'May 11 04:55:10 2024 GMT', 'subjectAltName': (('DNS', 'r.shared-319-default.ssl.fastly.net'),), 'OCSP': ('http://ocsp.globalsign.com/ca/gsatlasr3dvtlsca2023q1',), 'caIssuers': ('http://secure.globalsign.com/cacert/gsatlasr3dvtlsca2023q1.crt',), 'crlDistributionPoints': ('http://crl.globalsign.com/ca/gsatlasr3dvtlsca2023q1.crl',)}
  WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError("hostname 'files.pythonhosted.org' doesn't match 'r.shared-319-default.ssl.fastly.net'"))': /packages/bb/26/7945080113158354380a12ce26873dd6c1ebd88d47f5bc24e2c5bb38c16a/setuptools-68.2.2-py3-none-any.whl
  WARNING: Certificate did not match expected hostname: files.pythonhosted.org. Certificate: {'subject': ((('commonName', 'r.shared-319-default.ssl.fastly.net'),),), 'issuer': ((('countryName', 'BE'),), (('organizationName', 'GlobalSign nv-sa'),), (('commonName', 'GlobalSign Atlas R3 DV TLS CA 2023 Q1'),)), 'version': 3, 'serialNumber': '01D06257899F0DD2481ECE65A0533F7E', 'notBefore': 'Apr 10 04:55:11 2023 GMT', 'notAfter': 'May 11 04:55:10 2024 GMT', 'subjectAltName': (('DNS', 'r.shared-319-default.ssl.fastly.net'),), 'OCSP': ('http://ocsp.globalsign.com/ca/gsatlasr3dvtlsca2023q1',), 'caIssuers': ('http://secure.globalsign.com/cacert/gsatlasr3dvtlsca2023q1.crt',), 'crlDistributionPoints': ('http://crl.globalsign.com/ca/gsatlasr3dvtlsca2023q1.crl',)}
  WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError("hostname 'files.pythonhosted.org' doesn't match 'r.shared-319-default.ssl.fastly.net'"))': /packages/bb/26/7945080113158354380a12ce26873dd6c1ebd88d47f5bc24e2c5bb38c16a/setuptools-68.2.2-py3-none-any.whl
  WARNING: Certificate did not match expected hostname: files.pythonhosted.org. Certificate: {'subject': ((('commonName', 'r.shared-319-default.ssl.fastly.net'),),), 'issuer': ((('countryName', 'BE'),), (('organizationName', 'GlobalSign nv-sa'),), (('commonName', 'GlobalSign Atlas R3 DV TLS CA 2023 Q1'),)), 'version': 3, 'serialNumber': '01D06257899F0DD2481ECE65A0533F7E', 'notBefore': 'Apr 10 04:55:11 2023 GMT', 'notAfter': 'May 11 04:55:10 2024 GMT', 'subjectAltName': (('DNS', 'r.shared-319-default.ssl.fastly.net'),), 'OCSP': ('http://ocsp.globalsign.com/ca/gsatlasr3dvtlsca2023q1',), 'caIssuers': ('http://secure.globalsign.com/cacert/gsatlasr3dvtlsca2023q1.crt',), 'crlDistributionPoints': ('http://crl.globalsign.com/ca/gsatlasr3dvtlsca2023q1.crl',)}
  WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError("hostname 'files.pythonhosted.org' doesn't match 'r.shared-319-default.ssl.fastly.net'"))': /packages/bb/26/7945080113158354380a12ce26873dd6c1ebd88d47f5bc24e2c5bb38c16a/setuptools-68.2.2-py3-none-any.whl
  WARNING: Certificate did not match expected hostname: files.pythonhosted.org. Certificate: {'subject': ((('commonName', 'r.shared-319-default.ssl.fastly.net'),),), 'issuer': ((('countryName', 'BE'),), (('organizationName', 'GlobalSign nv-sa'),), (('commonName', 'GlobalSign Atlas R3 DV TLS CA 2023 Q1'),)), 'version': 3, 'serialNumber': '01D06257899F0DD2481ECE65A0533F7E', 'notBefore': 'Apr 10 04:55:11 2023 GMT', 'notAfter': 'May 11 04:55:10 2024 GMT', 'subjectAltName': (('DNS', 'r.shared-319-default.ssl.fastly.net'),), 'OCSP': ('http://ocsp.globalsign.com/ca/gsatlasr3dvtlsca2023q1',), 'caIssuers': ('http://secure.globalsign.com/cacert/gsatlasr3dvtlsca2023q1.crt',), 'crlDistributionPoints': ('http://crl.globalsign.com/ca/gsatlasr3dvtlsca2023q1.crl',)}
  WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError("hostname 'files.pythonhosted.org' doesn't match 'r.shared-319-default.ssl.fastly.net'"))': /packages/bb/26/7945080113158354380a12ce26873dd6c1ebd88d47f5bc24e2c5bb38c16a/setuptools-68.2.2-py3-none-any.whl
  WARNING: Certificate did not match expected hostname: files.pythonhosted.org. Certificate: {'subject': ((('commonName', 'r.shared-319-default.ssl.fastly.net'),),), 'issuer': ((('countryName', 'BE'),), (('organizationName', 'GlobalSign nv-sa'),), (('commonName', 'GlobalSign Atlas R3 DV TLS CA 2023 Q1'),)), 'version': 3, 'serialNumber': '01D06257899F0DD2481ECE65A0533F7E', 'notBefore': 'Apr 10 04:55:11 2023 GMT', 'notAfter': 'May 11 04:55:10 2024 GMT', 'subjectAltName': (('DNS', 'r.shared-319-default.ssl.fastly.net'),), 'OCSP': ('http://ocsp.globalsign.com/ca/gsatlasr3dvtlsca2023q1',), 'caIssuers': ('http://secure.globalsign.com/cacert/gsatlasr3dvtlsca2023q1.crt',), 'crlDistributionPoints': ('http://crl.globalsign.com/ca/gsatlasr3dvtlsca2023q1.crl',)}
  WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError("hostname 'files.pythonhosted.org' doesn't match 'r.shared-319-default.ssl.fastly.net'"))': /packages/bb/26/7945080113158354380a12ce26873dd6c1ebd88d47f5bc24e2c5bb38c16a/setuptools-68.2.2-py3-none-any.whl
  WARNING: Certificate did not match expected hostname: files.pythonhosted.org. Certificate: {'subject': ((('commonName', 'r.shared-319-default.ssl.fastly.net'),),), 'issuer': ((('countryName', 'BE'),), (('organizationName', 'GlobalSign nv-sa'),), (('commonName', 'GlobalSign Atlas R3 DV TLS CA 2023 Q1'),)), 'version': 3, 'serialNumber': '01D06257899F0DD2481ECE65A0533F7E', 'notBefore': 'Apr 10 04:55:11 2023 GMT', 'notAfter': 'May 11 04:55:10 2024 GMT', 'subjectAltName': (('DNS', 'r.shared-319-default.ssl.fastly.net'),), 'OCSP': ('http://ocsp.globalsign.com/ca/gsatlasr3dvtlsca2023q1',), 'caIssuers': ('http://secure.globalsign.com/cacert/gsatlasr3dvtlsca2023q1.crt',), 'crlDistributionPoints': ('http://crl.globalsign.com/ca/gsatlasr3dvtlsca2023q1.crl',)}
ERROR: Could not install packages due to an OSError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Max retries exceeded with url: /packages/bb/26/7945080113158354380a12ce26873dd6c1ebd88d47f5bc24e2c5bb38c16a/setuptools-68.2.2-py3-none-any.whl (Caused by SSLError(SSLCertVerificationError("hostname 'files.pythonhosted.org' doesn't match 'r.shared-319-default.ssl.fastly.net'")))

WARNING: You are using pip version 21.2.4; however, version 23.3.2 is available.
You should consider upgrading via the 'C:\d\S5R\python-install\bin\python.exe -m pip install --upgrade pip' command.
</code></pre>
<p>I updated CMake to the latest, and it failed the same way. I do not use any special CMake options with the superbuild. I use VS17 2022, and Qt 5.15.2. The computer is question has Windows 10, and I am trying to build in Release mode.</p>
<p>Does anyone have any suggestion? Thanks a lot!</p>

---

## Post #2 by @jamesobutler (2024-01-08 13:01 UTC)

<p>I build the same configuration and haven’t run into this issue. I last built about 2 weeks ago.</p>
<p>Since it worked on one computer, but not another definitely seems to point to a network issue for that one computer. Is it connected to a VPN or behind some corporate firewall? Anything else about that computer’s networking capabilities compared to the one that works?</p>

---

## Post #3 by @cpinter (2024-01-08 13:15 UTC)

<p>Thanks James! It is not behind firewall or VPN. It has a wired connection to the internet and since I tried to build it around 5 times and the superbuild needs to check out many GitHub repos etc, and it always failed the same place, I am quite certain it’s not about the connection. I can build older Slicer and custom app on the same computer.</p>
<p>If I had to guess I’d say it must be something in the requirements that changed in the past few months.</p>

---

## Post #4 by @jamesobutler (2024-01-08 15:08 UTC)

<p>Is the computer that is having problems able to go to <a href="https://files.pythonhosted.org/" rel="noopener nofollow ugc">https://files.pythonhosted.org/</a> successfully through a browser?</p>
<p>Doing a google search of the error you encounter brought me to the following page with the same description and another user provided a method of how they resolved it:</p>
<aside class="onebox stackexchange" data-onebox-src="https://stackoverflow.com/questions/77630264/could-not-install-packages-due-to-an-oserror-while-trying-to-download-python-p">
  <header class="source">

      <a href="https://stackoverflow.com/questions/77630264/could-not-install-packages-due-to-an-oserror-while-trying-to-download-python-p" target="_blank" rel="noopener nofollow ugc">stackoverflow.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/17129870/bushra" target="_blank" rel="noopener nofollow ugc">
    <img alt="Bushra" src="https://lh3.googleusercontent.com/a-/AOh14GhWb914A43KAuRuS6nkEoCHOb54LBXdNxrX9AYPIA=k-s256" class="thumbnail onebox-avatar" width="256" height="256">
  </a>

<h4>
  <a href="https://stackoverflow.com/questions/77630264/could-not-install-packages-due-to-an-oserror-while-trying-to-download-python-p" target="_blank" rel="noopener nofollow ugc">"Could not install packages due to an OSError" while trying to download python packages</a>
</h4>

<div class="tags">
  <strong>python, pip, ssl-certificate, pypi</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://stackoverflow.com/users/17129870/bushra" target="_blank" rel="noopener nofollow ugc">
    Bushra
  </a>
  on <a href="https://stackoverflow.com/questions/77630264/could-not-install-packages-due-to-an-oserror-while-trying-to-download-python-p" target="_blank" rel="noopener nofollow ugc">05:38AM - 09 Dec 23 UTC</a>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @cpinter (2024-01-08 15:45 UTC)

<p>Thanks again.</p>
<p><a href="https://files.pythonhosted.org/">https://files.pythonhosted.org/</a> is available from the computer where build was successful but not on the computer where it kept failing (getting a “Your connection is not private” error).</p>
<p>I’ll try the method you pointed out on stackoverflow.</p>

---

## Post #6 by @cpinter (2024-01-08 19:42 UTC)

<p>The build is proceeding, and I got a “Completed ‘python-setuptools’” message in CMake, so it seems to be working. I just realize the computer wasn’t restarted for months so either that was the problem, or the <a href="https://stackoverflow.com/questions/77630264/could-not-install-packages-due-to-an-oserror-while-trying-to-download-python-p">solution</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> suggested did the trick.</p>
<p>Thanks a lot for the quick help!</p>

---
