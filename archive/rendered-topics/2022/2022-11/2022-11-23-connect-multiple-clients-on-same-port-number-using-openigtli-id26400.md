---
topic_id: 26400
title: "Connect Multiple Clients On Same Port Number Using Openigtli"
date: 2022-11-23
url: https://discourse.slicer.org/t/26400
---

# Connect multiple clients on same port number using OpenIGTLink

**Topic ID**: 26400
**Date**: 2022-11-23
**URL**: https://discourse.slicer.org/t/connect-multiple-clients-on-same-port-number-using-openigtlink/26400

---

## Post #1 by @Srijeet_Chatterjee (2022-11-23 08:52 UTC)

<p>Hello,</p>
<p>I want to connect and stream images from an OpenIGTLink Server(sample server codes) to Slicer(streaming images) as well as a PyIgtl-client(for some preprocessing) on the same port number.</p>
<p>Can anyone please help me with this setup?</p>
<p>Thanks,<br>
Best Regards,<br>
Srijeet</p>

---

## Post #2 by @pll_llq (2022-11-23 21:33 UTC)

<p>If I understood your case correctly the servers should either be on different IPs or on different ports</p>

---

## Post #3 by @Srijeet_Chatterjee (2022-11-23 21:38 UTC)

<p>However, if using a Plus Server it works fine, If I am connecting to two different clients on same IP and same ports. I have created a server using OpenIGTlink sample server codes. But it doesn’t connect to two different clients at the same time.</p>
<p>I want to know, how can I enable this feature or is there something I am missing!</p>

---

## Post #4 by @pll_llq (2022-11-23 21:55 UTC)

<p>Sorry didn’t understand that you are trying to connect 2 different clients to the same server</p>

---

## Post #5 by @lassoan (2022-11-23 22:42 UTC)

<p>Both PlusServer and Slicer (with the connection in “server” mode) can send data to any number of clients, such as Slicer (with the connection in client mode) and pyigtl client. I’ve just tested this between 3 Slicer instances (one in server mode, two in client mode, all using the same port) and it worked well.</p>
<p>Limitations:</p>
<ul>
<li>I don’t think I’ve made pyigtl server able to handle multiple client connections. Once a client is connected, it does not accept new connections until that first client disconnects.</li>
<li>If a client stalls (keeps the connection open but does not consume the data) then it may block the server (until the client disconnects or starts communicating).</li>
</ul>

---

## Post #6 by @Srijeet_Chatterjee (2022-11-23 23:05 UTC)

<p>Thanks, you are absolutely correct.</p>
<p>The server I am using is not Pyigtl server, the server is built using the OpenIGTLink server i.e C++ code. (Limitation 2:  is observed with the Pyigtl server though)</p>
<p>Now my question is what exact changes do I need there, such that it can handle multiple clients (Just like the plus server for e.g). That would help a lot! thanks again <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @lassoan (2022-11-24 00:52 UTC)

<p>If you don’t want to implement a new server that can handle multiple clients then you can use PlusServer or Slicer as server. Both these servers can accept messages from another server (that cannot handle multiple clients) and broadcast the message to multiple clients.</p>

---
