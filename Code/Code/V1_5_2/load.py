import time
import os
import random
from datetime import datetime


colors = """
    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White
"""

def load_sequence():
    def color_green():
        os.system('color 0A')

    def clear():
        time.sleep(0.2)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.1)

    def generate_loading_message():
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        random_phrase = random.choice(loading_phrases)
        return f'{current_datetime} - {random_phrase}'

    def SetUp_messages_Long():
        for _ in range(25):
            print(generate_loading_message())
            time.sleep(0.05)  

    def SetUp_messages_Short():
        for _ in range(5):
            print(generate_loading_message())
            time.sleep(0.05)  

    def generate_loading_script():
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        random_phrase = random.choice(loading_scripts)
        return f'{current_datetime} - {random_phrase}'

    def Load_Scripts():
        os.system('color 04')
        time.sleep(0.1)

        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        random_phrase = random.choice(Before_loading_scripts)
        print((f'{current_datetime} - {random_phrase}'))

        for _ in loading_scripts:
            print(generate_loading_script())
            time.sleep(0.1)
        
        time.sleep(0.1)


    def setting_up():
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        random_phrase = random.choice(Before_loading_Phrases)
        print((f'{current_datetime} - {random_phrase}'))

        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        random_phrase = random.choice(setUP_phrases)
        print(f'{current_datetime} - {random_phrase}')
        time.sleep(0.2)
        os.system('color 30')


    setUP_phrases = [
        "Initializing the application. Please wait while we set up the environment",
        "Loading essential components. This may take a moment as we ensure all dependencies are in place",
        "Configuring the interface layout. Getting the user interface ready for a seamless experience",
        "Loading user preferences. Applying your personalized settings to create a customized interface",
        "Retrieving UI assets. We're gathering resources to make the interface visually engaging",
        "Organizing elements. We're arranging buttons, menus, and panels for easy navigation",
        "Loading interactive widgets. Preparing dynamic components for an interactive user experience",
        "Applying theme settings. Personalizing the interface appearance according to your chosen theme",
        "Adapting to screen resolution. Ensuring a responsive design that fits your device perfectly",
        "Implementing accessibility features. Making the interface usable for all users, regardless of their abilities",
        "Fine-tuning animations. Polishing the interface with subtle and smooth visual transitions",
        "Verifying compatibility with different browsers. Ensuring consistent UI performance across platforms",
        "Optimizing layout responsiveness. Making sure the interface adapts seamlessly to different screen sizes",
        "Integrating internationalization support. Enabling the interface to be displayed in multiple languages",
        "Setting up keyboard shortcuts. Streamlining navigation through convenient key combinations",
        "Validating UI elements. Rigorously testing all user interface components for functionality and reliability",
        "Performing usability tests. Ensuring the interface is intuitive and user-friendly",
        "Creating logical information architecture. Designing the interface's structure for efficient information organization",
        "Implementing typography guidelines. Selecting appropriate fonts and styles for better readability",
        "Applying color schemes. Choosing harmonious colors that enhance the interface aesthetics and readability"
    ]

    Before_loading_scripts = [
        "ABOUT TO LOAD THE SCRIPTS...",
        "PREPARING TO INITIALIZE MODULES...",
        "CONFIGURING MODULES FOR LOADING...",
        "LOADING SCRIPTS INTO MEMORY...",
        "SETTING UP MODULES FOR LOADING...",
        "LOADING REQUIRED MODULES...",
        "CONFIGURING SCRIPT LOADING PROCEDURE...",
        "LOADING SCRIPTS AND MODULES...",
        "INITIALIZING LOADING SEQUENCE...",
        "PREPARING SCRIPTS FOR LOADING..."
    ]

    loading_scripts = [
        "Loading Main.py - Initializing the main application module",
        "Loading BoxNest.py - Configuring the nesting module for efficient box arrangement",
        "Loading userQuestions.py - Setting up the module for capturing user input and questions",
        "Loading CreateANewDatabase.py - Creating a new database structure for storing data",
        "Loading Logo.py - Initializing the module for displaying the application logo",
        "Loading Load.py - Configuring the module for displaying loading messages",
    ]

    Before_loading_Phrases = [
        "LOADING USER INTERFACE",
        "INITIALIZING UI COMPONENTS",
        "CONFIGURING UI ELEMENTS",
        "PREPARING UI FOR DISPLAY",
        "LOADING UI RESOURCES",
        "SETTING UP UI LAYOUT",
        "LOADING UI TEMPLATES",
        "CONFIGURING UI STYLES",
        "LOADING UI MODULES",
        "INITIALIZING UI CONTROLS"
    ]

    loading_phrases = [
        "Initializing the application. Please wait while we set up the environment",
        "Loading essential components. This may take a moment as we ensure all dependencies are in place.",
        "Preparing the system for optimal performance. Hold on as we configure various settings",
        "Compiling necessary code modules. This process might take a while, so make yourself comfortable",
        "Optimizing resource allocation. We are carefully managing system resources for improved efficiency",
        "Verifying user permissions. Sit tight while we authenticate your access rights",
        "Establishing secure connections. We're ensuring a safe connection to our servers",
        "Loading the user interface. Relax as we create an intuitive and user-friendly experience.",
        "Retrieving updated data. We're fetching the latest information for you",
        "Performing data integrity checks. Your data is important to us, so we're ensuring its accuracy"
    ]


    color_green()
    SetUp_messages_Long()
    Load_Scripts()
    SetUp_messages_Short()
    setting_up()
    clear()


def clear_cmd():
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.2)

