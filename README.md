# **Message Disappearing App**
This simple application is built using Tkinter, a standard GUI (Graphical User Interface) toolkit for Python. The app allows users to type messages, and after a certain period of inactivity, the messages automatically disappear. Below are some key features and notes about the application:

## Features:
1.  **Auto-Disappearing Messages:** Messages entered into the text area will automatically disappear after a 4-second pause in typing.

2. **Initial Placeholder Text:** The text area is initialized with the message "Start Typing" in gray. This text disappears as soon as the user starts typing.

3. **Responsive Width:** The width of the text area dynamically adjusts based on the window size, ensuring a responsive and user-friendly interface.

4. **Enter Key Handling:** Pressing the "Enter" key inserts a newline character ("\n") into the text area.

## Usage:
1. Clone the repository:
  git clone https://github.com/Anandoptimus/Day90.git

2. Navigate to the project directory:
  cd Day90

3. Run the script:
  python main.py

## Screenshot:
![image](https://github.com/Anandoptimus/Day90/assets/101982906/77ebfbcc-eed9-4a7a-94a3-dd0e025929e0)


## Dependencies:
+ **Tkinter:** This application relies on the Tkinter library, which is included with most Python installations.

## Notes:
+ The app uses event handling to trigger actions such as updating text width, handling typing and not typing events, and managing focus in and out events.
+ The disappearance of messages is triggered by a 4-second timeout of inactivity.
+ Feel free to customize the application as needed for your specific use case or requirements.

## License:
This project is licensed under the MIT License - see the LICENSE file for details.
