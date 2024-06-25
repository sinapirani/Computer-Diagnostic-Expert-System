from experta import KnowledgeEngine, Fact, NOT, W, AND, OR, Rule, DefFacts

class ComputerDiagnostic(KnowledgeEngine):
    @DefFacts()
    def _initial_facts(self):
        yield Fact(action="diagnose")
        print("Welcome to the Computer Diagnostic Expert System!")

    @Rule(Fact(action='diagnose'),
          NOT(Fact(computer_turns_on=W())))
    def ask_if_computer_turns_on(self):
        computer_turns_on = yesno_prompt("Does the computer turn on?")
        self.declare(Fact(computer_turns_on=computer_turns_on))



    #Amir Monfared
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          NOT(Fact(internet_connection_issue=W())))
    def ask_if_internet_connection_issue(self):
        internet_connection_issue = yesno_prompt("Are you experiencing any issues with your internet connection (e.g., no connectivity, slow speeds)?")
        self.declare(Fact(internet_connection_issue=internet_connection_issue))

      #FATEMEH RADMARD
    
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          NOT(Fact(Bluetooth=W())))
    def ask_if_connects_bluetooth(self):
        Bluetooth = yesno_prompt("Does the computer connect to Bluetooth?")
        self.declare(Fact(Bluetooth=Bluetooth))
    
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          NOT(Fact(displays_output=W())))
    def ask_if_displays_output(self):
        displays_output = yesno_prompt("Does the computer display any output on the screen?")
        self.declare(Fact(displays_output=displays_output))

    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          NOT(Fact(boots_up=W())))
    def ask_if_boots_up(self):
        boots_up = yesno_prompt("Does the computer boot up and load the operating system?")
        self.declare(Fact(boots_up=boots_up))

    @Rule(Fact(action='diagnose'),
      Fact(computer_turns_on=True),
      Fact(displays_output=True),
      Fact(boots_up=True),
      NOT(Fact(blue_screen_error=W())))
    def ask_if_blue_screen_error(self):
      blue_screen = yesno_prompt("Did you encounter the Blue screen error?")
      self.declare(Fact(blue_screen_error=blue_screen))
        
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          NOT(Fact(connection=W())))
    def ask_if_connects(self):
        connection = yesno_prompt("Does the computer connect to Wi-Fi?")
        self.declare(Fact(connection=connection))


    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(blue_screen_error=True),
          NOT(Fact(after_update=W())))
    def ask_if_after_update(self):
        after_update = yesno_prompt("Did this problem happen to you after Windows update?")
        self.declare(Fact(after_update=after_update))

    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(blue_screen_error=True),
          Fact(after_update=True))
    def blue_screen_error_after_update(self):
        print("If you encounter a blue screen error after updating the device, delete the latest updates.")
        print("For this, you need to enter Windows in safe mode.")
        print("Before entering safe mode, it is necessary to enter the Windows recovery environment, which is called WinRE for short.")
        print("1. Press the power button of the device for 10 seconds to turn it off.")
        print("2. Press the power button again and turn on the device.")
        print("3. When the first indication is displayed on the screen (in some devices it is the manufacturer's logo), hold the power button again for 10 seconds to turn off the device.")
        print("4. After turning on the device, you must repeat the shutdown operation with the power button.")
        print("5. Finally, after the third time, allow the device to restart to be redirected to the WinRE screen.")
        print("\nNow you have to go through the following steps to enter safe mode:\n")
        print("On the Choose an option page, follow the path below:\n")
        print("Troubleshoot > Advanced options > Startup Settings > Restart\n")
        print("After the device restarts, you will see a list of options. The best option is to select item 5 or press the F5 key for safe mode with network.")
        print("After the device enters safe mode, follow the steps below to remove new updates from the control panel.")
        print("In the taskbar search bar, type <control panel> and then select Control Panel from the list of results.")

    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(blue_screen_error=True),
          Fact(after_update=False))
    def blue_screen_error_working(self):
        print("Some third-party antivirus software can cause Windows blue screen errors. You can temporarily remove this software to see if it is causing the problem. Then reinstall the software after your device is back up and running.")
        print("1. To solve this problem, you need to enter safe mode. So follow all the steps we explained before to enter this mode.")
        print("2. Now enter Windows Start and follow the following path:\n")
        print("Settings> System> Apps & features\n")
        print("3. Select Sort by name and change it to Sort by install date.")
        print("4. Select the third-party software you want to remove and click Uninstall.")
        print("5. After removing the program, restart the system.")
        print("6. Finally, exit safe mode according to the steps we mentioned earlier.")
        print("\nIf the above does not solve the problem, the last thing you can do yourself is to check the drivers. To check the following items, safe mode is required.\n")
        print("* Roll back the driver to the previous version:\n")
        print("1. To fix the Windows blue screen error, in the search bar of the taskbar, type the term device manager and search.\n")
        print("2. On the device manager page, open the device you want to restore. Right click on it and select Properties.")
        print("3. Select the Driver tab and go through Roll Back Driver > Yes.")
        print("\n* Disable third-party drivers:\n")
        print("If the driver is downgraded, but the error still persists, try the Disable setting to disable it. On the same Driver Properties page, this time go to Disable device > Yes.\n")
        print("* Remove third-party drivers:\n")
        print("To remove the driver in order to fix the Windows blue screen error, you must follow the path Uninstall > OK in the Properties page and the Driver tab. You may need to select <Delete the driver software for this device> in the Delete device confirmation box, and then select Uninstall > OK. To finalize, you need to restart the system.")
        print("If none of the above does not solve your problem, you should consider the following. In this way, there is also a possibility of a hardware problem.\n")


    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(blue_screen_error=False),
          Fact(connection=True),
          NOT(Fact(software_issue=W())))
    def ask_if_software_issue(self):
        software_issue = yesno_prompt(
            "Are you experiencing any software-related issues (e.g., program crashes, freezes, errors)?")
        self.declare(Fact(software_issue=software_issue))


    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(connection=True),
          Fact(software_issue=False))
    def suggest_hardware_issue(self):
        print(
            "The computer seems to be working fine physically and software-wise. The issue might be hardware-related.")

    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=False))
    def suggest_power_supply_issue(self):
        print("The computer may have a power supply issue. Please check the power cable connections and try again.")

    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=False))
    def suggest_display_issue(self):
        print("The computer may have a display issue. Please check the monitor connections and try again.")



    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=False))
    def suggest_boot_issue(self):
        print(
            "The computer might have a boot issue. Please check if the boot device (e.g., hard drive, "
            "SSD) is properly connected and functioning.")


    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(connection=False))
    def ask_if_connects_suggest(self):
        print("Please try the following steps:")
        print("1. Go to Control Panel")
        print("2. Go to Network and Sharing center")
        print("3. Go to Change adapter settings")
        print("4. Disable the Wi-Fi and then Enable again")

    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(connection=True),
          Fact(software_issue=True))
    def suggest_software_troubleshooting(self):
        print("The issue might be software-related. Please try the following steps:")
        print("1. Restart the computer and try again.")
        print("2. Update your software and drivers.")
        print("3. Scan for viruses and malware.")
        print("4. Check for software conflicts or compatibility issues.")
        print("5. If the issue persists, consider reinstalling the operating system or seeking professional help.")
        
    # Amirhossein Ramezani Shahrestani
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(software_issue=False),
          Fact(is_making_noise=False),
          NOT(Fact(keyboard_issue=W())))
    def ask_if_keyboard_issue(self):
        keyboard_issue = yesno_prompt("Are you experiencing any issues with the keyboard?")
        self.declare(Fact(keyboard_issue=keyboard_issue))

    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(software_issue=False),
          Fact(keyboard_issue=True))
    def suggest_keyboard_troubleshooting(self):
        print("The issue might be keyboard-related. Please try the following steps:")
        print("1. Check if the keyboard is properly connected.")
        print("2. Try using a different keyboard to see if the issue persists.")
        print("3. Update or reinstall the keyboard drivers.")
        print("4. Check for any software settings that might affect the keyboard functionality.")
        print("5. If the issue persists, consider replacing the keyboard or seeking professional help.")

        
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(software_issue=False),
          NOT(Fact(is_making_noise=W())))
    def ask_if_making_noise(self):
        is_making_noise = yesno_prompt("Is the computer making any unusual noises?")
        self.declare(Fact(is_making_noise=is_making_noise))

    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(software_issue=False),
          Fact(is_making_noise=True))
    def suggest_hardware_issue_noise(self):
        print("The computer is making unusual noises. This could indicate a hardware problem such as a failing hard drive or malfunctioning fan. Please try the following steps:")
        print("1. Check if any cables or components are loose inside the computer.")
        print("2. Ensure the fans are clean and not obstructed by dust or debris.")
        print("3. Listen carefully to identify the source of the noise.")
        print("4. If the noise persists, consider replacing the noisy component or seeking professional help.")


    # Rules for Sound Problems - Mahdi Behoftadeh
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          NOT(Fact(sound_works=W())))
    def ask_if_sound_works(self):
        sound_works = yesno_prompt("Does the sound work?")
        self.declare(Fact(sound_works=sound_works))

    # Rules for Sound Problems - Mahdi Behoftadeh
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(sound_works=False))
    def suggest_no_sound(self):
        print("There seems to be an issue with the sound. Please try the following steps:")
        print("1. Check if the speakers or headphones are properly connected.")
        print("2. Ensure that the volume is not muted or turned down too low.")
        print("3. Update or reinstall your audio drivers.")
        print("4. Check sound settings in the operating system.")
        print("5. Try using a different audio device.")

    # Rules for Sound Problems - Mahdi Behoftadeh
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(sound_works=True),
          NOT(Fact(sound_intermittent=W())))
    def ask_if_sound_intermittent(self):
        sound_intermittent = yesno_prompt("Is the sound intermittent?")
        self.declare(Fact(sound_intermittent=sound_intermittent))

    # Rules for Sound Problems - Mahdi Behoftadeh
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(sound_works=True),
          Fact(sound_intermittent=True))
    def suggest_intermittent_sound(self):
        print("There seems to be an intermittent sound issue. Please try the following steps:")
        print("1. Check if the audio cable is securely connected.")
        print("2. Ensure that there are no loose connections.")
        print("3. Update or reinstall your audio drivers.")
        print("4. Check for interference from other devices.")
        print("5. Test with another set of speakers or headphones.")

    # Rules for Sound Problems - Mahdi Behoftadeh
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(sound_works=True),
          Fact(sound_intermittent=False),
          NOT(Fact(sound_distorted=W())))
    def ask_if_sound_distorted(self):
        sound_distorted = yesno_prompt("Is the sound distorted?")
        self.declare(Fact(sound_distorted=sound_distorted))

    # Rules for Sound Problems - Mahdi Behoftadeh
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(sound_works=True),
          Fact(sound_intermittent=False),
          Fact(sound_distorted=True))
    def suggest_distorted_sound(self):
        print("There seems to be an issue with distorted sound. Please try the following steps:")
        print("1. Check if the audio cable is properly connected and not damaged.")
        print("2. Ensure that the audio drivers are up to date.")
        print("3. Adjust the audio settings in the operating system.")
        print("4. Test with another set of speakers or headphones.")
        print("5. Check for any electromagnetic interference from other devices.")

    # Rules for Application Crashes - Sarvenaz Jenabi
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          NOT(Fact(app_crashing=W())))
    def ask_if_app_crashing(self):
        app_crashing = yesno_prompt("Is any application crashing frequently?")
        self.declare(Fact(app_crashing=app_crashing))

    # Rules for Application Crashes - Sarvenaz Jenabi
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(app_crashing=True),
          NOT(Fact(app_name=W())))
    def ask_app_name(self):
        app_name = input("What is the name of the application that is crashing? ")
        self.declare(Fact(app_name=app_name))

    # Rules for Application Crashes - Sarvenaz Jenabi
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(app_crashing=True),
          Fact(app_name=MATCH.app_name),
          NOT(Fact(app_error_message=W())))
    def ask_app_error_message(self, app_name):
        app_error_message = input(f"Is there an error message when {app_name} crashes? If yes, please describe it: ")
        self.declare(Fact(app_error_message=app_error_message))

    # Rules for Application Crashes - Sarvenaz Jenabi
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(app_crashing=True),
          Fact(app_name=MATCH.app_name),
          Fact(app_error_message=MATCH.app_error_message))
    def suggest_app_crash_solution(self, app_name, app_error_message):
        print(f"There seems to be an issue with {app_name} crashing. Please try the following steps:")
        print("1. Check for updates for the application and install them.")
        print("2. Ensure that your operating system and drivers are up to date.")
        print("3. Try reinstalling the application.")
        print("4. Check for any available patches or hotfixes for the application.")
        print("5. Make sure your system meets the application's minimum requirements.")
        print("6. Check if the error message provides any clues or specific error codes.")
        if app_error_message:
            print(f"Error Message: {app_error_message}")
        print("7. Look up the error message or code online for specific solutions.")
        print("8. If the issue persists, consider contacting the application's support team.")

    # Rules for Application Crashes - Sarvenaz Jenabi
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(app_crashing=False))
    def no_app_crashes_detected(self):
        print("It seems there are no application crashes. Please ensure all your applications are up to date and running smoothly.")

    # Rules for High CPU Usage problems - Mehriyna Mohammadi
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(high_cpu_usage=True),
          NOT(Fact(background_processes=W())))
    def ask_if_background_processes(self):
        background_processes = yesno_prompt("Are there many background processes running?")
        self.declare(Fact(background_processes=background_processes))

    # Rules for High CPU Usage problems - Mehriyna Mohammadi
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(high_cpu_usage=True),
          Fact(background_processes=True))
    def suggest_closing_background_processes(self):
        print("There are many background processes running. Please try the following steps:")
        print("1. Open Task Manager or Activity Monitor and identify unnecessary background processes.")
        print("2. End or disable those processes to free up CPU resources.")
        print("3. Disable startup programs that you do not need.")

    # Rules for High CPU Usage problems - Mehriyna Mohammadi
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(high_cpu_usage=True),
          NOT(Fact(malware_scan=W())))
    def ask_if_malware_scan_done(self):
        malware_scan = yesno_prompt("Have you performed a malware scan?")
        self.declare(Fact(malware_scan=malware_scan))

    # Rules for High CPU Usage problems - Mehriyna Mohammadi
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(high_cpu_usage=True),
          Fact(malware_scan=False))
    def suggest_running_malware_scan(self):
        print("High CPU usage can be caused by malware. Please run a full system scan using a reliable antivirus software.")

    # Rules for High CPU Usage problems - Mehriyna Mohammadi
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(high_cpu_usage=True),
          Fact(malware_scan=True))
    def suggest_other_high_cpu_solutions(self):
        print("Please try the following additional steps to address high CPU usage:")
        print("1. Update your operating system and all drivers.")
        print("2. Check for software updates or patches that may resolve high CPU usage issues.")
        print("3. Consider increasing system cooling if overheating is causing high CPU usage.")
        print("4. Upgrade your CPU or add more RAM if your system is frequently under heavy load.")
    
    #Fatemeh Moradi
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(Bluetooth=False))
    def suggest_to_connect_Bluetooth(self):
        print("There may be a problem with your Bluetooth driver installation, check it out.")


#Mustafa Rahnamai
# New rule for checking hardware conflicts
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          NOT(Fact(hardware_conflict=W())))
    def ask_if_hardware_conflict(self):
        hardware_conflict = yesno_prompt("Are there any hardware conflicts in the device manager?")
        self.declare(Fact(hardware_conflict=hardware_conflict))

    # New rule for suggesting resolution for hardware conflicts
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(hardware_conflict=True))
    def suggest_hardware_conflict_resolution(self):
        print("There might be a hardware conflict. Please try the following steps:")
        print("1. Open the device manager and check for any devices with a yellow exclamation mark.")
        print("2. Try updating the drivers for the conflicting hardware.")
        print("3. If the issue persists, consider removing the device and restarting the computer.")

    # New rule for checking peripheral issues
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          NOT(Fact(peripheral_issue=W())))
    def ask_if_peripheral_issue(self):
        peripheral_issue = yesno_prompt("Are you experiencing issues with any external devices (e.g., keyboard, mouse, printer)?")
        self.declare(Fact(peripheral_issue=peripheral_issue))

    # New rule for suggesting resolution for peripheral issues
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(peripheral_issue=True))
    def suggest_peripheral_issue_resolution(self):
        print("There might be a peripheral issue. Please try the following steps:")
        print("1. Check the connections of your external devices.")
        print("2. Try unplugging and replugging the devices.")
        print("3. Update the drivers for the external devices.")
        print("4. Try using the devices on another computer to rule out hardware failure.")

    # New rule for checking system updates
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          NOT(Fact(system_update=W())))
    def ask_if_system_update(self):
        system_update = yesno_prompt("Is your operating system and all software up to date?")
        self.declare(Fact(system_update=system_update))

    # New rule for suggesting system update
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(system_update=False))
    def suggest_system_update(self):
        print("Your system might be out of date. Please ensure that you have the latest updates installed for your operating system and software.")

    #Rules for random crash ,zahra_azadeh
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(dropout=W()))
    def ask_if_dropout(self):
        dropout = yesno_prompt("Does the image suddenly disappear?")
        self.declare(Fact(dropout=dropout))
    
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(dropout=True))
    def suggest_random_crash(self):
        print("There seems to be a random crash issue. Please try the following steps:")
        print("1. Ensure that all hardware components are properly seated and not loose.")
        print("2. Update device drivers and operating system.")
        print("3. Check for malware and viruses.")
        print("4. Monitor system temperature for overheating issues.")

    #Seyed Mahdi Ashrafipour
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=False),
          Fact(boots_up=False))
    def suggest_graphics_card_issue(self):
        print("The computer may have a graphics card issue. Please check the graphics card connections and try again.")
    
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=False),
          Fact(software_issue=False))
    def suggest_os_corruption_issue(self):
        print("The operating system might be corrupted. Please consider repairing or reinstalling the operating system.")


    #Ariyan
    @Rule(Fact(action='diagnose'),
      Fact(computer_turns_on=True),
      Fact(displays_output=False))
    def suggest_display_issue(self):
        print("The computer may have a display issue. Please check the monitor connections and the graphics card.")
    
    @Rule(Fact(action='diagnose'),
      Fact(computer_turns_on=True),
      Fact(displays_output=True),
      Fact(boots_up=False),
      Fact(software_issue=False),
      Fact(hardware_issue=False))
    def suggest_power_supply_issue(self):
        print("The power supply might be faulty. Please check the power connections and consider replacing the power supply.")

    #Amir Mohammad Tafakory
    #New Rule for Time and Date issue
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          NOT(Fact(time_date=W())))
    def ask_if_time_and_date_incorrect(self):
        time_date = yesno_prompt("Is your system time and date incorrect?")
        self.declare(Fact(time_date=time_date))

    #New Rule for suggesting set time and date system
    @Rule(Fact(action='diagnose'),
        Fact(computer_turns_on=True),
        Fact(displays_output=True),
        Fact(boots_up=True),
        Fact(time_date=True))
    def suggest_set_time_and_date(self):
        print("Please try the following steps:")
        print(" 1. go to control panel")
        print(" 2. click on the clock and region")
        print(" 3. click on the date and time")
        print(" 4. click on the change time zone button")
        print(" 5. select your time zone or check the option Automatically adjust clock for daylight saving time")

    
    # Shaghayegh_Atefrad 
     
    @Rule(Fact(action='diagnose'), 
          Fact(computer_turns_on=True), 
          NOT(Fact(ram_issue=W()))) 
    def ask_if_ram_issue(self): 
        ram_issue = yesno_prompt("Are you experiencing any RAM-related issues (e.g., system crashes, memory errors)?") 
        self.declare(Fact(ram_issue=ram_issue)) 
     
    @Rule(Fact(action='diagnose'), 
          Fact(action='diagnose'), 
          Fact(computer_turns_on=True), 
          NOT(Fact(cpu_issue=W()))) 
    def ask_if_cpu_issue(self): 
        cpu_issue = yesno_prompt("Are you experiencing any CPU-related issues (e.g., high temperatures, performance problems)?") 
        self.declare(Fact(cpu_issue=cpu_issue)) 
     
    @Rule(Fact(action='diagnose'), 
          Fact(computer_turns_on=True), 
          NOT(Fact(graphics_card_issue=W()))) 
    def ask_if_graphics_card_issue(self): 
        graphics_card_issue = yesno_prompt("Are you experiencing any graphics card-related issues (e.g., display artifacts, low FPS)?") 
        self.declare(Fact(graphics_card_issue=graphics_card_issue))

    # Seyed_Daniel_Seyed_Saadat
# new rule for troubleshoot RAM incompatibility issues.

@Rule(Fact(action='diagnose'),
      Fact(computer_turns_on=True),
      Fact(displays_output=True),
      Fact(boots_up=True),
      Fact(software_issue=False),
      NOT(Fact(ram_issue=W())))
def ask_if_ram_issue(self):
    ram_issue = yesno_prompt("Are you experiencing any issues related to RAM (e.g., frequent crashes, memory errors)?")
    self.declare(Fact(ram_issue=ram_issue))

@Rule(Fact(action="diagnose_hardware"),
      Fact(ram_mismatch=True))
def check_ram_compatibility(self):
    print("There might be a RAM compatibility issue. Please check the following:")
    print("- Make sure all RAM modules are of the same type (DDR3, DDR4, etc.).")
    print("- Verify that the RAM modules have the same clock speed (e.g., 2400MHz).")
    print("- Ensure that the RAM modules are installed in the correct slots (usually in pairs for dual-channel mode).")
    print("- Check the motherboard manual for specific RAM compatibility information.")

@Rule(Fact(action="diagnose_hardware"),
      Fact(ram_mismatch=true),
      Fact(ram_compatibility_checked=True))
def recommend_ram_replacement(self):
    print("If the RAM modules are compatible but the issue persists, consider replacing the RAM with compatible modules.")
    print("Here are some additional troubleshooting tips:")
    print("- Try reseating the RAM modules in their slots.")
    print("- Test each RAM module individually to identify any faulty modules.")
    print("- Update the BIOS to the latest version, which might improve RAM compatibility.")
    print("If none of these suggestions resolve the issue, consult your motherboard manual or a computer technician for further assistance.")

###Fatemeh Ahmadinejad
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(software_issue=False),
          Fact(checked_ram=False))
    def suggest_ram_issue(self):
        print("try reseating or replacing the RAM modules to check for hardware problems.")
    
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(software_issue=False),
          Fact(checked_ram=True),
          Fact(checked_cpu=False))
    def suggest_cpu_issue(self):
        print("If your computer is experiencing performance issues or random crashes, consider checking for CPU-related problems.")
    
    #New rule for overloading
    @Rule(Fact)(action='diagnose'),
    
    Fact(computer_turns-on=True),
      Fact(displays_output=True)
      Fact(boots_up=True)
      Fact(software_issues=True)
      Not(Fact(overloading=w())))
    
    def ask_if_kill_task(self):
        kill_task = yesno_prompt("are you suffering from your computer stopped working?")
        self.declare(Fact(kill_task = kill_task))

# Rule for BIOS update failures - Arian Setudeh
@Rule(Fact(action='diagnose'),
      Fact(computer_turns_on=True),
      NOT(Fact(bios_update_failure=W())))
def ask_if_bios_update_failure(self):
    bios_update_failure = yesno_prompt("Have you recently attempted to update the BIOS and encountered issues?")
    self.declare(Fact(bios_update_failure=bios_update_failure))


# Rule for suggesting BIOS update resolution - Arian Setudeh
@Rule(Fact(action='diagnose'),
      Fact(computer_turns_on=True),
      Fact(bios_update_failure=True))
def suggest_bios_update_resolution(self):
    print("There might be an issue with the BIOS update process. Please try the following steps:")
    print("1. Ensure that the BIOS update file is compatible with your motherboard.")
    print("2. Check the manufacturer's website for any specific instructions or troubleshooting steps.")
    print("3. Retry the BIOS update process, ensuring that all instructions are followed carefully.")
    print("4. If the issue persists, consider seeking assistance from the manufacturer's support team or forums.")


    # Rule for BIOS settings reset - Arian Setudeh
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          NOT(Fact(bios_settings_reset=W())))
    def ask_if_bios_settings_reset(self):
        bios_settings_reset = yesno_prompt(
            "Have you noticed any unexpected changes in BIOS settings or the BIOS being reset?")
        self.declare(Fact(bios_settings_reset=bios_settings_reset))
    
    
    # Rule for suggesting BIOS settings reset resolution - Arian Setudeh
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(bios_settings_reset=True))
    def suggest_bios_settings_reset_resolution(self):
        print("The BIOS settings may have been reset unexpectedly. Please try the following steps:")
        print("1. Enter the BIOS setup utility and review the settings.")
        print("2. Restore default settings if necessary, and ensure that changes are saved properly.")
        print("3. Check for any hardware issues that may be causing the BIOS settings to reset.")
        print("4. If the issue persists, consider updating the BIOS firmware or contacting technical support.")
    
    # Rule for firmware corruption - Arian Setudeh
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          NOT(Fact(firmware_corruption=W())))
    def ask_if_firmware_corruption(self):
        firmware_corruption = yesno_prompt("Have you encountered any signs of firmware corruption or failure?")
        self.declare(Fact(firmware_corruption=firmware_corruption))
    
    # Rule for suggesting firmware corruption resolution - Arian Setudeh
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(firmware_corruption=True))
    def suggest_firmware_corruption_resolution(self):
        print("Firmware corruption may be causing issues with the system. Please try the following steps:")
        print("1. Check for firmware updates for your motherboard, storage devices, or other hardware components.")
        print("2. Attempt to reflash or reinstall the firmware for the affected devices.")
        print("3. Ensure that the firmware update process is performed correctly and without interruptions.")
        print("4. If the issue persists, consider contacting the manufacturer for further assistance.")


    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(software_issue=False),
          NOT(Fact(hardware_issue=W())))
    def ask_if_hardware_issue(self):
        hardware_issue = yesno_prompt("Are you experiencing any hardware-related issues (e.g., strange noises, overheating, hardware failures)?")
        self.declare(Fact(hardware_issue=hardware_issue))
    
    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(software_issue=False),
          Fact(hardware_issue=True))
    def suggest_hardware_troubleshooting(self):
        print("The issue might be hardware-related. Please try the following steps:")
        print("1. Check for loose or faulty hardware connections.")
        print("2. Clean the computer from dust and ensure proper ventilation.")
        print("3. Run hardware diagnostic tests to identify any faulty components.")
        print("4. If necessary, replace or repair the faulty hardware.")

    @Rule(Fact(action='diagnose'), Fact(computer_turns_on=True), Fact(displays_output=True), Fact(boots_up=True), NOT(Fact(sound_issue=W())))
    def ask_if_sound_issue(self):
        self.declare(Fact(sound_issue=yesno_prompt("Are you experiencing any sound issues?")))
    
    @Rule(Fact(action='diagnose'), Fact(computer_turns_on=True), Fact(displays_output=True), Fact(boots_up=True), Fact(sound_issue=True))
    def suggest_sound_troubleshooting(self):
        print("The issue might be sound-related. Please try the following steps:")
        print("1. Check if the speakers or headphones are properly connected.")
        print("2. Ensure the volume is not muted.")
        print("3. Update or reinstall sound drivers.")
        print("4. Check the sound settings in the operating system.")
        print("5. Try with a different audio device to rule out hardware issues.")

  @Rule(Fact(action='diagnose'), Fact(computer_turns_on=True), Fact(displays_output=True), Fact(boots_up=True), Fact(connection=True), Fact(software_issue=False), Fact(hardware_issue=False), NOT(Fact(driver_issue=W())))
    def ask_if_driver_issue(self):
        self.declare(Fact(driver_issue=yesno_prompt("Are you experiencing any driver issues?")))
    
    @Rule(Fact(action='diagnose'), Fact(computer_turns_on=True), Fact(displays_output=True), Fact(boots_up=True), Fact(connection=True), Fact(software_issue=False), Fact(hardware_issue=False), Fact(driver_issue=True))
    def suggest_driver_troubleshooting(self):
        print("The issue might be driver-related. Please try the following steps:")
        print("1. Update the device drivers.")
        print("2. Rollback to a previous driver version if the issue started after an update.")
        print("3. Uninstall and reinstall the problematic driver.")
        print("4. Check the manufacturer's website for driver updates or patches.")

def yesno_prompt(question):
    while True:
        response = input(question + " (yes/no): ").lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Please enter 'yes' or 'no'.")


engine = ComputerDiagnostic()
engine.reset()
engine.run()
