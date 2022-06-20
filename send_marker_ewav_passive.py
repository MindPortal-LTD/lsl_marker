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
    # time.sleep(initial_rest)
    viz.wait_key()
    
    while b < block_number:


        viz.show_text("Blue square is Go stim")
        trial_str = "trialStart_cond1"
        GoColour = "G"
        NoGoColour = "R"

        # colours of the warning stimulus (S1) and then imperative stimulus (S2)
        colourS1 = "R"
        colourS2 = "G"

        #     viz.show_text("Red square is Go stim")
        #     trial_str = "trialStart_cond2"
        #     GoColour = "R"
        #     NoGoColour = "B"
        
        viz.update()
        # time.sleep(initial_rest)
        # time.sleep(5)
        time.sleep(1) # CHANGED
        viz.blank_screen()
        viz.update()

        # # pseudorandomize trials
        # trials = np.concatenate((np.ones(5), np.zeros(5)), axis=None)
        # np.random.shuffle(trials)
        # n = 0 # trial count

        # single trial type
        trials = np.ones(10)
        # trials = np.zeros(10)
        n = 0  # trial count

        while n < trial_number:
            
            trial = trials[n]
            # trial start
            
            if trial == 1:
                # Stimulus 1 (warning)
                currentMarker = [trial_str+"_S1"]
                outlet.push_sample(currentMarker)
                viz.draw_square(colourS1)
                # viz.draw_Go_cue()
                viz.update()
                print(currentMarker)
                time.sleep(trial_duration/2)

                # Stimulus 2 (imperative)
                currentMarker = [trial_str + "_S2"]
                outlet.push_sample(currentMarker)
                viz.draw_square(colourS2)
                # viz.draw_Go_cue()
                viz.update()
                print(currentMarker)
                time.sleep(trial_duration/2)

                timeout_start = time.time()
                currentMarker = ["change_start"+"_Go"]
                outlet.push_sample(currentMarker)
                print(currentMarker)

                # while time.time() < timeout_start + trial_duration/2:
                #     viz.draw_highlighting(GoColour)
                #     viz.update()
                #     time.sleep(0.2)
                #     viz.draw_square(GoColour)
                #     viz.update()
                #     time.sleep(0.2)

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
    # settings (Original)
    trial_number = 10 #should be even
    initial_rest = 12
    trial_duration = 6
    rest_duration = 6
    block_number = 10

    # settings (Debug)
    trial_number = 4  # should be even
    initial_rest = 2
    trial_duration = 2
    rest_duration = 2
    block_number = 10
    # send marker
    viz_marker_ewav_passive(trial_number, initial_rest, trial_duration, rest_duration, block_number)