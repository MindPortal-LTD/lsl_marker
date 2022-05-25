"""send string-valued markers into LSL, with visualisation"""

import time
from pylsl import StreamInfo, StreamOutlet
from trial_viz import TrialVisual
import numpy as np

def viz_marker_gabor(trial_number=10, initial_rest=3, trial_duration=3, rest_duration=2,
                    orientations=[0, 90, 130], loc_y=0, loc_x=0):
    # create stream info
    info = StreamInfo('ExptMarkerStream', 'Markers', 1, 0, 'string', 'myuidw43536')

    # next make an outlet
    outlet = StreamOutlet(info)

    # initialise visualisation
    viz = TrialVisual()

    # start
    print("Now sending markers...")
    n = 0 # trial count
    # initial wait
    outlet.push_sample(['exptStart'])
    viz.draw_iti()
    viz.update()
    print("exptStart")
    time.sleep(initial_rest)

    while n < trial_number:

        # random orientation
        ori_idx = np.random.choice(np.arange(len(orientations)), 1)[0]
        orientation = orientations[ori_idx]
        # trial start
        trial_str = f'trialStart_{orientation}'
        outlet.push_sample([trial_str])
        viz.draw_gabor(orientation, loc_y=loc_y, loc_x=loc_x)
        viz.update()
        print(trial_str)
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
    trial_number = 3
    initial_rest = 1
    trial_duration = 2
    rest_duration = 1
    orientations = [0, 45, 90, 135]
    loc_y = 0
    loc_x = 0

    # send marker
    viz_marker_gabor(trial_number, initial_rest, trial_duration, rest_duration, 
                orientations, loc_y, loc_x)