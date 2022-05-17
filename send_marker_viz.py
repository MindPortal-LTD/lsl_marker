"""send string-valued markers into LSL, with visualisation"""

import time
from pylsl import StreamInfo, StreamOutlet
from trial_viz import TrialVisual

def viz_marker(trial_number=10, initial_rest=3, trial_duration=3, rest_duration=2):
    # create stream info
    info = StreamInfo('ExptMarkerStream', 'Markers', 1, 0, 'string', 'myuidw43536')

    # next make an outlet
    outlet = StreamOutlet(info)

    # initialise visualisation
    viz = TrialVisual()

    # start
    print("Now sending markers...")
    n = 0 # trial count
    while n < trial_number:
        # initial wait
        outlet.push_sample(['exptStart'])
        viz.draw_iti()
        viz.update()
        print("exptStart")
        time.sleep(initial_rest)

        # trial start
        outlet.push_sample(['trialStart'])
        viz.draw_cue()
        viz.update()
        print("trialStart")
        time.sleep(trial_duration)

        # trial end
        outlet.push_sample(['trialEnd'])
        viz.draw_iti()
        viz.update()
        print("trialEnd")
        time.sleep(rest_duration)

        # next trial
        n += 1
    
    viz.finish()

if __name__ == '__main__':
    # settings
    trial_number = 2
    initial_rest = 1
    trial_duration = 2
    rest_duration = 1
    # send marker
    viz_marker(trial_number, initial_rest, trial_duration, rest_duration)