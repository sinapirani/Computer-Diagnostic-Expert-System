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
          NOT(Fact(connection=W())))
    def ask_if_connects(self):
        connection = yesno_prompt("Does the computer connect to Wi-Fi?")
        self.declare(Fact(connection=connection))

    @Rule(Fact(action='diagnose'),
          Fact(computer_turns_on=True),
          Fact(displays_output=True),
          Fact(boots_up=True),
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
