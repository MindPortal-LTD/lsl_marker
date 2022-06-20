"""send string-valued markers into LSL, with visualisation"""

import time
from pylsl import StreamInfo, StreamOutlet
from trial_viz import TrialVisual
import numpy as np
# import keyboard


def viz_marker_ewav_active2(trial_number, initial_rest, trial_duration, rest_duration, block_number):
    # create stream info
    info = StreamInfo('ExptMarkerStream', 'Markers', 1, 0, 'string', 'myuidw43536')

    # next make an outlet
    outlet = StreamOutlet(info)

    # initialise visualisation
    viz = TrialVisual()

    # start
    print("Now sending markers...")
    b = 0  # block count

    # initial wait
    outlet.push_sample(['exptStart'])
    viz.blank_screen()

    viz.update()
    print("exptStart")
    # time.sleep(initial_rest)
    viz.wait_key()

    while b < block_number:

        # viz.show_text("If warning square is green, press the spacebar when the car appears. If the warning square is red, do nothing when the car appears.")
        viz.show_text("Green = spacebar, Red = no.")
        trial_str = "trialStart_cond1"
        GoColour = "G"
        NoGoColour = "R"

        # colours of the warning stimulus (S1)
        colourSR = "R"
        colourSG = "G"

        #     viz.show_text("Red square is Go stim")
        #     trial_str = "trialStart_cond2"
        #     GoColour = "R"
        #     NoGoColour = "B"

        viz.update()
        # time.sleep(initial_rest)
        # time.sleep(5)
        time.sleep(1)  # CHANGED

        viz.blank_screen()
        viz.update()

        # # pseudorandomize trials
        trials = np.concatenate((np.ones(5), np.zeros(5)), axis=None)
        np.random.shuffle(trials)
        n = 0  # trial count

        while n < trial_number:

            trial = trials[n]
            # trial start

            # Stimulus 1 (warning, red or green)
            if trial == 1:
                currentMarker = [trial_str + "_SR"]
                outlet.push_sample(currentMarker)
                currentSquare = colourSR

            if trial == 0:
                currentMarker = [trial_str + "_SG"]
                outlet.push_sample(currentMarker)
                currentSquare = colourSG

            viz.draw_square(currentSquare)

            viz.update()
            print(currentMarker)
            # time.sleep(trial_duration / 2)

            # non-sleep timer module + display countdown + redraw current rectangle
            startTime = time.time()  # time in seconds
            elapsedTime = time.time() - startTime
            while elapsedTime < (trial_duration / 2):
                # viz.draw_square(colourSG)
                # viz.update()
                remainingTime = (trial_duration / 2) - elapsedTime
                remainingTimeString = "{:.2f}".format(remainingTime)
                viz.show_numbers_and_square(str(remainingTimeString), currentSquare)
                viz.update()
                elapsedTime = time.time() - startTime

            # Stimulus 2 (imperative)
            currentMarker = [trial_str + "_S2"]
            outlet.push_sample(currentMarker)
            viz.draw_banana(f'./images/racecar.png')
            viz.update()

            print(currentMarker)
            time.sleep(trial_duration / 2)

            timeout_start = time.time()
            currentMarker = ["change_start" + "_Go"]
            outlet.push_sample(currentMarker)
            print(currentMarker)
            time.sleep(rest_duration)

            # next trial
            n += 1

        b += 1

        viz.finish()


if __name__ == '__main__':
    # settings (Original)
    trial_number = 10  # should be even
    initial_rest = 12
    trial_duration = 6
    rest_duration = 6
    block_number = 10

    # # settings (Debug)
    # trial_number = 4  # should be even
    # initial_rest = 2
    # trial_duration = 2
    # rest_duration = 2
    # block_number = 10
    # # send marker
    viz_marker_ewav_active2(trial_number, initial_rest, trial_duration, rest_duration, block_number)
