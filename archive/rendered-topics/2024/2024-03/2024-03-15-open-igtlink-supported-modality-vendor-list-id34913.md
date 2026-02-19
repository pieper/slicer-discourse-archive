---
topic_id: 34913
title: "Open Igtlink Supported Modality Vendor List"
date: 2024-03-15
url: https://discourse.slicer.org/t/34913
---

# (Open)IGTlink supported modality vendor list

**Topic ID**: 34913
**Date**: 2024-03-15
**URL**: https://discourse.slicer.org/t/open-igtlink-supported-modality-vendor-list/34913

---

## Post #1 by @jde (2024-03-15 15:46 UTC)

<p>Hi,<br>
is there an uptodate list of hardware vendors that support OpenIGTlink?<br>
(I’d ask this on OpenIGTlink but it looks like the project itself is no longer alive, or at least the contact page is a dead link)</p>
<p><strong>I’m looking for a standard that would allow real-time data acquisition from interventional modalities</strong></p>
<p>the ref mentioned in the slicer docs, looked promising but  PLUS seems rather old (and ultrasound/video focussed)</p>
<ul>
<li>OpenIGTLink extension:
<ul>
<li><strong>PLUS toolkit configuration file</strong> (.plus.xml): configuration file for real-time data acquisition from imaging and tracking devices and various sensors</li>
</ul>
</li>
</ul>
<p>Do any of the large (x-ray) modality vendors (GE, Philips, Siemens, Canon…) or maybe more specialised vendors (e.g. for ultrasound: Abbott, Boston scientific) support IGTlink?</p>
<p>Any pointers in the right direction much appreciated,<br>
thanks!</p>

---

## Post #2 by @lassoan (2024-03-17 01:32 UTC)

<p>OpenIGTLink is very actively used and maintained. It is a mature project, so not much changes are needed anymore.</p>
<p>Please provide link to the page that contains outdated information and we’ll fix it.</p>
<p>Most vendors (if they let third party access at all) tightly control who can get access to their devices and what they are allowed to do with it. Therefore their goal is not interoperality but tight control and optimal performance with only their system, As a result, each vendor provide its own proprietary interface and only a very few supports for open standard interfaces (e.g, Medtronic surgical navigation systems and some Siemens MRIs support OpenIGTLink). Instead, we build bridges between proprietary interfaces and OpenIGTLink. This allows building systems that work with a wide range of hardware with a single, standard, open interface.</p>
<p>If you are interested in interfacing with a certain device or certain type of devices then we can provide more specific information.</p>

---

## Post #3 by @jde (2024-03-18 09:01 UTC)

<p>Hi Andras,<br>
thanks for the follow-up. I understand the reasons behind a proprietary interface, hence my question. The way I read your reply is: most/some(?) vendors <strong>do</strong> offer an integration path but most vendors do so via a proprietary interface (rather than through a standard one). And then you build an IGT-bridge.</p>
<p>How long does this typically take, how open are OEMs to this development - e.g. it’s just a matter of asking for the API spec, or it’s a reverse engineering job - how long does an integration typically take? Or is it really only a minority that’s open. (and your better of just using a frame grabber).</p>
<p>I’m really trying to understand how “open” the market/vendors really are, 50/50 or 10/90…  Things I’ve been looking at:</p>
<pre><code class="lang-auto">https://www.leica-microsystems.com/products/surgical-microscopes/p/arveo-8/
https://www.cardiovascular.abbott/int/en/hcp/products/percutaneous-coronary-intervention/intravascular-imaging/optis-imaging-systems/about.html
https://www.siemens-healthineers.com/en-us/angio/options-and-upgrades/clinical-software-applications/ivusmap
https://www.usa.philips.com/healthcare/education-resources/technologies/igt/intravascular-ultrasound-ivus
</code></pre>
<p>(sorry I cannot post more than 3 links it seems)<br>
But really, these are just samples I’m trying to understand the broader picture here.</p>
<p>Thanks!</p>
<p>As for the links/info:</p>
<pre><code class="lang-auto">https://openigtlink.org/contact - points to a 404 (and your certificate is invalid)
tutorial/doc refs point to https://www.slicer.org/w/index.php/Documentation/4.2/Training#OpenIGTLink the openIGTlink (apr2012 - is the only reference) failed to load pdf (and i think latest is 4.10?)
https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html
only references the PLUS toolkit (no link) 
Google then leads me to this PLUS page with vendor references
http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Configuration.html
</code></pre>
<p>so all in all it’s not that easy to find a list of actively supported bridges for openigtlink (barring going through the docs of each project using it Slicer, Plus,…)</p>

---
