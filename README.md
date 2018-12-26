# Codebug_BTC_RealTime_Price


A Python script for Codebug that which exploits the Coindesk and Bitstamp API (V2 and v2)  
to display the price of Bitcoins in real time on the codebug led display

![Alt text](https://raw.githubusercontent.com/JonnyBanana/Codebug_Led_Animations/master/IMG/cb.jpg) 

I created two simple Python scripts that use the Coindesk (v1) and Bitstamp (v2) APIs respectively
Both require the tether_codebug firmware:https://github.com/codebugtools/codebug_tether
, which you can find in the "firmware" folder.
Guide to install the tethering firmware with Codebug: 

http://www.codebug.org.uk/learn/activity/66/tethering-codebug-with-python/

Guide Codebug Tether: 

https://codebug-tether.readthedocs.io/en/latest/

Have also a pdf in the "doc" folder.

In addition, the scripts are injected into the Codebug directly from the python shell </BR>
and it is therefore not possible to inject the code from the web interface. 
The codebug tether library for python is also required.

<h3>Global Requirements</h3>

-Python3
-codebug_tether Python Module
-codebug_tether firmware

