from experta import KnowledgeEngine, Fact, NOT, W, Rule, DefFacts


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
