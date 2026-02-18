# Slicer.org is down - invalid certification date

**Topic ID**: 28747
**Date**: 2023-04-04
**URL**: https://discourse.slicer.org/t/slicer-org-is-down-invalid-certification-date/28747

---

## Post #1 by @lassoan (2023-04-04 13:23 UTC)

<p>Starting this morning, <a href="http://slicer.org">slicer.org</a> is no longer accessible. It shows this error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eec22504ab125917f0291ba83a6a7109c08b995f.png" data-download-href="/uploads/short-url/y49ADgk6odNFf7Cva2Bga6A5nOf.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eec22504ab125917f0291ba83a6a7109c08b995f_2_690x440.png" alt="image" data-base62-sha1="y49ADgk6odNFf7Cva2Bga6A5nOf" width="690" height="440" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eec22504ab125917f0291ba83a6a7109c08b995f_2_690x440.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eec22504ab125917f0291ba83a6a7109c08b995f_2_1035x660.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eec22504ab125917f0291ba83a6a7109c08b995f.png 2x" data-dominant-color="323132"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1174×749 24.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Even if I click on “Advanced”, I just get some more details:</p>
<blockquote>
<p><a href="http://www.slicer.org">www.slicer.org</a> uses encryption to protect your information. When Microsoft Edge tried to connect to <a href="http://www.slicer.org">www.slicer.org</a> this time, the website sent back unusual and incorrect credentials. This may happen when an attacker is trying to pretend to be <a href="http://www.slicer.org">www.slicer.org</a>, or a WiFi sign-in screen has interrupted the connection. Your information is still secure because Microsoft Edge stopped the connection before any data was exchanged.</p>
<p>You can’t visit <a href="http://www.slicer.org">www.slicer.org</a> at the moment because the website uses HSTS. Network errors and attacks are usually temporary, so this page will probably work later.</p>
</blockquote>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jcfr">@jcfr</a> could you investigate?</p>

---

## Post #2 by @Sam_Horvath (2023-04-04 13:47 UTC)

<p>I am looking into it!</p>
<p>For anyone looking for Slicer resources, <a href="https://download.slicer.org/">the download site</a> and the <a href="https://slicer.readthedocs.io/en/latest/">documentation</a> are still available.</p>

---

## Post #3 by @Sam_Horvath (2023-04-04 14:18 UTC)

<p>The issue seems to be specific to the <a href="http://slicer.org">slicer.org</a> domain. The <a href="http://slicer.org">slicer.org</a> page can be accessed at the netlify address here:</p>
<p><a href="https://slicer-org.netlify.app/" class="onebox" target="_blank" rel="noopener">https://slicer-org.netlify.app/</a></p>

---

## Post #4 by @rbumm (2023-04-05 07:42 UTC)

<p>When I click a <a href="https://slicer.org">https://slicer.org</a> link from a google search I still get</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4a3595d1fe899297f7e80bf5245d43f4f3cade1.png" data-download-href="/uploads/short-url/pLZUWzR9UVoAArgHAAWaOh5bBoB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4a3595d1fe899297f7e80bf5245d43f4f3cade1.png" alt="image" data-base62-sha1="pLZUWzR9UVoAArgHAAWaOh5bBoB" width="690" height="473" data-dominant-color="FAFAFC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">977×671 16 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>with</p>
<pre><code class="lang-auto">NET::ERR_CERT_DATE_INVALID
Subject: wiki.slicer.org

Issuer: R3

Expires on: 03.04.2023

Current date: 05.04.2023

PEM encoded chain:
-----BEGIN CERTIFICATE-----
MIIFrjCCBJagAwIBAgISBFWDC+V2Ln0wVapjogmIxZjyMA0GCSqGSIb3DQEBCwUA
MDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQD
EwJSMzAeFw0yMzAxMDMyMTIyMDdaFw0yMzA0MDMyMTIyMDZaMBoxGDAWBgNVBAMT
D3dpa2kuc2xpY2VyLm9yZzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
AMYqSdoh9FAU6q7VsKDGJT+BpQnSmNBS7TXKx8HPwH/Cp3q1wSCDQ2m3WE7Vg95C
bCl+XCZTsA44Sprmp0YRv+OKUIwmJTIUbbbzFIddJwjiaDh68dgd4EaZBJV6EOLW
w6dTpKDG9j0jWQyLR27cwp70DaV9xLG+CtcXJSLun9/N2J6SWSVHyo78tUvt5TTg
M8mcJARmMKcT58PY0UYdPRPRlHoBRO0y7DedxRSoZWOxewULvrgotKgF28SEpwnW
ilLXPBq/u3Of1ZXxPhA2wdSlpT2RPuqSLmfP+wPFf7y9mKjG5tJ+vj5wAvSI8PfY
//XACRBGgCDGvmEX/Ph/mSMCAwEAAaOCAtQwggLQMA4GA1UdDwEB/wQEAwIFoDAd
BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDAYDVR0TAQH/BAIwADAdBgNV
HQ4EFgQU4vcaG6BsORWRUIEHHjkr4Be+cuIwHwYDVR0jBBgwFoAUFC6zF7dYVsuu
UAlA5h+vnYsUwsYwVQYIKwYBBQUHAQEESTBHMCEGCCsGAQUFBzABhhVodHRwOi8v
cjMuby5sZW5jci5vcmcwIgYIKwYBBQUHMAKGFmh0dHA6Ly9yMy5pLmxlbmNyLm9y
Zy8wgaIGA1UdEQSBmjCBl4IRaXNzdWVzLnNsaWNlci5vcmeCGG1hbnRpc2FyY2hp
dmUuc2xpY2VyLm9yZ4IKbmEtbWljLm9yZ4IKc2xpY2VyLm9yZ4IPd2lraS5uYS1t
aWMub3Jngg53aWtpLm5jaWd0Lm9yZ4IPd2lraS5zbGljZXIub3Jngg53d3cubmEt
bWljLm9yZ4IOd3d3LnNsaWNlci5vcmcwTAYDVR0gBEUwQzAIBgZngQwBAgEwNwYL
KwYBBAGC3xMBAQEwKDAmBggrBgEFBQcCARYaaHR0cDovL2Nwcy5sZXRzZW5jcnlw
dC5vcmcwggEFBgorBgEEAdZ5AgQCBIH2BIHzAPEAdwBvU3asMfAxGdiZAKRRFf93
FRwR2QLBACkGjbIImjfZEwAAAYV5ukKnAAAEAwBIMEYCIQCHFOp/Ttq+bwV3bPAm
bwlb4lB7A17+z8rFU1YMjkTnlQIhAKG19YSEXasxqynqZkM6owcpKqZtE5p7T3I7
OZKSIddxAHYA6D7Q2j71BjUy51covIlryQPTy9ERa+zraeF3fW0GvW4AAAGFebpC
YQAABAMARzBFAiBhLVaEkXMZRJI/2I93Ka7axbEqjonwGnwQDVqjPEn5YQIhALqE
DAFXf1aq9cqbM2kDJljg5IsaKNfa4odSEah0vRdPMA0GCSqGSIb3DQEBCwUAA4IB
AQA4/pYVMjyBc/48fQZdZMMiB2grrQN9kEF9NMb2UljGnhPB94tDPF1AGV6PJpC3
JuYFAtz6zil68qyGiLuZ3DvhkwkVHen+pVzzMRI3w/vPk8q75mYCWsdUZnPF92b8
EutX5ceGZienMwUEWtRRRGj8xiCg7gN37i/yNs2qNI8IW9QbRUxVEHGWk2ToavPm
wAYp8PiR9Z7Im4RFYri6I+vWI9Ii68W3NcRoHnmxeSc1vpOJIAMBFVDzbOynjSZI
YWJrnHslG3xv1KqEe2gJ7YB6/SHeYSwPxuuHeJ72AyDWvjzWn2B0dr7AEJmX5b9g
6Vl1KNsrfNxH2l4cz0lMEI0t
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIFFjCCAv6gAwIBAgIRAJErCErPDBinU/bWLiWnX1owDQYJKoZIhvcNAQELBQAw
TzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh
cmNoIEdyb3VwMRUwEwYDVQQDEwxJU1JHIFJvb3QgWDEwHhcNMjAwOTA0MDAwMDAw
WhcNMjUwOTE1MTYwMDAwWjAyMQswCQYDVQQGEwJVUzEWMBQGA1UEChMNTGV0J3Mg
RW5jcnlwdDELMAkGA1UEAxMCUjMwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
AoIBAQC7AhUozPaglNMPEuyNVZLD+ILxmaZ6QoinXSaqtSu5xUyxr45r+XXIo9cP
R5QUVTVXjJ6oojkZ9YI8QqlObvU7wy7bjcCwXPNZOOftz2nwWgsbvsCUJCWH+jdx
sxPnHKzhm+/b5DtFUkWWqcFTzjTIUu61ru2P3mBw4qVUq7ZtDpelQDRrK9O8Zutm
NHz6a4uPVymZ+DAXXbpyb/uBxa3Shlg9F8fnCbvxK/eG3MHacV3URuPMrSXBiLxg
Z3Vms/EY96Jc5lP/Ooi2R6X/ExjqmAl3P51T+c8B5fWmcBcUr2Ok/5mzk53cU6cG
/kiFHaFpriV1uxPMUgP17VGhi9sVAgMBAAGjggEIMIIBBDAOBgNVHQ8BAf8EBAMC
AYYwHQYDVR0lBBYwFAYIKwYBBQUHAwIGCCsGAQUFBwMBMBIGA1UdEwEB/wQIMAYB
Af8CAQAwHQYDVR0OBBYEFBQusxe3WFbLrlAJQOYfr52LFMLGMB8GA1UdIwQYMBaA
FHm0WeZ7tuXkAXOACIjIGlj26ZtuMDIGCCsGAQUFBwEBBCYwJDAiBggrBgEFBQcw
AoYWaHR0cDovL3gxLmkubGVuY3Iub3JnLzAnBgNVHR8EIDAeMBygGqAYhhZodHRw
Oi8veDEuYy5sZW5jci5vcmcvMCIGA1UdIAQbMBkwCAYGZ4EMAQIBMA0GCysGAQQB
gt8TAQEBMA0GCSqGSIb3DQEBCwUAA4ICAQCFyk5HPqP3hUSFvNVneLKYY611TR6W
PTNlclQtgaDqw+34IL9fzLdwALduO/ZelN7kIJ+m74uyA+eitRY8kc607TkC53wl
ikfmZW4/RvTZ8M6UK+5UzhK8jCdLuMGYL6KvzXGRSgi3yLgjewQtCPkIVz6D2QQz
CkcheAmCJ8MqyJu5zlzyZMjAvnnAT45tRAxekrsu94sQ4egdRCnbWSDtY7kh+BIm
lJNXoB1lBMEKIq4QDUOXoRgffuDghje1WrG9ML+Hbisq/yFOGwXD9RiX8F6sw6W4
avAuvDszue5L3sz85K+EC4Y/wFVDNvZo4TYXao6Z0f+lQKc0t8DQYzk1OXVu8rp2
yJMC6alLbBfODALZvYH7n7do1AZls4I9d1P4jnkDrQoxB3UqQ9hVl3LEKQ73xF1O
yK5GhDDX8oVfGKF5u+decIsH4YaTw7mP3GFxJSqv3+0lUFJoi5Lc5da149p90Ids
hCExroL1+7mryIkXPeFM5TgO9r0rvZaBFOvV2z0gp35Z0+L4WPlbuEjN/lxPFin+
HlUjr8gRsI3qfJOQFy/9rKIJR0Y/8Omwt/8oTWgy1mdeHmmjk7j1nYsvC9JSQ6Zv
MldlTTKB3zhThV1+XWYp6rjd5JW1zbVWEkLNxE7GJThEUG3szgBVGP7pSWTUTsqX
nLRbwHOoq7hHwg==
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIFazCCA1OgAwIBAgIRAIIQz7DSQONZRGPgu2OCiwAwDQYJKoZIhvcNAQELBQAw
TzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh
cmNoIEdyb3VwMRUwEwYDVQQDEwxJU1JHIFJvb3QgWDEwHhcNMTUwNjA0MTEwNDM4
WhcNMzUwNjA0MTEwNDM4WjBPMQswCQYDVQQGEwJVUzEpMCcGA1UEChMgSW50ZXJu
ZXQgU2VjdXJpdHkgUmVzZWFyY2ggR3JvdXAxFTATBgNVBAMTDElTUkcgUm9vdCBY
MTCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAK3oJHP0FDfzm54rVygc
h77ct984kIxuPOZXoHj3dcKi/vVqbvYATyjb3miGbESTtrFj/RQSa78f0uoxmyF+
0TM8ukj13Xnfs7j/EvEhmkvBioZxaUpmZmyPfjxwv60pIgbz5MDmgK7iS4+3mX6U
A5/TR5d8mUgjU+g4rk8Kb4Mu0UlXjIB0ttov0DiNewNwIRt18jA8+o+u3dpjq+sW
T8KOEUt+zwvo/7V3LvSye0rgTBIlDHCNAymg4VMk7BPZ7hm/ELNKjD+Jo2FR3qyH
B5T0Y3HsLuJvW5iB4YlcNHlsdu87kGJ55tukmi8mxdAQ4Q7e2RCOFvu396j3x+UC
B5iPNgiV5+I3lg02dZ77DnKxHZu8A/lJBdiB3QW0KtZB6awBdpUKD9jf1b0SHzUv
KBds0pjBqAlkd25HN7rOrFleaJ1/ctaJxQZBKT5ZPt0m9STJEadao0xAH0ahmbWn
OlFuhjuefXKnEgV4We0+UXgVCwOPjdAvBbI+e0ocS3MFEvzG6uBQE3xDk3SzynTn
jh8BCNAw1FtxNrQHusEwMFxIt4I7mKZ9YIqioymCzLq9gwQbooMDQaHWBfEbwrbw
qHyGO0aoSCqI3Haadr8faqU9GY/rOPNk3sgrDQoo//fb4hVC1CLQJ13hef4Y53CI
rU7m2Ys6xt0nUW7/vGT1M0NPAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNV
HRMBAf8EBTADAQH/MB0GA1UdDgQWBBR5tFnme7bl5AFzgAiIyBpY9umbbjANBgkq
hkiG9w0BAQsFAAOCAgEAVR9YqbyyqFDQDLHYGmkgJykIrGF1XIpu+ILlaS/V9lZL
ubhzEFnTIZd+50xx+7LSYK05qAvqFyFWhfFQDlnrzuBZ6brJFe+GnY+EgPbk6ZGQ
3BebYhtF8GaV0nxvwuo77x/Py9auJ/GpsMiu/X1+mvoiBOv/2X/qkSsisRcOj/KK
NFtY2PwByVS5uCbMiogziUwthDyC3+6WVwW6LLv3xLfHTjuCvjHIInNzktHCgKQ5
ORAzI4JMPJ+GslWYHb4phowim57iaztXOoJwTdwJx4nLCgdNbOhdjsnvzqvHu7Ur
TkXWStAmzOVyyghqpZXjFaH3pO3JLF+l+/+sKAIuvtd7u+Nxe5AW0wdeRlN8NwdC
jNPElpzVmbUq4JUagEiuTDkHzsxHpFKVK7q4+63SM1N95R1NbdWhscdCb+ZAJzVc
oyi3B43njTOQ5yOf+1CceWxG1bQVs5ZufpsMljq4Ui0/1lvh+wjChP4kqKOJ2qxq
4RgqsahDYVvTH9w7jXbyLeiNdd8XM2w9U/t7y0Ff/9yi0GE44Za4rF2LN9d11TPA
mRGunUHBcnWEvgJBQl9nJEiU0Zsnvgc/ubhPgXRR4Xq37Z0j4r7g1SgEEzwxA57d
emyPxgcYxn/eR44/KJ4EBs+lVDR3veyJm+kXQ99b21/+jh5Xos1AnX5iItreGCc=
-----END CERTIFICATE-----

Certificate Transparency:

SCT Sectigo 'Mammoth' CT log (Embedded in certificate, Verified)

SCT Google 'Argon2023' log (Embedded in certificate, Verified)

Schalte für größtmögliche Sicherheit in Chrome das erweiterte Safe Browsing ein
</code></pre>

---

## Post #5 by @Sam_Horvath (2023-04-05 14:14 UTC)

<p>Yep. it is still down. We are working on addressing the certificate issue.</p>

---

## Post #6 by @Sam_Horvath (2023-04-05 14:20 UTC)

<p>The certificate issue only affects sites in the <code>slicer.org</code> domain, so the main website and the wiki.  Everything else should still be accessible.  The main public resource that is still only on the wiki is the Trainings page.</p>

---

## Post #7 by @Sam_Horvath (2023-04-05 19:11 UTC)

<p>Should be back up now!</p>

---

## Post #8 by @lassoan (2023-04-05 19:51 UTC)

<p>Thank you, it all looks good now!</p>

---

## Post #9 by @jcfr (2023-04-05 20:15 UTC)

<h3><a name="p-93119-summary-of-the-incident-1" class="anchor" href="#p-93119-summary-of-the-incident-1" aria-label="Heading link"></a>Summary of the incident</h3>
<p>The following websites are all served from cloud instances on which the automated <code>https</code> certificate renewal process failed:</p>
<pre><code class="lang-auto">issues.slicer.org
mantisarchive.slicer.org
na-mic.org
slicer.org
wiki.na-mic.org
wiki.ncigt.org
wiki.slicer.org
www.na-mic.org
www.slicer.org
</code></pre>
<p>The renewal failure was likely due to the root certificate changes described <a href="https://docs.certifytheweb.com/docs/kb/kb-202109-letsencrypt/">here</a>. Following this change, the tooling available on the instance probably needed to be updated.</p>
<h3><a name="p-93119-mitigation-2" class="anchor" href="#p-93119-mitigation-2" aria-label="Heading link"></a>Mitigation</h3>
<p><strong>Short term:</strong></p>
<p>As a temporary measure, we implemented the following changes:</p>
<ul>
<li>converted our testing instance <code>download-staging.slicer.org</code> to serve the <code>slicer.org</code> landing page</li>
<li>updated DNS accordingly</li>
</ul>
<p><strong>Medium term:</strong></p>
<p>In the next week or two we will further consolidate and will have both the <code>slicer.org</code> landing page and the associated redirects managed by Kitware.</p>
<p>This will ensure the <code>slicer.org</code> instance is monitored and updated along side these instances:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Server</th>
<th>Description</th>
<th>Kitware Hosted</th>
<th>Netlify Hosted</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>download.slicer.org</code></td>
<td>Site allowing to download preview and stable application packages</td>
<td><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></td>
<td></td>
</tr>
<tr>
<td><code>download-staging.slicer.org</code></td>
<td><s>Testing server to help with development of the download site</s> Converted to serve <code>slicer.org</code></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/zap.png?v=15" title=":zap:" class="emoji only-emoji" alt=":zap:" loading="lazy" width="20" height="20"></td>
<td></td>
</tr>
<tr>
<td><code>slicer-packages.kitware.com</code></td>
<td>Slicer packages backend implementing REST API service (built on Girder) for managing Slicer application and extension packages</td>
<td><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></td>
<td></td>
</tr>
<tr>
<td><code>slicer.kitware.com</code></td>
<td>Slicer extensions legacy web application to allow older Slicer releases to install extensions through the extensions manager</td>
<td><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></td>
<td></td>
</tr>
<tr>
<td><code>extension.slicer.org</code></td>
<td>Deployment of the Slicer extensions catalog</td>
<td></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></td>
</tr>
</tbody>
</table>
</div>

---

## Post #10 by @pieper (2023-04-06 14:19 UTC)

<p>Now we are getting 404s on these links:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting</a></p>
<p><a href="https://www.slicer.org/wiki/Slicer3:Python" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Slicer3:Python</a></p>

---

## Post #11 by @jcfr (2023-04-06 17:26 UTC)

<p>The solution we were able to setup only take care  the landing page but many redirect end up being broken.</p>
<p>As hinted above, we are working on transition plan to have the relevant servers managed by Kitware but this will take some time.</p>

---

## Post #12 by @pieper (2023-04-07 13:29 UTC)

<p>Thanks to several dedicated people the issues have been resolved - let’s give them a big round of <img src="https://emoji.discourse-cdn.com/twitter/clap.png?v=12" title=":clap:" class="emoji" alt=":clap:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/clap.png?v=12" title=":clap:" class="emoji" alt=":clap:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/clap.png?v=12" title=":clap:" class="emoji" alt=":clap:" loading="lazy" width="20" height="20"></p>

---

## Post #13 by @freephile (2023-04-07 13:34 UTC)

<p>I just tested those links to confirm they are working now.</p>

---

## Post #14 by @lassoan (2023-07-06 11:56 UTC)

<p>This happened again <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
<p><a href="http://www.slicer.org">www.slicer.org</a> is down</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/freephile">@freephile</a> could you fix this? Thank you!</p>

---

## Post #15 by @jcfr (2023-07-06 13:09 UTC)

<p>We are almost done transitioning.</p>
<p>Certificate should be renewed shortly. Having a look at this particular issue now.</p>
<hr>
<p><em>Background:  We are still in the process of transitioning away from the current Digital Ocean cloud infrastructure. Waiting the final steps are completed, the current certificate will need to be renewed.</em></p>

---

## Post #16 by @jcfr (2023-07-06 15:37 UTC)

<h3><a name="p-97267-update-1" class="anchor" href="#p-97267-update-1" aria-label="Heading link"></a>Update</h3>
<ul>
<li>
<p>Certs have been renewed.</p>
</li>
<li>
<p>Access to the relevant services has been restored.</p>
</li>
</ul>
<h3><a name="p-97267-next-2" class="anchor" href="#p-97267-next-2" aria-label="Heading link"></a>Next</h3>
<p>We are in the process of finalizing the hosting of the Slicer and NA-MIC wiki to static hosting.</p>

---

## Post #17 by @lassoan (2023-07-06 15:51 UTC)

<p>Confirmed that <a href="https://www.slicer.org/">https://www.slicer.org/</a> works again - thank you for the quick fix!</p>

---
