================================================================
||       ████ █   █  ███  █   █  ████ █      ███   ████       ||
||      █     █   █ █   █ ██  █ █     █     █   █ █           ||
||      █     █████ █████ █ █ █ █  ██ █     █   █ █  ██       ||
||      █     █   █ █   █ █  ██ █   █ █     █   █ █   █       ||
||       ████ █   █ █   █ █   █  ███  █████  ███   ███        ||
================================================================

1.0.0
- Initial Creation.
- Added YouTube search function.
- Added Google search function.
- Added opening application function.

1.0.1
- Changed all calling function to take a string from user as input, and return a string output for text to speak to respond with.
- Moved YouTube search function to seperate module.
- Moved Google search function to seperate module.
- Moved opening application function to seperate module.
- Application module now uses a list of dictionaries to hold different applications and their filepath for dynamic functionality.
- Seperated the listening and encoding of audio sound into seperate function.

1.0.2
- Added Time and Date query functions to the new Time module.
- Seperated command search code from main method to seperate function. 

1.0.3
- Added Sound and Keyboard modules by Paradoxis (Free License).

1.0.4
- Added Weather module.
- Seperated no command found error to seperate function.

1.0.5 
- Added 2 more functions to the Weather module; the TemperatureSearch and ForcastSearch effectively splitting the WeatherSearch.
- Added GetWeatherData function to get API data for multiple different functions in Weather module; changes have been made to WeatherSearch with this in mind.
- Moved listening function in ARTEMIS module back to main code to increase sampling speed.

1.0.6
- Added Wiki module.