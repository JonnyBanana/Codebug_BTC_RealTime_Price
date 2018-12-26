# Codebug_BTC_RealTime_Price


A Python script for Codebug that which exploits the Coindesk and Bitstamp API (V2 and v2)  </br>
to display the price of Bitcoins in real time on the codebug led display

![Alt text](https://raw.githubusercontent.com/JonnyBanana/Codebug_Led_Animations/master/IMG/cb.jpg) 

I created two simple Python scripts that use the Coindesk (v1) and Bitstamp (v2) APIs respectively
Both require the tether_codebug firmware:

https://github.com/codebugtools/codebug_tether

which you can find in the "firmware" folder.

Codebug Tether Guide: 

https://codebug-tether.readthedocs.io/en/latest/

Have also a pdf in the "doc" folder.

In addition, the scripts are injected into the Codebug directly from the python shell </BR>
and it is therefore not possible to inject the code from the web interface. 
The codebug tether library for python is also required.

</BR>

![Alt text](https://raw.githubusercontent.com/JonnyBanana/Codebug_BTC_RealTime_Price/master/img/pimoroni-codebug-200-large.jpg)

</BR>

<h3>Global Requirements</h3>

-Python3</BR>
-codebug_tether python module</BR>
-codebug_tether firmware</BR>


<h4>How to Install Requirements</h4>

<h5>codebug_tether firmware</h5>

Guide Here: http://www.codebug.org.uk/learn/activity/66/tethering-codebug-with-python/

<h5>codebug_tether python module</h5>

<h6>Windows</h6>

  pip install codebug_tether

<h6>Linux</h6>

sudo pip3 install codebug_tether

<h6>Mac OS</h6>

I do not give a fuck!
