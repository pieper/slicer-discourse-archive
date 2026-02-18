# _Failed to connect to server 127.0.0.1:4100

**Topic ID**: 15095
**Date**: 2020-12-16
**URL**: https://discourse.slicer.org/t/failed-to-connect-to-server-127-0-0-1-4100/15095

---

## Post #1 by @DimaLat (2020-12-16 13:34 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11<br>
Expected behavior: Matlab bridge executes Matlab properly<br>
Actual behavior: There is an error calling Matlab</p>
<p>Debug: In D:\D\P\S-0-E-b\SlicerOpenIGTLink-build\OpenIGTLink\Source\igtlClientSocket.cxx, line 67<br>
igtl::ClientSocket(0000028AAE0E1B30):<br>
Failed to connect to server 127.0.0.1:4100</p>
<p>Waiting for Matlab startup … 59sec<br>
ERROR: Cannot connect to the server</p>
<p>I’ve tried this one:<br>
<em>netsh firewall add portopening tcp 4100 MatlabBridge</em><br>
and it still not work<br>
Then i tried a new one like:<br>
<em>netsh advfirewall firewall add rule name=“MatlabBridge” dir=in action=allow protocol=TCP localport=4100</em><br>
and it is not help.<br>
Please help, may be somebody know the sollution of this error?</p>

---

## Post #2 by @Mehri_Mehrnia (2022-05-30 01:15 UTC)

<p>the port is blocked by firewall probably. after I changed the Windows I got the same issue.</p>

---
