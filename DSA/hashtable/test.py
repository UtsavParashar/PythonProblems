# Description
# A log file shows LED indicator lights switching on and off.
# There are three different independent LED indicator lights that are of interest in the log.
# The LED colour is shown in the log file in uppercase: RED; GREEN; BLUE.
# Write a programme to calculate the duration, to the nearest second, of the period during which only the RED indicator light is on.

# Notes:

# You can assume that the log is in temporal order. The latest timestamps are at the end.
# You can assume that at the start of the log all LEDs are off. That may not be the case at the end of the log. Assume that the final log line is the final available timestamp and represents the end boundary of interest for this exercise.
# The format for the date and time is %Y-%m-%dT%H:%M:%S%z.
# INPUT
# string: Comprising multiple log lines, with a standard format as shown in the example below. You can assume that each input will not contain any more than 100 lines.

# OUTPUT
# Integer: Duration in seconds when only the RED LED is on.

# Example

# INPUT

# 2022-09-19T22:32:54+0000 INFO RED on
# 2022-09-19T22:32:58+0000 INFO RED off
# 2022-09-19T22:33:00+0000 INFO RED on
# 2022-09-19T22:33:17+0000 INFO BLUE on
# 2022-09-19T22:33:33+0000 INFO something else
# 2022-09-19T22:33:49+0000 INFO GREEN on
# 2022-09-19T22:33:49+0000 INFO something else
# 2022-09-19T22:34:01+0000 INFO something else happened
# 2022-09-19T22:34.55+0000 INFO something else happened
# 2022-09-19T22:36:49+0000 INFO something else again
# 2022-09-19T22:38:17+0000 INFO BLUE off
# 2022-09-19T22:39:49+0000 INFO RED off
# 2022-09-19T22:41:01+0000 INFO BLUE on
# 2022-09-19T22:42:07+0000 INFO GREEN off

# OUTPUT
# 20 <<< 4 + 16



from datetime import datetime

class LEDTracker:
    def __init__(self):
        self.red_on = False
        self.green_on = False
        self.blue_on = False
        self.red_on_start = None
        self.total_red_on_duration = 0

    def process_log_line(self, line):
        timestamp_str, _, led_info = line.split(' ', 2)
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S%z')
        led_color, action = led_info.split(' ')[1:3]

        if led_color == 'RED':
            self._process_red_led(action, timestamp)
        elif led_color == 'GREEN':
            self.green_on = (action == 'on')
        elif led_color == 'BLUE':
            self.blue_on = (action == 'on')

        if self.red_on and (self.green_on or self.blue_on):
            self.red_on_start = timestamp

    def _process_red_led(self, action, timestamp):
        if action == 'on':
            self.red_on = True
            self.red_on_start = timestamp
        elif action == 'off':
            if self.red_on and not self.green_on and not self.blue_on:
                self.total_red_on_duration += int((timestamp - self.red_on_start).total_seconds())
            self.red_on = False

    def get_total_red_on_duration(self):
        return self.total_red_on_duration

class Solution:
    def run(self, input):
        log_lines = input.strip().split('\n')
        tracker = LEDTracker()

        for line in log_lines:
            tracker.process_log_line(line)

        return tracker.get_total_red_on_duration()



import requests

class Solution:
    def run(self, pokemon_name):
        base_url = ''
        data = self.make_api_call(f'{base_url}{pokemon_name}')
        
        if data is None:
            return f'Error: Unable to fetch data for {pokemon_name}'
        
        evolution_chain_url = data['evolution_chain']['url']
        variation_data = self.make_api_call(evolution_chain_url)
        
        if variation_data is None:
            return f'Error: Unable to fetch evolution chain for {pokemon_name}'
        
        evolution_chain = self.parse_evolution_chain(variation_data['chain'])
        
        return json.dumps(evolution_chain)

    def make_api_call(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return response.json()

    def parse_evolution_chain(self, chain):
        result = {
            "name": chain["species"]["name"],
            "variations": []
        }
        for evolves_to in chain["evolves_to"]:
            result["variations"].append(self.parse_evolution_chain(evolves_to))
        return result