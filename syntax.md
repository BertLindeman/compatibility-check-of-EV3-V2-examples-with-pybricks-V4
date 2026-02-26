## Introduction

<details><summary>Web scraped using a program like this on windows. Only the URL is changed for another part of the doc</summary>

```python
import requests
from bs4 import BeautifulSoup

def extract_params(param_row):
    """Extract parameter name and description from a table row."""
    fields = param_row.find_all('td')
    if len(fields) == 2:
        param_name_raw = fields[0].get_text(strip=True)
        # Clean and format parameter name
        param_name = param_name_raw.split('(')[0].strip()  # Get just the name (before parentheses)

        # Handle complex descriptions
        param_desc_raw = fields[1]
        param_desc = ""
        
        for element in param_desc_raw.find_all(['p', 'ul']):
            if element.name == 'p':
                param_desc += element.get_text(strip=True) + " "
            elif element.name == 'ul':
                for li in element.find_all('li'):
                    param_desc += li.get_text(strip=True) + " "

        return param_name, param_desc.strip()
    return None, None

def scrape_pybricks_doc(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve the document")
        return {}

    soup = BeautifulSoup(response.content, 'html.parser')
    methods_info = {}

    # Find both class methods and regular methods
    for class_section in soup.find_all('dl', class_=['class', 'classmethod', 'method', 'attribute']):
        method_name = class_section.find('dt')
        if method_name:
            # Clean up the method name
            method_name = method_name.get_text(strip=True)
            method_name = method_name[:-1] if method_name[-1] == "¶" else method_name
            # add a space after class if needed
            # print(f"DEBUG 0 method_name {method_name} {method_name[0:5]}")
            method_name = "class " + method_name[5:] if method_name[0:5] == "class" else method_name
            # print(f"DEBUG 1 method_name {method_name} {method_name[0:5]}")

            # Get method description
            description = class_section.find('dd').find('p').get_text(strip=True)

            # Get parameters if available
            params_info = {}
            params_table = class_section.find('table', class_='docutils field-list')
            if params_table:
                param_rows = params_table.find_all('tr')
                for row in param_rows:
                    param_name, param_desc = extract_params(row)
                    if param_name and param_desc:
                        params_info[param_name] = param_desc
                    else:
                        pass
                        # print(f"Warning: Unexpected parameter layout for method '{method_name}'. Row: {row}")

            # Store the method details
            methods_info[method_name] = {
                'description': description,
                'parameters': params_info
            }

    return methods_info

def main():
    # url = "https://pybricks.com/ev3-micropython/hubs.html"  # Update as needed
    url = "https://pybricks.com/ev3-micropython/ev3devices.html"
    url = "https://pybricks.com/ev3-micropython/motors.html#control"
    url = "https://pybricks.com/ev3-micropython/parameters.html"
    url = "https://pybricks.com/ev3-micropython/tools.html"
    url = "https://pybricks.com/ev3-micropython/robotics.html"
    url = "https://pybricks.com/ev3-micropython/media.html"
    url = "https://pybricks.com/ev3-micropython/messaging.html"
    doc_methods = scrape_pybricks_doc(url)

    # Print the gathered data
    for method, details in doc_methods.items():
        print(f"{method} ")
        print(f"\tDescription: {details['description']}")
        if details['parameters']:
            print("\tParameters:")
            for param, desc in details['parameters'].items():
                print(f"  - {param}: {desc}")
        print()

if __name__ == "__main__":
    main()

```
</details>


## EV3Devices
- V2_syntax_ev3devices.py

Two tests are needed: one with a touch sensor on Port.S1 and another with the gyro sensor on Port.S1

Slight difference on motor.control.pid():

- V2   doc
    - pid(kp, ki, kd, integral_range, integral_rate, feed_forward)
- V3.6 doc
    - pid(kp, ki, kd, integral_deadzone, integral_rate)

##  hubs
- V2_syntax_hubs.py

Breaking changes:
1. ```python
    from pybricks.media.ev3dev import Font
    ```
    is now:
    ```python
    from pybricks.parameters import Font
    ```

2. ```python
   hub.speaker.set_volume
   ```
    is now:
   ```python
   hub.speaker.volume(nn)
   ```
Report of errors:
```
        Not supported: hub.speaker.play_file 
        Not supported: hub.speaker.say 
        Not supported: hub.speaker.set_speech_options 
        Not supported: hub.speaker.set_volume - use hub.speaker.volume(nn)
        Not supported: hub.speaker.set_font
        ImportError: no module named 'pybricks.media.ev3dev' use parameters
        Not supported: hub.screen.load_image
        Not supported: hub.screen.draw_image
        Not supported: hub.screen.save
```

## iodevices
- V2_syntax_iodevices.py

## media
- V2_syntax_media.py

## messaging
- V2_syntax_messaging.py

## NXTDevices
- V2_syntax_nxtdevices_part1
- V2_syntax_nxtdevices_part2

## robotics
- V2_syntax_robotics.py

## tools
- V2_syntax_tools.py

