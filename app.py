from experta import KnowledgeEngine, Fact, NOT, W, AND, OR, Rule, DefFacts, MATCH

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
          NOT(Fact(software_issue=W())))
    def ask_if_software_issue(self):
        software_issue = yesno_prompt("Are you experiencing any software-related issues (e.g., program crashes, freezes, errors)?")
        self.declare(Fact(software_issue=software_issue))


    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(software_issue=False))
    def suggest_hardware_issue(self):
        print("The computer seems to be working fine physically and software-wise. The issue might be hardware-related.")

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
        print("The computer might have a boot issue. Please check if the boot device (e.g., hard drive, SSD) is properly connected and functioning.")


    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
          Fact(software_issue=True))
    def suggest_software_troubleshooting(self):
        print("The issue might be software-related. Please try the following steps:")
        print("1. Restart the computer and try again.")
        print("2. Update your software and drivers.")
        print("3. Scan for viruses and malware.")
        print("4. Check for software conflicts or compatibility issues.")
        print("5. If the issue persists, consider reinstalling the operating system or seeking professional help.")


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