import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--calibrate", help="set the calibration mode of the esc")
args = parser.parse_args()

if args.calibrate == "calibrate" :
    print("calibrating...")

elif args.calibrate == "phases" :
    print("phasing")

else :
    print("driving")
