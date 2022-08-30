'''
markers test to unity
'''

import time
from pylsl import StreamInfo, StreamOutlet
import numpy as np

def unity_marker(random=True, wait_duration=0.005):
    # create stream info
    info = StreamInfo('ExptMarkerStream', 'MarkersToUnity', 1, 1)

    # next make an outlet
    outlet = StreamOutlet(info)

    print("Now sending markers...")
    while True:
        if random:
            mk = np.random.randint(0,2,1)
            outlet.push_sample(mk)
            time.sleep(wait_duration)

if __name__ == '__main__':
    unity_marker(random=True, wait_duration=0.01)