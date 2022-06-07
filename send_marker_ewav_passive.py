"""send string-valued markers into LSL, with visualisation"""

import time
from pylsl import StreamInfo, StreamOutlet
from trial_viz import TrialVisual
import numpy as np

def viz_marker_ewav_passive(trial_number, initial_rest, trial_duration, rest_duration, block_number):
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
    time.sleep(initial_rest)
    
    while b < block_number:

        if (b % 2) == 0:
            viz.show_text("Blue square is Go stim")
            trial_str = "trialStart_cond1"
            GoColour = "B"
            NoGoColour = "R"
        else:
            viz.show_text("Red square is Go stim")
            trial_str = "trialStart_cond2"
            GoColour = "R"
            NoGoColour = "B"
        
        viz.update()
        time.sleep(initial_rest)
        viz.blank_screen()
        viz.update()

        # pseudorandomize trials
        trials = np.concatenate((np.ones(5), np.zeros(5)), axis=None)
        np.random.shuffle(trials)
        n = 0 # trial count

        while n < trial_number:
            
            trial = trials[n]
            # trial start
            
            if trial == 1:
                #Go Trial
                outlet.push_sample([trial_str+"_Go"])
                viz.draw_square(GoColour)
                viz.draw_Go_cue()
                viz.update()
                print(trial_str+"_Go")
                time.sleep(trial_duration/2)

                timeout_start = time.time()
                outlet.push_sample(["change_start"+"_Go"])
                while time.time() < timeout_start + trial_duration/2:
                    viz.draw_highlighting(GoColour)
                    viz.update()
                    time.sleep(0.2)
                    viz.draw_square(GoColour)
                    viz.update()
                    time.sleep(0.2)

            else:
                #NoGo Trial
                outlet.push_sample([trial_str+"_NoGo"])
                viz.draw_square(NoGoColour)
                viz.update()
                print(trial_str+"_NoGo")
                time.sleep(trial_duration/2)
                outlet.push_sample(["change_start"+"_NoGo"])
                time.sleep(trial_duration/2)
                
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
    trial_number = 10 #should be even
    initial_rest = 5
    trial_duration = 6
    rest_duration = 6
    block_number = 10
    # send marker
    viz_marker_ewav_passive(trial_number, initial_rest, trial_duration, rest_duration, block_number)