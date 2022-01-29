# 7mind-app-Android

Settings:

1. Prerequisites:

	1. Have python 3+ installed to your pc
	   Link: https://www.python.org/downloads/

	2. Have pytest installed:
	   In terminal:  pip install pytest

	3. 7mind apk app downloaded to your localdrive on your pc
	   Link: https://m.apkpure.com/7mind-meditation-reinvented/de.sevenmind.android

	4. Android Studio Installed 
	   Link: https://developer.android.com/studio#downloads

	5. Java jdk installed ( Possibly Java 8)
	   Link: https://www.oracle.com/java/technologies/javase/javase8u211-later-archive-downloads.html


	6. Appium Desktop installed with settings: 1. Open Appium Desktop
								      2. Click Edit Configuration
								      3.  ANDROID_HOME(‘Path the Android SDK’) - this is environmental variable setting inside 										  appium server
								      4.  JAVA_HOME(‘Path to jdk’) - this is environmental variable setting inside appium server
								      5. Click Save & Restart
							      

7.1. Install Android Emulator: 
				   1. Open Android Studio
				   2. Click on Tools
				   3. Choose AVD Manager
				   4. Click +Create Virtual Device
				   5. Choose Pixel “5” & click next
				   6. Choose API level 30 & click next

7.2. For Android Real Device: 1. Download 7mind app from Google Play (On Real Device)


2.1. How to connect to Real Device: - For real device: 
						      1. Connect device to pc with usb or tcp
						      2. In terminal type: adb devices
						      3. Add the device name to the launchapp.py file/deviceName
						      4. Copy the path for 7mind apk on your localdrive and paste it 								      				         in Login-Android-Real Device folder to launchapp.py file/app 
								   

2.2. How to connect to Emulator: After emulator installed: 
							   1. Copy the path for 7mind apk on your localdrive and paste it 								       		    		      in Login-Android-Emulator folder to launchapp.py file/app
							   2.  open Android Studio
							   3. Click Tools from menu
							   4. Click AVD Manager from dropdown
							   5. Click play icon & wait for boot
							   6. Drag and drop the 7mind apk to the emulator from pc

3.1. How to run on Real Device: After properly connected: 
							  1. Open Appium Desktop and click Start Server
					  		  2. Open terminal at Login-Android-Real Device folder and type pytest -v test_login.py

3.2. How to run on Emulator: After properly connected:	  
							  1. Open Appium Desktop and click Start Server
							  2. Open terminal at Login-Android-Emulator folder and type pytest -v test_login.py
							  
							  Jenkins Test
							  Jenkins Test2
							  Jenkins Test3
							  Jenkins4
							  Jenkins Test5
