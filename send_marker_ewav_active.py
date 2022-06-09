"""send string-valued markers into LSL, with visualisation"""

import time
from pylsl import StreamInfo, StreamOutlet
from trial_viz import TrialVisual

def viz_marker_ewav_active(trial_number, initial_rest, trial_duration, rest_duration, block_number):
    # create stream info
    info = StreamInfo('ExptMarkerStream', 'Markers', 1, 0, 'string', 'myuidw43536')

    # next make an outlet
    outlet = StreamOutlet(info)

    # initialise visualisation
    viz = TrialVisual()

    # start
    print("Now sending markers...")
    b = 0 # block count

    # initial wait
    outlet.push_sample(['exptStart'])
    viz.blank_screen()

    viz.update()
    print("exptStart")
    viz.wait_key()
    # time.sleep(initial_rest)
    
    while b < block_number:

        if (b % 2) == 0:
            viz.show_text("E-wave block - \n visualize selection on 3")
            trial_str = "trialStart_exp"
        else:
            viz.show_text("Rest block - \n just look at the square")
            trial_str = "trialStart_rest"
        viz.update()
        time.sleep(5)
        viz.blank_screen()
        viz.update()

        n = 0 # trial count

        while n < trial_number:

            # trial start
            outlet.push_sample([trial_str])
            viz.draw_cue()
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

        b += 1
        
    viz.finish()

if __name__ == '__main__':
    # settings
    trial_number = 10
    initial_rest = 12
    trial_duration = 6
    rest_duration = 6
    block_number = 10
    # send marker
    viz_marker_ewav_active(trial_number, initial_rest, trial_duration, rest_duration, block_number)