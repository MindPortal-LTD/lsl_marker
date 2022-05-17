"""send string-valued markers into LSL."""

import time
from pylsl import StreamInfo, StreamOutlet

def main_marker(trial_number=10, initial_rest=3, trial_duration=3, rest_duration=2):
    # create stream info
    info = StreamInfo('ExptMarkerStream', 'Markers', 1, 0, 'string', 'myuidw43536')

    # next make an outlet
    outlet = StreamOutlet(info)

    print("Now sending markers...")
    n = 0 # trial count
    while n < trial_number:
        # initial wait
        outlet.push_sample(['exptStart'])
        print("exptStart")
        time.sleep(initial_rest)

        # trial start
        outlet.push_sample(['trialStart'])
        print("trialStart")
        time.sleep(trial_duration)

        # trial end
        outlet.push_sample(['trialEnd'])
        print("trialEnd")
        time.sleep(rest_duration)

        # next trial
        n += 1

if __name__ == '__main__':
    # settings
    trial_number = 30
    initial_rest = 3
    trial_duration = 2
    rest_duration = 1
    # send marker
    main_marker(trial_number, initial_rest, trial_duration, rest_duration)